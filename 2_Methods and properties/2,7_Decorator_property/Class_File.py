class File:
    def __init__(self, size: int):
        self._size_in_bytes = size
        print('name install')
    @property
    def size(self):
        print('getter')
        if self._size_in_bytes < 1024:
            return f'{self._size_in_bytes:.2f} B'
        if 1024 < self._size_in_bytes < 1048576:
            return f'{self._size_in_bytes / 1024:.2f} KB'
        if 1048576 < self._size_in_bytes < 1073741800:
            return f'{self._size_in_bytes / 1048576:.2f} MB'
        if self._size_in_bytes > 1073741800:
            return f'{self._size_in_bytes / 1073741800:.2f} GB'
    @size.setter
    def size(self, new):
        print('setter')
        self._size_in_bytes = new
