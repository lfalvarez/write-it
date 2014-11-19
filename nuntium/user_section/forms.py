# coding=utf-8
from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple, \
                        CharField, EmailField, SelectMultiple, TextInput, Textarea, \
                        URLField, IntegerField, CheckboxInput, NumberInput, URLInput, \
                        Select
from ..models import Message, WriteItInstance, OutboundMessage, \
    Confirmation, Membership, NewAnswerNotificationTemplate, \
    ConfirmationTemplate, Answer
from contactos.models import Contact
from django.forms import ValidationError, ModelChoiceField
from django.utils.translation import ugettext as _
from popolo.models import Person
from haystack.forms import SearchForm
from django.utils.html import format_html
from django.forms.util import flatatt
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from itertools import chain
from ..forms import WriteItInstanceCreateForm


class WriteItInstanceBasicForm(ModelForm):
    class Meta:
        model = WriteItInstance
        fields = ['name', 'persons']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'persons': SelectMultiple(attrs={'class': 'form-control chosen-person-select'}),
        }

class WriteItInstanceAdvancedUpdateForm(ModelForm):
    class Meta:
        model = WriteItInstance
        fields = ['moderation_needed_in_all_messages', \
        'allow_messages_using_form', \
        'rate_limiter', \
        'notify_owner_when_new_answer', \
        'autoconfirm_api_messages'
        ]
        widgets = {
            'moderation_needed_in_all_messages': CheckboxInput(attrs={'class': 'form-control'}),
            'allow_messages_using_form': CheckboxInput(attrs={'class': 'form-control'}),
            'rate_limiter': NumberInput(attrs={'class': 'form-control'}),
            'notify_owner_when_new_answer': CheckboxInput(attrs={'class': 'form-control'}),
            'autoconfirm_api_messages': CheckboxInput(attrs={'class': 'form-control'}),
        }

class NewAnswerNotificationTemplateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.writeitinstance = kwargs.pop('writeitinstance')
        super(NewAnswerNotificationTemplateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        template = super(NewAnswerNotificationTemplateForm, self).save(commit=False)
        template.writeitinstance = self.writeitinstance
        if commit:
            template.save()
        return template

    class Meta:
        model = NewAnswerNotificationTemplate
        fields = ['subject_template', 'template_html', 'template_text']

        widgets = {
            'subject_template': TextInput(attrs={'class': 'form-control'}),
            'template_html': Textarea(attrs={'class': 'form-control'}),
            'template_text': Textarea(attrs={'class': 'form-control'}),
        }

class ConfirmationTemplateForm(ModelForm):
    class Meta:
        model = ConfirmationTemplate
        fields = ['subject','content_html','content_text',]
        widgets = {
            'subject': TextInput(attrs={'class': 'form-control'}),
            'content_html': Textarea(attrs={'class': 'form-control'}),
            'content_text': Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args,**kwargs):
        if "writeitinstance" not in kwargs:
            raise ValidationError(_("WriteIt Instance not present"))
        self.writeitinstance = kwargs.pop("writeitinstance")
        super(ConfirmationTemplateForm, self).__init__(*args, **kwargs)

class SimpleInstanceCreateForm(WriteItInstanceCreateForm):
    class Meta:
        model = WriteItInstance
        fields = ('owner', 'name')

class WriteItInstanceCreateForm(WriteItInstanceCreateForm):
    class Meta:
        model = WriteItInstance
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        if 'owner' in kwargs:
            self.owner = kwargs.pop('owner')
        super(WriteItInstanceCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(WriteItInstanceCreateForm, self).save(commit=False)
        instance.owner = self.owner
        instance.save()
        self.relate_with_people()
        return instance

class AnswerForm(ModelForm):

    person = ModelChoiceField(queryset=Person.objects.none())
    class Meta:
        model = Answer
        fields = ('person', 'content')
        widgets = {
            'content': TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        self.message = kwargs.pop('message')
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['person'].queryset = self.message.people
        self.fields['person'].widget.attrs['class'] = 'form-control'


    def save(self, commit=True):
        answer = super(AnswerForm, self).save(commit=False)
        answer.message = self.message
        answer.save()
        return answer
