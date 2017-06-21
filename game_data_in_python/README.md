# Leverage Python Objects for Happier Development
A friend learning Python was building an RPG a while back.
Using dictionaries and lists for all the game data was causing him some grief,
so I wrote this small post (originally a gist) to illustrate how Python's objects
can be customized for handling data for a basic text-based RPG.

## Basic idea with a dict

```python
p = {
        'name': 'Ystr',
        'age': 119,
        'skills': ['spamming', 'egging']
    }
print(p['name']) # => Ystr
print(p['skills'][1]) # => egging
```

## Basic idea with a very simple class
The `__init__()` method tells Python how the object's **constructor** should behave.
In the code below, the **object** `p` is an **instance** of the **class** `Person`.
When we use `Person()` as if it were a function, we're really doing this:

1. Create a new object with all of the methods defined for the class `Person`.
2. Call the `__init__` method - the **constructor method** - of this new object.

*(Someone who knows more of the proper theory on OOP feel free to fix me where I'm fudging a bit.)*

```python
class Person(object):
    def __init__(name, age, *args):
        self.name = name
        self.age = age
        self.skills = args

p = Person('Ystr', 119, 'spamming', 'egging')

print("Name: {}".format(p.name))
print("Age: {}".format(p.age))

print("Skills:")
for skill in skills:
    print("\t{}".format(skill))
```

## Baking in printing
You can let Python know how to print your object by defining the `__str__()` method.

```python
class Person(object):
    def __init__(self, name, age, *args):
        self.name = name
        self.age = age
        self.skills = args

    def __str__(self):
        out = [
            'Name:\t{}'.format(self.name),
            'Age:\t{}'.format(self.age),
            'Skills:'
            ]
        skills = ['\t{}'.format(skill) for skill in self.skills]
        return '\n'.join(out + skills)

p = Person('Ystr', 119, 'spamming', 'egging')
print(p)
```

## Polymorphic constructors
Obviously, it's not convenient to manually create every single Person in your game.
You might have a number of ways that you wish to create a new NPC or player.
When testing in your interpreter (IDLE,) the above functionality is probably sufficient.
However, it's a real pain to keep typing in `Person('Ystr', 119, 'spamming', 'egging')`.
What if we wanted to create a `Person` from data that the game has already stored in a dict?
What if the game needs to load data for many villagers from a file when it starts up?

[JSON data](http://json.org/) looks an awful lot like Python dictionaries,
and it's pretty easy to [convert](https://docs.python.org/3/library/json.html) JSON to and from Python lists and dictionaries.

Earlier, we expressed Ystr as a Python dictionary.
Here's how the equivalent JSON string (which we can store in the file `ystr.json`) would look:

```json
{
    "name": "Ystr",
    "age": 119,
    "skills": ["spamming", "egging"]
}
```

Note that double-quotes were required for the JSON, whereas Python could use double or single.
Now, let's update our class definition to do the following:
- Create a `Person` from a `dict`
- Create a `Person` from JSON
- Store the attributes of a `Person` as a `dict`
- Store the attributes of a `Person` as JSON

```python
#!/usr/bin/env python
import json

class Person(object):
    def __init__(self, name, age, *args):
        self.name = name
        self.age = age
        self.skills = args

    def __str__(self):
        out = [
            'Name:\t{}'.format(self.name),
            'Age:\t{}'.format(self.age),
            'Skills:'
            ]
        skills = ['\t{}'.format(skill) for skill in self.skills]
        return '\n'.join(out + skills)

    @classmethod
    def from_dict(cls, d):
        name = str(d['name'])
        age = d['age']
        skills = [str(skill) for skill in d['skills']]
        return cls(name, age, *skills)

    @classmethod
    def from_JSON(cls, fp):
        """Read from JSON-format file-like object"""
        j = json.load(fp)
        return cls.from_dict(j)

    def to_dict(self):
        """Could use self.__dict__, but whatevs"""
        d = {}
        d['name'] = self.name
        d['age'] = self.age
        d['skills'] = self.skills
        return d

    def to_JSON(self):
        return json.dumps(self.to_dict())

if __name__ == '__main__':
    with open('ystr.json', 'r') as j:
        ystr = Person.from_JSON(j)

    print(ystr)
    print(ystr.to_dict())
    print(ystr.to_JSON())

    # Happy birthday, Ystr!
    ystr.age += 1
    with open('ystr.json', 'w') as f:
        json.dump(ystr.to_dict(), f)
```

Note that the `json` module defines functions `load`, `loads`, `dump`, and `dumps`.
The "s" version of each function denotes that it's operating on **s**trings.
That is, `load` loads from a file-like object,
whereas `loads` loads from a JSON-formatted string.
Similarly, `dump` writes to a file,
whereas `dumps` returns a string.
Here's a quick illustration you can play around with.
```python
filename = 'ystr.json'
with open(filename, 'r') as f:
    # j will be a dict, not a string
    j = json.load(f)

# Dump dictionary to a JSON-formatted string
j_dumped = json.dumps(j)
# Get a dictionary from the JSON-formatted string
a_copy_of_j = json.loads(j_dumped)

# Dump the dictionary to a JSON-formatted file
with open(filename, 'w') as f:
    json.dump(a_copy_of_j, f)
```

## What are all these weird `__methods__()`, anyway?
Nothing crazy.
Read up on Python's [descriptor protocol](https://docs.python.org/3/howto/descriptor.html?highlight=descriptor%20protocol)
to get a better idea of how parts of the language are implemented.

## Other stuff
Soon!
