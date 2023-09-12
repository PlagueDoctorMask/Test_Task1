import Note

def create_note():
    title = (input('enter the title: '))
    body = (input('create the note: '))
    return Note.Note(title=title, body=body)

def write_file(array, mode):
    file = open("Notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("Notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.toString(notes))
        file.write('\n')
    file.close


def read_file():
    array = []
    file = open("Notes.csv", "r", encoding='utf-8')
    notes = file.read().strip().split("\n")
    for n in notes:
        split_n = n.split(';')
        note = Note.Note(
            id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
        array.append(note)
    return array

def addNote():
    note = create_note()
    array = read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    write_file(array, 'a')
    print('The note has added')

def Show(mode):
    flag = True
    array = read_file()
    if mode == 'date':
        date = input('enter the date with pattern dd.mm.yyyy: ')
    for notes in array:
        if mode == 'all':
            flag = False
            print(Note.Note.map(notes))
        if mode == 'id':
            flag = False
            print('ID: ' + Note.Note.get_id(notes))
        if mode == 'date':
            flag = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map(notes))
    if flag == True:
        print('there are no notes')

def ActionsWithNotes(mode):
    id = input('enter the id of the chosen note: ')
    array = read_file()
    flag = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            flag = False
            if mode == 'edit':
                note = create_note()
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('The note has been changed')
            if mode == 'delete':
                array.remove(notes)
                print('The note has been deleted')
            if mode == 'show':
                print(Note.Note.map(notes))
    if flag == True:
        print('there is no such a note')
    write_file(array, 'a')

        