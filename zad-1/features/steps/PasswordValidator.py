from behave import *
from modules.PasswordValidator import PasswordValidator

use_step_matcher("re")


@given("there is a password validator")
def step_impl(context):
	context.passwordValidator = PasswordValidator()


@given("the password requires at least (?P<minUppercaseLettersCount>[0-9]+) uppercase letters?")
def step_impl(context, minUppercaseLettersCount):
	context.passwordValidator.minUppercaseLettersCount = int(minUppercaseLettersCount)


@given("the password requires at least (?P<minLettersCount>[0-9]+) letters?")
def step_impl(context, minLettersCount):
	context.passwordValidator.minLettersCount = int(minLettersCount)

@given("the password requires at least (?P<minDigitsCount>[0-9]+) digits?")
def step_impl(context, minDigitsCount):
	context.passwordValidator.minDigitsCount = int(minDigitsCount)

@given("the password requires at least (?P<minSpecialCharactersCount>[0-9]+) special characters?")
def step_impl(context, minSpecialCharactersCount):
	context.passwordValidator.minSpecialCharactersCount = int(minSpecialCharactersCount)

@when("the password is \"(?P<password>.+)\"")
def step_impl(context, password):
	context.password = password

@then("the password is invalid")
def step_impl(context):
	assert context.passwordValidator.validate(context.password) == False

@then("the password is valid")
def step_impl(context):
	assert context.passwordValidator.validate(context.password) == True