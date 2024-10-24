import os
import time

from modules.speedtest_module import run_speedtest
from modules.yt_saver_module import download_youtube

# Constants
MAIN_MENU_OPTIONS = ["Youtube Downloader", "Speedtest", "Вихід"]
YOUTUBE_QUALITY_OPTIONS = ["1080p", "720p", "480p", "Тільки аудіо"]
YOUTUBE_MENU_OPTIONS = ["Повернутись в головне меню"]

def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu(title, options):
    """Prints a menu with a title and options"""
    print("=" * 50)
    print(f"           {title}")
    print("=" * 50)
    for i, option in enumerate(options, start=1):
        print(f"[{i}] {option}")
    print("=" * 50)

def print_main_menu():
    """Prints the main menu"""
    print_menu("ГОЛОВНЕ МЕНЮ", MAIN_MENU_OPTIONS)

def print_youtube_menu():
    """Prints the YouTube menu"""
    print_menu("YOUTUBE DOWNLOADER", YOUTUBE_QUALITY_OPTIONS + YOUTUBE_MENU_OPTIONS)

def get_user_choice(options):
    """Gets the user's choice from a list of options"""
    while True:
        choice = input("\nВиберіть опцію (1-{}): ".format(len(options))).strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print("\nНеправильний вибір!")
        time.sleep(1.5)

def youtube_downloader():
    """YouTube downloader function"""
    while True:
        clear_screen()
        print_youtube_menu()
        choice = get_user_choice(YOUTUBE_QUALITY_OPTIONS + YOUTUBE_MENU_OPTIONS)
        if choice == len(YOUTUBE_QUALITY_OPTIONS) + 1:
            return
        quality = YOUTUBE_QUALITY_OPTIONS[choice - 1]
        url = input("Введіть URL відео: ").strip()
        if not url:
            print("\nURL не може бути порожнім!")
            time.sleep(1.5)
            continue
        output_path = input("\nШлях для збереження (Enter для поточної папки): ").strip()
        if not output_path:
            output_path = os.getcwd()
        clear_screen()
        print_menu("YOUTUBE DOWNLOADER", [])
        print("\nПочинаємо завантаження...\n")
        download_youtube(url, quality, output_path)
        print("\n" + "=" * 50)
        print("\n[1] Завантажити ще одне відео")
        print("[2] Повернутись в головне меню")
        next_action = get_user_choice([1, 2])
        if next_action != 1:
            return

def speedtest():
    """Speedtest function"""
    clear_screen()
    print_menu("SPEEDTEST", [])
    run_speedtest()
    print("\n" + "=" * 50)
    print("\n[1] Провести ще один тест")
    print("[2] Повернутись в головне меню")
    next_action = get_user_choice([1, 2])
    if next_action == 1:
        speedtest()

def main():
    """Main function"""
    while True:
        clear_screen()
        print_main_menu()
        choice = get_user_choice(MAIN_MENU_OPTIONS)
        if choice == 1:
            youtube_downloader()
        elif choice == 2:
            speedtest()
        elif choice == 3:
            clear_screen()
            print("Дякуємо за використання програми!")
            time.sleep(1.5)
            clear_screen()
            break

if __name__ == '__main__':
    main()
