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

class TransmissionCorridor(PowerSystemResource):
    """A corridor containing one or more rights of way
    """

    def __init__(self, TransmissionRightOfWays=None, ContainedIn=None, **kw_args):
        """Initializes a new 'TransmissionCorridor' instance.

        @param TransmissionRightOfWays: A transmission right-of-way is a member of a transmission corridor
        @param ContainedIn: A TransmissionPath is contained in a TransmissionCorridor.
        """
        self._TransmissionRightOfWays = []
        self.TransmissionRightOfWays = [] if TransmissionRightOfWays is None else TransmissionRightOfWays

        self._ContainedIn = []
        self.ContainedIn = [] if ContainedIn is None else ContainedIn

        super(TransmissionCorridor, self).__init__(**kw_args)

    def getTransmissionRightOfWays(self):
        """A transmission right-of-way is a member of a transmission corridor
        """
        return self._TransmissionRightOfWays

    def setTransmissionRightOfWays(self, value):
        for x in self._TransmissionRightOfWays:
            x._TransmissionCorridor = None
        for y in value:
            y._TransmissionCorridor = self
        self._TransmissionRightOfWays = value

    TransmissionRightOfWays = property(getTransmissionRightOfWays, setTransmissionRightOfWays)

    def addTransmissionRightOfWays(self, *TransmissionRightOfWays):
        for obj in TransmissionRightOfWays:
            obj._TransmissionCorridor = self
            self._TransmissionRightOfWays.append(obj)

    def removeTransmissionRightOfWays(self, *TransmissionRightOfWays):
        for obj in TransmissionRightOfWays:
            obj._TransmissionCorridor = None
            self._TransmissionRightOfWays.remove(obj)

    def getContainedIn(self):
        """A TransmissionPath is contained in a TransmissionCorridor.
        """
        return self._ContainedIn

    def setContainedIn(self, value):
        for x in self._ContainedIn:
            x._For = None
        for y in value:
            y._For = self
        self._ContainedIn = value

    ContainedIn = property(getContainedIn, setContainedIn)

    def addContainedIn(self, *ContainedIn):
        for obj in ContainedIn:
            obj._For = self
            self._ContainedIn.append(obj)

    def removeContainedIn(self, *ContainedIn):
        for obj in ContainedIn:
            obj._For = None
            self._ContainedIn.remove(obj)

