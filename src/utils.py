import os.path
from typing import Any

CYRRENT_DIR = os.path.dirname(__file__)


def open_html_file(file: str) -> Any:
    """Функция принимает HTML файл и возвращает считанные из него данные"""

    file_name = os.path.join(CYRRENT_DIR, '..', file)

    try:
        with open(file_name, 'r+') as f:
            data = f.read()
    except FileNotFoundError:
        return "Файл не найден"
    else:
        return data


if __name__ == '__main__':
    print(open_html_file('catalog.html'))
