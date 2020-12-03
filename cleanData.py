# cleaning of data and sending it to csv file and excel file
# separating the name to first_name and last_name

import pandas as pd
import xlsxwriter

# declare values
clean_data = xlsxwriter.Workbook('clean.xlsx')
csv_file = pd.read_csv('library-noises.csv', index_col = 'student_id')

# creating empty list
first_names_list = []
last_names_list = []

# declare the name column
csv_names = csv_file['name']

# splitting the first name and last name
for i in csv_names:
    a = []
    a = i.split()
    for j in a:
        # since there are some names that have 2 first names, implement a condition that would
        # split them and declare it as first name
        if len(a) == 2:
            first_name = a[0]
            last_name = a[1]

        if len(a) == 3:
            first_name = [a[0], a[1]]
            last_name = a[2]

    # append the list
    first_names_list.append(first_name)
    last_names_list.append(last_name)

# insert the rows
csv_file.insert(1, "First Name", first_names_list)
csv_file.insert(2, "Last Name", last_names_list)
# delete old data name

del csv_file['name']
# move to excel
csv_file.to_excel("clean.xlsx")

# since some names still has not been fully cleaned, we replaced those unwanted characters to empty spaces
read_excel = pd.read_excel("clean.xlsx", index_col = 'student_id', sheet_name='Sheet1')
excel_firstname = read_excel['First Name']
replace_name = excel_firstname.replace(',', '', regex=True)
replace_name1 = replace_name.str.strip('[')
replace_name2 = replace_name1.str.strip(']')
replace_name3 = replace_name2.str.replace("'", "")

del read_excel['First Name']
read_excel.insert(0, "First Name", replace_name3)
# sent to excel
read_excel.to_excel("clean.xlsx")
# sent to csv
read_excel.to_csv("clean.csv")
