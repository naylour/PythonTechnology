import sys
import os
import subprocess

def main():
    if len(sys.argv) != 3:
        print('Использование: uv run main.py lessonN taskK')
        return

    lesson = sys.argv[1] # lessonN
    task = sys.argv[2] # taskK

    file_path = os.path.join(lesson, f'{task}.py')

    if not os.path.exists(file_path):
        print(f'Файл \'{file_path}\' не найден!')
        return

    try:
        subprocess.run([sys.executable, file_path])
    except Exception as e:
        print(f'Ошибка при запуске {file_path}: {e}')
if __name__ == '__main__':
    main()
