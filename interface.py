from interests import list_of_inter
from base import base
from Person import person
from Person import is_int


class Interface:
    # Класс для взаимодействия - общения с пользователем. Так же именно он будет обрабатывать разного рода запросы
    # по изменению каким-то образом фильтра и иных вещей
    def __init__(self):
        # Конструктор для класса. Нам потребуется база данных, список всех профессий и фильтр
        self.all_inter = list_of_inter()
        self.data_base = base()
        self.user = person()

    def upload_base_from_file(self):
        self.data_base.read_person_from_file()

    def upload_spec_from_file(self):
        self.all_inter.read_from_file()

    def interact_with_user(self):
        # главная функция интерактива с пользователем
        self.upload_spec_from_file()
        self.upload_base_from_file()
        print('Привет, пользователь. Ты находишься на лучшем сайте  \'RuTinder\'.')
        self.user.fill_person_from_console(self.all_inter)
        self.data_base.sift_and_print(self.user)
        while True:

            console_input = input('1) Change user\n2) Show info\n3) Exit')
            if is_int(console_input):
                match int(console_input) :
                    case 1:
                        self.user.change_person_from_console(self.all_inter)
                        self.data_base.sift_and_print(self.user)
                    case 2:
                        self.user.print_user_person_info()
                    case 3:
                        break
