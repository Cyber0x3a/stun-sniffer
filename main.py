import psutil
import subprocess
import re
import threading
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem, Label, RichLog
from textual.reactive import reactive
from textual import events
from rich.text import Text
from rich.panel import Panel
from rich.console import Group
from rich.rule import Rule


TARGET_MSG_TYPE = "Binding Request"
def get_interfaces():
    interfaces = []
    addrs = psutil.net_if_addrs()
    for idx, (name, addr_list) in enumerate(addrs.items(), start=1):
        ipv4 = None
        for addr in addr_list:
            if addr.family == 2:  # IPv4
                ipv4 = addr.address
                break
        if ipv4:
            interfaces.append({"id": idx,"device": name,"name": name,"ip": ipv4})
    return interfaces


class CaptureIP(App):
    CSS = """
    Screen {
        align: center middle;
    }

    #interface_list {
        height: 10;
        width: 80;
        border: round white;
    }

    #output {
        height: 20;
        width: 80;
        border: round yellow;
        overflow: auto;
        margin-top: 1;
    }
    """

    selected_interface = reactive(None)
    tshark_process = None

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Label("Select a network interface to capture STUN packets (Press 'q' to quit):", id="label")
        self.list_view = ListView(id="interface_list")
        yield self.list_view


        self.output_log = RichLog(id="output", wrap=True, markup=True)
        yield self.output_log

        yield Footer()

    def on_mount(self) -> None:
        try:
            interfaces = get_interfaces()
            if not interfaces:
                self.exit(message="No interfaces with IPv4 addresses found. Make sure tshark has permissions (run as admin/root?).")

            for iface in interfaces:

                item_text = f"{iface['id']}: {iface['name']} ({iface['ip']})"

                composite_name = f"{iface['device']}|{iface['ip']}"
                self.list_view.append(ListItem(Label(item_text), name=composite_name))
        except RuntimeError as e:
            self.exit(message=str(e))

    async def on_list_view_selected(self, event: ListView.Selected) -> None:
        if self.selected_interface:
            return

        composite_name = event.item.name
        try:
            device, ip = composite_name.split("|")
        except (ValueError, AttributeError):
            self.output_log.write(Text(f"Error parsing interface data: {composite_name}", style="red"))
            return

        self.selected_interface = device

        self.list_view.display = False
        self.query_one("#label").update("Starting capture... Press 'q' to quit.")

        info_panel = Panel(Group(Text("Interface Selected", style="bold bright_green"), Text(f"Device: {device}", style="white"), Text(f"IP Address: {ip}", style="bright_white bold"),),
        border_style="bright_green",title=" Network Interface ",title_align="left",padding=(1, 2),expand=False,)
        self.output_log.write(info_panel)

        # --- Listening section ---
        waiting_content = Group(
            Text("Listening for STUN packets...", style="bold cyan"),
            Text(f"Target message type: {TARGET_MSG_TYPE}", style="cyan"),
            Text(f"Destination IP: {ip}", style="bright_white bold"),
        )
        self.output_log.write(waiting_content)
        self.output_log.write(Rule(style="dim cyan"))

        self.capture_stun(device, ip)

    def capture_stun(self, interface, interface_ip):
        def run_capture():
            try:
                display_filter = f"stun and ip.dst == {interface_ip}"

                self.tshark_process = subprocess.Popen(
                    ["tshark", "-i", interface, "-Y", display_filter, "-l"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding='utf-8'
                )

                ip_regex = re.compile(r'\b\d{1,3}(?:\.\d{1,3}){3}\b')

                for line in self.tshark_process.stdout:
                    if TARGET_MSG_TYPE in line:
                        ips = ip_regex.findall(line)
                        if len(ips) >= 2:
                            src_ip = ips[0]
                            dest_ip = ips[1]

                            title = Text("Target STUN Packet Found", style="bold bright_green", justify="center")
                            src_line = Text(f"Target IP: ", style="bold white") + Text(src_ip, style="bold red")
                            dest_line = Text(f"Your IP: ", style="bold white") + Text(dest_ip, style="bold cyan")
                            note = Text("Packet captured successfully.", style="dim yellow")

                            packet_panel = Panel(
                                Group(title, Text(""), src_line, dest_line, Text(""), note),
                                border_style="bright_green",
                                title=" STUN Capture ",
                                title_align="left",
                                padding=(1, 2),
                                expand=False,
                                subtitle="✨ powered by tshark ✨",
                                subtitle_align="right"
                            )

                            self.call_from_thread(self.output_log.write, packet_panel)
                            break
                        else:
                            fallback_panel = Panel(
                                Text(line.strip(), style="green"),
                                border_style="yellow",
                                title="⚠️  Unknown STUN Data",
                                padding=(1, 2)
                            )
                            self.call_from_thread(self.output_log.write, fallback_panel)
                            break

            except Exception as e:
                error_panel = Panel(
                    Text(f"Capture Error: {e}", style="bold red"),
                    border_style="red",
                    title="Error",
                    padding=(1, 2)
                )
                self.call_from_thread(self.output_log.write, error_panel)
            finally:
                if self.tshark_process:
                    self.tshark_process.terminate()
                    self.tshark_process.wait()
                    self.call_from_thread(
                        self.output_log.write,
                        Text("\nCapture stopped.", style="yellow")
                    )

        threading.Thread(target=run_capture, daemon=True).start()

    async def on_key(self, event: events.Key) -> None:
        if event.key == "q":
            if self.tshark_process:
                self.tshark_process.terminate()
            self.exit()

if __name__ == "__main__":
    CaptureIP().run()