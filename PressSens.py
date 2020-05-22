#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datalogger import *

# Gets a response from the Motors
def getDataPfeiffer():
    PfLog.getCtrlResponse()
    # PfLog.dre.command_rx_buf
    resp2 = PfLog.dre.command_rx_str
    splitresp = resp2.split(',')  # Splits the string into groups
    status1 = int(splitresp[0].strip())  # Removes whitespaces and assign to status of first channel
    value1 = float(splitresp[1].strip())  # Removes whitespaces and assign to value of first channel
    status2 = int(splitresp[2].strip())  # Removes whitespaces and assign to status of second channel
    value2 = float(splitresp[3].strip())  # Removes whitespaces and assign to value of second channel
    return status1, value1, status2, value2


# In[ ]:


serport = serial.Serial(
        port=config.cte_serial_port,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        rtscts=False,
        dsrdtr=False,
        xonxoff=True
    )
if config.cte_verbose:
    print("Chosen serial port: " + config.cte_serial_port)
datalogger(serport,getDataPfeiffer,rm_cat_press1,rm_cat_press2,"press")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



