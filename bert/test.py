from bert_punctuation import Bert_punctuation

Bert_punctuation = Bert_punctuation()

sents = ["она переключила внимание на развивающийся прогулочный рынок состоящий \
          из семей с независимым доходом", "думаю что поскольку теперь семьи \
          живут не так близко как прежде"]
sents_punctuation = Bert_punctuation.predict(sents)
print(sents_punctuation)
