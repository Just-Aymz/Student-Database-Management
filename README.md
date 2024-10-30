# **Database Management Project**
This project focuses on creating and interacting with a SQL database to manage and query data efficiently. Using Python, the database is accessed for various tasks, including inserting data, querying with specified parameters, and exporting query results to XML or JSON formats. This README provides details on the structure, setup, and usage of the project.

# **Table of Contents**
1. [Project Structure](#project-structure)
2. [Setup Instructions](#setup-instructions)
3. [Usage](#usage)
4. [Functions Review](#functions-review)
5. [Additional Notes](#additional-notes)
6. [License](#license)

# **Project Structure**
create_database.sql: Defines the SQL database structure and tables, and includes initial SQL commands to create tables and set up the database schema.
capstone_project.py: The main Python script to interact with the SQL database. It includes functions for querying data, formatting and saving output, and a command-line interface for user interaction.

# **Setup Instructions**

1. **Database Creation**:

  * Run the create_database.sql script to set up the database structure. This script defines tables and relationships necessary for the database.

2. **Python Environment**:
  * Ensure Python 3.x is installed with sqlite3, tabulate, and xml.etree.ElementTree.
  * Install any additional dependencies (if not available) using:
  ```
  pip install tabulate
  ```

3. Database File:
* The database file should be named HyperionDev.db and located in the same directory as the scripts for easy access. This name is specified within the Python script.


# **Usage**
**Running the Script**
  1. **Main Interaction (capstone_project.py)**:
  * Run capstone_project.py to interact with the database.
  * The script offers options to view and query specific data by typing commands, such as:
    * ```vs <student_id>```: View subjects taken by a student.
    * ```la <firstname> <surname>```: Lookup address by student name.
    * ```lr <student_id>```: List reviews for a given student.
    * ```lnc```: List students who haven't completed their course.
    * ```lf```: List students who completed their course with a mark ≤ 30.
**Saving Data**
The capstone_project.py script prompts the user to save query results in JSON or XML format. Simply enter a filename with the .json or .xml extension when prompted.

# **Functions Overview**
**capstone_project.py**
  * **formatting**: Converts query results into a list of dictionaries for structured output.
  * **storeDataAsJSON & storeDataAsXML**: Saves query results as JSON or XML.
  * **tableFormat**: Formats and displays query results in a readable table format.
  * **openDatabase**: Context manager for connecting to the SQLite database.
  * **Multiple Query Functions**: Various functions, such as courseNameByCourseCode, addressByNameAndSurname, and studentCompletedBelow30, handle specific queries.

# **Additional Notes**
* **Error Handling**: The script includes error handling for database connectivity and user input validation.
* **File Extensions**: Ensure that exported files have the correct .json or .xml extensions when saving data.

# **License**
This project is open-source under the MIT License. See LICENSE for more details.

