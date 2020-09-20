# Disturbia

Library for set of simple methods regarding distribution.

## Installation

```bash
pip install disturbia
```

## Usage

### Distribute

It returns the objects in the number of times they are specified, in a random order.

It uses Python's generator technique to save memory.

```python
from disturbia import distribute

distribution = distribute([
    ('six', 6),
    ('five', 5)
])

list(distribute) # will contain 'six' six times and 'five' five times in a random order.
```

## Development

### Testing

Tests are written using `pytest` and can be found in `tests/` directory.

Tests can be run using:

```bash
pytest
```

### Development

This package is distributed on PyPI.

To deploy a new version, update the version and then run:

```bash
python setup.py sdist bdist_wheel

twine upload dist/*
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
