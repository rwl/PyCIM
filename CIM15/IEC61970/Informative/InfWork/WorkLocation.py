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

from CIM15.IEC61968.Common.Location import Location

class WorkLocation(Location):
    """Information about a particular location for various forms of work such as a one call request.Information about a particular location for various forms of work such as a one call request.
    """

    def __init__(self, subdivision='', nearestIntersection='', block='', lot='', OneCallRequest=None, DesignLocations=None, *args, **kw_args):
        """Initialises a new 'WorkLocation' instance.

        @param subdivision: Name, identifier, or description of the subdivision, if applicable, in which work is to occur. 
        @param nearestIntersection: The names of streets at the nearest intersection to work area. 
        @param block: Name, identifier, or description of the block, if applicable, in which work is to occur. 
        @param lot: Name, identifier, or description of the lot, if applicable, in which work is to occur. 
        @param OneCallRequest:
        @param DesignLocations:
        """
        #: Name, identifier, or description of the subdivision, if applicable, in which work is to occur.
        self.subdivision = subdivision

        #: The names of streets at the nearest intersection to work area.
        self.nearestIntersection = nearestIntersection

        #: Name, identifier, or description of the block, if applicable, in which work is to occur.
        self.block = block

        #: Name, identifier, or description of the lot, if applicable, in which work is to occur.
        self.lot = lot

        self._OneCallRequest = None
        self.OneCallRequest = OneCallRequest

        self._DesignLocations = []
        self.DesignLocations = [] if DesignLocations is None else DesignLocations

        super(WorkLocation, self).__init__(*args, **kw_args)

    _attrs = ["subdivision", "nearestIntersection", "block", "lot"]
    _attr_types = {"subdivision": str, "nearestIntersection": str, "block": str, "lot": str}
    _defaults = {"subdivision": '', "nearestIntersection": '', "block": '', "lot": ''}
    _enums = {}
    _refs = ["OneCallRequest", "DesignLocations"]
    _many_refs = ["DesignLocations"]

    def getOneCallRequest(self):
        
        return self._OneCallRequest

    def setOneCallRequest(self, value):
        if self._OneCallRequest is not None:
            filtered = [x for x in self.OneCallRequest.WorkLocations if x != self]
            self._OneCallRequest._WorkLocations = filtered

        self._OneCallRequest = value
        if self._OneCallRequest is not None:
            if self not in self._OneCallRequest._WorkLocations:
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

