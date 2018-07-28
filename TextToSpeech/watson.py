from tts_watson.TtsWatson import TtsWatson

ttsWatson = TtsWatson('', '', 'en-US_AllisonVoice') 
texttospeak="Aman Dalal"
a=ttsWatson.play(texttospeak)
