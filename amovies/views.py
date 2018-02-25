from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from amovies.models import Users, Movies, MyCollects


def login(request):
    return render(request,'login.html')


def register(request):

    return render(request,'register.html')

def dologin(request):
    username = request.POST.get('username')
    password = request.POST.get('userpassword')
    user = Users.objects.filter(u_name=username)
    if len(user) > 0:
    # 比对用户名 密码
        if user.first().u_password == password:
            request.session['username'] = username
        #     登录成功   跳转回个人中心
            response = HttpResponseRedirect(reverse('amovies:home_logined'))
            return response
        else:
            return redirect(reverse('amovies:login'))

def doregister(request):

    try:
        username = request.POST.get("username")
        usericon = request.FILES["usericon"]
        password = request.POST.get("userpassword")
        email = request.POST.get("useremail")

        u = Users()
        u.u_name = username
        u.u_icons = usericon
        u.u_password = password
        u.u_email = email
        u.save()

        request.session['username'] = username
        return redirect(reverse('amovies:home_logined'))
    except Exception as e:
        print("注册失败")
        return HttpResponse("注册失败")


def home_logined(request):

    username = request.session.get("username")
    if username == None:
        username = "未登录"
        usericon = ''
        is_login = False
    else:
        is_login = True
        user = Users.objects.get(u_name=username)
        # usericon = "http://127.0.0.1:8000/static/uploadfiles/" + user.u_icon.path
        usericon = "http://127.0.0.1:8000/static/uploadfiles/" + user.u_icons.url

        # print(usericon)
    movies = Movies.objects.all()
    context = {
        "username": username,
        "usericon": usericon,
        "movies": movies,
        "is_login": is_login,
    }

    return render(request, 'home_logined.html', context=context)


def userinfo(request):

    username = request.session.get("username")
    uname = Users.objects.get(u_name=username)
    # usericon = uname.u_icons
    usericons = "http://127.0.0.1:8000/static/uploadfiles/" + uname.u_icons.url
    context = {
        "username": username,
        "usericon":usericons,
    }
    return render(request, 'userinfo.html', context=context)


def douserinfo(request):

    username = request.session.get("username")
    uname = Users.objects.get(u_name=username)

    icons = request.FILES['icon']
    email = request.POST.get('email')

    uname.u_icons = icons
    uname.u_email = email

    uname.save()

    return redirect(reverse("amovies:home_logined"))


def home(request):

    movies = Movies.objects.all()
    context = {
        "movies": movies,
    }

    return render(request, 'home.html', context=context)


def home_logined_collected(request):
    # 判断是否登录
    username = request.session.get("username")
    uname = Users.objects.get(u_name=username)
    usericon = "http://127.0.0.1:8000/static/uploadfiles/" + uname.u_icons.url
    print(usericon)
    if username == None:
        return redirect(reverse("amovies:login"))
    user = Users.objects.get(u_name=username)

    # print(type(user))
    mycollects = MyCollects.objects.filter(m_users=user)
    # print(type(mycollects))

    movies = Movies.objects.all()
    context = {
        "mycollects": mycollects,
        "username":username,
        "usericon":usericon,
        "movies":movies,
    }

    return render(request, 'home_logined_collected.html', context=context)


def addtomycollect(request):

    username = request.session.get("username")
    if username == None:
        return JsonResponse({"msg": "您还没有登录不能收藏，请先登录"})
    # 用户已登录
    movie_id = request.GET.get("movieid")
    movies = Movies.objects.get(pk=movie_id)
    # 获取登录用户信息
    user = Users.objects.get(u_name=username)
    # 去数据库中查找
    m = MyCollects.objects.filter(m_users=user).filter(m_movies=movies)
    if len(m) == 0:
        m = MyCollects()
    else:
        m = m.first()

    m.m_users = user
    m.m_movies = movies

    m.save()
    return JsonResponse({"msg": "添加成功"})


def delmycollect(request):
    mycollectid = request.GET.get("mycollectid")

    collect = MyCollects.objects.get(pk=mycollectid)
    collect.delete()

    return JsonResponse({"msg": "删除成功"})