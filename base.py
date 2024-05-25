from Person import person
from interests import list_of_inter


class base:
    def __init__(self):
        self.data_base = []
        self.free_id = 0

    def read_person_from_file(self):
        f_prof = open('input_file_of_person.txt')
        buf = person()
        while buf.fill_person_from_file(f_prof, self.free_id) == 1:
            self.data_base.append(buf.copy())
            self.free_id += 1
            # self.print()

    def print(self):
        for i in self.data_base:
            i.print_person_info()

    def sift_and_print(self, new_person: person):
        buf_data_base = base()

        for i in self.data_base:

            if new_person.check_cool(i) and i.check_cool(new_person):
                buf_data_base.data_base.append(i)

        buf_data_base.print()
