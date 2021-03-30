#!/usr/bin/env python3

list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

print(list1)

print(list1[1])

for i in list1:
    print(i +", ")

complexList = [["Anthony", "John"],["D", "R"],["Johnson", "James"]]

for i in range(len(complexList)-1):
    for j in range(len(complexList)):
        print(complexList[j][i])


        
