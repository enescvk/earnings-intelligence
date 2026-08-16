import ollama


def generate_response(prompt: str) -> str:
    """
    Sends a prompt to Ollama and returns the model's response.
    """

    response = ollama.chat(
        model="gemma4:12b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        think = False,
        options={
            "temperature": 0,
        }
    )

    content = response["message"]["content"]

    print("\nOLLAMA RESPONSE DEBUG:")
    print("DONE:", response.get("done"))
    print("DONE REASON:", response.get("done_reason"))
    print("CONTENT LENGTH:", len(content))
    print("CONTENT REPR:", repr(content))

    return content