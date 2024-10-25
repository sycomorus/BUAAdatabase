from django.contrib import admin
from .models import User, Student, Tutor, StudentPost, TutorPost, StudentNotification, TutorNotification, StudentPostSubject, TutorPostSubject, Review,StudyMaterial

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(StudentPost)
admin.site.register(TutorPost)
admin.site.register(StudentNotification)
admin.site.register(TutorNotification)
admin.site.register(StudentPostSubject)
admin.site.register(TutorPostSubject)
admin.site.register(Review)
admin.site.register(StudyMaterial)
