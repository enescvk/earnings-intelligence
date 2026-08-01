from pathlib import Path


def save_report(report: str, filename: str) -> None:
    """
    Saves the generated report as a Markdown file.
    """

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    output_path = reports_dir / filename

    output_path.write_text(report, encoding="utf-8")

    print(f"Report saved to {output_path}")