# ECOR 1042 Lab 6 - batch ui
# Name: Tim Lorange [10125737], Mohammed Abusalih [101203104]
# Submission Date: 09-12-2022

# Tim Lorange
# 10125737
from T119_M1_load_data import load_data
from T119_M2_curve_fit import curve_fit
from scipy.optimize import fminbound
import numpy as np
import matplotlib.pyplot as plt

def maximum(stu_dict: dict, attr: str) -> int:
  """
  Takes a student dictionary and an attribute and returns the value of that attribute with the highest average grade averages and the value of the average grade average of that attribute value.
  precondition: must be one of the 10 student attributes and student dict must be one of the 4 student dictionarys
  >manimum(load_data("student-mat.csv", "Health"), "Age")
  (16.892768697374986, 11.152631879584394)
  >manimum(load_data("student-mat.csv", "Failures"), "Health")
  (1.000005628673589, 11.8485647971968)
  """
  coef, min_max = curve_fit(stu_dict, attr, 2)
  maximum, minimum = min_max

  def min_curve_function(x):
      # solves for points reflected on the x-axis
      return -np.polyval(coef, x)

  x_max = fminbound(min_curve_function, minimum, maximum)
  y_max = np.polyval(coef, x_max)

  return (x_max, y_max)

# Mohammed Abusalih 
#101203104
def minimum(stu_dict: dict, attr: str) -> tuple:
  """
  Takes a student dictionary and an attribute and returns the       value of that attribute with the lowest average grade averages    and the value of the average grade average of that attribute      value.
  precondition: must be one of the 10 student attributes and        student dict must be one of the 4 student dictionarys
  >minimum(load_data("student-mat.csv", "Health"), "Age")
  (21.99999391225472, 8.017924139731878)
  >minimum(load_data("student-mat.csv", "Failures"), "Health")
  (3.686319218241047, 10.2661375290833)
  """
  # Calls the curve_fit function
  coef, min_max = curve_fit(stu_dict, attr, 2)
  maximum, minimum = min_max
  # returns a funtion with one input
  def min_curve_function(x):
      return np.polyval(coef, x)
  # Finds the minimum point in the curve
  x_g_min = fminbound(min_curve_function, minimum, maximum)
  y_g_min = np.polyval(coef, x_g_min)

  return x_g_min, y_g_min
