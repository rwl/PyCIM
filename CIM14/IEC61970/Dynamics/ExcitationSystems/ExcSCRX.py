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

from CIM14.IEC61970.Dynamics.ExcitationSystems.ExcitationSystem import ExcitationSystem

class ExcSCRX(ExcitationSystem):
    """Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem
    """

    def __init__(self, tb=0.0, cswitch=False, emin=0.0, k=0.0, te=0.0, emax=0.0, tatb=0.0, rcrfd=0.0, *args, **kw_args):
        """Initialises a new 'ExcSCRX' instance.

        @param tb: Denominator time constant of lag-lead block 
        @param cswitch: Power source switch:     1 ? fixed voltage     0 ? generator terminal voltage 
        @param emin: Minimum field voltage output 
        @param k: Gain (&gt; 0.) 
        @param te: Time constant of gain block (&gt; 0.) 
        @param emax: Maximum field voltage output 
        @param tatb: Ta/Tb - gain reduction ratio of lag-lead element 
        @param rcrfd: Rc/Rfd - ratio of field discharge resistance to field winding resistance 
        """
        #: Denominator time constant of lag-lead block
        self.tb = tb

        #: Power source switch:     1 ? fixed voltage     0 ? generator terminal voltage
        self.cswitch = cswitch

        #: Minimum field voltage output
        self.emin = emin

        #: Gain (&gt; 0.)
        self.k = k

        #: Time constant of gain block (&gt; 0.)
        self.te = te

        #: Maximum field voltage output
        self.emax = emax

        #: Ta/Tb - gain reduction ratio of lag-lead element
        self.tatb = tatb

        #: Rc/Rfd - ratio of field discharge resistance to field winding resistance
        self.rcrfd = rcrfd

        super(ExcSCRX, self).__init__(*args, **kw_args)

    _attrs = ["tb", "cswitch", "emin", "k", "te", "emax", "tatb", "rcrfd"]
    _attr_types = {"tb": float, "cswitch": bool, "emin": float, "k": float, "te": float, "emax": float, "tatb": float, "rcrfd": float}
    _defaults = {"tb": 0.0, "cswitch": False, "emin": 0.0, "k": 0.0, "te": 0.0, "emax": 0.0, "tatb": 0.0, "rcrfd": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

