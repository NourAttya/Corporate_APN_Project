#txt = "apple#banana#cherry#orange"
#x = txt.split("#")[0]
#print (x)

#a = [0, 1, 2, 3]
#for i in a:

 #   print ('loopback'+str(i))
import numpy    as np

a = [1,2,3,4,5,6]
b = [1,4,5]

c = np.in1d(a,b)
print(c)

IPs= [1,2]
for i in range(len(IPs)):
    if i>0:
        print(i)