from watson_developer_cloud import VisualRecognitionV3, WatsonApiException
from os.path import join, dirname
import json
visual_recognition = VisualRecognitionV3(version='2018-03-19',iam_api_key='')
path = join(dirname(__file__), 'banana1.jpeg')
with open(path, 'rb') as image_file:
	face_result = visual_recognition.classify(images_file=image_file)
	print(json.dumps(face_result, indent=2))
