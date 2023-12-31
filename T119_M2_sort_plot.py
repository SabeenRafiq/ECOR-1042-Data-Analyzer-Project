# ECOR 1042 Lab 5 - Sort Plot
# Team Members: Sabeen Rafiq, Tim Lorange, Kristine Guldbrandsen, Mohammed Abusalih
# Student Numbers: Sabeen Rafiq [101258923], Tim Lorange [101257372],
#                  Kristine Guldbrandsen [101269181], Mohammed Abusalih [101203104]
# Submission Date: 02-12-2022

import matplotlib.pyplot as plt
from T119_M1_load_data import *
import numpy as np


# Function 1
# sabeen Rafiq, Tim Lorange, Kristine Guldbrandsen, Mohammed Abusalih
def student_list(stu_dict: dict) -> list:
    """
    Returns the values of the inputted dictonary as one list
    Precondion: None
    >>>student_list(load_data("student-mat.csv", "Age"))
    [{'School': 'GP', 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 
    10, 'G1': 7, 'G2': 8, 'G3': 10, 'Age': 15}, {'School': 'GP', 'StudyTime': 3, 'Failures': 0, 
    'Health': 5, 'Absences': 2, 'G1': 15, 'G2': 14, 'G3': 15, 'Age': 15}, ...]
    >>>student_list({})
    []
    """
    student_list = []
    key_set = set()
    for key in stu_dict.keys():
        key_set.add(key)
    if {'GP', 'MB', 'MS', 'CF', 'BD'} == key_set:
        dict_type = "School"
    if {1, 2, 3, 4, 5} == key_set:
        dict_type = "Health"
    if {15, 16, 17, 18, 19, 20, 21, 22} == key_set:
        dict_type = "Age"
    if {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} == key_set:
        dict_type = "Failures"

    for elem in stu_dict:

        for item in stu_dict[elem]:

            item[dict_type] = elem
            student_list.append(item)
    return student_list

# Function 2

# Kristine Guldbrandsen
def sort_students_bubble(dictionary: dict, attribute: str) -> list:
    """
    The function sort_students_bubble sorts the list of students by their attri
    bute.The schools are sorted by alphabetical order, while the other attribut
    es are sorted in ascending numerical order. The function will return a list 
    that is sorted with a students data in dictionaries. 
    
    Preconditions:
    The dictionary and the attribute has to be in the function load_data. 
    
    examples:
    
    {'School': 'BD', 'Age': 16, 'StudyTime': 1, 'Failures': 0, 'Absences': 0, 'G1': 6, 'G2': 0, 'G3': 0, 'Health': 3}, {'School': 'BD', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 0, 'G1': 7, 'G2': 0, 'G3': 0, 'Health': 3} (...)
    

    """
    # define variable
    student_info = student_list(dictionary)
    swap = True

    if type((student_info[0].get(attribute))) == str:
        while swap:
            swap = False
            # loop through the dictionary:
            for dic in range(len(student_info) - 1):
                    if student_info[dic].get(attribute) > student_info[dic + 1].get(attribute):
                        # bubble swaps the keys in the individual dictionaries
                        temp = student_info[dic]
                        student_info[dic] = student_info[dic + 1]
                        student_info[dic + 1] = temp
                        swap = True
    else:

        while swap:
            swap = False
            # loop through the dictionary:
            for dic in range(len(student_info) - 1):
                    if int(student_info[dic].get(attribute)) > int(student_info[dic + 1].get(attribute)):
                        # bubble swaps the keys in the individual dictionaries
                        temp = student_info[dic]
                        student_info[dic] = student_info[dic + 1]
                        student_info[dic + 1] = temp
                        swap = True
    return student_info

# Function 3
# Mohammed Abusalih

