# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WriteItInstance'
        db.create_table(u'nuntium_writeitinstance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('moderation_needed_in_all_messages', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='writeitinstances', to=orm['auth.User'])),
            ('allow_messages_using_form', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('rate_limiter', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('notify_owner_when_new_answer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('autoconfirm_api_messages', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'nuntium', ['WriteItInstance'])

        # Adding model 'Membership'
        db.create_table(u'nuntium_membership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['popolo.Person'])),
            ('writeitinstance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nuntium.WriteItInstance'])),
        ))
        db.send_create_signal(u'nuntium', ['Membership'])

        # Adding model 'MessageRecord'
        db.create_table(u'nuntium_messagerecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('datetime', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 11, 19, 0, 0))),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'nuntium', ['MessageRecord'])

        # Adding model 'Message'
        db.create_table(u'nuntium_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author_name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('author_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('writeitinstance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nuntium.WriteItInstance'])),
            ('confirmated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('moderated', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'nuntium', ['Message'])

        # Adding model 'Answer'
        db.create_table(u'nuntium_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['popolo.Person'])),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['nuntium.Message'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'nuntium', ['Answer'])

        # Adding model 'NoContactOM'
        db.create_table(u'nuntium_nocontactom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nuntium.Message'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='new', max_length='10')),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['popolo.Person'])),
        ))
        db.send_create_signal(u'nuntium', ['NoContactOM'])

        # Adding model 'OutboundMessage'
        db.create_table(u'nuntium_outboundmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nuntium.Message'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='new', max_length='10')),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactos.Contact'])),
        ))
        db.send_create_signal(u'nuntium', ['OutboundMessage'])

        # Adding model 'OutboundMessageIdentifier'
        db.create_table(u'nuntium_outboundmessageidentifier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('outbound_message', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['nuntium.OutboundMessage'], unique=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'nuntium', ['OutboundMessageIdentifier'])

        # Adding model 'OutboundMessagePluginRecord'
        db.create_table(u'nuntium_outboundmessagepluginrecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('outbound_message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nuntium.OutboundMessage'])),
            ('plugin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djangoplugins.Plugin'])),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('number_of_attempts', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('try_again', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'nuntium', ['OutboundMessagePluginRecord'])

        # Adding model 'ConfirmationTemplate'
        db.create_table(u'nuntium_confirmationtemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('writeitinstance', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['nuntium.WriteItInstance'], unique=True)),
            ('content_html', self.gf('django.db.models.fields.TextField')(default='Hello {{ confirmation.message.author_name }}:<br />\nWe have received a message written by you in {{ site.current_site.domain }}.<br />\nThe message was:<br />\n<strong>Subject: </strong> {{ confirmation.message.subject }} <br/>\n<strong>Content: </strong> {{ confirmation.message.content|linebreaks }} <br />\n<strong>To: </strong>\n<ul>\n\t{% for person in confirmation.message.people %}\n\t<li>{{ person.name }}</li>\n\t{% endfor %}\n</ul>\n<br />\n\nPlease confirm that you have sent this message by clicking on the next link<br />\n<br />\n<a href="{{ confirmation_full_url }}">{{ confirmation_full_url }}</a>.\n<br />\n{% if confirmation.message.public %}\n<br />\nOnce you have confirmed, you will be able to access your message if you go to the next url<br />\n<br />\n<a href="{{ message_full_url }}">{{ message_full_url }}</a>.\n{% endif %}\n<br />\n\nThanks\n\nThe writeit team.')),
            ('content_text', self.gf('django.db.models.fields.TextField')(default='Hello {{ confirmation.message.author_name }}:\nWe have received a message written by you in {{ site.current_site.domain }}.\nThe message was:\nSubject:  {{ confirmation.message.subject }} \nContent:  {{ confirmation.message.content|linebreaks }}\nTo: {% for person in confirmation.message.people %}\n{{ person.name }}\n{% endfor %}\n\nPlease confirm that you have sent this message by copiying the next url in your browser.\n\n\n{{ confirmation_full_url }}.\n{% if confirmation.message.public %}\n\nOnce you have confirmed, you will be able to access your message if you go to the next url\n\n\n{{ message_full_url }}.\n\n{% endif %}\n\nThanks.\n\nThe writeit team.')),
            ('subject', self.gf('django.db.models.fields.CharField')(default='Confirmation email for a message in WriteIt\n', max_length=512)),
        ))
        db.send_create_signal(u'nuntium', ['ConfirmationTemplate'])

        # Adding model 'Confirmation'
        db.create_table(u'nuntium_confirmation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['nuntium.Message'], unique=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('created', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 11, 19, 0, 0))),
            ('confirmated_at', self.gf('django.db.models.fields.DateField')(default=None, null=True)),
        ))
        db.send_create_signal(u'nuntium', ['Confirmation'])

        # Adding model 'Moderation'
        db.create_table(u'nuntium_moderation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.OneToOneField')(related_name='moderation', unique=True, to=orm['nuntium.Message'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'nuntium', ['Moderation'])

        # Adding model 'AnswerWebHook'
        db.create_table(u'nuntium_answerwebhook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('writeitinstance', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answer_webhooks', to=orm['nuntium.WriteItInstance'])),
        ))
        db.send_create_signal(u'nuntium', ['AnswerWebHook'])

        # Adding model 'Subscriber'
        db.create_table(u'nuntium_subscriber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subscribers', to=orm['nuntium.Message'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'nuntium', ['Subscriber'])

        # Adding model 'NewAnswerNotificationTemplate'
        db.create_table(u'nuntium_newanswernotificationtemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('writeitinstance', self.gf('django.db.models.fields.related.OneToOneField')(related_name='new_answer_notification_template', unique=True, to=orm['nuntium.WriteItInstance'])),
            ('template_html', self.gf('django.db.models.fields.TextField')(default='Dear {{user}}: <br/>\n<br/>\nWe received an answer from {{person}} to your message "{{message.subject}}" and the answer is:<br/>\n<br/>\n{{answer.content}}<br/>\n<br/>\nThanks for using Write-It<br/>\n-- <br/>\nThe Write-it Team')),
            ('template_text', self.gf('django.db.models.fields.TextField')(default='Dear {{user}}:\n\nWe received an answer from {{person}} to your message "{{message.subject}}" and the answer is:\n\n{{answer.content}}\n\nThanks for using Write-It\n-- \nThe Write-it Team')),
            ('subject_template', self.gf('django.db.models.fields.CharField')(default='%(person)s has answered to your message %(message)s', max_length=255)),
        ))
        db.send_create_signal(u'nuntium', ['NewAnswerNotificationTemplate'])

        # Adding model 'RateLimiter'
        db.create_table(u'nuntium_ratelimiter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('writeitinstance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nuntium.WriteItInstance'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('day', self.gf('django.db.models.fields.DateField')()),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal(u'nuntium', ['RateLimiter'])


    def backwards(self, orm):
        # Deleting model 'WriteItInstance'
        db.delete_table(u'nuntium_writeitinstance')

        # Deleting model 'Membership'
        db.delete_table(u'nuntium_membership')

        # Deleting model 'MessageRecord'
        db.delete_table(u'nuntium_messagerecord')

        # Deleting model 'Message'
        db.delete_table(u'nuntium_message')

        # Deleting model 'Answer'
        db.delete_table(u'nuntium_answer')

        # Deleting model 'NoContactOM'
        db.delete_table(u'nuntium_nocontactom')

        # Deleting model 'OutboundMessage'
        db.delete_table(u'nuntium_outboundmessage')

        # Deleting model 'OutboundMessageIdentifier'
        db.delete_table(u'nuntium_outboundmessageidentifier')

        # Deleting model 'OutboundMessagePluginRecord'
        db.delete_table(u'nuntium_outboundmessagepluginrecord')

        # Deleting model 'ConfirmationTemplate'
        db.delete_table(u'nuntium_confirmationtemplate')

        # Deleting model 'Confirmation'
        db.delete_table(u'nuntium_confirmation')

        # Deleting model 'Moderation'
        db.delete_table(u'nuntium_moderation')

        # Deleting model 'AnswerWebHook'
        db.delete_table(u'nuntium_answerwebhook')

        # Deleting model 'Subscriber'
        db.delete_table(u'nuntium_subscriber')

        # Deleting model 'NewAnswerNotificationTemplate'
        db.delete_table(u'nuntium_newanswernotificationtemplate')

        # Deleting model 'RateLimiter'
        db.delete_table(u'nuntium_ratelimiter')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contactos.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contactos.ContactType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_bounced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['auth.User']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popolo.Person']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'contactos.contacttype': {
            'Meta': {'object_name': 'ContactType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'djangoplugins.plugin': {
            'Meta': {'ordering': "(u'_order',)", 'unique_together': "(('point', 'name'),)", 'object_name': 'Plugin'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'point': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangoplugins.PluginPoint']"}),
            'pythonpath': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'djangoplugins.pluginpoint': {
            'Meta': {'object_name': 'PluginPoint'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pythonpath': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nuntium.answer': {
            'Meta': {'object_name': 'Answer'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['nuntium.Message']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popolo.Person']"})
        },
        u'nuntium.answerwebhook': {
            'Meta': {'object_name': 'AnswerWebHook'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'writeitinstance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answer_webhooks'", 'to': u"orm['nuntium.WriteItInstance']"})
        },
        u'nuntium.confirmation': {
            'Meta': {'object_name': 'Confirmation'},
            'confirmated_at': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 11, 19, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'message': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['nuntium.Message']", 'unique': 'True'})
        },
        u'nuntium.confirmationtemplate': {
            'Meta': {'object_name': 'ConfirmationTemplate'},
            'content_html': ('django.db.models.fields.TextField', [], {'default': '\'Hello {{ confirmation.message.author_name }}:<br />\\nWe have received a message written by you in {{ site.current_site.domain }}.<br />\\nThe message was:<br />\\n<strong>Subject: </strong> {{ confirmation.message.subject }} <br/>\\n<strong>Content: </strong> {{ confirmation.message.content|linebreaks }} <br />\\n<strong>To: </strong>\\n<ul>\\n\\t{% for person in confirmation.message.people %}\\n\\t<li>{{ person.name }}</li>\\n\\t{% endfor %}\\n</ul>\\n<br />\\n\\nPlease confirm that you have sent this message by clicking on the next link<br />\\n<br />\\n<a href="{{ confirmation_full_url }}">{{ confirmation_full_url }}</a>.\\n<br />\\n{% if confirmation.message.public %}\\n<br />\\nOnce you have confirmed, you will be able to access your message if you go to the next url<br />\\n<br />\\n<a href="{{ message_full_url }}">{{ message_full_url }}</a>.\\n{% endif %}\\n<br />\\n\\nThanks\\n\\nThe writeit team.\''}),
            'content_text': ('django.db.models.fields.TextField', [], {'default': "'Hello {{ confirmation.message.author_name }}:\\nWe have received a message written by you in {{ site.current_site.domain }}.\\nThe message was:\\nSubject:  {{ confirmation.message.subject }} \\nContent:  {{ confirmation.message.content|linebreaks }}\\nTo: {% for person in confirmation.message.people %}\\n{{ person.name }}\\n{% endfor %}\\n\\nPlease confirm that you have sent this message by copiying the next url in your browser.\\n\\n\\n{{ confirmation_full_url }}.\\n{% if confirmation.message.public %}\\n\\nOnce you have confirmed, you will be able to access your message if you go to the next url\\n\\n\\n{{ message_full_url }}.\\n\\n{% endif %}\\n\\nThanks.\\n\\nThe writeit team.'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'default': "'Confirmation email for a message in WriteIt\\n'", 'max_length': '512'}),
            'writeitinstance': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['nuntium.WriteItInstance']", 'unique': 'True'})
        },
        u'nuntium.membership': {
            'Meta': {'object_name': 'Membership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popolo.Person']"}),
            'writeitinstance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nuntium.WriteItInstance']"})
        },
        u'nuntium.message': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Message'},
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'confirmated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderated': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'writeitinstance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nuntium.WriteItInstance']"})
        },
        u'nuntium.messagerecord': {
            'Meta': {'object_name': 'MessageRecord'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'datetime': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 11, 19, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nuntium.moderation': {
            'Meta': {'object_name': 'Moderation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'message': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'moderation'", 'unique': 'True', 'to': u"orm['nuntium.Message']"})
        },
        u'nuntium.newanswernotificationtemplate': {
            'Meta': {'object_name': 'NewAnswerNotificationTemplate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject_template': ('django.db.models.fields.CharField', [], {'default': "'%(person)s has answered to your message %(message)s'", 'max_length': '255'}),
            'template_html': ('django.db.models.fields.TextField', [], {'default': '\'Dear {{user}}: <br/>\\n<br/>\\nWe received an answer from {{person}} to your message "{{message.subject}}" and the answer is:<br/>\\n<br/>\\n{{answer.content}}<br/>\\n<br/>\\nThanks for using Write-It<br/>\\n-- <br/>\\nThe Write-it Team\''}),
            'template_text': ('django.db.models.fields.TextField', [], {'default': '\'Dear {{user}}:\\n\\nWe received an answer from {{person}} to your message "{{message.subject}}" and the answer is:\\n\\n{{answer.content}}\\n\\nThanks for using Write-It\\n-- \\nThe Write-it Team\''}),
            'writeitinstance': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'new_answer_notification_template'", 'unique': 'True', 'to': u"orm['nuntium.WriteItInstance']"})
        },
        u'nuntium.nocontactom': {
            'Meta': {'object_name': 'NoContactOM'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nuntium.Message']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['popolo.Person']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': "'10'"})
        },
        u'nuntium.outboundmessage': {
            'Meta': {'object_name': 'OutboundMessage'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contactos.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nuntium.Message']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': "'10'"})
        },
        u'nuntium.outboundmessageidentifier': {
            'Meta': {'object_name': 'OutboundMessageIdentifier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'outbound_message': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['nuntium.OutboundMessage']", 'unique': 'True'})
        },
        u'nuntium.outboundmessagepluginrecord': {
            'Meta': {'object_name': 'OutboundMessagePluginRecord'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_attempts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'outbound_message': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nuntium.OutboundMessage']"}),
            'plugin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangoplugins.Plugin']"}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'try_again': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'nuntium.ratelimiter': {
            'Meta': {'object_name': 'RateLimiter'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'day': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'writeitinstance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nuntium.WriteItInstance']"})
        },
        u'nuntium.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subscribers'", 'to': u"orm['nuntium.Message']"})
        },
        u'nuntium.writeitinstance': {
            'Meta': {'object_name': 'WriteItInstance'},
            'allow_messages_using_form': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'autoconfirm_api_messages': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderation_needed_in_all_messages': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notify_owner_when_new_answer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'writeitinstances'", 'to': u"orm['auth.User']"}),
            'persons': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'writeit_instances'", 'symmetrical': 'False', 'through': u"orm['nuntium.Membership']", 'to': u"orm['popolo.Person']"}),
            'rate_limiter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'popolo.person': {
            'Meta': {'object_name': 'Person'},
            'additional_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'created_at': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'death_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'honorific_prefix': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'honorific_suffix': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'patronymic_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'}),
            'sort_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'updated_at': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['nuntium']