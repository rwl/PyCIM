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

from CIM14.CDPSM.Unbalanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class PowerSystemResource(IdentifiedObject):
    """A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """

    def __init__(self, GeoLocation=None, PSRType=None, *args, **kw_args):
        """Initialises a new 'PowerSystemResource' instance.

        @param GeoLocation: Geographical location of this power system resource.
        @param PSRType: PSRType (custom classification) for this PowerSystemResource.
        """
        self._GeoLocation = None
        self.GeoLocation = GeoLocation

        self._PSRType = None
        self.PSRType = PSRType

        super(PowerSystemResource, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["GeoLocation", "PSRType"]
    _many_refs = []

    def getGeoLocation(self):
        """Geographical location of this power system resource.
        """
        return self._GeoLocation

    def setGeoLocation(self, value):
        if self._GeoLocation is not None:
            filtered = [x for x in self.GeoLocation.PowerSystemResources if x != self]
            self._GeoLocation._PowerSystemResources = filtered

        self._GeoLocation = value
        if self._GeoLocation is not None:
            if self not in self._GeoLocation._PowerSystemResources:
                self._GeoLocation._PowerSystemResources.append(self)

    GeoLocation = property(getGeoLocation, setGeoLocation)

    def getPSRType(self):
        """PSRType (custom classification) for this PowerSystemResource.
        """
        return self._PSRType

    def setPSRType(self, value):
        if self._PSRType is not None:
            filtered = [x for x in self.PSRType.PowerSystemResources if x != self]
            self._PSRType._PowerSystemResources = filtered

        self._PSRType = value
        if self._PSRType is not None:
            if self not in self._PSRType._PowerSystemResources:
                self._PSRType._PowerSystemResources.append(self)

    PSRType = property(getPSRType, setPSRType)

