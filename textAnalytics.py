#Sentiment analysis of consultation data
import os
import csv
import json
import requests
from pprint import pprint

text_analytics_base_url = "https://northeurope.api.cognitive.microsoft.com/text/analytics/v2.0/"
#subscription_key = "56957c0c36d84eec8dfbef92cda9a57a" #CP subscription key
subscription_key = "62b509ed027a4fb884cb2969bbc72756" #Visual Studio Pro subscription (VR)
sentiment_api_url = text_analytics_base_url + "sentiment"
#sentiment_api_url = text_analytics_base_url + "keyPhrases"
print(sentiment_api_url)

#Pre-processing
#Read consultation results (csv format)
dir = os.path.dirname(os.path.realpath(__file__))
print(dir)

inputFilePath = dir + "/consultation-09-03-2018-17-59-44.csv"

count = 0

list = []
with open(inputFilePath) as csvFile:
	reader = csv.reader(csvFile)
	#reader = csv.DictReader(csvFile)
	#rows = list(reader)	
	for row in reader:
		data = {}
		
		count += 1
		text = row[12].strip()
		if not text:
			continue
		
		
		data['id'] = str(count)
		data['language'] = 'en'
		data['text'] = text
		list.append(data)
		#if count > 500:
			#print(row[12])			
			#break;

print('number of non empty records')
print(count)		
			
documents = {}
documents['documents'] = list
	
#print(results)
	
#Read consultation results from citizen-space API
#TODO

#documents = {'documents' : [
#  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
#  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
#  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
#  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
#]}

#Send the data to the API

headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
#pprint(sentiments)

outputJsonPath = dir + "/sentiments_output.json"
#outputJsonPath = dir + "/key_phrases_output.json"
with open(outputJsonPath, "w") as outputfile:
	json.dump(sentiments, outputfile)
