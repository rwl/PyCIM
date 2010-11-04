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

from CIM14v13.IEC61968.Common.Location import Location

class WorkLocation(Location):
    """Information about a particular location for various forms of work such as a one call request.
    """

    def __init__(self, block='', nearestIntersection='', subdivision='', lot='', OneCallRequest=None, DesignLocations=None, *args, **kw_args):
        """Initializes a new 'WorkLocation' instance.

        @param block: Name, identifier, or description of the block, if applicable, in which work is to occur. 
        @param nearestIntersection: The names of streets at the nearest intersection to work area. 
        @param subdivision: Name, identifier, or description of the subdivision, if applicable, in which work is to occur. 
        @param lot: Name, identifier, or description of the lot, if applicable, in which work is to occur. 
        @param OneCallRequest:
        @param DesignLocations:
        """
        #: Name, identifier, or description of the block, if applicable, in which work is to occur.
        self.block = block

        #: The names of streets at the nearest intersection to work area.
        self.nearestIntersection = nearestIntersection

        #: Name, identifier, or description of the subdivision, if applicable, in which work is to occur.
        self.subdivision = subdivision

        #: Name, identifier, or description of the lot, if applicable, in which work is to occur.
        self.lot = lot

        self._OneCallRequest = None
        self.OneCallRequest = OneCallRequest

        self._DesignLocations = []
        self.DesignLocations = [] if DesignLocations is None else DesignLocations

        super(WorkLocation, self).__init__(*args, **kw_args)

    def getOneCallRequest(self):
        
        return self._OneCallRequest

    def setOneCallRequest(self, value):
        if self._OneCallRequest is not None:
            filtered = [x for x in self.OneCallRequest.WorkLocations if x != self]
            self._OneCallRequest._WorkLocations = filtered

        self._OneCallRequest = value
        if self._OneCallRequest is not None:
            self._OneCallRequest._WorkLocations.append(self)

    OneCallRequest = property(getOneCallRequest, setOneCallRequest)

    def getDesignLocations(self):
        
        return self._DesignLocations

    def setDesignLocations(self, value):
        for p in self._DesignLocations:
            filtered = [q for q in p.WorkLocations if q != self]
            self._DesignLocations._WorkLocations = filtered
        for r in value:
            if self not in r._WorkLocations:
                r._WorkLocations.append(self)
        self._DesignLocations = value

    DesignLocations = property(getDesignLocations, setDesignLocations)

    def addDesignLocations(self, *DesignLocations):
        for obj in DesignLocations:
            if self not in obj._WorkLocations:
                obj._WorkLocations.append(self)
            self._DesignLocations.append(obj)

    def removeDesignLocations(self, *DesignLocations):
        for obj in DesignLocations:
            if self in obj._WorkLocations:
                obj._WorkLocations.remove(self)
            self._DesignLocations.remove(obj)

