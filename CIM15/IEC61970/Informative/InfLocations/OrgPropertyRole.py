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

from CIM15.IEC61970.Informative.InfCommon.Role import Role

class OrgPropertyRole(Role):
    """Roles played between Organisations and a given piece of property. For example, the Organisation may be the owner, renter, occupier, taxiing authority, etc.Roles played between Organisations and a given piece of property. For example, the Organisation may be the owner, renter, occupier, taxiing authority, etc.
    """

    def __init__(self, LandProperty=None, ErpOrganisation=None, *args, **kw_args):
        """Initialises a new 'OrgPropertyRole' instance.

        @param LandProperty:
        @param ErpOrganisation:
        """
        self._LandProperty = []
        self.LandProperty = [] if LandProperty is None else LandProperty

        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        super(OrgPropertyRole, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["LandProperty", "ErpOrganisation"]
    _many_refs = ["LandProperty"]

    def getLandProperty(self):
        
        return self._LandProperty

    def setLandProperty(self, value):
        for p in self._LandProperty:
            filtered = [q for q in p.ErpOrganisationRoles if q != self]
            self._LandProperty._ErpOrganisationRoles = filtered
        for r in value:
            if self not in r._ErpOrganisationRoles:
                r._ErpOrganisationRoles.append(self)
        self._LandProperty = value

    LandProperty = property(getLandProperty, setLandProperty)

    def addLandProperty(self, *LandProperty):
        for obj in LandProperty:
            if self not in obj._ErpOrganisationRoles:
                obj._ErpOrganisationRoles.append(self)
            self._LandProperty.append(obj)

    def removeLandProperty(self, *LandProperty):
        for obj in LandProperty:
            if self in obj._ErpOrganisationRoles:
                obj._ErpOrganisationRoles.remove(self)
            self._LandProperty.remove(obj)

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.LandPropertyRoles if x != self]
            self._ErpOrganisation._LandPropertyRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            if self not in self._ErpOrganisation._LandPropertyRoles:
                self._ErpOrganisation._LandPropertyRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

