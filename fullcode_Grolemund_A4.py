# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 10:07:05 2025

This program calculates Presidents lucky number by their age and name.
It finds similar lucky numbers between Presidents, and creates panda data
frames to display them. It also creates bar charts to display many of the
findings.

@author: Kevin Grolemund
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def lucky_number_by_birthday(birthdate):
    """
    Takes a birthdate and calculates the lucky number from it.

    Parameters
    ----------
    birthdate : The birthdate to be calculated.

    Returns
    -------
    lucky_num : The lucky number for the birthdate.

    """
    sum = 0

    for i in range(len(birthdate)):
        if birthdate[i] == "-":
            continue
        else:
            num = int(birthdate[i])
            sum += num
            
    lucky_num = sum   
    while lucky_num > 9:
    
       new_lucky_num = 0
       while lucky_num > 0:
           # Get last digit out and adds it to sum
           digit = lucky_num % 10
           new_lucky_num += digit
           # Update lucky_num and continue the process until lucky_num == 0
           lucky_num = lucky_num // 10

       # lucky_num is at 0. 
       # Restore lucky_num back to it's updated value for the next loop
       lucky_num = new_lucky_num

    return lucky_num

def lucky_number_by_name(name):
    """
    Takes a person's name and calculates their lucky number from it.

    Parameters
    ----------
    name : The name to get the lucky number from.

    Returns
    -------
    magic_num : The name's lucky number.

    """
    clean_str = ""

    # Clean the string by only adding in alpha letters
    for i in range(len(name)):
        if name[i].isalpha():
            clean_str += name[i]

    # Make the string all lowercase. Calculate the total number from the string
    total = 0
    clean_str = clean_str.lower()

    for i in range(len(clean_str)):
        if clean_str[i] == 'a':
            total += 1
        elif clean_str[i] == 'b':
            total += 2
        elif clean_str[i] == 'c':
            total += 3
        elif clean_str[i] == 'd':
            total += 4
        elif clean_str[i] == 'e':
            total += 5
        elif clean_str[i] == 'f':
            total += 6
        elif clean_str[i] == 'g':
            total += 7
        elif clean_str[i] == 'h':
            total += 8
        elif clean_str[i] == 'i':
            total += 9
        elif clean_str[i] == 'j':
            total += 10
        elif clean_str[i] == 'k':
            total += 11
        elif clean_str[i] == 'l':
            total += 12
        elif clean_str[i] == 'm':
            total += 13
        elif clean_str[i] == 'n':
            total += 14
        elif clean_str[i] == 'o':
            total += 15
        elif clean_str[i] == 'p':
            total += 16
        elif clean_str[i] == 'q':
            total += 17
        elif clean_str[i] == 'r':
            total += 18
        elif clean_str[i] == 's':
            total += 19
        elif clean_str[i] == 't':
            total += 20
        elif clean_str[i] == 'u':
            total += 21
        elif clean_str[i] == 'v':
            total += 22
        elif clean_str[i] == 'w':
            total += 23
        elif clean_str[i] == 'x':
            total += 24
        elif clean_str[i] == 'y':
            total += 25
        elif clean_str[i] == 'z':
            total += 26


    # Loop and calculate the lucky number until lucky_num <= 9
    lucky_num = total   
    while lucky_num > 9:
        new_lucky_num = 0
        while lucky_num > 0:
            # Get last digit out. Add it to sum
            digit = lucky_num % 10
            new_lucky_num += digit
            # Update lucky_num. Continue process until lucky_num == 0
            lucky_num = lucky_num // 10

        # lucky_num is at 0
        # Restore lucky_num back to it's updated value for the next loop
        lucky_num = new_lucky_num

    return lucky_num

def display(data):
    """
    Prints and displays a panda data frame, with it's index values turned off.
    
    """
    print(data.to_string(index=False))

presidents = pd.read_csv(
           'https://raw.githubusercontent.com/gheniabla/datasets/master/us-presidents.csv')

