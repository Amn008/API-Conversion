import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
r = SpeechToTextV1(
    username='',
    password='',
    url='https://stream.watsonplatform.net/speech-to-text/api')
with open(join(dirname(__file__), 'output.wav'),
          'rb') as source:
    
   print( (((r.recognize(
                audio=source,
                content_type='audio/wav')['results'][0])['alternatives'])[0])['transcript'])
