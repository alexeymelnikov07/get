import mcp3021 as mcp
import time
adc = mcp.MCP3021(5.18,False)
a=[]
T0=time.time()
for i in range (100):
    a.append(adc.get_voltage())

print(time.time()-T0)