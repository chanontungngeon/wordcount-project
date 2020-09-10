

from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import operator
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist = fulltext.split()
    wordcount_dict={}
    for word in wordlist:
        if word in wordcount_dict:
            wordcount_dict[word] += 1
        else:
            wordcount_dict[word] = 1

    sortedwords = sorted(wordcount_dict.items(), key=operator.itemgetter(1), reverse=True)
    # x=Counter(wordlist)
    # print(x)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'wordcount_dict':sortedwords})

def about(request):
    return render(request, 'about.html')


def testplot(request):
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    response = HttpResponse(content_type = 'image/png')
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(response)
    response
    return render(request, 'testplt.html',{'response':response})
