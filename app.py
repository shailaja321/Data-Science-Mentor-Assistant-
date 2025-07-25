import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load TinyLlama model and tokenizer
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32)

# Create text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Define assistant behavior
def mentor_response(user_input):
    prompt = (
        f"User: {user_input}\nAssistant:"
    )
    response = generator(prompt, max_new_tokens=256, do_sample=True, temperature=0.7)
    return response[0]["generated_text"]

# Gradio interface
gr.Interface(
    fn=mentor_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your query", label="Your Query"),
    outputs=gr.Textbox(label="Assistant"),
    title="Data Science Mentor Assistant",
    description="An AI assistant that explains data science concepts like pandas, NumPy, machine learning, and more."
).launch()