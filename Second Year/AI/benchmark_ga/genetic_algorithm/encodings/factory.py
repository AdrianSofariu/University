from .real_encoding import RealEncoding
from .binary_encoding import BinaryEncoding


def get_encoding_handler(config, x_bounds, y_bounds):
    """
    Factory function to return the appropriate encoding class instance
    using a dictionary-based switch instead of if-else.

    Args:
        config (dict): Dictionary containing Genetic Algorithm (GA) parameters.
                       Must include the key "encoding" with a value of either "real" or "binary".
        x_bounds (tuple): Tuple defining the lower and upper bounds of the x-domain.
        y_bounds (tuple): Tuple defining the lower and upper bounds of the y-domain.

    Returns:
        object: An instance of the appropriate encoding class (RealEncoding or BinaryEncoding).

    Raises:
        ValueError: If the "encoding" value in the config dictionary is not "real" or "binary".
    """
    switch = {
        "real": RealEncoding,
        "binary": BinaryEncoding,
    }
    encoding_class = switch.get(config["encoding"])
    if encoding_class is None:
        raise ValueError(f"Unknown encoding type: {config['encoding']}")
    return encoding_class(config, x_bounds, y_bounds)
