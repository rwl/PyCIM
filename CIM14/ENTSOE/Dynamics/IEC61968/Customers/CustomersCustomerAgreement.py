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

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreIdentifiedObject import CoreIdentifiedObject

class CustomersCustomerAgreement(CoreIdentifiedObject):

    def __init__(self, Equipments=None, *args, **kw_args):
        """Initialises a new 'CustomersCustomerAgreement' instance.

        @param Equipments: 
        """
        self._Equipments = []
        self.Equipments = [] if Equipments is None else Equipments

        super(CustomersCustomerAgreement, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Equipments"]
    _many_refs = ["Equipments"]

    def getEquipments(self):
        """
        """
        return self._Equipments

    def setEquipments(self, value):
        for p in self._Equipments:
            filtered = [q for q in p.CustomerAgreements if q != self]
            self._Equipments._CustomerAgreements = filtered
        for r in value:
            if self not in r._CustomerAgreements:
                r._CustomerAgreements.append(self)
        self._Equipments = value

    Equipments = property(getEquipments, setEquipments)

    def addEquipments(self, *Equipments):
        for obj in Equipments:
            if self not in obj._CustomerAgreements:
                obj._CustomerAgreements.append(self)
            self._Equipments.append(obj)

    def removeEquipments(self, *Equipments):
        for obj in Equipments:
            if self in obj._CustomerAgreements:
                obj._CustomerAgreements.remove(self)
            self._Equipments.remove(obj)

