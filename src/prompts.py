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

Return your report using EXACTLY the following Markdown headings in this exact order:

# Executive Summary

Summarize the quarter in 2-3 paragraphs.

# Financial Highlights

Summarize the most important financial metrics discussed, such as revenue, EPS, margins, operating income, cash flow, guidance, or other key performance indicators mentioned by management.

# Positive Developments

Identify the company's major strengths, achievements, and positive business developments.

# Negative Developments

Identify challenges, weaknesses, or disappointing results.

# Risks

List the key risks mentioned or implied by management.

# Opportunities

List future growth opportunities discussed during the call.

# Management Guidance

Summarize management's outlook for future quarters.

# Key Quotes

Extract 3–5 short, impactful quotes from management that best reflect the company's strategy, outlook, or performance.

# Management Confidence

Give a confidence score from 1-10 and explain your reasoning.

Rules:

- Use only information from the transcript.
- Do not speculate.
- Do not invent facts.
- If a section cannot be completed from the transcript, write "Not discussed."
- Do not omit any section.
"""

    return prompt