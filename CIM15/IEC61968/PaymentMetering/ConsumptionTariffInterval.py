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

class ConsumptionTariffInterval(Element):
    """One of a sequence of intervals defined in terms of consumption quantity of a service such as electricity, water, gas, etc. It is typically used in association with TariffProfile to define the steps or blocks in a step tariff structure, where startValue simultaneously defines the entry value of this step and the closing value of the previous step. Where consumption is &gt;= startValue it falls within this interval and where consumption is &lt; startValue it falls within the previous interval.One of a sequence of intervals defined in terms of consumption quantity of a service such as electricity, water, gas, etc. It is typically used in association with TariffProfile to define the steps or blocks in a step tariff structure, where startValue simultaneously defines the entry value of this step and the closing value of the previous step. Where consumption is &gt;= startValue it falls within this interval and where consumption is &lt; startValue it falls within the previous interval.
    """

    def __init__(self, startValue=0.0, sequenceNumber=0, Charges=None, TariffProfiles=None, TouTariffIntervals=None, *args, **kw_args):
        """Initialises a new 'ConsumptionTariffInterval' instance.

        @param startValue: The lowest level of consumption that defines the starting point of this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle. 
        @param sequenceNumber: A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals. 
        @param Charges: All charges used to define this consumption tariff interval.
        @param TariffProfiles: All tariff profiles defined by this consumption tariff interval.
        @param TouTariffIntervals: All time of use tariff intervals influenced by this consumption tariff interval.
        """
        #: The lowest level of consumption that defines the starting point of this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle.
        self.startValue = startValue

        #: A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals.
        self.sequenceNumber = sequenceNumber

        self._Charges = []
        self.Charges = [] if Charges is None else Charges

        self._TariffProfiles = []
        self.TariffProfiles = [] if TariffProfiles is None else TariffProfiles

        self._TouTariffIntervals = []
        self.TouTariffIntervals = [] if TouTariffIntervals is None else TouTariffIntervals

        super(ConsumptionTariffInterval, self).__init__(*args, **kw_args)

    _attrs = ["startValue", "sequenceNumber"]
    _attr_types = {"startValue": float, "sequenceNumber": int}
    _defaults = {"startValue": 0.0, "sequenceNumber": 0}
    _enums = {}
    _refs = ["Charges", "TariffProfiles", "TouTariffIntervals"]
    _many_refs = ["Charges", "TariffProfiles", "TouTariffIntervals"]

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

    def getTouTariffIntervals(self):
        """All time of use tariff intervals influenced by this consumption tariff interval.
        """
        return self._TouTariffIntervals

    def setTouTariffIntervals(self, value):
        for p in self._TouTariffIntervals:
            filtered = [q for q in p.ConsumptionTariffIntervals if q != self]
            self._TouTariffIntervals._ConsumptionTariffIntervals = filtered
        for r in value:
            if self not in r._ConsumptionTariffIntervals:
                r._ConsumptionTariffIntervals.append(self)
        self._TouTariffIntervals = value

    TouTariffIntervals = property(getTouTariffIntervals, setTouTariffIntervals)

    def addTouTariffIntervals(self, *TouTariffIntervals):
        for obj in TouTariffIntervals:
            if self not in obj._ConsumptionTariffIntervals:
                obj._ConsumptionTariffIntervals.append(self)
            self._TouTariffIntervals.append(obj)

    def removeTouTariffIntervals(self, *TouTariffIntervals):
        for obj in TouTariffIntervals:
            if self in obj._ConsumptionTariffIntervals:
                obj._ConsumptionTariffIntervals.remove(self)
            self._TouTariffIntervals.remove(obj)

