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

class TransmissionService(IdentifiedObject):
    """Transmission products along posted transmission path.
    """

    def __init__(self, OfferedAs=None, Offering=None, TransContractFor=None, ScheduledBy=None, Offers=None, ReservedBy_ServiceReservation=None, *args, **kw_args):
        """Initializes a new 'TransmissionService' instance.

        @param OfferedAs: A transmission product is offered as a transmission service along a transmission path.
        @param Offering: A transmission service is offered on a transmission path.
        @param TransContractFor: A TransmissionService is sold according to the terms of a particular OpenAccessProduct agreement.
        @param ScheduledBy: A transmission schedule posts the available transmission capacity for a transmission line.
        @param Offers: The combination of a TransmissionProduct on a TransmissionPath is a TransmissionService, for which the TransmissionProvider must post one or two ATC's (AvailableTransmissionCapacity - Amount of possible flow by  direction).
        @param ReservedBy_ServiceReservation: A service reservation reserves a particular transmission service.
        """
        self._OfferedAs = []
        self.OfferedAs = [] if OfferedAs is None else OfferedAs

        self._Offering = []
        self.Offering = [] if Offering is None else Offering

        self._TransContractFor = None
        self.TransContractFor = TransContractFor

        self._ScheduledBy = []
        self.ScheduledBy = [] if ScheduledBy is None else ScheduledBy

        self._Offers = None
        self.Offers = Offers

        self._ReservedBy_ServiceReservation = []
        self.ReservedBy_ServiceReservation = [] if ReservedBy_ServiceReservation is None else ReservedBy_ServiceReservation

        super(TransmissionService, self).__init__(*args, **kw_args)

    def getOfferedAs(self):
        """A transmission product is offered as a transmission service along a transmission path.
        """
        return self._OfferedAs

    def setOfferedAs(self, value):
        for p in self._OfferedAs:
            filtered = [q for q in p.Offers if q != self]
            self._OfferedAs._Offers = filtered
        for r in value:
            if self not in r._Offers:
                r._Offers.append(self)
        self._OfferedAs = value

    OfferedAs = property(getOfferedAs, setOfferedAs)

    def addOfferedAs(self, *OfferedAs):
        for obj in OfferedAs:
            if self not in obj._Offers:
                obj._Offers.append(self)
            self._OfferedAs.append(obj)

    def removeOfferedAs(self, *OfferedAs):
        for obj in OfferedAs:
            if self in obj._Offers:
                obj._Offers.remove(self)
            self._OfferedAs.remove(obj)

    def getOffering(self):
        """A transmission service is offered on a transmission path.
        """
        return self._Offering

    def setOffering(self, value):
        for p in self._Offering:
            filtered = [q for q in p.OfferedOn if q != self]
            self._Offering._OfferedOn = filtered
        for r in value:
            if self not in r._OfferedOn:
                r._OfferedOn.append(self)
        self._Offering = value

    Offering = property(getOffering, setOffering)

    def addOffering(self, *Offering):
        for obj in Offering:
            if self not in obj._OfferedOn:
                obj._OfferedOn.append(self)
            self._Offering.append(obj)

    def removeOffering(self, *Offering):
        for obj in Offering:
            if self in obj._OfferedOn:
                obj._OfferedOn.remove(self)
            self._Offering.remove(obj)

    def getTransContractFor(self):
        """A TransmissionService is sold according to the terms of a particular OpenAccessProduct agreement.
        """
        return self._TransContractFor

    def setTransContractFor(self, value):
        if self._TransContractFor is not None:
            filtered = [x for x in self.TransContractFor.ProvidedBy_TransmissionService if x != self]
            self._TransContractFor._ProvidedBy_TransmissionService = filtered

        self._TransContractFor = value
        if self._TransContractFor is not None:
            self._TransContractFor._ProvidedBy_TransmissionService.append(self)

    TransContractFor = property(getTransContractFor, setTransContractFor)

    def getScheduledBy(self):
        """A transmission schedule posts the available transmission capacity for a transmission line.
        """
        return self._ScheduledBy

    def setScheduledBy(self, value):
        for p in self._ScheduledBy:
            filtered = [q for q in p.ScheduleFor if q != self]
            self._ScheduledBy._ScheduleFor = filtered
        for r in value:
            if self not in r._ScheduleFor:
                r._ScheduleFor.append(self)
        self._ScheduledBy = value

    ScheduledBy = property(getScheduledBy, setScheduledBy)

    def addScheduledBy(self, *ScheduledBy):
        for obj in ScheduledBy:
            if self not in obj._ScheduleFor:
                obj._ScheduleFor.append(self)
            self._ScheduledBy.append(obj)

    def removeScheduledBy(self, *ScheduledBy):
        for obj in ScheduledBy:
            if self in obj._ScheduleFor:
                obj._ScheduleFor.remove(self)
            self._ScheduledBy.remove(obj)

    def getOffers(self):
        """The combination of a TransmissionProduct on a TransmissionPath is a TransmissionService, for which the TransmissionProvider must post one or two ATC's (AvailableTransmissionCapacity - Amount of possible flow by  direction).
        """
        return self._Offers

    def setOffers(self, value):
        if self._Offers is not None:
            filtered = [x for x in self.Offers.OfferedBy if x != self]
            self._Offers._OfferedBy = filtered

        self._Offers = value
        if self._Offers is not None:
            self._Offers._OfferedBy.append(self)

    Offers = property(getOffers, setOffers)

    def getReservedBy_ServiceReservation(self):
        """A service reservation reserves a particular transmission service.
        """
        return self._ReservedBy_ServiceReservation

    def setReservedBy_ServiceReservation(self, value):
        for p in self._ReservedBy_ServiceReservation:
            filtered = [q for q in p.Reserves_TransmissionService if q != self]
            self._ReservedBy_ServiceReservation._Reserves_TransmissionService = filtered
        for r in value:
            if self not in r._Reserves_TransmissionService:
                r._Reserves_TransmissionService.append(self)
        self._ReservedBy_ServiceReservation = value

    ReservedBy_ServiceReservation = property(getReservedBy_ServiceReservation, setReservedBy_ServiceReservation)

    def addReservedBy_ServiceReservation(self, *ReservedBy_ServiceReservation):
        for obj in ReservedBy_ServiceReservation:
            if self not in obj._Reserves_TransmissionService:
                obj._Reserves_TransmissionService.append(self)
            self._ReservedBy_ServiceReservation.append(obj)

    def removeReservedBy_ServiceReservation(self, *ReservedBy_ServiceReservation):
        for obj in ReservedBy_ServiceReservation:
            if self in obj._Reserves_TransmissionService:
                obj._Reserves_TransmissionService.remove(self)
            self._ReservedBy_ServiceReservation.remove(obj)

