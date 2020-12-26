class Rulebook:
    skip = [" "]

    def __init__(self, rules):
        self.rules = rules
        self.last_valid_rule = None

    def is_exhausted(self):
        for rule in self.rules:
            if rule.is_alive:
                return False

        return True

    def parse(self, char):
        if char in self.skip:
            return

        for rule in self.rules:
            rule.parse(char)

            if rule.is_alive:
                self.last_valid_rule = rule

    def reset(self):
        for rule in self.rules:
            rule.reset()
            self.last_valid_rule = None