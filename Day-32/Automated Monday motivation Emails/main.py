import smtplib
import datetime as dt
import random


MY_EMAIL = "testing email address"
MY_PASSWORD = "password"
FILE_PATH="c:/Users/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/Day-31/Automated Monday motivation Emails"


now = dt.datetime.now()
weekday = now.weekday()


if weekday == 0:
    with open(f"{FILE_PATH}/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )