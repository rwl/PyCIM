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

from CIM14.IEC61970.StateVariables.StateVariable import StateVariable

class SvTapStep(StateVariable):
    """State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.
    """

    def __init__(self, continuousPosition=0.0, position=0, TapChanger=None, *args, **kw_args):
        """Initialises a new 'SvTapStep' instance.

        @param continuousPosition: The floating point tap position. 
        @param position: The integer tap position. 
        @param TapChanger: The tap changer associated with the tap step state.
        """
        #: The floating point tap position.
        self.continuousPosition = continuousPosition

        #: The integer tap position.
        self.position = position

        self._TapChanger = None
        self.TapChanger = TapChanger

        super(SvTapStep, self).__init__(*args, **kw_args)

    _attrs = ["continuousPosition", "position"]
    _attr_types = {"continuousPosition": float, "position": int}
    _defaults = {"continuousPosition": 0.0, "position": 0}
    _enums = {}
    _refs = ["TapChanger"]
    _many_refs = []

    def getTapChanger(self):
        """The tap changer associated with the tap step state.
        """
        return self._TapChanger

    def setTapChanger(self, value):
        if self._TapChanger is not None:
            self._TapChanger._SvTapStep = None

        self._TapChanger = value
        if self._TapChanger is not None:
            self._TapChanger._SvTapStep = self

    TapChanger = property(getTapChanger, setTapChanger)

