import regex as re


class UserInputParser(object):
    integer_compiler = re.compile(r'^\d+$')
    formula_compiler = re.compile(r'=((({(?P<index>\d+)})|(\d+))[\+\-\/\*])+(({(?P<index>\d+)})|(\d+))')

    def validate(self, value):
        result = self.check_integer(value)
        if not result:
            result = self.check_formula(value)
        if not result:
            raise Exception("Invalid Input, please verify that you insert an integer or valid formula.")
        return self.format_result(*result)

    def check_integer(self, value):
        search_result = re.search(self.integer_compiler, value)
        if search_result and search_result.group():
            return search_result.group(), None, []

    def check_formula(self, value):
        search_result = re.match(self.formula_compiler, value)
        if search_result and search_result.group():
            return None, search_result.group(), search_result.captures('index')

    def format_result(self, value, formula, dependencies):
        formatted_result = {
            'value': value,
            'formula': formula,
            'dependencies': [int(dependency) for dependency in dependencies]
        }
        return formatted_result

    def inject_formula_values(self, formula, values):
        rendered_formula = formula
        for index, value in values.items():
            index_representation = '{' + str(index) + '}'
            rendered_formula = rendered_formula.replace(index_representation, str(value))
        return rendered_formula
