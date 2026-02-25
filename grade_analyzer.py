# Name: MI ASJATH AHAMED
# Roll Number: iitp_aimltn_2602113
# Assignment: Python Functions & Modularity

def process_scores(students):
    averages = {}
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)
    return averages


def classify_grades(averages):
    classified = {}
    for name, avg in averages.items():
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "F"
        classified[name] = (avg, grade)
    return classified


def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    
    total_students = len(classified)
    passed = 0

    for name, (avg, grade) in classified.items():
        if avg >= passing_avg:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"

        print(f"{name} | Avg: {avg} | Grade: {grade} | Status: {status}")

    print("===============================")
    print("Total Students:", total_students)
    print("Passed:", passed)
    print("Failed:", total_students - passed)

    return passed


if __name__ == "__main__":
    students = {
        "Alice": [85, 90, 88],
        "Bob": [60, 65, 63],
        "Clara": [95, 92, 90]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
