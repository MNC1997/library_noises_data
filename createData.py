# create the data from scratch to a csv file

import csv
import datetime as dt
import pandas as pd
import random

# create csv file
with open('library-noises.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    # create header columns
    thewriter.writerow(['student_id', 'name', 'course', 'date', 'time', 'table', 'Sound Level'])
    # loop the code
    for i in range(5):
        # set initial values of direction of arrival of noises
        x = 50
        y = 15
        # random value of the sound pressure level (noise)
        SPL = random.randrange(50, 100)
        print(SPL)
        # declare the location of the table
        dictTable = {'Table1': 50 <= x <= 80 and 6 <= y <= 30,
                     'Table2': -4 <= x <= 1 and 10 <= y <= 30,
                     'Table3': -85 <= x <= -5 and 20 <= y <= 60,
                     'Table4': 15 <= x <= 35 and -4 <= y <= 4,
                     'Table5': -5 <= x <= 4 and -5 <= y <= 4,
                     'Table6': -35 <= x <= -10 and -5 <= y <= 5
                     }
        # initial code
        while SPL > 70:

            for table in dictTable:
                if dictTable[table] == True:
                    # get data of the students at the library
                    df = pd.read_csv('library.csv')
                    # getting random students from the library.csv file
                    randomObject = df.sample()
                    randomName = randomObject.iloc[0, 0]
                    randomId = randomObject.iloc[0, 1]
                    randomCourse = randomObject.iloc[0, 2]
                    date_obj = dt.date.today()
                    x = dt.datetime.now()
                    time_obj = x.strftime("%X")
                    # insert the dataset
                    thewriter.writerow([randomId, randomName, randomCourse, date_obj, time_obj, table, SPL])
            break
