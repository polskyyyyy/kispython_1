class StateMachine:
    state = 'A'

    def open(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'E'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise (KeyError)

    def file(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'A'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'D':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'C'
            return 9
        else:
            raise (KeyError)


def main():
    return StateMachine()


o = main()
print(o.open())  # 0
print(o.open())  # 2
print(o.file())  # 7
print(o.file())  # 9
print(o.file())  # 4
print(o.open())  # 0
print(o.file())  # 1
print(o.open())  # 3
print(o.open())  # 5
print(o.file())  # 7
print(o.open())  # 8
