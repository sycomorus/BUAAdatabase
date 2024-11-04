from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db import models
import json
import random
import pytz
from datetime import datetime, timedelta
from .models import User, Student,Tutor,Post,PostSubject,Link,Notification,Review,StudyMaterial,Todo

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

            request.session['user_id'] = user.user_id 

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

            request.session['user_id'] = user.user_id
            sendNotice(user,"注册成功","欢迎加入家教综合服务平台！")

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
        else:
            post=Post(
                user_id=user,
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
            post.save()
            for subject in subjects:
                postSubject=PostSubject(
                    post_id=post,
                    subject=subject,
                )
                postSubject.save()
            result={'data':{}}
            result['code'] = 0
            return JsonResponse(result)
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
        else:
            try:
                post=Post.objects.get(user_id=user,is_completed=False)
                post.title=title
                post.startDate=startDate
                post.endDate=endDate
                post.location=location
                post.fullLocation=fullLocation
                post.telephoneNumber=telephoneNumber
                post.emailAddress=email
                post.content=content
                post.save()
                PostSubject.objects.filter(post_id=post).delete()
                for subject in subjects:
                    postSubject=PostSubject(
                        post_id=post,
                        subject=subject,
                    )
                    postSubject.save()
                result={'data':{}}
                result['code'] = 0
                return JsonResponse(result)
            except Post.DoesNotExist:
                post=Post(
                    user_id=user,
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
                    postSubject=PostSubject(
                        post_id=post,
                        subject=subject,
                    )
                    postSubject.save()
                result={'data':{}}
                result['code'] = 0
                return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

@csrf_exempt
def getSavedPost(request):
    if request.method == 'GET':
        try:
            user_id=request.GET.get('id')
            user=User.objects.get(user_id=int(user_id))
            if user.identity==0:
                raise Exception("管理员无法获取帖子")
            else:
                try:
                    post=Post.objects.get(user_id=user,is_completed=False)
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
                    subjects=PostSubject.objects.filter(post_id=post)
                    result['data']['subjects']=[subject.subject for subject in subjects]
                except:
                    result={'data':{}}
                    result['code'] = 0
                return JsonResponse(result)
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
        user=User.objects.get(user_id=request_id)
        try:
            if user.identity==0:
                raise Exception("管理员现在还不知道干啥")
            else:
                if user.identity==1:
                    filter_id=2
                else:
                    filter_id=1
                
                if request_query=="":
                    posts=Post.objects.filter(is_completed=True,user_id__identity=filter_id)
                else:
                    subjectsLine=PostSubject.objects.filter(subject=request_query)
                    subjectsFits=set([subject.post_id for subject in subjectsLine])
                    userLine=User.objects.filter(username=request_query)
                    userFits=Post.objects.filter(user_id__in=userLine)
                    OtherFits=Post.objects.filter(
                        models.Q(title=request_query)|
                        models.Q(content=request_query)
                    )
                    all_posts=list(set(list(subjectsFits)+list(userFits)+list(OtherFits)))
                    posts=[]
                    for post in all_posts:
                        if post.is_completed and post.user_id.identity==filter_id:
                            posts.append(post)
                
                return_posts=[]
                for post in posts:
                    user=post.user_id
                    now = datetime.now(pytz.timezone('Asia/Shanghai'))
                    post_date = post.postDate.astimezone(pytz.timezone('Asia/Shanghai'))
                    time_diff = now - post_date
                    if time_diff < timedelta(hours=24):
                        date_display = f"{time_diff.seconds // 3600}小时前"
                    elif time_diff < timedelta(days=3):
                        date_display = f"{time_diff.days}天前"
                    else:
                        date_display = post_date.strftime("%Y-%m-%d")
                    return_subject_lines=PostSubject.objects.filter(post_id=post)
                    returnSubjects=[]
                    for subject in return_subject_lines:
                        returnSubjects.append(subject.subject)
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
        except User.DoesNotExist:
            raise Exception("用户不存在")
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})
    

