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

# Modified by Gustav Holm (guholm@kth.se) & Francis J. Gómez (fragom@kth.se)
# Modified date: 05/06/2017

from CIM16.IEC61970.Dynamics.SynchronousMachineDetailed import SynchronousMachineDetailed

class SynchronousMachineEquivalentCircuit(SynchronousMachineDetailed):
    
    def __init__(self, r1d=0.0, r1q=0.0, r2q=0.0, rfd=0.0, x1d=0.0, x1q=0.0, x2q=0.0, xad=0.0, xaq=0.0, xf1d=0.0, xfd=0.0, *args, **kw_args):
    
        self.r1d = r1d

        self.r1q = r1q

        self. r2q = r2q

        self.rfd = rfd

        self.x1d = x1d

        self.x1q = x1q

        self.x2q = x2q

        self.xad = xad

        self.xaq = xaq

        self.xf1d = xf1d

        self.xfd = xfd

        super(SynchronousMachineEquivalentCircuit, self).__init__(*args, **kw_args)

    _attrs = ["r1d", "r1q", "r2q", "rfd", "x1d", "x1q", "x2q", "xad", "xaq", "xf1d", "xfd"]
    _attr_types = {"r1d": float, "r1q": float, "r2q": float, "rfd": float, "x1d": float, "x1q": float, "x2q": float, "xad": float, "xaq": float, "xf1d": float, "xfd": float}
    _defaults = {"r1d": 0.0, "r1q": 0.0, "r2q": 0.0, "rfd": 0.0, "x1d": 0.0, "x1q": 0.0, "x2q": 0.0, "xad": 0.0, "xaq": 0.0, "xf1d": 0.0, "xfd": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []


