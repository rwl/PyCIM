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

class CUContractorItem(IdentifiedObject):
    """Compatible unit contractor item.Compatible unit contractor item.
    """

    def __init__(self, bidAmount=0.0, activityCode='', CompatibleUnits=None, status=None, *args, **kw_args):
        """Initialises a new 'CUContractorItem' instance.

        @param bidAmount: The amount that a given contractor will charge for performing this unit of work. 
        @param activityCode: Activity code identifies a specific and distinguishable unit of work. 
        @param CompatibleUnits:
        @param status:
        """
        #: The amount that a given contractor will charge for performing this unit of work.
        self.bidAmount = bidAmount

        #: Activity code identifies a specific and distinguishable unit of work.
        self.activityCode = activityCode

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self.status = status

        super(CUContractorItem, self).__init__(*args, **kw_args)

    _attrs = ["bidAmount", "activityCode"]
    _attr_types = {"bidAmount": float, "activityCode": str}
    _defaults = {"bidAmount": 0.0, "activityCode": ''}
    _enums = {}
    _refs = ["CompatibleUnits", "status"]
    _many_refs = ["CompatibleUnits"]

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for p in self._CompatibleUnits:
            filtered = [q for q in p.CUContractorItems if q != self]
            self._CompatibleUnits._CUContractorItems = filtered
        for r in value:
            if self not in r._CUContractorItems:
                r._CUContractorItems.append(self)
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self not in obj._CUContractorItems:
                obj._CUContractorItems.append(self)
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self in obj._CUContractorItems:
                obj._CUContractorItems.remove(self)
            self._CompatibleUnits.remove(obj)

    status = None

