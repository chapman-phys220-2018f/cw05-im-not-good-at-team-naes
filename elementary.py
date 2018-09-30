#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Royal Cuevas
# 2285562
# cueva114@mail.chapman.edu
# PHYS220 Fall 2018
# CW 05

import numpy as np
import scipy.constants as const


class Particle(object):
    mass = 12
    position = (3.0, 10.0, 20.0)
    momentum = (40.0, 50.0, 0.60)
    
    def __init__(self, x, y ,z):
        """Class constructor
        
        Sets initial values for 3 attributes.
        Requires a floating point triple as an
        arguement for the starting position of the particle"""
        
        self.position = (x, y ,z)
        self.mass = 1.0
        self.momentum = (0.0, 0.0, 0.0)
        
    def impulse(self, px, py, pz):
        """Alters the momentum by the impulse amount.
        Requires floating point triple to set impulse
        value."""
        print(self.momentum)
        self.momentum = tuple(np.add(self.momentum, (px, py, pz)))
        print(self.momentum)
        
    def move(self, dt):
        """Moves particle by one dt.
        Requires time unit for movement measurement."""
        #dt*momentum/mass
        self.position = tuple(np.add(np.divide(tuple((dt*x for x in self.momentum)), self.mass), self.position))
        print(self.position)
        
class ChargedParticle(Particle):
    charge = "-"
    def __init__(self, charge, x, y, z):
        Particle.__init__(self, x, y, z)
        self.charge = charge
    
class Electron(ChargedParticle):
    def __init__(self, x, y, z):
        ChargedParticle.__init__(self, "-", x, y, z)
        self.mass = const.m_e

class Proton(ChargedParticle):
    def __init__(self, x, y, z):
        ChargedParticle.__init__(self, "+", x, y, z)
        self.mass = const.m_p