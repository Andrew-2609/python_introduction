class NoteError(Exception):
    pass


class NoteValueError(NoteError):
    def __init__(self, message):
        self.message = message


while True:
    try:
        note = int(input("Insert an integer note from 0 to 10: "))
        if note > 10:
            raise NoteValueError("The note must not be bigger than 10!")
        elif note < 0:
            raise NoteValueError("The note must be bigger than 0!")
    except ValueError:
        print("The value must be an integer.")
    except NoteValueError as nve:
        print(nve)
    else:
        print("The typed note was: ".format(note))
        break
