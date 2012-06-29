
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext, ugettext_lazy as _
from models import PowerReport, Device, Contributor, Area

class ContributorAdminForm(forms.ModelForm):

    name = forms.RegexField(
        label=_("Name"), max_length=30, regex=r"^[\w.@+-]+$",
        help_text = _("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages = {
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password = ReadOnlyPasswordHashField(label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    def clean_password(self):
        return self.initial["password"]

    class Meta:
        model = Contributor


class ContributorForm(forms.ModelForm):
    class Meta:
        model = Contributor

class PowerReportForm(forms.ModelForm):
    class Meta:
        model = PowerReport

    def clean_duration(self):
        duration = self.cleaned_data['duration']

        #ensure that duration is a positive number (PositiveInteger fields can be == 0)
        if duration == 0:
            raise forms.ValidationError('Duration values must be larger than 0.')

        return data

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
