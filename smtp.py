import smtplib
import time
import sys
import textwrap



SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587



def plain_email(smtp_acct, smtp_pass, tgt_acct, subject, contents):
    message = textwrap.dedent(f'''
           Subject: {subject}
           From: {smtp_acct}
           To: {tgt_acct}

           {contents.decode()}
            ''')

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls() #TLS
    server.login(smtp_acct, smtp_pass)

    server.sendmail(smtp_acct, tgt_acct, message)

    time.sleep(1)
    server.quit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python smtp.py [account] [password] [target accounts]")
        sys.exit()

    smtp_acct = sys.argv[1]
    smtp_pass = sys.argv[2]
    tgt_acct = sys.argv[3]
    # subject: String // contents: Bytes
    subject = "HEEEEEE"
    contents = b'12345454'

    plain_email(smtp_acct, smtp_pass, tgt_acct, subject, contents)
