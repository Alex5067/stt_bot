from aiogram import Bot, Dispatcher, executor, types
import os
from pathlib import Path
import logging
from stt import STT
from bert.bert import Bert_punctuation

API_TOKEN = "YOUR_TOKEN"

logging.basicConfig(level = logging.INFO)
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)
stt = STT()
Bert_punctuation = Bert_punctuation(model_file="bert/bert_punctuation.tar.gz",
                                        vocab_file="bert/vocab.txt")

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nОтправь аудиосообщение,\nчтобы получить текст.")

@dp.message_handler(content_types = [types.ContentType.VOICE, types.ContentType.AUDIO, types.ContentType.DOCUMENT])
async def audio_handler(message: types.Message):
    if message.content_type == types.ContentType.VOICE:
        file_id = message.voice.file_id
    elif message.content_type == types.ContentType.AUDIO:
        file_id = message.audio.file_id
    elif message.content_type == types.ContentType.DOCUMENT:
        file_id = message.document.file_id
    else:
        await message.reply("Неправильный формат документа")
        return
    file = await bot.get_file(file_id)
    f_path = file.file_path
    f_disk = Path("", f"{file_id}.tmp")
    await bot.download_file(f_path, destination = f_disk)
    await message.reply("Получено")
    text = stt.audio_to_text(f_disk)
    text_punctuation = Bert_punctuation.predict(text)
    elem_text = ' '.join(text_punctuation)
    elem_text = elem_text.capitalize()
    elem_text += '.'
    if not text_punctuation:
        await message.reply("Формат не поддерживается")
    await message.answer(elem_text)
    os.remove(f_disk)
    await message.reply("Done")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)