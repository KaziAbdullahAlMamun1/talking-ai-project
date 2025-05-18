from faster_whisper import WhisperModel


class Transcriber(WhisperModel):
    def __init__(self,model_size="medium"):
        super().__init__(model_size)
        
        self.model = WhisperModel(model_size,device="cpu",compute_type="float32")
    def transcribe(self,file_name="audio.mp3"):
        segments, info = self.model.transcribe(file_name, beam_size=5,language="en")
        with open("transcribe.txt","w") as file:
            for segment in segments:
                file.write(f"{segment.text}.")
                print(f"{segment.text}.")