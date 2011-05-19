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

class OrgPsrRole(Role):
    """Roles played between Organisations and Power System Resources.Roles played between Organisations and Power System Resources.
    """

    def __init__(self, ErpOrganisation=None, PowerSystemResource=None, *args, **kw_args):
        """Initialises a new 'OrgPsrRole' instance.

        @param ErpOrganisation:
        @param PowerSystemResource:
        """
        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        super(OrgPsrRole, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpOrganisation", "PowerSystemResource"]
    _many_refs = []

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.PowerSystemResourceRoles if x != self]
            self._ErpOrganisation._PowerSystemResourceRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            if self not in self._ErpOrganisation._PowerSystemResourceRoles:
                self._ErpOrganisation._PowerSystemResourceRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

    def getPowerSystemResource(self):
        
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.ErpOrganisationRoles if x != self]
            self._PowerSystemResource._ErpOrganisationRoles = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            if self not in self._PowerSystemResource._ErpOrganisationRoles:
                self._PowerSystemResource._ErpOrganisationRoles.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

