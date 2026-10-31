import re


STATUS_PATTERN = r"(NORMAL|HIGH|LOW|BORDERLINE|ELEVATED)"


def _extract(
    text: str,
    test_name: str,
    pattern: str,
    unit: str,
) -> dict | None:
    match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)

    if not match:
        return None

    value_text = match.group(1).replace(",", "")

    try:
        value = float(value_text)
    except ValueError:
        return None

    reference_range = match.group(2).strip()
    status = match.group(3).strip().upper()

    return {
        "test_name": test_name,
        "value": value,
        "value_text": match.group(1),
        "unit": unit,
        "reference_range": reference_range,
        "status": status,
    }


def extract_clinical_observations(text: str) -> list[dict]:
    """
    Extract structured laboratory observations from a medical report.

    This deterministic parser supports common variations in laboratory
    report wording and formatting.
    """

    patterns = [
        (
            "Hemoglobin",
            rf"Hemoglobin(?:\s*\(Hb\))?\s*(?:.*?\s)?([\d.]+)\s+g/dL\s+(.+?)\s+{STATUS_PATTERN}",
            "g/dL",
        ),
        (
            "WBC",
            rf"(?:Total Leucocyte Count|White Blood Cell Count|WBC)(?:\s*\(WBC\))?\s*(?:.*?\s)?([\d,]+)\s+/(?:µ|u)?L\s+(.+?)\s+{STATUS_PATTERN}",
            "/µL",
        ),
        (
            "RBC",
            rf"(?:RBC Count|Red Blood Cell Count|RBC)\s*(?:.*?\s)?([\d.]+)\s+mil/(?:µ|u)?L\s+(.+?)\s+{STATUS_PATTERN}",
            "mil/µL",
        ),
        (
            "Platelets",
            rf"(?:Platelet Count|Platelets)\s*(?:.*?\s)?([\d,]+)\s+/(?:µ|u)?L\s+(.+?)\s+{STATUS_PATTERN}",
            "/µL",
        ),
        (
            "PCV",
            rf"(?:Packed Cell Volume(?:\s*\(PCV\s*/\s*Hematocrit\))?|PCV|Hematocrit)\s*([\d.]+)\s+%\s+(.+?)\s+{STATUS_PATTERN}",
            "%",
        ),
        (
            "MCV",
            rf"(?:Mean Corpuscular Volume\s*\(MCV\)|MCV)\s*(?:.*?\s)?([\d.]+)\s+fL\s+(.+?)\s+{STATUS_PATTERN}",
            "fL",
        ),
        (
            "Neutrophils",
            rf"Neutrophils\s+([\d.]+)\s+%\s+(.+?)\s+{STATUS_PATTERN}",
            "%",
        ),
        (
            "Lymphocytes",
            rf"Lymphocytes\s+([\d.]+)\s+%\s+(.+?)\s+{STATUS_PATTERN}",
            "%",
        ),
        (
            "Monocytes",
            rf"Monocytes\s+([\d.]+)\s+%\s+(.+?)\s+{STATUS_PATTERN}",
            "%",
        ),
        (
            "Eosinophils",
            rf"Eosinophils\s+([\d.]+)\s+%\s+(.+?)\s+{STATUS_PATTERN}",
            "%",
        ),
        (
            "Fasting Glucose",
            rf"(?:Fasting Plasma Glucose|Fasting Glucose)(?:\s*\(FPG\))?\s*(?:.*?\s)?([\d.]+)\s+mg/dL\s+(.+?)\s+{STATUS_PATTERN}",
            "mg/dL",
        ),
        (
            "HbA1c",
            rf"HbA1c(?:\s*\(Glycated Hemoglobin\))?\s*(?:.*?\s)?([\d.]+)\s+%\s+(.+?)\s+{STATUS_PATTERN}",
            "%",
        ),
        (
            "Creatinine",
            rf"(?:Serum Creatinine|Creatinine)\s*(?:.*?\s)?([\d.]+)\s+mg/dL\s+(.+?)\s+{STATUS_PATTERN}",
            "mg/dL",
        ),
        (
            "eGFR",
            rf"(?:Estimated GFR(?:\s*\(eGFR(?:,\s*CKD-EPI)?\))?|eGFR)\s*(?:.*?\s)?([\d.]+)\s+mL/min/1\.73m[²2]\s*(.+?)\s+{STATUS_PATTERN}",
            "mL/min/1.73m²",
        ),
        (
            "ALT/SGPT",
            rf"(?:Serum Alanine Aminotransferase\s*\(ALT/\s*SGPT\)|ALT/SGPT|ALT)\s*(?:.*?\s)?([\d.]+)\s+U/L\s+(.+?)\s+{STATUS_PATTERN}",
            "U/L",
        ),
        (
            "Total Cholesterol",
            rf"Total Cholesterol\s*(?:.*?\s)?([\d.]+)\s+mg/dL\s+(.+?)\s+{STATUS_PATTERN}",
            "mg/dL",
        ),
        (
            "Triglycerides",
            rf"Triglycerides\s*(?:.*?\s)?([\d.]+)\s+mg/dL\s+(.+?)\s+{STATUS_PATTERN}",
            "mg/dL",
        ),
        (
            "HDL",
            rf"(?:HDL Cholesterol\s*\(Direct\)|HDL)\s*(?:.*?\s)?([\d.]+)\s+mg/dL\s+(.+?)\s+{STATUS_PATTERN}",
            "mg/dL",
        ),
        (
            "LDL",
            rf"(?:LDL Cholesterol\s*\(Calculated\)|LDL)\s*(?:.*?\s)?([\d.]+)\s+mg/dL\s+(.+?)\s+{STATUS_PATTERN}",
            "mg/dL",
        ),
    ]

    observations = []

    for test_name, pattern, unit in patterns:
        observation = _extract(
            text,
            test_name,
            pattern,
            unit,
        )

        if observation:
            observations.append(observation)

    return observations