from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db import models
import json
import random
import pytz
from datetime import datetime, timedelta
from .models import User, Student,Tutor,StudentPost,TutorPost,StudentPostSubject,TutorPostSubject

@csrf_exempt
def home(request):
    return HttpResponse("Welcome to the Home Page")

@csrf_exempt
def login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body.get('name')  # 使用 username 而不是 name
        password = body.get('password')
        result = {'data': {}}
        try:
            # 查询数据库中是否存在对应的用户
            user = User.objects.get(username=username, password=password)
            if user.identity == 0:
                result['data']['roles'] = [{'id': 'admin'}]
            elif user.identity == 1:
                result['data']['roles'] = [{'id': 'teacher'}]
            elif user.identity == 2:
                result['data']['roles'] = [{'id': 'student'}]
            else:
                raise Exception("未知身份")
            result['data']['id'] = str(user.user_id)

            # 登录成功
            result['code'] = 0
            result['data']['token'] = "Authorization:" + str(random.random())
            result['message'] = "登录成功"
        except User.DoesNotExist:
            # 用户不存在或密码错误
            result['code'] = -1
            result['message'] = "账户名或密码错误"
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

    
@csrf_exempt
def register(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body.get('name')
        password = body.get('password')
        role = body.get('role')
        try:
            # 检查用户是否已经存在
            user = User.objects.get(username=username)
            result={'data':{}}
            result['code'] = -1
            return JsonResponse(result)
        except User.DoesNotExist:
            # 创建用户
            user = User(username=username, 
                        password=password, 
                        identity=-1,
                        registration_date=datetime.now(pytz.timezone('Asia/Shanghai')))
            user.save()
            result={'data':{}}
            if role == "admin":
                user.identity = 0
                user.save()
                result['data']['roles']=[{'id': 'admin'}]
            elif role == "teacher":
                user.identity = 1
                user.save()
                tutor=Tutor(user_id=user)
                tutor.save()
                result['data']['roles']=[{'id': 'teacher'}]
            elif role == "student":
                user.identity = 2
                user.save()
                student=Student(user_id=user)
                student.save()
                result['data']['roles']=[{'id': 'student'}]
            else:
                raise Exception("未知身份")
            result['code'] = 0
            result['data']['token']="Authorization:" + str(random.random())
            result['data']['id'] = str(user.user_id)
            return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

@csrf_exempt
def sendPost(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        request_id=int(body.get('id'))
        title = body.get('data').get('title')
        startDate = body.get('data').get('startDate')
        endDate = body.get('data').get('endDate')
        subjects=body.get('data').get('subjects')
        location=body.get('data').get('location')
        fullLocation=body.get('data').get('fullLocation')
        telephoneNumber=body.get('data').get('telephoneNumber')
        email=body.get('data').get('emailAddress')
        content=body.get('data').get('content')
        is_complete = all([title, startDate, endDate, subjects, location, fullLocation, telephoneNumber, email, content])
        if not is_complete:
            return JsonResponse({'code': 0})
        
        try :
            user=User.objects.get(user_id=request_id)
        except User.DoesNotExist:
            return JsonResponse({'code': -1, 'message': '用户不存在'})
        
        if user.identity ==0:
            raise Exception("管理员无法发帖")
        elif user.identity ==1:
            tutorPost=TutorPost(
                tutor_id=Tutor.objects.get(user_id=user),
                title=title,
                postDate=datetime.now(pytz.timezone('Asia/Shanghai')),
                startDate=startDate,
                endDate=endDate,
                location=location,
                fullLocation=fullLocation,
                telephoneNumber=telephoneNumber,
                emailAddress=email,
                content=content,
                is_completed=True,
            )
            tutorPost.save()
            for subject in subjects:
                tutorPostSubject=TutorPostSubject(
                    tutorPost_id=tutorPost,
                    subject=subject,
                )
                tutorPostSubject.save()
            result={'data':{}}
            result['code'] = 0
            return JsonResponse(result)
        elif user.identity ==2:
            studentPost = StudentPost(
                student_id=Student.objects.get(user_id=user),
                title=title,
                postDate=datetime.now(pytz.timezone('Asia/Shanghai')),
                startDate=startDate,
                endDate=endDate,
                location=location,
                fullLocation=fullLocation,
                telephoneNumber=telephoneNumber,
                emailAddress=email,
                content=content,
                is_completed=True,
            )
            studentPost.save()
            for subject in subjects:
                studentPostSubject=StudentPostSubject(
                    studentPost_id=studentPost,
                    subject=subject,
                )
                studentPostSubject.save()
            result={'data':{}}
            result['code'] = 0
            return JsonResponse(result)
        else:
            raise Exception("未知身份")
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

@csrf_exempt
def savePost(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        request_id=int(body.get('id'))
        title = body.get('data').get('title')
        startDate = body.get('data').get('startDate') or None
        endDate = body.get('data').get('endDate') or None
        subjects=body.get('data').get('subjects')
        location=body.get('data').get('location')
        fullLocation=body.get('data').get('fullLocation')
        telephoneNumber=body.get('data').get('telephoneNumber')
        email=body.get('data').get('emailAddress') or None
        content=body.get('data').get('content')

        try:
            user=User.objects.get(user_id=request_id)
        except User.DoesNotExist:
            return JsonResponse({'code': -1, 'message': '用户不存在'})
        
        if user.identity ==0:
            raise Exception("管理员无法保存帖子")
        elif user.identity ==1:
            try:
                tutor=Tutor.objects.get(user_id=user)
                post=TutorPost.objects.get(tutor_id=tutor,is_completed=False)
                post.title=title
                post.startDate=startDate
                post.endDate=endDate
                post.location=location
                post.fullLocation=fullLocation
                post.telephoneNumber=telephoneNumber
                post.emailAddress=email
                post.content=content
                post.save()
                TutorPostSubject.objects.filter(tutorPost_id=post).delete()
                for subject in subjects:
                    tutorPostSubject=TutorPostSubject(
                        tutorPost_id=post,
                        subject=subject,
                    )
                    tutorPostSubject.save()
                result={'data':{}}
                result['code'] = 0
                return JsonResponse(result)
            except TutorPost.DoesNotExist:
                post=TutorPost(
                    tutor_id=tutor,
                    title=title,
                    startDate=startDate,
                    endDate=endDate,
                    location=location,
                    fullLocation=fullLocation,
                    telephoneNumber=telephoneNumber,
                    emailAddress=email,
                    content=content,
                    is_completed=False,
                )
                post.save()
                for subject in subjects:
                    tutorPostSubject=TutorPostSubject(
                        tutorPost_id=post,
                        subject=subject,
                    )
                    tutorPostSubject.save()
                result={'data':{}}
                result['code'] = 0
                return JsonResponse(result)
        elif user.identity ==2:
            try:
                student=Student.objects.get(user_id=user)
                post=StudentPost.objects.get(student_id=student,is_completed=False)
                post.title=title
                post.startDate=startDate
                post.endDate=endDate
                post.location=location
                post.fullLocation=fullLocation
                post.telephoneNumber=telephoneNumber
                post.emailAddress=email
                post.content=content
                post.save()
                StudentPostSubject.objects.filter(studentPost_id=post).delete()
                for subject in subjects:
                    studentPostSubject=StudentPostSubject(
                        studentPost_id=post,
                        subject=subject,
                    )
                    studentPostSubject.save()
                result={'data':{}}
                result['code'] = 0
                return JsonResponse(result)
            except StudentPost.DoesNotExist:
                post=StudentPost(
                    student_id=student,
                    title=title,
                    startDate=startDate,
                    endDate=endDate,
                    subjects=subjects,
                    location=location,
                    fullLocation=fullLocation,
                    telephoneNumber=telephoneNumber,
                    emailAddress=email,
                    content=content,
                    tags=subjects,
                    is_completed=False,
                )
                post.save()
                for subject in subjects:
                    studentPostSubject=StudentPostSubject(
                        studentPost_id=post,
                        subject=subject,
                    )
                    studentPostSubject.save()
                result={'data':{}}
                result['code'] = 0
                return JsonResponse(result)
        else:
            raise Exception("未知身份")
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

@csrf_exempt
def getSavedPost(request):
    if request.method == 'GET':
        try:
            user_id=request.GET.get('id')
            user=User.objects.get(user_id=int(user_id))
            tutor=None
            student=None
            try:
                tutor=Tutor.objects.get(user_id=user)
                identity=1
            except Tutor.DoesNotExist:
                student=Student.objects.get(user_id=user)
                identity=2
            
            if identity==2:
                try:
                    post=StudentPost.objects.get(student_id=student,is_completed=False)
                    result={'data':{}}
                    result['code'] = 0
                    result['data']['title']=post.title
                    result['data']['startDate']=post.startDate
                    result['data']['endDate']=post.endDate
                    result['data']['location']=post.location
                    result['data']['fullLocation']=post.fullLocation
                    result['data']['telephoneNumber']=post.telephoneNumber
                    result['data']['emailAddress']=post.emailAddress
                    result['data']['content']=post.content
                    subjects=StudentPostSubject.objects.filter(studentPost_id=post)
                    result['data']['subjects']=[subject.subject for subject in subjects]
                except:
                    result={'data':{}}
                    result['code'] = 0
                return JsonResponse(result)
            elif identity==1:
                try:
                    post=TutorPost.objects.get(tutor_id=tutor,is_completed=False)
                    result={'data':{}}
                    result['code'] = 0
                    result['data']['title']=post.title
                    result['data']['startDate']=post.startDate
                    result['data']['endDate']=post.endDate
                    result['data']['location']=post.location
                    result['data']['fullLocation']=post.fullLocation
                    result['data']['telephoneNumber']=post.telephoneNumber
                    result['data']['emailAddress']=post.emailAddress
                    result['data']['content']=post.content
                    subjects=TutorPostSubject.objects.filter(tutorPost_id=post)
                    result['data']['subjects']=[subject.subject for subject in subjects]
                except:
                    result={'data':{}}
                    result['code'] = 0
                return JsonResponse(result)
            else:
                raise Exception("未知身份")
        except User.DoesNotExist:
            result={'data':{}}
            result['code'] = 0
            return JsonResponse(result)     
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})


@csrf_exempt
def getPosts(request):
    if request.method == 'GET':
        request_id=int(request.GET.get('id'))
        request_page=int(request.GET.get('page'))
        request_query=request.GET.get('query')
        start=(request_page-1)*10
        end=request_page*10
        returnSubjects=[]
        try:
            user=User.objects.get(user_id=request_id)
            if user.identity==0:
                raise Exception("管理员现在还不知道干啥")
            elif user.identity==2:
                if request_query=="":
                    posts=TutorPost.objects.filter(is_completed=True)
                else:
                    subjectsLine=TutorPostSubject.objects.filter(subject=request_query)
                    subjectsFits=[subject.tutorPost_id for subject in subjectsLine]
                    userLine=User.objects.filter(username=request_query,identity=1)
                    tutorLine=Tutor.objects.filter(user_id__in=userLine)
                    tutorFits=TutorPost.objects.filter(tutor_id__in=tutorLine)
                    OtherFits=TutorPost.objects.filter(
                        models.Q(title=request_query)|
                        models.Q(content=request_query)
                    )
                    all_posts=list(set(subjectsFits+list(tutorFits)+list(OtherFits)))
                    posts=[]
                    for post in all_posts:
                        if post.is_completed:
                            posts.append(post)
                returnSubjectLines=list(TutorPostSubject.objects.filter(tutorPost_id__in=posts))
                for subject in returnSubjectLines:
                    returnSubjects.append(subject.subject)
                
                return_posts=[]
                for post in posts:
                    user=post.tutor_id.user_id
                    now = datetime.now(pytz.timezone('Asia/Shanghai'))
                    post_date = post.postDate.astimezone(pytz.timezone('Asia/Shanghai'))
                    time_diff = now - post_date
                    if time_diff < timedelta(hours=24):
                        date_display = f"{time_diff.seconds // 3600}小时前"
                    elif time_diff < timedelta(days=3):
                        date_display = f"{time_diff.days}天前"
                    else:
                        date_display = post_date.strftime("%Y-%m-%d")
                    return_posts.append({
                        'id':str(post.post_id),
                        'title':post.title,
                        'tags':returnSubjects,
                        'content':post.content,
                        'author':user.username,
                        'authorId':user.user_id,
                        'date':date_display,
                        'location':post.location,
                    })
                result={'posts':return_posts[start:end],'total':len(posts)}
                return JsonResponse(result)
            elif user.identity==1:
                if request_query=="":
                    posts=StudentPost.objects.filter(is_completed=True)
                else:
                    subjectsLine=StudentPostSubject.objects.filter(subject=request_query)
                    subjectsFits=[subject.studentPost_id for subject in subjectsLine]
                    userLine=User.objects.filter(username=request_query,identity=2)
                    studentLine=Student.objects.filter(user_id__in=userLine)
                    studentFits=[StudentPost.objects.get(student_id=student) for student in studentLine]
                    OtherFits=StudentPost.objects.filter(
                        models.Q(title=request_query)|
                        models.Q(content=request_query)
                    )
                    all_posts=list(set(subjectsFits+studentFits+list(OtherFits)))
                    posts=[]
                    for post in all_posts:
                        if post.is_completed:
                            posts.append(post)
                returnSubjectLines=list(StudentPostSubject.objects.filter(studentPost_id__in=posts))
                for subject in returnSubjectLines:
                    returnSubjects.append(subject.subject)

                return_posts=[]
                for post in posts:
                    user=post.student_id.user_id
                    now = datetime.now(pytz.timezone('Asia/Shanghai'))
                    post_date = post.postDate.astimezone(pytz.timezone('Asia/Shanghai'))
                    time_diff = now - post_date
                    if time_diff < timedelta(hours=24):
                        date_display = f"{time_diff.seconds // 3600}小时前"
                    elif time_diff < timedelta(days=3):
                        date_display = f"{time_diff.days}天前"
                    else:
                        date_display = post_date.strftime("%Y-%m-%d")
                    return_posts.append({
                        'id':str(post.post_id),
                        'title':post.title,
                        'tags':returnSubjects,
                        'content':post.content,
                        'author':user.username,
                        'authorId':user.user_id,
                        'date':date_display,
                        'location':post.location,
                    })
                result={'posts':return_posts[start:end],'total':len(posts)}
                return JsonResponse(result)
            else:
                raise Exception("未知身份")
        except User.DoesNotExist:
            raise Exception("用户不存在")
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})



@csrf_exempt
def get_routes_config(request):
    if request.method == 'GET':
        routes_config = [
            # 示例路由配置
            {'path': '/dashboard', 'name': 'Dashboard', 'component': 'Dashboard'},
            {'path': '/profile', 'name': 'Profile', 'component': 'Profile'}
        ]
        return JsonResponse({'code': 0, 'data': routes_config})
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})