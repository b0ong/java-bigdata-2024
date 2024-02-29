# file: p46_tts.py
# desc: Text to Speech

#pip install gTTS


from gtts import gTTS
text = input('소리로 바굴 텍스트 입력 > ')

speech = gTTS(text=text, lang='ko')
speech.save('./day07/tts.mp3')
