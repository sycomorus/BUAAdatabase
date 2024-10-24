from django.db import models

# 用户表
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    identity = models.IntegerField()  # 0: 管理员,1: 家教, 2: 学生
    registration_date = models.DateField()

    def __str__(self):
        return self.username

# 学生表
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True,null=True)
    gender = models.IntegerField(blank=True,null=True)  # 0: 男, 1: 女
    contact = models.CharField(max_length=255,null=True,blank=True)
    grade = models.IntegerField(blank=True,null=True)
    

    def __str__(self):
        return self.name

# 家教表
class Tutor(models.Model):
    id = models.BigAutoField(primary_key=True)
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True,null=True)
    gender = models.IntegerField(blank=True,null=True)  # 0: 男, 1: 女
    contact = models.CharField(max_length=255,blank=True,null=True) 
    grade = models.IntegerField(blank=True,null=True)
    rating = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

# 招聘帖表
class RecruitmentPost(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    tags=models.JSONField(default=list,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    postDate = models.DateTimeField(blank=True,null=True)
    startDate = models.DateField(blank=True,null=True)
    endDate = models.DateField(blank=True,null=True)
    subjects = models.JSONField(default=list,blank=True,null=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    fullLocation = models.CharField(max_length=255,blank=True,null=True)
    telephoneNumber = models.CharField(max_length=255,blank=True,null=True)
    emailAddress = models.EmailField(max_length=255,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    is_completed = models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return self.title

# 求职帖表
class JobPost(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    tags=models.JSONField(default=list,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    postDate = models.DateTimeField(blank=True,null=True)
    startDate = models.DateField(blank=True,null=True)
    endDate = models.DateField(blank=True,null=True)
    subjects = models.JSONField(default=list,blank=True,null=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    fullLocation = models.CharField(max_length=255,blank=True,null=True)
    telephoneNumber = models.CharField(max_length=255,blank=True,null=True)
    emailAddress = models.EmailField(max_length=255,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    is_completed = models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return self.title

# 学习资料表
class StudyMaterial(models.Model):
    id = models.BigAutoField(primary_key=True)
    uploader_id = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='uploaded_materials')
    receiver_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='received_materials')
    upload_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return f"Material {self.id}"

# 评价表
class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    reviewer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_reviews')
    reviewed_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reviews')
    rating = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"Review {self.id}"

# 通知表
class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    recipient_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # related_post_id = models.ForeignKey(JobPost, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notification {self.id}"

