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

class CULaborCode(IdentifiedObject):
    """Labor code associated with various compatible unit labor items.Labor code associated with various compatible unit labor items.
    """

    def __init__(self, code='', CULaborItems=None, status=None, *args, **kw_args):
        """Initialises a new 'CULaborCode' instance.

        @param code: Labor code. 
        @param CULaborItems:
        @param status:
        """
        #: Labor code.
        self.code = code

        self._CULaborItems = []
        self.CULaborItems = [] if CULaborItems is None else CULaborItems

        self.status = status

        super(CULaborCode, self).__init__(*args, **kw_args)

    _attrs = ["code"]
    _attr_types = {"code": str}
    _defaults = {"code": ''}
    _enums = {}
    _refs = ["CULaborItems", "status"]
    _many_refs = ["CULaborItems"]

    def getCULaborItems(self):
        
        return self._CULaborItems

    def setCULaborItems(self, value):
        for x in self._CULaborItems:
            x.CULaborCode = None
        for y in value:
            y._CULaborCode = self
        self._CULaborItems = value

    CULaborItems = property(getCULaborItems, setCULaborItems)

    def addCULaborItems(self, *CULaborItems):
        for obj in CULaborItems:
            obj.CULaborCode = self

    def removeCULaborItems(self, *CULaborItems):
        for obj in CULaborItems:
            obj.CULaborCode = None

    status = None

