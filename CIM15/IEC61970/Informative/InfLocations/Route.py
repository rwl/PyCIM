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

class Route(IdentifiedObject):
    """Route that is followed, for example by service crews.Route that is followed, for example by service crews.
    """

    def __init__(self, category='', Crews=None, status=None, Locations=None, *args, **kw_args):
        """Initialises a new 'Route' instance.

        @param category: Category by utility's work management standards and practices. 
        @param Crews:
        @param status:
        @param Locations:
        """
        #: Category by utility's work management standards and practices.
        self.category = category

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self.status = status

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        super(Route, self).__init__(*args, **kw_args)

    _attrs = ["category"]
    _attr_types = {"category": str}
    _defaults = {"category": ''}
    _enums = {}
    _refs = ["Crews", "status", "Locations"]
    _many_refs = ["Crews", "Locations"]

    def getCrews(self):
        
        return self._Crews

    def setCrews(self, value):
        for x in self._Crews:
            x.Route = None
        for y in value:
            y._Route = self
        self._Crews = value

    Crews = property(getCrews, setCrews)

    def addCrews(self, *Crews):
        for obj in Crews:
            obj.Route = self

    def removeCrews(self, *Crews):
        for obj in Crews:
            obj.Route = None

    status = None

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.Routes if q != self]
            self._Locations._Routes = filtered
        for r in value:
            if self not in r._Routes:
                r._Routes.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._Routes:
                obj._Routes.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._Routes:
                obj._Routes.remove(self)
            self._Locations.remove(obj)

