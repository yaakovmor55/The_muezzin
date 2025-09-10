from faster_whisper import WhisperModel

class AudioTranscriber:
    def __init__(self, model_size="tiny"):
        self.model = WhisperModel(model_size)

    def transcribe(self, file_path):
        segments, info = self.model.transcribe(file_path)
        text= " "
        for segment in segments:
            text += segment.text
        return text.strip()

