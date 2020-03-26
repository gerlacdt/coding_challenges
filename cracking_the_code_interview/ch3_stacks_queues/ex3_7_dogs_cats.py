"""People can adopt animals from an animal shelter. They can adopt the
"oldest" animal or they can select the older cat or dog (then you
receive the oldest animal of that type)
"""

from collections import deque
import pytest


class Dog:
    def __init__(self, name):
        self.order = 0
        self.name = name

    def __str__(self):
            return "{} Dog: {}".format(self.order, self.name)

    def __repr__(self):
            return "{} Dog: {}".format(self.order, self.name)


class Cat:
    def __init__(self, name):
        self.order = 0
        self.name = name

    def __str__(self):
        return "{} Cat: {}".format(self.order, self.name)

    def __repr__(self):
        return "{} Cat: {}".format(self.order, self.name)


class AnimalShelter:
    def __init__(self):
        self.order = 0
        self.dogs = deque([])
        self.cats = deque([])

    def __str__(self):
        return "(order: {} dogs: {} cats: {})".format(self.order,
                                                      self.dogs, self.cats)

    def enqueue(self, animal):
        animal.order = self.order
        if isinstance(animal, Cat):
            self.cats.append(animal)
        elif isinstance(animal, Dog):
            self.dogs.append(animal)
        else:
            raise RuntimeError("Only cats or dogs can be enqueued")
        self.order += 1

    def dequeAny(self):
        oldestCat = oldestDog = None
        if len(self.cats) > 0:
            oldestCat = self.cats[-1]
        if len(self.dogs) > 0:
            oldestDog = self.dogs[-1]
        if not oldestCat and not oldestDog:
            raise RuntimeError("no animal to deque")
        if not oldestCat and oldestDog:
            return self.dogs.popleft()
        if not oldestDog and oldestCat:
            return self.cats.popleft()
        if oldestDog and oldestCat:
            if oldestDog.order < oldestCat.order:
                return self.dogs.popleft()
            else:
                return self.cats.popleft()

    def dequeCat(self):
        if len(self.cats) <= 0:
            raise RuntimeError("no cats to deque")
        return self.cats.popleft()

    def dequeDog(self):
        if len(self.dogs) <= 0:
            raise RuntimeError("no dogs to deque")
        return self.dogs.popleft()


def test():
    shelter = AnimalShelter()
    shelter.enqueue(Cat("cat0"))
    shelter.enqueue(Dog("dog1"))
    shelter.enqueue(Dog("dog2"))
    shelter.enqueue(Dog("dog3"))

    result = shelter.dequeAny()
    assert result.name == "cat0" and result.order == 0

    result = shelter.dequeDog()
    assert result.name == "dog1" and result.order == 1

    with pytest.raises(RuntimeError) as exinfo:
        shelter.dequeCat()
    assert str(exinfo.value) == "no cats to deque"

    result = shelter.dequeAny()
    assert result.name == "dog2" and result.order == 2

    result = shelter.dequeAny()
    assert result.name == "dog3" and result.order == 3

    with pytest.raises(RuntimeError) as exinfo:
        shelter.dequeAny()
    assert str(exinfo.value) == "no animal to deque"
