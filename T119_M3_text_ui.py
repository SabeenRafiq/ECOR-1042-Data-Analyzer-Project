# ECOR 1042 Lab 6 - T119_M3_text_ui.py
# Team Members: Sabeen Rafiq [101258923]
# Submission Date: 08-12-2022

from T119_M3_optimization import minimum, maximum
from T119_M1_load_data import load_data, add_average
from T119_M2_sort_plot import *

def get_command() -> str:
    """
    Return user input and display text ui 
    Example:
    get_command()
    The available commands are:
    1. L)oad Data
    2. S)ort Data
         'School' 'Age' 'StudyTime' 'Failures' 'Health'
         'Absences' 'G1' 'G2' 'G3' 'G_Avg'
    3. H)istogram
         'School' 'Age' 'StudyTime' 'Failures' 'Health'
         'Absences'
    4. W)orst _____ for Grades
         'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
    5. B)est _____ for Grades
         'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
    6. Q)uit
    Please type your command: L
    """
    print("""The available commands are:
    1. L)oad Data
    2. S)ort Data
         'School' 'Age' 'StudyTime' 'Failures' 'Health'
         'Absences' 'G1' 'G2' 'G3' 'G_Avg'
    3. H)istogram
         'School' 'Age' 'StudyTime' 'Failures' 'Health'
         'Absences'
    4. W)orst _____ for Grades
         'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
    5. B)est _____ for Grades
         'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
    6. Q)uit""")

    # Get and Return user input for command
    user_input = input("Please type your command: ")
    return user_input

def loaded_data() -> dict:
    """
    Loads data given file name and attribute from user 
    Example: 
    loaded_data()
    Please enter the name of the file: student-mat.csv
    Please enter the attribute to use as key: Age
    Data Loaded
    
    loaded_data()
    Please enter the name of the file: student-mat.csv
    Please enter the attribute to use as key: averages
    Invalid attribute
    Please enter the attribute to use as key: G_Avg
    Data Loaded
    """
    # define set with all valid attributes to load data with
    valid_attribute = {'School', 'Age', 'StudyTime', 'Failures', 'Health',
             'Absences', 'G1', 'G2', 'G3', 'G_Avg'}

    # Get file name and key from user
    file_name = input("Please enter the name of the file: ")
    key = input("Please enter the attribute to use as key: ")

    # Only contuniue with code when attribute is in the valid attributes options
    while key not in valid_attribute:
        print("Invalid attribute")
        key = input("Please enter the attribute to use as key: ")

    # load the data
    loaded_data = add_average(load_data(file_name, key))

    # Notify the user
    print("Data Loaded")

    # Return the loaded data
    return loaded_data

def print_format(attribute: str) -> str:
    """
    Return a string with appropriate formatting depending on input string
    print_format("Age")
    Age years old
    """
    if attribute == "Age":
        attribute = str(attribute) + " years old"
    elif attribute == "StudyTime":
        attribute = str(attribute) + " hours"
    elif attribute == "Failures":
        attribute = str(attribute) + " failures"
    elif attribute == "Health":
        attribute = "a health of " + str(attribute)
    else:
        attribute = str(attribute) + " Absences"
    return attribute

def execute_command(command: str, loaded_data: dict) -> None:

    # Define valid attributes for sorting data and getting worst/best grades
    valid_attribute = {'School', 'Age', 'StudyTime', 'Failures', 'Health',
             'Absences', 'G1', 'G2', 'G3', 'G_Avg'}
    valid_attribute_grade = {'Age', 'StudyTime', 'Failures', 'Health',
             'Absences'}
    valid_att_hist = {'School', 'Age', 'StudyTime', 'Failures', 'Health',
             'Absences'}
    
     # Ensure data is loaded
    if loaded_data == {}:
        print("File not loaded. Please, load a file first.")
        return
    
    # If command is to sort data:
    if command == 'S' or command == 's':
        
        # define variables
        sort_attribute = ""

        # ensure attribute for sorting is valid
        while sort_attribute not in valid_attribute:
            sort_attribute = input("""Please enter the attribute you want to use for sorting: 
'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
'G1' 'G2' 'G3' 'G_Avg': """)

        # sort the data
        sorted_data = sort_students_bubble(loaded_data, sort_attribute)        

        # Ask user to show data or not
        display_data = input(
            "Data Sorted. Do you want to display the data?: ")

        # Show data if wanted
        if display_data == "Y" or display_data == 'y':
            print(sorted_data)
         
    # If command Histogram
    elif command == 'H' or command == 'h':
        # Define variables
        histogram_att = ''

        # Ensure attribute is valid
        while histogram_att not in valid_att_hist:
            histogram_att = input("""Please enter the attribute you want to use for the histogram: 
'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences': """)

        # Make and plots histogram
        histogram(loaded_data, histogram_att)

    # If command Worst Grade
    elif command == 'W' or command == 'w':
        # Define variables
        worst_grade_att = ''

        # Ensure attribute is valid
        while worst_grade_att not in valid_attribute_grade:
            worst_grade_att = input("""Please enter the attribute you want to calculate the worse value of the attribute for in terms of grades:
'Age' 'StudyTime' 'Failures' 'Health' 'Absences': """)

        # Get worst grade
        worst_grade = minimum(worst_grade_att)

        # gets appropirate string for output
        print_format(worst_grade_att)

        # print worst grade
        print("The worst value for the attribute {0} is {1}".format(
            worst_grade_att, worst_grade))

    # If command Worst Grade
    elif command == 'B' or command == 'b':
        # Define variables
        best_grade_att = ''

         # Ensure attribute is valid
        while best_grade_att not in valid_attribute_grade:
            
            best_grade_att = input("""Please enter the attribute you want to calculate the best value of the attribute for in terms of grades:
'Age' 'StudyTime' 'Failures' 'Health' 'Absences': """)

        # get best grade
        best_grade = maximum(best_grade_att)

        # gets appropirate string for output
        print_format(best_grade_att)

        # print best grade
        print("The best value for the attribute {0} is {1}".format(
            best_grade_att, best_grade))

# Define variables
data = {}

# Get command from user (and shows UI)
command = get_command()

# Define valid commands
valid_command = {"Q", "q", "S", 's', "H", 'h', "W", 'w', "B", 'b', "L", "l"}

# While loop:
while True:
    # Load data
    if command == 'L' or command == 'l':
        data = loaded_data()
    # Quit program
    elif command == 'Q' or command == 'q':
        break
    # Notify the user of the invalid command
    elif command not in valid_command:
        print("Invalid command")
    # Execute command (if not L)
    else:
        set_return = execute_command(command, data)
    # Show user interface again ...
    command = get_command()
