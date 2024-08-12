class Notebook:
    def __init__(self, args):
        self._notes = list(args)

    @property
    def notes_list(self):
        count = 1
        for note in self._notes:
            print(f'{count}.{note}')
            count += 1


note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list
