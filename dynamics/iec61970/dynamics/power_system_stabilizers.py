# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA


from dynamics import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_PowerSystemStabilizers"

class PowerSystemStabilizer(Element):
    """ A PSS provides an input (Vs) to the excitation system model to improve damping of system oscillations.  A variety of input signals may be used depending on the particular design.
    """
    pass
    # <<< power_system_stabilizer
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PowerSystemStabilizer' instance.

        """


        super(PowerSystemStabilizer, self).__init__(*args, **kw_args)
    # >>> power_system_stabilizer



class PssIEEE4B(PowerSystemStabilizer):
    """ PSS type IEEE PSS4B
    """
    pass
    # <<< pss_ieee4_b
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PssIEEE4B' instance.

        """


        super(PssIEEE4B, self).__init__(*args, **kw_args)
    # >>> pss_ieee4_b



class PssIEEE2B(PowerSystemStabilizer):
    """ IEEE (2005) PSS2B Model  This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.
    """
    # <<< pss_ieee2_b
    # @generated
    def __init__(self, t10=0.0, a=0.0, ks1=0.0, ks3=0.0, t11=0.0, ks2=0.0, vstmin=0.0, vsi1max=0.0, vsi2max=0.0, tb=0.0, t2=0.0, ta=0.0, t1=0.0, t4=0.0, n=False, t3=0.0, m=False, t6=0.0, t8=0.0, vsi1min=0.0, t7=0.0, t9=0.0, ks4=0.0, tw2=0.0, tw1=0.0, tw4=0.0, vsi2min=0.0, tw3=0.0, vstmax=0.0, *args, **kw_args):
        """ Initialises a new 'PssIEEE2B' instance.

        @param t10: Lead/lag time constant 
        @param a: Numerator constant 
        @param ks1: Stabilizer gain 
        @param ks3: Gain on signal #2 input before ramp-tracking filter 
        @param t11: Lead/lag time constant 
        @param ks2: Gain on signal #2 
        @param vstmin: Stabilizer output min limit 
        @param vsi1max: Input signal #1 max limit 
        @param vsi2max: Input signal #2 max limit 
        @param tb: Lag time constant 
        @param t2: Lead/lag time constant 
        @param ta: Lead constant 
        @param t1: Lead/lag time constant 
        @param t4: Lead/lag time constant 
        @param n: Order of ramp tracking filter 
        @param t3: Lead/lag time constant 
        @param m: Denominator order of ramp tracking filter 
        @param t6: Time constant on signal #1 
        @param t8: Lead of ramp tracking filter 
        @param vsi1min: Input signal #1 min limit 
        @param t7: Time constant on signal #2 
        @param t9: Lag of ramp tracking filter 
        @param ks4: Gain on signal #2 input after ramp-tracking filter 
        @param tw2: Second washout on signal #1 
        @param tw1: First washout on signal #1 
        @param tw4: Second washout on signal #2 
        @param vsi2min: Input signal #2 min limit 
        @param tw3: First washout on signal #2 
        @param vstmax: Stabilizer output max limit 
        """
        # Lead/lag time constant 
        self.t10 = t10

        # Numerator constant 
        self.a = a

        # Stabilizer gain 
        self.ks1 = ks1

        # Gain on signal #2 input before ramp-tracking filter 
        self.ks3 = ks3

        # Lead/lag time constant 
        self.t11 = t11

        # Gain on signal #2 
        self.ks2 = ks2

        # Stabilizer output min limit 
        self.vstmin = vstmin

        # Input signal #1 max limit 
        self.vsi1max = vsi1max

        # Input signal #2 max limit 
        self.vsi2max = vsi2max

        # Lag time constant 
        self.tb = tb

        # Lead/lag time constant 
        self.t2 = t2

        # Lead constant 
        self.ta = ta

        # Lead/lag time constant 
        self.t1 = t1

        # Lead/lag time constant 
        self.t4 = t4

        # Order of ramp tracking filter 
        self.n = n

        # Lead/lag time constant 
        self.t3 = t3

        # Denominator order of ramp tracking filter 
        self.m = m

        # Time constant on signal #1 
        self.t6 = t6

        # Lead of ramp tracking filter 
        self.t8 = t8

        # Input signal #1 min limit 
        self.vsi1min = vsi1min

        # Time constant on signal #2 
        self.t7 = t7

        # Lag of ramp tracking filter 
        self.t9 = t9

        # Gain on signal #2 input after ramp-tracking filter 
        self.ks4 = ks4

        # Second washout on signal #1 
        self.tw2 = tw2

        # First washout on signal #1 
        self.tw1 = tw1

        # Second washout on signal #2 
        self.tw4 = tw4

        # Input signal #2 min limit 
        self.vsi2min = vsi2min

        # First washout on signal #2 
        self.tw3 = tw3

        # Stabilizer output max limit 
        self.vstmax = vstmax



        super(PssIEEE2B, self).__init__(*args, **kw_args)
    # >>> pss_ieee2_b



class PssSB4(PowerSystemStabilizer):
    """ Power sensitive stabilizer model
    """
    pass
    # <<< pss_sb4
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PssSB4' instance.

        """


        super(PssSB4, self).__init__(*args, **kw_args)
    # >>> pss_sb4



class PssSB(PowerSystemStabilizer):
    """ Dual input PSS, pss2a and transient stabilizer
    """
    pass
    # <<< pss_sb
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PssSB' instance.

        """


        super(PssSB, self).__init__(*args, **kw_args)
    # >>> pss_sb



class PssSK(PowerSystemStabilizer):
    """ PSS Slovakian type &ndash; three inputs
    """
    pass
    # <<< pss_sk
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PssSK' instance.

        """


        super(PssSK, self).__init__(*args, **kw_args)
    # >>> pss_sk



class PssPTIST3(PowerSystemStabilizer):
    """ PTI microprocessor-based stabilizer model type 3
    """
    pass
    # <<< pss_ptist3
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PssPTIST3' instance.

        """


        super(PssPTIST3, self).__init__(*args, **kw_args)
    # >>> pss_ptist3



class PssIEEE1A(PowerSystemStabilizer):
    """ PSS type IEEE PSS1A
    """
    pass
    # <<< pss_ieee1_a
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PssIEEE1A' instance.

        """


        super(PssIEEE1A, self).__init__(*args, **kw_args)
    # >>> pss_ieee1_a



class PssIEEE3B(PowerSystemStabilizer):
    """ PSS type IEEE PSS3B
    """
    pass
    # <<< pss_ieee3_b
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PssIEEE3B' instance.

        """


        super(PssIEEE3B, self).__init__(*args, **kw_args)
    # >>> pss_ieee3_b



class PssWSCC(PowerSystemStabilizer):
    """ Dual input PSS
    """
    pass
    # <<< pss_wscc
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PssWSCC' instance.

        """


        super(PssWSCC, self).__init__(*args, **kw_args)
    # >>> pss_wscc



class PssPTIST1(PowerSystemStabilizer):
    """ PTI microprocessor-based stabilizer model type 1
    """
    pass
    # <<< pss_ptist1
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PssPTIST1' instance.

        """


        super(PssPTIST1, self).__init__(*args, **kw_args)
    # >>> pss_ptist1



class PssSH(PowerSystemStabilizer):
    """ Siemens H infinity PSS
    """
    pass
    # <<< pss_sh
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'PssSH' instance.

        """


        super(PssSH, self).__init__(*args, **kw_args)
    # >>> pss_sh



# <<< power_system_stabilizers
# @generated
# >>> power_system_stabilizers
