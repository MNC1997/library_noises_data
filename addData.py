# add more data in a loop

import csv
import datetime as dt
import pandas as pd
import random
import time


def main():

    for i in range(4):
        # add data from the csv file
        with open('library-noises.csv', 'a+', newline='') as f:
            thewriter = csv.writer(f)
            x = 50
            y = 15
            SPL = random.randrange(50, 100)
            dictTable = {'Table1': 50 <= x <= 80 and 6 <= y <= 30,
                         'Table2': -4 <= x <= 1 and 10 <= y <= 30,
                         'Table3': -85 <= x <= -5 and 20 <= y <= 60,
                         'Table4': 15 <= x <= 35 and -4 <= y <= 4,
                         'Table5': -5 <= x <= 4 and -5 <= y <= 4,
                         'Table6': -35 <= x <= -10 and -5 <= y <= 5
                         }
            while SPL > 70:

                for table in dictTable:
                    if dictTable[table] == True:
                        df = pd.read_csv('library.csv')
                        randomObject = df.sample()
                        randomName = randomObject.iloc[0, 0]
                        randomId = randomObject.iloc[0, 1]
                        randomCourse = randomObject.iloc[0, 2]
                        date_obj = dt.date.today()
                        x = dt.datetime.now()
                        time_obj = x.strftime("%X")
                        thewriter.writerow([randomId, randomName, randomCourse, date_obj, time_obj, table, SPL])
                break
    time.sleep(5)
    main()

main()