@csrf_exempt
def getPost(request):
    if request.method == 'GET':
        post_id=int(request.GET.get('id'))
        try:
            post=Post.objects.get(post_id=post_id)
            result={'data':{}}
            result['code'] = 0
            result['data']['title']=post.title
            result['data']['author']=post.user_id.username
            result['data']['location']=post.location
            result['data']['fullLocation']=post.fullLocation
            result['data']['telephoneNumber']=post.telephoneNumber
            result['data']['emailAddress']=post.emailAddress
            subject_lines=PostSubject.objects.filter(post_id=post)
            subjects=[]
            for subject in subject_lines:
                subjects.append(subject.subject)
            result['data']['subjects']=subjects
            result['data']['content']=post.content
            return JsonResponse(result)
            
        except Post.DoesNotExist:
            return JsonResponse({'code': -1, 'message': '帖子不存在'})

@csrf_exempt
def agreePostRequest(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_id=int(body.get('id'))
        post_id=int(body.get('postId'))
        accepter=User.objects.get(user_id=user_id)
        post=Post.objects.get(post_id=post_id)
        title=post.title
        post_owner=post.user_id
        sendNotice(post_owner,"帖子被接收",f"您题为《{title}》的帖子已被接收，请在待办事项中查看")
        sendTodo(post_owner,post,accepter)
        result={'data':{}}
        result['code'] = 0
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})
    
@csrf_exempt
def updateStudentInfo(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        request_id=int(body.get('id'))
        grade = body.get('data').get('grade')
        gender = body.get('data').get('gender')
        age=body.get('data').get('age')
        email=body.get('data').get('email')
        telephone=body.get('data').get('telephone')
        address=body.get('data').get('address')
        intro=body.get('data').get('intro')
        personalSignature=body.get('data').get('personalSignature')

        user=User.objects.get(user_id=request_id)
        student=Student.objects.get(user_id=user)
        student.grade=grade
        student.gender=gender
        student.age=age
        student.email=email
        student.telephone=telephone
        student.address=address
        student.intro=intro
        student.personalSignature=personalSignature
        student.save()

        result={'data':{}}
        result['code'] = 0
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

@csrf_exempt
def getStudentInfo(request):
    if request.method == 'GET':
        request_id=int(request.GET.get('id'))
        result={'data':{}}
        result['code'] = 0
        user=User.objects.get(user_id=request_id)
        student=Student.objects.get(user_id=user)
        result['data']['name']=user.username
        result['data']['email']=student.email
        result['data']['telephone']=student.telephone
        result['data']['address']=student.address
        result['data']['personalSignature']=student.personalSignature
        result['data']['intro']=student.intro
        result['data']['age']=student.age
        result['data']['gender']=student.gender
        result['data']['grade']=student.grade
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})
    
@csrf_exempt
def updateTeacherInfo(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        request_id=int(body.get('id'))
        degree=body.get('data').get('degree')
        gender=body.get('data').get('gender')
        age=body.get('data').get('age')
        email=body.get('data').get('email')
        telephone=body.get('data').get('telephone')
        address=body.get('data').get('address')
        intro=body.get('data').get('intro')
        personalSignature=body.get('data').get('personalSignature')

        user=User.objects.get(user_id=request_id)
        tutor=Tutor.objects.get(user_id=user)
        tutor.degree=degree
        tutor.gender=gender
        tutor.age=age
        tutor.email=email
        tutor.telephone=telephone
        tutor.address=address
        tutor.intro=intro
        tutor.personalSignature=personalSignature
        tutor.save()

        result={'data':{}}
        result['code'] = 0
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})
    
