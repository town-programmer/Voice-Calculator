import speech_recognition as sr
import pyttsx3

class voice_command:
    listener = sr.Recognizer() # initialising recognizer

    engine = pyttsx3.init() # initializing text to speech

    voices = engine.getProperty('voices') # getting all voices
    engine.setProperty('voice',voices[1].id)

    def talk(self, text):
        self.text = text
        self.engine.say(text)
        self.engine.runAndWait()
    
    def take_command(self):
        my_mic = sr.Microphone(device_index=1)
        with my_mic as source:
            print('Listening...')
            self.talk('Listening')
            #self.listener.adjust_for_ambient_noise(source)
            self.voice = self.listener.listen(source)
        self.command = self.listener.recognize_google(self.voice)
        self.command = self.command.lower()
        self.talk(self.command)
        return self.command

    def run_command(self):
        self.command = self.take_command()
        if self.command == 'repeat':
            self.take_command()