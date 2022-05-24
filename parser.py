#!/usr/bin/env python3

import sys
import re
from tabulate import tabulate 

def auth_parser(file):

    ip = []

    for line in file:
           
        trash = 0 

        pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        ip_match = pattern.search(line)
    
        if ip_match is None:
            trash += 1

        else:
            ip_string = ip_match.group(0)
            ip.append(ip_string)

    #print(ip)
    counted = []
    final_list = []
    total_sum = 0

    for each in ip:
        if each not in counted:
            counted.append(each)
            inner_list = []
            count = ip.count(each)
            total_sum += count
            inner_list.append(count)
            inner_list.append(each)
            final_list.append(inner_list)
    #print(final_list)

    for each in final_list:
        percent = (each[0] / total_sum) * 100
        each.insert(0,percent)

    #print(final_list)
    final_list.sort(key=lambda x: x[1])
    
    print(tabulate(final_list, headers=["percentage","count","ip address"]))
     


def main():
    file_name = sys.argv[1]
    with open(file_name) as file_name:
    
        auth_parser(file_name)

 
if __name__ == "__main__":
 main()
