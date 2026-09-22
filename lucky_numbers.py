# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 10:07:05 2025
Updated with new skills on 9/22/26

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
    birthdate_nums_str = birthdate.replace('-', '')
    lucky_num = sum(int(num) for num in birthdate_nums_str)
    # Lucky num has to be single digit
    # While num is more than 1 digit, loop through, find new sum of current lucky_num
    while len(str(lucky_num)) > 1:
        lucky_num = sum(int(num) for num in str(lucky_num))

    return lucky_num

def lucky_number_by_name(name):
    """
    Takes a person's name and calculates their lucky number from it.
x
    Parameters
    ----------
    name : The name to get the lucky number from.

    Returns
    -------
    magic_num : The name's lucky number.

    """

    # Clean the string by only adding in alpha letters
    name_letters_list = [letter.lower() for letter in name if letter.isalpha()]
    clean_name = ''.join(name_letters_list)

    # Calculate the total number from the strings letters
    total = 0

    letter_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                     'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                     'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
                     's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
                     'y': 25, 'z': 26}

    for i in range(len(clean_name)):
        letter = clean_name[i]
        total += letter_values[letter]


    # Loop and calculate the lucky number until lucky_num is single digit
    lucky_num = total   
    while len(str(lucky_num)) > 1:
        lucky_num = sum(int(num) for num in str(lucky_num))

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
    lucky_num = str(row["lucky_number_by_birthday"])
    bday_luckynum_dict[lucky_num] += 1
        
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
    lucky_num = str(row["lucky_number_by_name"])
    name_luckynum_dict[lucky_num] += 1
 
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
