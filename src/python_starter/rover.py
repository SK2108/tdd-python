class Rover:
    def __init__(self):
        """Initialize the rover's position and orientation."""
        self.position = (0, 0)
        self.orientation = 'N'
        self._directions = ['N', 'E', 'S', 'W']

    def execute(self, commands):
        for command in commands:
            if command == 'L':
                self._turn_left()
            elif command == 'R':
                self._turn_right()
            elif command == 'F':
                self._move_forward()
            elif command == 'B':
                self._move_backward()

    def _turn_left(self):
        current_index = self._directions.index(self.orientation)
        self.orientation = self._directions[(current_index - 1) % 4]

    def _turn_right(self):
        current_index = self._directions.index(self.orientation)
        self.orientation = self._directions[(current_index + 1) % 4]

    def _move_forward(self):
        x, y = self.position
        if self.orientation == 'N':
            y += 1
        elif self.orientation == 'S':
            y -= 1
        elif self.orientation == 'E':
            x += 1
        elif self.orientation == 'W':
            x -= 1
        self.position = (x, y)

    def _move_backward(self):
        x, y = self.position
        if self.orientation == 'N':
            y -= 1
        elif self.orientation == 'S':
            y += 1
        elif self.orientation == 'E':
            x -= 1
        elif self.orientation == 'W':
            x += 1
        self.position = (x, y)