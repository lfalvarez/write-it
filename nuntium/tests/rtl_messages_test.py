# coding=utf-8
from global_test_case import GlobalTestCase as TestCase
from ..models import Message, WriteItInstance
from popit.models import Person

class RTLTextInMessages(TestCase):
    def setUp(self):
        super(RTLTextInMessages,self).setUp()
        self.writeitinstance1 = WriteItInstance.objects.all()[0]
        self.person1 = Person.objects.all()[0]
        self.person2 = Person.objects.all()[1]

    def test_create_a_message_with_subject_and_content(self):

    	content = u"فإنها تجعل من بين أهدافها تحقيق الوحدة الإفريقية"
    	subject = u"كما تؤكد عزمها على مواصلة العمل للمحافظة على السلام والأمن في العالم"
    	message = Message.objects.create(content=content, subject=subject, \
    		persons=[self.person1,self.person2],
    		writeitinstance=self.writeitinstance1)

    	message_from_db = Message.objects.get(id=message.id)
    	self.assertEquals(message_from_db.content, content)
    	self.assertEquals(message_from_db.subject, subject)
    	self.assertTrue(len(message_from_db.slug))