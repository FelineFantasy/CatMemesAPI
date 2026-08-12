# 🐱 CatMemesAPI

Random cat memes API. 1000 memes, zero dogs. Built with FastAPI.

**🔗 Live API:** https://catmemesapi.onrender.com

**📖 Interactive Docs:** https://catmemesapi.onrender.com/docs

---

## ⚠️ WARNING ⚠️

**NEVER open the `memes/` folder in your browser or file explorer!**

- Folder contains **1000+ JPG files** (85 MB total)
- Your browser **will crash** or freeze for minutes
- Your file explorer might stop responding
- **Only access memes through the API endpoints**

✅ **Correct way:** Use `/meme/search?limit=5` or `/meme/{meme_id}`  
❌ **Wrong way:** Clicking on `memes/` folder in GitHub web interface

*Your RAM will thank you.*

## 📝 Description

CatMemeAPI returns random cat memes with metadata (width, height). All memes are curated and sorted.

### Features

- 🐱 1000 cat memes
- 🖼️ Returns image dimensions (width, height)
- 📦 Single endpoint for random memes
- ⚡ FastAPI + PIL
- ⚠️ **Safe API access only** (no browser folder browsing!)

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

## 🎮 Usage

Start the server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### API Endpoints

| Endpoint                       | Description        |
|:------------------------------ |:------------------ |
| **GET** `/`                    | API info           |
| **GET** `/meme/search?limit=5` | Get 5 random memes |
| **GET** `/meme/{meme_id}`      | Get meme by ID     |

### Example response (`/meme/search?limit=2`)

```json
[
  {
    "id": 42,
    "url": "http://localhost:8000/meme/42",
    "width": 640,
    "height": 480
  },
  {
    "id": 777,
    "url": "http://localhost:8000/meme/777",
    "width": 800,
    "height": 600
  }
]
```

## 📦 Requirements

- Python 3.x
- FastAPI
- uvicorn
- Pillow

## 📁 Project Files

```text
CatMemesAPI/
├── .github/
│   └── FUNDING.yml
├── memes/
│   └── (1000+ JPG files)
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 💖 Support the Project

If you enjoy **CatMemesAPI** and want to help keep the project alive, you can support me here:

[![DonationAlerts](https://img.shields.io/badge/DonationAlerts-Support-blue.svg)](https://www.donationalerts.com/r/FelineFantasy)

Your support helps me:
- 🐱 Keep developing new features
- 🛠️ Fix bugs and improve the game
- ☕ Stay awake while coding at 4 AM

Every little bit is appreciated! ❤️

#### 👤 Author

- **FelineFantasy**
- **License**: MIT
