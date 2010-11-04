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

class TimeTariffInterval(Element):
    """One of a sequence of time intervals defined in terms of real time. It is typically used in association with TariffProfile to define the intervals in a time of use tariff structure, where startDateTime simultaneously determines the starting point of this interval and the ending point of the previous interval.
    """

    def __init__(self, startDateTime='', sequenceNumber=0, TariffProfiles=None, Charges=None, **kw_args):
        """Initializes a new 'TimeTariffInterval' instance.

        @param startDateTime: A real time marker that defines the starting time (typically it is the time of day) for this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle. 
        @param sequenceNumber: A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals. 
        @param TariffProfiles: All tariff profiles defined by this time tariff interval.
        @param Charges: All charges used to define this time tariff interval.
        """
        #: A real time marker that defines the starting time (typically it is the time of day) for this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle.
        self.startDateTime = startDateTime

        #: A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals.
        self.sequenceNumber = sequenceNumber

        self._TariffProfiles = []
        self.TariffProfiles = [] if TariffProfiles is None else TariffProfiles

        self._Charges = []
        self.Charges = [] if Charges is None else Charges

        super(TimeTariffInterval, self).__init__(**kw_args)

    def getTariffProfiles(self):
        """All tariff profiles defined by this time tariff interval.
        """
        return self._TariffProfiles

    def setTariffProfiles(self, value):
        for p in self._TariffProfiles:
            filtered = [q for q in p.TimeTariffIntervals if q != self]
            self._TariffProfiles._TimeTariffIntervals = filtered
        for r in value:
            if self not in r._TimeTariffIntervals:
                r._TimeTariffIntervals.append(self)
        self._TariffProfiles = value

    TariffProfiles = property(getTariffProfiles, setTariffProfiles)

    def addTariffProfiles(self, *TariffProfiles):
        for obj in TariffProfiles:
            if self not in obj._TimeTariffIntervals:
                obj._TimeTariffIntervals.append(self)
            self._TariffProfiles.append(obj)

    def removeTariffProfiles(self, *TariffProfiles):
        for obj in TariffProfiles:
            if self in obj._TimeTariffIntervals:
                obj._TimeTariffIntervals.remove(self)
            self._TariffProfiles.remove(obj)

    def getCharges(self):
        """All charges used to define this time tariff interval.
        """
        return self._Charges

    def setCharges(self, value):
        for p in self._Charges:
            filtered = [q for q in p.TimeTariffIntervals if q != self]
            self._Charges._TimeTariffIntervals = filtered
        for r in value:
            if self not in r._TimeTariffIntervals:
                r._TimeTariffIntervals.append(self)
        self._Charges = value

    Charges = property(getCharges, setCharges)

    def addCharges(self, *Charges):
        for obj in Charges:
            if self not in obj._TimeTariffIntervals:
                obj._TimeTariffIntervals.append(self)
            self._Charges.append(obj)

    def removeCharges(self, *Charges):
        for obj in Charges:
            if self in obj._TimeTariffIntervals:
                obj._TimeTariffIntervals.remove(self)
            self._Charges.remove(obj)

