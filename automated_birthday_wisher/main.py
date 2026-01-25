import pandas
import smtplib
import datetime as dt
import random
import os
# ............ CONSTANTS .....................#
MY_EMAIL="your_email@example.com"           # put your email here
MY_PASSWORD=os.getenv("MY_GMAIL_PASSWORD")      # saved my environment variable for security, you can put your password here directly but not recommended

# ................ Get current date ....................#
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day


data = pandas.read_csv("birthdays.csv") # type: ignore

for (index, row) in data.iterrows():
    # Check if today is anyone's birthday
    if row['month'] == current_month and row['day'] == current_day:
        # Pick a random letter to send to the person
        random_letter = f'letter_templates/letter_{random.randint(1,3)}.txt'
        with open(random_letter, 'r') as letter:
            content = letter.read()
            content = content.replace("[NAME]", f"{row["name"]}")
        
        # Send the letter to the person
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, 
                                to_addrs=f"{row['email']}", 
                                msg=f"Subject:It's your birthday!!\n\n{content}"
                                )


        
