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

from CIM14v13.IEC61970.Core.EquipmentContainer import EquipmentContainer

class Line(EquipmentContainer):
    """Contains equipment beyond a substation belonging to a power transmission line.
    """

    def __init__(self, TransmissionRightOfWay=None, Flowgates=None, Region=None, **kw_args):
        """Initializes a new 'Line' instance.

        @param TransmissionRightOfWay: A transmission line can be part of a transmission corridor
        @param Flowgates:
        @param Region: A Line can be contained by a SubGeographical Region.
        """
        self._TransmissionRightOfWay = None
        self.TransmissionRightOfWay = TransmissionRightOfWay

        self._Flowgates = []
        self.Flowgates = [] if Flowgates is None else Flowgates

        self._Region = None
        self.Region = Region

        super(Line, self).__init__(**kw_args)

    def getTransmissionRightOfWay(self):
        """A transmission line can be part of a transmission corridor
        """
        return self._TransmissionRightOfWay

    def setTransmissionRightOfWay(self, value):
        if self._TransmissionRightOfWay is not None:
            filtered = [x for x in self.TransmissionRightOfWay.Lines if x != self]
            self._TransmissionRightOfWay._Lines = filtered

        self._TransmissionRightOfWay = value
        if self._TransmissionRightOfWay is not None:
            self._TransmissionRightOfWay._Lines.append(self)

    TransmissionRightOfWay = property(getTransmissionRightOfWay, setTransmissionRightOfWay)

    def getFlowgates(self):
        
        return self._Flowgates

    def setFlowgates(self, value):
        for p in self._Flowgates:
            filtered = [q for q in p.Lines if q != self]
            self._Flowgates._Lines = filtered
        for r in value:
            if self not in r._Lines:
                r._Lines.append(self)
        self._Flowgates = value

    Flowgates = property(getFlowgates, setFlowgates)

    def addFlowgates(self, *Flowgates):
        for obj in Flowgates:
            if self not in obj._Lines:
                obj._Lines.append(self)
            self._Flowgates.append(obj)

    def removeFlowgates(self, *Flowgates):
        for obj in Flowgates:
            if self in obj._Lines:
                obj._Lines.remove(self)
            self._Flowgates.remove(obj)

    def getRegion(self):
        """A Line can be contained by a SubGeographical Region.
        """
        return self._Region

    def setRegion(self, value):
        if self._Region is not None:
            filtered = [x for x in self.Region.Lines if x != self]
            self._Region._Lines = filtered

        self._Region = value
        if self._Region is not None:
            self._Region._Lines.append(self)

    Region = property(getRegion, setRegion)

