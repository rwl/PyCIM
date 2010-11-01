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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class CommunicationLink(PowerSystemResource):
    """The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.
    """

    def __init__(self, RemoteUnits=None, *args, **kw_args):
        """Initializes a new 'CommunicationLink' instance.

        @param RemoteUnits: RTUs may be attached to communication links.
        """
        self._RemoteUnits = []
        self.RemoteUnits = [] if RemoteUnits is None else RemoteUnits

        super(CommunicationLink, self).__init__(*args, **kw_args)

    def getRemoteUnits(self):
        """RTUs may be attached to communication links.
        """
        return self._RemoteUnits

    def setRemoteUnits(self, value):
        for p in self._RemoteUnits:
            filtered = [q for q in p.CommunicationLinks if q != self]
            self._RemoteUnits._CommunicationLinks = filtered
        for r in value:
            if self not in r._CommunicationLinks:
                r._CommunicationLinks.append(self)
        self._RemoteUnits = value

    RemoteUnits = property(getRemoteUnits, setRemoteUnits)

    def addRemoteUnits(self, *RemoteUnits):
        for obj in RemoteUnits:
            if self not in obj._CommunicationLinks:
                obj._CommunicationLinks.append(self)
            self._RemoteUnits.append(obj)

    def removeRemoteUnits(self, *RemoteUnits):
        for obj in RemoteUnits:
            if self in obj._CommunicationLinks:
                obj._CommunicationLinks.remove(self)
            self._RemoteUnits.remove(obj)

