# Python - Almost a circle

![Circle](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/331/giphy.mp4)

In this project, I developed three interconnected classes in Python to represent rectangles and squares. The project focused on object-oriented programming concepts, and I created a custom test suite using the `unittest` module to verify the functionality of each class.

The implementation of the project involved utilizing various Python tools and concepts, including:
- Importing modules
- Handling exceptions
- Working with private attributes
- Implementing getter and setter methods
- Utilizing class and static methods
- Applying inheritance
- Performing file I/O operations
- Using `args` and `kwargs` for flexible argument handling
- Serializing and deserializing objects to JSON and CSV formats
- Conducting unit testing with `unittest`

## Tests :heavy_check_mark:

* [tests/test_models](./tests/test_models): This folder contains independently developed test files for each class:
  * [test_base.py](./tests/test_models/test_base.py)
  * [test_rectangle.py](./tests/test_models/test_rectangle.py)
  * [test_square.py](./tests/test_models/test_square.py)

## Classes :cl:

### Base
Represents the base class for all other classes in the project. It includes the following features:

- Private class attribute: `__nb_objects = 0`
- Public instance attribute: `id`
- Class constructor: `def __init__(self, id=None)`
  - If `id` is `None`, it increments `__nb_objects` and assigns its value to the public instance attribute `id`.
  - Otherwise, it sets the public instance attribute `id` to the provided `id`.
- Static method: `def to_json_string(list_dictionaries)`
  - Returns the JSON string serialization of a list of dictionaries.
  - If `list_dictionaries` is `None` or empty, it returns the string `"[]"`.
- Class method: `def save_to_file(cls, list_objs)`
  - Writes the JSON serialization of a list of objects to a file.
  - The parameter `list_objs` should be a list of instances derived from the `Base` class.
  - If `list_objs` is `None`, it saves an empty list.
  - The file is saved with the name `<cls name>.json` (e.g., `Rectangle.json`).
  - If the file already exists, it overwrites the existing file.
- Static method: `def from_json_string(json_string)`
  - Returns a list of objects deserialized from a JSON string.
  - The parameter `json_string` should be a string representing a list of dictionaries.
  - If `json_string` is `None` or empty, it returns an empty list.
- Class method: `def create(cls, **dictionary)`
  - Instantiates an object with the attributes provided in `**dictionary`.
- Class method: `def load_from_file(cls)`
  - Returns a list of objects instantiated from a JSON file.
  - It reads from the JSON file `<cls name>.json` (e.g., `Rectangle.json`).
  - If the file does not exist, it returns an empty list.
- Class method: `def save_to_file_csv(cls, list_objs)`
  - Writes the CSV serialization of a list of objects to a file.
  - The parameter `list_objs` should be a list of instances derived from the `Base` class.
  - If `list_objs` is `None`, it saves an empty list.
  - The file is saved with the name `<cls name>.csv` (e.g., `Rectangle.csv`).
  - Objects are serialized in the format `<id>,<width>,<height>,<x>,<y>` for `Rectangle` objects and `<id>,<size>,<x>,<y>` for `Square` objects.
- Class method: `def load_from_file_csv(cls)`
  - Returns a list of objects instantiated from a CSV file.
  - It reads from the CSV file `<cls name>.csv` (e.g., `Rectangle.csv`).
  - If the file does not exist, it returns an empty list.
- Static method: `def draw(list_rectangles, list_squares)`
  - Draws `Rectangle` and `Square` instances in a GUI window using the `turtle` module.
  - The parameter `list_rectangles` should be a list of `Rectangle` objects to be drawn.
  - The parameter `list_squares` should be a list of `Square` objects to be drawn.

### Rectangle
Represents a rectangle and inherits from the `Base` class. It includes the following features:

- Private instance attributes: `__width`, `__height`, `__x`, and `__y`
  - Each private instance attribute has its own getter and setter methods.
- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None)`
  - Raises a `TypeError` exception with the message `<attribute> must be an integer` if `width`, `height`, `x`, or `y` is not an integer.
  - Raises a `ValueError` exception with the message `<attribute> must be > 0` if `width` or `height` is less than or equal to 0.
  - Raises a `ValueError` exception with the message `<attribute> must be >= 0` if `x` or `y` is less than 0.
- Public method: `def area(self)`
  - Returns the area of the `Rectangle` instance.
- Public method: `def display(self)`
  - Prints the `Rectangle` instance to the standard output using the `#` character.
  - Prints new lines for the `y` coordinate and spaces for the `x` coordinate.
- Overridden `__str__` method
  - Prints a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y>`.
- Public method: `def update(self, *args, **kwargs)`
  - Updates an instance of `Rectangle` with the given attributes.
  - `*args` must be supplied in the following order: `id`, `width`, `height`, `x`, `y`.
  - `**kwargs` is expected to be a double pointer to a dictionary of new key-value attributes to update the `Rectangle` with.
  - `**kwargs` is skipped if `*args` exists.
- Public method: `def to_dictionary(self)`
  - Returns the dictionary representation of a `Rectangle` instance.

### Square
Represents a square and inherits from the `Rectangle` class. It includes the following features:

- Class constructor: `def __init__(self, size, x=0, y=0, id=None)`
  - Assigns the `width` and `height` attributes of the `Rectangle` superclass using the `size` value.
- Overridden `__str__` method
  - Prints a `Square` instance in the format `[Square] (<id>) <x>/<y>`.
- Public method: `def update(self, *args, **kwargs)`
  - Updates an instance of `Square` with the given attributes.
  - `*args` must be supplied in the following order: `id`, `size`, `x`, `y`.
  - `**kwargs` is expected to be a double pointer to a dictionary of new key-value attributes to update the `Square` with.
  - `**kwargs` is skipped if `*args` exists.
- Public method: `def to_dictionary(self)`
  - Returns the dictionary representation of a `Square` instance.
