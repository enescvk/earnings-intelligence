def build_report_prompt(transcript: str) -> str:
    """
    Creates the prompt that will be sent to the LLM.
    """

    prompt = f"""
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

    return prompt