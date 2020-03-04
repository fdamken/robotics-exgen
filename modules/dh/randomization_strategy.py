import random
from typing import List, Optional, Tuple



class DhRandomizationStrategy:
    def __init__(self,
                 possible_thetas: Optional[List[str]] = None,
                 possible_alphas: Optional[List[str]] = None,
                 nonzero_d_probability: float = 0.25,
                 nonzero_a_probability: float = 0.25,
                 revolute_joint_probability: float = 0.5):
        if possible_thetas is None:
            possible_thetas = ['-Pi/2', 'Pi/2', 'Pi', None]
        if possible_alphas is None:
            possible_alphas = ['-Pi/2', 'Pi/2', 'Pi', None]

        self._possible_thetas = possible_thetas
        self._possible_alphas = possible_alphas
        self._nonzero_d_probability = nonzero_d_probability
        self._nonzero_a_probability = nonzero_a_probability
        self._revolute_joint_probability = revolute_joint_probability


    def draw_theta(self) -> str:
        return random.choice(self._possible_thetas)


    def draw_alpha(self) -> str:
        return random.choice(self._possible_alphas)


    def draw_d(self, link_length_index: int) -> Tuple[int, Optional[str]]:
        if random.random() < self._nonzero_d_probability:
            return link_length_index + 1, ('l_' + str(link_length_index))
        return link_length_index, None


    def draw_a(self, link_length_index: int) -> Tuple[int, Optional[str]]:
        if random.random() < self._nonzero_a_probability:
            return link_length_index + 1, ('l_' + str(link_length_index))
        return link_length_index, None


    def draw_rho(self):
        return 1 if random.random() < self._revolute_joint_probability else 0
