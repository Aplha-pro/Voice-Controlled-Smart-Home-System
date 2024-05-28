# Modules to Use
### TTS Modules:
* eSpeak
* pyttsx3
* gTTS (Google Text-to-Speech)
* TTS from the transformers library (using suno/bark)
* Festival (another open-source TTS)

### STT Modules:
* SpeechRecognition (using Google Web Speech API)
* Vosk
* DeepSpeech
* Wit.ai
* Mozilla DeepSpeech

 
Best Modules are:- 
* GTTS (Text-to-Speech) *by Google*
* SpeechRecognition (Speech-to-text) *by Google*  
We are using `SpeechRecognition` for STT and `pyttsx3` for TTS
  
``pip install gtts SpeechRecognition pyaudio``

pyaudio plays a crucial role in enabling both `gtts` and `SpeechRecognition` to function properly:

* Why pyaudio? Both text-to-speech and speech-to-text functionalities involve audio. `pyaudio acts as a bridge between Python and your computer's audio hardware`.
* What does pyaudio do? It provides Python with the ability to:
* Play audio: This is necessary for gtts to generate audible speech from the text you provide.
* Record audio: This is essential for SpeechRecognition to capture spoken audio from your microphone and convert it to text.

In simpler terms, `pyaudio acts as the audio driver for these libraries`, allowing them to interact with your `sound card` and `microphone`. 
Without it, gtts wouldn't be able to produce speech, and SpeechRecognition wouldn't be able to record audio for processing.

* playsound: This is a higher-level, third-party Python module designed specifically for playing audio files with a simple API. It often works behind the scenes by leveraging the capabilities of your system's audio libraries or other underlying modules like pyaudio.
* pyaudio: This is a lower-level Python library that provides a more direct interface for working with audio on various operating systems. It offers functionalities for both playing and recording audio but requires more code and configuration compared to playsound.
