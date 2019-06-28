# List Manipulation Service

This is a microservice built for transforming list of data into a different data set using nameko framework.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [nameko](https://nameko.readthedocs.io/en/stable/index.html).

```
pip install nameko
```

Go to [rabbitmq](https://www.rabbitmq.com/) and download rabbitmq then run:

```
brew services start rabbitmq
brew services stop rabbitmq
brew services restart rabbitmq
```

## Usage
A nameko service is just a class:

```python
from nameko.rpc import rpc
import math

class ListManipulationService:
    name = "list_manipulation_service"

    @rpc
    def squareOddNumbers(self, numbersList = []):
        oddNumbers = list(filter(lambda number: number % 2, numbersList))
        squareOddNumberList = list(map(lambda oddNumber: math.sqrt(oddNumber), oddNumbers))
        return squareOddNumberList
```

You can run it in a shell:

```
$ nameko run nameko run ListManipulationService
starting services: list_manipulation_service
...
```
And play with it from another:

```
$ nameko shell
>>> n.rpc.list_manipulation_service.squareOddNumbers([1, 3, 5, 6, 8, 9])
# [1.0, 1.7320508075688772, 2.23606797749979, 3.0]
```