from django.shortcuts import render
import re

# Create your views here.
def homepage(request):
    return render(request, "index.html",)

def wordcounter(request):
    fulltext = request.POST["fulltext"]
    textlist = re.split(', |_|-|!| |',fulltext)
    wordlength = len(textlist)
    wordDictionaries = {}
    for word in textlist:
        if word in wordDictionaries:
            wordDictionaries[word] += 1
        else:
            wordDictionaries[word] = 1
    return render(request, "counter.html", {'wordlength': wordlength, 'fulltext': fulltext,'wordDictionaries': wordDictionaries})
