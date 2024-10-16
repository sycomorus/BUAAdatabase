# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import Student, Tutor, User
# from django.utils import timezone

# # 创建Student时自动创建User
# @receiver(pre_save, sender=Student)
# def create_user_for_student(sender, instance, **kwargs):
#     if instance.user_id is None:  # 只在没有关联的User时创建
#         user = User.objects.create(
#             username=instance.name,  # 使用name作为username，或根据需要更改
#             password='default_password',  # 设置默认密码，可以后续修改
#             email=f"{instance.name.lower()}@example.com",  # 设置默认邮箱
#             identity=0,  # 0表示学生
#             registration_date=timezone.now()
#         )
#         instance.user = user  # 关联到Student

# # 创建Tutor时自动创建User
# @receiver(pre_save, sender=Tutor)
# def create_user_for_tutor(sender, instance, **kwargs):
#     if instance.user_id is None:  # 只在没有关联的User时创建
#         user = User.objects.create(
#             username=instance.name,  # 使用name作为username，或根据需要更改
#             password='default_password',  # 设置默认密码，可以后续修改
#             email=f"{instance.name.lower()}@example.com",  # 设置默认邮箱
#             identity=1,  # 1表示家教
#             registration_date=timezone.now()
#         )
#         instance.user = user  # 关联到Tutor