def sort_students_selection(student_dict: dict, sorting_key: str) -> list:
    """The function sorts the students using selection sort, the first input parameter will call a list of dictionaries using the load_data function, and the list will be sorted by the second input parameter(a key).

    >>>sort_students_selection('School','G1')
    [{'Age': '18', 'StudyTime': '2', 'Failures': '1', 'Health': '5', 'Absences': '8', 'G1': '3', 'G2': '5', 'G3': '5', 'School': 'BD'}, {'Age': '16', 'StudyTime': '1', 'Failures': '2', 'Health': '5', 'Absences': '0', 'G1': '4', 'G2': '0', 'G3': '0', 'School': 'MB'},...]
    >>>sort_students_selection('Failures','Age')
    [{'School': 'GP', 'Age': 15, 'StudyTime': 3, 'Health': 5, 'Absences': 2, 'G1': 15, 'G2': 14, 'G3': 15, 'Failures': 0}, {'School': 'GP', 'Age': 16, 'StudyTime': 2, 'Health': 5, 'Absences': 0, 'G1': 14, 'G2': 15, 'G3': 15, 'Failures': 0},...]
    """

    # Makes a list of student dictionaries
    student_info = student_list(student_dict)

    # Checks if the value of the key is an int
    if type(student_info[0].get(sorting_key)) == str:
        # Sorts the list using selction sort
        for i in range(len(student_info)):
            min_value = i
            for j in range(i + 1, len(student_info)):
                if student_info[min_value].get(sorting_key) > student_info[j].get(sorting_key):
                    min_value = j
                student_info[i], student_info[min_value] = student_info[min_value], student_info[i]
    else:
        for i in range(len(student_info)):
            min_value = i
            for j in range(i + 1, len(student_info)):
                if int(student_info[min_value].get(sorting_key)) > int(student_info[j].get(sorting_key)):
                    min_value = j
                student_info[i], student_info[min_value] = student_info[min_value], student_info[i]

    return student_info

# Function 4
  # Sabeen Rafiq
def histogram(stu_dict: dict, attribute: str) -> None:
    """
    Plots a histogram for the attribute inputted based on the data 
    inputted from the inputted dictonary
    Preconidions: None
    >>> histogram(load_data("student-mat.csv", "Age"), "Health")
    #Plots Histogram of Health vs. Number of Students, Return None
    """
    student_info = student_list(stu_dict)

    dict_of_keys = {}
    list_of_keys = []

    for i in range(len(student_info)):
        list_of_keys.append(student_info[i].get(attribute))

    for key in list_of_keys:
        dict_of_keys[key] = 0

    for i in range(len(student_info)):
        for x in list(dict_of_keys.keys()):
            if student_info[i].get(attribute) == x:
                dict_of_keys[x] = dict_of_keys.get(x) + 1

    fig1 = plt.figure()
    plt.title(attribute + " vs. Student Data Histogram")
    plt.xlabel(attribute)
    plt.ylabel('Number Of Students')

    x = list(dict_of_keys.keys())
    y = list(dict_of_keys.values())

    plt.bar(x, y, color='purple', edgecolor="black")
    plt.show()

# Function 5
# Tim Lorange
def curve_fit(stu_dict: dict, attr: str, order: int) -> list:
    """
    Given a dictionary load_data, an attribute from the student information in 
    the dictionary and and order (degree) of a polynomial. In the function it 
    will calculate the average grade for each student. Returns the coefficients 
    for a polynomial with given degree, x-axis of all integer values of the 
    attribute and y-axis is the average of G_avg.
    
    precondition: 1 <= order <= 5, attr != "School", stu_dict must be from the
    load_data module
    
    >>>curve_fit(load_data("student-mat.csv", "School"),"Failures",5)
    [-0.0, 0.355, -2.735, 11.36]
    >>>curve_fit(load_data("student-mat.csv", "School"),"Failures",1)
    [-1.67, 11.005]
    >>>curve_fit(load_data("student-mat.csv", "Health"),"StudyTime",3)
    [-0.35833, 2.66, -5.28167, 13.23]
    """
    g_avg = add_average(stu_dict)
    # calculates and adds G_Avg to every student in the dictionary
    stu_list = student_list(g_avg)
    # turns the new dictionary into a list of student
    key_set = set()
    for i in stu_list:
        key_set.add(i[attr])
    # puts values for the attribute into a set
    y = []
    for key in key_set:
        g_avg_sum = 0
        num_stu = 0
        for stu_info in stu_list:
            if stu_info[attr] == key:
                g_avg_sum += stu_info["G_Avg"]
                num_stu += 1

        y += [round((g_avg_sum / num_stu), 2)]
    # finds the average of G_Avg for each value of the given attribute
    keys = []
    for i in key_set:
        keys += [i]
    # coverts the set into a list
    x = keys
    if order > len(x):
        order = len(x) - 1
        coef = tuple(np.polyfit(x, y, order))
    else:
        coef = tuple(np.polyfit(x, y, order))

    # calculates the coefficient for the polynomial
    return coef


# main script

if __name__ == '__main__':

    # Function 1
    student_list(load_data("student-mat.csv", "Age"))

    # Function 2
    sort_students_bubble(load_data("student-mat.csv", "Health"), "Age")

    # Function 3
    sort_students_selection(load_data('student-mat.csv', 'Health'), 'G1')

    # Function 4
    histogram(load_data("student-mat.csv", "Age"), "School")

    # Function 5
    curve_fit(load_data("student-mat.csv", "School"), "Failures", 5)

