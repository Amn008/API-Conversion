# coding=utf-8
from __future__ import print_function
import json
from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(version='2018-05-31',username='',password='')

example_text ='Hola, cómo estás?'
target_lang='en'
print(json.dumps(language_translator.translate(example_text, source='es',target=target_lang, indent=2)))
'''
print(json.dumps(
    language_translator.translate('Hola, cómo estás?', source='es',
                                  target='en'), indent=2,
    ensure_ascii=False))

print(json.dumps(
    language_translator.translate('Messi is the best ever',
                                  model_id='en-es-conversational'),
    indent=2))

print(json.dumps(language_translator.identify('你好'), indent=2))

#print(json.dumps(language_translator.list_identifiable_languages(), indent=2))
'''
