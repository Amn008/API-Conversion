import_statement=''
credentials=''
input_text=''
function_call=''


with open("google_text_input_speech.py") as f:
    lines = f.readlines()
#	lines = [l for l in lines if "from google.cloud import texttospeech" in l]
    for a in lines:
    	if "from google.cloud import texttospeech" in a:
    		import_statement="from tts_watson.TtsWatson import TtsWatson"
    
    	if "os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/aman/Desktop/Final/TextToSpeech/DJANGO-API-IMPLEMENT-37d0007f53c4.json'" in a:
    		credentials="ttsWatson = TtsWatson('', '', 'en-US_AllisonVoice') "
	
    	if "client = texttospeech.TextToSpeechClient()" in a:
    		function_call="a=ttsWatson.play(texttospeak)"

    	if "texttospeak='Aman Dalal'" in a:
    		input_text="texttospeak='Aman Dalal'"

    lines= import_statement + "\n"+credentials+"\n" +input_text+"\n"+function_call

    with open("converted_watson.py", "w") as f1:
        f1.writelines(lines)
