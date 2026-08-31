# Create data as a list of dictionaries
data = [
    {'Name': 'Sanzu', 'Age': 20, 'Score': 99},
    {'Name': 'Bob', 'Age': 25, 'Score': 90},
    {'Name': 'Charlie', 'Age': 23, 'Score': 88}
]

# Show the whole table
for row in data:
    print(row)

# Get basic statistics for Age and Score
ages = [row['Age'] for row in data]
scores = [row['Score'] for row in data]

print("Age - min:", min(ages), "max:", max(ages), "mean:", sum(ages)/len(ages))
print("Score - min:", min(scores), "max:", max(scores), "mean:", sum(scores)/len(scores))

# Access the Age column
print("Ages:", ages)

# Filter rows (e.g., Age > 21)
filtered = [row for row in data if row['Age'] > 21]
print("People with Age > 21:", filtered)

# Find the person with the highest score
highest = max(data, key=lambda x: x['Score'])
print("Person with highest score:", highest)

# Sort data by Age (ascending)
sorted_by_age = sorted(data, key=lambda x: x['Age'])
print("Sorted by Age:", sorted_by_age)

# Add a new person
data.append({'Name': 'Amit', 'Age': 22, 'Score': 91})
print("After adding Amit:", data)

# Average score for people older than 21
scores_over_21 = [row['Score'] for row in data if row['Age'] > 21]
if scores_over_21:
    print("Average score (Age > 21):", sum(scores_over_21)/len(scores_over_21))
else:
    print("No one over 21.")

# Save the data to a CSV file
import csv
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

import csv

# Load students from CSV
def load_students(filename):
    students = []
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['Age'] = int(row['Age'])
                row['Score'] = int(row['Score'])
                students.append(row)
    except FileNotFoundError:
        pass  # File doesn't exist yet
    return students

# Save students to CSV
def save_students(filename, students):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Age', 'Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

# Add a new student
def add_student(students):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    score = int(input("Enter score: "))
    students.append({'Name': name, 'Age': age, 'Score': score})
    print("Student added!")

# Display all students
def display_students(students):
    print("All Students:")
    for s in students:
        print(s)

# Search student by name
def search_student(students):
    name = input("Enter name to search: ")
    found = [s for s in students if s['Name'].lower() == name.lower()]
    if found:
        for s in found:
            print(s)
    else:
        print("No student found with that name.")

def delete_student(students):
    name = input("Enter name to delete: ")
    original_count = len(students)
    students[:] = [s for s in students if s['Name'].lower() != name.lower()]
    if len(students) < original_count:
        print("Student deleted.")
    else:
        print("No student found with that name.")

def show_statistics(students):
    if not students:
        print("No students to analyze.")
        return
    scores = [s['Score'] for s in students]
    print("Score - min:", min(scores), "max:", max(scores), "mean:", sum(scores)/len(scores))

def main():
    filename = 'students.csv'
    students = load_students(filename)
    while True:
        print("\n1. Add Student\n2. Display All\n3. Search by Name\n4. Delete Student\n5. Show Statistics\n6. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            show_statistics(students)
        elif choice == '6':
            save_students(filename, students)
            print("Data saved. Goodbye! Sanzu")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()