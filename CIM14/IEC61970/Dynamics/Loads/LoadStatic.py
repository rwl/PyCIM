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

class LoadStatic(AggregateLoad):
    """General Static Load Model. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.
    """

    def __init__(self, staticLoadType="ZIP1", ep1=0.0, kp3=0.0, eq3=0.0, kp2=0.0, eq2=0.0, kqf=0.0, kq4=0.0, kq2=0.0, kp1=0.0, ep2=0.0, eq1=0.0, kpf=0.0, kp4=0.0, kq3=0.0, ep3=0.0, kq1=0.0, *args, **kw_args):
        """Initialises a new 'LoadStatic' instance.

        @param staticLoadType: Type of static load model Values are: "ZIP1", "exponential", "ZIP2"
        @param ep1: 
        @param kp3: 
        @param eq3: 
        @param kp2: 
        @param eq2: 
        @param kqf: 
        @param kq4: 
        @param kq2: 
        @param kp1: 
        @param ep2: 
        @param eq1: 
        @param kpf: 
        @param kp4: 
        @param kq3: 
        @param ep3: 
        @param kq1: 
        """
        #: Type of static load model Values are: "ZIP1", "exponential", "ZIP2"
        self.staticLoadType = staticLoadType


        self.ep1 = ep1


        self.kp3 = kp3


        self.eq3 = eq3


        self.kp2 = kp2


        self.eq2 = eq2


        self.kqf = kqf


        self.kq4 = kq4


        self.kq2 = kq2


        self.kp1 = kp1


        self.ep2 = ep2


        self.eq1 = eq1


        self.kpf = kpf


        self.kp4 = kp4


        self.kq3 = kq3


        self.ep3 = ep3


        self.kq1 = kq1

        super(LoadStatic, self).__init__(*args, **kw_args)

    _attrs = ["staticLoadType", "ep1", "kp3", "eq3", "kp2", "eq2", "kqf", "kq4", "kq2", "kp1", "ep2", "eq1", "kpf", "kp4", "kq3", "ep3", "kq1"]
    _attr_types = {"staticLoadType": str, "ep1": float, "kp3": float, "eq3": float, "kp2": float, "eq2": float, "kqf": float, "kq4": float, "kq2": float, "kp1": float, "ep2": float, "eq1": float, "kpf": float, "kp4": float, "kq3": float, "ep3": float, "kq1": float}
    _defaults = {"staticLoadType": "ZIP1", "ep1": 0.0, "kp3": 0.0, "eq3": 0.0, "kp2": 0.0, "eq2": 0.0, "kqf": 0.0, "kq4": 0.0, "kq2": 0.0, "kp1": 0.0, "ep2": 0.0, "eq1": 0.0, "kpf": 0.0, "kp4": 0.0, "kq3": 0.0, "ep3": 0.0, "kq1": 0.0}
    _enums = {"staticLoadType": "StaticLoadType"}
    _refs = []
    _many_refs = []

