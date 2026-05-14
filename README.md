<p align="center">
  <img src="assets/banner.png" alt="Epic Free Games Claimer Banner" width="100%">
</p>

<h1 align="center">Epic Free Games Claimer 🎮</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Playwright-Enabled-green?style=for-the-badge&logo=playwright" alt="Playwright">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status">
</p>

---

## 📖 Overview

The **Epic Free Games Claimer** is a semi-automated automation tool designed to help you claim free games from the Epic Games Store safely and efficiently. Unlike fully automated scripts that require your credentials, this tool prioritizes **account security** by requiring a manual login session.

> [!TIP]
> This script uses **Playwright** to handle browser interactions, ensuring a smooth and human-like claiming process.

---

## ✨ Key Features

- 🔐 **Secure Login:** No credentials are ever stored. You login manually through a standard browser window.
- 🎯 **Smart Detection:** Automatically identifies all available free games on the store.
- ⏭️ **Library Check:** Detects games already in your library and skips them to save time.
- 🛡️ **Safety Limits:** Includes built-in limits and delays to mimic human behavior and avoid account flags.
- 🛠️ **Interactive Choice:** Prompts you before claiming each game, giving you full control.

---

## 🛠 Tech Stack

- **Language:** Python 3.9+
- **Automation:** [Playwright](https://playwright.dev/)
- **Browser:** Chromium (managed by Playwright)

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.9+](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/) or Chromium installed

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Rajmund09/epic-free-games-claimer.git
   cd epic-free-games-claimer
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright Browsers:**
   ```bash
   playwright install chromium
   ```

---

## ▶️ Usage Guide

Run the script using the following command:

```bash
python epic_free_games.py
```

### The Workflow:
1. **Automation Starts:** A Chromium window will open at the Epic Games Store login page.
2. **Manual Login:** Login to your account as you normally would.
3. **Continue:** Return to your terminal and press **ENTER** once you are logged in.
4. **Claiming:** The script will find free games. For each game, it will ask if you want to claim it. Type `y` to confirm.
5. **Success:** The script will handle the checkout process and confirm when the game is added to your library.

---

## ⚠️ Safety & Disclaimer

- **Educational Purpose:** This project is for educational purposes only.
- **Privacy:** This script **does not** collect, store, or transmit your Epic Games credentials.
- **Use at Your Own Risk:** While designed with safety in mind, use this tool responsibly. We are not responsible for any actions taken by Epic Games against your account.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information (if applicable).

---

## 👤 Author

**Rajmund**
- GitHub: [@Rajmund09](https://github.com/Rajmund09)
- Built with ❤️ for the gaming community.