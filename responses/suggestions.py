from marshmallow_dataclass import dataclass


@dataclass
class Suggestions:
    name: str
    latitude: float
    longitude: float
    score: float


@dataclass
class SuggestionsResponse:
    suggestions: list[Suggestions]
