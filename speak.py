from TTS.api import TTS
import torch
class Ai_speaker(TTS):
    def __init__(self):
        super().__init__()
        
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.location = "./output.wav"
    def speak(self,text="A journey to the west is mostly wanted"):
        tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)

        tts.tts_to_file(text=text,file_path=self.location,language="en",speaker='Wulf Carlevaro')
        return self.location
        
