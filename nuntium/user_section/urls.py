from django.conf.urls import patterns, include, url
from .views import UserAccountView, WriteItInstanceUpdateView, \
        YourContactsView, YourInstancesView, WriteItInstanceAdvancedUpdateView, \
        WriteItInstanceTemplateUpdateView, NewAnswerNotificationTemplateUpdateView, \
        ConfirmationTemplateUpdateView, WriteItInstanceCreateView, \
        MessagesPerWriteItInstance, \
        MessageDetail, MessageDelete, AnswerCreateView, ModerationView, AnswerUpdateView
        
urlpatterns = patterns('',
    url(r'^accounts/profile/?$', UserAccountView.as_view(), name='account'),
    url(r'^accounts/your_contacts/?$', YourContactsView.as_view(), name='your-contacts'),
    url(r'^accounts/your_instances/?$', YourInstancesView.as_view(), name='your-instances'),
    url(r'^writeitinstance/edit/(?P<pk>[-\d]+)/?$', WriteItInstanceUpdateView.as_view(), \
        name = 'writeitinstance_basic_update'),
    url(r'^writeitinstance/advanced_edit/(?P<pk>[-\d]+)/?$', \
        WriteItInstanceAdvancedUpdateView.as_view(), \
        name = 'writeitinstance_advanced_update'),
    url(r'^writeitinstance/(?P<pk>[-\d]+)/messages/?$', \
        MessagesPerWriteItInstance.as_view(), \
        name = 'messages_per_writeitinstance'),
    url(r'^message/(?P<pk>[-\d]+)/answers/?$', \
        MessageDetail.as_view(), \
        name = 'message_detail'),
    url(r'^message/(?P<pk>[-\d]+)/create_answers/?$', \
        AnswerCreateView.as_view(), \
        name = 'create_answer'), 
    url(r'^message/answers/update_answers/(?P<pk>[-\d]+)/?$', \
        AnswerUpdateView.as_view(), \
        name = 'update_answer'), 
    url(r'^message/(?P<pk>[-\d]+)/delete/?$', \
        MessageDelete.as_view(), \
        name = 'message_delete'),
    
    url(r'^message/(?P<pk>[-\d]+)/moderate/?$', \
        ModerationView.as_view(), \
        name = 'moderate_message'),


    url(r'^writeitinstance/edit/(?P<pk>[-\d]+)/templates/?$', \
        WriteItInstanceTemplateUpdateView.as_view(), \
        name = 'writeitinstance_template_update'),
    url(r'^writeitinstance/edit/(?P<pk>[-\d]+)/templates/new_answer_notification/?$',
        NewAnswerNotificationTemplateUpdateView.as_view(),
        name = 'edit_new_answer_notification_template'),
    url(r'^writeitinstance/edit/(?P<pk>[-\d]+)/templates/confirmation_template/?$',
        ConfirmationTemplateUpdateView.as_view(),
        name = 'edit_confirmation_template'),
    url(r'^writeitinstance/create/?$',
        WriteItInstanceCreateView.as_view(),
        name = 'create_writeit_instance'),
    )
