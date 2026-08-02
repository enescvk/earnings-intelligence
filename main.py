from src.prompts import ReportPrompt
from src.metadata import extract_metadata
from src.llm import generate_response
from src.report_writer import save_report


def main():

    with open("transcripts/Apple.txt", "r", encoding="utf-8") as file:
        transcript = file.read()

    metadata = extract_metadata(transcript)

    print(metadata)

    report_prompt = ReportPrompt.build(transcript)

    report = generate_response(report_prompt)

    save_report(report, metadata.filename)


if __name__ == "__main__":
    main()