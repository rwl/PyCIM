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

from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment

class RegulatingCondEq(ConductingEquipment):
    """A type of conducting equipment that can regulate a quanity (i.e. voltage or flow) at a specific point in the network.
    """

    def __init__(self, Controls=None, RegulatingControl=None, **kw_args):
        """Initializes a new 'RegulatingCondEq' instance.

        @param Controls: The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator.
        @param RegulatingControl: The regulating control scheme in which this equipment participates.
        """
        self._Controls = []
        self.Controls = [] if Controls is None else Controls

        self._RegulatingControl = None
        self.RegulatingControl = RegulatingControl

        super(RegulatingCondEq, self).__init__(**kw_args)

    def getControls(self):
        """The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator.
        """
        return self._Controls

    def setControls(self, value):
        for x in self._Controls:
            x._RegulatingCondEq = None
        for y in value:
            y._RegulatingCondEq = self
        self._Controls = value

    Controls = property(getControls, setControls)

    def addControls(self, *Controls):
        for obj in Controls:
            obj._RegulatingCondEq = self
            self._Controls.append(obj)

    def removeControls(self, *Controls):
        for obj in Controls:
            obj._RegulatingCondEq = None
            self._Controls.remove(obj)

    def getRegulatingControl(self):
        """The regulating control scheme in which this equipment participates.
        """
        return self._RegulatingControl

    def setRegulatingControl(self, value):
        if self._RegulatingControl is not None:
            filtered = [x for x in self.RegulatingControl.RegulatingCondEq if x != self]
            self._RegulatingControl._RegulatingCondEq = filtered

        self._RegulatingControl = value
        if self._RegulatingControl is not None:
            self._RegulatingControl._RegulatingCondEq.append(self)

    RegulatingControl = property(getRegulatingControl, setRegulatingControl)

