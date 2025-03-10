# OTP:
import random
def generate_otp(length=6):
    digits = "0123456789"
    OTP = ""
    for _ in range(length):
        OTP += random.choice(digits)
    return OTP

# Generate a 6-digit OTP:
otp = generate_otp()
print("Generated OTP:", otp)
"""
# OTP in phone number:
import random
from twilio.rest import Client

# Function to generate OTP
def generate_otp(length=6):
    digits = "0123456789"
    OTP = ""
    for _ in range(length):
        OTP += random.choice(digits)
    return OTP

# Function to send OTP via SMS
def send_otp_via_sms(otp, phone_number):
    # Twilio credentials
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_phone_number = 'your_twilio_phone_number'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Your OTP code is {otp}',
        from_=twilio_phone_number,
        to=phone_number
    )

    print(f"Message sent with SID: {message.sid}")

# Generate a 6-digit OTP
otp = generate_otp()
print("Generated OTP:", otp)

# Send the OTP via SMS
send_otp_via_sms(otp, '+1234567890')"""

# OTP in Email Address:
"""import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(otp, to_email):
    from_email = "your-email@gmail.com"
    password = "your-email-password"

    # Set up the server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login to the email account
    server.login(from_email, password)

    # Create the email content
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = "Your OTP Code"
    body = f"Your OTP code is {otp}"
    msg.attach(MIMEText(body, "plain"))

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())

    # Close the server connection
    server.quit()

# Generate a 6-digit OTP
otp = generate_otp()
print("Generated OTP:", otp)

# Send the OTP via email
send_email(otp, "recipient-email@example.com")"""