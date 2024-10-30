# -------------------------- Import Libraries -------------------------

import sqlite3
from contextlib import contextmanager
import tabulate
import json
import xml.etree.ElementTree as ET
from typing import Generator

# ------------------------ Function Definition ------------------------


def formatting(data: list[tuple], keys: list[str]) -> list[dict]:
    """
    A function that returns a list of dictionaries, from a list of
    tuples

    Args:
        data: list.
            A list of tuples as a result of a query to a
            database.
        keys: list.
            The key values that will be used for the
            list_dct, where the values within the tuples in the data
            argument.

    Returns:
        mapping: list
            A list of dictionaries

    """
    # Use the map function to apply the lambda function to get a
    # dictionary in a map object
    mapping = map(lambda x: dict(zip(keys, x)), data)
    # List comprehension on the map object
    mapping = [dct for dct in mapping]

    return mapping


def storeDataAsJSON(data: list[tuple], filename: str) -> None:
    """
    A function that is responsible for storing a list of tuples into a
    .json file.

    Args:
        data: list.
            A list of tuples as a result of a query to a
            database.
        keys: list.
            The key values that will be used for the
            list_dct, where the values within the tuples in the data
            argument.
        filename: str.
            Name the json file will be stored as.

    Returns:
        None
    """
    # Store the list of tuples as a list of dictionaries
    with open(f'{filename}', 'w') as file:
        # Indent the file, to enhance readibility
        json.dump(data, file, indent=4)


def storeDataAsXML(data: list[tuple], filename: str) -> None:
    """
    A function that is responsible for storing a list of tuples into a
    .xml file.

    Args:
        data: list.
            A list of tuples as a result of a query to a
            database.
        filename: str.
            Name the .xml file will be stored as.

    Returns:
        None
    """
    if command == 'vs':
        # Create the root element
        root = ET.Element("data")
        # Iterate over tuples in the data list
        for element in data:
            # Create the sub element to come below the root element
            tuple_element = ET.SubElement(root, "tuple")

            # Create the sub elements to come below the tuple element
            subjects_element = ET.SubElement(tuple_element, "subject")
            subjects_element.text = (element['Subjects'])

    elif command == 'la':
        # Create the root element
        root = ET.Element("data")
        for element in data:
            # Create the sub element as the children of the root element
            tuple_element = ET.SubElement(root, "tuple")

            # Create the sub elements as the children of the tuple element
            street_element = ET.SubElement(tuple_element, "street_name")
            street_element.text = (element['Street Name'])

            city_element = ET.SubElement(tuple_element, "city")
            city_element.text = (element['City'])

    elif command == 'lr':
        # Create the root element
        root = ET.Element("data")
        for element in data:
            # Create the sub element as the children of the root element
            tuple_element = ET.SubElement(root, "tuple")

            # Create the sub elements as the children of the tuple element
            completeness_element = (
                ET.SubElement(tuple_element, "completeness")
            )
            completeness_element.text = str(element['Completeness'])

            efficiency_element = (
                ET.SubElement(tuple_element, "efficiency")
            )
            efficiency_element.text = str(element['Efficiency'])

            style_element = (
                ET.SubElement(tuple_element, "style")
            )
            style_element.text = str(element['Style'])

            documentation_element = (
                ET.SubElement(tuple_element, "documentation")
            )
            documentation_element.text = str(element['Documentation'])

            review_element = ET.SubElement(tuple_element, "review")
            review_element.text = (element['Review'])

    elif command == 'lc':
        # Create the root element
        root = ET.Element("data")
        # Iterate over tuples in the data list
        for element in data:
            # Create the sub element to come below the root element
            tuple_element = ET.SubElement(root, "tuple")

            # Create the sub elements to come below the tuple element
            teacher_element = ET.SubElement(tuple_element, "subject")
            teacher_element.text = (element['Subjects'])

    elif command == 'lnc':
        # Create the root element
        root = ET.Element("data")
        # Iterate over tuples in the data list
        for element in data:
            # Create the sub element to come below the root element
            tuple_element = ET.SubElement(root, "tuple")

            # Create the sub elements to come below the tuple element
            student_number_element = ET.SubElement(tuple_element, "student_id")
            student_number_element.text = (element['Student ID'])

            firstname_element = ET.SubElement(tuple_element, "first_name")
            firstname_element.text = (element['First Name'])

            lastname_element = ET.SubElement(tuple_element, "last_name")
            lastname_element.text = (element['Last Name'])

            email_address_element = (
                ET.SubElement(tuple_element, "email_address")
            )
            email_address_element.text = (element['Email Address'])

            course_element = ET.SubElement(tuple_element, "course")
            course_element.text = (element['Course'])

    elif command == 'lf':
        # Create the root element
        root = ET.Element("data")
        # Iterate over tuples in the data list
        for element in data:
            # Create the sub element to come below the root element
            tuple_element = ET.SubElement(root, "tuple")

            # Create the sub elements to come below the tuple element
            student_number_element = ET.SubElement(tuple_element, "student_id")
            student_number_element.text = (element['Student ID'])

            firstname_element = ET.SubElement(tuple_element, "first_name")
            firstname_element.text = (element['First Name'])

            lastname_element = ET.SubElement(tuple_element, "last_name")
            lastname_element.text = (element['Last Name'])

            email_address_element = (
                ET.SubElement(tuple_element, "email_address")
            )
            email_address_element.text = (element['Email Address'])

            course_element = ET.SubElement(tuple_element, "course")
            course_element.text = (element['Course'])

            marks_element = ET.SubElement(tuple_element, "mark")
            marks_element.text = str(element['Marks'])

    # Convert the tree to a string and indent for readability
    tree = ET.ElementTree(root)
    # Indentation for readability
    ET.indent(tree, space="    ", level=0)
    # Write the formatted XML to a file
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def tableFormat(query_list: list[tuple], column_names: list[str]) -> str:
    """
    A function that prints a format-fixed width table for pretty printing.

    Args:
        query_list: list.
            List of tuples representing the data queried from a
            database
        column_names: list.
            List of names which are columns from the queried  database
            table.

    Returns:
        table: str.
            Prettified string into a table from the queried database
    """
    table = (
        tabulate.tabulate(query_list, headers=column_names, showindex=True)
    )

    print(f'\n{table}')


