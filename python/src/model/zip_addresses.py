from src.model.model import model

class zip_addresses(model):
    zip_address_id = model.get_db_instance(model).Column(model.get_db_instance(model).Integer, primary_key = True)
    def find_data(self):
        all_data = self.find_all(zip_addresses)
        if all_data == None:
            return []
        else:
            return all_data
