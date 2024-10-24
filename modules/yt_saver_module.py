from pytube import YouTube
import sys


def progress_bar(progress, total, prefix=''):
    bar_length = 30
    filled_length = int(round(bar_length * progress / float(total)))
    percents = round(100.0 * progress / float(total), 1)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\r{prefix}[{bar}] {percents}%')
    sys.stdout.flush()


def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress_bar(bytes_downloaded, total_size, 'Завантаження: ')


def download_youtube(url, quality="720p", output_path=None):
    try:
        yt = YouTube(url, on_progress_callback=progress_callback)
        print(f"Назва відео: {yt.title}")
        print(f"Автор: {yt.author}")
        print(f"Тривалість: {yt.length} секунд")
        print("-" * 50)

        if quality == "audio":
            stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.filter(res=quality, mime_type="video/mp4").first()
            if not stream:
                print(f"\nЯкість {quality} недоступна. Використовуємо найкращу доступну якість...")
                stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

        if not stream:
            print("\nПомилка: Не вдалося знайти відповідний потік для завантаження")
            return

        print(f"\nПочинаємо завантаження...")
        stream.download(output_path=output_path)
        print("\nЗавантаження завершено успішно!")

    except Exception as e:
        print(f"\nПомилка: {str(e)}")
