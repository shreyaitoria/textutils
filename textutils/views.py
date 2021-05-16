#i have created this file_ shreya
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request,'index.html')

def analyze(request):
     djtext=request.POST.get('text','off')
     removepunc =request.POST.get('removepunc', 'off')
     capfirst = request.POST.get('capfirst', 'off')
     lower=request.POST.get('lower', 'off')
     spaceremove=request.POST.get('spaceremove', 'off')
     charcount = request.POST.get('charcount', 'off')
     analyzed = djtext
     if removepunc!='off':
          analyzed=''
          punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          for char in djtext:
               if char not in punctuations:
                    analyzed=analyzed +  char
          l = "not counted"
          params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed, 'length': l}
     if capfirst!='off':
          analyzed=analyzed.upper()
          print(analyzed)
          l="not counted"
          params = {'purpose': 'uppercase', 'analyzed_text': analyzed, 'length': l}
     if lower!='off':
          analyzed =analyzed.lower()
          l = "not counted"
          params = {'purpose': 'new line remover', 'analyzed_text': analyzed, 'length': l}
     if spaceremove!='off':
          djtext = analyzed
          analyzed = ""
          for index, char in enumerate(djtext):
               if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char
          l="not counted"
          params = {'purpose': 'extra sapce remover', 'analyzed_text': analyzed, 'length': l}
     if charcount!="off":
          l=len(analyzed)
          params = {'purpose': 'character count', 'analyzed_text': analyzed, 'length': l}

     return render(request,'analyze.html',params)
