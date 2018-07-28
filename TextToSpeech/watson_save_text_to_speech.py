#from __future__ import print_function
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
username='',
password='')

#print(json.dumps(text_to_speech.list_voices(), indent=2))

with open(join(dirname(__file__), 'output.wav'),
'wb') as audio_file:
	audio_file.write(
		text_to_speech.synthesize('Hi this is audio file for speech to text API', accept='audio/wav',
		voice="en-US_AllisonVoice").content)

#print(json.dumps(text_to_speech.get_pronunciation('Watson', format='spr'), indent=2))

# print(json.dumps(text_to_speech.list_voice_models(), indent=2))
