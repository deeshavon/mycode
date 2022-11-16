#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
proto.sort(proto2) #this line will HOPEFULLY sort the data that includes the appended data in protoa after

protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
#proto.sort(proto2) #this line will HOPEFULLY sort the data that includes the appended data in protoa after
#print(proto)

