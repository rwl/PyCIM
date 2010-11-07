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

from CIM14.Dynamics.PowerSystemStabilizers.PowerSystemStabilizer import PowerSystemStabilizer

class PssIEEE2B(PowerSystemStabilizer):
    """IEEE (2005) PSS2B Model  This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.
    """

    def __init__(self, t11=0.0, vsi1max=0.0, t3=0.0, tw3=0.0, vstmax=0.0, t2=0.0, n=0, vsi1min=0.0, t9=0.0, ks2=0.0, vstmin=0.0, j1=0, tw1=0.0, tb=0.0, t7=0.0, vsi2max=0.0, t6=0.0, t1=0.0, m=0, vsi2min=0.0, a=0.0, t4=0.0, tw4=0.0, ks4=0.0, ta=0.0, ks3=0.0, t10=0.0, tw2=0.0, j2=0, ks1=0.0, t8=0.0, **kw_args):
        """Initializes a new 'PssIEEE2B' instance.

        @param t11: Lead/lag time constant 
        @param vsi1max: Input signal #1 max limit 
        @param t3: Lead/lag time constant 
        @param tw3: First washout on signal #2 
        @param vstmax: Stabilizer output max limit 
        @param t2: Lead/lag time constant 
        @param n: Order of ramp tracking filter 
        @param vsi1min: Input signal #1 min limit 
        @param t9: Lag of ramp tracking filter 
        @param ks2: Gain on signal #2 
        @param vstmin: Stabilizer output min limit 
        @param j1: Input signal #1 code 1	shaft speed 2	frequency of bus voltage 3	generator electrical power 4	generator accelerating power 5	amplitude of bus voltage 6              derivative of bus voltage amplitude 
        @param tw1: First washout on signal #1 
        @param tb: Lag time constant 
        @param t7: Time constant on signal #2 
        @param vsi2max: Input signal #2 max limit 
        @param t6: Time constant on signal #1 
        @param t1: Lead/lag time constant 
        @param m: Denominator order of ramp tracking filter 
        @param vsi2min: Input signal #2 min limit 
        @param a: Numerator constant 
        @param t4: Lead/lag time constant 
        @param tw4: Second washout on signal #2 
        @param ks4: Gain on signal #2 input after ramp-tracking filter 
        @param ta: Lead constant 
        @param ks3: Gain on signal #2 input before ramp-tracking filter 
        @param t10: Lead/lag time constant 
        @param tw2: Second washout on signal #1 
        @param j2: Input signal #2 code 1	shaft speed 2	frequency of bus voltage 3	generator electrical power 4	generator accelerating power 5	amplitude of bus voltage 6              derivative of bus voltage amplitude 
        @param ks1: Stabilizer gain 
        @param t8: Lead of ramp tracking filter 
        """
        #: Lead/lag time constant
        self.t11 = t11

        #: Input signal #1 max limit
        self.vsi1max = vsi1max

        #: Lead/lag time constant
        self.t3 = t3

        #: First washout on signal #2
        self.tw3 = tw3

        #: Stabilizer output max limit
        self.vstmax = vstmax

        #: Lead/lag time constant
        self.t2 = t2

        #: Order of ramp tracking filter
        self.n = n

        #: Input signal #1 min limit
        self.vsi1min = vsi1min

        #: Lag of ramp tracking filter
        self.t9 = t9

        #: Gain on signal #2
        self.ks2 = ks2

        #: Stabilizer output min limit
        self.vstmin = vstmin

        #: Input signal #1 code 1	shaft speed 2	frequency of bus voltage 3	generator electrical power 4	generator accelerating power 5	amplitude of bus voltage 6              derivative of bus voltage amplitude
        self.j1 = j1

        #: First washout on signal #1
        self.tw1 = tw1

        #: Lag time constant
        self.tb = tb

        #: Time constant on signal #2
        self.t7 = t7

        #: Input signal #2 max limit
        self.vsi2max = vsi2max

        #: Time constant on signal #1
        self.t6 = t6

        #: Lead/lag time constant
        self.t1 = t1

        #: Denominator order of ramp tracking filter
        self.m = m

        #: Input signal #2 min limit
        self.vsi2min = vsi2min

        #: Numerator constant
        self.a = a

        #: Lead/lag time constant
        self.t4 = t4

        #: Second washout on signal #2
        self.tw4 = tw4

        #: Gain on signal #2 input after ramp-tracking filter
        self.ks4 = ks4

        #: Lead constant
        self.ta = ta

        #: Gain on signal #2 input before ramp-tracking filter
        self.ks3 = ks3

        #: Lead/lag time constant
        self.t10 = t10

        #: Second washout on signal #1
        self.tw2 = tw2

        #: Input signal #2 code 1	shaft speed 2	frequency of bus voltage 3	generator electrical power 4	generator accelerating power 5	amplitude of bus voltage 6              derivative of bus voltage amplitude
        self.j2 = j2

        #: Stabilizer gain
        self.ks1 = ks1

        #: Lead of ramp tracking filter
        self.t8 = t8

        super(PssIEEE2B, self).__init__(**kw_args)

