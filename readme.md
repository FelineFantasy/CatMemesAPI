# 🐱 CatMemeAPI

Random cat memes API. 1000 memes, zero dogs. Built with FastAPI.

## 📝 Description

CatMemeAPI returns random cat memes with metadata (width, height). All memes are curated and sorted.

### Features

- 🐱 1000 cat memes
- 🖼️ Returns image dimensions (width, height)
- 📦 Single endpoint for random memes
- ⚡ FastAPI + PIL

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

#### 👤 Author

- **FelineFantasy**
- **License**: MIT
