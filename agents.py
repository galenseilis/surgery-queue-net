import numpy as np
import queueing_tool as qt


class Surgery(qt.Agent):
    '''Surgery''' 

    def __init__(self):
        super().__init__()

        self.benchmark = np.random.randint(0,6)
        self.gender = np.random.choice(['Male', 'Female', 'Other'])
        self.surgery_type = np.random.choice(
            [
                'Laparoscopy',
                'Appendectomy',
                'Cesarian section'
                ]
            )

    def __repr__(self):
        return f"Surgery({self.agent_id})"

    def __lt__(self, other):
        return self._time + self.benchmark < other._time + other.benchmark

    def __gt__(self, other):
        return self._time + self.benchmark > other._time + other.benchmark

    def __eq__(self, other):
        return self._time + self.benchmark == other._time + other.benchmark

    def __le__(self, other):
        return self._time + self.benchmark <= other._time + other.benchmark

    def __ge__(self, other):
        return self._time + self.benchmark >= other._time + other.benchmark
