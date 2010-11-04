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

from CIM14v13.Element import Element

class AreaReserveSpec(Element):
    """The control area's reserve specification
    """

    def __init__(self, areaReserveSpecName='', raiseRegMarginReqt=0.0, lowerRegMarginReqt=0.0, primaryReserveReqt=0.0, opReserveReqt=0.0, spinningReserveReqt=0.0, HostControlAreas=None, ReserveEnergyTransaction=None, **kw_args):
        """Initializes a new 'AreaReserveSpec' instance.

        @param areaReserveSpecName: The Identification or name of the control area's reserve specification. A particular specification could correspond to pre-defined power system conditions, e.g., emergency situations. 
        @param raiseRegMarginReqt: Raise active power regulating margin requirement, the amount of generation that can be picked up by control in 10 minutes 
        @param lowerRegMarginReqt: Lower active power regulating margin requirement, the amount of generation that can be dropped by control in 10 minutes 
        @param primaryReserveReqt: Primary active power reserve requirement, where primary reserve is generating capability that is fully available within 10 minutes. Primary reserve is composed of spinning reserve and quick-start reserve. 
        @param opReserveReqt: Operating active power reserve requirement, where operating reserve is the generating capability that is fully available within 30 minutes. Operating reserve is composed of primary reserve (t less than 10 min) and secondary reserve (10 less than t less than 30 min). 
        @param spinningReserveReqt: Spinning active power reserve requirement, spinning reserve is generating capability that is presently synchronized to the network and is fully available within 10 minutes 
        @param HostControlAreas: A control area has one or more area reserve specifications
        @param ReserveEnergyTransaction: A Reserve type of energy transaction can count towards an area reserve specification.
        """
        #: The Identification or name of the control area's reserve specification. A particular specification could correspond to pre-defined power system conditions, e.g., emergency situations.
        self.areaReserveSpecName = areaReserveSpecName

        #: Raise active power regulating margin requirement, the amount of generation that can be picked up by control in 10 minutes
        self.raiseRegMarginReqt = raiseRegMarginReqt

        #: Lower active power regulating margin requirement, the amount of generation that can be dropped by control in 10 minutes
        self.lowerRegMarginReqt = lowerRegMarginReqt

        #: Primary active power reserve requirement, where primary reserve is generating capability that is fully available within 10 minutes. Primary reserve is composed of spinning reserve and quick-start reserve.
        self.primaryReserveReqt = primaryReserveReqt

        #: Operating active power reserve requirement, where operating reserve is the generating capability that is fully available within 30 minutes. Operating reserve is composed of primary reserve (t less than 10 min) and secondary reserve (10 less than t less than 30 min).
        self.opReserveReqt = opReserveReqt

        #: Spinning active power reserve requirement, spinning reserve is generating capability that is presently synchronized to the network and is fully available within 10 minutes
        self.spinningReserveReqt = spinningReserveReqt

        self._HostControlAreas = []
        self.HostControlAreas = [] if HostControlAreas is None else HostControlAreas

        self._ReserveEnergyTransaction = None
        self.ReserveEnergyTransaction = ReserveEnergyTransaction

        super(AreaReserveSpec, self).__init__(**kw_args)

    def getHostControlAreas(self):
        """A control area has one or more area reserve specifications
        """
        return self._HostControlAreas

    def setHostControlAreas(self, value):
        for x in self._HostControlAreas:
            x._AreaReserveSpec = None
        for y in value:
            y._AreaReserveSpec = self
        self._HostControlAreas = value

    HostControlAreas = property(getHostControlAreas, setHostControlAreas)

    def addHostControlAreas(self, *HostControlAreas):
        for obj in HostControlAreas:
            obj._AreaReserveSpec = self
            self._HostControlAreas.append(obj)

    def removeHostControlAreas(self, *HostControlAreas):
        for obj in HostControlAreas:
            obj._AreaReserveSpec = None
            self._HostControlAreas.remove(obj)

    def getReserveEnergyTransaction(self):
        """A Reserve type of energy transaction can count towards an area reserve specification.
        """
        return self._ReserveEnergyTransaction

    def setReserveEnergyTransaction(self, value):
        if self._ReserveEnergyTransaction is not None:
            filtered = [x for x in self.ReserveEnergyTransaction.AreaReserveSpec if x != self]
            self._ReserveEnergyTransaction._AreaReserveSpec = filtered

        self._ReserveEnergyTransaction = value
        if self._ReserveEnergyTransaction is not None:
            self._ReserveEnergyTransaction._AreaReserveSpec.append(self)

    ReserveEnergyTransaction = property(getReserveEnergyTransaction, setReserveEnergyTransaction)

