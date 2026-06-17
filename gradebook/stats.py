def average_per_student(records: list[dict]) -> dict[str, float]:
    totals = {}
    counts = {}

    for record in records:
        name = record["name"]
        score = record["score"]

        totals[name] = totals.get(name, 0) + score
        counts[name] = counts.get(name, 0) + 1

    averages = {}
    for name in totals:
        averages[name] = round(totals[name] / counts[name], 2)

    return averages


def subjects_offered(records: list[dict]) -> set[str]:
    return {record["subject"] for record in records}


def top_scorer(records: list[dict]) -> tuple[str, float]:
    averages = average_per_student(records)
    name = max(averages, key=averages.get)
    return (name, averages[name])


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    averages = average_per_student(records)

    passed = [
        name
        for name, avg in averages.items()
        if avg >= threshold
    ]

    return sorted(passed)