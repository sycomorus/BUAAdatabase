from django.contrib import admin
from .models import User, Student, Tutor, RecruitmentPost, StudyMaterial, Review, JobPost, Notification

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(RecruitmentPost)
admin.site.register(StudyMaterial)
admin.site.register(Review)
admin.site.register(JobPost)
admin.site.register(Notification)
