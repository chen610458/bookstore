import datetime
from django.shortcuts import render
from django.http import HttpResponse

time=datetime.datetime.now()
strtime=" "
timenow=time.hour
def main(request):
    if timenow <= 12:
        strtime="如果是上午：歡迎光臨，來杯提神的咖啡吧"
    else:
        strtime="如果是下午：歡迎光臨，來份下午茶吧" 
    return HttpResponse(strtime)


# Create your views here.
