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

from CIM14.Element import Element

class OperatingShare(Element):
    """Specifies the contract relationship between a PowerSystemResource and a contract participant.
    """

    def __init__(self, percentage=0.0, PowerSystemResource=None, OperatingParticipant=None, **kw_args):
        """Initializes a new 'OperatingShare' instance.

        @param percentage: Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%. 
        @param PowerSystemResource: The PowerSystemResource to which the attribues apply.   The percentage ownership of all owners of a PowerSystemResource should add to 100%.
        @param OperatingParticipant: The linkage to a owners  and its linkage attributes like percentage ownership.   The ownership percentage should add to 100% for all owners of a PowerSystemResource, but a PSROwner may own any percentage of any number of PowerSystemResource objects.
        """
        #: Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%.
        self.percentage = percentage

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._OperatingParticipant = None
        self.OperatingParticipant = OperatingParticipant

        super(OperatingShare, self).__init__(**kw_args)

    def getPowerSystemResource(self):
        """The PowerSystemResource to which the attribues apply.   The percentage ownership of all owners of a PowerSystemResource should add to 100%.
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.OperatingShare if x != self]
            self._PowerSystemResource._OperatingShare = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._OperatingShare.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getOperatingParticipant(self):
        """The linkage to a owners  and its linkage attributes like percentage ownership.   The ownership percentage should add to 100% for all owners of a PowerSystemResource, but a PSROwner may own any percentage of any number of PowerSystemResource objects.
        """
        return self._OperatingParticipant

    def setOperatingParticipant(self, value):
        if self._OperatingParticipant is not None:
            filtered = [x for x in self.OperatingParticipant.OperatingShare if x != self]
            self._OperatingParticipant._OperatingShare = filtered

        self._OperatingParticipant = value
        if self._OperatingParticipant is not None:
            self._OperatingParticipant._OperatingShare.append(self)

    OperatingParticipant = property(getOperatingParticipant, setOperatingParticipant)

