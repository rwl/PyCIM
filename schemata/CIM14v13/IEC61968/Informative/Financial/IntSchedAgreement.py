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

from CIM14v13.IEC61968.Common.Agreement import Agreement

class IntSchedAgreement(Agreement):
    """A type of agreement that provides the default method by which interchange schedules are to be integrated to obtain hourly energy schedules for accounting.
    """

    def __init__(self, defaultIntegrationMethod=None, Organisations=None, *args, **kw_args):
        """Initializes a new 'IntSchedAgreement' instance.

        @param defaultIntegrationMethod: The default method by which interchange schedules are to be integrated to obtain hourly energy schedules for accounting. Method #1 is to integrate the instantaneous schedule between the hourly boundaries. Method #2 compensates for any up/down ramping that occurs across the hourly boundary (this is called block accounting). 
        @param Organisations:
        """
        #: The default method by which interchange schedules are to be integrated to obtain hourly energy schedules for accounting. Method #1 is to integrate the instantaneous schedule between the hourly boundaries. Method #2 compensates for any up/down ramping that occurs across the hourly boundary (this is called block accounting). 
        self.defaultIntegrationMethod = defaultIntegrationMethod

        self._Organisations = []
        self.Organisations = [] if Organisations is None else Organisations

        super(IntSchedAgreement, self).__init__(*args, **kw_args)

    def getOrganisations(self):
        
        return self._Organisations

    def setOrganisations(self, value):
        for p in self._Organisations:
            filtered = [q for q in p.IntSchedAgreement if q != self]
            self._Organisations._IntSchedAgreement = filtered
        for r in value:
            if self not in r._IntSchedAgreement:
                r._IntSchedAgreement.append(self)
        self._Organisations = value

    Organisations = property(getOrganisations, setOrganisations)

    def addOrganisations(self, *Organisations):
        for obj in Organisations:
            if self not in obj._IntSchedAgreement:
                obj._IntSchedAgreement.append(self)
            self._Organisations.append(obj)

    def removeOrganisations(self, *Organisations):
        for obj in Organisations:
            if self in obj._IntSchedAgreement:
                obj._IntSchedAgreement.remove(self)
            self._Organisations.remove(obj)

