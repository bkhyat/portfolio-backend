from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class User(AbstractUser):
#     address = models.CharField(max_length=200, null=True, blank=True)
#

class CustomBaseModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(CustomBaseModel):
    class Meta:
        ordering = ['order']

    value = models.TextField()
    order = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.value


class Experience(CustomBaseModel):
    designation = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    job_type = models.CharField(choices=[('Full Time', 'Full Time'),
                                         ('Part Time', 'Part Time'),
                                         ('Contract', 'Contract'),
                                         ('Freelancing', 'Freelancing'),
                                         ('Other', 'Other')],
                                max_length=11
                                )
    job_model = models.CharField(choices=[('On Site', 'On Site'),
                                          ('Remote', 'Remote'),
                                          ('Hybrid (Onsite + Remote)', 'Hybrid (Onsite + Remote)')],
                                 max_length=24
                                 )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    skills = models.ManyToManyField('TechSkill')

    class Meta:
        ordering = ("-start_date",)

    def __str__(self):
        return f'{self.designation} at {self.organization}'


class ExperienceDescription(CustomBaseModel):
    bullet = models.CharField(max_length=200)
    order = models.SmallIntegerField()
    experience = models.ForeignKey('Experience', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.order} - {self.bullet}'


class TechSkillCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class TechSkill(CustomBaseModel):
    name = models.CharField(max_length=50)
    level = models.SmallIntegerField(choices=[(1, 1),
                                              (2, 2),
                                              (3, 3),
                                              (4, 4),
                                              (5, 5)]
                                     )
    category = models.ForeignKey('TechSkillCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SoftSkill(CustomBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Education(CustomBaseModel):
    university = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    level = models.CharField(choices=[('High School', 'High School'),
                                      ('Bachelor', 'Bachelor'),
                                      ('Masters', 'Masters'),
                                      ('Phd', 'Phd')],
                             max_length=11
                             )
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    score = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.level}, {self.course} at {self.university}'


class Interest(CustomBaseModel):
    interest = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.interest


class Contact(CustomBaseModel):
    contact_type = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.contact_type}: {self.contact_info}'


class Achievement(CustomBaseModel):
    description = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True, max_length=200)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.id} - {self.description}'


class Project(CustomBaseModel):
    project_name = models.CharField(max_length=200)
    project_description = models.CharField(max_length=500)
    tech_stacks = models.ManyToManyField(TechSkill)
    completed_at = models.DateField(null=True)
    url = models.URLField(null=True, blank=True, max_length=200)
    has_demo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-completed_at']

    def __str__(self):
        return f'{self.id} - {self.project_name} - {self.completed_at}'


class CoursesAndCertification(CustomBaseModel):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500)
    certification_url = models.URLField(max_length=200, null=True, blank=True)
    completed_at = models.DateField(null=True)

    class Meta:
        ordering = ['-completed_at']

    def __str__(self):
        return f'{self.id} - {self.title}'

