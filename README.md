# ID Number Generator

This Python script generates valid ID numbers based on certain rules. It includes functions to check the validity of an ID, to generate the next valid ID, and a class to iterate over valid ID numbers.

## Table of Contents
- [Description](#description)
- [Usage](#usage)
- [Functions](#functions)
- [Classes](#classes)
- [Dependencies](#dependencies)
- [License](#license)

## Description

The script provides functionalities to generate and iterate over valid ID numbers. It includes a function `chek_id_valid` to check the validity of an ID number according to specific rules, a generator function `id_generator` to generate the next valid ID, and a class `IDIterator` to iterate over valid ID numbers.

## Usage

1. Run the script.
2. Input an initial ID number.
3. Choose between generating IDs (`gen`) or iterating over IDs (`it`).
4. The script will output the next 10 valid IDs.

## Functions

### `chek_id_valid(id_number)`

- Description: Checks the validity of an ID number based on specific rules.
- Parameters:
  - `id_number`: The ID digits to be checked.
- Returns:
  - `True` if the ID is valid, `False` otherwise.

### `id_generator(id_number)`

- Description: Generates the next valid ID number.
- Parameters:
  - `id_number`: The initial ID number.
- Yields:
  - The next valid ID number.

## Classes

### `IDIterator`

- Description: A class to iterate over valid ID numbers.
- Methods:
  - `__init__(self, id=99999999)`: Initializes the IDIterator object with an initial ID.
  - `__iter__(self)`: Returns an iterator object.
  - `__next__(self)`: Generates the next valid ID number.
  
## Dependencies

- This script does not have any external dependencies.


