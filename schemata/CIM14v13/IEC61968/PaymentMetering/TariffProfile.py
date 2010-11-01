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

from CIM14v13.IEC61968.Common.Document import Document

class TariffProfile(Document):
    """A schedule of charges; structure associated with Tariff that allows the definition of complex tarif structures such as step and time of use when used in conjunction with TimeTariffInterval and Charge. Inherited 'status.value' is defined in the context of the utility's business rules, for example: active, inactive, etc.
    """

    def __init__(self, tariffCycle='', ConsumptionTariffIntervals=None, Tariffs=None, TimeTariffIntervals=None, *args, **kw_args):
        """Initializes a new 'TariffProfile' instance.

        @param tariffCycle: The frequency at which the tariff charge schedule is repeated Examples are: once off on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc. At the end of each cycle, the business rules are reset to start from the beginning again. 
        @param ConsumptionTariffIntervals: All consumption tariff intervals used to define this tariff profile.
        @param Tariffs: All tariffs defined by this tariff profile.
        @param TimeTariffIntervals: All time tariff intervals used to define this tariff profile.
        """
        #: The frequency at which the tariff charge schedule is repeated Examples are: once off on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc. At the end of each cycle, the business rules are reset to start from the beginning again. 
        self.tariffCycle = tariffCycle

        self._ConsumptionTariffIntervals = []
        self.ConsumptionTariffIntervals = [] if ConsumptionTariffIntervals is None else ConsumptionTariffIntervals

        self._Tariffs = []
        self.Tariffs = [] if Tariffs is None else Tariffs

        self._TimeTariffIntervals = []
        self.TimeTariffIntervals = [] if TimeTariffIntervals is None else TimeTariffIntervals

        super(TariffProfile, self).__init__(*args, **kw_args)

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

