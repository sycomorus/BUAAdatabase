from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import random
from datetime import datetime, timedelta
from .models import User, RecruitmentPost,JobPost

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
                raise Exception("Unknown identity")
            result['data']['id'] = str(user.id)

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
            result={'data':{}}
            if role == "admin":
                identity = 0
                result['data']['roles']=[{'id': 'admin'}]
            elif role == "teacher":
                identity = 1
                result['data']['roles']=[{'id': 'teacher'}]
            elif role == "student":
                identity = 2
                result['data']['roles']=[{'id': 'student'}]
            user = User(username=username, 
                        password=password, 
                        identity=identity, 
                        registration_date=datetime.now())
            user.save()
            result['code'] = 0
            result['data']['token']="Authorization:" + str(random.random())
            result['data']['id'] = str(user.id)
            return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

@csrf_exempt
def sendPost(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        id=body.get('id')
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
        
        # try :
        #     user=User.objects.get(id=id)
        # except User.DoesNotExist:
        #     return JsonResponse({'code': -1, 'message': '用户不存在'})
        
        # if user.identity ==0:
        #     raise Exception("管理员无法发帖")
        # elif user.identity ==1:
        #     jobPost=JobPost(
        #         user_id=User.objects.get(id=id),
        #         title=title,
        #         startDate=startDate,
        #         endDate=endDate,
        #         subjects=subjects,
        #         location=location,
        #         fullLocation=fullLocation,
        #         telephoneNumber=telephoneNumber,
        #         emailAddress=email,
        #         content=content,
        #         tags=subjects,
        #         is_completed=is_complete,
        #     )


        try:
            # 创建招聘帖
            recruitmentPost = RecruitmentPost(
                user_id=User.objects.get(id=id),
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
                is_completed=is_complete,
            )
            recruitmentPost.save()
            result={'data':{}}
            result['code'] = 0
            return JsonResponse(result)
        except Exception as e:
            print(e)
            result={'data':{}}
            result['code'] = -1
            return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

@csrf_exempt
def savePost(request):
    print("bbbbb")
    if request.method == 'POST':
        print("aaaaaaaa")
        body = json.loads(request.body)
        id=body.get('id')
        title = body.get('data').get('title')
        startDate = body.get('data').get('startDate') or None
        endDate = body.get('data').get('endDate') or None
        subjects=body.get('data').get('subjects')
        location=body.get('data').get('location')
        fullLocation=body.get('data').get('fullLocation')
        telephoneNumber=body.get('data').get('telephoneNumber') or None
        email=body.get('data').get('emailAddress') or None
        content=body.get('data').get('content')
        try:
            # 创建招聘帖
            print("in")
            recruitmentPost = RecruitmentPost(
                user_id=User.objects.get(id=id),
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
            recruitmentPost.save()
            result={'data':{}}
            result['code'] = 0
            print("out")
            return JsonResponse(result)
        except Exception as e:
            print(e)
            result={'data':{}}
            result['code'] = -1
            return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})

@csrf_exempt
def getSavedPost(request):
    if request.method == 'GET':
        try:
            user_id=request.GET.get('id')
            post=RecruitmentPost.objects.get(user_id=user_id,is_completed=False)
            result={'data':{}}
            result['code'] = 0
            result['data']['title']=post.title
            result['data']['startDate']=post.startDate
            result['data']['endDate']=post.endDate
            result['data']['subjects']=post.subjects
            result['data']['location']=post.location
            result['data']['fullLocation']=post.fullLocation
            result['data']['telephoneNumber']=post.telephoneNumber
            result['data']['emailAddress']=post.emailAddress
            result['data']['content']=post.content
            return JsonResponse(result)
        except RecruitmentPost.DoesNotExist:
            result={'data':{}}
            result['code'] = 0
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