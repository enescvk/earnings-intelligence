from src.prompts import build_report_prompt
from src.llm import generate_response
from src.report_writer import save_report



def main():

    with open("transcripts/nvidia.txt", "r", encoding="utf-8") as file:
        transcript = file.read()

    prompt = build_report_prompt(transcript)

    report = generate_response(prompt)

    save_report(report, "NVDA_Q1_2027.md")


if __name__ == "__main__":
    main()