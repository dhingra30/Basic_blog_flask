from smtplib import SMTP


class SendEmail:
    def __init__(self, message):
        self.message = message

    def send_message(self):
        with SMTP("smtp.gmail.com", 587) as email:
            email.starttls()
            email.login(user="rahuldhingraajd@gmail.com", password="zkds fsul vwmw yofg")
            email.sendmail(to_addrs="rahuldhingraajd@gmail.com", from_addr="rahuldhingraajd@gmail.com",
                           msg=self.message)

