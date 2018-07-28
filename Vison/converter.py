import_statement=''
credentials=''
print_text=''
open_file=''
input_image=''
fun_call=''

with open("Google_visual.py") as f:
    lines = f.readlines()
#	lines = [l for l in lines if "from google.cloud import texttospeech" in l]
    for a in lines:
    	if "from google.cloud import vision" in a:
    		import_statement="from watson_developer_cloud import VisualRecognitionV3, WatsonApiException"+"\n"+"from os.path import join, dirname"+"\n"+"import json"

    
    	if "os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/aman/Desktop/Final/Vison/NewAgent-880fdb455b33.json'" in a:
    		credentials="visual_recognition = VisualRecognitionV3(version='2018-03-19',iam_api_key='')"
	
    	if "detect_labels('banana.jpeg')" in a:
    		input_image="path = join(dirname(__file__), 'banana1.jpeg')"

        if "    with io.open(path, 'rb') as image_file:" in a:
            open_file="with open(path, 'rb') as image_file:"

        if '    image = types.Image(content=content)' in a:
            fun_call="\tface_result = visual_recognition.classify(images_file=image_file)"

    	if "    print('Labels:')" in a:
    		print_text="\tprint(json.dumps(face_result, indent=2))"

    lines= import_statement + "\n"+credentials+"\n"+input_image+"\n"+open_file+"\n"+fun_call+"\n"+print_text

    with open("converted_watson.py", "w") as f1:
        f1.writelines(lines)
