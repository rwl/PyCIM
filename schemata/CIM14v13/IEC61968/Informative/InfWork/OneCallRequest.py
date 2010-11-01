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

class OneCallRequest(Document):
    """A request for other utilities to mark their underground facilities prior to commencement of construction and/or maintenance.
    """

    def __init__(self, markingInstruction='', markedIndicator=False, explosivesUsed=False, WorkLocations=None, *args, **kw_args):
        """Initializes a new 'OneCallRequest' instance.

        @param markingInstruction: Instructions for marking a dig area, if applicable. 
        @param markedIndicator: True if work location has been marked, for example for a dig area. 
        @param explosivesUsed: True if explosives have been or are planned to be used. 
        @param WorkLocations:
        """
        #: Instructions for marking a dig area, if applicable. 
        self.markingInstruction = markingInstruction

        #: True if work location has been marked, for example for a dig area. 
        self.markedIndicator = markedIndicator

        #: True if explosives have been or are planned to be used. 
        self.explosivesUsed = explosivesUsed

        self._WorkLocations = []
        self.WorkLocations = [] if WorkLocations is None else WorkLocations

        super(OneCallRequest, self).__init__(*args, **kw_args)

    def getWorkLocations(self):
        
        return self._WorkLocations

    def setWorkLocations(self, value):
        for x in self._WorkLocations:
            x._OneCallRequest = None
        for y in value:
            y._OneCallRequest = self
        self._WorkLocations = value

    WorkLocations = property(getWorkLocations, setWorkLocations)

    def addWorkLocations(self, *WorkLocations):
        for obj in WorkLocations:
            obj._OneCallRequest = self
            self._WorkLocations.append(obj)

    def removeWorkLocations(self, *WorkLocations):
        for obj in WorkLocations:
            obj._OneCallRequest = None
            self._WorkLocations.remove(obj)

