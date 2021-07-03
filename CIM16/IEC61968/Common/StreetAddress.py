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


class StreetAddress(object):
    """General purpose street address information.General purpose street address information.
    """

    def __init__(self, status=None, streetDetail=None, townDetail=None):
        """Initialises a new 'StreetAddress' instance.

        @param status: Status of this address.
        @param streetDetail: Street detail.
        @param townDetail: Town detail.
        """
        self.status = status

        self.streetDetail = streetDetail

        self.townDetail = townDetail


    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["status", "streetDetail", "townDetail"]
    _many_refs = []

    # Status of this address.
    status = None

    # Street detail.
    streetDetail = None

    # Town detail.
    townDetail = None

