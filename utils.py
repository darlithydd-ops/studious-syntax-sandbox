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

def apply_comic_style(text, size=40, color='#FF4B4B', center=True):
    align = 'center' if center else 'left'
    style = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@700&display=swap');
    .comic-container {{
        font-family: 'Comic Neue', cursive !important;
        font-size: {size}px !important;
        color: {color} !important;
        text-align: {align} !important;
        font-weight: 700 !important;
        margin: 10px 0px;}}
    </style>
    <div class='comic-container'>{text}</div>
    """
    st.markdown(style, unsafe_allow_html=True)

def apply_pixel_style(text, size=20, color='#FF4B4B', center=True):
    align = 'center' if center else 'left'
    style = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    .pixel-container {{
        font-family: 'Press Start 2P', monospace !important;
        font-size: {size}px !important;
        color: {color} !important;
        text-align: {align} !important;
        line-height: 1.5 !important;}}
    </style>
    <div class='pixel-container'>{text}</div>
    """
    st.markdown(style, unsafe_allow_html=True)
    
def apply_caveat_style(text, size=40, color='#FF4B4B', center=True):
    align = 'center' if center else 'left'
    style = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&display=swap');
    .caveat-container {{
        font-family: 'Caveat', cursive !important;
        font-size: {size}px !important;
        color: {color} !important;
        text-align: {align} !important;
        font-weight: 700 !important;
        margin: 10px 0px;}}
    </style>
    <div class='caveat-container'>{text}</div>
    """
    st.markdown(style, unsafe_allow_html=True)

def st_error_centered(text):
    style = """
    <style>
    div[data-testid="stAlert"] {text-align: center !important;}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)
    st.error(text)

