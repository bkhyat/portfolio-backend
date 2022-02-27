from rest_framework import serializers
from resume.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('order', 'value')
