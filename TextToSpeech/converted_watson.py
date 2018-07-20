from tts_watson.TtsWatson import TtsWatson
ttsWatson = TtsWatson('5b8523f8-4396-41a2-b3d6-704bf47567cb', 'u0H6TzFeo3kz', 'en-US_AllisonVoice') 
texttospeak='Aman Dalal'
a=ttsWatson.play(texttospeak)