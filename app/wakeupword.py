import numpy as np

import sounddevice as sd
from openwakeword.model import Model

class WakeWordDectector:
    def __init__(self):
        self.model = Model(
             wakeword_models=["hey_jarvis"],  
    inference_framework="onnx"
        )
        self.sample_rate = 16000
        self.chunk_size = 1280
        self.threshold = 0.6
    def listen(self):
        self.model.reset()
        print("Listening for wake word...")

        with sd.InputStream(channels=1, samplerate=self.sample_rate, blocksize=self.chunk_size,dtype='int16') as stream:
            while True:
                audio_data,overflow = stream.read(self.chunk_size)
                audio_data = audio_data.flatten()
                prediction = self.model.predict(audio_data)
                for wakeword, score in prediction.items():
                    
                    if score > self.threshold:
                        
                        return True