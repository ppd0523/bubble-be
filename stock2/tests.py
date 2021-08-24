from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from membership.models import User
from django.utils import timezone
import json
from django.core.files.uploadedfile import SimpleUploadedFile



class ConditionTest(TestCase):
    def setUp(self) -> None:
        User(username='emma', nickname='emma_nick', password='1212').save()

        with open('stock2/tests/dummy.csv', 'rb') as dummy_f:
            file = SimpleUploadedFile('dummy.csv', content=dummy_f.read())

        with open('stock2/tests/condition.txt', 'r', encoding='utf-8') as cond_f:
            js = json.loads(cond_f.read())

            if isinstance(js, dict):
                js['file'] = file
            elif isinstance(js, list):
                for d in js:
                    d['file'] = file

        if isinstance(js, dict):
            seri = ConditionSerializer(data=js, write_only=True)
        elif isinstance(js, list):
            seri = ConditionSerializer(data=js, many=True, write_only=True)

        if seri.is_valid():
            seri.save()
        else:
            print(seri.errors)


    def tearDown(self) -> None:
        pass

    def test_reports(self):
        temp_cond = {
            'cond_order': 0,
            'cond_name': '돌파매매',
            'cond_owner': 'emma',
        }

        # self.assertDictEqual(, temp_cond, 'condition serializing fail')
        # raw1 = {"cond_index":"000","cond_name":"돌파매매","create_date":timezone.localdate()}
        # print(ConditionSerializer(data=raw1).is_valid(raise_exception=True))
