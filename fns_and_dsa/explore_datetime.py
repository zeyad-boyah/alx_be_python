from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)


def calculate_future_date():
    num_of_days_in_the_future = int(input("Enter the number of days to add to the current date: "))
    now = datetime.now()
    future_date = now + timedelta(days=num_of_days_in_the_future)
    print(future_date.strftime("%Y-%m-%d"))


display_current_datetime()
calculate_future_date()
