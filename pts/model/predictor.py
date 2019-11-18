from abc import ABC, abstractmethod
from typing import Iterator

from pts.dataset import Dataset

from .forecast import Forecast


class Predictor(ABC):
    def __init__(self, prediction_length: int, freq: str) -> None:
        self.prediction_length = prediction_length
        self.freq = freq

    @abstractmethod
    def predict(self, dataset: Dataset, **kwargs) -> Iterator[Forecast]:
        pass
