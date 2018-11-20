from django.http import HttpResponse, JsonResponse,HttpResponseRedirect,Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, render
from app01.models import Accont , Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import app01.fileUtil as fileUtil
import json
# Create your views here.

def is_login(func):
    '''
        登录装饰器
    '''
    def wrapper(request):
        if request.session.get('is_login', None):
            return func(request)
        else:
            return HttpResponseRedirect('/login/')
    return wrapper

@is_login
def getAdvertisingList(request):
    '''
        分页显示文章
    '''
    username = request.session['username']
    allArticle = Article.objects.all()
    count = len(allArticle)
    paginator = Paginator(allArticle,10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    response = {'count':count,'advertisings':articles,'username':username}
    return render_to_response('article-list.html',response)

@is_login
def delAdvertising(request):
    '''
        删除文章
    '''
    if request.method == 'POST':
        article = Article.objects.get(id=request.POST.get('id'))
        response = {'msg':'','code':0}
        if article == None:
            response['msg'] = '该文章不存在'
            response['code'] = 0
        else:
            res = article.delete()
            if res[0] == 1:
                response['msg'] = '删除成功'
                response['code'] = 1
            else:
                response['msg'] = '删除失败'
                response['code'] = 0
        return JsonResponse(response)
    else:
        return render_to_response('404.html')

@is_login
def addAdvertisingHtml(request):
    return render_to_response('article-add.html')

def updAdvertising(request):
    pass

@is_login
def addAdvertising(request):
    '''
        添加文章
    '''
    response = {'msg':'','code':0}
    if request.method == 'POST':
        title = request.POST.get('title')
        source = request.POST.get('source')
        url =request.POST.get('URL')
        imgs = request.FILES.getlist('img')
        article = Article(title=title,source=source,url=url)
        art = Article.objects.filter(title=title)
        if len(art) == 0:
            try:
                article.head_img = fileUtil.article_dir_path(article,imgs[0]) 
                article.head_img2 = fileUtil.article_dir_path(article,imgs[1])
                article.head_img3 = fileUtil.article_dir_path(article,imgs[2])
            except IndexError:
                pass
            finally:
                article.save()
                response['msg'] = '添加成功'
                response['code'] = 1
        else:
            response['msg'] = '标题已存在'
            response['code'] = 0
        return JsonResponse(response)
    else:
        return render_to_response('404.html')


def loginHtml(request):
    return render_to_response('login.html')

def dologin(request):
    '''
        登录
    '''
    if request.method == 'POST':
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        accont = Accont.objects.filter(name=name,password=pwd)
        response = {'msg':'','code':0}
        if len(accont) == 0:
            response['msg'] = '用户名或密码错误'
            response['code'] = 0
        else:
            request.session['username'] = name
            request.session["is_login"] = True
            response['msg'] = '登录成功'
            response['code'] = 1
        return JsonResponse(response)
    else:
        return render_to_response('login.html')

@is_login
def logout(request):
    '''
        退出登录
    '''
    request.session.clear()
    return render_to_response('login.html')

def get_all_information(request):
    '''
        获取所有资讯
    '''
    allArticle = list(Article.objects.all().values("id","title","source","head_img","head_img2","head_img3","url"))
    count = len(allArticle)
    response = {'count':count, 'date': allArticle}
    resp = HttpResponse(json.dumps(response))
    resp['Access-Control-Allow-Origin'] = '*'
    return resp