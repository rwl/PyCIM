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

from CIM14v13.IEC61968.Common.ActivityRecord import ActivityRecord

class PSREvent(ActivityRecord):
    """Event recording the change in operational status of a PowerSystemResource.
    """

    def __init__(self, kind='inService', PowerSystemResource=None, *args, **kw_args):
        """Initializes a new 'PSREvent' instance.

        @param kind: Kind of event. Values are: "inService", "unknown", "pendingAdd", "outOfService", "pendingRemove", "other", "pendingReplace"
        @param PowerSystemResource: Power system resource that generated this event.
        """
        #: Kind of event. Values are: "inService", "unknown", "pendingAdd", "outOfService", "pendingRemove", "other", "pendingReplace"
        self.kind = kind

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        super(PSREvent, self).__init__(*args, **kw_args)

    def getPowerSystemResource(self):
        """Power system resource that generated this event.
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.PSREvent if x != self]
            self._PowerSystemResource._PSREvent = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._PSREvent.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

