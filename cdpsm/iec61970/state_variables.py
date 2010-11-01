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

""" State variables for analysis solutions such as powerflow.
"""

from cdpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_StateVariables"

class SvTapStep(Element):
    """ State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.
    """
    # <<< sv_tap_step
    # @generated
    def __init__(self, continuous_position=0.0, position=0, tap_changer=None, *args, **kw_args):
        """ Initialises a new 'SvTapStep' instance.

        @param continuous_position: The floating point tap position. 
        @param position: The integer tap position. 
        @param tap_changer: The tap changer associated with the tap step state.
        """
        # The floating point tap position. 
        self.continuous_position = continuous_position

        # The integer tap position. 
        self.position = position


        self._tap_changer = None
        self.tap_changer = tap_changer


        super(SvTapStep, self).__init__(*args, **kw_args)
    # >>> sv_tap_step

    # <<< tap_changer
    # @generated
    def get_tap_changer(self):
        """ The tap changer associated with the tap step state.
        """
        return self._tap_changer

    def set_tap_changer(self, value):
        if self._tap_changer is not None:
            self._tap_changer._sv_tap_step = None

        self._tap_changer = value
        if self._tap_changer is not None:
            self._tap_changer._sv_tap_step = self

    tap_changer = property(get_tap_changer, set_tap_changer)
    # >>> tap_changer



# <<< state_variables
# @generated
# >>> state_variables
