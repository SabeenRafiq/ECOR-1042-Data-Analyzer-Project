# Timothy Lorange
# 101257372
from T119_M1_load_data import load_data, add_average
import matplotlib.pyplot as plt
import numpy as np
from T119_M2_sort_plot import student_list

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
    return coef, (max(keys), min(keys))


curve_fit(load_data("student-mat.csv", "School"), "Age", 2)
curve_fit(load_data("student-mat.csv", "Health"), "StudyTime", 3)
curve_fit(load_data("student-mat.csv", "Age"), "G1", 4)
curve_fit(load_data("student-mat.csv", "Failures"), "G2", 2)
