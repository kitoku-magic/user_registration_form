from src.model.model import model

class zip_address(model):
    __tablename__ = 'zip_address'
    zip_address_id = model.get_db_instance(model).Column(model.get_db_instance(model).Integer, primary_key = True)
    def find_data(self):
        all_data = self.find_all(zip_address)
        if all_data == None:
            return []
        else:
            return all_data
