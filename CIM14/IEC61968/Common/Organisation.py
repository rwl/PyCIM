# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Organisation(IdentifiedObject):
    """Organisation that might have roles as utility, contractor, supplier, manufacturer, customer, etc.
    """

    def __init__(self, electronicAddress=None, streetAddress=None, phone2=None, phone1=None, postalAddress=None, *args, **kw_args):
        """Initialises a new 'Organisation' instance.

        @param electronicAddress: Electronic address.
        @param streetAddress: Street address.
        @param phone2: Additional phone number.
        @param phone1: Phone number.
        @param postalAddress: Postal address, potentially different than 'streetAddress' (e.g., another city).
        """
        self.electronicAddress = electronicAddress

        self.streetAddress = streetAddress

        self.phone2 = phone2

        self.phone1 = phone1

        self.postalAddress = postalAddress

        super(Organisation, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["electronicAddress", "streetAddress", "phone2", "phone1", "postalAddress"]
    _many_refs = []

    # Electronic address.
    electronicAddress = None

    # Street address.
    streetAddress = None

    # Additional phone number.
    phone2 = None

    # Phone number.
    phone1 = None

    # Postal address, potentially different than 'streetAddress' (e.g., another city).
    postalAddress = None