# Calculate each president's lucky num by bday. Add it to a list
luckynum_by_bday_list = []

for i, row in presidents.iterrows():
    lucky_num = lucky_number_by_birthday(row["Birthdate"])
    luckynum_by_bday_list.append(lucky_num)

# Create new column from the luckynum_by_bday_list
presidents["lucky_number_by_birthday"] = luckynum_by_bday_list

# Calculate each president's lucky num by name. Add it to a list
luckynum_by_name_list = []

for i, row in presidents.iterrows():
    lucky_num = lucky_number_by_name(row["Name"])
    luckynum_by_name_list.append(lucky_num)
    
# Create new column from the lucknum_by_name_list
presidents["lucky_number_by_name"] = luckynum_by_name_list

print('Problem #1:\n')
# Print starting panda data frame
display(presidents)
        
print('\nProblem #2:\n')       

# Create a dictionary to keep track of the number of Presidents born in 
# each month
birth_month_count = {'January': 0, 'February': 0, 'March': 0,
                     'April': 0, 'May': 0, 'June': 0, 'July': 0,
                     'August': 0, 'September': 0, 'October': 0,
                     'November': 0, 'December': 0}

# Go to birthdate column, list slice the birth month, add 1 to the month dict
for i, row in presidents.iterrows():
    birthdate = row["Birthdate"]
    month = birthdate[5:7]
    if month == '01':
        birth_month_count['January'] += 1
    elif month == '02':
        birth_month_count['February'] += 1
    elif month == '03':
        birth_month_count['March'] += 1
    elif month == '04':
        birth_month_count['April'] += 1
    elif month == '05':
        birth_month_count['May'] += 1
    elif month == '06':
        birth_month_count['June'] += 1
    elif month == '07':
        birth_month_count['July'] += 1
    elif month == '08':
        birth_month_count['August'] += 1
    elif month == '09':
        birth_month_count['September'] += 1
    elif month == '10':
        birth_month_count['October'] += 1
    elif month == '11':
        birth_month_count['November'] += 1
    elif month == '12':
        birth_month_count['December'] += 1

# Create new panda data frame that has months and how many Presidents born
# in that month
month_list = []     # Jan-Dec
month_count_list = []

# Loop through the dictionary and put the necessary data into each list
for key, value in birth_month_count.items():
    month_list.append(key)
    month_count_list.append(value)
    

presidents_by_month = pd.DataFrame()

presidents_by_month['Month'] = month_list
presidents_by_month['Count'] = month_count_list
display(presidents_by_month)

# Create a bar chart of the findings
plt.figure(figsize=(13, 5))
plt.title('Presidents by Birth Month', fontsize=24, fontstyle='italic')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.grid(True, axis='y', color='0.5', linestyle='--')
plt.bar(month_list, month_count_list, edgecolor='black', linewidth=2)
plt.show()


print('\nProblem #3:\n')
# Dictionary to count how many of each bday lucky nums the Presidents had
bday_luckynum_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
                  '7': 0, '8': 0, '9':0}

for i, row in presidents.iterrows():
    lucky_num = row["lucky_number_by_birthday"]
    if lucky_num == 1:
        bday_luckynum_dict['1'] += 1
    elif lucky_num == 2:
        bday_luckynum_dict['2'] += 1
    elif lucky_num == 3:
        bday_luckynum_dict['3'] += 1
    elif lucky_num == 4:
        bday_luckynum_dict['4'] += 1
    elif lucky_num == 5:
        bday_luckynum_dict['5'] += 1
    elif lucky_num == 6:
        bday_luckynum_dict['6'] += 1
    elif lucky_num == 7:
        bday_luckynum_dict['7'] += 1
    elif lucky_num == 8:
        bday_luckynum_dict['8'] += 1
    elif lucky_num == 9:
        bday_luckynum_dict['9'] += 1
        
luckynum_list = []
bday_count_list = []

# Loop through the dict and put the necessary data into each list
for key, value in bday_luckynum_dict.items():
    luckynum_list.append(key)
    bday_count_list.append(value)

