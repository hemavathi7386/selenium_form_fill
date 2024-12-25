from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 587  
app.config['MAIL_USE_TLS'] = True  
app.config['MAIL_USE_SSL'] = False  
app.config['MAIL_USERNAME'] = 'neelirothuh@gmail.com'  
app.config['MAIL_PASSWORD'] = 'degq hzsw ffuk zzqc'  
app.config['MAIL_DEFAULT_SENDER'] = 'neelirothuh@gmail.com'  

mail = Mail(app)

@app.route('/send-assignment', methods=['GET'])
def send_assignment():
    subject = "Python (Selenium) Assignment - Hemavathi"
    recipients = ['tech@themedius.ai']  
    cc = ['hr@themedius.ai']  
    msg = Message(subject, recipients=recipients, cc=cc)

    msg.body = """Dear Team,

Please find attached the required items for the Python (Selenium) assignment submission:
1. Screenshot of the form filled.
2. Source code link (GitHub).-https://github.com/hemavathi7386/selenium_form_fill

3. Documentation.
4. Resume.
5. Past projects/work samples.
data scraping -https://colab.research.google.com/drive/1GO6gsP4k6PAl-Jxx3GFQJNZtkMQaO2-_?authuser=2
data science-project -https://huggingface.co/spaces/Hemavathineelirothu/diabetic_retinopath
6. Yes I am available for full time

Thanks & Regards,
N.Hemavathi
"""

    # Attach files
    files_to_attach = [
        'confirmation_page.png',       # Screenshot of the form
        'medius Tec.docx',    # Documentation
        'Untitled5.ipynb',           # Resume
        'filled_form.pdf',         
    ]

    for file in files_to_attach:
        try:
            with open(file, 'rb') as f:
                msg.attach(file, 'application/octet-stream', f.read())
        except FileNotFoundError:
            return f"Error: File {file} not found. Please ensure all files are in the same directory as the script."

    try:
        mail.send(msg)
        return "Email sent successfully with all attachments!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
