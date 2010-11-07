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

from CIM14.IEC61970.Meas.Control import Control

class Command(Control):
    """A Command is a discrete control used for supervisory control.
    """

    def __init__(self, value=0, normalValue=0, ValueAliasSet=None, Discrete=None, **kw_args):
        """Initializes a new 'Command' instance.

        @param value: The value representing the actuator output 
        @param normalValue: Normal value for Control.value e.g. used for percentage scaling 
        @param ValueAliasSet: The Commands using the set for translation.
        @param Discrete: The Measurement variable used for control.
        """
        #: The value representing the actuator output
        self.value = value

        #: Normal value for Control.value e.g. used for percentage scaling
        self.normalValue = normalValue

        self._ValueAliasSet = None
        self.ValueAliasSet = ValueAliasSet

        self._Discrete = None
        self.Discrete = Discrete

        super(Command, self).__init__(**kw_args)

    def getValueAliasSet(self):
        """The Commands using the set for translation.
        """
        return self._ValueAliasSet

    def setValueAliasSet(self, value):
        if self._ValueAliasSet is not None:
            filtered = [x for x in self.ValueAliasSet.Commands if x != self]
            self._ValueAliasSet._Commands = filtered

        self._ValueAliasSet = value
        if self._ValueAliasSet is not None:
            self._ValueAliasSet._Commands.append(self)

    ValueAliasSet = property(getValueAliasSet, setValueAliasSet)

    def getDiscrete(self):
        """The Measurement variable used for control.
        """
        return self._Discrete

    def setDiscrete(self, value):
        if self._Discrete is not None:
            self._Discrete._Command = None

        self._Discrete = value
        if self._Discrete is not None:
            self._Discrete._Command = self

    Discrete = property(getDiscrete, setDiscrete)

