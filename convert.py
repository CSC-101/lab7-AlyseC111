from typing import Optional

def str_to_float(string: str) -> Optional[float]:
    try:
        if "." in string:
            return float(string)
    except TypeError:
        return None