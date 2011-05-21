# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class RemoteUnit(PowerSystemResource):
    """A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc.
    """

    def __init__(self, remoteUnitType="IED", CommunicationLinks=None, RemotePoints=None, *args, **kw_args):
        """Initialises a new 'RemoteUnit' instance.

        @param remoteUnitType: Type of remote unit. Values are: "IED", "ControlCenter", "RTU", "SubstationControlSystem"
        @param CommunicationLinks: RTUs may be attached to communication links.
        @param RemotePoints: Remote points this Remote unit contains.
        """
        #: Type of remote unit. Values are: "IED", "ControlCenter", "RTU", "SubstationControlSystem"
        self.remoteUnitType = remoteUnitType

        self._CommunicationLinks = []
        self.CommunicationLinks = [] if CommunicationLinks is None else CommunicationLinks

        self._RemotePoints = []
        self.RemotePoints = [] if RemotePoints is None else RemotePoints

        super(RemoteUnit, self).__init__(*args, **kw_args)

    _attrs = ["remoteUnitType"]
    _attr_types = {"remoteUnitType": str}
    _defaults = {"remoteUnitType": "IED"}
    _enums = {"remoteUnitType": "RemoteUnitType"}
    _refs = ["CommunicationLinks", "RemotePoints"]
    _many_refs = ["CommunicationLinks", "RemotePoints"]

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
            x.RemoteUnit = None
        for y in value:
            y._RemoteUnit = self
        self._RemotePoints = value

    RemotePoints = property(getRemotePoints, setRemotePoints)

    def addRemotePoints(self, *RemotePoints):
        for obj in RemotePoints:
            obj.RemoteUnit = self

    def removeRemotePoints(self, *RemotePoints):
        for obj in RemotePoints:
            obj.RemoteUnit = None

