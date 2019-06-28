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

## In conclusion

```
I think the task taught me great lesson of being able to switch from Javascript into Python while getting used to the syntax and rules. The time it took to be able to finish the task took longer as I was constantly learning new framework like Nameko and Rabbitmq to be able to run my service successfully. I am currently at a point of running the service using docker container, still a work in progress at the moment but the service runs well locally.
```

### Technology comparison:
#### Advantages: 
```
1.  Nameko is a great tool for running micro-services and focus on individual/shared functionalities. Provides command-line interface which runs and interacts services easily over Nameko shell. Make use of TDD for testing functions.

2.  Rabbitmq is another awesome technology which functions as a message broker that implements  Advanced Messaging Queue Protocol(AMQP), an open message protocol. So far there is not a disadvantage I have encouted since I started working with it.
```
#### Disadvantages:
```
1.  Setting up Nameko to interact with other tools like Docker is not as straight forward or well documented. I had to rely on making sure my services work on my local machine without using any container. It took more time trying to interact Docker and Nameko service due to research and apply than implementing the functions and documentation.
```