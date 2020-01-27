import numpy as np
from nptdms import TdmsFile
import os
import matplotlib.pyplot as plt

user_input = input("Enter the path of your file:")

assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
print("Hooray we found your file!")

f_sample = input("Enter sampling rate in Hz:")
padValue= int(f_sample)

current = []
voltage = []

for file in os.listdir(user_input):
    if file.endswith(".tdms"):
        tdms_file_path = os.path.join(user_input, file)
        
        tdms_file = TdmsFile(tdms_file_path)
        tdms_file.group_channels('Untitled')
        channel_object = tdms_file.object('Untitled', 'Dev5/ai1')
        channel_object2 = tdms_file.object('Untitled', 'Dev5/ai0')
        
        i = channel_object2.data < 0
        i = i.astype(np.int)
        index_0_size = i.size - 1
        for x in range(1, index_0_size-1,1):
            if i[x] == 1 & i[x-1] == 0:
                if x < padValue:
                    i[1:x:1] = 1
                else:
                    i[x-padValue:x:1] = 1
        
        for x in range(index_0_size-1,1,-1):
            if i[x] == 1 & i[x+1] == 0:
                if x+padValue > index_0_size:
                    i[x:index_0_size:1] = 1
                else:
                    i[x:x+padValue:1] = 1
        c_temp = np.delete(channel_object2.data, i)
        v_temp = np.delete(channel_object.data, i)
        
        voltage = np.concatenate((voltage, v_temp), axis = 0)
        current = np.concatenate((current, c_temp), axis = 0)

#Now start massaging
#i = np.where(current < 0)

time = np.arange(0,current.size/int(f_sample),1/int(f_sample))
plt.plot(time, current)