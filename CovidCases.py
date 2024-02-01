import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from urllib.request import urlretrieve
import functions

urlretrieve("https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv","italy_covid_data.csv")

covid_data = pd.read_csv("italy_covid_data.csv")

def convert_to_date(covid_data):
    dates = pd.to_datetime(covid_data["date"])
    covid_data["years"] = pd.DatetimeIndex(dates).year
    covid_data["month"] = pd.DatetimeIndex(dates).month
    covid_data["day"] = pd.DatetimeIndex(dates).day
    covid_data["weekday"] = pd.DatetimeIndex(dates).weekday
    return covid_data


def data_for_month(value):
    covid_data_coverted = convert_to_date(covid_data)
    covid_data_month = covid_data_coverted[covid_data_coverted["month"] == value]
    covid_data_month_metric = covid_data_coverted[
        ["new_cases", "new_deaths", "new_tests"]
    ]
    return covid_data_month_metric.sum()


def data_by_day(value, weekday):
    covid_data_converted = convert_to_date(covid_data)
    covid_data_month = covid_data_converted[covid_data_converted["month"] == value]
    covid_data_day = covid_data_month[covid_data_month["weekday"] == weekday]
    covid_data_day_metric = covid_data_day[["new_cases", "new_deaths", "new_tests"]]
    return covid_data_day_metric.sum()


def print_charts(covid_data):
    covid_data_date=convert_to_date(covid_data)

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
            value = int(
                input(
                    """For which month would you like to look for:
                1: January
                2. Feb
                3. Mar
                4. April
                5. May
                6. June
                7. July
                8. August
                9. September
                10. October
                11. November
                12. December\n"""
                )
            )
            result = data_for_month(value)
            print("Total are: ", result)
            choice_day = input(
                "Do you wish to check for the data for the day as well? Y for Yes or N for No\n"
            ).lower()
            if choice_day == "y":
                weekday = int(
                    input(
                        """Enter the day for which you would like to see: 
                                0: Monday
                                1: Tuesday
                                2: Wednesday
                                3: Thursday
                                4: Friday
                                5: Saturday
                                6: Sunday\n"""
                    )
                )
                result = data_by_day(value, weekday)
                print(f"The data for the day you chose is:  {result}")
            elif choice_day == "n":
                continue
            else:
                print("You entered wrong value")
                break

        elif entry == 7:
            print_charts(covid_data)
