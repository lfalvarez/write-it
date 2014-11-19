# coding=utf-8
from global_test_case import GlobalTestCase as TestCase
from django.core.urlresolvers  import reverse
from django.core.urlresolvers import reverse as original_reverse
from ..models import WriteItInstance, Message
from django.test.client import Client, RequestFactory
from django.contrib.sites.models import Site
from django.conf import settings
from popolo.models import Person


class MessagesPerPersonViewTestCase(TestCase):
	def setUp(self):
		super(MessagesPerPersonViewTestCase, self).setUp()
		self.writeitinstance = WriteItInstance.objects.get(id=1)
		self.pedro = Person.objects.get(name="Pedro")
		self.marcel = Person.objects.get(name="Marcel")
		self.client = Client()

	def test_has_an_url(self):
		url = reverse('messages_per_person'
			, kwargs={
				'pk':self.pedro.id,
				'slug':self.writeitinstance.slug

				})

		self.assertTrue(url)


	def test_it_is_reachable(self):
		url = reverse('messages_per_person'
			, kwargs={
			'pk':self.pedro.id,
			'slug':self.writeitinstance.slug
			})
		response = self.client.get(url)

		expected_messages = Message.objects.filter(
			person=self.pedro,
			confirmated=True,
			writeitinstance=self.writeitinstance)

		self.assertEquals(response.status_code, 200)
		self.assertIn('person', response.context)
		self.assertEquals(response.context['person'], self.pedro)
		self.assertIn('message_list', response.context)
		self.assertQuerysetEqual(
		    expected_messages,
		    [repr(r) for r in response.context['message_list']]
		)
		self.assertTemplateUsed(response, 'nuntium/message/per_person.html')
		self.assertTemplateUsed(response, 'base.html')

	def test_it_does_not_show_private_messages(self):
		private_message = Message.objects.create(content = 'Content 1', 
            author_name='Felipe', 
            author_email="falvarez@votainteligente.cl", 
            subject='Fiera es una perra feroz', 
            writeitinstance= self.writeitinstance,
            public=False,
            confirmated = True,
            persons = [self.pedro])
		private_message.moderate()

		#this private message should not be shown

		url = reverse('messages_per_person'
			, kwargs={
				'pk':self.pedro.id,
				'slug':self.writeitinstance.slug
				})

		response = self.client.get(url)

		self.assertNotIn(private_message, response.context['message_list'])


	def test_show_only_messages_that_are_related_to_the_writeitinstance(self):
		the_other_instance = WriteItInstance.objects.get(id=2)

		message = Message.objects.create(content = 'Content 1', 
            author_name='Felipe', 
            author_email="falvarez@votainteligente.cl", 
            subject='Fiera es una perra feroz', 
            writeitinstance= the_other_instance,
            public=True,
            confirmated = True,
            persons = [self.pedro])

		url = reverse('messages_per_person'
			, kwargs={
				'pk':self.pedro.id,
				'slug':self.writeitinstance.slug
				})

		response = self.client.get(url)

		#should not be here cause it belongs to other writeit instance
		self.assertNotIn(message, response.context['message_list'])