# -*- coding: utf-8 -*- 
from __future__ import print_function
from watson_developer_cloud import LanguageTranslatorV3
import json
language_translator = LanguageTranslatorV3(version='2018-05-31',username='b0c787c9-5a0e-47a9-a558-cede8d8a501a',password='CYFEqCfPFe6w')
example_text ='Hola, cómo estás?'
target_lang='en'
print(json.dumps(language_translator.translate(example_text, source='es',target=target_lang, indent=2)))