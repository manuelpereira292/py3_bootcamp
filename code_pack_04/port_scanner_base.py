#!/usr/bin/env python
# coding: utf-8

# # Port Scanner
# ## Training RUMOS
# 

# This is Already Done!


import socket

def conn_scan(host, port):
    print('[*] Scanning port {}'.format(port), end='')
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.send(b'KNOK...KNOK\r\n')
            data = s.recv(1024)
        print(' ... open')
        #print(data)
    except:
        print(' ... close')


# Start Here! 
# 
# make sure this happens
# 
# [*] Scanning host 185.240.248.25  
# [*] Scanning port 22 ... open  
# [*] Scanning port 23 ... close  
# [*] Scanning port 80 ... open  
# 


def port_scan(host, ports):
    print("[+] Scanning host {}".format(host))
    #print(type(ports)) # <class 'list'>
    
    for port in ports:
        conn_scan(host, port)

if __name__ == '__main__':
    hosts='185.240.248.25'
    ports = [22, 80, 143]
    port_scan(hosts, ports)
