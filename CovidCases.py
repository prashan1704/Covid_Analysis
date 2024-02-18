import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from urllib.request import urlretrieve
import functions
import Frontend

urlretrieve("https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv","italy_covid_data.csv")

covid_data = pd.read_csv("italy_covid_data.csv")

if __name__=="__main__":
    per=functions.perform()

    itr = True
    while itr:
        print(
            """Let me know what would you like to fetch of year 2020: Please press accordingly:
        1. Total death OR cases OR tests
        2. What is the overall death rate (ratio of reported deaths to reported cases)?
        3. What is the overall number of tests conducted? A total of 935310 tests were conducted before daily test numbers were reported.
        4. Maximum Death, Maximum Cases and Maximum Test as per date
        5. Minimum Death, Minimum Cases and Minimum Test as per date
        6. Check the data as per Month 
        7. See the visualization reports
        8. Quit
    """
        )
        entry = int(input("Enter your choice: "))
        if entry == 1:
            choice = input("Enter D for DEATH, C for CASES and T for TESTS: ").lower()
            if choice == "d":
                print(f"Total death is {per.sum_death()}")
            elif choice == "c":
                print(f"Total death is {per.sum_cases()}")
            elif choice == "t":
                print(f"Total death is {per.sum_tests()}")

        elif entry == 2:
            print("The death ratio is {:.2f}".format((per.sum_death() / per.sum_cases()) * 100))

        elif entry == 3:
            print(f"The total number of tests conducted are: {per.sum_tests()+935310}")

        elif entry == 4:
            result = per.maximum()
            print(f"The maximum number was on date {result}")
        elif entry == 5:
            result = per.minimum()
            print(f"The minimum number was on date {result}")

        elif entry == 6:
            dis=Frontend.perform()
            dis.displaying()
            
        elif entry == 7:
             pass
        elif entry==8:
            itr=False
        else:
            print("You entered wrong value")
