# Automate_Email

This project contains a simple python script which is used to sends the similar message to multiple recipient's.

## Dependencies

This project requires only Python standard library
(more specifically, the `csv`, `email`, and `smtplib` modules).

## Running the script

The script requires two configuration files

* `emails.csv` should contain all the recipient's mail id.
* `credentials.txt` should contain your login credentials such as E-mail id and Login Password.
* Make sure `automate_email.py`, `emails.csv` and `credentials.txt` are in same folder.

## Error !
While running the script if you get any error like `Username and Password not accepted`.

`raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. For more information, go to\n5.7.8  https://support.google.com/mail/?p=BadCredentials d9443c01a7336-22ac7b62917sm114854365ad.11 - gsmtp')`

1. Go to `https://myaccount.google.com/apppasswords`
2. Sign in and set **App Name**.
3. A 16-Digit code will be generated copy that and replace it in `credentials.txt` instead of original password (Remove spaces).
