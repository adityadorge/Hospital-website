from django.http import HttpResponse
from django.shortcuts import render 
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse
import requests
import tweepy


# Create your views here.
def index(request):
	#return HttpResponse("Hello world")
	return render(request, 'Hospital_App/temp.html')

def stats(request):
	data=requests.get('https://corona.lmao.ninja/v2/countries?yesterday&sort').json()
	country_name=request.GET.get('search')
	if country_name:
		return HttpResponseRedirect(reverse('Hospital_App:spec_stats',args=[country_name]))						
	return render(request,'Hospital_App/stats.html',{'data':data})

def spec_stats(request,country_name):
	data=requests.get(f'https://corona.lmao.ninja/v2/countries/{country_name}').json()
	return render(request,'Hospital_App/spec_stats.html',{'data':data})

def tweets(request):
	auth = tweepy.OAuthHandler('VIZN84XeKrtocHWmIFVT0kwYI','wRfJ7U1bcZxWaWjchYChZXjhQWQhqZsxTWbucjNzibEhAIq24t','1521125708767973376-daUhUcFUSiiqu4eaGGCrZvjTRFiSs0', 'zzVzdYVBiGV7ZwnjE3TZ3tPpk3idhr7hr6evvSTuHi602')
	api = tweepy.API(auth)
	# search_words = ["#Health"]
	# date_since = "2020-05-21"
	tweets = tweepy.Cursor(api.search_tweets ,q=["#Health"],lang="en",since_id="2020-05-21").items(50)
	tweets_copy = []
	for tweet in tweets:
		tweets_copy.append(tweet.text)
	return render(request,'Hospital_App/tweets.html',{'tweets_copy':tweets_copy})
