import smtplib, ssl

context = ssl.create_default_context()

message = """
Hello, this is a test message!
Formatting done like this:
<h1>How are you?</h1>
"""
sender_email = "sender@sorc3r3r.io"
password = input("Enter your password: ")
receiver_email = "receiver@sorc3r3r.io"

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
