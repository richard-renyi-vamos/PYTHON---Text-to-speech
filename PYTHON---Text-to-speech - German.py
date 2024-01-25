from gtts import gTTS
import os

# Text you want to read aloud
text = "Hallo, wie geht es dir heute?"

# Create a gTTS object
tts = gTTS(text=text, lang='de')

# Save the speech to an mp3 file
tts.save("speech.mp3")

# Play the speech
os.system("mpg321 speech.mp3")
