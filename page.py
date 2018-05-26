class Page(object):
		
	def __init__(self, experience=False):
		self.__coeff = []
		self.__power = []
		self.__exp = bool(experience)
	
	def add_coefficient(self, value):
		self.__coeff.append(value)
		self.__power.append(len(self.__coeff))
		
	def add_coefficient_and_power(self, value, power_value):
		self.__coeff.append(value)
		self.__power.append(power_value)
		
	def get_coefficient(self, power):
		return self.__coeff[self.__power[power]]
	
	def get_coefficient_count(self):
		return len(self.__coeff)
		
	def get_power(self, which):
		return self.__power[which]
		
	def get_power_count(self):
		return len(self.__power)
		
	def is_experience(self):
		return self.__exp
		
	def remove_coefficient(self):
		self.__coeff.pop(len(self.__coeff) - 1)
		self.__power.pop(len(self.__power) - 1)
		
	def remove_coefficient_and_power(self):
		self.remove_coefficient()
	
	def set_coefficient(self, power, value):
		self.__coeff[self.__power[power]] = value
		
	def set_experience(self, value):
		self.__exp = bool(value)
		
	def set_power(self, which, value):
		self.__power[which] = value

	def evaluate(self, param_value):
		result = 0
		counter = 0
		for c in self.__coeff:
			result = result + c * param_value ** self.__power[counter]
			counter = counter + 1
			if self.__exp:
				result = result - c
		return result
		
	def integer_evaluate(self, param_value):
		result = 0
		counter = 0
		for c in self.__coeff:
			result = int(result + c * param_value ** self.__power[counter])
			counter = counter + 1
			if self.__exp:
				result = int(result - c)
		return result
		
	def evaluate_to_list(self, start, end, increment=1):
		result = []
		counter = start
		while counter <= end:
			result.append(self.evaluate(counter))
			counter = counter + increment
		return result
		
	def integer_evaluate_to_list(self, start, end, increment=1):
		result = []
		counter = int(start)
		finish = int(end)
		while counter <= finish:
			result.append(self.integer_evaluate(counter))
			counter = counter + int(increment)
		return result