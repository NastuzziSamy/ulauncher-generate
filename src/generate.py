from src.consts import GENERATORS


class Generate():
    def __init__(self, params):
        self.use_generator(params.pop(0) if params else '')

        self.args = params


    def use_generator(self, name):
        if not name:
            self.gen_name = None
            self.generator = None
            return

        for (gen_name, gen_data) in GENERATORS.items():
            if gen_name.startswith(name):
                self.gen_name = gen_name
                self.generator = gen_data['class']()
                return


    def has_generator(self):
        return self.generator is not None


    def has_args(self):
        return len(self.args) > 0


    def execute(self):
        if self.has_args():
            return self.generator.generate(self.args)
        else:
            return self.generator.show_defaults()