from nameko.rpc import rpc
from dahuffman import HuffmanCodec
import math

class GreetingService:
    name = "greeting_service"

    @rpc
    def squareOddNumbers(self, numbers = []):
        oddNumbers = list(filter(lambda number: number % 2, numbers))
        res = list(map(lambda oddNumber: math.sqrt(oddNumber), oddNumbers))
        return res

    @rpc
    def encodedStringDict(self, listOfStrings = []):
        codec = HuffmanCodec.from_data(listOfStrings)
        encoded = codec.encode(listOfStrings)
        encodedDict = dict( zip(listOfStrings, encoded ))
        return encodedDict



    # ["hello", "at" , "test" , "this" , "here" , "now" ]

    # [1, 2, 3, 4, 5, 6, 9]
