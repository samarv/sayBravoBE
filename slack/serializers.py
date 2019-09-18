from django.contrib.auth.models import User, Group
from .models import organizations, users, shoutouts
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class OrganizationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = organizations
        fields = ['name', 'slack_org_id', 'channel_name',
                  'channel_id', 'access_token', 'bot_access_token']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
