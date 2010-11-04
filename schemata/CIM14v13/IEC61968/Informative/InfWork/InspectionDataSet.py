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

from CIM14v13.IEC61968.Informative.InfAssets.ProcedureDataSet import ProcedureDataSet

class InspectionDataSet(ProcedureDataSet):
    """Documents the result of one inspection, a type of Procedure, for a given attribute of an asset.
    """

    def __init__(self, locationCondition='', AccordingToSchedules=None, *args, **kw_args):
        """Initializes a new 'InspectionDataSet' instance.

        @param locationCondition: Description of the conditions of the location where the asset resides. 
        @param AccordingToSchedules:
        """
        #: Description of the conditions of the location where the asset resides.
        self.locationCondition = locationCondition

        self._AccordingToSchedules = []
        self.AccordingToSchedules = [] if AccordingToSchedules is None else AccordingToSchedules

        super(InspectionDataSet, self).__init__(*args, **kw_args)

    def getAccordingToSchedules(self):
        
        return self._AccordingToSchedules

    def setAccordingToSchedules(self, value):
        for x in self._AccordingToSchedules:
            x._ForInspectionDataSet = None
        for y in value:
            y._ForInspectionDataSet = self
        self._AccordingToSchedules = value

    AccordingToSchedules = property(getAccordingToSchedules, setAccordingToSchedules)

    def addAccordingToSchedules(self, *AccordingToSchedules):
        for obj in AccordingToSchedules:
            obj._ForInspectionDataSet = self
            self._AccordingToSchedules.append(obj)

    def removeAccordingToSchedules(self, *AccordingToSchedules):
        for obj in AccordingToSchedules:
            obj._ForInspectionDataSet = None
            self._AccordingToSchedules.remove(obj)

