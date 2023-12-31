# ECOR 1042 Lab 3 - Load Data
# Team Members: Sabeen Rafiq, Tim Lorange, Kristine Guldbrandsen, Mohammed Abusalih
# Student Numbers: Sabeen Rafiq [101258923], Tim Lorange [101257372],
#                  Kristine Guldbrandsen [101269181], Mohammed Abusalih [101203104]
# Submission Date: 18-11-2022

import string
from typing import List
from check_equal import check_equal

#Sabeen Rafiq
def student_school_dictionary(file_name: str) -> dict:
    """
    Description: Returns the content of a file contaning student's information 
    sorted by the student's school's intials
    Precondition: file_name == 'student-mat.csv'
    Example: 
    student_school_dictionary('student-mat.csv')
    >>>{'GP': [{'Age': '18', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}, {another student's data} ...], 
    'MB': [{'Age': '16', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 
    'Absences': '12', 'G1': '5', 'G2': '5', 'G3': '5'}, {another student's data}, ... ], 
    , 'Another school' : [{}] ... } 
    
    Repeated for each school in the file. 
    Overall dictionary contains all student information stored in file
    """

    # define varaibles
    sorted_stu_info = {}
    school_indiv_stu_info = []
    indiv_stu_info = {}
    prev_line = []

    # open file
    all_stu_info = open(file_name, "r")

    # create counter to count which line of the file is being read
    line_num = 0

    # iterate through each line of the file
    for line in all_stu_info:

        # remove any white space and \n from each line of the document
        # split each line into a list creating a new element between each ','
        line = line.strip().split(",")

        # create list of info types in 1st line doc ('Age', 'Health'...)
        if line_num == 0:
            info_type = line.copy()

        else:
            if line_num == 1:
                # set previous line's intinal value to the 1st school on the list
                # to ensure the student data for the 1st school is accounted for (line 48)
                prev_line[0] = line[0]

            # create dictonary that stores the data for one student
            # not including School (1st elem in line) {info_type : value}
            for x in range(1, len(line)):
                indiv_stu_info[info_type[x]] = int(line[x])

            # Check if school of current line is the same as previous line
            # if so add the indiv student infomation to a list for the same school
            # else reset to []
            if prev_line[0] != line[0]:
                school_indiv_stu_info = []

            # Create list contating all student infomation dict for one school
            school_indiv_stu_info.append(indiv_stu_info)

            # reset indiv_stu_info to blank for new student
            indiv_stu_info = {}

            # create dictonary contaning {school: school_indiv_stu_info}
            sorted_stu_info[line[0]] = school_indiv_stu_info

        # add one to number of lines from file read
        line_num += 1

        # set previous line to the line that was read
        prev_line = line.copy()

    # close file
    all_stu_info.close()

    # return sorted infomation
    return sorted_stu_info

