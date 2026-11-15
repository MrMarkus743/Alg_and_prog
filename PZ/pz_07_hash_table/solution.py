import hashlib
import os
import secrets


# Задача 1: Безопасное сохранение элемента в словарь, если ключа еще нет
def safe_insert(hash_table, key, value):
    if key not in hash_table:
        hash_table[key] = value
        return True
    return False


# Вспомогательная функция вычисления хеша файла
def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


# Задача 2: Группировка файлов с одинаковым содержимым в директории
def group_duplicate_files(folder_path):
    hash_map = {}
    if not os.path.exists(folder_path):
        return {}

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            file_hash = get_file_hash(full_path)
            if file_hash not in hash_map:
                hash_map[file_hash] = []
            hash_map[file_hash].append(filename)

    duplicates = {h: files for h, files in hash_map.items() if len(files) > 1}
    return duplicates


# Задача 3: Проверка наличия дубликата файла в папке Директория_1
def find_duplicate_in_folder(target_file, search_folder):
    if not os.path.isfile(target_file) or not os.path.exists(search_folder):
        return None

    target_hash = get_file_hash(target_file)

    for filename in os.listdir(search_folder):
        candidate_path = os.path.join(search_folder, filename)
        if os.path.isfile(candidate_path) and get_file_hash(candidate_path) == target_hash:
            return filename

    return None


# Задача 4: Хеширование паролей со статической и динамической солью
STATIC_SALT = "university_static_salt_2026"


def hash_password_static(password):
    salted = password + STATIC_SALT
    return hashlib.sha256(salted.encode("utf-8")).hexdigest()


def hash_password_dynamic(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(8)
    salted = password + salt
    pwd_hash = hashlib.sha256(salted.encode("utf-8")).hexdigest()
    return pwd_hash, salt


# Задача 5: Регистрация и авторизация пользователей на хеш-таблице
class AuthSystem:
    def __init__(self):
        self.users = {}

    def register(self, login, password):
        if login in self.users:
            return False
        pwd_hash, salt = hash_password_dynamic(password)
        self.users[login] = {"hash": pwd_hash, "salt": salt}
        return True

    def login(self, login, password):
        if login not in self.users:
            return False
        stored_hash = self.users[login]["hash"]
        salt = self.users[login]["salt"]
        check_hash, _ = hash_password_dynamic(password, salt)
        return check_hash == stored_hash


# Задача 6: Собственная хеш-таблица на массиве с открытой адресацией
class CustomHashTable:
    DELETED = "<DELETED>"

    def __init__(self, size=20):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash_function(self, key):
        return len(key) % self.size

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = None

        for step in range(self.size):
            curr_idx = (idx + step) % self.size
            cell = self.table[curr_idx]

            if cell is None:
                target_idx = first_deleted if first_deleted is not None else curr_idx
                self.table[target_idx] = (key, value)
                self.count += 1
                return True

            if cell == self.DELETED:
                if first_deleted is None:
                    first_deleted = curr_idx
                continue

            if cell[0] == key:
                self.table[curr_idx] = (key, value)
                return True

        if first_deleted is not None:
            self.table[first_deleted] = (key, value)
            self.count += 1
            return True

        return False

    def remove(self, key):
        idx = self.hash_function(key)
        for step in range(self.size):
            curr_idx = (idx + step) % self.size
            cell = self.table[curr_idx]

            if cell is None:
                return False

            if cell != self.DELETED and cell[0] == key:
                self.table[curr_idx] = self.DELETED
                self.count -= 1
                return True
        return False

    def get_load_factor(self):
        return round(self.count / self.size, 2)


if __name__ == "__main__":
    test_dict = {"Студент 1": 4, "Студент 2": 5}
    print("Задача 1: Вставка нового ключа:", safe_insert(test_dict, "Студент 3", 5))
    print("Задача 1: Повторная вставка ключа:", safe_insert(test_dict, "Студент 1", 3))

    folder_demo = "Директория_1"
    os.makedirs(folder_demo, exist_ok=True)
    with open(os.path.join(folder_demo, "file1.txt"), "w", encoding="utf-8") as f:
        f.write("Тестовый контент 1")
    with open(os.path.join(folder_demo, "file1_copy.txt"), "w", encoding="utf-8") as f:
        f.write("Тестовый контент 1")
    with open(os.path.join(folder_demo, "file2.txt"), "w", encoding="utf-8") as f:
        f.write("Другой контент")

    print("\nЗадача 2 (Дубликаты в папке):", group_duplicate_files(folder_demo))

    external_file = "check_copy.txt"
    with open(external_file, "w", encoding="utf-8") as f:
        f.write("Тестовый контент 1")
    dup_name = find_duplicate_in_folder(external_file, folder_demo)
    print(f"Задача 3: Дубликат файла '{external_file}' в '{folder_demo}': {dup_name}")
    if os.path.exists(external_file):
        os.remove(external_file)

    pwd = "StudentPassword2026"
    st_hash = hash_password_static(pwd)
    dyn_hash, salt_val = hash_password_dynamic(pwd)
    print(f"\nЗадача 4 (Статический хеш): {st_hash[:16]}...")
    print(f"Задача 4 (Динамический хеш): {dyn_hash[:16]}... | Соль: {salt_val}")

    auth = AuthSystem()
    sample_users = [
        ("user1", "Pass1"),
        ("user2", "Pass2"),
        ("user3", "Pass3"),
        ("user4", "Pass4"),
        ("user5", "Pass5"),
    ]
    for u, p in sample_users:
        auth.register(u, p)

    print("\nЗадача 5: Проверка входа user1 с верным паролем:", auth.login("user1", "Pass1"))
    print("Задача 5: Проверка входа user1 с неверным паролем:", auth.login("user1", "Wrong"))

    ht = CustomHashTable(size=20)
    items = [
        ("Водоросли", 280),
        ("Картофель", 260),
        ("Лук-порей", 59),
        ("Манго", 291),
        ("Орехи грецкие", 266),
        ("Салями", 225),
        ("Специи", 283),
        ("Сыр сливочный", 152),
        ("Творог", 215),
        ("Тофу", 142),
        ("Хек", 248),
        ("Чай черный", 118),
        ("Чернила каракатицы", 95),
        ("Шампиньоны", 101),
        ("Финик", 104),
    ]

    for k, v in items:
        ht.insert(k, v)

    print(f"\nЗадача 6а: Заполнено {len(items)} элементов. Load Factor = {ht.get_load_factor()}")

    to_delete = ["Орехи грецкие", "Водоросли", "Специи", "Манго"]
    for k in to_delete:
        ht.remove(k)

    print(f"Задача 6б: После удаления 4 элементов. Load Factor = {ht.get_load_factor()}")