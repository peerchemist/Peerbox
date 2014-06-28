#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import glob
import os

## target device gcc -dumpmachine

host_prefix="armv6l-unknown-linux-gnueabihf-"

## this device's gcc -dumpmachine

slave_prefix="arm-linux-gnueabihf-"

## remove all present sym links

os.system("find . -maxdepth 1 -type l -exec rm -f {} \;")

## list all files in this dir

files = glob("*")

## Make link from slave_prefix to host_prefix

def slave_to_host(i):
    
    slave = i.replace(slave_prefix, host_prefix)
        
    link = "ln -s {0} {1}".format(i, slave)
        
    return link
    

## Link slave prefix to generic name (g++, gcc...)

def host_to_generic(i):

    g = i.replace(slave_prefix, "")
    
    link = "ln -s {0} {1}".format(i, g)         
    
    return link 



def linkit(i):
    
    if slave_prefix in i:
    
        link = slave_to_host(i)
    
        print "LINKING: slave to host: {0} to {1}".format(i, link)
        
        os.system(link)

        link = host_to_generic(i)
        
        print "LINKING: host to generic: {0} to {1}".format(i, link)
        
        os.system(link)
        
    else:
        pass
    

for i in files:

    linkit(i)
    
    
    
## add some special links

# g++ to c++

g = slave_prefix + "g++"

c = slave_prefix + "c++"

print "LINKING: {0} to {1}".format(g, c)

link = "ln -s {0} {1}".format(g, c)

os.system(link)


# gcc-4.*.* to gcc

gcc = slave_prefix + "gcc"

print "LINKING: {0}gcc-4.* {1}".format(slave_prefix, gcc)

link = "ln -s {0}gcc-4.8.3 {1}".format(slave_prefix, gcc)

os.system(link)


# ld.bfd to ld

ldbfd = slave_prefix + "ld.bfd"

ld = slave_prefix + "ld"

print "LINKING: {0} to {1}".format(ldbfd, ld)

link = "ln -s {0} {1}".format(ldbfd, ld)

os.system(link)



    
    
