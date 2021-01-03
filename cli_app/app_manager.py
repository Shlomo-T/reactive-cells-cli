from cli_app.data_manager import DataManager
from cli_app.parser import UserInputParser


class AppManager(object):

    data_manager = DataManager()

    def current_status(self):
        records = self.data_manager.get_list(projection={'index': True, 'value': True, '_id': False})
        return [record_data for record_data in records]

    def init_db(self, raw_records):
        self.data_manager.drop()
        for index, value in enumerate(raw_records):
            res = UserInputParser().validate(value.strip())
            res['index'] = index
            if res['formula']:
                res['value'] = self.evaluate_formula(res['formula'], res['dependencies'])
            print(res)
            self.data_manager.write_record(res)

    def modify_record(self, index, new_value):
        self.data_manager.validate_index(index)
        result = UserInputParser().validate(new_value.strip())
        if result['formula']:
            result['value'] = self.evaluate_formula(result['formula'], result['dependencies'])
        self.data_manager.update_record(index, result)

        records_to_update = self.get_values_by_dependencies(index)
        for record in records_to_update:
            result['value'] = self.evaluate_formula(record['formula'], record['dependencies'])
            self.data_manager.update_record(record['index'], result)

    def get_values_by_dependencies(self, index):
        records = self.data_manager.get_list(query={"dependencies": index})
        return [record for record in records]

    def get_by_index(self, indexes):
        records = self.data_manager.get_list(query={"index": {'$in': indexes}})
        return [record for record in records]

    def evaluate_formula(self, formula, dependencies):
        dependencies_values = self.data_manager.get_list(query={"index": {'$in': dependencies}},
                                                         projection={'value': True, 'index': True, '_id': False})
        if len(dependencies) != len(dependencies_values):
            raise Exception("Amount of calculated values mismatch to the amount of formula dependencies")
        values = {record['index']: record['value'] for record in dependencies_values}
        rendered_formula = formula.replace('=', '')
        rendered_formula = UserInputParser().inject_formula_values(rendered_formula, values)
        return eval(rendered_formula)
