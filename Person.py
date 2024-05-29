from interests import list_of_inter


def is_float(element: any) -> bool:
    # Проверка, того что элемент это число с плавающей запятой
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


def is_int(element: any) -> bool:
    # Проверка, того что элемент это целое число
    if element is None:
        return False
    try:
        int(element)
        return True
    except ValueError:
        return False


class person:
    def __init__(self):
        id = -1
        name = ''
        gender = 'F'
        city = ''
        age = 18
        list_of_interests = []
        min_age = 18
        max_age = 18
        acc_gender = 'M'
        min_int = 0

    def delete_all_info(self) -> None:
        # Удаляет всю информации из фильтра, просто упрощение, чтобы не удалять все вручную
        self.name = None
        self.gender = None
        self.city = None
        self.age = None
        self.list_of_interests = None
        self.min_age = None
        self.max_age = None
        self.acc_gender = None
        self.min_int = None

    def print_user_person_info(self):
        print('------------------------------')
        print('NAME:', self.name)
        print('Gander:', self.gender)
        print('Age:', self.age)
        print('City:', self.city)
        print('Min_age', self.min_age)
        print('Max_age', self.max_age)
        print('acc_gender', self.acc_gender)
        print('min_int', self.min_int)
        if len(self.list_of_interests) != 0:
            print('Interests:')
            for i in self.list_of_interests:
                print(i)
        print('------------------------------')

    def print_person_info(self):
        # Функция выводит информацию о фильтре
        print('------------------------------')
        print('NAME:', self.name)
        print('Gander:', self.gender)
        print('Age:', self.age)
        print('City:', self.city)
        if len(self.list_of_interests) != 0:
            print('Interests:')
            for i in self.list_of_interests:
                print(i)
        print('------------------------------')

    def change_name_from_console(self):
        # Функция смены имени с консоли

        console_input = input('Fill NAME\n')
        self.name = console_input

    def change_gender_from_console(self):
        # Функция смены имени с консоли

        while True:
            console_input = input('Fill Gender\n')
            if console_input == 'F' or console_input == 'M':
                break
        self.gender = console_input

    def change_city_from_console(self):
        # Функция смены имени с консоли

        console_input = input('Fill City\n')
        self.city = console_input

    def change_age_from_console(self):
        # Функция смены имени с консоли

        while True:
            console_input = input('Fill Age\n')
            if is_int(console_input) and 18 <= int(console_input):
                break
        self.age = int(console_input)

    def change_min_age_from_console(self):
        # Функция смены имени с консоли

        while True:
            console_input = input('Fill min_Age\n')
            if is_int(console_input) and 18 <= int(console_input):
                break
        self.min_age = int(console_input)

    def change_max_age_from_console(self):
        # Функция смены имени с консоли

        while True:
            console_input = input('Fill max_Age\n')
            if is_int(console_input) and max(18, self.min_age) <= int(console_input):
                break
        self.max_age = int(console_input)

    def change_acc_gender_from_console(self):
        # Функция смены имени с консоли

        while True:
            console_input = input('Fill acc_Gender\n')
            if console_input == 'F' or console_input == 'M':
                break
        self.acc_gender = console_input

    def change_min_int_from_console(self):
        while True:
            console_input = input('Fill min_int\n')
            if is_int(console_input) and 0 <= int(console_input):
                break
        self.min_int = int(console_input)

    def change_list_of_inter(self, inter_list: list_of_inter):
        pos = inter_list.print()
        buf = set()
        print(pos, 'Exit')
        while True:
            console_input = input()
            if is_int(console_input) and 0 < int(console_input) <= pos:
                if int(console_input) == pos:
                    break
                else:
                    buf.add(inter_list.inter[int(console_input) - 1])
        self.list_of_interests = buf

    def fill_person_from_console(self, inter_list: list_of_inter):

        self.change_name_from_console()

        self.change_gender_from_console()

        self.change_city_from_console()

        self.change_age_from_console()

        self.change_min_age_from_console()

        self.change_max_age_from_console()

        self.change_acc_gender_from_console()

        self.change_min_int_from_console()

        self.change_list_of_inter(inter_list)

    def change_person_from_console(self, inter_list: list_of_inter):
        print('Change')
        print('1)Name', '2)Gender', '3)City', '4)Age', '5)min_age', '6)max_age', '7)acc_gender', '8)min_int',
              '9)list_inter', '10)Exit', sep='\n')
        while True:
            console_input = input()
            if is_int(console_input):
                match int(console_input):
                    case 1:
                        self.change_name_from_console()
                    case 2:
                        self.change_gender_from_console()
                    case 3:
                        self.change_city_from_console()
                    case 4:
                        self.change_age_from_console()
                    case 5:
                        self.change_min_age_from_console()
                    case 6:
                        self.change_max_age_from_console()
                    case 7:
                        self.change_acc_gender_from_console()
                    case 8:
                        self.change_min_int_from_console()
                    case 9:
                        self.change_list_of_inter(inter_list)
                    case 10:
                        break

    def fill_person_from_file(self, f_person, id):
        buf = f_person.readline()[: -1].split(';')
        if len(buf) <= 8:
            return 0
        self.id = id
        self.name = buf[0].split()[0]
        self.age = int(buf[1].split()[0])
        self.gender = buf[2].split()[0]
        self.acc_gender = buf[3].split()[0]
        self.city = buf[4].split()[0]
        self.min_age = int(buf[5].split()[0])
        self.max_age = int(buf[6].split()[0])
        self.min_int = int(buf[7].split()[0])
        self.list_of_interests = set(buf[8].split(','))
        return 1

    def check_cool(self, new_person: 'person'):
        cost = 0
        if new_person.city != self.city:
            cost += 10
        if self.min_age > new_person.age or self.max_age < new_person.age:
            cost += min(abs(new_person.age - self.min_age), abs(self.max_age - new_person.age))
        count = 0
        for i in self.list_of_interests:
            if i in new_person.list_of_interests:
                count += 1
        cost += max(0, self.min_int - count) * 2
        return cost

    def copy(self):
        buf = person()
        buf.name = self.name
        buf.gender = self.gender
        buf.city = self.city
        buf.age = self.age
        buf.list_of_interests = self.list_of_interests
        buf.min_age = self.min_age
        buf.max_age = self.max_age
        buf.acc_gender = self.acc_gender
        buf.min_int = self.min_int
        return buf
