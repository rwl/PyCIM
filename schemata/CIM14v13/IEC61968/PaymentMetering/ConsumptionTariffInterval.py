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

class ConsumptionTariffInterval(Element):
    """One of a sequence of intervals defined in terms of consumption quantity of a service such as electricity, water, gas, etc. It is typically used in association with TariffProfile to define the steps or blocks in a step tariff structure, where startValue simultaneously defines the entry value of this step and the closing value of the previous step. Where consumption is &gt;= startValue it falls within this interval and where consumption is &lt; startValue it falls within the previous interval.
    """

    def __init__(self, sequenceNumber=0, startValue=0.0, Charges=None, TariffProfiles=None, *args, **kw_args):
        """Initializes a new 'ConsumptionTariffInterval' instance.

        @param sequenceNumber: A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals. 
        @param startValue: The lowest level of consumption that defines the starting point of this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle. 
        @param Charges: All charges used to define this consumption tariff interval.
        @param TariffProfiles: All tariff profiles defined by this consumption tariff interval.
        """
        #: A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals. 
        self.sequenceNumber = sequenceNumber

        #: The lowest level of consumption that defines the starting point of this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle. 
        self.startValue = startValue

        self._Charges = []
        self.Charges = [] if Charges is None else Charges

        self._TariffProfiles = []
        self.TariffProfiles = [] if TariffProfiles is None else TariffProfiles

        super(ConsumptionTariffInterval, self).__init__(*args, **kw_args)

    def getCharges(self):
        """All charges used to define this consumption tariff interval.
        """
        return self._Charges

    def setCharges(self, value):
        for p in self._Charges:
            filtered = [q for q in p.ConsumptionTariffIntervals if q != self]
            self._Charges._ConsumptionTariffIntervals = filtered
        for r in value:
            if self not in r._ConsumptionTariffIntervals:
                r._ConsumptionTariffIntervals.append(self)
        self._Charges = value

    Charges = property(getCharges, setCharges)

    def addCharges(self, *Charges):
        for obj in Charges:
            if self not in obj._ConsumptionTariffIntervals:
                obj._ConsumptionTariffIntervals.append(self)
            self._Charges.append(obj)

    def removeCharges(self, *Charges):
        for obj in Charges:
            if self in obj._ConsumptionTariffIntervals:
                obj._ConsumptionTariffIntervals.remove(self)
            self._Charges.remove(obj)

    def getTariffProfiles(self):
        """All tariff profiles defined by this consumption tariff interval.
        """
        return self._TariffProfiles

    def setTariffProfiles(self, value):
        for p in self._TariffProfiles:
            filtered = [q for q in p.ConsumptionTariffIntervals if q != self]
            self._TariffProfiles._ConsumptionTariffIntervals = filtered
        for r in value:
            if self not in r._ConsumptionTariffIntervals:
                r._ConsumptionTariffIntervals.append(self)
        self._TariffProfiles = value

    TariffProfiles = property(getTariffProfiles, setTariffProfiles)

    def addTariffProfiles(self, *TariffProfiles):
        for obj in TariffProfiles:
            if self not in obj._ConsumptionTariffIntervals:
                obj._ConsumptionTariffIntervals.append(self)
            self._TariffProfiles.append(obj)

    def removeTariffProfiles(self, *TariffProfiles):
        for obj in TariffProfiles:
            if self in obj._ConsumptionTariffIntervals:
                obj._ConsumptionTariffIntervals.remove(self)
            self._TariffProfiles.remove(obj)

