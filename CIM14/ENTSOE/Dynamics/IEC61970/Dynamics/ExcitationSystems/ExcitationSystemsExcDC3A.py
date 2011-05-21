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

class ExcitationSystemsExcDC3A(CorePowerSystemResource):

    def __init__(self, vrmax=0.0, ke=0.0, te=0.0, exclim=0.0, se1=0.0, se2=0.0, trh=0.0, kv=0.0, e1=0.0, e2=0.0, vrmin=0.0, tr=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcDC3A' instance.

        @param vrmax: 
        @param ke: 
        @param te: 
        @param exclim: 
        @param se1: 
        @param se2: 
        @param trh: 
        @param kv: 
        @param e1: 
        @param e2: 
        @param vrmin: 
        @param tr: 
        """

        self.vrmax = vrmax


        self.ke = ke


        self.te = te


        self.exclim = exclim


        self.se1 = se1


        self.se2 = se2


        self.trh = trh


        self.kv = kv


        self.e1 = e1


        self.e2 = e2


        self.vrmin = vrmin


        self.tr = tr

        super(ExcitationSystemsExcDC3A, self).__init__(*args, **kw_args)

    _attrs = ["vrmax", "ke", "te", "exclim", "se1", "se2", "trh", "kv", "e1", "e2", "vrmin", "tr"]
    _attr_types = {"vrmax": float, "ke": float, "te": float, "exclim": float, "se1": float, "se2": float, "trh": float, "kv": float, "e1": float, "e2": float, "vrmin": float, "tr": float}
    _defaults = {"vrmax": 0.0, "ke": 0.0, "te": 0.0, "exclim": 0.0, "se1": 0.0, "se2": 0.0, "trh": 0.0, "kv": 0.0, "e1": 0.0, "e2": 0.0, "vrmin": 0.0, "tr": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

