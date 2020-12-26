from abc import abstractmethod

class BaseRule:
    def __init__(self):
        self.state = ""
        self.is_alive = True

    @abstractmethod
    def validate(self, char):
        return True

    def parse(self, char):
        if self.validate(self.state + char):
            self.state += char
        else self.is_alive = False

    def reset(self):
        self.state = ""
