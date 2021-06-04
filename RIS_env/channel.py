# this file clarify the channel class used in /RIS_env/env.py
import numpy as np

class Channel():
    def __init__(self, Tx = None, Rx = None, fre = 28e9) -> None:
        pass
        self.Tx = Tx # the transmiter object
        self.Rx = Rx # the reciever object
        self.frequency = fre        # carrier frequency, Hz
        self.cluster_num = 1        # number of the clusters in the channel
        self.scatterer_num = []     # number of the scatterers in each cluster, list()
        self.subchannel_list = []   # list of the Subchannel class
        self.LoS_channel = None     # the LoS channel object

    def reset(self):
        # regenerate all subchannels
        self.cluster_num = 1


class Subchannel:
    def __init__(self, dis = 1) -> None:
        self.distance = dis     # distance between the transceivers, m

