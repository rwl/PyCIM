# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.IEC61970.Dynamics.Loads.AggregateLoad import AggregateLoad

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

