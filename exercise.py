class Flatten:
    def __init__(self):
        self.empty_list = []

    def set_flatten_list(self, x):
        if isinstance(x, list) == False:
            return "Must be a list"

        for a in x:
            if isinstance(a, list):
                self.set_flatten_list(a)
            else:
                self.empty_list.append(a)

    def get_flatten_list(self):
        return self.empty_list
