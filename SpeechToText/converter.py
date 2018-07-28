import_statement=''
credentials=''
print_text=''
open_file=''


with open("google_speech_to_text.py") as f:
    lines = f.readlines()
#	lines = [l for l in lines if "from google.cloud import texttospeech" in l]
    for a in lines:
    	if "import speech_recognition as sr" in a:
    		import_statement="from watson_developer_cloud import SpeechToTextV1"+"\n"+"from os.path import join, dirname"
    
    	if 'cred="AIzaSyCRptLxqzkiWw4JBwIefCcMuKDJaWGwadE"' in a:
    		credentials="cred= SpeechToTextV1(username='',password='')"
	
    	if 'with sr.AudioFile("output.wav") as source:' in a:
    		open_file="with open(join(dirname(__file__), 'output.wav'),'rb') as source:"

    	if "print(sr.Recognizer().recognize_google(sr.Recognizer().record(source), cred))" in a:
    		print_text="\tprint( (((cred.recognize(audio=source,content_type='audio/wav')['results'][0])['alternatives'])[0])['transcript'])"

    lines= import_statement + "\n"+credentials+"\n" +open_file+"\n"+print_text

    with open("converted_watson.py", "w") as f1:
        f1.writelines(lines)
