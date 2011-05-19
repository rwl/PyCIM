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

class OrgOrgRole(Role):
    """Roles played between Organisations and other Organisations. This includes role ups for ogranisations, cost centers, profit centers, regulatory reporting, etc. Note that the parent and child relationship is indicated by the name on each end of the association.Roles played between Organisations and other Organisations. This includes role ups for ogranisations, cost centers, profit centers, regulatory reporting, etc. Note that the parent and child relationship is indicated by the name on each end of the association.
    """

    def __init__(self, clientID='', ParentOrganisation=None, ChildOrganisation=None, *args, **kw_args):
        """Initialises a new 'OrgOrgRole' instance.

        @param clientID: Identifiers of the organisation held by another organisation, such as a government agency (federal, state, province, city, county), financial institution (Dun and Bradstreet), etc. 
        @param ParentOrganisation:
        @param ChildOrganisation:
        """
        #: Identifiers of the organisation held by another organisation, such as a government agency (federal, state, province, city, county), financial institution (Dun and Bradstreet), etc.
        self.clientID = clientID

        self._ParentOrganisation = None
        self.ParentOrganisation = ParentOrganisation

        self._ChildOrganisation = None
        self.ChildOrganisation = ChildOrganisation

        super(OrgOrgRole, self).__init__(*args, **kw_args)

    _attrs = ["clientID"]
    _attr_types = {"clientID": str}
    _defaults = {"clientID": ''}
    _enums = {}
    _refs = ["ParentOrganisation", "ChildOrganisation"]
    _many_refs = []

    def getParentOrganisation(self):
        
        return self._ParentOrganisation

    def setParentOrganisation(self, value):
        if self._ParentOrganisation is not None:
            filtered = [x for x in self.ParentOrganisation.ChildOrganisationRoles if x != self]
            self._ParentOrganisation._ChildOrganisationRoles = filtered

        self._ParentOrganisation = value
        if self._ParentOrganisation is not None:
            if self not in self._ParentOrganisation._ChildOrganisationRoles:
                self._ParentOrganisation._ChildOrganisationRoles.append(self)

    ParentOrganisation = property(getParentOrganisation, setParentOrganisation)

    def getChildOrganisation(self):
        
        return self._ChildOrganisation

    def setChildOrganisation(self, value):
        if self._ChildOrganisation is not None:
            filtered = [x for x in self.ChildOrganisation.ParentOrganisationRoles if x != self]
            self._ChildOrganisation._ParentOrganisationRoles = filtered

        self._ChildOrganisation = value
        if self._ChildOrganisation is not None:
            if self not in self._ChildOrganisation._ParentOrganisationRoles:
                self._ChildOrganisation._ParentOrganisationRoles.append(self)

    ChildOrganisation = property(getChildOrganisation, setChildOrganisation)

