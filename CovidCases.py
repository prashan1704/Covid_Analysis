import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from urllib.request import urlretrieve

urlretrieve("https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv","./Covid_Analysis/italy_covid_data.csv")
covid_data = pd.read_csv("./Covid_Analysis/italy_covid_data.csv")


def sum_death():
    total_death = covid_data["new_deaths"].sum()
    return total_death


def sum_cases():
    total_cases = covid_data["new_cases"].sum()
    return total_cases


def sum_tests():
    total_tests = covid_data["new_tests"].sum()
    return total_tests


def maximum():
    choice = input("Enter D for death, C for cases and T for tests: ").lower()
    if choice == "d":
        max_death = covid_data.new_deaths.max()
        index = covid_data.index[covid_data["new_deaths"] == max_death].tolist()
        value = index[0]
        return covid_data.date.loc[value]
    elif choice == "c":
        max_case = covid_data.new_cases.max()
        index = covid_data.index[covid_data["new_cases"] == max_case].tolist()
        value = index[0]
        return covid_data.date.loc[value]

    elif choice == "t":
        max_test = covid_data.new_tests.max()
        index = covid_data.index[covid_data["new_tests"] == max_test].tolist()
        value = index[0]
        return covid_data.date.loc[value]


def minimum():
    choice = input("Enter D for death, C for cases and T for tests: ").lower()
    if choice == "d":
        min_death = covid_data.new_deaths.min()
        index = covid_data.index[covid_data["new_deaths"] == min_death].tolist()
        value = index[0]
        print("*" * 10)
        return covid_data.date.loc[value]

    elif choice == "c":
        min_case = covid_data.new_cases.min()
        index = covid_data.index[covid_data["new_cases"] == min_case].tolist()
        value = index[0]
        return covid_data.date.loc[value]

    elif choice == "t":
        min_test = covid_data.new_tests.min()
        index = covid_data.index[covid_data["new_tests"] == min_test].tolist()
        value = index[0]
        return covid_data.date.loc[value]


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
            print(f"Total death is {sum_death()}")
        elif choice == "c":
            print(f"Total death is {sum_cases()}")
        elif choice == "t":
            print(f"Total death is {sum_tests()}")

    elif entry == 2:
        print("The death ratio is {:.2f}".format((sum_death() / sum_cases()) * 100))

    elif entry == 3:
        print(f"The total number of tests conducted are: {sum_tests()+935310}")

    elif entry == 4:
        result = maximum()
        print(f"The maximum number was on date {result}")
    elif entry == 5:
        result = minimum()
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
