from src.prompts import build_report_prompt
from src.llm import generate_response


def main():

    with open("transcripts/nvidia.txt", "r", encoding="utf-8") as file:
        transcript = file.read()

    prompt = build_report_prompt(transcript)

    report = generate_response(prompt)

    print(report)


if __name__ == "__main__":
    main()