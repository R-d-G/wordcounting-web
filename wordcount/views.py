from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request,'home.html',{'thisis':'my name'})

def count(request):
	fulltext=request.GET['fulltext']
	wordlist=fulltext.split()
	Dict={}
	for word in wordlist:
		if(word in Dict):
			Dict[word]+=1
		else:
			Dict[word]=1
	sortedwords=sorted(Dict.items(),key=operator.itemgetter(1),reverse=True)
	return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'Dict':sortedwords})

def about(request):
	return render(request,'about.html')