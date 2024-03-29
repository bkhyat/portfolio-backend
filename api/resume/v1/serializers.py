from itertools import groupby

from django.contrib.auth.models import User
from rest_framework import serializers

from resume.models import SoftSkill, Education, Contact, Experience, TechSkill, Profile, ExperienceDescription, \
    Interest, Achievement, Project, CoursesAndCertification


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance):
        return instance.value


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('contact_type', 'contact_info')


class SoftSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftSkill
        fields = '__all__'

    def to_representation(self, instance):
        return instance.name


class TechSkillSerializer(serializers.ModelSerializer):
    category = serializers.CharField(read_only=True, source='category.category')

    class Meta:
        model = TechSkill
        fields = ("name", "level", "category")


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ('created_at', 'updated_at', 'id', 'user')


class ExperienceTechSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechSkill
        fields = '__all__'

    def to_representation(self, instance):
        return instance.name


class ExperienceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceDescription
        fields = '__all__'

    def to_representation(self, instance):
        return instance.bullet


class ExperienceSerializer(serializers.ModelSerializer):
    skills = ExperienceTechSkillSerializer(many=True)
    bullets = ExperienceDescriptionSerializer(many=True, source="experiencedescription_set")

    class Meta:
        model = Experience
        exclude = ('created_at', 'updated_at', 'id', 'user')

    # def to_representation(self, instance):
    #     return instance.skills.name


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

    def to_representation(self, instance):
        return instance.interest


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CoursesAndCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesAndCertification
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(many=True, source="profile_set")
    contacts = ContactSerializer(many=True, source="contact_set")
    soft_skills = SoftSkillSerializer(many=True, source="softskill_set")
    educations = EducationSerializer(many=True, source="education_set")
    experiences = ExperienceSerializer(many=True, source="experience_set")
    tech_skills = TechSkillSerializer(many=True, source="techskill_set")
    interests = InterestSerializer(many=True, source="interest_set")
    achievements = AchievementSerializer(many=True, source="achievement_set")
    certifications = CoursesAndCertificationSerializer(many=True, source="coursesandcertification_set")
    projects = ProjectSerializer(many=True, source="project_set")

    class Meta:
        model = User
        fields = (
            "profiles", "contacts", "soft_skills", "educations", "experiences", "tech_skills", "interests",
            "achievements",
            "certifications", "projects")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        tech_skills, soft_skills = data.pop('tech_skills'), data.pop('soft_skills')
        data["skills"] = {
            "soft_skills": soft_skills,
            "tech_skills": {key: [{"name": item["name"], "level": item["level"]}
                                  for item in grp]
                            for key, grp in groupby(tech_skills, key=lambda skill: skill['category'])}
        }
        return data
