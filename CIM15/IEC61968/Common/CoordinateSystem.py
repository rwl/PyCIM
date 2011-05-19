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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class CoordinateSystem(IdentifiedObject):
    """Coordinate reference system.Coordinate reference system.
    """

    def __init__(self, crsUrn='', Diagrams=None, Location=None, GmlDiagramObjects=None, *args, **kw_args):
        """Initialises a new 'CoordinateSystem' instance.

        @param crsUrn: A Uniform Resource Name (URN) for the coordinate reference system (crs) used to define 'Location.PositionPoints'. An example would be the European Petroleum Survey Group (EPSG) code for a coordinate reference system, defined in URN under the Open Geospatial Consortium (OGC) namespace as: urn:ogc :def:uom:EPSG::XXXX, where XXXX is an EPSG code (a full list of codes can be found at the EPSG Registry website http://www.epsg-registry.org/). To define the coordinate system as being WGS84 (latitude, longitude) using an EPSG OGC, this attribute would be urn:ogc:def:uom:EPSG::4236. A profile should limit this code to a set of allowed URNs agreed to by all sending and receiving parties. 
        @param Diagrams:
        @param Location: All locations described with position points in this coordinate system.
        @param GmlDiagramObjects:
        """
        #: A Uniform Resource Name (URN) for the coordinate reference system (crs) used to define 'Location.PositionPoints'. An example would be the European Petroleum Survey Group (EPSG) code for a coordinate reference system, defined in URN under the Open Geospatial Consortium (OGC) namespace as: urn:ogc :def:uom:EPSG::XXXX, where XXXX is an EPSG code (a full list of codes can be found at the EPSG Registry website http://www.epsg-registry.org/). To define the coordinate system as being WGS84 (latitude, longitude) using an EPSG OGC, this attribute would be urn:ogc:def:uom:EPSG::4236. A profile should limit this code to a set of allowed URNs agreed to by all sending and receiving parties.
        self.crsUrn = crsUrn

        self._Diagrams = []
        self.Diagrams = [] if Diagrams is None else Diagrams

        self._Location = []
        self.Location = [] if Location is None else Location

        self._GmlDiagramObjects = []
        self.GmlDiagramObjects = [] if GmlDiagramObjects is None else GmlDiagramObjects

        super(CoordinateSystem, self).__init__(*args, **kw_args)

    _attrs = ["crsUrn"]
    _attr_types = {"crsUrn": str}
    _defaults = {"crsUrn": ''}
    _enums = {}
    _refs = ["Diagrams", "Location", "GmlDiagramObjects"]
    _many_refs = ["Diagrams", "Location", "GmlDiagramObjects"]

    def getDiagrams(self):
        
        return self._Diagrams

    def setDiagrams(self, value):
        for x in self._Diagrams:
            x.CoordinateSystem = None
        for y in value:
            y._CoordinateSystem = self
        self._Diagrams = value

    Diagrams = property(getDiagrams, setDiagrams)

    def addDiagrams(self, *Diagrams):
        for obj in Diagrams:
            obj.CoordinateSystem = self

    def removeDiagrams(self, *Diagrams):
        for obj in Diagrams:
            obj.CoordinateSystem = None

    def getLocation(self):
        """All locations described with position points in this coordinate system.
        """
        return self._Location

    def setLocation(self, value):
        for x in self._Location:
            x.CoordinateSystem = None
        for y in value:
            y._CoordinateSystem = self
        self._Location = value

    Location = property(getLocation, setLocation)

    def addLocation(self, *Location):
        for obj in Location:
            obj.CoordinateSystem = self

    def removeLocation(self, *Location):
        for obj in Location:
            obj.CoordinateSystem = None

    def getGmlDiagramObjects(self):
        
        return self._GmlDiagramObjects

    def setGmlDiagramObjects(self, value):
        for p in self._GmlDiagramObjects:
            filtered = [q for q in p.CoordinateSystems if q != self]
            self._GmlDiagramObjects._CoordinateSystems = filtered
        for r in value:
            if self not in r._CoordinateSystems:
                r._CoordinateSystems.append(self)
        self._GmlDiagramObjects = value

    GmlDiagramObjects = property(getGmlDiagramObjects, setGmlDiagramObjects)

    def addGmlDiagramObjects(self, *GmlDiagramObjects):
        for obj in GmlDiagramObjects:
            if self not in obj._CoordinateSystems:
                obj._CoordinateSystems.append(self)
            self._GmlDiagramObjects.append(obj)

    def removeGmlDiagramObjects(self, *GmlDiagramObjects):
        for obj in GmlDiagramObjects:
            if self in obj._CoordinateSystems:
                obj._CoordinateSystems.remove(self)
            self._GmlDiagramObjects.remove(obj)

