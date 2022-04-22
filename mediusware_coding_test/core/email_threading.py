import threading
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EmailThread(threading.Thread):
    def __init__(
        self,
        html_content,
        subject,
        sender_email,
        receiver_email,
        reply_to_email=None,
        connection=None,
    ):
        self.html_content = html_content
        self.subject = subject
        self.sender = sender_email
        self.connection = connection
        self.recipient_list = [
            receiver_email,
        ]
        self.reply_to_email_list = []
        if reply_to_email:
            self.reply_to_email_list.append(reply_to_email)

        threading.Thread.__init__(self)

    def run(self):
        kwargs = {}
        if self.connection:
            kwargs = {"connection": self.connection}

        msg = EmailMultiAlternatives(
            subject=self.subject,
            from_email=self.sender,
            to=self.recipient_list,
            reply_to=self.reply_to_email_list,
            **kwargs,
        )
        msg.attach_alternative(self.html_content, "text/html")
        msg.content_subtype = "html"
        msg.send()


def send_html_mail(
    subject,
    context,
    html_template,
    sender_email,
    receiver_email,
    reply_to_email=None,
    connection=None,
):
    html_content = render_to_string(html_template, context)

    EmailThread(
        html_content,
        subject,
        sender_email,
        receiver_email,
        reply_to_email,
        connection=connection,
    ).start()
