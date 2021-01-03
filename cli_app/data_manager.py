import pymongo


class DataManager(object):

    # Use local db by default
    client = pymongo.MongoClient()
    cli_db = client['cli_db']
    cli_collection = cli_db['cli_collection']

    def write_record(self, record):
        self.cli_collection.save(record)

    def get_list(self, query=None, projection=None):
        records = self.cli_collection.find(query, projection=projection)
        return [record for record in records]

    def get_by_index(self, index):
        record = self.cli_collection.find_one({'index': index})
        return record

    def update_record(self, index, new_values):
        self.cli_collection.update_one({'index': index}, {"$set": new_values}, upsert=True)

    def validate_index(self, index):
        record = self.get_by_index(index)
        if not record:
            raise Exception("Record with index {0} does not exists.".format(index))
        return record

    def drop(self):
        self.cli_collection.drop()
