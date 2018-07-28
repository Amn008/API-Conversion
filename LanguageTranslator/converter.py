# -*- coding: utf-8 -*- 
import_statement=''
credentials=''
input_text=''
function_call=''
encoding=''
input_lang=''

with open("Google_language_translator.py") as f:
    lines = f.readlines()

    for a in lines:

        if "# -*- coding: utf-8 -*- " in a:
            encoding="# -*- coding: utf-8 -*- "
    
    	if "from google.cloud import translate" in a:
    		import_statement="from __future__ import print_function"+"\n"+"from watson_developer_cloud import LanguageTranslatorV3"+"\n"+"import json"
    
    	if "os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/aman/Desktop/Final/LanguageTranslator/NewAgent-9c23594fa4f6.json" in a:
    		credentials="language_translator = LanguageTranslatorV3(version='2018-05-31',username='',password='')"

        if "example_text ='Hola, cómo estás?'" in a:
            input_text="example_text ='Hola, cómo estás?'"

        if "target_lang='en'" in a:
            input_lang="target_lang='en'"
	
    	if "    translate_client = translate.Client()" in a:
    		function_call="print(json.dumps(language_translator.translate(example_text, source='es',target=target_lang, indent=2)))"

    	

    lines= encoding+"\n"+import_statement + "\n"+credentials+"\n" +input_text+"\n"+input_lang+"\n"+function_call

    with open("converted_watson.py", "w") as f1:
        f1.writelines(lines)

    print "Google API has been converted into Watson Language Translator API ... Try it by running converted_watson.py file"
