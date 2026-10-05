"""Marks & Grade Calculator
Enter marks for each subject and get total, percentage, grade and result.
"""


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    return "F"


def read_marks(subject, max_marks):
    """Keep asking until a valid mark is entered."""
    while True:
        try:
            marks = float(input(f"Marks in {subject} (out of {max_marks:.0f}): "))
            if 0 <= marks <= max_marks:
                return marks
            print(f"  Please enter a value between 0 and {max_marks:.0f}.")
        except ValueError:
            print("  Please enter a number.")


def main():
    print("=== Marks & Grade Calculator ===")
    name = input("Student name: ").strip()
    count = int(input("Number of subjects: "))
    max_marks = float(input("Maximum marks per subject: "))

    results = {}
    for i in range(1, count + 1):
        subject = input(f"Name of subject {i}: ").strip()
        results[subject] = read_marks(subject, max_marks)

    total = sum(results.values())
    percentage = total / (count * max_marks) * 100
    grade = get_grade(percentage)
    passed = percentage >= 40 and min(results.values()) >= 0.33 * max_marks
    status = "PASS" if passed else "FAIL"

    print("\n--- Report Card ---")
    print(f"Name: {name}")
    for subject, marks in results.items():
        print(f"{subject:<20}{marks:>6.1f}/{max_marks:.0f}")
    print(f"Total: {total:.1f}/{count * max_marks:.0f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {status}")


if __name__ == "__main__":
    main()
