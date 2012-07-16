from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import get_template
from django.template import Context
from optparse import make_option
from feowl.models import Contributor
import settings


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--limit', '-l', dest='limit', default=20,
            help='Pass the Range of contributors you want to send a newsletter'),
    )
    help = 'Send newsletter to a range of contributors'

    can_import_settings = True

    def  handle(self, *args, **options):
        limit = options.get("limit")

        contributors = Contributor.objects.all().exclude(name=settings.ANONYMOUS_USER_NAME).order_by('-enquiry')[:limit]
        messages = []
        plaintext = get_template('email.txt')
        html = get_template('email.html')
        subject = 'hello'
        connection = get_connection()
        connection.open()

        for user in contributors:
            if user.email and user.name:
                print "{0} - {1} -- {2}".format(user.name, user.email, user.enquiry)
                d = Context({'name': user.name})
                text_content = plaintext.render(d)
                html_content = html.render(d)
                msg = EmailMultiAlternatives(subject, text_content, settings.NEWSLETTER_FROM, [user.email], connection=connection)
                msg.attach_alternative(html_content, "text/html")
                messages.append(msg)

        connection.send_messages(messages)
        connection.close()