@csrf_exempt
def getTeacherInfo(request):
    if request.method == 'GET':
        request_id=int(request.GET.get('id'))

        result={'data':{}}
        result['code'] = 0
        user=User.objects.get(user_id=request_id)
        tutor=Tutor.objects.get(user_id=user)
        result['data']['name']=user.username
        result['data']['email']=tutor.email
        result['data']['telephone']=tutor.telephone
        result['data']['address']=tutor.address
        result['data']['personalSignature']=tutor.personalSignature
        result['data']['intro']=tutor.intro
        result['data']['gender']=tutor.gender
        result['data']['age']=tutor.age
        result['data']['degree']=tutor.degree
        result['data']['rate']=tutor.rate
        result['data']['rateNum']=tutor.rateNum
        comments=Review.objects.filter(tutor_id=user)
        return_comments=[]
        for comment in comments:
            return_comments.append({
                'id':str(comment.review_id),
                'studentName':comment.student_id.username,
                'rating':comment.rating,
                'content':comment.content,
                'date':comment.date,
            })
        result['data']['comments']=return_comments
        print(result)
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})

@csrf_exempt
def getUserPosts(request):
    if request.method == 'GET':
        request_id=int(request.GET.get('id'))
        user=User.objects.get(user_id=request_id)
        posts=Post.objects.filter(user_id=user)

        return_posts=[]
        result={'data':{}}
        result['code'] = 0
        for post in posts:
            return_posts.append({
                'id':str(post.post_id),
                'title':post.title,
                'content':post.content,
            })
        result['data']['posts']=return_posts
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})

@csrf_exempt
def deletePost(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        post_id=int(body.get('id'))
        post=Post.objects.get(post_id=post_id)
        post.delete()
        result={'data':{}}
        result['code'] = 0
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

@csrf_exempt
def link(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        tutor_id=int(body.get('teacherId'))
        student_id=int(body.get('studentId'))
        tutor=User.objects.get(user_id=tutor_id)
        student=User.objects.get(user_id=student_id)

        link=Link(tutor_id=tutor,student_id=student)
        link.save()

        user_id=request.session['user_id']
        if user_id==tutor_id:
            sendNotice(student,"招聘成功",f"您正式成为{tutor.username}的学生")
        else:
            sendNotice(tutor,"应聘成功",f"您正式成为{student.username}的家教")

        result={'data':{}}
        result['code'] = 0
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})
    
@csrf_exempt
def unlink(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        tutor_id=int(body.get('teacherId'))
        student_id=int(body.get('studentId'))
        tutor=User.objects.get(user_id=tutor_id)
        student=User.objects.get(user_id=student_id)

        link=Link.objects.get(tutor_id=tutor,student_id=student)
        link.delete()

        user_id=request.session['user_id']
        if user_id==tutor_id:
            sendNotice(student,"解除招聘",f"您已经不再是{tutor.username}的学生")
        else:
            sendNotice(tutor,"解除应聘",f"您已经不再是{student.username}的家教")

        result={'data':{}}
        result['code'] = 0
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

@csrf_exempt
def refuseLink(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        tutor_id=int(body.get('teacherId'))
        student_id=int(body.get('studentId'))
        tutor=User.objects.get(user_id=tutor_id)
        student=User.objects.get(user_id=student_id)

        user_id=request.session['user_id']
        if user_id==tutor_id:
            sendNotice(student,"招聘失败",f"很抱歉，{tutor.username}未同意您的招聘")
        else:
            sendNotice(tutor,"应聘失败",f"很抱歉，{student.username}未同意您的应聘")

        result={'data':{}}
        result['code'] = 0
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})
    
@csrf_exempt
def getStudents(request):
    if request.method == 'GET':
        request_id=int(request.GET.get('id'))
        students=Link.objects.filter(tutor_id=request_id)
        return_students=[]
        result={'data':{}}
        result['code'] = 0
        for student in students:
            return_students.append({
                'id':str(student.student_id.user_id),
                'name':student.student_id.username,
            })
        result['data']['students']=return_students
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})
    
