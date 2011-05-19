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

class BusinessRole(IdentifiedObject):
    """A business role that this organisation plays. A single organisation typically performs many functions, each one described as a role.A business role that this organisation plays. A single organisation typically performs many functions, each one described as a role.
    """

    def __init__(self, category='', Organisations=None, status=None, *args, **kw_args):
        """Initialises a new 'BusinessRole' instance.

        @param category: Category by utility's corporate standards and practices. 
        @param Organisations:
        @param status:
        """
        #: Category by utility's corporate standards and practices.
        self.category = category

        self._Organisations = []
        self.Organisations = [] if Organisations is None else Organisations

        self.status = status

        super(BusinessRole, self).__init__(*args, **kw_args)

    _attrs = ["category"]
    _attr_types = {"category": str}
    _defaults = {"category": ''}
    _enums = {}
    _refs = ["Organisations", "status"]
    _many_refs = ["Organisations"]

    def getOrganisations(self):
        
        return self._Organisations

    def setOrganisations(self, value):
        for p in self._Organisations:
            filtered = [q for q in p.BusinessRoles if q != self]
            self._Organisations._BusinessRoles = filtered
        for r in value:
            if self not in r._BusinessRoles:
                r._BusinessRoles.append(self)
        self._Organisations = value

    Organisations = property(getOrganisations, setOrganisations)

    def addOrganisations(self, *Organisations):
        for obj in Organisations:
            if self not in obj._BusinessRoles:
                obj._BusinessRoles.append(self)
            self._Organisations.append(obj)

    def removeOrganisations(self, *Organisations):
        for obj in Organisations:
            if self in obj._BusinessRoles:
                obj._BusinessRoles.remove(self)
            self._Organisations.remove(obj)

    status = None

