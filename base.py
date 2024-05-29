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
        buf_list = []
        for i in range(len(self.data_base)):

            if new_person.acc_gender == self.data_base[i].gender and self.data_base[i].acc_gender == new_person.gender:
                buf_list.append(
                    [new_person.check_cool(self.data_base[i]) + self.data_base[i].check_cool(new_person), i])
        for i in sorted(buf_list):
            buf_data_base.data_base.append(self.data_base[i[1]])
        # print(sorted(buf_list))
        buf_data_base.print()
