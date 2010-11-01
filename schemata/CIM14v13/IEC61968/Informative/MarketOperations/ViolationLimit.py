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

from CIM14v13.IEC61970.Meas.Limit import Limit

class ViolationLimit(Limit):
    """A type of limit that indicates if it is enforced and, through association, the organisation responsible for setting the limit.
    """

    def __init__(self, enforced=False, Organisations=None, Flowgate=None, Season=None, Measurement=None, *args, **kw_args):
        """Initializes a new 'ViolationLimit' instance.

        @param enforced: True if limit is enforced. 
        @param Organisations:
        @param Flowgate:
        @param Season: Limits may differ based on the season
        @param Measurement:
        """
        #: True if limit is enforced. 
        self.enforced = enforced

        self._Organisations = []
        self.Organisations = [] if Organisations is None else Organisations

        self._Flowgate = None
        self.Flowgate = Flowgate

        self._Season = None
        self.Season = Season

        self._Measurement = None
        self.Measurement = Measurement

        super(ViolationLimit, self).__init__(*args, **kw_args)

    def getOrganisations(self):
        
        return self._Organisations

    def setOrganisations(self, value):
        for p in self._Organisations:
            filtered = [q for q in p.ViolationLimits if q != self]
            self._Organisations._ViolationLimits = filtered
        for r in value:
            if self not in r._ViolationLimits:
                r._ViolationLimits.append(self)
        self._Organisations = value

    Organisations = property(getOrganisations, setOrganisations)

    def addOrganisations(self, *Organisations):
        for obj in Organisations:
            if self not in obj._ViolationLimits:
                obj._ViolationLimits.append(self)
            self._Organisations.append(obj)

    def removeOrganisations(self, *Organisations):
        for obj in Organisations:
            if self in obj._ViolationLimits:
                obj._ViolationLimits.remove(self)
            self._Organisations.remove(obj)

    def getFlowgate(self):
        
        return self._Flowgate

    def setFlowgate(self, value):
        if self._Flowgate is not None:
            filtered = [x for x in self.Flowgate.ViolationLimits if x != self]
            self._Flowgate._ViolationLimits = filtered

        self._Flowgate = value
        if self._Flowgate is not None:
            self._Flowgate._ViolationLimits.append(self)

    Flowgate = property(getFlowgate, setFlowgate)

    def getSeason(self):
        """Limits may differ based on the season
        """
        return self._Season

    def setSeason(self, value):
        if self._Season is not None:
            filtered = [x for x in self.Season.ViolationLimits if x != self]
            self._Season._ViolationLimits = filtered

        self._Season = value
        if self._Season is not None:
            self._Season._ViolationLimits.append(self)

    Season = property(getSeason, setSeason)

    def getMeasurement(self):
        
        return self._Measurement

    def setMeasurement(self, value):
        if self._Measurement is not None:
            filtered = [x for x in self.Measurement.ViolationLimits if x != self]
            self._Measurement._ViolationLimits = filtered

        self._Measurement = value
        if self._Measurement is not None:
            self._Measurement._ViolationLimits.append(self)

    Measurement = property(getMeasurement, setMeasurement)

