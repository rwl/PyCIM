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

class LoadsLoadStatic(CorePowerSystemResource):

    def __init__(self, ep2=0.0, ep1=0.0, kp2=0.0, ep3=0.0, kp1=0.0, kq4=0.0, kq3=0.0, kq2=0.0, kq1=0.0, eq1=0.0, eq2=0.0, kp4=0.0, kp3=0.0, eq3=0.0, staticLoadType="", kqf=0.0, kpf=0.0, *args, **kw_args):
        """Initialises a new 'LoadsLoadStatic' instance.

        @param ep2:  
        @param ep1:  
        @param kp2:  
        @param ep3:  
        @param kp1:  
        @param kq4:  
        @param kq3:  
        @param kq2:  
        @param kq1:  
        @param eq1:  
        @param eq2:  
        @param kp4:  
        @param kp3:  
        @param eq3:  
        @param staticLoadType:  
        @param kqf:  
        @param kpf:  
        """
        #: 
        self.ep2 = ep2

        #: 
        self.ep1 = ep1

        #: 
        self.kp2 = kp2

        #: 
        self.ep3 = ep3

        #: 
        self.kp1 = kp1

        #: 
        self.kq4 = kq4

        #: 
        self.kq3 = kq3

        #: 
        self.kq2 = kq2

        #: 
        self.kq1 = kq1

        #: 
        self.eq1 = eq1

        #: 
        self.eq2 = eq2

        #: 
        self.kp4 = kp4

        #: 
        self.kp3 = kp3

        #: 
        self.eq3 = eq3

        #: 
        self.staticLoadType = staticLoadType

        #: 
        self.kqf = kqf

        #: 
        self.kpf = kpf

        super(LoadsLoadStatic, self).__init__(*args, **kw_args)

    _attrs = ["ep2", "ep1", "kp2", "ep3", "kp1", "kq4", "kq3", "kq2", "kq1", "eq1", "eq2", "kp4", "kp3", "eq3", "staticLoadType", "kqf", "kpf"]
    _attr_types = {"ep2": float, "ep1": float, "kp2": float, "ep3": float, "kp1": float, "kq4": float, "kq3": float, "kq2": float, "kq1": float, "eq1": float, "eq2": float, "kp4": float, "kp3": float, "eq3": float, "staticLoadType": str, "kqf": float, "kpf": float}
    _defaults = {"ep2": 0.0, "ep1": 0.0, "kp2": 0.0, "ep3": 0.0, "kp1": 0.0, "kq4": 0.0, "kq3": 0.0, "kq2": 0.0, "kq1": 0.0, "eq1": 0.0, "eq2": 0.0, "kp4": 0.0, "kp3": 0.0, "eq3": 0.0, "staticLoadType": "", "kqf": 0.0, "kpf": 0.0}
    _enums = {"staticLoadType": "LoadsStaticLoadType"}
    _refs = []
    _many_refs = []

