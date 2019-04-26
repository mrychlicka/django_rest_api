# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView


class PersonalInformation(APIView):

    def get(self):
        response_data = {
            'name': 'Malgorzata',
            'last name': 'Rychlicka',
        }

        return Response(response_data)


class Localization(APIView):

    def get(self):
        response_json = {
            'country': 'poland',
            'city': 'poznan'
        }
        return Response(response_json)
