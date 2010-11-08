# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.Dynamics.Loads.AggregateLoad import AggregateLoad

class LoadMotor(AggregateLoad):
    """Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as 'induction motor load'.  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  Either a 'one-cage' or 'two-cage' model of the induction machine can be modeled.  Magnetic saturation is not modeled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors.
    """

    def __init__(self, tv=0.0, pfrac=0.0, vt=0.0, d=0.0, ra=0.0, ls=0.0, lfac=0.0, tpo=0.0, h=0.0, lp=0.0, lpp=0.0, tppo=0.0, tbkr=0.0, *args, **kw_args):
        """Initialises a new 'LoadMotor' instance.

        @param tv: Voltage trip pickup time (default = 999) 
        @param pfrac: Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0) 
        @param vt: Voltage threshold for tripping (default = 0) 
        @param d: Damping factor 
        @param ra: Stator resistance 
        @param ls: Synchronous reactance 
        @param lfac: Loading factor &ndash; ratio of initial P to motor MVA base 
        @param tpo: Transient rotor time constant 
        @param h: Inertia constant 
        @param lp: Transient reactance 
        @param lpp: Sub-transient reactance 
        @param tppo: Sub-transient rotor time constant 
        @param tbkr: Circuit breaker operating time (default = 999) 
        """
        #: Voltage trip pickup time (default = 999)
        self.tv = tv

        #: Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0)
        self.pfrac = pfrac

        #: Voltage threshold for tripping (default = 0)
        self.vt = vt

        #: Damping factor
        self.d = d

        #: Stator resistance
        self.ra = ra

        #: Synchronous reactance
        self.ls = ls

        #: Loading factor &ndash; ratio of initial P to motor MVA base
        self.lfac = lfac

        #: Transient rotor time constant
        self.tpo = tpo

        #: Inertia constant
        self.h = h

        #: Transient reactance
        self.lp = lp

        #: Sub-transient reactance
        self.lpp = lpp

        #: Sub-transient rotor time constant
        self.tppo = tppo

        #: Circuit breaker operating time (default = 999)
        self.tbkr = tbkr

        super(LoadMotor, self).__init__(*args, **kw_args)

    _attrs = ["tv", "pfrac", "vt", "d", "ra", "ls", "lfac", "tpo", "h", "lp", "lpp", "tppo", "tbkr"]
    _attr_types = {"tv": float, "pfrac": float, "vt": float, "d": float, "ra": float, "ls": float, "lfac": float, "tpo": float, "h": float, "lp": float, "lpp": float, "tppo": float, "tbkr": float}
    _defaults = {"tv": 0.0, "pfrac": 0.0, "vt": 0.0, "d": 0.0, "ra": 0.0, "ls": 0.0, "lfac": 0.0, "tpo": 0.0, "h": 0.0, "lp": 0.0, "lpp": 0.0, "tppo": 0.0, "tbkr": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

