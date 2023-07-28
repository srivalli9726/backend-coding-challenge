from dataclasses import field

from marshmallow_dataclass import dataclass


@dataclass
class Suggestions:
    q: str
    lat: float = field(default=None)
    lng: float = field(default=None)
