# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 13:57:39 2019

@author: Shibani Abhyankar
Purpose: Set up class for MFCC - Mel Frequency ceptsrum coeffiecients

"""
import matplotlib.pyplot as mlplt         # Helps with ploting images
import numpy as np                       # Basic array functionalities
from scipy.signal import get_window      # window generations 

class MFCC_Features(object):        
    
    def find_next_pow_2(self,x):
        if (x<0):
            return 0
        power =1
        while(power<x):
            power=power*2
        return power    
      
    
    def plot_figure(self,input,istime):
        if(istime):
            # time domain plot
            time_slots = np.linspace(0,len(input)/self.sampling_frequency,len(input))
            mlplt.figure(1)
            mlplt.title('Time Domain Signal')
            mlplt.plot(time_slots, input)
            mlplt.show()
        else:
            freq_slots = 1
            
    def GetwindowedBuffers(self,input):
        window_hamming = get_window(self.window_type,self.window_length)
        num_windows =len(input)/(self.window_length - self.window_shift)
        
        buffer_sig = np.zeros(shape=(num_windows,self.fftlength))
        index=0;
        for k  in range(0,len(input) -self.window_length,self.window_shift):
            win_sig = np.multiply(window_hamming,input[k : k +self.window_length])
            buffer_sig[index,0:self.window_length] = win_sig
            index = index + 1
        return buffer_sig
        

    def __init__(self, window_type,window_size,window_shift,sampling_frequency):
        self.window_type = window_type
        self.window_shift = int(window_shift * sampling_frequency)
        self.window_length = int(window_size * sampling_frequency)
        self.sampling_frequency = sampling_frequency
        self.fftlength = self.find_next_pow_2(self.window_length)
        self.number_of_filterbanks =23
        low_range =300
        if sampling_frequency>8000:
           high_range = 8000
        else:
            high_range =4000
        self.frequency_range =[low_range ,high_range]
        
    
    def getMelFrequency(self,f_range):
        mel_result = np.zeros(len(f_range))
        for freq in range(0,len(f_range)):
            mel_result[freq] = 1125 * np.log(1 + f_range[freq] /700)
        return mel_result

    def getHzFrequency(self,m_range):
        Hz_result = np.zeros(len(m_range))
        for mel in m_range:
            Hz_result[mel] = 700 * (np.exp(m_range[mel]/1125)-1)
        return Hz_result
    
    
    
    def generateMelFilterbank(self):
        mel_frequency_range = self.getMelFrequency(self.frequency_range)
        
        step_size = np.floor((mel_frequency_range[1] - mel_frequency_range[0]) /self.number_of_filterbanks)
        mel_steps = np.range(mel_frequency_range[0],mel_frequency_range[1],step_size)
        
        
        
        
    def extract_mfcc_features(self,input):
        windowed_input_buffers = self.GetwindowedBuffers(input)
        
        


