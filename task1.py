from datetime import datetime

user_date=input("Input date in format YYYY-MM-DD, please ")

def get_days_from_today(date):
    try:
        user_datetime=datetime.strptime(date,"%Y-%m-%d")
        difference_days=(datetime.today()-user_datetime).days
        print(difference_days)
        return difference_days
    except ValueError:
        print("Invalid value")
        return "Invalid value"

get_days_from_today(user_date)