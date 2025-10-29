<div align="center">
<br/>
<div style="background: linear-gradient(145deg, #111, #222); border-radius: 20px; padding: 25px 50px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5); border: 1px solid #333;">
  <h1 style="font-family: 'Segoe UI', 'Helvetica Neue', sans-serif; font-weight: 700; font-size: 2.8em; color: #00f2ff; text-shadow: 0 0 10px #00f2ff, 0 0 25px rgba(0, 242, 255, 0.5);">
    STUN Packet Sniffer 🌐⚡
  </h1>
  <p style="font-size: 1.2em; color: #aab; max-width: 800px; margin-top: -10px;">
    A terminal-based application to capture & analyze STUN packets in real-time.
  </p>
</div>

<br/>

<div align="center" style="padding: 15px 0;">
    <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white&logoWidth=20" alt="Python Version">
    <img src="https://img.shields.io/badge/Made%20with-Textual-007ACC?style=for-the-badge&logo=python&logoColor=white&logoWidth=20" alt="Made with Textual">
    <img src="https://img.shields.io/github/license/cyber0x3a/stun-sniffer?style=for-the-badge&color=green" alt="License">
    <img src="https://img.shields.io/github/stars/cyber0x3a/stun-sniffer?style=for-the-badge&color=blue&label=Stars" alt="Stars">
</div>

<div align="center" style="display: flex; justify-content: center; gap: 10px; margin-top: 10px;">
  <a href="https://github.com/cyber0x3a/stun-sniffer" style="text-decoration: none;">
    <span style="background-color: #282c34; color: #00f2ff; padding: 10px 20px; border-radius: 8px; font-weight: bold; border: 1px solid #00f2ff;">Browse Code</span>
  </a>
  <a href="https://github.com/cyber0x3a/stun-sniffer/issues" style="text-decoration: none;">
    <span style="background-color: #282c34; color: #aaa; padding: 10px 20px; border-radius: 8px; font-weight: bold; border: 1px solid #555;">Report a Bug</span>
  </a>
</div>

</div>

---

## 🚀 **About The Project**

<div align="center" style="margin-top: 20px;">
  <div style="border-radius: 15px; padding: 8px; border: 1px solid #444; background: #111; box-shadow: 0 0 25px rgba(0, 242, 255, 0.15);">
    <img src="https://raw.githubusercontent.com/goruha/goruha/main/Panda.gif" alt="Demo GIF" style="border-radius: 10px; width: 100%; max-width: 750px;">
  </div>
  <p style="color: #889; font-style: italic; margin-top: 10px;">(Application Demo)</p>
</div>

### ✨ **Key Features**

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 20px;">
    <div style="background: #1c1c21; border-radius: 10px; padding: 20px; border: 1px solid #333;">
        <h4 style="color: #00f2ff; margin-top: 0;">🌐 Real-Time Capture</h4>
        <p style="color: #aab; font-size: 0.9em;">Instantly sniffs and displays STUN packets from your network interface.</p>
    </div>
    <div style="background: #1c1c21; border-radius: 10px; padding: 20px; border: 1px solid #333;">
        <h4 style="color: #00f2ff; margin-top: 0;">🖥️ Interactive TUI</h4>
        <p style="color: #aab; font-size: 0.9em;">A clean and intuitive Textual User Interface for seamless operation.</p>
    </div>
    <div style="background: #1c1c21; border-radius: 10px; padding: 20px; border: 1px solid #333;">
        <h4 style="color: #00f2ff; margin-top: 0;">🎨 Beautiful Output</h4>
        <p style="color: #aab; font-size: 0.9em;">Leverages Rich to provide beautifully formatted, colorized output.</p>
    </div>
</div>

---

## 🛠️ **Tech Stack**

This project is built with a modern, asynchronous Python stack.

<div align="center" style="margin-top: 20px; padding: 20px; background: #1c1c21; border-radius: 10px; border: 1px solid #333;">
  <div style="display: flex; justify-content: center; gap: 25px; flex-wrap: wrap;">
    <img src="https://skillicons.dev/icons?i=python&theme=dark" alt="Python" title="Python" />
    <img src="https://skillicons.dev/icons?i=powershell&theme=dark" alt="PowerShell/Bash" title="Shell" />
    <img src="https://skillicons.dev/icons?i=git&theme=dark" alt="Git" title="Git" />
    <img src="https://skillicons.dev/icons?i=github&theme=dark" alt="GitHub" title="GitHub" />
  </div>
  <p align="center" style="font-size: 0.9em; color: #aaa; margin-top: 20px;">
    <i>Core Libraries: Textual, Rich, psutil</i>
  </p>
