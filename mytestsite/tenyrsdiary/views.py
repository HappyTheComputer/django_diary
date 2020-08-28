from django.shortcuts import render

# Create your views here.
def toDay(request):
    print('click today!')
    return render(request, 'tenyrsdiary/index.html')

def lastDay(request):
    print('click last day!')
    return render(request, 'tenyrsdiary/index.html')

def nextDay(request):
    print('click next day!')
    return render(request, 'tenyrsdiary/index.html')

def inputDiary(request):
    print('input diary!')
    return render(request, 'tenyrsdiary/index.html')