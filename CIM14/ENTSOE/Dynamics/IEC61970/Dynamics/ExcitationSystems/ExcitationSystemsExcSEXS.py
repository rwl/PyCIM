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

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CorePowerSystemResource import CorePowerSystemResource

class ExcitationSystemsExcSEXS(CorePowerSystemResource):

    def __init__(self, k=0.0, tatb=0.0, efdmin=0.0, te=0.0, tc=0.0, kc=0.0, tb=0.0, emin=0.0, emax=0.0, efdmax=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcSEXS' instance.

        @param k: 
        @param tatb: 
        @param efdmin: 
        @param te: 
        @param tc: 
        @param kc: 
        @param tb: 
        @param emin: 
        @param emax: 
        @param efdmax: 
        """

        self.k = k


        self.tatb = tatb


        self.efdmin = efdmin


        self.te = te


        self.tc = tc


        self.kc = kc


        self.tb = tb


        self.emin = emin


        self.emax = emax


        self.efdmax = efdmax

        super(ExcitationSystemsExcSEXS, self).__init__(*args, **kw_args)

    _attrs = ["k", "tatb", "efdmin", "te", "tc", "kc", "tb", "emin", "emax", "efdmax"]
    _attr_types = {"k": float, "tatb": float, "efdmin": float, "te": float, "tc": float, "kc": float, "tb": float, "emin": float, "emax": float, "efdmax": float}
    _defaults = {"k": 0.0, "tatb": 0.0, "efdmin": 0.0, "te": 0.0, "tc": 0.0, "kc": 0.0, "tb": 0.0, "emin": 0.0, "emax": 0.0, "efdmax": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

