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

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_VoltageCompensator"

class VoltageCompensator(Element):
    """ A voltage compensator adjusts the terminal voltage feedback to the excitation system by adding a quantity that is proportional to the terminal current of the generator. It is linked to a specific generator by the Bus number and Unit ID
    """
    # <<< voltage_compensator
    # @generated
    def __init__(self, rcomp=0.0, xcomp=0.0, *args, **kw_args):
        """ Initialises a new 'VoltageCompensator' instance.

        @param rcomp: Compensating (compounding) resistance 
        @param xcomp: Compensating (compounding) reactance 
        """
        # Compensating (compounding) resistance 
        self.rcomp = rcomp

        # Compensating (compounding) reactance 
        self.xcomp = xcomp



        super(VoltageCompensator, self).__init__(*args, **kw_args)
    # >>> voltage_compensator



class VcompIEEE(VoltageCompensator):
    """ IEEE Voltage Compensation Model
    """
    pass
    # <<< vcomp_ieee
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'VcompIEEE' instance.

        """


        super(VcompIEEE, self).__init__(*args, **kw_args)
    # >>> vcomp_ieee



class VcompCross(VoltageCompensator):
    """ Voltage Compensation Model for Cross-Compound Generating Unit
    """
    # <<< vcomp_cross
    # @generated
    def __init__(self, xcomp2=0.0, rcomp2=0.0, *args, **kw_args):
        """ Initialises a new 'VcompCross' instance.

        @param xcomp2: Cross-Compensating (compounding) reactance 
        @param rcomp2: Cross-Compensating (compounding) resistance 
        """
        # Cross-Compensating (compounding) reactance 
        self.xcomp2 = xcomp2

        # Cross-Compensating (compounding) resistance 
        self.rcomp2 = rcomp2



        super(VcompCross, self).__init__(*args, **kw_args)
    # >>> vcomp_cross



# <<< voltage_compensator
# @generated
# >>> voltage_compensator
