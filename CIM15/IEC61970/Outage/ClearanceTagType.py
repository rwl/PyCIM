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

class ClearanceTagType(IdentifiedObject):
    """Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.
    """

    def __init__(self, ClearanceTags=None, *args, **kw_args):
        """Initialises a new 'ClearanceTagType' instance.

        @param ClearanceTags: The ClearanceTags currently being defined for this type.
        """
        self._ClearanceTags = []
        self.ClearanceTags = [] if ClearanceTags is None else ClearanceTags

        super(ClearanceTagType, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ClearanceTags"]
    _many_refs = ["ClearanceTags"]

    def getClearanceTags(self):
        """The ClearanceTags currently being defined for this type.
        """
        return self._ClearanceTags

    def setClearanceTags(self, value):
        for x in self._ClearanceTags:
            x.ClearanceTagType = None
        for y in value:
            y._ClearanceTagType = self
        self._ClearanceTags = value

    ClearanceTags = property(getClearanceTags, setClearanceTags)

    def addClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj.ClearanceTagType = self

    def removeClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj.ClearanceTagType = None

