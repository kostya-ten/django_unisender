import os

from django.test import TestCase
from django_tasker_unisender import unisender
from django.conf import settings


class BaseTest(TestCase):
    def setUp(self) -> None:
        self.unisender = unisender.Unisender(
            api_key=getattr(settings, 'UNISENDER_API_KEY', os.environ.get('UNISENDER_API_KEY'))
        )

    def test_list(self):

        list_id = self.unisender.create_list(title="test_py")
        self.assertRegex(str(list_id), '^[0-9]+$')

        test_data = None
        for item in self.unisender.get_lists():
            if item.get('title') == 'test_py':
                test_data = item

        if not test_data:
            raise Exception('Not found test_py')

        self.unisender.delete_list(list_id=list_id)

        # list_id = unisender.create_list('')
        # self.assertRegex(str(list_id), '^[0-9]+$')
        #
        # lists = unisender.get_list()
        #
        # test_data = None
        # for item in lists:
        #     if item.get('title') == 'test_py':
        #         test_data = item
        #
        # if not test_data:
        #     raise Exception('Not found test_py')
        #
        # unisender.delete_list(list_id=list_id)

    # def test_subscribe(self):
    #     #list_id = unisender.create_list('test_py')
    #
    #     unisender.subscribe(
    #         list_id=1,
    #         fields={'fields[email]': 'kostya@yandex.ru'},
    #     )
