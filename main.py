from generate_email_addresses import *


def ensure_unique_emails(email_dict):
    # Ensure unique email addresses
    unique_emails = {}
    for student, email in email_dict.items():
        count = 1
        original_email = email
        while email in unique_emails.values():
            email = f"{original_email[:-10]}{count}@gmail.com"
            count += 1
        unique_emails[student] = email
    return unique_emails


def main():
    file_path = r'C:\Users\25475\Desktop\Test Files.xlsx'
    sheet_names = ['File_A', 'File_B']

    # Read student names and genders from the .xlsx file
    df = read_students_from_excel(file_path, sheet_names)

    males = []
    females = []

    for index, row in df.iterrows():
        student_name = row['Student Name']
        gender = row['Gender']

        # Parse the student's name
        first_name, last_name = parse_student_name(student_name)

        # Generate the email address
        email = generate_email(first_name, last_name)

        # Add the student to the appropriate gender list
        if gender == 'M':  # Male
            males.append((student_name, email))
        elif gender == 'F':  # Female
            females.append((student_name, email))

    # Get the number of male and female students
    num_of_males = len(males)
    num_of_females = len(females)

    # Print the list of male students and their count
    print(f"\nMale Students ({num_of_males}):")
    for student, email in males:
        print(f"Student Name: {student} - Email address: {email}")

    # Print the list of female students and their count
    print(f"\nFemale Students ({num_of_females}):")
    for student, email in females:
        print(f"Student Name: {student} - Email address: {email}")

    special_char_students = find_students_with_special_characters(df)

    print(f"\nStudents with Special Characters:")
    for index, row in special_char_students.iterrows():
        print(row['Student Name'])


if __name__ == "__main__":
    main()