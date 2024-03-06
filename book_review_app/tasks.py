from datetime import datetime


def email_confirmation_task(message):
    with open('email_confirmation.txt', 'a') as file:
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f'\n[{date_time}]: {message}')
