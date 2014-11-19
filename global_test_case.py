from django.test import TestCase
from django.utils.unittest import skipUnless
from django.core.management import call_command
from tastypie.test import ResourceTestCase
from django.conf import settings
from django.contrib.sites.models import Site
import os
import subprocess
import threading
from django.db import DEFAULT_DB_ALIAS

_LOCALS = threading.local()

def set_test_db(db_name):
    "Sets the database name to route to."
 
    setattr(_LOCALS, 'test_db_name', db_name)
 
 
def get_test_db():
    "Get the current database name or the default."
 
    return getattr(_LOCALS, 'test_db_name', DEFAULT_DB_ALIAS)
 
 
def del_test_db():
    "Clear the database name (restore default)"
 
    try:
        delattr(_LOCALS, 'test_db_name')
    except AttributeError:
        pass
 
 
class TestUsingDbRouter(object):
    "Simple router to allow DB selection by name."
 
    def db_for_read(self, model, **kwargs):
        return get_test_db()
 
    def db_for_write(self, model, **kwargs):
        return get_test_db()
 
 
class UsingDbMixin(object):
    "A mixin to allow a TestCase to select the DB to use."
 
    multi_db = True
    using_db = None
 
    def setUp(self, *args, **kwargs):
        super(UsingDbMixin, self).setUp(*args, **kwargs)
        set_test_db(self.using_db)
 
    def tearDown(self, *args, **kwargs):
        del_test_db()
        super(UsingDbMixin, self).tearDown(*args, **kwargs)

class WriteItTestCaseMixin(object):
    fixtures = ['example_data.yaml']
    def setUp(self):
        self.site = Site.objects.get_current()

    def assertModerationMailSent(self, message, moderation_mail):
        self.assertEquals(moderation_mail.to[0], message.writeitinstance.owner.email)
        self.assertTrue(message.content in moderation_mail.body)
        self.assertTrue(message.subject in moderation_mail.body)
        self.assertTrue(message.author_name in moderation_mail.body)
        self.assertTrue(message.author_email in moderation_mail.body)
        
        for person in message.people:
            self.assertTrue(person.name in moderation_mail.body)



class GlobalTestCase(WriteItTestCaseMixin, TestCase):
    pass


class ResourceGlobalTestCase(WriteItTestCaseMixin ,ResourceTestCase ):
    pass

@skipUnless(settings.LOCAL_ELASTICSEARCH, "No local elasticsearch")
class SearchIndexTestCase(GlobalTestCase):
    def setUp(self):
        super(SearchIndexTestCase, self).setUp()
        call_command('rebuild_index', verbosity=0, interactive = False)
    