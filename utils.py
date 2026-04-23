import string
import smtplib
import secrets
import streamlit as st
from email.message import EmailMessage

def send_email(receiver_email, content, subject):
    
    smtp_port = 465
    smtp_server = st.secrets['emails']['smtp_server']
    sender_email = st.secrets['emails']['smtp_user']
    sender_password = st.secrets['emails']['smtp_password']

    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True
    except Exception:
        return False

def generate_verification_code():
    
    return ''.join(secrets.choice(string.digits) for _ in range(4))

def apply_otp_style(label_text="Код"):
    
    style = f"""
    <style>
    input[aria-label='{label_text}'] {{
        text-align: center !important;
        letter-spacing: 10px !important;
    }}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

