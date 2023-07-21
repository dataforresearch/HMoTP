# -*- coding: utf-8 -*-
"""
Created on 2023/05/27

@author: R. Wang @SDU 
"""
import numpy as np
import scipy.stats
from WaveletPacketEnergy import WaveletPacketEnergy

    
def exfeature(signal_, Fs=5000):
    '''

    Parameters
    ----------
    signal_ : TYPE
        the orginal cutting signal.
    Fs : TYPE
        sampling frequency. The default is 5000.

    Returns
    -------
    f_mat : TYPE
        feature matrix.

    '''
    N = len(signal_)
    y = signal_
    # # time domain features
    t_mean_1 = np.mean(y)                                    # 1 average
    t_max_2 = np.max(y)                                     # 2 max
    t_std_3  = np.std(y, ddof=1)                             # 3 standard deviation
    t_fgf_4  = ((np.mean(np.sqrt(np.abs(y)))))**2           
    t_rms_5  = np.sqrt((np.mean(y**2)))                      # 5 RMS
    t_pp_6   = 0.5*(np.max(y)-np.min(y))                     
    t_skew_7   = scipy.stats.skew(y)                         # 7 skewness
    t_kur_8 = scipy.stats.kurtosis(y)                        # 8  Kurtosis
    t_cres_9  = np.max(np.abs(y))/t_rms_5                    # 9 Crest Factor
    t_clear_10  = np.max(np.abs(y))/t_fgf_4                   # 10  Clearance Factor
    t_shape_11 = (N * t_rms_5)/(np.sum(np.abs(y)))           # 11 Shape fator
    t_imp_12  = ( np.max(np.abs(y)))/(np.mean(np.abs(y)))    # 12 Impulse Fator
    # # frequency domain features（f_13:f_24）
    L = len(signal_) 
    PL = abs(np.fft.fft(signal_ / L))[: int(L / 2)]
    PL[0] = 0
    f = np.fft.fftfreq(L, 1 /Fs)[: int(L / 2)]
    x = f
    y = PL
    K = len(y)
    f_13 = np.mean(y)
    f_14 = np.var(y)
    f_15 = (np.sum((y - f_13)**3))/(K * ((np.sqrt(f_14))**3))
    f_16 = (np.sum((y - f_13)**4))/(K * ((f_14)**2))
    f_17 = (np.sum(x * y))/(np.sum(y))
    f_18 = np.sqrt((np.mean(((x- f_17)**2)*(y))))
    f_19 = np.sqrt((np.sum((x**2)*y))/(np.sum(y)))
    f_20 = np.sqrt((np.sum((x**4)*y))/(np.sum((x**2)*y)))
    f_21 = (np.sum((x**2)*y))/(np.sqrt((np.sum(y))*(np.sum((x**4)*y))))
    f_22 = f_18/f_17
    f_23 = (np.sum(((x - f_17)**3)*y))/(K * (f_18**3))
    f_24 = (np.sum(((x - f_17)**4)*y))/(K * (f_18**4))
    f_25 = WaveletPacketEnergy(signal_,3)[0] #3-layer WaveletPacket
    f_26 = WaveletPacketEnergy(signal_,3)[1]
    f_27 = WaveletPacketEnergy(signal_,3)[2]
    f_28 = WaveletPacketEnergy(signal_,3)[3]
    f_29 = WaveletPacketEnergy(signal_,3)[4]
    f_30 = WaveletPacketEnergy(signal_,3)[5]
    f_31 = WaveletPacketEnergy(signal_,3)[6]
    f_32 = WaveletPacketEnergy(signal_,3)[7]
    f_mat = np.array([t_mean_1,t_max_2, t_std_3, t_fgf_4, t_rms_5, t_pp_6,
                      t_skew_7,   t_kur_8,  t_cres_9,  t_clear_10, t_shape_11, t_imp_12,
                      f_13, f_14, f_15, f_16, f_17, f_18, f_19, f_20, f_21, f_22, f_23, f_24,
                      f_25,f_26,f_27,f_28,f_29,f_30,f_31,f_32])
    return f_mat

    