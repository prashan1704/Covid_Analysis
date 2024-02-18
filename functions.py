from urllib.request import urlretrieve
import pandas as pd


class perform:
    def __init__(self):
        urlretrieve(
            "https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv",
            "italy_covid_data.csv",
        )
        covid_data = pd.read_csv("italy_covid_data.csv")
        self.covid_data = covid_data

    def sum_death(self):
        total_death = self.covid_data["new_deaths"].sum()
        return total_death

    def sum_cases(self):
        total_cases = self.covid_data["new_cases"].sum()
        return total_cases

    def sum_tests(self):
        total_tests = self.covid_data["new_tests"].sum()
        return total_tests

    def maximum(self):
        choice = input("Enter D for death, C for cases and T for tests: ").lower()
        if choice == "d":
            max_death = self.covid_data.new_deaths.max()
            index = self.covid_data.index[
                self.covid_data["new_deaths"] == max_death
            ].tolist()
            value = index[0]
            return self.covid_data.date.loc[value]
        elif choice == "c":
            max_case = self.covid_data.new_cases.max()
            index = self.covid_data.index[
                self.covid_data["new_cases"] == max_case
            ].tolist()
            value = index[0]
            return self.covid_data.date.loc[value]

        elif choice == "t":
            max_test = self.covid_data.new_tests.max()
            index = self.covid_data.index[
                self.covid_data["new_tests"] == max_test
            ].tolist()
            value = index[0]
            return self.covid_data.date.loc[value]

    def minimum(self):
        choice = input("Enter D for death, C for cases and T for tests: ").lower()
        if choice == "d":
            min_death = self.covid_data.new_deaths.min()
            index = self.covid_data.index[
                self.covid_data["new_deaths"] == min_death
            ].tolist()
            value = index[0]
            print("*" * 10)
            return self.covid_data.date.loc[value]

        elif choice == "c":
            min_case = self.covid_data.new_cases.min()
            index = self.covid_data.index[
                self.covid_data["new_cases"] == min_case
            ].tolist()
            value = index[0]
            return self.covid_data.date.loc[value]

        elif choice == "t":
            min_test = self.covid_data.new_tests.min()
            index = self.covid_data.index[
                self.covid_data["new_tests"] == min_test
            ].tolist()
            value = index[0]
            return self.covid_data.date.loc[value]

    def convert_to_date(self):
        dates = pd.to_datetime(self.covid_data["date"])
        self.covid_data["years"] = pd.DatetimeIndex(dates).year
        self.covid_data["month"] = pd.DatetimeIndex(dates).month
        self.covid_data["day"] = pd.DatetimeIndex(dates).day
        self.covid_data["weekday"] = pd.DatetimeIndex(dates).weekday
        return self.covid_data

    def data_for_month(self, value):
        covid_data_coverted = perform.convert_to_date(self)
        covid_data_month = covid_data_coverted[covid_data_coverted["month"] == value]
        covid_data_month_metric = covid_data_coverted[
            ["new_cases", "new_deaths", "new_tests"]
        ]
        return covid_data_month_metric.sum()


    def data_by_day(self, value, weekday):
        covid_data_converted = perform.convert_to_date(self)
        covid_data_month = covid_data_converted[covid_data_converted["month"] == value]
        covid_data_day = covid_data_month[covid_data_month["weekday"] == weekday]
        covid_data_day_metric = covid_data_day[["new_cases", "new_deaths", "new_tests"]]
        return covid_data_day_metric.sum()
