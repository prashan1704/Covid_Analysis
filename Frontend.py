import functions

per=functions.perform()

class perform:
   def __init__(self):
       pass
   def displaying(self):
      itr = True
      while itr:
         a = int(
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
                     12. December
                     13. Quit\n"""
            )
         )
         if a == 13:
            itr = False
         elif a in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            result = per.data_for_month(a)                    
            print("Total are: ", result)
            # print("you choose the month: You did a great job")
            choice_day = input(
                  "Do you wish to check for the data for the day as well? Y for Yes or N for No\n"
            ).lower()
            if choice_day == "y":
                  d = True
                  while d:
                     weekday = int(
                        input(
                              """Enter the day for which you would like to see: 
                                    0: Monday
                                    1: Tuesday
                                    2: Wednesday
                                    3: Thursday
                                    4: Friday
                                    5: Saturday
                                    6: Sunday
                                    7: Quit\n"""
                        )
                     )
                     if weekday == 7:
                        d = False
                     elif weekday in [0, 1, 2, 3, 4, 5, 6]:
                        result = per.data_by_day(a, weekday)
                        print(f"The data for the day you chose is:  {result}")

                     else:
                        print("Unfortunately, you entered the Wrong value")
                        continue

            elif choice_day == "n":
                  continue
            else:
                  print("Unfortunately, you entered the Wrong value")
                  continue
         else:
            print("Unfortunately, you entered the Wrong value")
            continue
