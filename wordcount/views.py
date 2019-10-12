from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html', {'x': 'Hi I am Designing My Second WepSite'})


def count(request):
    fulltext = request.GET['fulltext']
    # request.GET[] we use it to get the value of url parameter which is named here as 'fulltext' and we store it in variable
    words = fulltext.split()
    # split() function split a string into words depending on space
    worddictionary = {}
    for word in words:
        if word in worddictionary:
            # increase by 1
            worddictionary[word] += 1
        else:
            # add to wordsdictionary
            worddictionary[word] = 1
    wordsorted = sorted(worddictionary.items(),
                        key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'words': len(words), 'wordsorted': wordsorted})


def about(request):
    return render(request, 'about.html')
