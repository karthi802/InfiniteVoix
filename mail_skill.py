import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Email account details
def sendEmail(recipient_email,subject,content):
    email_address = "karthi2003ind@gmail.com"
    password = "bfgp mthu sfqy qhyf"

    # Create a message object
    message = MIMEMultipart()
    message["From"] = email_address
    message["To"] = recipient_email
    message["Subject"] = subject


    # Email body
    message.attach(MIMEText(content, "plain"))

    # Attach a file (optional)
    # file_path = "path_to_attachment.pdf"
    # with open(file_path, "rb") as attachment:
    #     part = MIMEApplication(attachment.read(), Name="attachment.pdf")
    #     part['Content-Disposition'] = f'attachment; filename="{file_path}"'
    #     message.attach(part)

    # Connect to the SMTP server (Gmail, in this example)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, password)

    # Send the email
    server.sendmail(email_address, recipient_email, message.as_string())

    # Quit the server
    server.quit()
