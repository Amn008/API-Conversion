# coding=utf-8
from __future__ import print_function
import json
from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-31',
    username='b0c787c9-5a0e-47a9-a558-cede8d8a501a',
    password='CYFEqCfPFe6w')

example_text ='Hola, cómo estás?'

print(json.dumps(language_translator.translate(example_text, source='es',target='en', indent=2)))
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