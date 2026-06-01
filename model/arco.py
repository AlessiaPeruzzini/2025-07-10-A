from dataclasses import dataclass

from model.products import Product


@dataclass
class Arco:
    p1: Product
    p2: Product
    peso: int
