import re
from datetime import datetime, date


DATE_PATTERNS = [
    r"SAMPLE\s+COLLECTED\s*:\s*(\d{1,2}-[A-Za-z]{3}-\d{4})",
    r"COLLECTION\s+DATE\s*:\s*(\d{1,2}-[A-Za-z]{3}-\d{4})",
    r"COLLECTED\s+ON\s*:\s*(\d{1,2}-[A-Za-z]{3}-\d{4})",
    r"REPORT\s+DATE\s*:\s*(\d{1,2}-[A-Za-z]{3}-\d{4})",
    r"DATE\s+OF\s+COLLECTION\s*:\s*(\d{1,2}-[A-Za-z]{3}-\d{4})",
]


def extract_report_date(text: str) -> date | None:
    """
    Extract the sample collection date from medical report text.

    Returns a Python date object, or None if no supported date is found.
    """

    for pattern in DATE_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            date_text = match.group(1)

            try:
                return datetime.strptime(
                    date_text,
                    "%d-%b-%Y",
                ).date()

            except ValueError:
                continue

    return None