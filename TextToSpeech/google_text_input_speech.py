from google.cloud import texttospeech
import pyglet

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/aman/Desktop/Final/TextToSpeech/DJANGO-API-IMPLEMENT-37d0007f53c4.json'
texttospeak='Aman Dalal'

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.types.SynthesisInput(
    text=texttospeak
         )
voice = texttospeech.types.VoiceSelectionParams(language_code='en-US', ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)
response = client.synthesize_speech(synthesis_input, voice, audio_config)

with open('text_output_speech.mp3', 'wb') as out:
    out.write(response.audio_content)
out.close()


music = pyglet.resource.media('text_output_speech.mp3')
music.play()

pyglet.app.run()
print"fuck"