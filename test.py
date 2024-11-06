from datetime import date

today = date.today()
today_format = today.strftime("%d-%m-%y")
print(f"todays date is: {today_format}")