from nameko.rpc import rpc
from dahuffman import HuffmanCodec
import math

class GreetingService:
    name = "greeting_service"

    @rpc
    def squareOddNumbers(self, numbersList = []):
        oddNumbers = list(filter(lambda number: number % 2, numbersList))
        squareOddNumberList = list(map(lambda oddNumber: math.sqrt(oddNumber), oddNumbers))
        return squareOddNumberList

    @rpc
    def encodedStringDict(self, listOfStrings = []):
        codec = HuffmanCodec.from_data(listOfStrings)
        encodeResults = codec.encode(listOfStrings)
        def decodeListOfString(encode):
            decodeResults = codec.decode(encode)
            return decodeResults
        decodedList = decodeListOfString(encodeResults)

        encodedDict = dict( zip(listOfStrings, encodeResults ))
        return encodedDict, decodedList
