import shutil

base_dir = "my_files/"


def write_file(file_name, text):
    file = open(base_dir + file_name, 'w')
    file.write(text)
    file.close()


def update_file(file_name, text):
    file = open(base_dir + file_name, 'a')
    file.write(text)
    file.close()


def read_file(file_name):
    file = open(base_dir + file_name, 'r')
    text = file.read()
    print(text)


def copy_file_from_base_to_my_files(file_name):
    shutil.copy(file_name, base_dir)


def move_file_from_to(file_current_location, file_new_location):
    shutil.move(file_current_location, file_new_location)


def str_list_to_int_list(str_list):
    list_of_ints = []
    for item in str_list:
        list_of_ints.append(int(item))

    return list_of_ints


def average_note(file_name):
    file = open(base_dir + file_name, 'r')
    students = file.read()
    students = students.split('\n')
    average_note_dict = []
    for student in students:
        student_notes = student.split(',')
        student_name = student_notes[0]
        student_notes.pop(0)
        student_avg_note = sum(str_list_to_int_list(student_notes)) / len(student_notes)
        average_note_dict.append({student_name: student_avg_note})

    return average_note_dict


if __name__ == '__main__':
    avg_notes_list = average_note("notas.txt")

    write_file("avg_notes_by_student.txt", str(avg_notes_list))

    read_file("avg_notes_by_student.txt")
