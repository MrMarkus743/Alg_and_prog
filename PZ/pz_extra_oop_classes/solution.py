# Задача 1: Иерархия пользователей образовательной платформы
class User:
    _user_counter = 1
    _existing_logins = set()

    def __init__(self, login, password):
        self._validate_login(login)
        self._validate_password(password)

        self.user_id = self._generate_id()
        self.user_type = self.__class__.__name__
        self._login = login
        self._password = password

        User._existing_logins.add(login)

    @classmethod
    def _generate_id(cls):
        uid = f"U{cls._user_counter:03d}"
        cls._user_counter += 1
        return uid

    @classmethod
    def _validate_login(cls, login):
        if login in cls._existing_logins:
            raise ValueError(f"Логин '{login}' уже занят!")

    @staticmethod
    def _validate_password(password):
        if len(password) < 7:
            raise ValueError("Пароль должен быть не короче 7 символов!")
        has_digit = any(c.isdigit() for c in password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        if not (has_digit and has_lower and has_upper):
            raise ValueError("Пароль должен содержать цифры, строчные и заглавные буквы!")

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        if new_login != self._login:
            self._validate_login(new_login)
            User._existing_logins.remove(self._login)
            User._existing_logins.add(new_login)
            self._login = new_login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._validate_password(new_password)
        self._password = new_password

    def show_info(self):
        print(f"[{self.user_type}] ID: {self.user_id} | Логин: {self._login} | Пароль: {self._password}")


class Student(User):
    _student_counter = 1

    def __init__(self, login, password, name, course):
        super().__init__(login, password)
        self.user_id = f"S{Student._student_counter:03d}"
        Student._student_counter += 1
        self.name = name
        self.course = course

    def show_info(self):
        print(f"[{self.user_type}] ID: {self.user_id} | Имя: {self.name} | Курс: {self.course} | Логин: {self._login}")


class Teacher(User):
    _teacher_counter = 1

    def __init__(self, login, password, name, experience):
        super().__init__(login, password)
        self.user_id = f"T{Teacher._teacher_counter:03d}"
        Teacher._teacher_counter += 1
        self.name = name
        self.experience = experience
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Преподаватель {self.name} добавил студента {student.name}")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Преподаватель {self.name} удалил студента {student.name}")

    def show_info(self):
        print(f"[{self.user_type}] ID: {self.user_id} | Имя: {self.name} | Стаж: {self.experience} лет | Студентов: {len(self.students)}")


# Задача 2: Класс-обертка MyList
class MyList(list):
    def print_info(self):
        print(f"Данный список содержит {len(self)} элемента(ов)")

    def drop_value(self, value):
        while value in self:
            self.remove(value)
        return self

    def add_indeces(self):
        new_items = []
        for i, val in enumerate(self):
            new_items.append(f"id-{i}")
            new_items.append(val)
        self.clear()
        self.extend(new_items)
        return self

    def append(self, value):
        next_idx = len(self) // 2
        super().append(f"id-{next_idx}")
        super().append(value)


# Задача 3: Симуляция «Пекарня»
class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class Manager:
    def __init__(self, name):
        self.name = name

    def inspect_bakery(self, revenue, stock):
        print(f"Начальник {self.name}: выручка {revenue} руб., остаток товара: {len(stock)} шт.")


class Baker:
    def __init__(self, name):
        self.name = name

    def bake(self, name, category, price):
        print(f"Пекарь {self.name} выпекает свежий '{name}' ({category})")
        return Product(name, category, price)


class Cashier:
    def __init__(self, name):
        self.name = name

    def sell(self, customer, product):
        if customer.wallet >= product.price:
            customer.wallet -= product.price
            customer.basket.append(product)
            print(f"Кассир {self.name}: продан '{product.name}' за {product.price} руб. клиенту {customer.name}")
            return product.price
        else:
            print(f"Кассир {self.name}: у клиента {customer.name} не хватает денег на '{product.name}'")
            return 0


class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.basket = []


def run_bakery_simulation():
    manager = Manager("Иван Петрович")
    baker = Baker("Алексей")
    cashier = Cashier("Анна")
    customer = Customer("Дмитрий", 350)

    stock = [
        baker.bake("Бородинский", "хлеб", 60),
        baker.bake("Синнабон", "булочка", 90),
        baker.bake("Сэндвич с курицей", "готовая еда", 130),
        baker.bake("Капучино", "напитки", 100),
    ]

    revenue = 0
    revenue += cashier.sell(customer, stock[1])
    revenue += cashier.sell(customer, stock[3])

    manager.inspect_bakery(revenue, stock)


