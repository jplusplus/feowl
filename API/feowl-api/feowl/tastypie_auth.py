from tastypie.authentication import ApiKeyAuthentication

class ConfigurableApiKeyAuthentication(ApiKeyAuthentication):
    """
    Just like standard APIKeyAuthentication,
    but with configurable parameters in case the parameters would be ambiguous.
    """

    def __init__(self, username_param='username', api_key_param='api_key'):
        self.username_param = username_param
        self.api_key_param = api_key_param

    def is_authenticated(self, request, **kwargs):
        """
        Finds the user and checks their API key.

        Should return either ``True`` if allowed, ``False`` if not or an
        ``HttpResponse`` if you need something custom.
        """
        from django.contrib.auth.models import User

        username = request.GET.get(self.username_param) or request.POST.get(self.username_param)
        api_key = request.GET.get(self.api_key_param) or request.POST.get(self.api_key_param)

        if not username or not api_key:
            return self._unauthorized()

        try:
            user = User.objects.get(username=username)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()

        request.user = user
        return self.get_key(user, api_key)