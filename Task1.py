import datetime

from collections import defaultdict
from datetime import timedelta

def get_birthdays_per_week(users):
    
    # This time we should get current date
    today = datetime.date.today()
    birthdays_by_weekday = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        # Converting by the type date
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the number of days from today until the upcoming birthday
        delta_days = (birthday_this_year - today).days


        # I really hate this part and couldn´t handle it whithout help 
        if 0 <= delta_days < 7:
            weekday = (today + timedelta(days=delta_days)).strftime("%A")

            # Now let´s try to shift birthdazs away from weekend
            if weekday == "Saturday":
                weekday = "Monday"
            elif weekday == "Sunday":
                delta_days += 1
                weekday = (today + timedelta(days=delta_days)).strftime("%A")

            birthdays_by_weekday[weekday].append(name)

    # Display birthdays per weekday
    for weekday, names in birthdays_by_weekday.items():
        if names:  # Only print weekdays with birthdays
            print(f"{weekday}: {', '.join(names)}")


# Let's create a list of dictionaries (one of them could be used to check workability). 
users = [
    {"name": "Vynohradova Ruslana", "birthday": datetime.date(1994, 5 , 10)},
    {"name": "Vynohradova Ganna", "birthday": datetime.date(1970, 3, 10)},
    {"name": "Vynohradov Oleksandr", "birthday": datetime.date(1994, 12, 31)},
    {"name": "Nepokrytyh Roman", "birthday": datetime.date(1993, 2, 28)},
    {"name": "Sorokina Valeriia", "birthday": datetime.date(2002, 6, 9)},
    {"name": "Sorokina Kristina", "birthday": datetime.date(2004, 7, 2)},
]

get_birthdays_per_week(users)
