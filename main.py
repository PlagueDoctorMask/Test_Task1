import defs

print("\nNotes\nChoose a number of action: \n\n1) To show all the notes\n3) To add the note\n3) To delete the note\n4) To edit the note\n5) To find the note by id\n6) To find the note by the date\n7) To shut down the app\n")
flag = True
choice = int(input())
while(flag):
    if choice==1:
        defs.Show("all")
    if choice==2:
        defs.addNote()
    if choice==3:
        defs.ActionsWithNotes("delete")
    if choice==4:
        defs.ActionsWithNotes("edit")
    if choice==5:
        defs.Show("id")
    if choice==6:
        defs.Show("date")
    if choice==7:
        print("Shutting down")
        flag = False