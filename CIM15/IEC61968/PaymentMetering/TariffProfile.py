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

from CIM15.IEC61968.Common.Document import Document

class TariffProfile(Document):
    """A schedule of charges; structure associated with Tariff that allows the definition of complex tarif structures such as step and time of use when used in conjunction with TimeTariffInterval and Charge. Inherited 'status.value' is defined in the context of the utility's business rules, for example: active, inactive, etc.A schedule of charges; structure associated with Tariff that allows the definition of complex tarif structures such as step and time of use when used in conjunction with TimeTariffInterval and Charge. Inherited 'status.value' is defined in the context of the utility's business rules, for example: active, inactive, etc.
    """

    def __init__(self, tariffCycle='', Tariffs=None, ConsumptionTariffIntervals=None, TimeTariffIntervals=None, *args, **kw_args):
        """Initialises a new 'TariffProfile' instance.

        @param tariffCycle: The frequency at which the tariff charge schedule is repeated Examples are: once off on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc. At the end of each cycle, the business rules are reset to start from the beginning again. 
        @param Tariffs: All tariffs defined by this tariff profile.
        @param ConsumptionTariffIntervals: All consumption tariff intervals used to define this tariff profile.
        @param TimeTariffIntervals: All time tariff intervals used to define this tariff profile.
        """
        #: The frequency at which the tariff charge schedule is repeated Examples are: once off on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc. At the end of each cycle, the business rules are reset to start from the beginning again.
        self.tariffCycle = tariffCycle

        self._Tariffs = []
        self.Tariffs = [] if Tariffs is None else Tariffs

        self._ConsumptionTariffIntervals = []
        self.ConsumptionTariffIntervals = [] if ConsumptionTariffIntervals is None else ConsumptionTariffIntervals

        self._TimeTariffIntervals = []
        self.TimeTariffIntervals = [] if TimeTariffIntervals is None else TimeTariffIntervals

        super(TariffProfile, self).__init__(*args, **kw_args)

    _attrs = ["tariffCycle"]
    _attr_types = {"tariffCycle": str}
    _defaults = {"tariffCycle": ''}
    _enums = {}
    _refs = ["Tariffs", "ConsumptionTariffIntervals", "TimeTariffIntervals"]
    _many_refs = ["Tariffs", "ConsumptionTariffIntervals", "TimeTariffIntervals"]

    def getTariffs(self):
        """All tariffs defined by this tariff profile.
        """
        return self._Tariffs

    def setTariffs(self, value):
        for p in self._Tariffs:
            filtered = [q for q in p.TariffProfiles if q != self]
            self._Tariffs._TariffProfiles = filtered
        for r in value:
            if self not in r._TariffProfiles:
                r._TariffProfiles.append(self)
        self._Tariffs = value

    Tariffs = property(getTariffs, setTariffs)

    def addTariffs(self, *Tariffs):
        for obj in Tariffs:
            if self not in obj._TariffProfiles:
                obj._TariffProfiles.append(self)
            self._Tariffs.append(obj)

    def removeTariffs(self, *Tariffs):
        for obj in Tariffs:
            if self in obj._TariffProfiles:
                obj._TariffProfiles.remove(self)
            self._Tariffs.remove(obj)

    def getConsumptionTariffIntervals(self):
        """All consumption tariff intervals used to define this tariff profile.
        """
        return self._ConsumptionTariffIntervals

    def setConsumptionTariffIntervals(self, value):
        for p in self._ConsumptionTariffIntervals:
            filtered = [q for q in p.TariffProfiles if q != self]
            self._ConsumptionTariffIntervals._TariffProfiles = filtered
        for r in value:
            if self not in r._TariffProfiles:
                r._TariffProfiles.append(self)
        self._ConsumptionTariffIntervals = value

    ConsumptionTariffIntervals = property(getConsumptionTariffIntervals, setConsumptionTariffIntervals)

    def addConsumptionTariffIntervals(self, *ConsumptionTariffIntervals):
        for obj in ConsumptionTariffIntervals:
            if self not in obj._TariffProfiles:
                obj._TariffProfiles.append(self)
            self._ConsumptionTariffIntervals.append(obj)

    def removeConsumptionTariffIntervals(self, *ConsumptionTariffIntervals):
        for obj in ConsumptionTariffIntervals:
            if self in obj._TariffProfiles:
                obj._TariffProfiles.remove(self)
            self._ConsumptionTariffIntervals.remove(obj)

    def getTimeTariffIntervals(self):
        """All time tariff intervals used to define this tariff profile.
        """
        return self._TimeTariffIntervals

    def setTimeTariffIntervals(self, value):
        for p in self._TimeTariffIntervals:
            filtered = [q for q in p.TariffProfiles if q != self]
            self._TimeTariffIntervals._TariffProfiles = filtered
        for r in value:
            if self not in r._TariffProfiles:
                r._TariffProfiles.append(self)
        self._TimeTariffIntervals = value

    TimeTariffIntervals = property(getTimeTariffIntervals, setTimeTariffIntervals)

    def addTimeTariffIntervals(self, *TimeTariffIntervals):
        for obj in TimeTariffIntervals:
            if self not in obj._TariffProfiles:
                obj._TariffProfiles.append(self)
            self._TimeTariffIntervals.append(obj)

    def removeTimeTariffIntervals(self, *TimeTariffIntervals):
        for obj in TimeTariffIntervals:
            if self in obj._TariffProfiles:
                obj._TariffProfiles.remove(self)
            self._TimeTariffIntervals.remove(obj)

