from django.db import models

# 用户表 BCNF
class User(models.Model):
    # 主码、主属性
    user_id = models.BigAutoField(primary_key=True)
    # 主属性
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    identity = models.IntegerField()  # 0: 管理员,1: 家教, 2: 学生
    registration_date = models.DateField()

    def __str__(self):
        return self.username

# 学生表 BCNF
class Student(models.Model):
    # 主码、主属性
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True,null=True)
    gender = models.IntegerField(blank=True,null=True)  # 0: 男, 1: 女
    # 主属性
    contact = models.CharField(max_length=255,null=True,blank=True)
    # 主属性
    email = models.EmailField(max_length=255,blank=True,null=True)
    grade = models.IntegerField(blank=True,null=True)
    

    def __str__(self):
        return self.user_id.username

# 家教表 BCNF
class Tutor(models.Model):
    # 主码、主属性
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True,null=True)
    gender = models.IntegerField(blank=True,null=True)  # 0: 男, 1: 女
    # 主属性
    contact = models.CharField(max_length=255,blank=True,null=True)
    # 主属性
    email = models.EmailField(max_length=255,blank=True,null=True)
    rating = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.user_id.username

# 学生Post表 BCNF
class StudentPost(models.Model):
    # 主码、主属性
    post_id = models.BigAutoField(primary_key=True)
    # 外码
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True,null=True)
    postDate = models.DateTimeField(blank=True,null=True)
    startDate = models.DateField(blank=True,null=True)
    endDate = models.DateField(blank=True,null=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    fullLocation = models.CharField(max_length=255,blank=True,null=True)
    telephoneNumber = models.CharField(max_length=255,blank=True,null=True)
    emailAddress = models.EmailField(max_length=255,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    is_completed = models.BooleanField()

    def __str__(self):
        return self.title

# 学生Post表的科目表 BCNF
class StudentPostSubject(models.Model):
    # 主码、主属性
    studentPost_id = models.ForeignKey(StudentPost, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.subject
    
# 家教Post表 BCNF
class TutorPost(models.Model):
    # 主码、主属性
    post_id = models.BigAutoField(primary_key=True)
    # 外码
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True,null=True)
    postDate = models.DateTimeField(blank=True,null=True)
    startDate = models.DateField(blank=True,null=True)
    endDate = models.DateField(blank=True,null=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    fullLocation = models.CharField(max_length=255,blank=True,null=True)
    telephoneNumber = models.CharField(max_length=255,blank=True,null=True)
    emailAddress = models.EmailField(max_length=255,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    is_completed = models.BooleanField()

    def __str__(self):
        return self.title
    
# 家教Post表的科目表 BCNF
class TutorPostSubject(models.Model):
    # 主码、主属性
    tutorPost_id = models.ForeignKey(TutorPost, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.subject

# 学生通知表 BCNF 
class StudentNotification(models.Model):
    # 主码、主属性
    studentNotification_id = models.BigAutoField(primary_key=True)
    # 外码
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    # 外码
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    notificationDate = models.DateTimeField(blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    is_read = models.BooleanField()

    def __str__(self):
        return self.content

# 家教通知表 BCNF   
class TutorNotification(models.Model):
    # 主码、主属性
    tutorNotification_id = models.BigAutoField(primary_key=True)
    # 外码
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    # 外码
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    notificationDate = models.DateTimeField(blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    is_read = models.BooleanField()

    def __str__(self):
        return

# 学习资料表 BCNF
class StudyMaterial(models.Model):
    # 主码、主属性
    material_id = models.BigAutoField(primary_key=True)
    # 外码
    uploader_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    # 外码
    receiver_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    upload_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return f"Material {self.material_id}"

# 评价表 BCNF
class Review(models.Model):
    # 主码、主属性
    review_id = models.BigAutoField(primary_key=True)
    # 外码
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    # 外码
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"Review {self.review_id}"