def usageIsIncorrect(input: list[str], num_args: int) -> bool:
    """
    A function that is responsible for validifying the input provided
    by the user

    Args:
        input: list.
            A list of string created from the user input
        num_args: int.
            Representing the total arguments provided by the user based
            on the argument of the inpute parameter

    Returns:
        bool
    """
    if len(input) != num_args + 1:
        print(f"The {input[0]} command requires {num_args} arguments.")
        return True
    return False


# Use contextmanager as decorator which enables us to borrow the
# functionality of the contextmanager function, without altering the
# function itself.
@contextmanager
def openDatabase(db_name) -> Generator:
    """
    A function that is responsible for opening a connection to the
    database provided as an argument. This function helps in
    managing the context of the set up and tear down temporary of
    contexts, establish and resolve custom settings, and acquire and
    release resources. In this case, the context from a database

    Args:
        db_name: str
            The name of the database to connect to.

    Returns:
        None

    """
    conn = sqlite3.connect(db_name)

    # Establish a connection to the database
    try:
        yield conn
    # If no connection could be made to the database
    except sqlite3.Error:
        print("Please store your database as HyperionDev.db")
        quit()
    # Close the database connection regardless of whether the
    # connection was made or not
    finally:
        conn.close()


def courseNameByCourseCode(student_id: str) -> list[tuple]:
    """
    A function that queries the HyperionDev.db to return a list of
    tuples

    Args:
        student_id: str.
            The student id of a student in the HyperionDev.db

    Returns:
        queried_table: list.
            List of tuples representing the queried data from
            HyperionDev.db
    """
    queried_table = (
        cursor.execute(
            """
            SELECT c.course_name
            FROM StudentCourse AS sc
            RIGHT JOIN Course as c
            ON sc.course_code = c.course_code
            WHERE sc.student_id=:query
            """,
            {'query': student_id}
        )
    )

    return queried_table.fetchall()


def addressByNameAndSurname(first_name: str, surname: str) -> list[tuple]:
    """
    A function that queries the HyperionDev.db to return a list of
    tuples

    Args:
        first_name: str.
            First name of a student in the HyperionDev.db
        surname: str.
            Last name of a surname in the HyperionDev.db

    Returns:
        queried_table: list.
            List of tuples representing the queried data from
            HyperionDev.db
    """
    queried_table = (
        cursor.execute(
            """
            SELECT a.street, a.city
            FROM Student AS s
            RIGHT JOIN Address AS a
            ON s.address_id = a.address_id
            WHERE s.first_name=:name AND s.last_name=:surname
            """,
            {'name': first_name, 'surname': surname}
        )
    )

    return queried_table.fetchall()


