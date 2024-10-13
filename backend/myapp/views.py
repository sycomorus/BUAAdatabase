from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import random
from datetime import datetime, timedelta

def home(request):
    return HttpResponse("Welcome to the Home Page")

@csrf_exempt
def login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        name = body.get('name')
        password = body.get('password')

        result = {'data': {}}
        success = False

        if name == 'admin' and password == '888888':
            success = True
            result['data']['permissions'] = [{'id': 'queryForm', 'operation': ['add', 'edit']}]
            result['data']['roles'] = [{'id': 'admin', 'operation': ['add', 'edit', 'delete']}]
        elif name == 'teacher' and password == '888888':
            success = True
            result['data']['permissions'] = [{'id': 'queryForm', 'operation': ['add', 'edit']}]
            result['data']['roles'] = [{'id': 'teacher', 'operation': ['add', 'edit', 'delete']}]
        elif name == 'student' and password == '888888':
            success = True
            result['data']['permissions'] = [{'id': 'queryForm', 'operation': ['add', 'edit']}]
            result['data']['roles'] = [{'id': 'student', 'operation': ['add', 'edit', 'delete']}]
        else:
            success = False

        if success:
            result['code'] = 0
            result['message'] = '欢迎回来'
            result['data']['user'] = {
                'name': name,
                'avatar': 'https://example.com/avatar.png',
                'address': 'City',
                'position': 'Position'
            }
            result['data']['token'] = 'Authorization:' + str(random.random())
            result['data']['expireAt'] = (datetime.now() + timedelta(minutes=30)).isoformat()
        else:
            result['code'] = -1
            result['message'] = '账户名或密码错误（admin/888888 or test/888888）'

        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})
    
@csrf_exempt
def register(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        name = body.get('name')
        password = body.get('password')
        role = body.get('role')

        # 处理注册逻辑，例如保存到数据库
        # 假设注册成功
        result = {
            'code': 0,
            'message': '注册成功',
            'data': {
                'name': name,
                'role': role
            }
        }
        return JsonResponse(result)
    else:
        return JsonResponse({'code': -1, 'message': '仅支持POST请求'})


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