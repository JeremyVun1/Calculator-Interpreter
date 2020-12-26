class Rulebook:
    def __init__(self, rules):
        self.rules = rules

    def is_valid(self):
        for rule in self.rules:
            if rule.is_valid:
                return True

        return False

    def parse(self, char):
        for rule in self.rules:
            rule.parse(char)

    def reset(self):
        for rule in self.rules:
            rule.reset()