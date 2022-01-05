Feature: Song
	Scenario: get line 1
		When the line 1 is requested
		Then the return value is "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."

	Scenario: get line 2
		When the line 2 is requested
		Then the return value is "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."

	Scenario: get line "test"
		When the line "test" is requested
		Then a TypeError is raised

	Scenario: get line -1
		When the line -1 is requested
		Then an IndexError is raised

	Scenario: get lines from 1 to 1
		When the lines from 1 to 1 are requested
		Then the return value is ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."]

	Scenario: get lines from 1 to 2
		When the lines from 1 to 2 are requested
		Then the return value is ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.", "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."]

	Scenario: get lines from 2 to 1
		When the lines from 2 to 1 are requested
		Then a ValueError is raised

	Scenario: get lines from -1 to 1
		When the lines from -1 to 1 are requested
		Then an IndexError is raised

	Scenario: get lines from "abc" to "test"
		When the lines from "abc" to "test" are requested
		Then a TypeError is raised