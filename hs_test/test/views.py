# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User

def user_page(request, username):
    user = User.objects.get(username=username)
    
    hs_test = user.hs_test_set.all()
    
    templete = get_template('user_page.html')
    variable = Context({
                        'username': username,
                        'hs_test': hs_test,
    })
    output = templete.render(variable)
    return HttpResponse(output)


def main_page(request):
    templete = get_template('main_page.html')
    variable = Context({
                        'head_title': '장고 북마크',
                        'page_title': '장고 북마크에 오신것을 환영합니다',
                        'page_body': '북마크를 저장하고 공유하세요..^^',
    })
    output = templete.render(variable)
    return HttpResponse(output)
    
