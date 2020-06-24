# I have created this file - Yash Mathur.
from django.http import HttpResponse
from django.shortcuts import render

# var = open("C:/Users/ranu hp/Desktop/BasicDraft.txt", "r")
# var1 = var.read()
# print(var.read())

# DJANGO TUTORIAL 0-7
# def index(request):
#     return HttpResponse('''<a href = "http://www.google.com" target = "_blank"> <h1 style = "color: brown;">Way To Google</h1> </a>
#      <a href = "http://www.youtube.com" target = "_blank"> <h1 style = "color: brown;">Way to Youtube</h1> </a>
#      <a href = "http://www.facebook.com" target = "_blank"> <h1 style = "color: brown;">Way To Facebook</h1> </a>
#      <a href = "http://www.instagram.com" target = "_blank"> <h1 style = "color: brown;"> Way To Instagram </h1> </a>
#      <a href = "http://www.linkedin.com" target = "_blank"> <h1 style = "color: brown;"> Way To Linkedin </h1> </a> ''')

# DJANGO TUTORIAL 8
# def index(request):
#
#     return render(request,'index.html')
#     # return HttpResponse("Home")
#
#
# def removepunc(request):
#     var = request.GET.get("text", "default")
#     print(var)
#     var1 = var.upper()
#     # print(var1)
#     return HttpResponse('''<a href = "http://127.0.0.1:8000/"> <h3> Back To Home Page </h3> </a> Remove Punc
#      <br>'''), HttpResponse(var1)
#
# def capfirst(request):
#     return HttpResponse(''' <a href = "http://127.0.0.1:8000/"> <h3> Back To Home Page </h3> </a> Capitalize First''')
#
# def newlineremove(request):
#     return HttpResponse(''' <a href = "http://127.0.0.1:8000/"> <h3> Back To Home Page </h3> </a>NewLine Remove First''')
#
# def spaceremove(request):
#     return HttpResponse(''' <a href = "http://127.0.0.1:8000/"> <h3> Back To Home Page </h3> </a>Space Remover''')
#
# def charcount(request):
#     return HttpResponse(''' <a href = "http://127.0.0.1:8000/"> <h3> Back To Home Page </h3> </a> CharCount''')

# Tutorial 9

def home(request):
    return render(request,'index.html')

def links(request):
    return render(request,'links.html')

def analyse(request):
    var = request.POST.get('text','harry')
    var1 = request.POST.get('remove Punctuation', 'off')
    var2 = request.POST.get('Upper Case', 'off')
    var3 = request.POST.get('Lower Case', 'off')
    var4 = request.POST.get('Space Remover', 'off')
    var5 = request.POST.get('charcount', 'off')
    # print(var)

    for i in var:
        print(i,end=" ")

    print("")
    print(var1,var2,var3,var4)
    final = ""
    result = 0

    if(var1=='on'):
        list = [',' , ';' , ':' , '.' , '!' , '?' , '"' , "'" , '-' , '/'  , '(' , ')' , '[' , ']' , '...' , '*']
        for i in var:
            if(i not in list):
                final+=i
            else:
                continue

        result = {'type2': final}

    if(var2=='on'):
        if len(final)==0:
            final = var
            final = final.upper()
            result = {'type2': final}

        else:
          final = final.upper()
          result = {'type2': final}


    if(var3=='on'):
        if(len(final)==0):
            final=var
            final = final.lower()
            result = {'type2': final}
        else:
            final = final.lower()
            result = {'type2': final}


    if(var4=='on'):
        if(len(final)==0):
            final = var
            for i in final:
                if(i==" "):
                   final = final.replace(" ","")

            result = {'type2': final}

        else:
            for i in final:
                if(i==" "):
                    final = final.replace(" ","")

            result = {'type2': final}

    if(var5=='on'):
        if(len(final)!=0):
            final = len(final)
            result = {'type2': final}

        else:
            final = len(var)
            result = {'type2': final}

    print(final)

    if(var1=='off'and var2=='off'and var3=='off' and var4=='off'):
        final = ''
        result = {'type2':final}

    return render(request,'analyse.html',result)














