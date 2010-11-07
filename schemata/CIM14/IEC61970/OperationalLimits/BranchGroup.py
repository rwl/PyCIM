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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BranchGroup(IdentifiedObject):
    """A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network.
    """

    def __init__(self, minimumReactivePower=0.0, monitorActivePower=False, minimumActivePower=0.0, maximumReactivePower=0.0, maximumActivePower=0.0, monitorReactivePower=False, BranchGroupTerminal=None, **kw_args):
        """Initializes a new 'BranchGroup' instance.

        @param minimumReactivePower: The minimum reactive power flow. 
        @param monitorActivePower: Monitor the active power flow. 
        @param minimumActivePower: The minimum active power flow. 
        @param maximumReactivePower: The maximum reactive power flow. 
        @param maximumActivePower: The maximum active power flow. 
        @param monitorReactivePower: Monitor the reactive power flow. 
        @param BranchGroupTerminal: The directed branch group terminals to be summed.
        """
        #: The minimum reactive power flow.
        self.minimumReactivePower = minimumReactivePower

        #: Monitor the active power flow.
        self.monitorActivePower = monitorActivePower

        #: The minimum active power flow.
        self.minimumActivePower = minimumActivePower

        #: The maximum reactive power flow.
        self.maximumReactivePower = maximumReactivePower

        #: The maximum active power flow.
        self.maximumActivePower = maximumActivePower

        #: Monitor the reactive power flow.
        self.monitorReactivePower = monitorReactivePower

        self._BranchGroupTerminal = []
        self.BranchGroupTerminal = [] if BranchGroupTerminal is None else BranchGroupTerminal

        super(BranchGroup, self).__init__(**kw_args)

    def getBranchGroupTerminal(self):
        """The directed branch group terminals to be summed.
        """
        return self._BranchGroupTerminal

    def setBranchGroupTerminal(self, value):
        for x in self._BranchGroupTerminal:
            x._BranchGroup = None
        for y in value:
            y._BranchGroup = self
        self._BranchGroupTerminal = value

    BranchGroupTerminal = property(getBranchGroupTerminal, setBranchGroupTerminal)

    def addBranchGroupTerminal(self, *BranchGroupTerminal):
        for obj in BranchGroupTerminal:
            obj._BranchGroup = self
            self._BranchGroupTerminal.append(obj)

    def removeBranchGroupTerminal(self, *BranchGroupTerminal):
        for obj in BranchGroupTerminal:
            obj._BranchGroup = None
            self._BranchGroupTerminal.remove(obj)

