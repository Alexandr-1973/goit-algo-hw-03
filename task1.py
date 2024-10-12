from datetime import datetime

user_date=input("Input date in format YYYY-MM-DD, please ")

def get_days_from_today(date):
    try:
        user_datetime=datetime.strptime(date,"%Y-%m-%d")
        difference_days=(datetime.today()-user_datetime).days
        print(difference_days)
        return difference_days
    except ValueError:
        user_new_date=input("You input invalid format date. Please, input date in format YYYY-MM-DD ")
        get_days_from_today(user_new_date)

get_days_from_today(user_date)