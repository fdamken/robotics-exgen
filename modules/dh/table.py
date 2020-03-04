from typing import List, Optional, Union

from tabulate import tabulate

from modules.dh.joint_data import DhJointData
from modules.dh.randomization_strategy import DhRandomizationStrategy



class DhTable:
    _no_joints: int
    _joints: List[DhJointData]


    def __init__(self, no_joints: int):
        """
        Initializes a new DH-table.

        :param no_joints: The number of joints.
        :param joints: The joint data to be set.
        """

        self._no_joints = no_joints
        # This has to be initialized with set_joints(..) or generate_random_joints(..).
        self._joints = []


    def __str__(self) -> str:
        data = []
        for it_joint in self._joints:
            data.append((it_joint.get_index(),
                         it_joint.get_theta_str(),
                         it_joint.get_d_str(),
                         it_joint.get_alpha_str(),
                         it_joint.get_a_str()))
        return tabulate(data, headers = ('i', 'θ_i', 'd_i', 'α_i', 'a_i'), colalign = ('center',), tablefmt = 'orgtbl')


    def __repr__(self) -> str:
        return "(_no_joints, _joints): (%d, %s)" % (self._no_joints, repr(self._joints))


    def generate_random_joints(self, randomization_strategies: Optional[Union[DhRandomizationStrategy, List[DhRandomizationStrategy]]] = None):
        """
        Generates random joints.
        """

        if not randomization_strategies:
            randomization_strategies = DhRandomizationStrategy()

        self._joints = []
        link_length_index = 1
        for it_i in range(0, self._no_joints):
            if type(randomization_strategies) == list:
                randomization_strategy = randomization_strategies[it_i]
            else:
                randomization_strategy = randomization_strategies

            theta = randomization_strategy.draw_theta()
            (link_length_index, d) = randomization_strategy.draw_d(link_length_index)
            alpha = randomization_strategy.draw_alpha()
            (link_length_index, a) = randomization_strategy.draw_a(link_length_index)
            rho = randomization_strategies.draw_rho()

            self._joints.append(DhJointData(it_i + 1, theta, d, alpha, a, rho))


    def get_joints(self) -> List[DhJointData]:
        return self._joints.copy()


    def set_joints(self, joints: List[DhJointData] = None):
        self._joints = joints
