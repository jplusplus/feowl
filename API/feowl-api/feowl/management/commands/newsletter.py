from django.core.management.base import NoArgsCommand
from feowl.models import Contributor


class Command(NoArgsCommand):
    help = 'Send newsletter to a range of contributors'

    def  handle_noargs(self, **options):
        contributors = Contributor.objects.all().exclude(name="Anonymous")
        for user in contributors:
            if user.email:
                print "{0} - {1}".format(user.name, user.email)
