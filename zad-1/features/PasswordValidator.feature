Feature: PasswordValidator
	Zadaniem klasy jest sprawdzenie czy podane hasła
	spełniają wymagania podane podczas tworzenia instancji klasy.

	Scenario: at least 8 letters, password "abc":
		Given there is a password validator
		and the password requires at least 8 letters
		When the password is "abc"
		Then the password is invalid

	Scenario: at least 8 letters, password "abcdefgh":
		Given there is a password validator
		and the password requires at least 8 letters
		When the password is "abcdefgh"
		Then the password is valid

	Scenario: at least 1 digit and 1 special character, password "abcdefgh":
		Given there is a password validator
		and the password requires at least 1 digit
		and the password requires at least 1 special character
		When the password is "abcdefgh"
		Then the password is invalid

	Scenario: at least 1 digit and 1 special character, password "@1":
		Given there is a password validator
		and the password requires at least 1 digit
		and the password requires at least 1 special character
		When the password is "@1"
		Then the password is valid

	Scenario: at least 5 uppercase letters, password "ABCDe":
		Given there is a password validator
		and the password requires at least 5 uppercase letters
		When the password is "abcdefgh"
		Then the password is invalid

	Scenario: at least 5 uppercase letters, password "ABCDE":
		Given there is a password validator
		and the password requires at least 5 uppercase letters
		When the password is "ABCDE"
		Then the password is valid
