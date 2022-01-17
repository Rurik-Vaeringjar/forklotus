# forklotus/exceptions.py

class LotusError(Exception):
	'''Base class for exceptions in this module.'''

	def __str__(self):
		return self.message

class DictTypeError(LotusError):
	'''Error class to be raised when an incorrect object is passed to a class constructor.'''

	def __init__(self, goal_class, dict_obj):
		self.goal_class = goal_class
		self.dict_obj = dict_obj
		self.message = '\n ↳ Was expecting an object of type dict that matches the ' 
		self.message += f"{self.goal_class} class, got an object of type "
		self.message += str(type(self.dict_obj)) + ' instead.'

class DictKeyError(LotusError):
	'''Error class to be raised when an invalid dictionary key is used'''

	def __init__(self, goal_class, key):
		self.goal_class = goal_class
		self.key = key
		self.message = f"\n ↳ Was expecting \'{self.key}\' in dictionary passed to {self.goal_class} class, was not found."

class ListTypeError(LotusError):
	'''Error class to be raised when an incorrect object is passed to a class constructor.'''

	def __init__(self, goal_class, list_obj):
		self.goal_class = goal_class
		self.dict_obj = dict_obj
		self.message = '\n ↳ Was expecting an object of type list that matches the ' 
		self.message += f"{self.goal_class} class, got an object of type "
		self.message += str(type(self.list_obj)) + ' instead.'

class NonPlatformError(LotusError):
	'''Error class to be raised when an invalid platform is called in the constructor of a wf_api'''

	def __init__(self, fake_platform):
		self.fake_platform = fake_platform
		self.message = f"\n ↳ {self.fake_platform} is not a valid platform. "
		self.message += 'Pass \'pc\', \'ps4\', \'xb1\', or \'swi\'.'

class StatusCodeError(LotusError):
	'''Error class to be raised when a response object does not have a 200 status code.'''

	def __init__(self, actual_code, call_name):
		self.actual_code = actual_code
		self.call_name = call_name
		self.message = f"\n ↳ Warning: response object from API call {self.call_name}"
		self.message += ' returned with a status code of ' + str(self.actual_code)
		self.message += ', not 200. Forwarding response object anyway.'

