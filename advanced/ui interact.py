from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

def n(x):
    return x
interact(n, x =20);
interact(n, x =True);
interact(n, x ="Hello, Mutellip");

@interact(x = True, y = 1.0)
def g(x,y):
    return (x, y)
def h(p, q):
    return (p, q)
interact(h, p=5, q =fixed(20));

IntSlider(min=-10,max=30,step=1,value=10)
interact(f, x=widgets.IntSlider(min=-10,max=30,step=1,value=10));
