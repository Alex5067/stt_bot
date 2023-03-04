import json
import subprocess
from datetime import datetime
from bert.bert import Bert_punctuation

from vosk import KaldiRecognizer, Model

class STT:
    def __init__(self):
        self.model_path = "models/vosk"
        self.sample_rate = 48000
        self.ffmpeg_path = "models/ffmpeg"
        model = Model(self.model_path)
        self.kaldi = KaldiRecognizer(model, self.sample_rate)
        self.kaldi.SetWords(True)

    def audio_to_text(self, audio_file = None):
        process = subprocess.Popen(
        [
         self.ffmpeg_path,
         "-loglevel", "quiet",
         "-i", audio_file,
         "-ar", str(self.sample_rate),
         "-ac", "1",
         "-f", "s16le",
         "-"
         ], stdout = subprocess.PIPE)

        while True:
            data = process.stdout.read(4000)
            if (len(data) == 0):
                break
            if self.kaldi.AcceptWaveform(data):
                pass
        result_json = self.kaldi.FinalResult()
        result_dict = json.loads(result_json)
        return [result_dict["text"]]

if __name__ == "__main__":
    # Распознование аудио
    start_time = datetime.now()
    stt = STT()
    Bert_punctuation = Bert_punctuation(model_file="Bert_Punctuation_ru/bert_punctuation.tar.gz",
                                        vocab_file="Bert_Punctuation_ru/vocab.txt")
    text = stt.audio_to_text("test-1.ogg")
    text_punctuation = Bert_punctuation.predict(text)
    print(text_punctuation)
    print("Время выполнения:", datetime.now() - start_time)


