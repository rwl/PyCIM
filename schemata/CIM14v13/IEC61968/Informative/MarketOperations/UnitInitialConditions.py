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

class UnitInitialConditions(IdentifiedObject):
    """Resource status at the end of a given clearing period.
    """

    def __init__(self, resourceStatus=0, cumStatusChanges=0, statusDate='', resourceMW=0.0, timeInStatus=0.0, cumEnergy=None, GeneratingUnit=None, **kw_args):
        """Initializes a new 'UnitInitialConditions' instance.

        @param resourceStatus: Resource status at the end of previous clearing period:  0 - off-line  1 - on-line production  2 - in shutdown process  3 - in startup process 
        @param cumStatusChanges: Cumulative number of status changes of the resource. 
        @param statusDate: Time and date for resourceStatus 
        @param resourceMW: Resource MW output at the end of previous clearing period. 
        @param timeInStatus: Time in market trading intervals the resource is in the state as of the end of the previous clearing period. 
        @param cumEnergy: Cumulative energy production over trading period. 
        @param GeneratingUnit:
        """
        #: Resource status at the end of previous clearing period:  0 - off-line  1 - on-line production  2 - in shutdown process  3 - in startup process
        self.resourceStatus = resourceStatus

        #: Cumulative number of status changes of the resource.
        self.cumStatusChanges = cumStatusChanges

        #: Time and date for resourceStatus
        self.statusDate = statusDate

        #: Resource MW output at the end of previous clearing period.
        self.resourceMW = resourceMW

        #: Time in market trading intervals the resource is in the state as of the end of the previous clearing period.
        self.timeInStatus = timeInStatus

        #: Cumulative energy production over trading period.
        self.cumEnergy = cumEnergy

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(UnitInitialConditions, self).__init__(**kw_args)

    def getGeneratingUnit(self):
        
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        if self._GeneratingUnit is not None:
            filtered = [x for x in self.GeneratingUnit.UnitInitialConditions if x != self]
            self._GeneratingUnit._UnitInitialConditions = filtered

        self._GeneratingUnit = value
        if self._GeneratingUnit is not None:
            self._GeneratingUnit._UnitInitialConditions.append(self)

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

