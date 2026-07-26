import ollama


def generate_response(prompt: str) -> str:
    """
    Sends a prompt to Ollama and returns the model's response.
    """

    response = ollama.chat(
        model="gemma4:12b",   # Change this if you're using another model
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]