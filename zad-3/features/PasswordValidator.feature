Feature: PasswordValidator
	Zadaniem klasy jest sprawdzenie czy podane hasła
	spełniają wymagania podane podczas tworzenia instancji klasy.

	@minLettersCount
	Scenario: at least 8 letters, password "abc":
		Given there is a password validator
		and the password requires at least 8 letters
		When the password is "abc"
		Then the password is invalid

	@minLettersCount
	Scenario: at least 8 letters, password "abcdefgh":
		Given there is a password validator
		and the password requires at least 8 letters
		When the password is "abcdefgh"
		Then the password is valid

	@minLettersCount @minDigitsCount @minSpecialCharactersCount
	Scenario: at least 1 digit and 1 special character, password "abcdefgh":
		Given there is a password validator
		and the password requires at least 1 digit
		and the password requires at least 1 special character
		When the password is "abcdefgh"
		Then the password is invalid

	@minDigitsCount @minSpecialCharactersCount
	Scenario: at least 1 digit and 1 special character, password "@1":
		Given there is a password validator
		and the password requires at least 1 digit
		and the password requires at least 1 special character
		When the password is "@1"
		Then the password is valid

	@minUppercaseLettersCount
	Scenario: at least 5 uppercase letters, password "ABCDe":
		Given there is a password validator
		and the password requires at least 5 uppercase letters
		When the password is "abcdefgh"
		Then the password is invalid

	@minUppercaseLettersCount
	Scenario: at least 5 uppercase letters, password "ABCDE":
		Given there is a password validator
		and the password requires at least 5 uppercase letters
		When the password is "ABCDE"
		Then the password is valid

	@minUppercaseLettersCount @minDigitsCount @minSpecialCharactersCount
	Scenario: at least 1 digit, 1 special character, 2 uppercase letters, password "3AA(":
		Given there is a password validator
		and the password requires at least 1 digit
		and the password requires at least 1 special character
		and the password requires at least 2 uppercase letters
		When the password is "3AA("
		Then the password is valid

	@minUppercaseLettersCount @minDigitsCount @minSpecialCharactersCount
	Scenario: at least 1 digit, 1 special character, 2 uppercase letters, password "ABCDE":
		Given there is a password validator
		and the password requires at least 1 digit
		and the password requires at least 1 special character
		and the password requires at least 2 uppercase letters
		When the password is "ABCDE"
		Then the password is invalid

	@minDigitsCount
	Scenario: at least 0 digits, password "ABCDE":
		Given there is a password validator
		and the password requires at least 0 digits
		When the password is "ABCDE"
		Then the password is valid

	@minUppercaseLettersCount @minLettersCount
	Scenario: at least 2 uppercase letters, at least 3 letters, password "ABf":
		Given there is a password validator
		and the password requires at least 2 uppercase letters
		and the password requires at least 3 letters
		When the password is "ABf"
		Then the password is valid
	
	@minUppercaseLettersCount @minLettersCount
	Scenario: at least 2 uppercase letters, at least 3 letters, password "Amm":
		Given there is a password validator
		and the password requires at least 2 uppercase letters
		and the password requires at least 3 letters
		When the password is "Amm"
		Then the password is invalid