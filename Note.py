from datetime import datetime
import uuid


class Note:
    def constructor(self, id = str(uuid.uuid1())[0:3],  title = "text", body = "text", date = str(datetime.now().strftime("%d.%m.%Y %H:%M"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(note):
        return note.id

    def set_id(note):
        note.id = str(uuid.uuid1())[0:3]

    def get_title(note):
        return note.title
    
    def set_title(note, title):
        note.title = title

    def get_body(note):
        return note.body
    
    def set_body(note, body):
        note.body = body

    def get_date(note):
        return note.date

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M"))

    def toString(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map(note):
        return '\nID: ' + note.id + '\n' + 'Title: ' + note.title + '\n' + 'Note: ' + note.body + '\n' + 'Date: ' + note.date