# llm_api.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI()

# Load your fine-tuned LLM model and tokenizer from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("llmModeluser/therapy_trained_model")
model = AutoModelForCausalLM.from_pretrained("llmModeluser/therapy_trained_model")

class Input(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(input_data: Input):
    prompt = input_data.prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=300, do_sample=True, top_k=50, top_p=0.95, num_return_sequences=1)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"response": generated_text}