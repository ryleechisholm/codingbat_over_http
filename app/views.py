from django.http.response import HttpResponse
from django.http.request import HttpRequest 
from django.shortcuts import render

def near_hundred(request: HttpRequest, num: int) -> HttpResponse:
    return HttpResponse((abs(100 - num) <= 10) or (abs(200 - num) <= 10))

def string_splosion(request: HttpRequest, str: str) -> HttpResponse:
    result = ""
    for i in range(len(str)):
        result = result + str[:i+1]
    return HttpResponse(result)

def cat_dog(request: HttpRequest, str: str) -> HttpResponse:
    return HttpResponse(str.count("cat") == str.count("dog"))

def lone_sum(request: HttpRequest, a: int, b: int, c: int) -> HttpResponse:
    if a == b == c:
        return HttpResponse(0)
    elif b == c:
        return HttpResponse(a)
    elif a == c:
        return HttpResponse(b)
    elif a == b:
        return HttpResponse(c)
    else:
        return HttpResponse(a + b + c)