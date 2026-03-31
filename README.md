# 🎙️ Discord Voice Joiner

A high-performance, asynchronous tool designed to keep Discord tokens connected to a voice channel 24/7. Perfect for VDS/VPS usage to maintain a constant presence in a server.

---

## 🌟 Features

- **🚀 Multiple Token Support**: Connect dozens of accounts simultaneously.
- **🔄 Auto-Reconnect**: Automatically reconnects if a connection is dropped or a token is kicked.
- **🛡️ Rate-Limit Protection**: Built-in delays and connection capping to avoid Discord rate limits.
- **⚡ Async/Websocket**: Uses asynchronous programming for maximum efficiency and low resource usage.
- **🎨 Premium UI**: Stylish CLI interface with color-coded logs.

---

## 🛠️ Installation

1. **Python**: Ensure you have [Python 3.8+](https://www.python.org/downloads/) installed.
2. **Setup**: Run `install.bat` to install the required dependencies:
   ```bash
   install.bat
   ```

---

## 🚀 How to Use

1. **Tokens**: Add your Discord user tokens to `tokens.txt` (one per line).
2. **Start**: Run `start.bat`.
3. **Configure**: 
   - Select option `1` to join a voice channel.
   - Enter the **Server (Guild) ID**.
   - Enter the **Channel ID**.
4. **Sit back**: The tool will now keep your tokens in the channel.

---

## ⚠️ Disclaimer

This tool is for educational purposes only. Using "self-bots" or automated user accounts is against the [Discord Terms of Service](https://discord.com/terms). Use this tool at your own risk. The developer is not responsible for any account bans.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
