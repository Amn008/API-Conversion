import_statement1=''
import_statement2=''
import_statement3=''
credentials=''
input_text=''
functionprint_statement_call=''
print_statement=''

with open("GoogleNLP.py") as f:
    lines = f.readlines()

    for a in lines:

    	if "import os" in a:
    		import_statement1="from __future__ import print_function"+"\n"+"import json"
    
        if "from google.cloud import language" in a:
            import_statement2="from watson_developer_cloud import NaturalLanguageUnderstandingV1"
        
        if "from google.cloud.language import enums,types" in a:
            import_statement3="from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions"
    
    	if "os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/aman/Desktop/Final/NLP/NewAgent-24b28450e41c.json'" in a:
    		credentials="natural_language_understanding = NaturalLanguageUnderstandingV1(version='2017-02-27',username='ad1af379-1947-47bd-8ddd-63046e9deefb',password='X5HxOGCwU64N')"

        if "text = 'Bruce Banner is the Hulk and Bruce Wayne is BATMAN!.Superman fears not Banner, but Wayne.'" in a:
            input_text="input_text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne.'"

        if "entities = language_analysis(text)" in a:
            function_call="response = natural_language_understanding.analyze(text=input_text,features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions()))"
	
    	if "        print(('name', e.name), ('type', entity_type[e.type]))" in a:
    		print_statement="print(json.dumps(response, indent=2))"

    	

    lines= import_statement1+"\n"+import_statement2 + "\n"+import_statement3 + "\n"+credentials+"\n" +input_text+"\n"+function_call+"\n"+print_statement

    with open("converted_watson.py", "w") as f1:
        f1.writelines(lines)

    print "Google API has been converted into WatsonAPI ... Try it by running converted_watson.py file"