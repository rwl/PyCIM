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

class SlotConnection(IdentifiedObject):
    """Standard connectivity if not specified at the instance level..
    """

    def __init__(self, connectionFrame0=None, slotInput0=None, slotOutput0=None, **kw_args):
        """Initializes a new 'SlotConnection' instance.

        @param connectionFrame0:
        @param slotInput0:
        @param slotOutput0:
        """
        self._connectionFrame0 = None
        self.connectionFrame0 = connectionFrame0

        self._slotInput0 = None
        self.slotInput0 = slotInput0

        self._slotOutput0 = None
        self.slotOutput0 = slotOutput0

        super(SlotConnection, self).__init__(**kw_args)

    def getconnectionFrame0(self):
        
        return self._connectionFrame0

    def setconnectionFrame0(self, value):
        if self._connectionFrame0 is not None:
            filtered = [x for x in self.connectionFrame0.slotConnection0 if x != self]
            self._connectionFrame0._slotConnection0 = filtered

        self._connectionFrame0 = value
        if self._connectionFrame0 is not None:
            self._connectionFrame0._slotConnection0.append(self)

    connectionFrame0 = property(getconnectionFrame0, setconnectionFrame0)

    def getslotInput0(self):
        
        return self._slotInput0

    def setslotInput0(self, value):
        if self._slotInput0 is not None:
            self._slotInput0._slotConnection0 = None

        self._slotInput0 = value
        if self._slotInput0 is not None:
            self._slotInput0._slotConnection0 = self

    slotInput0 = property(getslotInput0, setslotInput0)

    def getslotOutput0(self):
        
        return self._slotOutput0

    def setslotOutput0(self, value):
        if self._slotOutput0 is not None:
            filtered = [x for x in self.slotOutput0.slotConnection0 if x != self]
            self._slotOutput0._slotConnection0 = filtered

        self._slotOutput0 = value
        if self._slotOutput0 is not None:
            self._slotOutput0._slotConnection0.append(self)

    slotOutput0 = property(getslotOutput0, setslotOutput0)