# Задача 4: Симуляция «Ферма»
class Animal:
    def __init__(self, kind, cost, product_income):
        self.kind = kind
        self.cost = cost
        self.product_income = product_income
        self.stage = 1
        self.fed = False

    def feed(self):
        self.fed = True

    def grow(self):
        if self.fed and self.stage < 3:
            self.stage += 1
        self.fed = False

    def collect(self):
        if self.stage >= 2:
            return self.product_income * self.stage
        return 0


class Crop:
    def __init__(self, name, cost, harvest_income):
        self.name = name
        self.cost = cost
        self.harvest_income = harvest_income
        self.stage = 1

    def grow(self):
        if self.stage < 3:
            self.stage += 1

    def harvest(self):
        if self.stage == 3:
            return self.harvest_income
        return 0


class Farm:
    def __init__(self):
        self.coins = 100
        self.animals = [Animal("Курица", cost=30, product_income=15)]
        self.crops = [Crop("Пшеница", cost=10, harvest_income=25), Crop("Пшеница", cost=10, harvest_income=25)]
        self.fields_total = 5
        self.pens_total = 3
        self.day = 1
        self.is_night = False

    def status(self):
        time_of_day = "Ночь" if self.is_night else "День"
        print(f"--- День {self.day} ({time_of_day}) | Монеты: {self.coins} | Полей: {len(self.crops)}/{self.fields_total} | Животных: {len(self.animals)}/{self.pens_total} ---")

    def buy_animal(self, kind):
        catalog = {
            "курица": (30, 15),
            "овца": (70, 40),
            "корова": (150, 90),
        }
        if kind.lower() not in catalog:
            return
        cost, inc = catalog[kind.lower()]
        if self.coins >= cost and len(self.animals) < self.pens_total:
            self.coins -= cost
            self.animals.append(Animal(kind, cost, inc))
            print(f"Куплено животное: {kind} за {cost} монет")

    def buy_crop(self, name):
        catalog = {
            "пшеница": (10, 25),
            "кукуруза": (20, 50),
            "картошка": (35, 90),
        }
        if name.lower() not in catalog:
            return
        cost, inc = catalog[name.lower()]
        if self.coins >= cost and len(self.crops) < self.fields_total:
            self.coins -= cost
            self.crops.append(Crop(name, cost, inc))
            print(f"Посажена культура: {name} за {cost} монет")

    def feed_animals(self):
        for animal in self.animals:
            animal.feed()
        print("Все животные накормлены")

    def harvest(self):
        income = 0
        left_crops = []
        for crop in self.crops:
            gain = crop.harvest()
            if gain > 0:
                income += gain
            else:
                left_crops.append(crop)
        self.crops = left_crops

        for animal in self.animals:
            income += animal.collect()

        self.coins += income
        print(f"Собрана продукция и урожай на сумму: {income} монет")

    def upgrade_farm(self):
        cost = 100
        if self.coins >= cost:
            self.coins -= cost
            self.fields_total += 3
            self.pens_total += 2
            print(f"Ферма улучшена! Полей теперь {self.fields_total}, загонов {self.pens_total}")

    def next_phase(self):
        if not self.is_night:
            self.is_night = True
            print("Наступила ночь...")
        else:
            self.is_night = False
            self.day += 1
            for a in self.animals:
                a.grow()
            for c in self.crops:
                c.grow()
            print(f"Наступил новый день {self.day}!")


def run_farm_demo():
    farm = Farm()
    farm.status()
    farm.feed_animals()
    farm.buy_crop("кукуруза")
    farm.buy_animal("овца")
    farm.next_phase()
    farm.next_phase()
    farm.harvest()
    farm.upgrade_farm()
    farm.status()


if __name__ == "__main__":
    print("--- Проверка Задачи 1 (Иерархия пользователей) ---")
    user = User("base_user", "Pass1234")
    user.show_info()

    student = Student("ivan_stud", "Secret77", "Иван", 2)
    student.show_info()

    teacher = Teacher("petr_teach", "Teach2026", "Петр Сергеевич", 12)
    teacher.add_student(student)
    teacher.show_info()

    print("\n--- Проверка Задачи 2 (MyList) ---")
    my_list = MyList([1, 2, 3, 2, 40, 2])
    my_list.print_info()
    my_list.drop_value(2)
    print("После drop_value(2):", my_list)

    indexed_list = MyList([1, 3, 9, 80])
    indexed_list.add_indeces()
    print("После add_indeces():", indexed_list)
    indexed_list.append(10)
    print("После append(10):", indexed_list)

    print("\n--- Проверка Задачи 3 (Симуляция Пекарни) ---")
    run_bakery_simulation()

    print("\n--- Проверка Задачи 4 (Симуляция Фермы) ---")
    run_farm_demo()