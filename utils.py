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
        font-family: monospace !important;
        letter-spacing: 12px !important;
        caret-color: transparent !important;
        text-indent: 9px !important;
    }}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

import streamlit as st

def st_funny(text, size=40, color="#FF4B4B", center=True):

    align = "center" if center else "left"
    style = f"""
    <style>
    @import url('https://googleapis.com');
    .funny-container {{
        font-family: 'Comic Neue' !important;
        font-size: {size}px;
        color: {color};
        text-align: {align};
        font-weight: 700;
        margin: 10px 0px;
    }}
    </style>
    <div class="funny-container">{text}</div>
    """
    st.markdown(style, unsafe_allow_html=True)

def st_pixel(text, size=20, color="#00FF00", center=True):
    align = "center" if center else "left"
    st.markdown(
        f"""
        <style>
        /* Импорт должен быть в самом верху блока style */
        @import url('https://googleapis.com');
        
        .pixel-label {{
            font-family: 'Press Start 2P', system-ui !important;
            font-size: {size}px !important;
            color: {color} !important;
            text-align: {align} !important;
            display: block !important;
            width: 100%;
        }}
        </style>
        <span class="pixel-label">{text}</span>
        """,
        unsafe_allow_html=True
    )

