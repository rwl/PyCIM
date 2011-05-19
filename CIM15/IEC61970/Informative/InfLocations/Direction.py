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

from CIM15.Element import Element

class Direction(Element):
    """Used for navigating from one location to another location.Used for navigating from one location to another location.
    """

    def __init__(self, directionInfo='', Location=None, *args, **kw_args):
        """Initialises a new 'Direction' instance.

        @param directionInfo: Detailed directional information. 
        @param Location:
        """
        #: Detailed directional information.
        self.directionInfo = directionInfo

        self._Location = None
        self.Location = Location

        super(Direction, self).__init__(*args, **kw_args)

    _attrs = ["directionInfo"]
    _attr_types = {"directionInfo": str}
    _defaults = {"directionInfo": ''}
    _enums = {}
    _refs = ["Location"]
    _many_refs = []

    def getLocation(self):
        
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.Directions if x != self]
            self._Location._Directions = filtered

        self._Location = value
        if self._Location is not None:
            if self not in self._Location._Directions:
                self._Location._Directions.append(self)

    Location = property(getLocation, setLocation)

