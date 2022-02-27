from rest_framework import serializers
from resume.models import Experience, ExperienceDescription, TechSkill, TechSkillCategory


class TechSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechSkill
        fields = '__all__'

    def to_representation(self, instance):
        return instance.name


class ExperienceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceDescription
        fields = ('id', 'order', 'bullet')

    def to_representation(self, instance):
        return [instance.order, instance.bullet]


class ExperienceSerializer(serializers.ModelSerializer):
    skills = TechSkillSerializer(many=True, read_only=True)
    experiencedescription_set = ExperienceDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = '__all__'
