from abc import abstractmethod

class BaseRule:
    def __init__(self):
        self.state = ""
        self.is_alive = True

    @abstractmethod
    def validate(self, char):
        raise NotImplementedError("validate not implemented")

    def parse(self, char):
        new_state = self.state + char
        if self.validate(new_state):
            self.state = new_state
        else:
            self.is_alive = False

    def reset(self):
        self.state = ""
        self.is_alive = True

    @abstractmethod
    def get_token(self):
        raise NotImplementedError("get_token not implemented")