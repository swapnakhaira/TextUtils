
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def about(requests):
    return HttpResponse("hello My Son")

def home(requests):
    return HttpResponse('''<h1>This is my home</h1> <a href= "https://timesofindia.indiatimes.com/defaultinterstitial.cms">times of india</a>''')

def analyze(request):
    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines','analyzed_text':  analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if(charcount == "on"):

        count = 0
        for i in djtext:
            count = count+1
            # analyzed = analyzed + len(str(char))
        params = {'purpose': 'Count the character', 'analyzed_text': count}
        djtext = count

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcount != "on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)

def capfirst(request):
    s = '''<h2>Navigation Bar<br></h2>
    <a href ="http://127.0.0.1:8000/home/">Go to home page"</a><br>
        <a href = "https://timesofindia.indiatimes.com/defaultinterstitial.cms">TOI</a><br>
        <a href = "https://www.hindustantimes.com">HTN</a>'''
    return HttpResponse(s)

