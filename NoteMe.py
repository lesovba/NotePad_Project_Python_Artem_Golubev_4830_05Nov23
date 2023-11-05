import os
import json
from datetime import datetime

# Конструктор класса NotesManager.
# Инициализирует атрибуты объекта, такие как notes_file (имя файла для хранения заметок)
# и notes (список заметок, загружаемый из файла или создаваемый пустым).
class NotesManager:
    def __init__(self):
        self.notes_file = "notes.json"
        self.notes = self.load_notes()

    # Метод load_notes загружает список заметок из файла
    # notes.json, если файл существует.
    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as file:
                try:
                    notes = json.load(file)
                    return notes
                except json.JSONDecodeError:
                    print("Ошибка при чтении файла заметок. Создан новый файл.")
        return []

    # Метод save_notes сохраняет текущий список заметок в файл notes.json.
    def save_notes(self):
        with open(self.notes_file, "w") as file:
            json.dump(self.notes, file, indent=2)

    # Метод create_note создает новую заметку с заданным заголовком и содержимым.
    # Также добавляет заметку в список и сохраняет обновленный список в файле.
    def create_note(self, title, content, date=None):
        if date is None:
            date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        note = {"title": title, "content": content, "date": date}
        self.notes.append(note)
        self.save_notes()
        print(f"Заметка '{title}' создана.")

    # Метод list_notes выводит список всех заметок, если они существуют.
    def list_notes(self):
        if not self.notes:
            print("Список заметок пуст.")
        else:
            print("Список заметок:")
            for idx, note in enumerate(self.notes, 1):
                print(f"{idx}. {note['title']} ({note['date']})")

    # Метод view_note_by_date выводит заметки по дате
    def view_note_by_date(self, date):
        filtered_notes = [note for note in self.notes if note["date"].startswith(date)]
        if filtered_notes:
            print(f"Заметки за {date}:")
            for idx, note in enumerate(filtered_notes, 1):
                print(f"{idx}. {note['title']} ({note['date']})")
        else:
            print(f"Нет заметок за {date}.")

    # Метод view_note для просмотра заметки
    def view_note(self, index):
        if 1 <= index <= len(self.notes):
            note = self.notes[index - 1]
            print(f"\n{note['title']} ({note['date']})\n{note['content']}")
        else:
            print("Неверный индекс заметки.")

    # Метод edit_note для редактирования заметки
    def edit_note(self, index, new_title, new_content):
        if 1 <= index <= len(self.notes):
            self.notes[index - 1]["title"] = new_title
            self.notes[index - 1]["content"] = new_content
            self.save_notes()
            print(f"Заметка {index} отредактирована.")
        else:
            print("Неверный индекс заметки.")

    # Метод delete_note для удаления заметки
    def delete_note(self, index):
        if 1 <= index <= len(self.notes):
            deleted_note = self.notes.pop(index - 1)
            self.save_notes()
            print(f"Заметка '{deleted_note['title']}' удалена.")
        else:
            print("Неверный индекс заметки.")

# В методе main реализовал главное меню консольного приложения
def main():
    notes_manager = NotesManager()

    while True:
        print("\n1. Создать заметку")
        print("2. Список заметок")
        print("3. Просмотреть заметку по дате")
        print("4. Просмотреть заметку")
        print("5. Редактировать заметку")
        print("6. Удалить заметку")
        print("7. Выход")

        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            content = input("Введите текст заметки: ")
            notes_manager.create_note(title, content)
        elif choice == "2":
            notes_manager.list_notes()
        elif choice == "3":
            date = input("Введите дату (гггг-мм-дд): ")
            notes_manager.view_note_by_date(date)
        elif choice == "4":
            notes_manager.list_notes()
            index = int(input("Введите номер заметки для просмотра: "))
            notes_manager.view_note(index)
        elif choice == "5":
            notes_manager.list_notes()
            index = int(input("Введите номер заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_content = input("Введите новый текст заметки: ")
            notes_manager.edit_note(index, new_title, new_content)
        elif choice == "6":
            notes_manager.list_notes()
            index = int(input("Введите номер заметки для удаления: "))
            notes_manager.delete_note(index)
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 7.")

# Запуск приложения реализовал через условие, проверяющее,
# что скрипт запускается напрямую, а не импортируется как модуль.
if __name__ == "__main__":
    main()
