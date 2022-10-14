from django.contrib import admin
from resume.models import (Profile,
                           Experience,
                           ExperienceDescription,
                           TechSkillCategory,
                           TechSkill,
                           SoftSkill,
                           Education,
                           Interest,
                           Contact, Project, CoursesAndCertification, Achievement)


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)


class ExperienceDescriptionAdmin(admin.StackedInline):
    model = ExperienceDescription
    extra = 3


class ExperienceAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields': []}),
    #     ('Description', {'fields': })
    # ]
    inlines = [ExperienceDescriptionAdmin]


admin.site.register(Experience, ExperienceAdmin)


class TechSkillCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(TechSkillCategory, TechSkillCategoryAdmin)


class TechSkillAdmin(admin.ModelAdmin):
    pass


admin.site.register(TechSkill, TechSkillAdmin)


class SoftSkillAdmin(admin.ModelAdmin):
    pass


admin.site.register(SoftSkill, SoftSkillAdmin)


class EducationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Education, EducationAdmin)


class InterestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Interest, InterestAdmin)


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)


class AchievementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Achievement, AchievementAdmin)


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)


class CoursesAndCertificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(CoursesAndCertification, CoursesAndCertificationAdmin)

