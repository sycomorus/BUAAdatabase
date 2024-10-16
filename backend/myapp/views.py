from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import random
from datetime import datetime, timedelta
from .models import User, RecruitmentPost

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
                tags=subjects
            )
            print("out")
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