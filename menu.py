"""
Laboratory 4.6
menu.py
GitHub: https://github.com/just1ce415/notebook.git
"""

import sys
from notebook import Notebook

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        '''
        Docstring
        '''
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        '''
        Docstring
        '''
        print("""
Notebook Menu

1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        '''
        Docstring
        '''
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
            note.id, note.tags, note.memo))

    def search_notes(self):
        '''
        Docstring
        '''
        note_filter = input("Search for: ")
        notes = self.notebook.search(note_filter)
        self.show_notes(notes)

    def add_note(self):
        '''
        Docstring
        '''
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        '''
        Docstring
        '''
        note_id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            if not self.notebook.modify_memo(note_id, memo):
                print('Error')
        if tags:
            if not self.notebook.modify_tags(note_id, tags):
                print('Error')

    def quit(self):
        '''
        Docstring
        '''
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
