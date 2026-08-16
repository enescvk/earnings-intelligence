from pathlib import Path

from src.prompts import ReportPrompt
from src.metadata import extract_metadata
from src.llm import generate_response
from src.report_writer import save_report


def main():

    transcript_path = Path("transcripts/Microsoft.txt")

    with open(transcript_path, "r", encoding="utf-8") as file:
        transcript = file.read()

    transcript_name = transcript_path.stem

    metadata = extract_metadata(transcript, transcript_name)

    print(metadata)

    report_prompt = ReportPrompt.build(transcript)

    report = generate_response(report_prompt)

    save_report(report, metadata.filename)


if __name__ == "__main__":
    main()