# In class example

class Cars:

  def __init__(self):
    pass


  def read_car_makes(self):

    with open("car-makes", "r") as make_file:
      car_makes = { make[:-1] for make in make_file }

    return car_makes


  def read_car_models(self):

    with open("car-models", "r") as model_file:
      car_models = { model[:-1] for model in model_file }

    return car_models


  def create_collection(self):

    makes = self.read_car_makes()
    models = self.read_car_models()