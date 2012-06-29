from django.contrib.gis import admin as admin_gis
from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.views.decorators.debug import sensitive_post_parameters
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.template.response import TemplateResponse
from django.contrib import messages

from tastypie.admin import ApiKeyInline
from tastypie.models import ApiAccess, ApiKey

from models import PowerReport, Area, Device, Contributor
from forms import ContributorAdminForm

class UserModelAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [ApiKeyInline]

class ContributorAdmin(admin.ModelAdmin):
    form = ContributorAdminForm
    change_password_form = AdminPasswordChangeForm    
    change_user_password_template = None    

    def get_urls(self):
        from django.conf.urls import patterns
        return patterns('',
            (r'^(\d+)/password/$',
             self.admin_site.admin_view(self.contributor_change_password))
        ) + super(ContributorAdmin, self).get_urls()

    @sensitive_post_parameters()
    def contributor_change_password(self, request, id, form_url=''):
        if not self.has_change_permission(request):
            raise PermissionDenied
        contributor = get_object_or_404(self.queryset(request), pk=id)
        if request.method == 'POST':
            form = self.change_password_form(contributor, request.POST)
            if form.is_valid():
                form.save()
                msg = ugettext('Password changed successfully.')
                messages.success(request, msg)
                return HttpResponseRedirect('..')
        else:
            form = self.change_password_form(contributor)

        fieldsets = [(None, {'fields': form.base_fields.keys()})]
        adminForm = admin.helpers.AdminForm(form, fieldsets, {})

        context = {
            'title': _('Change password: %s') % escape(contributor.name),
            'adminForm': adminForm,
            'form_url': mark_safe(form_url),
            'form': form,
            'is_popup': '_popup' in request.REQUEST,
            'add': True,
            'change': False,
            'has_delete_permission': False,
            'has_change_permission': True,
            'has_absolute_url': False,
            'opts': self.model._meta,
            'original': contributor,
            'save_as': False,
            'show_save': True,
        }
        return TemplateResponse(request, [
            self.change_user_password_template or
            'admin/auth/user/change_password.html'
        ], context, current_app=self.admin_site.name)

admin.site.unregister(User)
admin.site.register(User, UserModelAdmin)

admin.site.register(PowerReport, admin_gis.OSMGeoAdmin)
admin.site.register(Area, admin_gis.OSMGeoAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Device)

admin.site.register(ApiKey)
admin.site.register(ApiAccess)
