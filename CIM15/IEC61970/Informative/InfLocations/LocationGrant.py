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

class LocationGrant(Agreement):
    """A grant provides a right, as defined by type, for a parcel of land. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.A grant provides a right, as defined by type, for a parcel of land. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """

    def __init__(self, propertyData='', LandProperty=None, *args, **kw_args):
        """Initialises a new 'LocationGrant' instance.

        @param propertyData: Property related information that describes the Grant's land parcel. For example, it may be a deed book number, deed book page number, and parcel number. 
        @param LandProperty: Land property this location grant applies to.
        """
        #: Property related information that describes the Grant's land parcel. For example, it may be a deed book number, deed book page number, and parcel number.
        self.propertyData = propertyData

        self._LandProperty = None
        self.LandProperty = LandProperty

        super(LocationGrant, self).__init__(*args, **kw_args)

    _attrs = ["propertyData"]
    _attr_types = {"propertyData": str}
    _defaults = {"propertyData": ''}
    _enums = {}
    _refs = ["LandProperty"]
    _many_refs = []

    def getLandProperty(self):
        """Land property this location grant applies to.
        """
        return self._LandProperty

    def setLandProperty(self, value):
        if self._LandProperty is not None:
            filtered = [x for x in self.LandProperty.LocationGrants if x != self]
            self._LandProperty._LocationGrants = filtered

        self._LandProperty = value
        if self._LandProperty is not None:
            if self not in self._LandProperty._LocationGrants:
                self._LandProperty._LocationGrants.append(self)

    LandProperty = property(getLandProperty, setLandProperty)

