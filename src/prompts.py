class ReportPrompt:
    TEMPLATE = """
You are an experienced equity research analyst.

-------------------------
BEGIN TRANSCRIPT
-------------------------

{transcript}

-------------------------
END TRANSCRIPT
-------------------------

Analyze the following earnings call transcript and generate a professional investment research report.

Return the report using EXACTLY the following headings
in the EXACT order shown below.

Do not reorder, rename, or omit any section.

# Executive Summary

Write 2–3 concise paragraphs that summarize:

• Overall business performance
• Major strategic developments
• Future outlook

Focus on what matters most to investors.

# Financial Highlights

Extract the most important financial metrics explicitly reported during the earnings call.

Prioritize quantitative information.

Include, when available:
- Total Revenue
- Revenue Growth (YoY / QoQ)
- EPS
- Gross Margin
- Operating Income
- Net Income
- Free Cash Flow
- Cash Balance
- Segment Revenue
- Capital Return
- Guidance

If numerical values are mentioned, include them exactly as reported.

Do not replace financial metrics with business commentary.

If no financial metrics are discussed, write "Not discussed."

# Positive Developments

Identify the company's major strengths, achievements, and positive business developments.

# Negative Developments

Identify challenges, weaknesses, or disappointing results.

# Risks

List the key risks mentioned or implied by management.

# Opportunities

List the major future growth opportunities discussed by management.

Do not repeat information already covered in Positive Developments.

# Management Guidance

Summarize management's outlook for future quarters.

# Key Quotes

Extract 3–5 short, impactful quotes from management that best reflect the company's strategy, outlook, or performance.

# Management Confidence

Assess management's confidence during the earnings call.

Provide:

Assign a confidence score between 1 (very low confidence) and 10 (very high confidence).
- Supporting Evidence:
    - Evidence 1
    - Evidence 2
    - Evidence 3

Base your assessment only on management's tone, language, guidance, and statements made during the transcript.
Do not speculate.

Rules:

- Use only information from the transcript.
- Do not speculate.
- Do not invent facts.
- If a section cannot be completed from the transcript, write "Not discussed."
- Do not omit any section.

Before returning your answer, verify that:

- Every required section is present.
- The sections appear in the exact order requested.
- No section is repeated.
- No information is repeated across sections.
"""

    @classmethod
    def build(cls, transcript: str) -> str:
        return cls.TEMPLATE.format(transcript=transcript)


class MetadataPrompt:
    TEMPLATE = """
    -------------------------
    BEGIN TRANSCRIPT
    -------------------------

    {transcript}

    -------------------------
    END TRANSCRIPT
    -------------------------

    Extract the following metadata from the earnings call transcript.

    Return ONLY valid JSON.

    Do not explain anything.
    Do not summarize the transcript.
    Do not wrap the JSON inside markdown.

    If a value cannot be determined from the transcript, return null.

    IMPORTANT INSTRUCTIONS FOR FISCAL YEAR AND QUARTER:

    The earnings period may be expressed in many different ways.

    Quarter examples include:
    - Q1, Q2, Q3, Q4
    - First Quarter, Second Quarter, Third Quarter, Fourth Quarter
    - 1st Quarter, 2nd Quarter, 3rd Quarter, 4th Quarter
    - First quarter of fiscal year 2026
    - FY26 Fourth Quarter
    - FY2026 Q4

    Normalize the quarter to exactly one of:
    - Q1
    - Q2
    - Q3
    - Q4

    For example:
    - "First Quarter" -> "Q1"
    - "Second Quarter" -> "Q2"
    - "Third Quarter" -> "Q3"
    - "Fourth Quarter" -> "Q4"
    - "FY26 Fourth Quarter" -> "Q4"

    Fiscal year may be expressed as:
    - FY26
    - FY 26
    - FY2026
    - FY 2026
    - fiscal year 2026
    - fiscal 2026

    Normalize the fiscal year to the four-digit year.

    For example:
    - "FY26" -> "2026"
    - "FY 26" -> "2026"
    - "FY2026" -> "2026"
    - "FY 2026" -> "2026"

    Pay particular attention to the title and opening section of the transcript,
    as earnings-call titles frequently contain the fiscal year and quarter.

    Return this exact JSON schema:

    {{
        "company": null,
        "ticker": null,
        "quarter": null,
        "fiscal_year": null,
        "call_date": null,
        "ceo": null,
        "cfo": null
    }}
    """

    @classmethod
    def build(cls, transcript: str) -> str:
        return cls.TEMPLATE.format(transcript=transcript)