from django.shortcuts import render, redirect
from django import forms
from django.forms import fields
class F1Form(forms.Form):
    user = fields.CharField(
        max_length=10, min_length=3, required=True,   # 不能为空
        error_messages={
            'required': '用户名不能为空',
            'max_length': '太长',
            'min_length': '太短',
        }
    )
    pwd = fields.CharField(min_length=8, required=True)
    age = fields.IntegerField(required=True,
                              error_messages={
                                  'required': '年龄不能为空',
                                  'invalid': '为数字'               #格式错误
                              })
    email = fields.EmailField(required=True)
    #上面的名字不是瞎起的，是对应前端的input标签的name
def f1(request):
    if request.method == 'GET':
        ob = F1Form()
        return render(request, 'f1.html', {'ob': ob})
    else:
        obj = F1Form(request.POST)    #Post有所有前端数据
        if obj.is_valid():            #全て验证成功
            print('验证成功', obj.cleaned_data)   #验证成功的数据
            return redirect('http://www.xiaohuar.com')
        else:
            print('失敗した', obj.errors)
            return render(request, 'f1.html', {'obj': obj})

