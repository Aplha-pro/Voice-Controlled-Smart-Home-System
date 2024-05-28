import playsound
from gtts import gTTS

text = "Hello GPT"
sound = gTTS(text, lang='en')
#sound.save('testing.mp3')
playsound.playsound('testing.mp3')
