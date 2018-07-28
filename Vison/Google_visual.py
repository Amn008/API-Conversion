# label detection only
import  io
from google.cloud import vision
from google.cloud.vision import types
import os

# import googleapiclient.discovery
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/aman/Desktop/Final/Vison/NewAgent-880fdb455b33.json'
def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)
detect_labels('banana.jpeg')