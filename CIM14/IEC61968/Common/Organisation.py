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

