import os
from google.cloud import language
from google.cloud.language import enums,types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/aman/Desktop/Final/NLP/NewAgent-24b28450e41c.json'

def language_analysis(text):
        client = language.LanguageServiceClient()
        document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

        #sent_analysis = client.analyze_sentiment(document=document).document_sentiment
       # print(dir(sent_analysis))
        entities = client.analyze_entities(document).entities
        #return sent_analysis, entities
        return entities


text = 'Bruce Banner is the Hulk and Bruce Wayne is BATMAN!.Superman fears not Banner, but Wayne.'

#sentiment, entities = language_analysis(text)
entities = language_analysis(text)
print('Text: {}'.format(text))
#print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION', 'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

for e in entities:
        #print(('name', e.name), ('type', entity_type[e.type]), ('metadata', e.metadata), ('salience', e.salience), ('wiki-page', e.metadata.get('wikipedia_url', '-')))		
        print(('name', e.name), ('type', entity_type[e.type]))