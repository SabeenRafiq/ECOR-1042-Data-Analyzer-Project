# ECOR 1042 Lab 6 - batch ui
# Name: Kristine Guldbrandsen
# Student Number: 101269181
# Submission Date: 09-12-2022

from T119_M3_optimization import *
from T119_M1_load_data import load_data, add_average
from T119_M2_sort_plot import * 


def loaded_data(file_name, key):
  """
  the function loaded_data takes a file as an input and execute the commands in them.
  It also returns a histogram with the data inputted.
  
  examples:
  
  Please enter the name of the file where your commands are sorted: user_file.txt
  Data Loaded
  Data Sorted
  The best value for the attribute Age is 100
  The worst value for the attribute Health is 0
  + a histogram
  """
  # set with all valid attributes to load data
  valid_attribute = {'School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2',
    'G3', 'G_Avg'}

  # Only continue when attribute is in the valid attributes options
  while key not in valid_attribute:
    return

  # load the data
  loaded_data = add_average(load_data(file_name, key))

  # Notify user
  print("Data Loaded")

  # Return loaded data
  return loaded_data


def print_format(attribute: str) -> str:
  """
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


def execute_command(command: str, loaded_data: dict):
  """
  """
  # Define valid attributes for sorting data and getting worst/best grades
  valid_attribute = {'School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2',
    'G3', 'G_Avg'}
  
  valid_attribute_grade = {'Age', 'StudyTime', 'Failures', 'Health', 'Absences'}
  
  valid_att_hist = {'School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences'}

  # Ensure data is loaded
  if loaded_data == {}:
    print("File not loaded. Please, load a file first.")
    return

  # checks if lines in the list from file is s or S:
  if command[0] == 'S' or command[0] == 's':


    # ensure attribute for sorting is valid
    sort_attribute = command[1]
    if sort_attribute not in valid_attribute:
      print('input for attribute not valid.')
      return

    # sort the data
    sorted_data = sort_students_bubble(loaded_data, sort_attribute)
    print('Data Sorted') 
    # connect display_data to what is inside list
    display_data = command[2]

    # Show data if wanted
    if display_data == "Y" or display_data == 'y':
      print(sorted_data)

  # If line in list command Histogram
  elif command[0] == 'H' or command[0] == 'h':
    # Define variables
    histogram_att = ''

    # Ensure attribute is valid
    while histogram_att not in valid_att_hist:
      histogram_att = command[1]

    # Make and plots histogram
    histogram(loaded_data, histogram_att)

  # If line in list command Worst Grade
  elif command[0] == 'W' or command[0] == 'w':
    # Define variables
    worst_grade_att = ''

    # Ensure attribute is valid
    while worst_grade_att not in valid_attribute_grade:
      worst_grade_att = command[1]

    # Get worst grade
    worst_grade = minimum(worst_grade_att)

    # gets appropirate string for output
    print_format(worst_grade_att)

    # print worst grade
    print("The worst value for the attribute {0} is {1}".format(
      worst_grade_att, worst_grade))

  # If first part of list is b or B
  elif command[0] == 'B' or command[0] == 'b':
    # Define variables
    best_grade_att = ''

    # Ensure attribute is valid
    while best_grade_att not in valid_attribute_grade:

      best_grade_att = command[1]
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

# Define valid commands
valid_command = {"Q", "q", "S", 's', "H", 'h', "W", 'w', "B", 'b', "L", "l"}

commands_sorted = input('Please enter the name of the file where your commands are sorted: ')


file = open(commands_sorted, "r")  

for line in file:
  line = line.strip().split(';')
  # Load data
  if line[0] == 'L' or line[0] == 'l':
    data = loaded_data(line[1], line[2])
  # Quit program
  elif line[0] == 'Q' or line[0] == 'q':
    break
  # Notify the user of the invalid command
  elif line[0] not in valid_command:
    print("Invalid command")
  # Execute command (if not L)
  else:
    set_return = execute_command(line, data)
    
file.close()