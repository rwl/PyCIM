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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class RemoteUnit(PowerSystemResource):
    """A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc.
    """

    def __init__(self, remoteUnitType='IED', CommunicationLinks=None, RemotePoints=None, **kw_args):
        """Initializes a new 'RemoteUnit' instance.

        @param remoteUnitType: Type of remote unit. Values are: "IED", "ControlCenter", "RTU", "SubstationControlSystem"
        @param CommunicationLinks: RTUs may be attached to communication links.
        @param RemotePoints: Remote points this Remote unit contains.
        """
        #: Type of remote unit.Values are: "IED", "ControlCenter", "RTU", "SubstationControlSystem"
        self.remoteUnitType = remoteUnitType

        self._CommunicationLinks = []
        self.CommunicationLinks = [] if CommunicationLinks is None else CommunicationLinks

        self._RemotePoints = []
        self.RemotePoints = [] if RemotePoints is None else RemotePoints

        super(RemoteUnit, self).__init__(**kw_args)

    def getCommunicationLinks(self):
        """RTUs may be attached to communication links.
        """
        return self._CommunicationLinks

    def setCommunicationLinks(self, value):
        for p in self._CommunicationLinks:
            filtered = [q for q in p.RemoteUnits if q != self]
            self._CommunicationLinks._RemoteUnits = filtered
        for r in value:
            if self not in r._RemoteUnits:
                r._RemoteUnits.append(self)
        self._CommunicationLinks = value

    CommunicationLinks = property(getCommunicationLinks, setCommunicationLinks)

    def addCommunicationLinks(self, *CommunicationLinks):
        for obj in CommunicationLinks:
            if self not in obj._RemoteUnits:
                obj._RemoteUnits.append(self)
            self._CommunicationLinks.append(obj)

    def removeCommunicationLinks(self, *CommunicationLinks):
        for obj in CommunicationLinks:
            if self in obj._RemoteUnits:
                obj._RemoteUnits.remove(self)
            self._CommunicationLinks.remove(obj)

    def getRemotePoints(self):
        """Remote points this Remote unit contains.
        """
        return self._RemotePoints

    def setRemotePoints(self, value):
        for x in self._RemotePoints:
            x._RemoteUnit = None
        for y in value:
            y._RemoteUnit = self
        self._RemotePoints = value

    RemotePoints = property(getRemotePoints, setRemotePoints)

    def addRemotePoints(self, *RemotePoints):
        for obj in RemotePoints:
            obj._RemoteUnit = self
            self._RemotePoints.append(obj)

    def removeRemotePoints(self, *RemotePoints):
        for obj in RemotePoints:
            obj._RemoteUnit = None
            self._RemotePoints.remove(obj)