@csrf_exempt
def getTeachers(request):
    if request.method == 'GET':
        request_id=int(request.GET.get('id'))
        teachers=Link.objects.filter(student_id=request_id)
        return_teachers=[]
        result={'data':{}}
        result['code'] = 0
        for teacher in teachers:
            return_teachers.append({
                'id':str(teacher.tutor_id.user_id),
                'name':teacher.tutor_id.username,
            })
        result['data']['teachers']=return_teachers
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})


@csrf_exempt
def sendNotice(user,title,description):
    notification=Notification(
        user_id=user,
        notificationDate=datetime.now(pytz.timezone('Asia/Shanghai')),
        title=title,
        description=description,
        is_read=False,
        )
    notification.save()

@csrf_exempt
def getNotices(request):
    if request.method == 'GET':
        request_id=int(request.GET.get('id'))
        user=User.objects.get(user_id=request_id)
        notifications=Notification.objects.filter(user_id=user)

        return_notifications=[]
        result={'data':{}}
        result['code'] = 0
        for notification in notifications:
            return_notifications.append({
                'title':notification.title,
                'description':notification.description,
            })
        result['data']['notices']=return_notifications
        new_len=len(Notification.objects.filter(user_id=user,is_read=False))
        Notification.objects.filter(user_id=user).update(is_read=True)
        result['data']['newNum']=new_len
        print(result)
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})

@csrf_exempt
def submitComment(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        student_id=int(body.get('studentId'))
        tutor_id=int(body.get('teacherId'))
        rating=int(body.get('rate'))
        comment=body.get('comment')
        user=User.objects.get(user_id=student_id)
        tutor=User.objects.get(user_id=tutor_id)
        review=Review(
            student_id=user,
            tutor_id=tutor,
            rating=rating,
            content=comment,
            date=datetime.now(pytz.timezone('Asia/Shanghai')),
        )
        review.save()
        result={'data':{}}
        result['code'] = 0
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'}) 

@csrf_exempt
def submitLearningMaterial(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        tutor_id=int(body.get('teacherId'))
        student_id=int(body.get('studentId'))
        file_name=body.get('filename')
        download_link=body.get('downloadLink')
        user=User.objects.get(user_id=student_id)
        tutor=User.objects.get(user_id=tutor_id)
        material=StudyMaterial(
            tutor_id=tutor,
            student_id=user,
            file_name=file_name,
            download_link=download_link,
            upload_date=datetime.now(pytz.timezone('Asia/Shanghai')),
        )
        material.save()
        result={'data':{}}
        result['code'] = 0
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})
    
@csrf_exempt
def getLearningMaterials(request):
    if request.method == 'GET':
        request_id=int(request.GET.get('id'))
        user=User.objects.get(user_id=request_id)
        materials=StudyMaterial.objects.filter(student_id=user)

        return_materials=[]
        result={'data':{}}
        result['code'] = 0
        for material in materials:
            return_materials.append({
                'id':str(material.material_id),
                'filename':material.file_name,
                'publisher':material.tutor_id.username,
                'downloadLink':material.download_link,
                'uploadDate':material.upload_date,
            })
        result['data']['materials']=return_materials
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持GET请求'})

@csrf_exempt
def sendTodo(user,post,accepter):
    todo=Todo(
        owner_id=user,
        accepter_id=accepter,
        accept_post_id=post,
        is_completed=False,
    )
    todo.save()

@csrf_exempt
def getTodos(request):
    if request.method == 'GET':
        request_id=int(request.GET.get('id'))
        user=User.objects.get(user_id=request_id)
        todos=Todo.objects.filter(owner_id=user)

        return_todos=[]
        result={'data':{}}
        result['code'] = 0
        for todo in todos:
            return_todos.append({
                'id':str(todo.todo_id),
                'postId':todo.accept_post_id.post_id,
                'accepterName':todo.accepter_id.username,
                'accepterId':todo.accepter_id.user_id,
            })
        result['data']['todos']=return_todos
        return JsonResponse(result)
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