def reviewTextByStudentID(student_id: str) -> list[tuple]:
    """
    A function that queries the HyperionDev.db to return a list of
    tuples

    Args:
        student_id: str.
            The student id of a student in the HyperionDev.db

    Returns:
        queried_table: list.
            List of tuples representing the queried data from
            HyperionDev.db
    """
    queried_table = (
        cursor.execute(
            """
            SELECT
                r.completeness, r.efficiency, r.style, r.documentation,
                r.review_text
            FROM Review AS r
            RIGHT JOIN  Student as s
            ON r.student_id = s.student_id
            WHERE s.student_id=:query
            """,
            {'query': student_id}
        )
    )

    return queried_table.fetchall()


def courseNameByTeacherID(teacher_id: str) -> list[tuple]:
    """
    A function that queries the HyperionDev.db to return a list of
    tuples

    Args:
        teacher_id: str.
            The id of a teacher in the HyperionDev.db

    Returns:
        queried_table: list.
            List of tuples representing the queried data from
            HyperionDev.db
    """
    queried_table = (
        cursor.execute(
            """
            SELECT course_name
            FROM Course
            WHERE teacher_id=:teacher_id
            """,
            {'teacher_id': teacher_id}
        )
    )

    return queried_table.fetchall()


def incompleteStudents() -> list[tuple]:
    """
    A function that queries the HyperionDev.db to return a list of
    tuples

    Returns:
        queried_table: list.
            List of tuples representing the queried data from
            HyperionDev.db
    """
    queried_table = (
        cursor.execute(
            """
            WITH JoinedStudent AS (
            SELECT
                Student.student_id, Student.first_name, Student.last_name,
                Student.email, StudentCourse.student_id,
                StudentCourse.is_complete, StudentCourse.course_code
            FROM Student
            RIGHT JOIN StudentCourse
            ON Student.student_id = StudentCourse.student_id
            WHERE StudentCourse.is_complete = 0
            )
            SELECT
                js.student_id, js.first_name, js.last_name, js.email,
                C.course_name
            FROM Course AS c
            RIGHT JOIN JoinedStudent AS js
            ON js.course_code = C.course_code
            """
        )
    )

    return queried_table.fetchall()


def studentCompletedBelow30() -> list[tuple]:
    """
    A function that queries the HyperionDev.db to return a list of
    tuples

    Returns:
        queried_table: list.
            List of tuples representing the queried data from
            HyperionDev.db
    """
    queried_table = (
        cursor.execute(
            """
            WITH JoinedStudent AS (
            SELECT
                Student.student_id, Student.first_name, Student.last_name,
                Student.email, StudentCourse.student_id,
                StudentCourse.is_complete, StudentCourse.course_code,
                StudentCourse.mark
            FROM Student
            RIGHT JOIN StudentCourse
            ON Student.student_id = StudentCourse.student_id
            WHERE StudentCourse.is_complete == 1 AND StudentCourse.mark <= 30
            )
            SELECT
                js.student_id, js.first_name, js.last_name, js.email,
                C.course_name, js.mark
            FROM Course AS c
            RIGHT JOIN JoinedStudent AS js
            ON js.course_code = C.course_code
            """
        )
    )

    return queried_table.fetchall()


def offerToStore(data):
    """
    A function that requests the user whether they wish to save the
    queried data from the database as a .json or an .xml file.

    Args:
        data: list.
            A list of a tuples based on the data queried from the
            database HyperionDev.db
    """
    while True:
        print("\nWould you like to store this result?")
        choice = input("Y/[N]? : ").strip().lower()

        if choice == "y":
            filename = input("Specify filename. Must end in .xml or .json: ")
            ext = filename.split(".")[-1]
            if ext == 'xml':
                storeDataAsXML(data, filename)
                break
            elif ext == 'json':
                storeDataAsJSON(data, filename)
                break
            else:
                print("Invalid file extension. Please use .xml or .json")

        elif choice == 'n':
            break

        else:
            print("Invalid choice")

# ------------------ Execute SQL file to the database -----------------


with openDatabase('HyperionDev.db') as conn:
    cursor = conn.cursor()

    # Load and execute the SQL file into the HyperionDev database
    with open('create_database.sql', 'r', encoding='utf-8') as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
    conn.commit()

# -------------------------- Main Application -------------------------

