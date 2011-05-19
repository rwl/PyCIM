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

class Organisation(IdentifiedObject):
    """Organisation that might have roles as utility, contractor, supplier, manufacturer, customer, etc.Organisation that might have roles as utility, contractor, supplier, manufacturer, customer, etc.
    """

    def __init__(self, phone2=None, phone1=None, streetAddress=None, postalAddress=None, electronicAddress=None, BusinessRoles=None, *args, **kw_args):
        """Initialises a new 'Organisation' instance.

        @param phone2: Additional phone number.
        @param phone1: Phone number.
        @param streetAddress: Street address.
        @param postalAddress: Postal address, potentially different than 'streetAddress' (e.g., another city).
        @param electronicAddress: Electronic address.
        @param BusinessRoles:
        """
        self.phone2 = phone2

        self.phone1 = phone1

        self.streetAddress = streetAddress

        self.postalAddress = postalAddress

        self.electronicAddress = electronicAddress

        self._BusinessRoles = []
        self.BusinessRoles = [] if BusinessRoles is None else BusinessRoles

        super(Organisation, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["phone2", "phone1", "streetAddress", "postalAddress", "electronicAddress", "BusinessRoles"]
    _many_refs = ["BusinessRoles"]

    # Additional phone number.
    phone2 = None

    # Phone number.
    phone1 = None

    # Street address.
    streetAddress = None

    # Postal address, potentially different than 'streetAddress' (e.g., another city).
    postalAddress = None

    # Electronic address.
    electronicAddress = None

    def getBusinessRoles(self):
        
        return self._BusinessRoles

    def setBusinessRoles(self, value):
        for p in self._BusinessRoles:
            filtered = [q for q in p.Organisations if q != self]
            self._BusinessRoles._Organisations = filtered
        for r in value:
            if self not in r._Organisations:
                r._Organisations.append(self)
        self._BusinessRoles = value

    BusinessRoles = property(getBusinessRoles, setBusinessRoles)

    def addBusinessRoles(self, *BusinessRoles):
        for obj in BusinessRoles:
            if self not in obj._Organisations:
                obj._Organisations.append(self)
            self._BusinessRoles.append(obj)

    def removeBusinessRoles(self, *BusinessRoles):
        for obj in BusinessRoles:
            if self in obj._Organisations:
                obj._Organisations.remove(self)
            self._BusinessRoles.remove(obj)

