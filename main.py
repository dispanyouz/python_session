import os
import logging

class FileManager:
    def __init__(self, directory_path, log_file='file_manager.log'):
        self.directory_path = directory_path
        self.log_file = log_file

        # Инициализация логгера
        logging.basicConfig(filename=self.log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def _log(self, message, level=logging.INFO):
        logging.log(level, message)

    def list_files(self):
        try:
            # Получение списка файлов в указанной директории
            files = os.listdir(self.directory_path)
            self._log(f"Listing files in {self.directory_path}: {files}")
            return files
        except OSError as e:
            # Обработка ошибок, если директория не найдена или доступ к ней запрещен
            self._log(f"Error listing files: {e}", level=logging.ERROR)
            return []

    def create_file(self, file_name):
        file_path = os.path.join(self.directory_path, file_name)
        try:
            # Создание нового файла
            with open(file_path, 'w') as file:
                self._log(f"File created: {file_path}")
            return True
        except IOError as e:
            # Обработка ошибок при создании файла
            self._log(f"Error creating file {file_path}: {e}", level=logging.ERROR)
            return False

    def delete_file(self, file_name):
        file_path = os.path.join(self.directory_path, file_name)
        try:
            # Удаление файла
            os.remove(file_path)
            self._log(f"File deleted: {file_path}")
            return True
        except FileNotFoundError:
            # Обработка ошибки, если файл не найден
            self._log(f"File not found: {file_path}", level=logging.ERROR)
            return False
        except Exception as e:
            # Обработка других ошибок при удалении файла
            self._log(f"Error deleting file {file_path}: {e}", level=logging.ERROR)
            return False

    def edit_file(self, file_name):
        file_path = os.path.join(self.directory_path, file_name)
        try:
            # Редактирование файла
            with open(file_path, 'a') as file:
                content = input("Введите новое содержимое файла (для завершения введите Ctrl + D): ")
                file.write(content)
            self._log(f"File edited: {file_path}")
            return True
        except FileNotFoundError:
            # Обработка ошибки, если файл не найден
            self._log(f"File not found: {file_path}", level=logging.ERROR)
            return False
        except Exception as e:
            # Обработка других ошибок при редактировании файла
            self._log(f"Error editing file {file_path}: {e}", level=logging.ERROR)
            return False

    def view_file(self, file_name):
        file_path = os.path.join(self.directory_path, file_name)
        try:
            # Просмотр содержимого файла
            with open(file_path, 'r') as file:
                content = file.read()
                print(f"Content of file {file_name}:\n\n{content}\n\n")
            self._log(f"File viewed: {file_path}")
            return True
        except FileNotFoundError:
            # Обработка ошибки, если файл не найден
            self._log(f"File not found: {file_path}", level=logging.ERROR)
            return False
        except Exception as e:
            # Обработка других ошибок при просмотре файла
            self._log(f"Error viewing file {file_path}: {e}", level=logging.ERROR)
            return False

# Функция для вывода меню
def print_menu():
    print("1. Список файлов")
    print("2. Создать файл")
    print("3. Редактировать файл")
    print("4. Просмотреть файл")
    print("5. Удалить файл")
    print("0. Выйти")

# Пример использования
if __name__ == "__main__":
    directory_path = 'C:\Python test dir'
    file_manager = FileManager(directory_path)

    while True:
        print_menu()
        choice = input("Выберите действие (введите номер): ")

        if choice == '1':
            files = file_manager.list_files()
            print("Files in directory:", files)
        elif choice == '2':
            new_file_name = input("Введите имя нового файла: ")
            if file_manager.create_file(new_file_name):
                print(f"File {new_file_name} created successfully")
        elif choice == '3':
            file_to_edit = input("Введите имя файла для редактирования: ")
            if file_manager.edit_file(file_to_edit):
                print(f"File {file_to_edit} edited successfully")
        elif choice == '4':
            file_to_view = input("Введите имя файла для просмотра: ")
            if file_manager.view_file(file_to_view):
                print(f"File {file_to_view} viewed successfully")
        elif choice == '5':
            file_to_delete = input("Введите имя файла для удаления: ")
            if file_manager.delete_file(file_to_delete):
                print(f"File {file_to_delete} deleted successfully")
        elif choice == '0':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите правильный номер.")
