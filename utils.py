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

def add_otp_focus_script():
    return st.components.v1.html(
        """
        <script>
        setTimeout(() => {
            const allInputs = window.parent.document.querySelectorAll('input');
            const otpInputs = Array.from(allInputs).filter(input => input.id.includes('otp_'));
            
            otpInputs.forEach((input, index) => {
                input.addEventListener('input', () => {
                    if (input.value.length === 1 && index < otpInputs.length - 1) {
                        otpInputs[index + 1].focus();
                    }
                });
                input.addEventListener('keydown', (e) => {
                    if (e.key === 'Backspace' && input.value.length === 0 && index > 0) {
                        otpInputs[index - 1].focus();
                    }
                });
            });
        }, 500); 
        </script>
        """,
        height=0,
    )
