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

class ServiceReservation(Element):
    """A ServiceReservation is a reservation for either AncillaryServices or TransmissionServices. In the case of TransmissionServices, this is the right to some amount of AvailableTransmissionCapacity for a product on a path in a direction for some specific period of time
    """

    def __init__(self, Holds=None, Resells=None, Reserves_AncillaryServices=None, Sells=None, Reserves_TransmissionService=None, *args, **kw_args):
        """Initializes a new 'ServiceReservation' instance.

        @param Holds: A Marketer holds title to a ServiceReservation.
        @param Resells: A ServiceReservation may be resold by a Marketer.
        @param Reserves_AncillaryServices: A ServiceReservation guarantees a certain AncillaryService.
        @param Sells: A TransmissionProvider sells the right to transmit energy across the wires in a ServiceReservation.
        @param Reserves_TransmissionService: A service reservation reserves a particular transmission service.
        """
        self._Holds = None
        self.Holds = Holds

        self._Resells = None
        self.Resells = Resells

        self._Reserves_AncillaryServices = []
        self.Reserves_AncillaryServices = [] if Reserves_AncillaryServices is None else Reserves_AncillaryServices

        self._Sells = None
        self.Sells = Sells

        self._Reserves_TransmissionService = []
        self.Reserves_TransmissionService = [] if Reserves_TransmissionService is None else Reserves_TransmissionService

        super(ServiceReservation, self).__init__(*args, **kw_args)

    def getHolds(self):
        """A Marketer holds title to a ServiceReservation.
        """
        return self._Holds

    def setHolds(self, value):
        if self._Holds is not None:
            filtered = [x for x in self.Holds.HeldBy if x != self]
            self._Holds._HeldBy = filtered

        self._Holds = value
        if self._Holds is not None:
            self._Holds._HeldBy.append(self)

    Holds = property(getHolds, setHolds)

    def getResells(self):
        """A ServiceReservation may be resold by a Marketer.
        """
        return self._Resells

    def setResells(self, value):
        if self._Resells is not None:
            self._Resells._ResoldBy = None

        self._Resells = value
        if self._Resells is not None:
            self._Resells._ResoldBy = self

    Resells = property(getResells, setResells)

    def getReserves_AncillaryServices(self):
        """A ServiceReservation guarantees a certain AncillaryService.
        """
        return self._Reserves_AncillaryServices

    def setReserves_AncillaryServices(self, value):
        for x in self._Reserves_AncillaryServices:
            x._ReservedBy_ServiceReservation = None
        for y in value:
            y._ReservedBy_ServiceReservation = self
        self._Reserves_AncillaryServices = value

    Reserves_AncillaryServices = property(getReserves_AncillaryServices, setReserves_AncillaryServices)

    def addReserves_AncillaryServices(self, *Reserves_AncillaryServices):
        for obj in Reserves_AncillaryServices:
            obj._ReservedBy_ServiceReservation = self
            self._Reserves_AncillaryServices.append(obj)

    def removeReserves_AncillaryServices(self, *Reserves_AncillaryServices):
        for obj in Reserves_AncillaryServices:
            obj._ReservedBy_ServiceReservation = None
            self._Reserves_AncillaryServices.remove(obj)

    def getSells(self):
        """A TransmissionProvider sells the right to transmit energy across the wires in a ServiceReservation.
        """
        return self._Sells

    def setSells(self, value):
        if self._Sells is not None:
            filtered = [x for x in self.Sells.SoldBy if x != self]
            self._Sells._SoldBy = filtered

        self._Sells = value
        if self._Sells is not None:
            self._Sells._SoldBy.append(self)

    Sells = property(getSells, setSells)

    def getReserves_TransmissionService(self):
        """A service reservation reserves a particular transmission service.
        """
        return self._Reserves_TransmissionService

    def setReserves_TransmissionService(self, value):
        for p in self._Reserves_TransmissionService:
            filtered = [q for q in p.ReservedBy_ServiceReservation if q != self]
            self._Reserves_TransmissionService._ReservedBy_ServiceReservation = filtered
        for r in value:
            if self not in r._ReservedBy_ServiceReservation:
                r._ReservedBy_ServiceReservation.append(self)
        self._Reserves_TransmissionService = value

    Reserves_TransmissionService = property(getReserves_TransmissionService, setReserves_TransmissionService)

    def addReserves_TransmissionService(self, *Reserves_TransmissionService):
        for obj in Reserves_TransmissionService:
            if self not in obj._ReservedBy_ServiceReservation:
                obj._ReservedBy_ServiceReservation.append(self)
            self._Reserves_TransmissionService.append(obj)

    def removeReserves_TransmissionService(self, *Reserves_TransmissionService):
        for obj in Reserves_TransmissionService:
            if self in obj._ReservedBy_ServiceReservation:
                obj._ReservedBy_ServiceReservation.remove(self)
            self._Reserves_TransmissionService.remove(obj)

