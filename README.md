# 🩺 AI-Powered Diabetes Question Answering System using FLAN-T5

## 📌 Overview

This project is an AI-based question answering system designed to provide responses to diabetes-related queries. It uses a fine-tuned FLAN-T5 transformer model to generate answers based on user input.

The system is built with:

* **Frontend:** React (Vite + Tailwind CSS)
* **Backend:** FastAPI
* **Model:** FLAN-T5 (Hugging Face Transformers)

---

## 🚀 Features

* Chat-based interface for user interaction
* Real-time response generation
* Domain-specific answers (diabetes-related)
* FastAPI backend for efficient API handling
* Clean and simple UI

---

## 🏗️ Project Structure

```
diabetes-chat-ui/
│
├── diabetes-backend/
│   ├── main.py
│   ├── requirements.txt
│   └── model/   (not included in repo)
│
├── diabetes-frontend/
│   ├── src/
│   ├── package.json
│
└── README.md
```

---

## ⚙️ Prerequisites

Make sure you have installed:

* Python 3.8+
* Node.js (v16 or above)
* npm or yarn

---

## 🔧 Backend Setup (FastAPI)

### Step 1: Navigate to backend

```
cd diabetes-backend
```

### Step 2: Create virtual environment

```
python -m venv venv
```

### Step 3: Activate environment

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

### Step 4: Install dependencies

```
pip install -r requirements.txt
```

### Step 5: Add model

Place your trained FLAN-T5 model inside:

```
diabetes-backend/model/
```

⚠️ Model files are not included due to size.

### Step 6: Run backend server

```
uvicorn main:app --reload
```

👉 Backend runs at:

```
http://127.0.0.1:8000
```

---

## 💻 Frontend Setup (React)

### Step 1: Navigate to frontend

```
cd diabetes-frontend
```

### Step 2: Install dependencies

```
npm install
```

### Step 3: Run frontend

```
npm run dev
```

👉 Frontend runs at:

```
http://localhost:5173
```

---

## 📦 Download Model

Due to large file size, the trained FLAN-T5 model is not included in this repository.

👉 Download the model from:
https://drive.google.com/drive/folders/1T3iQPiiw238GCHTATlYoYNebgn4iFADn?usp=drive_link

After downloading, place the folder inside:

```bash
diabetes-backend/model/
```

Make sure the structure looks like:

```bash
model/
├── config.json
├── pytorch_model.bin
├── tokenizer_config.json
├── special_tokens_map.json
```


## 🔗 API Endpoint

**POST /chat**

Request:

```json
{
  "question": "What is diabetes?"
}
```

Response:

```json
{
  "answer": "Diabetes is a condition where blood sugar levels are high..."
}
```

---

## 📷 Screenshots

![alt text](<Screenshot 2026-04-04 132942.png>)

---

## ⚠️ Limitations

* Responses may not always be medically accurate
* Model performance depends on training data
* Not a replacement for professional medical advice

---

## 🔮 Future Improvements

* Improve model accuracy with better dataset
* Add voice input support
* Deploy using cloud (AWS / Render)
* Add user authentication

---

## 👨‍💻 Authors

* Your Team Names Here

---

## 📄 License

This project is for academic purposes only.