presidents_bday_luckynumber = pd.DataFrame()
presidents_bday_luckynumber['luckynumber'] = luckynum_list
presidents_bday_luckynumber['count'] = bday_count_list
display(presidents_bday_luckynumber)

# Create a bar chart of our findings
plt.figure(figsize=(10, 5))
plt.title('Number of Presidents by Birthday Lucky Numbers', fontsize=16, fontstyle='italic')
plt.xlabel('Lucky Number', fontsize=14)
plt.ylabel('Count', fontsize=15)
plt.grid(True, axis='y', color='0.5', linestyle='--')
plt.bar(luckynum_list, bday_count_list, edgecolor='black', linewidth=2)
plt.show()

print('\nProblem #4:\n')
# Dictionary to keep count of the name lucky numbers
name_luckynum_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
                  '7': 0, '8': 0, '9':0}

for i, row in presidents.iterrows():
    lucky_num = row["lucky_number_by_name"]
    if lucky_num == 1:
        name_luckynum_dict['1'] += 1
    elif lucky_num == 2:
        name_luckynum_dict['2'] += 1
    elif lucky_num == 3:
        name_luckynum_dict['3'] += 1
    elif lucky_num == 4:
        name_luckynum_dict['4'] += 1
    elif lucky_num == 5:
        name_luckynum_dict['5'] += 1
    elif lucky_num == 6:
        name_luckynum_dict['6'] += 1
    elif lucky_num == 7:
        name_luckynum_dict['7'] += 1
    elif lucky_num == 8:
        name_luckynum_dict['8'] += 1
    elif lucky_num == 9:
        name_luckynum_dict['9'] += 1
 
name_count_list = []

# Loop through dict and add the count value to the list
# We have a list of the months from before. Will re-use that
for v in name_luckynum_dict.values():
    name_count_list.append(v)

presidents_name_luckynumber = pd.DataFrame()
presidents_name_luckynumber['luckynumber'] = luckynum_list
presidents_name_luckynumber['count'] = name_count_list
display(presidents_name_luckynumber)

# Create a bar chart of our findings
plt.figure(figsize=(10, 5))
plt.title('Number of Presidents by Name Lucky Numbers', fontsize=16, fontstyle='italic')
plt.xlabel('Lucky Number', fontsize=14)
plt.ylabel('Count', fontsize=15)
plt.grid(True, axis='y', color='0.5', linestyle='--')
plt.bar(luckynum_list, name_count_list, edgecolor='black', linewidth=2)
plt.show()

print('\nProblem #5:\n')
# Create new data frame with the counts of lucky nums
# by Bdays and by name
presidents_luckynumber = pd.DataFrame()
presidents_luckynumber['luckynumber'] = luckynum_list
presidents_luckynumber['bday_luckynumber'] = bday_count_list
presidents_luckynumber['name_luckynumber'] = name_count_list
display(presidents_luckynumber)

# Create a bar chart that shows the count for each lucky number
# Each lucky number has 2 values per x value
plt.figure(figsize=(15, 5))

# Create space on the chart for the 2 x values
w, x = 0.4, np.arange(len(luckynum_list))
fig, ax = plt.subplots()
ax.bar(x - w / 2, bday_count_list, width=w, label='Bday Lucky Num', 
       edgecolor='black', linewidth=1.5)
ax.bar(x + w / 2, name_count_list, width=w, label='Name Lucky Num',
       edgecolor='black', linewidth=1.5)
# Make sure the x ticks show every lucky num (1-9)
ax.set_xticks(x)
ax.set_xticklabels(luckynum_list)
ax.grid(True, axis='y', color='0.5', linestyle='--')
# Display the names of the values in the legend
ax.legend(loc=9)

plt.title('Presidents by Lucky Numbers', fontsize=16, fontstyle='italic')
plt.xlabel('Lucky Number', fontsize=14)
plt.ylabel('Count', fontsize=15)
plt.show()