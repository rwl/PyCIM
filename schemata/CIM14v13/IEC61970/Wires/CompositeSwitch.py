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

from CIM14v13.IEC61970.Core.Equipment import Equipment

class CompositeSwitch(Equipment):
    """A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.
    """

    def __init__(self, compositeSwitchType='', Switches=None, **kw_args):
        """Initializes a new 'CompositeSwitch' instance.

        @param compositeSwitchType: An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any 
        @param Switches: Switches contained in this Composite switch.
        """
        #: An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any
        self.compositeSwitchType = compositeSwitchType

        self._Switches = []
        self.Switches = [] if Switches is None else Switches

        super(CompositeSwitch, self).__init__(**kw_args)

    def getSwitches(self):
        """Switches contained in this Composite switch.
        """
        return self._Switches

    def setSwitches(self, value):
        for x in self._Switches:
            x._CompositeSwitch = None
        for y in value:
            y._CompositeSwitch = self
        self._Switches = value

    Switches = property(getSwitches, setSwitches)

    def addSwitches(self, *Switches):
        for obj in Switches:
            obj._CompositeSwitch = self
            self._Switches.append(obj)

    def removeSwitches(self, *Switches):
        for obj in Switches:
            obj._CompositeSwitch = None
            self._Switches.remove(obj)

