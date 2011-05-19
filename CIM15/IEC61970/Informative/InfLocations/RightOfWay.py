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

from CIM15.IEC61968.Common.Agreement import Agreement

class RightOfWay(Agreement):
    """A right-of-way (ROW) is for land where it is lawful to use for a public road, an electric power line, etc. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.A right-of-way (ROW) is for land where it is lawful to use for a public road, an electric power line, etc. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """

    def __init__(self, propertyData='', LandProperties=None, *args, **kw_args):
        """Initialises a new 'RightOfWay' instance.

        @param propertyData: Property related information that describes the ROW's land parcel. For example, it may be a deed book number, deed book page number, and parcel number. 
        @param LandProperties: All land properties this right of way applies to.
        """
        #: Property related information that describes the ROW's land parcel. For example, it may be a deed book number, deed book page number, and parcel number.
        self.propertyData = propertyData

        self._LandProperties = []
        self.LandProperties = [] if LandProperties is None else LandProperties

        super(RightOfWay, self).__init__(*args, **kw_args)

    _attrs = ["propertyData"]
    _attr_types = {"propertyData": str}
    _defaults = {"propertyData": ''}
    _enums = {}
    _refs = ["LandProperties"]
    _many_refs = ["LandProperties"]

    def getLandProperties(self):
        """All land properties this right of way applies to.
        """
        return self._LandProperties

    def setLandProperties(self, value):
        for p in self._LandProperties:
            filtered = [q for q in p.RightOfWays if q != self]
            self._LandProperties._RightOfWays = filtered
        for r in value:
            if self not in r._RightOfWays:
                r._RightOfWays.append(self)
        self._LandProperties = value

    LandProperties = property(getLandProperties, setLandProperties)

    def addLandProperties(self, *LandProperties):
        for obj in LandProperties:
            if self not in obj._RightOfWays:
                obj._RightOfWays.append(self)
            self._LandProperties.append(obj)

    def removeLandProperties(self, *LandProperties):
        for obj in LandProperties:
            if self in obj._RightOfWays:
                obj._RightOfWays.remove(self)
            self._LandProperties.remove(obj)

