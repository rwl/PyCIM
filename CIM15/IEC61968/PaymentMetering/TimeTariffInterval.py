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

from CIM15.Element import Element

class TimeTariffInterval(Element):
    """One of a sequence of time intervals defined in terms of real time. It is typically used in association with TariffProfile to define the intervals in a time of use tariff structure, where startDateTime simultaneously determines the starting point of this interval and the ending point of the previous interval.One of a sequence of time intervals defined in terms of real time. It is typically used in association with TariffProfile to define the intervals in a time of use tariff structure, where startDateTime simultaneously determines the starting point of this interval and the ending point of the previous interval.
    """

    def __init__(self, startDateTime='', sequenceNumber=0, ConsumptionTariffIntervals=None, TariffProfiles=None, Charges=None, *args, **kw_args):
        """Initialises a new 'TimeTariffInterval' instance.

        @param startDateTime: A real time marker that defines the starting time (typically it is the time of day) for this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle. 
        @param sequenceNumber: A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals. 
        @param ConsumptionTariffIntervals: All consumption tariff intervals that introduce variation in this time of use tariff interval; allows to express e.g., peak hour prices that are different with different consumption blocks.
        @param TariffProfiles: All tariff profiles defined by this time tariff interval.
        @param Charges: All charges used to define this time tariff interval.
        """
        #: A real time marker that defines the starting time (typically it is the time of day) for this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle.
        self.startDateTime = startDateTime

        #: A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals.
        self.sequenceNumber = sequenceNumber

        self._ConsumptionTariffIntervals = []
        self.ConsumptionTariffIntervals = [] if ConsumptionTariffIntervals is None else ConsumptionTariffIntervals

        self._TariffProfiles = []
        self.TariffProfiles = [] if TariffProfiles is None else TariffProfiles

        self._Charges = []
        self.Charges = [] if Charges is None else Charges

        super(TimeTariffInterval, self).__init__(*args, **kw_args)

    _attrs = ["startDateTime", "sequenceNumber"]
    _attr_types = {"startDateTime": str, "sequenceNumber": int}
    _defaults = {"startDateTime": '', "sequenceNumber": 0}
    _enums = {}
    _refs = ["ConsumptionTariffIntervals", "TariffProfiles", "Charges"]
    _many_refs = ["ConsumptionTariffIntervals", "TariffProfiles", "Charges"]

    def getConsumptionTariffIntervals(self):
        """All consumption tariff intervals that introduce variation in this time of use tariff interval; allows to express e.g., peak hour prices that are different with different consumption blocks.
        """
        return self._ConsumptionTariffIntervals

    def setConsumptionTariffIntervals(self, value):
        for p in self._ConsumptionTariffIntervals:
            filtered = [q for q in p.TouTariffIntervals if q != self]
            self._ConsumptionTariffIntervals._TouTariffIntervals = filtered
        for r in value:
            if self not in r._TouTariffIntervals:
                r._TouTariffIntervals.append(self)
        self._ConsumptionTariffIntervals = value

    ConsumptionTariffIntervals = property(getConsumptionTariffIntervals, setConsumptionTariffIntervals)

    def addConsumptionTariffIntervals(self, *ConsumptionTariffIntervals):
        for obj in ConsumptionTariffIntervals:
            if self not in obj._TouTariffIntervals:
                obj._TouTariffIntervals.append(self)
            self._ConsumptionTariffIntervals.append(obj)

    def removeConsumptionTariffIntervals(self, *ConsumptionTariffIntervals):
        for obj in ConsumptionTariffIntervals:
            if self in obj._TouTariffIntervals:
                obj._TouTariffIntervals.remove(self)
            self._ConsumptionTariffIntervals.remove(obj)

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

