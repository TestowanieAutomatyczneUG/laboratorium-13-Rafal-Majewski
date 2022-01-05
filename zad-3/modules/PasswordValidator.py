class PasswordValidator:
	def __init__(self, *, minLettersCount = 0, minUppercaseLettersCount = 0, minDigitsCount = 0, minSpecialCharactersCount = 0):
		self.minLettersCount = minLettersCount
		self.minDigitsCount = minDigitsCount
		self.minSpecialCharactersCount = minSpecialCharactersCount
		self.minUppercaseLettersCount = minUppercaseLettersCount
	def validate(self, password):
		lettersCount = 0
		digitsCount = 0
		specialCharactersCount = 0
		uppercaseLettersCount = 0
		try:
			for character in password:
				if character.isupper():
					uppercaseLettersCount += 1
				if character.isalpha():
					lettersCount += 1
				elif character.isdigit():
					digitsCount += 1
				else:
					specialCharactersCount += 1
		except TypeError:
			raise TypeError("Non iterable datatype provided as the input")
		except AttributeError:
			raise TypeError("Non string datatype provided in the input")

		if uppercaseLettersCount < self.minUppercaseLettersCount:
			return False
		if lettersCount < self.minLettersCount:
			return False
		if digitsCount < self.minDigitsCount:
			return False
		if specialCharactersCount < self.minSpecialCharactersCount:
			return False
		return True