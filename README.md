### Описание
Telegram-бот с распознаванием голосовых сообщений и восстановлением пунктуации.

### Технологии
aiogram, bert, vosk, ffmpeg

### Алгоритм работы
Кидаем боту аудио или голосовое сообщение, аудио конвертируется в текст с помощью Vosk, этот текст подаём в модель Bert, чтобы восстановить пунктуацию, получаем текст.

### Команды
- /start - Приветствие, появляется при первом старте бота
- /help - Повторяет сообщение при первом старте бота

### Запуск проекта

Клонируйте репозиторий и перейдите в него в командной строке

Укажите токен вашего бота в bot.py.

Скачайте модели и поместите в необходимые папки. Где взять модели описано ниже.

После скачивания моделей запустите код bot.py в Python.

### Модель Vosk, веса Bert, а также FFmpeg

*Vosk*
Модель доступна на сайте [проекта](https://alphacephei.com/vosk/models "Vosk - оффлайн-распознавание аудио"). Скачайте модель, разархивируйте и поместите папку model с файлами в папку models/vosk
- [vosk-model-ru-0.22       - 1.5 Гб](https://alphacephei.com/vosk/models/vosk-model-ru-0.22.zip "Модель vosk-model-ru-0.22 - 1.5 Гб") - лучше распознает, но дольше и весит много.
- [vosk-model-small-ru-0.22 - 45 Мб](https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip "Модель vosk-model-small-ru-0.22 - 45 Мб") - хуже распознает, но быстрее и весит мало.

*FFmpeg*
Скачайте набор exe файлов с сайта [проекта](https://ffmpeg.org/download.html "FFmpeg - набор open-source библиотек для конвертирования аудио- и видео в различных форматах.") и поместите файл ffmpeg.exe в папку models/vosk

*Bert*
Скачайте веса [BERT](https://drive.google.com/file/d/190dLqhRjqgNJLKBqz0OxQ3TzxSm5Qbfx/view?usp=sharing) и поместите архив в папку bert/
