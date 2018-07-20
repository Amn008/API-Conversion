# -*- coding: utf-8 -*- 
from google.cloud import translate
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/aman/Desktop/Final/LanguageTranslator/NewAgent-9c23594fa4f6.json'

def translate_text(text,target='en'):
    

    translate_client = translate.Client()
    result = translate_client.translate(text,target_language=target)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(result['detectedSourceLanguage']))

example_text ='Hola, cómo estás?'
target_lang='en'
translate_text(example_text.decode('utf-8'),target=target_lang)