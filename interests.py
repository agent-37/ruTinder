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


class list_of_inter:
    inter = []

    def add_specialization(self, new_int: str):

        if new_int not in self.inter:
            self.inter.append(new_int)

    def read_from_file(self):
        # чтение специализаций из файла с проверкой повторений
        with open('input_file_of_int.txt') as f_spec:
            file_str = f_spec.readline()[:-1]
            self.add_specialization(file_str)
            while file_str:
                file_str = f_spec.readline()[:-1]
                if file_str != '':
                    self.add_specialization(file_str)

    def print(self):
        pos = 1
        for i in self.inter:
            print(pos, i)
            pos += 1
        return pos