</div>

---

## ⚙️ **Getting Started**

<details>
<summary style="font-size: 1.2em; font-weight: bold; color: #2c313a; cursor: pointer;">
  Click here for installation instructions
</summary>

<div style="margin-top: 15px; padding: 20px; background: #1c1c21; border-radius: 10px; border: 1px solid #333; color: #d1d5db; font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;">

<h3 style="color: #00f2ff; border-bottom: 2px solid #333; padding-bottom: 5px;"><strong>Prerequisites</strong></h3>

> ⚠️ **Important:** <code style="background-color: #2c313a; color: #e5c07b; padding: 3px 6px; border-radius: 4px;">tshark</code> requires administrative/root privileges for packet capturing.

- **<a href="https://www.python.org/downloads/" style="color: #61afef; text-decoration: none;">Python 3.9+</a>**
- **<a href="https://www.wireshark.org/download/" style="color: #61afef; text-decoration: none;">tshark (Wireshark's CLI)</a>**
- **<a href="https://git-scm.com/downloads" style="color: #61afef; text-decoration: none;">Git</a>**

<h3 style="color: #00f2ff; border-bottom: 2px solid #333; padding-bottom: 5px; margin-top: 25px;"><strong>Installation Steps</strong></h3>

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/cyber0x3a/stun-sniffer.git
    cd stun-sniffer
    ```

2.  **Set Up a Virtual Environment (Recommended)**

    ```bash
    # Create & activate the environment
    python -m venv .venv && source .venv/bin/activate
    ```

    _On Windows, use <code style="background-color: #2c313a; color: #e5c07b; padding: 3px 6px; border-radius: 4px;">.venv\Scripts\activate</code>_

3.  **Install Dependencies**

    ```bash
    python -m pip install --upgrade pip
    python -m pip install textual rich psutil
    ```
</div>
</details>

---

## 🧠 **Usage**

Running the application is straightforward.

1.  **Execute the main script from your terminal:**

    ```bash
    python capture_stun.py
    ```

2.  **Inside the TUI:**
    - Use `↑`/`↓` keys to navigate the network interface list.
    - Press `Enter` to select an interface and start sniffing.
    - Press `q` or `Ctrl+C` to exit.

### **Example Terminal Output**

<div style="margin: 20px auto; padding: 20px; border-radius: 10px; background-color: #1a1a1d; border: 1px solid #333; max-width: 700px; font-family: 'Consolas', 'Courier New', monospace;">
    <div style="color: #00f2ff; margin-bottom: 10px;">🌐 Interface Selected: Wi-Fi (192.168.1.10)</div>
    <div style="color: #aaa; margin-bottom: 15px;">Listening for STUN packets...</div>
    <div style="padding: 15px; border-radius: 5px; background-color: #25252a; border-left: 3px solid #00f2ff;">
        <div style="color: #fafafa; font-weight: bold;">✨ Target STUN Packet Found ✨</div>
        <div style="color: #00f2ff; margin-top: 10px;"> > Your IP:    <span style="color: #f0f0f0;">192.168.1.10</span></div>
        <div style="color: #00f2ff;"> > Target IP:  <span style="color: #f0f0f0;">52.14.89.23</span></div>
    </div>
</div>

---

## 💡 **Use Case**

This tool is useful for network diagnostics and understanding STUN-based connections, such as those used in:

- **VoIP & Video Calls:** Capture the IP addresses of clients during WhatsApp (Tested) or similar calls.  
- **Testing NAT Traversal:** Analyze how your NAT handles STUN requests.  

> ⚠️ **Note:** For STUN-based IP discovery to work, the WhatsApp user must be an active contact who has previously exchanged messages, voice, or video calls with you. Simply being in a call is not enough; otherwise, WhatsApp may route traffic through its servers to protect the client’s public IP. Always respect privacy and local laws when analyzing network traffic.

---

## 🗺️ **Roadmap**

See the [open issues](https://github.com/cyber0x3a/stun-sniffer/issues) for a full list of proposed features and known issues.

- [ ] **TUI Enhancements:** Add real-time counters and colored banners.
- [ ] **Logging:** Implement an option to log captured packets to a file.
- [ ] **Cross-Platform:** Improve compatibility and testing for Linux & macOS.
- [ ] **Error Handling:** Add robust checks for `tshark` permissions.
- [ ] **Packet Details:** Create a detailed view for decoded packet information.

---

<div align="center">
  <h3 style="color: #ddd;">✨ Built with passion for cyber security enthusiasts ✨</h3>
</div>