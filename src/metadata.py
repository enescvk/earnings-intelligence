from dataclasses import dataclass
from typing import Optional
import json

from src.prompts import MetadataPrompt
from src.llm import generate_response


@dataclass
class ReportMetadata:
    company: str
    ticker: str
    quarter: str
    fiscal_year: str
    call_date: Optional[str]
    ceo: Optional[str]
    cfo: Optional[str]

    @property
    def filename(self) -> str:
        return f"{self.ticker}_{self.quarter}_{self.fiscal_year}.md"

def extract_metadata(transcript: str) -> ReportMetadata:
    """
    Extracts metadata from an earnings call transcript using the LLM.

    Parameters
    ----------
    transcript : str
        Full earnings call transcript.

    Returns
    -------
    ReportMetadata
        Parsed metadata object.
    """

    prompt = MetadataPrompt.build(transcript)

    response = generate_response(prompt)

    try:
        metadata = json.loads(response)

    except json.JSONDecodeError as e:
        raise ValueError(
            "LLM did not return valid JSON.\n\n"
            f"Response:\n{response}"
        ) from e

    return ReportMetadata(
        company=metadata.get("company"),
        ticker=metadata.get("ticker"),
        quarter=metadata.get("quarter"),
        fiscal_year=metadata.get("fiscal_year"),
        call_date=metadata.get("call_date"),
        ceo=metadata.get("ceo"),
        cfo=metadata.get("cfo"),
    )