from dataclasses import dataclass
from typing import Optional
import json
import re

from src.prompts import MetadataPrompt
from src.llm import generate_response


@dataclass
class ReportMetadata:
    transcript_name: str
    company: str
    ticker: Optional[str]
    quarter: str
    fiscal_year: str
    call_date: Optional[str]
    ceo: Optional[str]
    cfo: Optional[str]

    @property
    def filename(self) -> str:
        return f"{self.transcript_name}_{self.quarter}_{self.fiscal_year}.md"


def normalize_quarter(quarter: Optional[str]) -> Optional[str]:
    """
    Normalize different quarter representations to Q1-Q4.
    """

    if not quarter:
        return None

    value = str(quarter).strip().lower()

    quarter_map = {
        "q1": "Q1",
        "q2": "Q2",
        "q3": "Q3",
        "q4": "Q4",

        "first": "Q1",
        "second": "Q2",
        "third": "Q3",
        "fourth": "Q4",

        "1st": "Q1",
        "2nd": "Q2",
        "3rd": "Q3",
        "4th": "Q4",
    }

    # Direct matches
    if value in quarter_map:
        return quarter_map[value]

    # Look for Q1-Q4 anywhere in the value
    match = re.search(r"\bq([1-4])\b", value)

    if match:
        return f"Q{match.group(1)}"

    # Look for written quarter names
    for word, normalized in quarter_map.items():
        if re.search(rf"\b{re.escape(word)}\b", value):
            return normalized

    return None


def normalize_fiscal_year(fiscal_year: Optional[str]) -> Optional[str]:
    """
    Normalize fiscal year representations to a four-digit year.

    Examples:
        FY26 -> 2026
        FY 26 -> 2026
        FY2026 -> 2026
        FY 2026 -> 2026
        fiscal year 2026 -> 2026
    """

    if not fiscal_year:
        return None

    value = str(fiscal_year).strip().lower()

    # Four-digit year
    match = re.search(r"\b(20\d{2})\b", value)

    if match:
        return match.group(1)

    # Two-digit fiscal year
    match = re.search(r"\bfy\s*(\d{2})\b", value)

    if match:
        year = int(match.group(1))
        return f"20{year:02d}"

    return None


def extract_quarter_from_text(text: str) -> Optional[str]:
    """
    Extract the quarter from a transcript header/title.

    Examples:
        Q1 -> Q1
        Q4 -> Q4
        Fourth Quarter -> Q4
        4th Quarter -> Q4
    """

    value = text.lower()

    quarter_patterns = [
        (r"\bq1\b", "Q1"),
        (r"\bq2\b", "Q2"),
        (r"\bq3\b", "Q3"),
        (r"\bq4\b", "Q4"),

        (r"\bfirst\s+quarter\b", "Q1"),
        (r"\bsecond\s+quarter\b", "Q2"),
        (r"\bthird\s+quarter\b", "Q3"),
        (r"\bfourth\s+quarter\b", "Q4"),

        (r"\b1st\s+quarter\b", "Q1"),
        (r"\b2nd\s+quarter\b", "Q2"),
        (r"\b3rd\s+quarter\b", "Q3"),
        (r"\b4th\s+quarter\b", "Q4"),
    ]

    for pattern, quarter in quarter_patterns:
        if re.search(pattern, value):
            return quarter

    return None


def extract_fiscal_year_from_text(text: str) -> Optional[str]:
    """
    Extract the fiscal year from a transcript header/title.

    Examples:
        FY26 -> 2026
        FY 26 -> 2026
        FY2026 -> 2026
        FY 2026 -> 2026
        Fiscal Year 2026 -> 2026
        First Quarter 2026 -> 2026
        1Q 2026 -> 2026
        Q1 2026 -> 2026
    """

    value = text.lower()

    # FY2026 / FY 2026
    match = re.search(r"\bfy\s*(20\d{2})\b", value)

    if match:
        return match.group(1)

    # FY26 / FY 26
    match = re.search(r"\bfy\s*(\d{2})\b", value)

    if match:
        return f"20{match.group(1)}"

    # Fiscal Year 2026
    match = re.search(r"\bfiscal\s+year\s+(20\d{2})\b", value)

    if match:
        return match.group(1)

    # Fiscal 2026
    match = re.search(r"\bfiscal\s+(20\d{2})\b", value)

    if match:
        return match.group(1)

    # Q1 2026 / Q2 2026 / Q3 2026 / Q4 2026
    match = re.search(r"\bq[1-4]\s+(20\d{2})\b", value)

    if match:
        return match.group(1)

    # 1Q 2026 / 2Q 2026 / 3Q 2026 / 4Q 2026
    match = re.search(r"\b[1-4]q\s+(20\d{2})\b", value)

    if match:
        return match.group(1)

    # First Quarter 2026 / Second Quarter 2026 / etc.
    match = re.search(
        r"\b(?:first|second|third|fourth)\s+quarter\s+(20\d{2})\b",
        value
    )

    if match:
        return match.group(1)

    # 1st Quarter 2026 / 2nd Quarter 2026 / etc.
    match = re.search(
        r"\b(?:1st|2nd|3rd|4th)\s+quarter\s+(20\d{2})\b",
        value
    )

    if match:
        return match.group(1)

    return None


def normalize_metadata(metadata: dict) -> dict:
    """
    Normalize LLM-generated metadata before constructing ReportMetadata.
    """

    return {
        "company": metadata.get("company"),
        "ticker": (
            metadata.get("ticker").strip().upper()
            if metadata.get("ticker")
            else None
        ),
        "quarter": normalize_quarter(metadata.get("quarter")),
        "fiscal_year": normalize_fiscal_year(metadata.get("fiscal_year")),
        "call_date": metadata.get("call_date"),
        "ceo": metadata.get("ceo"),
        "cfo": metadata.get("cfo"),
    }


def extract_metadata(transcript: str, transcript_name: str) -> ReportMetadata:
    """
    Extract metadata from an earnings call transcript.

    Uses the LLM for semantic metadata and deterministic
    extraction from the transcript header for quarter and
    fiscal year.
    """

    prompt = MetadataPrompt.build(transcript)

    response = generate_response(prompt)

    print("\nRAW METADATA RESPONSE:")
    print(repr(response))

    try:
        metadata = json.loads(response)

    except json.JSONDecodeError as e:
        raise ValueError(
            "LLM did not return valid JSON.\n\n"
            f"Response repr:\n{response!r}"
        ) from e

    # Extract highly structured information directly from
    # the transcript header.
    header = transcript[:1000]

    header_quarter = extract_quarter_from_text(header)
    header_fiscal_year = extract_fiscal_year_from_text(header)

    # Prefer deterministic extraction when available.
    if header_quarter is not None:
        metadata["quarter"] = header_quarter

    if header_fiscal_year is not None:
        metadata["fiscal_year"] = header_fiscal_year

    # Normalize all metadata after merging the two sources.
    metadata = normalize_metadata(metadata)

    return ReportMetadata(
    transcript_name=transcript_name,
    company=metadata.get("company"),
    ticker=metadata.get("ticker"),
    quarter=metadata.get("quarter"),
    fiscal_year=metadata.get("fiscal_year"),
    call_date=metadata.get("call_date"),
    ceo=metadata.get("ceo"),
    cfo=metadata.get("cfo"),
    )