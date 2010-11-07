# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.Dynamics.Loads.AggregateLoad import AggregateLoad

class LoadStatic(AggregateLoad):
    """General Static Load Model. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.
    """

    def __init__(self, staticLoadType='ZIP1', ep1=0.0, kp3=0.0, eq3=0.0, kp2=0.0, eq2=0.0, kqf=0.0, kq4=0.0, kq2=0.0, kp1=0.0, ep2=0.0, eq1=0.0, kpf=0.0, kp4=0.0, kq3=0.0, ep3=0.0, kq1=0.0, **kw_args):
        """Initializes a new 'LoadStatic' instance.

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
        #: Type of static load modelValues are: "ZIP1", "exponential", "ZIP2"
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

        super(LoadStatic, self).__init__(**kw_args)

