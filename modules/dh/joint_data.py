class DhJointData:
    def __init__(self, index: int, theta: str, d: str, alpha: str, a: str, rho: int):
        """
        Initializes a new DH-table entry.

        The string constants should be something like ``'Pi'``, ``'Pi/2'`` or ``l``. Do not insert variables like ``'q'`` here!
        instead, use the `rho` parameter to specify whether the joint is a revolute or prismatic joint.

        :param index: Index of this joint.
        :param theta: The theta parameter (constant).
        :param d: The d parameter (constant).
        :param alpha: The alpha parameter.
        :param a: The a parameter.
        :param rho: Type of this joint (1 = revolute, 0 = prismatic).
        """

        self._index = index
        self._theta = theta
        self._d = d
        self._alpha = alpha
        self._a = a
        self._rho = rho


    def __str__(self) -> str:
        return "theta: %s, d: %s, alpha: %s, a: %s" % (
                self.get_theta_str(), self.get_d_str(), self.get_alpha_str(), self.get_a_str())


    def __repr__(self) -> str:
        return "(_index, _theta, _d, _alpha, _a, _rho): (%d, %s, %s, %s, %s, %d)" % (
                self._index, self._theta, self._d, self._alpha, self._a, self._rho)


    def get_index(self) -> int:
        return self._index


    def get_theta_str(self) -> str:
        if self._rho == 1:
            if self._theta:
                return "%s + q_%d" % (self._theta, self._index)
            return "q_%d" % self._index
        return self._theta if self._theta else '0'


    def get_d_str(self) -> str:
        if self._rho == 0:
            if self._d:
                return "%s + q_%d" % (self._d, self._index)
            return "q_%d" % self._index
        return self._d if self._d else '0'


    def get_alpha_str(self) -> str:
        return self._alpha if self._alpha else '0'


    def get_a_str(self) -> str:
        return self._a if self._a else '0'
