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

class Hazard(IdentifiedObject):
    """A hazard is any object or condition that is a danger for causing loss or perils to an asset and/or people. Examples of hazards are trees growing under overhead power lines, a park being located by a substation (i.e., children climb fence to recover a ball), a lake near an overhead distribution line (fishing pole/line contacting power lines), etc.A hazard is any object or condition that is a danger for causing loss or perils to an asset and/or people. Examples of hazards are trees growing under overhead power lines, a park being located by a substation (i.e., children climb fence to recover a ball), a lake near an overhead distribution line (fishing pole/line contacting power lines), etc.
    """

    def __init__(self, category='', Locations=None, status=None, *args, **kw_args):
        """Initialises a new 'Hazard' instance.

        @param category: Category by utility's corporate standards and practices. 
        @param Locations: The point or polygon location of a given hazard.
        @param status:
        """
        #: Category by utility's corporate standards and practices.
        self.category = category

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self.status = status

        super(Hazard, self).__init__(*args, **kw_args)

    _attrs = ["category"]
    _attr_types = {"category": str}
    _defaults = {"category": ''}
    _enums = {}
    _refs = ["Locations", "status"]
    _many_refs = ["Locations"]

    def getLocations(self):
        """The point or polygon location of a given hazard.
        """
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.Hazards if q != self]
            self._Locations._Hazards = filtered
        for r in value:
            if self not in r._Hazards:
                r._Hazards.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._Hazards:
                obj._Hazards.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._Hazards:
                obj._Hazards.remove(self)
            self._Locations.remove(obj)

    status = None

