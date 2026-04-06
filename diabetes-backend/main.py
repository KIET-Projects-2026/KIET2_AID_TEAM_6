from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

# ----------------------------
# APP
# ----------------------------
app = FastAPI()

# ----------------------------
# CORS (THIS FIXES YOUR ERROR)
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React
    allow_credentials=True,
    allow_methods=["*"],  # allow OPTIONS, POST
    allow_headers=["*"],
)

# ----------------------------
# MODEL LOAD
# ----------------------------
MODEL_PATH = "./model"  # adjust if needed

tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
model.eval()

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# ----------------------------
# REQUEST SCHEMA
# ----------------------------
class ChatRequest(BaseModel):
    question: str

# ----------------------------
# ROUTES
# ----------------------------
@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
    prompt = f"Instruction: {req.question}\nAnswer:"

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).to(device)

    # Generate a longer, complete answer. Use max_new_tokens to control output length
    # (max_length mixes input+output in some HF versions and can cause truncation).
    outputs = model.generate(
        **inputs,
        max_new_tokens=512,
        num_beams=4,
        no_repeat_ngram_size=3,
        repetition_penalty=1.5,
        early_stopping=False,
        do_sample=False,
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"answer": answer}
