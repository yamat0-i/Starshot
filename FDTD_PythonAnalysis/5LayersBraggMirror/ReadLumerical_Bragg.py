#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 19:02:37 2022

@author: mark
"""

import numpy as np

# Switch
debug = True

def ReadLumericalDataFile2D(fname):
    x = np.array([])
    y = np.array([])
    data = []
    with open("5LayersBraggMirror_cSi_0.3-1.5um_v3.dat") as f:
        
        # Read header 
        headerlen = 2
        for ll in np.arange(headerlen):
            check = f.readline()
            if debug:
                print(ll)
                print(check)
                
        # Get x values
        # Read and discard x label
        label = f.readline()
        if debug:
            print(label)
        xread = True
        ll = 0
        while xread:
            xstr = f.readline()
            if debug:
                print(ll)
                print(xstr)
                print(xstr=='\n')
            if xstr=='\n':
                print("End of x block")
                xread = False
            else:
                if debug:
                    print("Will append %f"%float(xstr))
                x = np.append(x,float(xstr)) 
                if debug:
                    print("Length of x")
                    print(len(x))
            ll += 1
        if debug:
            print("x is")
            print(x)
        
        # Get y values
        # Read and discard y label
        label = f.readline()
        if debug:
            print(label)
        yread = True
        ll = 0
        while yread:
            ystr = f.readline()
            if debug:
                print(ll)
                print(ystr)
                print(ystr=='\n')
            if ystr=='\n':
                print("End of y block")
                yread = False
            else:
                if debug:
                    print("Will append %f"%float(ystr))
                y = np.append(y,float(ystr)) 
                if debug:
                    print("Length of y")
                    print(len(y))
            ll += 1
        if debug:
            print("y is")
            print(y)        
            
        # Read in data    
        nx = len(x)
        ny = len(y)
        print("nx=%d"%nx)
        print("ny=%d"%ny)
            
        # Read and discard data header
        label = f.readline()
        if debug:
            print(label)
        data = np.zeros((nx,ny)) 
        dataread = True
        ll = 0
        while dataread:
            if debug:
                print(ll)
            datastr = f.readline()
            #if debug:
            #    print(datastr)
            if datastr == '\n':
                dataread = False
            else:
                column = [float(i) for i in datastr[1:].split(' ')]
                #if debug:
                #    print(column)
                #    print(len(column))
                data[ll,:] = column
            ll+=1
        print("Data read in finished.")
        if debug:
            print(data)
    
    return x,y,data