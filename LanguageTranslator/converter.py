'''
with open('google_text_input_speech.py', 'r') as file :
  filedata = file.read()

# Replace the target string
if filedata == "from google.cloud import texttospeech":
	print "1"
	filedata = filedata.replace('from google.cloud import texttospeech', 'from tts_watson.TtsWatson import TtsWatson')
filedata = filedata.replace("os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/aman/Desktop/DJANGO-API-IMPLEMENT-37d0007f53c4.json'","ttsWatson = TtsWatson('5b8523f8-4396-41a2-b3d6-704bf47567cb', 'u0H6TzFeo3kz', 'en-US_AllisonVoice') ")

# Write the file out again
with open('file.py', 'w') as file:
  file.write(filedata)


f = open('google_text_input_speech.py','r')
f1 = open('file.py', 'w')

#doIHaveToCopyTheLine=False

for line in f.readlines():
    if 'from google.cloud import texttospeech' in line:
    	line.replace('from google.cloud import texttospeech', 'from tts_watson.TtsWatson import TtsWatson')
    #    doIHaveToCopyTheLine=True

    else:
    	f1.write("fuck")
    #if doIHaveToCopyTheLine:
     #   f1.write(line)

f1.close()
f.close()
'''
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
    		credentials="ttsWatson = TtsWatson('5b8523f8-4396-41a2-b3d6-704bf47567cb', 'u0H6TzFeo3kz', 'en-US_AllisonVoice') "
	
    	if "client = texttospeech.TextToSpeechClient()" in a:
    		function_call="a=ttsWatson.play(texttospeak)"

    	if "texttospeak='Aman Dalal'" in a:
    		input_text="texttospeak='Aman Dalal'"

    lines= import_statement + "\n"+credentials+"\n" +input_text+"\n"+function_call

    with open("converted_watson.py", "w") as f1:
        f1.writelines(lines)