# Store the applications 'landing menu' as a docstring
usage = '''
What would you like to do?

d                          - Demo
vs <student_id>            - View subjects taken by a student
la <firstname> <surname>   - Lookup address for a given firstname and surname
lr <student_id>            - All reviews for a given student_id
lc <teacher_id>            - All courses being given by teacher_id
lnc                        - All students who haven't completed their course
lf                         - All students who have completed their course and
                             achieved 30 or below
e                          - exit this program

Type your option here: '''

print("Welcome to the data querying app!")

while True:
    print()
    # Get input from user.
    # Split the input string into a list of strings.
    user_input = input(usage).split(" ")

    # Parse user input into command and args
    # Store the first string in the user_input list as command
    command = user_input[0]

    # If the length of the user_input list is greater than 1, then
    # list values of user_input as variable args, excluding the
    # first element
    if len(user_input) > 1:
        args = user_input[1:]

    # Return the firstname and the surname for each student
    if command == 'd':
        print('😁 A nice bit of code from me to you - this', end=' ')
        print('prints all student names and surnames:\n')
        with openDatabase('HyperionDev.db') as conn:
            cursor = conn.cursor()
            data = cursor.execute("SELECT * FROM Student")
            data = data.fetchall()
            for _, firstname, surname, _, _ in data:
                print(f"{firstname} {surname}")

    # View courses by student_id
    elif command == 'vs':
        if usageIsIncorrect(user_input, 1):
            continue
        student_id = args[0]
        data = None
        with openDatabase('HyperionDev.db') as conn:
            cursor = conn.cursor()
            data = courseNameByCourseCode(student_id)
            headings = ['Subjects']
        tableFormat(data, headings)
        offerToStore(formatting(data, headings))

    # View the address by student name and surname
    elif command == 'la':
        if usageIsIncorrect(user_input, 2):
            continue
        name = args[0]
        surname = args[1]
        data = None
        with openDatabase('HyperionDev.db') as conn:
            cursor = conn.cursor()
            data = addressByNameAndSurname(name, surname)
            headings = ['Street Name', 'City']
        tableFormat(data, headings)
        offerToStore(formatting(data, headings))

    # View the reviews by student IDs
    elif command == 'lr':
        if usageIsIncorrect(user_input, 1):
            continue
        student_id = args[0]
        data = None
        with openDatabase('HyperionDev.db') as conn:
            cursor = conn.cursor()
            data = reviewTextByStudentID(student_id)

            # Iterate over the list of tuples.
            for tuple_data in data:
                # Unpack each tuple
                completeness, efficiency, style, \
                    documentation, review = tuple_data

                # Store the desired string format
                string_format = (
                    f'\nCompleteness : {completeness}\n'
                    f'Efficiency   : {efficiency}\n'
                    f'Style        : {style}\n'
                    f'Documentation: {documentation}\n'
                    f'Review       : {review}'
                )
                print(f'{string_format}\n')
            headings = ['Completeness', 'Efficiency', 'Style',
                        'Documentation', 'Review']
        offerToStore(formatting(data, headings))

    # View course name by the teacher id
    elif command == 'lc':
        if usageIsIncorrect(user_input, 1):
            continue
        teacher_id = args[0]
        data = None
        with openDatabase('HyperionDev.db') as conn:
            cursor = conn.cursor()
            data = courseNameByTeacherID(teacher_id)
            headings = ['Subjects']
        tableFormat(data, headings)
        offerToStore(formatting(data, headings))

    # View the total number of students that have not completed their
    # courses
    elif command == 'lnc':
        data = None
        with openDatabase('HyperionDev.db') as conn:
            cursor = conn.cursor()
            data = incompleteStudents()
            headings = ['Student ID', 'First Name', 'Last Name',
                        'Email Address', 'Course']
        tableFormat(data, headings)
        offerToStore(formatting(data, headings))

    # View the total students who have completed their courses with
    # a mark lower than 30
    elif command == 'lf':
        data = None
        with openDatabase('HyperionDev.db') as conn:
            cursor = conn.cursor()
            data = studentCompletedBelow30()
            headings = ['Student ID', 'First Name', 'Last Name',
                        'Email Address', 'Course', 'Marks']
        tableFormat(data, headings)
        offerToStore(formatting(data, headings))

    elif command == 'e':
        print("\nProgramme exited successfully!\n")
        break

    else:
        print(f"Incorrect command: '{command}'")
