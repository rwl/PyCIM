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

class ExcSEXS(ExcitationSystem):
    """Simplified Excitation System Model
    """

    def __init__(self, tb=0.0, kc=0.0, emax=0.0, tatb=0.0, tc=0.0, efdmin=0.0, efdmax=0.0, emin=0.0, k=0.0, te=0.0, *args, **kw_args):
        """Initialises a new 'ExcSEXS' instance.

        @param tb: Denominator time constant of lag-lead block 
        @param kc: PI controller gain (&gt; 0. if Tc &gt; 0.) 
        @param emax: Maximum field voltage output 
        @param tatb: Ta/Tb - gain reduction ratio of lag-lead element 
        @param tc: PI controller phase lead time constant 
        @param efdmin: Field voltage clipping minimum limit 
        @param efdmax: Field voltage clipping maximum limit 
        @param emin: Minimum field voltage output 
        @param k: Gain (&gt; 0.) 
        @param te: Time constant of gain block (&gt; 0.) 
        """
        #: Denominator time constant of lag-lead block
        self.tb = tb

        #: PI controller gain (&gt; 0. if Tc &gt; 0.)
        self.kc = kc

        #: Maximum field voltage output
        self.emax = emax

        #: Ta/Tb - gain reduction ratio of lag-lead element
        self.tatb = tatb

        #: PI controller phase lead time constant
        self.tc = tc

        #: Field voltage clipping minimum limit
        self.efdmin = efdmin

        #: Field voltage clipping maximum limit
        self.efdmax = efdmax

        #: Minimum field voltage output
        self.emin = emin

        #: Gain (&gt; 0.)
        self.k = k

        #: Time constant of gain block (&gt; 0.)
        self.te = te

        super(ExcSEXS, self).__init__(*args, **kw_args)

    _attrs = ["tb", "kc", "emax", "tatb", "tc", "efdmin", "efdmax", "emin", "k", "te"]
    _attr_types = {"tb": float, "kc": float, "emax": float, "tatb": float, "tc": float, "efdmin": float, "efdmax": float, "emin": float, "k": float, "te": float}
    _defaults = {"tb": 0.0, "kc": 0.0, "emax": 0.0, "tatb": 0.0, "tc": 0.0, "efdmin": 0.0, "efdmax": 0.0, "emin": 0.0, "k": 0.0, "te": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

