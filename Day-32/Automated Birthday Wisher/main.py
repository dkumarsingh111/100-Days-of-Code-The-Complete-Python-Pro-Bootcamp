from datetime import datetime
import pandas as pd
import random
import smtplib


MY_EMAIL = "exampleemail"
MY_PASSWORD = "password"
FILE_PATH="c:/Users/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/Day-31/Automated Birthday Wisher"


today = datetime.now()
today_tuple = (today.month, today.day)


data = pd.read_csv(f"{FILE_PATH}/birthdays.csv")


birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"{FILE_PATH}/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )