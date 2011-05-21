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

from CIM14.IEC61970.Dynamics.RotatingMachine import RotatingMachine

class AsynchronousMachine(RotatingMachine):
    """An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine.
    """

    def __init__(self, xm=0.0, xs=0.0, xpp=0.0, xlr2=0.0, rr2=0.0, tpo=0.0, rr1=0.0, xp=0.0, tppo=0.0, xlr1=0.0, *args, **kw_args):
        """Initialises a new 'AsynchronousMachine' instance.

        @param xm: Magnetizing reactance 
        @param xs: Synchronous reactance (&gt;= Xp) 
        @param xpp: Sub-transient reactance (unsaturated) (&gt; Xl) 
        @param xlr2: Damper 2 winding leakage reactance 
        @param rr2: Damper 2 winding resistance 
        @param tpo: Transient rotor time constant (&gt; Tppo) 
        @param rr1: Damper 1 winding resistance 
        @param xp: Transient reactance (unsaturated) (&gt; =Xpp) 
        @param tppo: Sub-transient rotor time constant (&gt; 0.) 
        @param xlr1: Damper 1 winding leakage reactance 
        """
        #: Magnetizing reactance
        self.xm = xm

        #: Synchronous reactance (&gt;= Xp)
        self.xs = xs

        #: Sub-transient reactance (unsaturated) (&gt; Xl)
        self.xpp = xpp

        #: Damper 2 winding leakage reactance
        self.xlr2 = xlr2

        #: Damper 2 winding resistance
        self.rr2 = rr2

        #: Transient rotor time constant (&gt; Tppo)
        self.tpo = tpo

        #: Damper 1 winding resistance
        self.rr1 = rr1

        #: Transient reactance (unsaturated) (&gt; =Xpp)
        self.xp = xp

        #: Sub-transient rotor time constant (&gt; 0.)
        self.tppo = tppo

        #: Damper 1 winding leakage reactance
        self.xlr1 = xlr1

        super(AsynchronousMachine, self).__init__(*args, **kw_args)

    _attrs = ["xm", "xs", "xpp", "xlr2", "rr2", "tpo", "rr1", "xp", "tppo", "xlr1"]
    _attr_types = {"xm": float, "xs": float, "xpp": float, "xlr2": float, "rr2": float, "tpo": float, "rr1": float, "xp": float, "tppo": float, "xlr1": float}
    _defaults = {"xm": 0.0, "xs": 0.0, "xpp": 0.0, "xlr2": 0.0, "rr2": 0.0, "tpo": 0.0, "rr1": 0.0, "xp": 0.0, "tppo": 0.0, "xlr1": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

