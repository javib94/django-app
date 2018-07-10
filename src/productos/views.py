from django.shortcuts import render
from django.http import HttpResponse
import redis 
import os

# Create your views here.

def index(request):
	redis = os.environ['REDIS_URL']	
	redisClient = redis.StrictRedis(host=redis, port=6379, db=0)
	numbers = "numbers"
	chain = request.GET.get("cadena")
	redisClient.hset(numbers, chain, chain)
		
	return HttpResponse("<h1>String "+ chain + " saved. </h1>")



def elements(request):
	redis = os.environ['REDIS_URL']	
	redisClient = redis.StrictRedis(host=redis, port=6379, db=0)
	numbers = "numbers"
	values = redisClient.hgetall(numbers)
	ressponse = '<table > <tr><th>Strings</th></tr> '
	for val in values: 
		ressponse+='<tr><td>'+val.decode('ascii')+'</td></tr>'

	ressponse+= "</table>"
	return HttpResponse(ressponse)
