def detect_attention(observations: list[dict]) -> list[dict]:
    """
    Detect observations that may deserve attention.

    This is a deterministic rule-based component for the
    educational/research prototype of MedIntel AI.

    It does not provide diagnosis or treatment recommendations.
    """

    attention_statuses = {
        "HIGH",
        "LOW",
        "ELEVATED",
        "BORDERLINE",
    }

    results = []

    for observation in observations:
        status = observation.get("status")

        result = {
            "test_name": observation.get("test_name"),
            "value": observation.get("value"),
            "unit": observation.get("unit"),
            "status": status,
            "attention": status in attention_statuses,
        }

        results.append(result)

    return results