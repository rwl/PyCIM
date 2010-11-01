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

class TransmissionRightOfWay(PowerSystemResource):
    """A collection of transmission lines that are close proximity to each other.
    """

    def __init__(self, TransmissionCorridor=None, Lines=None, *args, **kw_args):
        """Initializes a new 'TransmissionRightOfWay' instance.

        @param TransmissionCorridor: A transmission right-of-way is a member of a transmission corridor
        @param Lines: A transmission line can be part of a transmission corridor
        """
        self._TransmissionCorridor = None
        self.TransmissionCorridor = TransmissionCorridor

        self._Lines = []
        self.Lines = [] if Lines is None else Lines

        super(TransmissionRightOfWay, self).__init__(*args, **kw_args)

    def getTransmissionCorridor(self):
        """A transmission right-of-way is a member of a transmission corridor
        """
        return self._TransmissionCorridor

    def setTransmissionCorridor(self, value):
        if self._TransmissionCorridor is not None:
            filtered = [x for x in self.TransmissionCorridor.TransmissionRightOfWays if x != self]
            self._TransmissionCorridor._TransmissionRightOfWays = filtered

        self._TransmissionCorridor = value
        if self._TransmissionCorridor is not None:
            self._TransmissionCorridor._TransmissionRightOfWays.append(self)

    TransmissionCorridor = property(getTransmissionCorridor, setTransmissionCorridor)

    def getLines(self):
        """A transmission line can be part of a transmission corridor
        """
        return self._Lines

    def setLines(self, value):
        for x in self._Lines:
            x._TransmissionRightOfWay = None
        for y in value:
            y._TransmissionRightOfWay = self
        self._Lines = value

    Lines = property(getLines, setLines)

    def addLines(self, *Lines):
        for obj in Lines:
            obj._TransmissionRightOfWay = self
            self._Lines.append(obj)

    def removeLines(self, *Lines):
        for obj in Lines:
            obj._TransmissionRightOfWay = None
            self._Lines.remove(obj)

