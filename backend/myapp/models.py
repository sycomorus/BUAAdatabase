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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_id_student')
    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=255,blank=True,null=True)
    # 主属性
    telephone = models.CharField(max_length=255,null=True,blank=True)
    # 主属性
    email = models.EmailField(max_length=255,blank=True,null=True)
    grade = models.CharField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    intro= models.TextField(blank=True,null=True)
    personalSignature = models.CharField(max_length=255,blank=True,null=True)
    

    def __str__(self):
        return self.user_id.username

# 家教表 BCNF
class Tutor(models.Model):
    # 主码、主属性
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_id_tutor')
    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=255,blank=True,null=True)
    # 主属性
    telephone = models.CharField(max_length=255,blank=True,null=True)
    # 主属性
    email = models.EmailField(max_length=255,blank=True,null=True)
    rate = models.FloatField(blank=True,null=True)
    rateNum = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    intro= models.TextField(blank=True,null=True)
    personalSignature = models.CharField(max_length=255,blank=True,null=True)
    degree = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.user_id.username

# Post表 BCNF
class Post(models.Model):
    # 主码、主属性
    post_id = models.BigAutoField(primary_key=True)
    # 外码
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_id_post')
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

# Post表的科目表 BCNF
class PostSubject(models.Model):
    # 主码、主属性
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_id_subject')
    subject = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.subject

# 通知表 BCNF   
class Notification(models.Model):
    # 主码、主属性
    notification_id = models.BigAutoField(primary_key=True)
    # 外码
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_id_notice')
    notificationDate = models.DateTimeField(blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    is_read = models.BooleanField()

    def __str__(self):
        return self.notification_id

# 学习资料表 BCNF
class StudyMaterial(models.Model):
    # 主码、主属性
    material_id = models.BigAutoField(primary_key=True)
    # 外码
    tutor_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tutor_id_material')
    # 外码
    student_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='student_id_material')
    file_name = models.CharField(max_length=255)
    download_link = models.CharField(max_length=255)
    upload_date = models.DateField()

    def __str__(self):
        return f"Material {self.material_id}"

# 评价表 BCNF
class Review(models.Model):
    # 主码、主属性
    review_id = models.BigAutoField(primary_key=True)
    # 外码
    student_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='student_id_review')
    # 外码
    tutor_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tutor_id_review')
    rating = models.FloatField(blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    date= models.DateField(blank=True,null=True)

    def __str__(self):
        return f"Review {self.review_id}"

# 师生关系表 BCNF
class Link(models.Model):
    # 主码、主属性
    link_id = models.BigAutoField(primary_key=True)
    # 外码
    student_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='student_id_link')
    # 外码
    tutor_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tutor_id_link')

    def __str__(self):
        return f"Link {self.link_id}"

# 待办事项表 BCNF
class Todo(models.Model):
    # 主码、主属性
    todo_id = models.BigAutoField(primary_key=True)
    # 外码
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='owner_id_todo')
    accepter_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender_id_todo')
    accept_post_id = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='source_post_id_todo')
    is_completed = models.BooleanField()

    def __str__(self):
        return f"Todo {self.todo_id}"
