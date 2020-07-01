from django.shortcuts import render
import re

# Create your views here.
def homepage(request):
    return render(request, "index.html",)

def about(request):
    return render(request, "about.html")

def wordcounter(request):
    fulltext = request.POST["fulltext"]
    fulltext = fulltext.strip()
    textlist = re.split(', |_|-|!|@|#|$|%|"|&|.|*|;|:| |',fulltext)
    wordlength = len(textlist)
    new_text_list = []
    i = 0
    while wordlength > i:
        if textlist[i] == "":
            i = i + 1
            continue
        new_text_list.append(textlist[i])
        i = i + 1
    wordlength = len(new_text_list)
    wordDictionaries = {}
    for word in new_text_list:
        if word.lower() in wordDictionaries:
            wordDictionaries[word.lower()] += 1
        else:
            wordDictionaries[word.lower()] = 1
    return render(request, "counter.html", {'wordlength': wordlength, 'fulltext': fulltext,'wordDictionaries': wordDictionaries})
