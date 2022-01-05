from behave import *
import json

use_step_matcher("re")

def resolveGetLine(context, args):
	try:
		context.returnValue = context.song.getLine(*args)
	except Exception as exception:
		context.returnException = exception

def resolveGetLines(context, args):
	try:
		context.returnValue = context.song.getLines(*args)
	except Exception as exception:
		context.returnException = exception

@when("the line \"(?P<lineNumber>.+)\" is requested")
def step_impl(context, lineNumber):
	resolveGetLine(context, (lineNumber,))

@when("the line (?P<lineNumberAsText>.+) is requested")
def step_impl(context, lineNumberAsText):
	lineNumber = int(lineNumberAsText)
	resolveGetLine(context, (lineNumber,))

@when("the lines from \"(?P<lineNumberStart>.+)\" to \"(?P<lineNumberEnd>.+)\" are requested")
def step_impl(context, lineNumberStart, lineNumberEnd):
	resolveGetLines(context, (lineNumberStart, lineNumberEnd))



@when("the lines from (?P<lineNumberStartAsText>.+) to (?P<lineNumberEndAsText>.+) are requested")
def step_impl(context, lineNumberStartAsText, lineNumberEndAsText):
	lineNumberStart = int(lineNumberStartAsText)
	lineNumberEnd = int(lineNumberEndAsText)
	resolveGetLines(context, (lineNumberStart, lineNumberEnd))


@then("the return value is \[(?P<returnValueTableBodyAsText>.+)\]")
def step_impl(context, returnValueTableBodyAsText):
	returnValue = json.loads("[" + returnValueTableBodyAsText + "]")
	assert context.returnValue == returnValue

@then("the return value is \"(?P<returnValue>.+)\"")
def step_impl(context, returnValue):
	assert context.returnValue == returnValue

@then("an? ValueError is raised")
def step_impl(context):
	assert isinstance(context.returnException, ValueError)

@then("an? TypeError is raised")
def step_impl(context):
	assert isinstance(context.returnException, TypeError)

@then("an? IndexError is raised")
def step_impl(context):
	assert isinstance(context.returnException, IndexError)
