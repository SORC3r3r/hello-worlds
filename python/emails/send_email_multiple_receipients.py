import email, smtplib, ssl, csv

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Huf Secure Mobile - Weekly Incident Report"
body = """Dear {name},

this is an auto-generated email sent by python.

BR
SORC3r3r
"""
sender_email = "sender@sorc3r3r.io"
receiver_email = "receiver@sorc3r3r.io"
password = input("Enter your password: ")

def prepare_message(name, body):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    #message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    body = body.format(name=name)
    print(body)
    message.attach(MIMEText(body, "plain"))

    filename = "movemee-incident-report.xlsx"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    return text

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.mailbox.org", 465, context=context) as server:
    server.login(sender_email, password)
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            print(f"Sending Email to {name}")
            content = ""
            content = prepare_message(name, body)
            server.sendmail(
                sender_email,
                email,
                content,
            )
