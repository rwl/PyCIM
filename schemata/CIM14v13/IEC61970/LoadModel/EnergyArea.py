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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class EnergyArea(IdentifiedObject):
    """The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """

    def __init__(self, ControlArea=None, **kw_args):
        """Initializes a new 'EnergyArea' instance.

        @param ControlArea: The control area specification that is used for the load forecast.
        """
        self._ControlArea = None
        self.ControlArea = ControlArea

        super(EnergyArea, self).__init__(**kw_args)

    def getControlArea(self):
        """The control area specification that is used for the load forecast.
        """
        return self._ControlArea

    def setControlArea(self, value):
        if self._ControlArea is not None:
            self._ControlArea._EnergyArea = None

        self._ControlArea = value
        if self._ControlArea is not None:
            self._ControlArea._EnergyArea = self

    ControlArea = property(getControlArea, setControlArea)

