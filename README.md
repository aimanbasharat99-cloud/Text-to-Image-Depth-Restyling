# 🔍 Text-to-Image Retrieval System

> Search through images using natural language — type "a red car at sunset" and get the most visually matching images back instantly.

Built as a **Software Integration project during my M2 (MSc) in International Biometrics and Intelligent Vision at UPEC, Paris.**

---

## 💡 What It Does

This system lets you search a collection of images using plain text queries. You type something like *"a dog running on grass"* and it finds the most visually similar images from your dataset — no labels or tags needed.

Under the hood it uses **OpenAI's CLIP model** to turn both text and images into vectors, stores them in a **ChromaDB vector database**, and finds the closest matches using similarity search.

---

## 🏗️ Architecture

```
User types a query
       ↓
CLIP model encodes the text → vector
       ↓
ChromaDB finds closest image vectors
       ↓
Top-K matching images returned with similarity scores
       ↓
Results shown in Web UI or saved to /results folder
```

---

## ✨ Features

- 🔎 **Natural language image search** — no need to tag or label images
- ⚡ **Fast inference** — images are pre-embedded, search is instant
- 🌐 **Web UI** — simple browser interface to search and view results
- 🔌 **REST API** — FastAPI backend with `/search` and `/stats` endpoints
- ⚙️ **Configurable** — swap CLIP model variant, batch size, top-K in `config.py`
- 💾 **Persistent database** — ChromaDB stores embeddings so you don't re-encode every time

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Embeddings | OpenAI CLIP (ViT-B/32) |
| Vector DB | ChromaDB |
| API | FastAPI + Pydantic |
| Frontend | HTML / JavaScript |
| Image Processing | Pillow |
| Deep Learning | PyTorch, torchvision |

---

## 🚀 How to Run

**1. Clone the repo**
```bash
git clone https://github.com/aimanbasharat99-cloud/Text-to-Image-Depth-Restyling.git
cd Text-to-Image-Depth-Restyling
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your images**
```
Put your images inside the /dataset folder
Supported formats: .jpg .jpeg .png .bmp .webp
```

**4. Embed your images (run once)**
```bash
python embed_images.py
```

**5. Search!**

Option A — interactive terminal mode:
```bash
python main.py
```

Option B — run the API server:
```bash
uvicorn api:app --reload
```
Then open `index.html` in your browser.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/search` | Search images by text query |
| GET | `/stats` | Get database stats |

**Example request:**
```json
POST /search
{
  "query": "a cat sitting on a chair",
  "top_k": 5
}
```

---

## ⚙️ Configuration

Edit `config.py` to customise:

```python
MODEL_NAME = "ViT-B/32"   # swap to "ViT-L/14" for better quality
TOP_K = 5                  # number of results to return
BATCH_SIZE = 32            # reduce if you run out of memory
```

---

## 👤 Author

**Aiman Basharat Abbasi**
MSc — International Biometrics & Intelligent Vision, UPEC Paris
[LinkedIn](https://linkedin.com/in/aiman-basharat-abbasi-892137219) · [GitHub](https://github.com/aimanbasharat99-cloud)
