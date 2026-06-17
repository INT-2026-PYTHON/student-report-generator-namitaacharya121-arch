from .stats import (
    average_per_student,
    subjects_offered,
    top_scorer,
    passing_students
)

def format_report(records: list[dict]) -> str:

    averages = average_per_student(records)
    subjects = sorted(subjects_offered(records))
    topper_name, topper_avg = top_scorer(records)
    passed = passing_students(records)

    report = []
    report.append(f"Total Records: {len(records)}")

    report.append("\nSubjects Offered:")
    for subject in subjects:
        report.append(subject)

    report.append("\nAverage Scores:")
    for name in sorted(averages):
        report.append(f"{name}: {averages[name]}")

    report.append(
        f"\nTop Scorer: {topper_name} ({topper_avg})"
    )

    report.append("\nPassing Students:")
    for student in passed:
        report.append(student)

    return "\n".join(report)