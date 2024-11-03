from django.contrib import admin
from .models import User, Student, Tutor, Post, Notification, PostSubject, Review,StudyMaterial,Link,Todo

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Post)
admin.site.register(Notification)
admin.site.register(PostSubject)
admin.site.register(Review)
admin.site.register(StudyMaterial)
admin.site.register(Link)
admin.site.register(Todo)
