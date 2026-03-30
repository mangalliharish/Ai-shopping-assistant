from huggingface_hub import InferenceClient
import os

# Initialize client using API key from environment
client = InferenceClient(
    api_key=os.getenv("HF_API_KEY")
)

def generate_response(prompt: str) -> str:
    try:
        response = client.text_generation(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            prompt=prompt,
            max_new_tokens=200,
            temperature=0.7
        )
        return response.strip()
    except Exception as e:
        return f"Error: {str(e)}"