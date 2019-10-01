from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'index.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dic = {}
    for word in word_list:
        if word in word_dic:
            #increase
            word_dic[word] +=1
        else:
            #add to the dic
            word_dic[word] = 1

    sorted_words =sorted(word_dic.items(), key=operator.itemgetter(1),reverse= True)           
    
         



    return render(request, 'count.html',{'fulltext':fulltext,'count': len(word_list), 'sorted_words':word_dic.items()})
def about(request):
    return render(request, 'about.html')

   