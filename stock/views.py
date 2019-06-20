# Create your views here.
import sys

from django.http import HttpResponse

# 导入项目相对路径
# sys.path.insert(0, '.\\stock_app')
# 导入项目绝对路劲
sys.path.insert(0, 'C:\\Users\\Saber\\Desktop\\Saber\\stock\\stock_app')
# sys.path.insert(1,'C:\\Users\\Saber\\Desktop\\Saber\\stock\\stock_app\\controller')
sys.path.insert(2, 'C:\\Users\\Saber\\Desktop\\Saber\\stock\\stock_app\\utils')
# sys.path.insert(3,'C:\\Users\\Saber\\Desktop\\Saber\\stock\\stock_app\\modle')
import sql_utils as su
import json


def parse_post(request):
    if request.method != 'POST':
        return HttpResponse('需要POST请求')

    post_body = request.body
    if post_body is None:
        return HttpResponse('入参不能为空')

    received_json_data = json.loads(post_body)
    name = received_json_data.get('name')
    date = received_json_data.get('date')

    if name is None:
        return HttpResponse('name 入参不能为空')

    if date is None:
        return HttpResponse('date 入参不能为空')
    return name, date


def get_popularity_data(request):
    """后去股票热度指数"""
    response = parse_post(request)
    if type(response) is HttpResponse:
        return response
    name, date = response
    res = su.get_clear_popularity_data(name, date)
    return HttpResponse(res.to_json(), content_type='application/json')


def get_jetton_data(request):
    """后去股票筹码分布"""
    response = parse_post(request)
    if type(response) is HttpResponse:
        return response
    name, date = response
    res = su.get_clear_jetton_data(name, date)
    return HttpResponse(res.to_json(), content_type='application/json')


def get_stock_data(request):
    """后去股票详情"""
    response = parse_post(request)
    if type(response) is HttpResponse:
        return response
    name, date = response
    res = su.get_clear_stock_data(name, date)
    return HttpResponse(res.to_json(), content_type='application/json')
