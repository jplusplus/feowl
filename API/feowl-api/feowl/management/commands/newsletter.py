from django.core.management.base import NoArgsCommand
from feowl.models import Contributor
import settings


class Command(NoArgsCommand):
    help = 'Send newsletter to a range of contributors'

    def  handle_noargs(self, **options):
        contributors = Contributor.objects.all().exclude(name=settings.ANONYMOUS_USER_NAME).order_by('enquiry')
        for user in contributors:
            if user.email:
                print "{0} - {1} -- {2}".format(user.name, user.email, user.enquiry)
