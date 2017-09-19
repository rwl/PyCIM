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

# Modified by Gustav Holm (guholm@kth.se) & Francis J. Gomez (fragom@kth.se)
# Modified date: 05/06/2017

from CIM16.IEC61970.Dynamics.SynchronousMachineDetailed import SynchronousMachineDetailed

class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
    
    def __init__(self, ks=0.0, xDirectSync=0.0, xDirectTrans=0.0, xDirectSubtrans=0.0, xQuadSync=0.0, xQuadTrans=0.0, xQuadSubtrans=0.0, tpdo=0.0, tppdo=0.0, tpqo=0.0, tppqo=0.0, tc=0.0, rotorType=None, modelType=None, *args, **kw_args):
    
        self.ks = ks

        self.xDirectSync = xDirectSync

        self.xDirectTrans = xDirectTrans

        self.xDirectSubtrans = xDirectSubtrans

        self.xQuadSync = xQuadSync

        self.xQuadTrans =xQuadTrans

        self.xQuadSubtrans = xQuadSubtrans

        self.tpdo = tpdo

        self.tppdo = tppdo

        self.tpqo = tpqo

        self.tppqo = tppqo

        self.tc = tc

        self.rotorType = rotorType

        self.modelType = modelType

        super(SynchronousMachineTimeConstantReactance, self).__init__(*args, **kw_args)

    _attrs = ["ks", "xDirectSync", "xDirectTrans", "xDirectSubtrans", "xQuadSync", "xQuadTrans", "xQuadSubtrans", "tpdo", "tppdo", "tpqo", "tppqo", "tc"]
    _attr_types = {"ks": float, "xDirectSync": float, "xDirectTrans": float, "xDirectSubtrans": float, "xQuadSync": float, "xQuadTrans": float, "xQuadSubtrans": float, "tpdo": float, "tppdo": float, "tpqo": float, "tppqo": float, "tc": float}
    _defaults = {"ks": 0.0, "xDirectSync": 0.0, "xDirectTrans": 0.0, "xDirectSubtrans": 0.0, "xQuadSync": 0.0, "xQuadTrans": 0.0, "xQuadSubtrans": 0.0, "tpdo": 0.0, "tppdo": 0.0, "tpqo": 0.0, "tppqo": 0.0, "tc": 0.0}
    _enums = {"rotorType": "RotorKind", "modelType": "SynchronousMachineModelKind"}
    _refs = []
    _many_refs = []


