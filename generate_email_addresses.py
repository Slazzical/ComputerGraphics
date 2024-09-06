import pandas as pd
import re


def generate_email(first_name, last_name):
    # Remove any special characters from the last name
    last_name = re.sub(r'[^a-zA-Z]', '', last_name)
    first_name = re.sub(r'[^a-zA-Z]', '', first_name)
    email = f"{last_name[0].lower()}{first_name.lower()}@gmail.com"
    return email


def read_students_from_excel(file_path, sheet_names):
    # Read data from all sheets and extract the necessary columns (Student Name and Gender)
    all_data = []
    for sheet in sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet, engine='openpyxl')
        all_data.append(df[['Student Name', 'Gender']])  # Extract Student Name and Gender

    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df


def parse_student_name(full_name):
    # Split the student name in "Lname, Middlename Fname" format
    parts = full_name.split(', ')
    last_name = parts[0]
    rest_name = parts[1].split()
    first_name = rest_name[-1]  # Extract the first name
    return first_name, last_name


def find_students_with_special_characters(df):
    # Regular expression to match names with special characters
    special_char_regex = re.compile(r'[^\w\s,]')

    special_char_students = df[df['Student Name'].apply(lambda name: bool(special_char_regex.search(name)))]

    return special_char_students


