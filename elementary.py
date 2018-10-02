#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####
# Amelia & Royal
# Email: roseto@chapman.edu
# CW 5
# PHYS 220
# Septemeber 27, 2018
####

import scipy.constants

class Particle(object):
    """Particle is a class that should have 3 initialized variables: Mass(a float), Position(A triplet of floats), Momentum(A triplet of floats)"""
    mass = 0.0
    position = (0.0,0.0,0.0)
    momentum = (0.0,0.0,0.0)

    def __init__(self, x, y, z):
        """Class constructor
>>>>>>> f2002266b5ad377e51769e208e400ff6725ae9d2
        Sets initial values for 3 attributes.
        Requires a floating point triple as an
        arguement for the starting position of the particle"""
        self.position = (x, y, z)
        self.mass = 1.0
        self.momentum = (0.0,0.0,0.0)

    def impulse(self, px,py,pz):
        """Alters the momentum by the impulse amount.
        Requires floating point triple to set impulse
        value."""
        self.momentum = (self.momentum[0]+px,self.momentum[1]+py,self.momentum[2]+pz)

    def move(self, dt):
        """Moves particle by one dt.
        Requires time unit for movement measurement."""
        #dt*momentum/mass
        self.position = (self.position[0] + (dt/self.mass)*self.momentum[0],self.position[1]+(dt/self.mass)*self.momentum[1],self.position[2]+(dt/self.mass)*self.momentum[2])


class ChargedParticle(Particle):
    charge = 0.0

    def __init__(self, x, y, z):
        super(Particle,self).__init__(x, y, z)
        self.charge = 0.0

class Electron(ChargedParticle):

    def __init__(self, x, y, z):
        self.charge = -scipy.constants.e
        super(ChargedParticle,self).__init__(x, y, z)
        self.mass = scipy.constants.m_e

class Proton(ChargedParticle):

    def __init__(self, x, y, z):
        self.charge = scipy.constants.e
        super(ChargedParticle,self).__init__(x, y, z)
        self.mass = scipy.constants.m_p

    def main(argv):
        pass
