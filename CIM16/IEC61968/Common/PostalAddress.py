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


class PostalAddress(object):
    """General purpose postal address information.General purpose postal address information.
    """

    def __init__(self, poBox='', postalCode='', streetDetail=None, townDetail=None):
        """Initialises a new 'PostalAddress' instance.

        @param poBox: Post office box. 
        @param postalCode: Postal code for the address. 
        @param streetDetail: Street detail.
        @param townDetail: Town detail.
        """
        #: Post office box.
        self.poBox = poBox

        #: Postal code for the address.
        self.postalCode = postalCode

        self.streetDetail = streetDetail

        self.townDetail = townDetail


    _attrs = ["poBox", "postalCode"]
    _attr_types = {"poBox": str, "postalCode": str}
    _defaults = {"poBox": '', "postalCode": ''}
    _enums = {}
    _refs = ["streetDetail", "townDetail"]
    _many_refs = []

    # Street detail.
    streetDetail = None

    # Town detail.
    townDetail = None

