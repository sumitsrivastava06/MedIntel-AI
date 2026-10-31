
from collections import defaultdict


def analyze_trends(observations: list[dict]) -> list[dict]:
    """
    Analyze longitudinal clinical observations.

    Observations should contain:
        test_name, value, unit, status, and observed_at.

    Observations without dates are excluded from chronological
    comparisons because their order cannot be established reliably.
    """

    grouped = defaultdict(list)

    for observation in observations:
        if observation.get("value") is None:
            continue

        grouped[observation["test_name"]].append(observation)

    trends = []

    for test_name, values in grouped.items():

        dated_values = [
            item for item in values
            if item.get("observed_at")
        ]

        dated_values.sort(
            key=lambda item: item["observed_at"]
        )

        latest = (
            dated_values[-1]
            if dated_values
            else None
        )

        previous = (
            dated_values[-2]
            if len(dated_values) >= 2
            else None
        )

        trend = {
            "test_name": test_name,
            "unit": (
                latest.get("unit")
                if latest
                else values[-1].get("unit")
            ),
            "latest_value": (
                latest.get("value")
                if latest
                else None
            ),
            "latest_status": (
                latest.get("status")
                if latest
                else None
            ),
            "latest_observed_at": (
                latest.get("observed_at")
                if latest
                else None
            ),
            "previous_value": None,
            "previous_observed_at": None,
            "change": None,
            "change_percent": None,
            "direction": "insufficient_dated_data",
            "attention": False,
            "comparison_available": False,
        }

        if latest is not None:
            if latest.get("status") not in (None, "NORMAL"):
                trend["attention"] = True

        if previous is not None:
            previous_value = previous["value"]
            latest_value = latest["value"]

            trend["previous_value"] = previous_value
            trend["previous_observed_at"] = (
                previous.get("observed_at")
            )
            trend["comparison_available"] = True

            change = latest_value - previous_value

            trend["change"] = round(change, 2)

            if previous_value != 0:
                trend["change_percent"] = round(
                    (change / previous_value) * 100,
                    2,
                )

            if change > 0:
                trend["direction"] = "increasing"
            elif change < 0:
                trend["direction"] = "decreasing"
            else:
                trend["direction"] = "stable"

        elif latest is not None:
            trend["direction"] = "no_previous_value"

        trends.append(trend)

    return trends
