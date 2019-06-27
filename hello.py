from nameko.rpc import rpc
import math


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)

    @rpc
    def squareOddNumbers(self, numbers = []):
        oddNumbers = list(filter(lambda number: number % 2, numbers))
        res = list(map(lambda oddNumber: math.sqrt(oddNumber), oddNumbers))
        return res

    # [1, 2, 3, 4, 5, 6, 9]
