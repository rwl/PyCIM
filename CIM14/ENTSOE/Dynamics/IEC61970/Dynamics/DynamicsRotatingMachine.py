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

from CIM14.ENTSOE.Dynamics.IEC61970.Wires.WiresRegulatingCondEq import WiresRegulatingCondEq

class DynamicsRotatingMachine(WiresRegulatingCondEq):

    def __init__(self, ratedS=0.0, s1=0.0, s12=0.0, h=0.0, parametersFormType="equivalentCircuit", d=0.0, rs=0.0, xls=0.0, *args, **kw_args):
        """Initialises a new 'DynamicsRotatingMachine' instance.

        @param ratedS:  
        @param s1:  
        @param s12:  
        @param h:  
        @param parametersFormType:  Values are: "equivalentCircuit", "timeConstantReactance"
        @param d:  
        @param rs:  
        @param xls:  
        """
        #: 
        self.ratedS = ratedS

        #: 
        self.s1 = s1

        #: 
        self.s12 = s12

        #: 
        self.h = h

        #:  Values are: "equivalentCircuit", "timeConstantReactance"
        self.parametersFormType = parametersFormType

        #: 
        self.d = d

        #: 
        self.rs = rs

        #: 
        self.xls = xls

        super(DynamicsRotatingMachine, self).__init__(*args, **kw_args)

    _attrs = ["ratedS", "s1", "s12", "h", "parametersFormType", "d", "rs", "xls"]
    _attr_types = {"ratedS": float, "s1": float, "s12": float, "h": float, "parametersFormType": str, "d": float, "rs": float, "xls": float}
    _defaults = {"ratedS": 0.0, "s1": 0.0, "s12": 0.0, "h": 0.0, "parametersFormType": "equivalentCircuit", "d": 0.0, "rs": 0.0, "xls": 0.0}
    _enums = {"parametersFormType": "GeneratorsParametersFormType"}
    _refs = []
    _many_refs = []

