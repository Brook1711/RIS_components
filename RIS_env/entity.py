# this file clarify the transceiver and RIS class used in /RIS_env/env.py
import numpy as np

class Transceiver:
    type = 'Tx'     # 'Tx' or 'Rx'
    position = np.array([0, 0, 0]) # the coordinate of the entity, np.array(), shape: 1 X 3
