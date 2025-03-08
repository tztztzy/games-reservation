from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import users
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        errormsg = ''
        
        if not phone:
            errormsg = '手机号不能为空'
        elif not password:
            errormsg = '密码不能为空'
        
        if not errormsg:
            try:
                user_obj = users.objects.get(phone_number=phone)
                # 使用Django的check_password函数验证密码
                if check_password(password, user_obj.password):
                    # 登录成功，将用户信息存入session
                    request.session['user_id'] = user_obj.id
                    request.session['user_name'] = user_obj.user_name
                    return redirect('/home')
                else:
                    errormsg = '密码错误'
            except Exception as e:
                # 处理查询不到用户的情况
                errormsg = '账号不存在，请重新输入'
        
        return render(request, 'login.html', {'message': errormsg})
    
    return render(request, 'login.html')

def logout(request):
    # 清除session
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_name' in request.session:
        del request.session['user_name']
    return redirect('/login')

def register(request):
    return render(request, 'register.html')

def save_register(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        student_number = request.POST.get('student_number')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        
        errormsg = ''
        if not phone:
            errormsg = '手机号不能为空'
        elif not username:
            errormsg = '用户名不能为空'
        elif not student_number:
            errormsg = '学号不能为空'
        elif not password:
            errormsg = '密码不能为空'
        elif password != repassword:
            errormsg = '确认密码与密码不一致'
        
        # 检查手机号和学号是否已存在
        if not errormsg:
            if users.objects.filter(phone_number=phone).exists():
                errormsg = '该手机号已被注册'
            elif users.objects.filter(student_number=student_number).exists():
                errormsg = '该学号已被注册'
        
        if not errormsg:
            # 创建新用户 - 密码会在save方法中自动加密
            users.objects.create(
                user_name=username,
                phone_number=phone,
                student_number=student_number,
                password=password
            )
            # 注册成功，重定向到登录页
            return redirect('/login')
        else:
            return render(request, 'register.html', {'errormsg': errormsg})
    
    return redirect('/register')