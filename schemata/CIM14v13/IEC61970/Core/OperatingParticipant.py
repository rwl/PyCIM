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

class OperatingParticipant(IdentifiedObject):
    """An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.
    """

    def __init__(self, OperatingShare=None, *args, **kw_args):
        """Initializes a new 'OperatingParticipant' instance.

        @param OperatingShare: The operating shares of an operating participant.   An operating participant can be reused for any number of PSR's.
        """
        self._OperatingShare = []
        self.OperatingShare = [] if OperatingShare is None else OperatingShare

        super(OperatingParticipant, self).__init__(*args, **kw_args)

    def getOperatingShare(self):
        """The operating shares of an operating participant.   An operating participant can be reused for any number of PSR's.
        """
        return self._OperatingShare

    def setOperatingShare(self, value):
        for x in self._OperatingShare:
            x._OperatingParticipant = None
        for y in value:
            y._OperatingParticipant = self
        self._OperatingShare = value

    OperatingShare = property(getOperatingShare, setOperatingShare)

    def addOperatingShare(self, *OperatingShare):
        for obj in OperatingShare:
            obj._OperatingParticipant = self
            self._OperatingShare.append(obj)

    def removeOperatingShare(self, *OperatingShare):
        for obj in OperatingShare:
            obj._OperatingParticipant = None
            self._OperatingShare.remove(obj)

