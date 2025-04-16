# 📧 Python Automated Email Sender with Attachments

This Python script automates the process of sending personalized emails (with file attachments) using Gmail's SMTP server. It's perfect for small batch email campaigns, notifications, or simple mailing systems.

## 🚀 Features

- ✅ Secure login using credentials stored in a text file
- ✅ Send emails to a list of recipients from a CSV file
- ✅ Supports file attachments (PDF, images, documents, etc.)
- ✅ Modular, readable code structure
- ✅ Easily customizable subject and message body

## 📂 File Structure

```
Automate_Email/
├── email_sender.py
├── credentials.txt
├── emails.csv
├── sample.pdf
└── README.md
```

## 🔧 Setup Instructions

1. **Install Python** if not already installed.
2. **Create a Gmail App Password** (required if you have 2FA enabled):
   - Visit: https://myaccount.google.com/apppasswords
   - Login to your account and provide an app name. (e.g., `automate_mail`)
   - Copy the 16-digit code and store it in `credentials.txt` without **spaces**.

3. **Prepare Required Files**:
   - credentials.txt:
     ```
     your_email@gmail.com
     your_app_password_here
     ```
   - emails.csv:
     ```
     recipient1@example.com
     recipient2@example.com
     recipient3@example.com
     ```

   - Place the file you want to attach (e.g., `sample.pdf`) in the same directory.

4. **Run the Script**:
   ```bash
   python automate_email.py
