
# https://www.django-rest-framework.org/tutorial/quickstart/

from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']
