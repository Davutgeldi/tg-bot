# 🛒 tg-bot

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![aiogram](https://img.shields.io/badge/aiogram-3.x-green.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()

Telegram bot for submitting purchase requests for online services.

---

## 📌 Description

tg-bot is a Telegram bot that allows users to submit requests for purchasing online services (subscriptions, digital products, accounts, etc.).

After receiving a request, the admin reviews it and completes the purchase manually.

---

## ✨ Features

- Submit purchase requests  
- Forward requests to admin  
- Simple and fast workflow  
- Lightweight and easy to use  

---

## 🛠 Tech Stack

- Python  
- aiogram  
- uv  
- Telegram Bot API  

---

## 📂 Project Structure

```
src/              Bot source code  
pyproject.toml    Project config  
uv.lock           Dependencies lock  
README.md         Documentation  
```

---

## 🚀 Setup & Run

### 1) Clone repository

```
git clone https://github.com/Davutgeldi/tg-bot.git
cd tg-bot
```

---

### 2) Install dependencies

```
uv sync
```

---

### 3) Configure environment

Create `.env` file:

```
BOT_TOKEN=your_bot_token_here
ADMIN_ID=your_telegram_id
```

---

### 4) Run bot

```
python src/main.py
```

---

## 🔐 Security

- Do not share your bot token  
- Use `.env` for secrets  
- Add `.env` to `.gitignore`  
- Regenerate token if leaked  

---

## 📄 License

MIT

---

## 👤 Author

Developed by Davutgeldi
