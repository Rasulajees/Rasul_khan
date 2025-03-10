# Student Marksheet Generator

def get_student_details():
    name = input("Enter the student's name: ")
    num_subjects = int(input("Enter the number of subjects: "))
    subjects = {}

    for _ in range(num_subjects):
        subject_name = input("Enter the subject name: ")
        marks = float(input(f"Enter marks for {subject_name}: "))
        subjects[subject_name] = marks
    return name, subjects

def calculate_total_and_average(subjects):
    total_marks = sum(subjects.values())
    average_marks = total_marks / len(subjects)
    return total_marks, average_marks

def display_marksheet(name, subjects, total, average):
    print("\n----------- Marksheet -----------")
    print(f"Student Name: {name}")
    print("---------------------------------")
    print("Subject\t\tMarks")
    print("---------------------------------")
    for subject, marks in subjects.items():
        print(f"{subject}\t\t{marks}")
    print("---------------------------------")
    print(f"Total Marks:\t{total}")
    print(f"Average Marks:\t{average:.2f}")
    print("---------------------------------")

# Main program execution
if __name__ == "__main__":
    student_name, subjects = get_student_details()
    total, average = calculate_total_and_average(subjects)
    display_marksheet(student_name, subjects, total, average)
