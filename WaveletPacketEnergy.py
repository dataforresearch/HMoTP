# -*- coding: utf-8 -*-
"""
Created on 2023/05/27

@author: Runqiong Wang @SDU
"""

import numpy as np
import pywt
import pywt.data


def WaveletPacketEnergy(inputsignal,level):
    wp = pywt.WaveletPacket(data=inputsignal, wavelet='db1',mode='symmetric',maxlevel=level)
    energy = [] #energy of ‘level’ layer
    for i in [node.path for node in wp.get_level(level, 'freq')]:
        re=(wp[i].data) #Decomposition coefficient for the ith node of the LEVEL layer
        energy.append(pow(np.linalg.norm(re,ord=None),2))
    return energy


    