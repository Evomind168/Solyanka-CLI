from speedtest import Speedtest
import sys
import time


def progress_bar(progress, total, prefix=''):
    bar_length = 30
    filled_length = int(round(bar_length * progress / float(total)))
    percents = round(100.0 * progress / float(total), 1)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\r{prefix}[{bar}] {percents}%')
    sys.stdout.flush()


def run_speedtest():
    try:
        s = Speedtest()
        print("Тестування серверів...")
        s.get_best_server()

        print("\nТестування швидкості завантаження...")
        for i in range(100):
            progress_bar(i + 1, 100, 'Прогрес: ')
            time.sleep(0.02)
        download_speed = round(s.download() / (10 ** 6), 2)

        print("\n\nТестування швидкості відвантаження...")
        for i in range(100):
            progress_bar(i + 1, 100, 'Прогрес: ')
            time.sleep(0.02)
        upload_speed = round(s.upload() / (10 ** 6), 2)

        print("\n\nРезультати тестування:")
        print("=" * 50)
        print(f"Швидкість завантаження: {download_speed} Mbps")
        print(f"Швидкість відвантаження: {upload_speed} Mbps")
        print("=" * 50)
    except Exception as e:
        print(f"\nПомилка: {e}")