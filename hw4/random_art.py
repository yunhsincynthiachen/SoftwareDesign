# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: yunhsincynthiachen
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
import math

def build_random_function(min_depth, max_depth):
    # build_random_function will build random functions by randomly choosing a number, indexed to 
    # a certain function (prod,cos_pi, sin_pi, squared, mean, x and y), in order to pass in
    # to evaluate_random_function, which will make mathematical functions that are solveable

    variablelist = [["x"],["y"]]
    if max_depth <=1:
        return variablelist[randint(0,1)]
        
    a = build_random_function(min_depth-1,max_depth-1)
    b = build_random_function(min_depth-1,max_depth-1)
    
    prod = ["prod",a,b]
    cos_pi = ["cos_pi",a]
    sin_pi = ["sin_pi",a]
    squared = ["**2",a]
    mean = ["mean",a,b]
    x = a
    y = b
    
    randfunclist = [prod,cos_pi,sin_pi,squared,mean,x,y]
    
    if min_depth > 1:
        return randfunclist[randint(0,4)]
    if min_depth <= 1:
        return randfunclist[randint(0,6)]
   
        
def evaluate_random_function(f, x, y):
    # list that represents a function needs to be made into a mathematical function that is 
    # solveable
    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y
    elif f[0] == "prod":
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    elif f[0] == "cos_pi":
        return math.cos(math.pi*evaluate_random_function(f[1],x,y))
    elif f[0] == "sin_pi":
        return math.sin(math.pi*evaluate_random_function(f[1],x,y))
    elif f[0] == "**2":
        return (evaluate_random_function(f[1],x,y))**2
    elif f[0] == "mean":
        return ((evaluate_random_function(f[1],x,y))+evaluate_random_function(f[2],x,y))/2
    


def make_art():
    # in make_art(), red, green and blue will be created with build_random_functions that take in 
    # minimum and maximum depths, and then provide certain pixels and turn them into a certain range
    # that will be created into integers that create red, green and blue colors that will be 
    # taken into as pixels
    
    r = build_random_function(4,7)
    g = build_random_function(3,12)
    b = build_random_function(5,9)

    
    im = Image.new("RGB",(1600,900))
    pix = im.load() 
    
    for x in range(1600):
        for y in range(900):
            xscale = (x/(1600/2.0))- 1
            yscale = (y/(900/2.0))- 1
            red = evaluate_random_function(r,xscale,yscale)
            green = evaluate_random_function(g,xscale,yscale)
            blue = evaluate_random_function(b,xscale,yscale)
            redscale = (red + 1)*(255/2.0)
            greenscale = (green + 1)*(255/2.0)
            bluescale = (blue + 1)*(255/2.0) 
            redd = int(redscale)
            greenn = int(greenscale)
            bluee = int(bluescale)
            pix[x,y] = (redd,greenn,bluee)
    im.save('awesomepic10.png')
    im.show()

if __name__ == '__main__':
    print make_art()    