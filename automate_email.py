import csv
from email.message import EmailMessage
import smtplib
import mimetypes
import os

def get_credentials(filepath):
    with open(filepath, "r") as f:
        email_id = f.readline().strip()
        login_pass = f.readline().strip()
    return (email_id, login_pass)

def login(email_id, login_pass, s):
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(email_id, login_pass)
    print("Login successful")

def attach_file(message, filepath):
    if not os.path.isfile(filepath):
        print(f"Attachment file not found: {filepath}")
        return

    mime_type, _ = mimetypes.guess_type(filepath)
    mime_type, mime_subtype = mime_type.split('/') if mime_type else ("application", "octet-stream")

    with open(filepath, 'rb') as file:
        message.add_attachment(
            file.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=os.path.basename(filepath)
        )

def send_mail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    email_id, login_pass = get_credentials("credentials.txt")
    login(email_id, login_pass, s)

    subject = "Welcome to Python" # Mention your subject here
    # Add your body of the email here
    body = """
            Hello welcome to python automated mailing system. 
        """

    # Reading email id from csv file
    with open("emails.csv", newline="") as csvfile:
        id = csv.reader(csvfile)
        for row in id:
            recipient = row[0].strip()
            if not recipient:
                continue

            message = EmailMessage()
            message.set_content(body)
            message['Subject'] = subject
            message['From'] = email_id
            message['To'] = recipient

            # Add your attachment here
            attach_file(message, "sample.pdf")  # change "sample.pdf" to your required file to be sent

            s.send_message(message)
            print("Email sent to ->", recipient)

    s.quit()
    print("All emails sent.")

if __name__ == "__main__":
    send_mail()
