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
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

list0 = ["Mary", "Louis", "Molly", "Dhruv"]
print("LIST0: " +str(list0))
list1 = list0.insert(0, "Not_Mary")
print("LIST1: " +str(list1))
list2 = list0.remove("Molly")
print("LIST2: " + str(list2))
list3 = list0.sort()
print("LIST3: " + str(list3))
print("LIST0: " + str(list0))
