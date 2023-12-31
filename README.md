# README File
## General Information
>**Contact Information**

**Name**: Sabeen Rafiq 

**Email**: sabeenrafiq@cmail.carleton.ca
>**Software Information**

**Software Name**: Student Database Version 1.0

**Date**: December 9th, 2022

>License

Copyright (c) .NET Foundation and Contributors
All rights reserved.
# About the Software
>T119_M1_load_data.py
- Use T119_M1_load_data.py file to load, sort and add averages to student data
>T119_M2_sort_plot.py
- Use T119_M2_sort_plot.py file to sort student data by various attributes, make a histogram of data or get the coefficients for a polynomial comparing the grade averages and attributes of the students. 
>T119_M3_optimization.py
- Use T119_M3_optimization.py to find the local minimum and maximum of a polynomial that represents the grade averages and attributes of the students
>T119_text_ui.py
- Use T119_text_ui.py to use an interactive interance to load, sort and represent data. It is also able to find the local minimum and maximum of a polynomial that represents the grade averages and attributes of the students, along with the coeffiecents for said polynomial.
>T119_batch_ui.py
- Use T119_batch_ui.py to read commands from a file to load, sort and represent data. It is also able to find the local minimum and maximum of a polynomial that represents the grade averages and attributes of the students, along with the coeffiecents for said polynoimal.

# Installation
>Python and Wing 101 8
- A ide with the capability to read and run python files must be downloaded. For this software Wing 101 8 was installed by going to [https://wingware.com/](https://wingware.com/) and installing the appropriate version of wing for your computer. Then the latest version of python must also be downloaded. The appropriate version for your laptop must be installed from [https://www.python.org/downloads/](https://www.python.org/downloads/). 
>Pip, Matplotlib, NumPy and SciPy

>To install pip type the following commands into the command prompt:
- python -m pip install -U pip
- python --version
- pip -V

>To install Matplotlib, NumPy and SciPy type the following commands into the command prompt:
- pip install matplotlib
- pip install numpy
- pip install scipy

# Usage
>python User interface (UI)

When prompted, input a command corresponding to the way you want the data manipulated. The commands that are valid are L)oad data, S)ort data, B)est, W)orst and Q)uit.
The command load data must be called before any other command can be carried out.
When done the command quit will end the program.
>Python Batch User Interface
>
When prompted, input the name of the text files containing the commands corresponding to how the user wants the data to be manipulated. The commands that are valid are L)oad data, S)ort data, B)est, W)orst and Q)uit. 
The format of the text file must be one “full command” per line separated by semi-colons.
The command load data must be the first command in the text file before any other command can be carried out.
When done the command quit will end the program.
>Python User Interface Load
>
When prompted, input “L” or “l”, it will tell the user to input the file name, which is “student-mat.csv” and then it will ask for the attribute that the data will be sorted/called by. The attributes available for this command are “School”, “Health”, “Age” and “Failures”.
The program will then inform the user that the data has been successfully loaded
If the attribute is not correct the code will notify the user and prompt the user to try again
The data must be loaded before the user can input any of the other commands
>Python User interface Sort data
>
When prompted, input “S” or “s” to carry out the sort data command, then it will prompt the user to input the attribute that the data is going to be sorted by. This can be one of the ten attributes: “School”, “StudyTime”, “Failures” “Age”, “Health”, “Absences”, “G1”, “G2”, “G3” or “G_Avg”. After the user will Input whether they want the sorted data to be displayed with “Y” for yes and “N” for no.
The data must be loaded first using the load data function. If data is not loaded it will prompt the user to load data.
>Python User Interface Best
> 
When prompted, input “B” or “b”, it will tell the user to input an attribute and then return the value of that attribute for which the students have the best average of grade averages. The attributes available for this command are “School”, “StudyTime”, “Failures” “Age”, “Health”, “Absences”, “G1”, “G2”, “G3” or “G_Avg”.
The data must be loaded before the user can call this command. If the data is not loaded the program will inform the user and prompt them to load the data.
It will return a tuple with the first number being the value of the input attribute that has the highest average of the grade average, and the second number will be the average of the grade average.
>Python User Interface Worst
>
When prompted, input “W” or “w”, it will tell the user to input an attribute and then return the value of that attribute for which the students have the best average of grade averages. The averages available for this command are “School”, “StudyTime”, “Failures” “Age”, “Health”, “Absences”, “G1”, “G2”, “G3” or “G_Avg”.
The data must be loaded before the user can call this command. If the data is not loaded the program will inform the user and prompt them to load the data.
It will return a tuple with the first number being the value of the input attribute that has the lowest average of the grade average, and the second number will be the average of the grade average.

# Credits
>T119_M1_load_data.py
- Sabeen Rafiq: student_school_dictionary, student_list, get_G_Avg, get_dict_len, check_key, test_4
- Kristine Guldbrandsen: student_age_dictionary
- Tim Lorange:student_health_dictionary, student_list, individual_student_entries
- Mohammed Tarig: student_failures_dictionary, size_of_the_lists
- Collaboratively: load_data, add_average
  
>T119_M2_sort_plot.py 
- Sabeen Rafiq: histogram
- Kristine Guldbrandsen: sort_students_bubble
- Tim Lorange: curve_fit
- Mohammed Tarig: sort_students_selection
- Collaboratively: student_list
  
>T119_M3_optimization.py 
- Tim Lorange: maximum, min_curve_function
- Mohammed Tarig: minimum, min_curve_function
  
>T119_text_ui.py
- Sabeen Rafiq: get_command, loaded_data, print_format, execute_command
  
>T119_batch_ui.py
- Kristine Guldbrandsen: loaded_data, print_format, execute_command
