from django.contrib import admin
from mailit.models import MailItTemplate
from nuntium.models import WriteItInstance
from nuntium.admin import WriteItInstanceAdmin

class MailItTemplateInline(admin.ModelAdmin):
	pass

admin.site.register(MailItTemplate, MailItTemplateInline)