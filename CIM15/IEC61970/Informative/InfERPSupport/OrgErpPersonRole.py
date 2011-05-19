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

class OrgErpPersonRole(Role):
    """Roles played between Persons and Organisations.Roles played between Persons and Organisations.
    """

    def __init__(self, clientID='', ErpPerson=None, ErpOrganisation=None, *args, **kw_args):
        """Initialises a new 'OrgErpPersonRole' instance.

        @param clientID: Identifiers of the person held by an organisation, such as a government agency (federal, state, province, city, county), financial institutions, etc. 
        @param ErpPerson:
        @param ErpOrganisation:
        """
        #: Identifiers of the person held by an organisation, such as a government agency (federal, state, province, city, county), financial institutions, etc.
        self.clientID = clientID

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        super(OrgErpPersonRole, self).__init__(*args, **kw_args)

    _attrs = ["clientID"]
    _attr_types = {"clientID": str}
    _defaults = {"clientID": ''}
    _enums = {}
    _refs = ["ErpPerson", "ErpOrganisation"]
    _many_refs = []

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.ErpOrganisationRoles if x != self]
            self._ErpPerson._ErpOrganisationRoles = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            if self not in self._ErpPerson._ErpOrganisationRoles:
                self._ErpPerson._ErpOrganisationRoles.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.ErpPersonRoles if x != self]
            self._ErpOrganisation._ErpPersonRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            if self not in self._ErpOrganisation._ErpPersonRoles:
                self._ErpOrganisation._ErpPersonRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