#Tim Lorange
def student_health_dictionary(file_name: str) -> dict:
    """
    When given the file name of the data in student-mat.cvs returns a 
    dictionary where the health is the key and the values are lists of dicts 
    with keys of str to identify the data.
    precondition: must only have 9 attributes 
    student_health_dictionary('student_mat.csv')
    >>>{ 1 : [ {'School':'GP', 'Age': 17, 'StudyTime': 4.2, 'Failures': 3,
    'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10 },
    {another element},
    … ],
    2 : [ {'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1,
    'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7},
    {another element},
    … ],
    … }

    """
    infile = open(file_name, 'r')

    data_list = []
    for line in infile:
        # splits attribute values into a list
        line = line.strip().split(",")
        data_list.extend(line)

    attr_list = data_list[:9]
    for value in attr_list:
        # removes attribute names from the begining of data_list
        data_list.remove(value)

    for data_i in range(0, len(data_list), 9):
        # transforms everything but school name into a int
        for repeat in range(8):
            data_i += 1
            data_list[data_i] = int(data_list[data_i])

    student_health_dict = {}
    health1 = []
    health2 = []
    health3 = []
    health4 = []
    health5 = []

    for dict_num in range(len(data_list) // 9):
        temp_dict = {}
        for i in range(9):
            if i != 4:
                temp_dict[attr_list[i]] = data_list[dict_num * 9 + i]
        if data_list[dict_num * 9 + 4] == 1:
            health1.append(temp_dict)
        elif data_list[dict_num * 9 + 4] == 2:
            health2.append(temp_dict)
        elif data_list[dict_num * 9 + 4] == 3:
            health3.append(temp_dict)
        elif data_list[dict_num * 9 + 4] == 4:
            health4.append(temp_dict)
        else:
            health5.append(temp_dict)

    student_health_dict[1] = health1
    student_health_dict[2] = health2
    student_health_dict[3] = health3
    student_health_dict[4] = health4
    student_health_dict[5] = health5
    infile.close()
    return student_health_dict


#Kristine Guldbrandsen
def student_age_dictionary(file_name: str) -> dict:
    """
    The code returns a dictionary with age as a key. Student ages ranges from 
    15-22.Each key contains a list with more dictionaries with each students
    information. 
  
    preconditions:
    the index of the header will not be 1 and should therefore not be included 
    in the lists. That is because age has 1 as an index and we want it to be 
    the key.
  
    examples: 
    student_age_dictionary('student-mat.csv')
    >>>{ 15 : [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3,
    'Health': 3, 'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10},
    {another element},
    … ],
    16 : [ {'School': 'MS', 'StudyTime': 1, 'Failures': 1.2,
    'Health': 4, 'Absences': 10, 'G1': 9, 'G2': 11, 'G3': 7},
    {another element},
    … ],
  
    this will continue to 22. 


    """
    # open file with information that is going to be sorted
    datafile = open(file_name, 'r')

    # make empty list
    file_list = []
    for lines in datafile:
        # splits the different attributes into a list at commas, and removes any spaces and new lines
        lines = lines.strip().split(",")

        # adds specific elements to end of list
        file_list.extend(lines)

    category_list = file_list[:9]

    for number in category_list:
        # will delete any attribute names on top of list
        file_list.remove(number)

    for data_a in range(0, len(file_list), 9):
    #  changes all except for age to an integer
        for repeat in range(8):
            data_a += 1            # loop through whole list one by one
            file_list[data_a] = int(file_list[data_a])

    # make empty lists and a dictionary for to store information of the students
    student_age_dict = {}
    age15 = []
    age16 = []
    age17 = []
    age18 = []
    age19 = []
    age20 = []
    age21 = []
    age22 = []

    for dict_num in range(len(file_list) // 9):
        temp_dict = {}
        for i in range(9):
            if i != 1:
                    temp_dict[category_list[i]] = file_list[dict_num * 9 + i]
        if file_list[dict_num * 9 + 1] == 15:
            age15.append(temp_dict)
        elif file_list[dict_num * 9 + 1] == 16:
            age16.append(temp_dict)
        elif file_list[dict_num * 9 + 1] == 17:
            age17.append(temp_dict)
        elif file_list[dict_num * 9 + 1] == 18:
            age18.append(temp_dict)
        elif file_list[dict_num * 9 + 1] == 19:
            age19.append(temp_dict)
        elif file_list[dict_num * 9 + 1] == 20:
            age20.append(temp_dict)
        elif file_list[dict_num * 9 + 1] == 21:
            age21.append(temp_dict)
        else:
            age22.append(temp_dict)

    # add dictionary found above to empty lists
    student_age_dict[15] = age15
    student_age_dict[16] = age16
    student_age_dict[17] = age17
    student_age_dict[18] = age18
    student_age_dict[19] = age19
    student_age_dict[20] = age20
    student_age_dict[21] = age21
    student_age_dict[22] = age22

    datafile.close()
    return student_age_dict

#Mohammed Abusalih
def student_failures_dictionary(file_name: str) -> dict:
    """
    Returns a dictionary of student information with the key being the number of failures ranging from 0 to 10.
    Preconditions:file_name == 'student-mat.csv'

    >>>student_failures_dictionary('student-mat.csv')
    {0: [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6},...(other student info)],
    1: {'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6},...(other student info)],
    2:[...], ...}

    """
    # Opens file
    infile = open(file_name, 'r')

    student_info = []
    for line in infile:
        # Removes all spaces and turns values into a list.
        line = line.strip().split(",")
        student_info.extend(line)

    attr_list = student_info[:9]
    for value in attr_list:
        student_info.remove(value)

    for i in range(0, len(student_info), 9):
        for x in range(8):
            i += 1
            # Converst all data(except 'School') into "int" type
            student_info[i] = int(student_info[i])

    student_failures_dict = {}
    
    # Empty lists to populate with data with corresponding 'Failure' values.
    failures0 = []
    failures1 = []
    failures2 = []
    failures3 = []
    failures4 = []
    failures5 = []
    failures6 = []
    failures7 = []
    failures8 = []
    failures9 = []
    failures10 = []

    # Loop adds student data to the list with corresponding 'Failure' values.
    for dict_num in range(len(student_info) // 9):
        temp_dict = {}
        for i in range(9):
            if i != 3:
                temp_dict[attr_list[i]] = student_info[dict_num * 9 + i]
        if student_info[dict_num * 9 + 3] == 0:
            failures0.append(temp_dict)
        elif student_info[dict_num * 9 + 3] == 1:
            failures1.append(temp_dict)
        elif student_info[dict_num * 9 + 3] == 2:
            failures2.append(temp_dict)
        elif student_info[dict_num * 9 + 3] == 3:
            failures3.append(temp_dict)
        elif student_info[dict_num * 9 + 3] == 4:
            failures4.append(temp_dict)
        elif student_info[dict_num * 9 + 3] == 5:
            failures5.append(temp_dict)
        elif student_info[dict_num * 9 + 3] == 6:
            failures6.append(temp_dict)
        elif student_info[dict_num * 9 + 3] == 7:
            failures7.append(temp_dict)
        elif student_info[dict_num * 9 + 3] == 8:
            failures8.append(temp_dict)
        elif student_info[dict_num * 9 + 3] == 9:
            failures9.append(temp_dict)
        else:
            failures10.append(temp_dict)
            
    # Adds each list with the student data to the dictionary.
    student_failures_dict[0] = failures0
    student_failures_dict[1] = failures1
    student_failures_dict[2] = failures2
    student_failures_dict[3] = failures3
    student_failures_dict[4] = failures4
    student_failures_dict[5] = failures5
    student_failures_dict[6] = failures6
    student_failures_dict[7] = failures7
    student_failures_dict[8] = failures8
    student_failures_dict[9] = failures9
    student_failures_dict[10] = failures10
    
    # Closes file
    infile.close()
    
    return student_failures_dict


#Sabeen Rafiq, Tim Lorange, Mohammed Abusalih, Kristine Guldbrandsen

def load_data(file_name: str, key: str) -> dict:
    """
    Description: Returns a dictonary with sorted student data by inputted 
    attribute (key)
    Precondtion: None
    Example: 
    load_data('student-mat.csv', 'School')
    >>>{'GP': [{'Age': '18', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}, {another student's data} ...], 
    'MB': [{'Age': '16', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 
    'Absences': '12', 'G1': '5', 'G2': '5', 'G3': '5.0'}, {another student's data}, ... ], 
    , 'Another school' : [{}] ... } 
    
    Repeated for each school in the file. 
    Overall dictionary contains all student information stored in file
    
    """
    # if-elif-else statments to call the apporiate function to sort the
    # inputted file by the desired key / attribute
    if key == 'School':
        return student_school_dictionary(file_name)
    elif key == 'Health':
        return student_health_dictionary(file_name)
    elif key == 'Age':
        return student_age_dictionary(file_name)
    elif key == 'Failures':
        return student_failures_dictionary(file_name)
    else:
        print('Invalid Key')
        return {}
#Sabeen Rafiq, Tim Lorange, Mohammed Abusalih, Kristine Guldbrandsen
def add_average(stu_dict: dict) -> dict:
    """
    Description: adds the average of G1 G2 and G3 to an inputted dictonary (G_Avg)
    Precondtion: stu_dict must include minimum 1 element
    Example: 
    add_average(load_data('student-mat.csv', 'School'))
    >>> {'GP': [{'Age': '18', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 
    'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6', 'G_Avg': '5.67'}, {another student's data} ...], 
    'MB': [{'Age': '16', 'StudyTime': '2', 'Failures': '0', 'Health': '3', 
    'Absences': '12', 'G1': '5', 'G2': '5', 'G3': '5', 'G_Avg': '5'}, {another student's data}, ... ], 
    , 'Another school' : [{}] ... } 
    
    Repeated for each school in the file. 
    Overall dictionary contains all student information stored in file
    
    """
    # define a new list
    new_list = []

    # loop to create one list containty a dictionary of every student's information
    for stu_info_key in stu_dict:
        # stu_info is every key in stu_dict
        new_list += stu_dict.get(stu_info_key)

    for i in range(len(new_list)):
        # get values of g1, g2 and g3 from each student's dictionary
        g1 = new_list[i].get('G1')
        g2 = new_list[i].get('G2')
        g3 = new_list[i].get('G3')

        # calculate the average of g11, g2, g3
        g_avg = round((int(g1) + int(g2) + int(g3)) / 3, 2)
        
        # add the average grade to each student's dictionary
        new_list[i].update({'G_Avg': g_avg})
        
    return stu_dict

#Sabeen Rafiq, Tim Lorange
def student_list(stu_dict: dict) -> list:
    student_list = []
    for elem in stu_dict:
        for item in stu_dict[elem]:
            student_list.append(item)
    return student_list


if __name__ == '__main__':

    # Test 1:
    test_passed_total = 0
    test_failed_total = 0

    print('Test #1: Ensure the Keys in a Dictionary are Correct\n')
    
    check_equal("Test #1: School Dictionary", set(load_data("student-mat.csv",
                'School').keys()), set({'GP', 'MB', 'CF', 'BD', 'MS'}))
    if set(load_data("student-mat.csv", 'School').keys()) == set({'GP', 'MB', 'CF', 'BD', 'MS'}):
        test_passed_total += 1

    check_equal("Test #1: Age Dictionary", set(load_data("student-mat.csv",
                'Age').keys()), set({15, 16, 17, 18, 19, 20, 21, 22}))
    if set(load_data("student-mat.csv", 'Age').keys()) == set({15, 16, 17, 18, 19, 20, 21, 22}):
        test_passed_total += 1

    check_equal("Test #1: Health Dictionary", set(load_data("student-mat.csv",
                'Health').keys()), set({1, 2, 3, 4, 5}))
    if set(load_data("student-mat.csv", 'Health').keys()) == set({1, 2, 3, 4, 5}):
        test_passed_total += 1    

    check_equal("Test #1: Failures Dictionary", set(load_data("student-mat.csv",
                'Failures').keys()), set({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
    if set(load_data("student-mat.csv", 'Failures').keys()) == set({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}):
        test_passed_total += 1        

    test_passed_failed = 4 - test_passed_total
    
    print("Overall Results for Test #1:\nTotal Tests Run: (4)  Total Tests Passed: ({0})  Total Tests Failed: ({1})".format(
        test_passed_total, test_passed_failed))
    print('----------------------------------------------------------')    

    # Test 2:

    # Starts the counters for number of tests, tests passed and tests failed
    test = 0
    num_of_failures = 0
    num_of_passes = 0

    def size_of_the_lists(dict_name: str, file_name: str) -> str:
        """The function tests if the size of the list(number of students) in a dictionary created from a file is the same as size of the list of the actual file.
        Returns "PASSED" for when the size of the lists are the same or "FAILED" ,expected and actual values if they are not.
    
        Preconditions:file_name == "student-mat.csv"
    
        >>>size_of_the_lists('School', "student-mat.csv")
        Test#1 School PASSED
        ------
        >>>size_of_the_lists('Failures', "student-mat.csv")
        Test#2 Failures FAILED: expected 395, got 390
        ------
        """

        # Counts the number of students directly from the file.
        infile = open(file_name, 'r')
        student_info = []
        for line in infile:
            line = line.strip().split(",")
            student_info.extend(line)
        expected_num_of_students = int(len(student_info) / 9 - 1)

        # Dictionay is called using the load_data function.
        dict_of_students = load_data(file_name, dict_name)

        # Counts the number of students by adding the size of the lists assigned to each key in the dictionary.
        num_of_students = 0
        for i in dict_of_students.keys():
            num_of_students = num_of_students + len(dict_of_students.get(i))

        # Increments the number of tests by 1.
        global test
        test += 1

        check_equal(str("Test #2 " + dict_name + " Dictionary"),
                    num_of_students, expected_num_of_students)

        # Increments the number of passes by 1.
        if num_of_students == expected_num_of_students:
            global num_of_passes
            num_of_passes += 1
        # Increments the number of failures by 1.
        elif num_of_students != expected_num_of_students:
            global num_of_failures
            num_of_failures += 1

    print("\n\nTest #2: Ensure the Sum of Values Associated with the Keys Contains the Correct Number of Entries\n")
    
    # The function is called four times, once using each dictionary.
    size_of_the_lists('School', "student-mat.csv")
    size_of_the_lists('Health', "student-mat.csv")
    size_of_the_lists('Age', "student-mat.csv")
    size_of_the_lists('Failures', "student-mat.csv")
    
    # Prints the total number of tests conducted, passed, and failed>
    print('Overall Results for Test #2: \nTotal Tests: (' + str(test) + ') Total Passed: (' + str(num_of_passes) +
          ') Total Failed: (' + str(num_of_failures) + ")")
    print("----------------------------------------------------------")
    
    
    # Test 3:

    fail_count = 0
    pass_count = 0
    def individual_student_entries(stu_dict: str) -> None:
        """
        given the student data dictionary format (e.g. 'School', 'Health'...)
        the function will return whether the data is stored properly in the 
        dictionary with a string containing "Passed" or "Failed" and more 
        information on why if it failed.
        precondition: must be one of the four student dictionaries from load_data.
        
        stored correctly
        >>>individual_student_entries('Health')
        Test #3 Health dictionary: Passed
        
        stored incorrectly but all student data is stored
        >>>individual_student_entries('Failures')
        Test #3: Failures dictionary FAILED: expected {'School': 'GP', 'Age': 18,\
        'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, got\
        {'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Health': 3, 'Absences': 4,\ 
        'G1': 5, 'G2': 5, 'G3': 6} 
        """
        expected = {'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0,
            'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}
        test_value_list = []
        temp_stu_info = []
        stu_key = "no match"
        counter = 0
        
        if stu_dict == 'School':
                expected.pop("School")
                description = 'School Dictionary'
        elif stu_dict == 'Health':
                expected.pop("Health")
                description = 'Health Dictionary'
        elif stu_dict == 'Age':
                expected.pop("Age")
                description = 'Age Dictionary'
        elif stu_dict == 'Failures':
                expected.pop("Failures")
                description = 'Failures Dictionary'
                
        stu_dict = load_data('student-mat.csv', stu_dict)
         
        for values in expected.values():
            test_value_list += [values]
            # gets the test values ready to compare
        for key in stu_dict:
            dict_key = stu_dict[key]
            # separtes the student info from keys in dictionary
            for individual_dict in dict_key:
                # separates the student info dictionaries from list of dictionaries
                for info in individual_dict.values():
                    # makes a list with the an one students infomation(no titles)
                    temp_stu_info += [info]
                if temp_stu_info == test_value_list:
                    stu_key = key
                    stu_index = counter
                counter += 1
                temp_stu_info = []  # resets the list for next student information
            counter = 0  # resets the counter for next key
        if stu_key == "no match":
            print("Test #3 FAILED: could not find expected student:({0}) in data".
                format(expected))
            global fail_count
            fail_count += 1
            return
    
        actual = stu_dict[stu_key][stu_index]
        check_equal("Test #3: " + description, actual, expected)
        if actual == expected:
            global pass_count
            pass_count += 1
        else:
            fail_count += 1

    print("\n\nTest #3: Ensure the Individual Student Entries in a Dictionary Are Stored Correctly\n")
    individual_student_entries('School')
    individual_student_entries("Health")
    individual_student_entries('Age')
    individual_student_entries('Failures')
    
    print('Overall Results for Test #3: \nTotal Tests: ({0}) Total Passed: ({1}) Total Failed: ({2})'
          .format(pass_count + fail_count, pass_count, fail_count))
    print("----------------------------------------------------------")


    # Test 4:
    test_pass = []

    print('\n\nTest #4: When add_average is called: Number of Students does not Change, G_Avg is Added and is Properly Calculated \n')

  #Sabeen Rafiq
    def get_G_Avg(stu_dict: dict, index: int, key, expected) -> float:
        """
        Description: Returns the G_Avg value from a given dictonary, given the
        key and index of the specific student
        Precondition: Key must be in the given dictonary, index must be valid
        Examples:
        >>>get_G_Avg(add_average(load_data('student-mat.csv', "Failures")), -1, 3, 8.33)
        8.33
        """
        try:
            actual = 0
            dict_stu = stu_dict.get(key)[index]
            actual = round(dict_stu.get("G_Avg"), 3)
    
            return actual
        except:
            return "Invalid Syntax"
    
    def get_dict_len(stu_dict: dict) -> int:
        """
        Description: Returns length of a given dictonary
        Precondition: None
        Examples:
        >>>get_dict_len(add_average(load_data('student-mat.csv', "Failures")))
        395
        """
        num_stu = 0
        for elem in stu_dict:
            for lists in stu_dict[elem]:
                num_stu += 1

        return num_stu
    
    def check_key(stu_dict: dict) -> bool:
        """
        Description: Checks if given dictonary has key "G_Avg"
        Precondition: None
        Examples:
        >>>check_key(add_average(load_data('student-mat.csv', "Failures")))
        'G_Avg'
        >>>check_key(load_data('student-mat.csv', "Failures"))
        None
        """
        
        try:
            for elem in stu_dict:
                lists = stu_dict[elem][0]
                if lists.get('G_Avg') != None:
                    return 'G_Avg'
            return None
        except:
            return None
      #Sabeen Rafiq  
    def test_4(test_name, stu_pos_1, key_1, g_avg_1, stu_pos_2, key_2, g_avg_2, stu_pos_3, key_3, g_avg_3):
        """
        Description: Checks and prints if a dictonary passed 5 tests: dict length of 395, has key G_Avg, and G_Avg is 
        calculated correctly in 3 inputted locations
        Precondition: None
        Examples:
        >>>test_4('School', 0, 'GP', 5.67, 1, 'MB', 11.33, -1, 'MS', 8.67)
        Test #4 School Dictionary: PASSED
        ------
        >>>test_4('School', 0, 'MB', 5.67, 1, 'MB', 11.33, -1, 'MS', 8.67)
        Test #4 School Dictionary FAILED: expected 5.67, got 5.0
        ------
        """
        test_type = load_data('student-mat.csv', test_name)
        add_average(test_type)
        
        # First Test: Checking Number of Students in Dictionary do not Change:
        if get_dict_len(test_type) != 395:
            return check_equal("Test #4 " + test_name + " Dictionary",
                    get_dict_len(test_type), 395)

        # Second Test: Checking G_Avg key is Added to Dictionary
        if check_key(test_type) != 'G_Avg':
            return check_equal("Test #4 " + test_name + ":",
                        check_key(test_type), 'G_Avg')

        # Third Test: Checking G_Avg Calculated Correctly:
        if get_G_Avg(test_type, stu_pos_1, key_1, g_avg_1) != g_avg_1:
            return check_equal("Test #4 " + test_name + " Dictionary",
                    get_G_Avg(test_type, stu_pos_1, key_1, g_avg_1), g_avg_1)

        if get_G_Avg(test_type, stu_pos_2, key_2, g_avg_2) != g_avg_2:
            return check_equal("Test #4 " + test_name + " Dictionary",
                    get_G_Avg(test_type, stu_pos_2, key_2, g_avg_2), g_avg_2)

        if get_G_Avg(test_type, stu_pos_3, key_3, g_avg_3) != g_avg_3:
            return check_equal("Test #4 " + test_name + " Dictionary",
                        get_G_Avg(test_type, stu_pos_3, key_3, g_avg_3), g_avg_3)


        # If none of the above tests failed then print passed:
        test_pass.append(1)
        check_equal("Test #4 " + test_name + " Dictionary", 1, 1)

    # School Dictionary -> Checking G_Avg Calculations for
    # First student in 'GP', Second student in 'MB', Last student in 'MS'
    test_4('School', 0, 'GP', 5.67, 1, 'MB', 11.33, -1, 'MS', 8.67)
    
    # Age Dictionary -> Checking G_Avg Calculations for
    # First student in Age 15, Second student in Age 18, Last student in Age 22
    test_4('Age', 0, 15, 8.33, 1, 18, 3.67, -1, 22, 7.33)
    
    # Health Dictionary -> Checking G_Avg Calculations for
    # First student in Health 1, Second student in Health 3, Last student in Health 5
    test_4('Health', 0, 1, 5.67, 1, 3, 5.33, -1, 5, 8.67)
    
    # Failures Dictionary -> Checking G_Avg Calculations for
    # First student in Failures 0, Second student in Failures 2, Last student in Failures 3
    test_4('Failures', 0, 0, 5.67, 1, 2, 6.33, -1, 3, 8.33)
    
    print('Overall Results for Test #4:')
    
    # Output Results
    print("Total Tests Run: (4)  Total Tests Passed: ({0})  Total Tests Failed: ({1})".format(
        sum(test_pass), 4 - sum(test_pass)))
    print('----------------------------------------------------------')    


    # Overall Counter:
    total_tests_pass = 0
    total_tests_fail = 0
    
    # test 1
    if test_passed_total == 4:
        total_tests_pass += 1
    else:
        total_tests_pass += 1
    # test 2
    if num_of_passes == 4:
        total_tests_pass += 1
    else:
        total_tests_fail += 1
    
    # test 3
    if pass_count == 4:
        total_tests_pass += 1
    else:
        total_tests_fail += 1
        
    # test 4
    if sum(test_pass) == 4:
        total_tests_pass += 1
    else:
        total_tests_fail += 1

    print("\nOverall Results for Tests #1, #2, #3, #4: \n-------------------------------------------------------\n" +
          "Total Tests Run: 4 \nTotal Tests Passed: {0}  \nTotal Tests Failed: {1}\n-------------------------------------------------------".format(
              total_tests_pass, total_tests_fail))

# Calls to each function, test all scenarios
# test each function
student_school_dictionary('student-mat.csv')
student_health_dictionary('student-mat.csv')
student_age_dictionary('student-mat.csv')
student_failures_dictionary('student-mat.csv')

# test load_data from main frame
load_data('student-mat.csv', 'School')
load_data('student-mat.csv', 'Health')
load_data('student-mat.csv', 'Age')
load_data('student-mat.csv', 'Failures')
# load_data('student-mat.csv', 'Student Number')

# test add_average from the main frame
add_average(load_data('student-mat.csv', 'School'))
add_average(load_data('student-mat.csv', 'Health'))
add_average(load_data('student-mat.csv', 'Age'))
add_average(load_data('student-mat.csv', 'Failures'))