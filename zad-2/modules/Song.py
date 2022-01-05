class Song:
	__song=[
		strippedLine for strippedLine in [
			line.strip() for line in """
				On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
				On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
				On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
				On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
			""".split("\n")
		] if strippedLine
	]
	def getLine(self, lineNumber):
		if not isinstance(lineNumber, int):
			raise TypeError("Line number must be an integer")
		try:
			if lineNumber < 1:
				raise IndexError
			return self.__song[lineNumber-1]
		except:
			raise IndexError("No such line")
	def getLines(self, startLineNumber = None, endLineNumber = None):
		startLineNumber = 1 if startLineNumber is None else startLineNumber
		endLineNumber = len(self.__song) if endLineNumber is None else endLineNumber
		try:
			if startLineNumber < 1 or endLineNumber < 1 or startLineNumber > len(self.__song) or endLineNumber > len(self.__song):
				raise IndexError
			if endLineNumber < startLineNumber:
				raise ValueError("End line number cannot be smaller than start line number")
			return self.__song[startLineNumber-1:endLineNumber]
		except IndexError:
			raise IndexError("No such line")
		except Exception as exception:
			raise exception
	def getAllLines(self):
		return self.__song
