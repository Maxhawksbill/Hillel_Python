class Counter:
    def __init__(self, initial_value, min_value=0, max_value=100):
        self.min_value = min_value
        self.initial_value = initial_value
        self.max_value = max_value

    def increase(self):
        if self.min_value > self.initial_value:
            print('Initial value can not be less than Minimum Value\n'
                  'Your counter has been reset to:', self.min_value)
            self.initial_value = self.min_value
        if self.initial_value > self.max_value:
            raise Exception('Your counter is out of range!')

        self.initial_value += 1
        if self.initial_value > self.max_value:
            raise Exception('Your counter is out of range!')
        return self.initial_value

    def output(self):
        print(self.initial_value)


counter1 = Counter(4, 0, 5)
counter1.output()
counter1.increase()
counter1.output()
counter1.increase()
counter1.output()
