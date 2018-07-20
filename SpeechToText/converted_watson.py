from watson_developer_cloud import SpeechToTextV1
from os.path import join, dirname
cred= SpeechToTextV1(username='0e66a1df-d369-43fe-b32f-1d18c199314f',password='bIeZjddxuyWW')
with open(join(dirname(__file__), 'output.wav'),'rb') as source:
	print( (((cred.recognize(audio=source,content_type='audio/wav')['results'][0])['alternatives'])[0])['transcript'])