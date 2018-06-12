import json
import keras.backend as K 
from keras.layers import Dense, LSTM, Bidirectional, Embedding



class BaseModel(object):
	""" Base model class with load and save methods """
	def __init__(self):
		self.model = None

	def save(self, weights_file, params_file):
		self.save_weights(weights_file)
		self.save_params(params_file)

	def save_weights(self, file_path):
		self.model.save_weights(file_path)

	def save_params(self, file_path):
		with open(file_path, 'w') as f:
			params = {name.lstrip('_'): val for name, val in vars(self).items()
						if name not in {'_loss','model','_embeddings'}}
			json.dump(params, f, sort_keys=True, indent=4)

	@classmethod
	def load(cls, weights_file, params_file):
		params = cls.load_params(params_file)
		self = cls(**params)
		self.build()
		self.load_weights(weights_file)
		return self 

	@classmethod
	def load_params(cls, file_path):
		with open(file_path) as f:
			params = json.load(f)




































