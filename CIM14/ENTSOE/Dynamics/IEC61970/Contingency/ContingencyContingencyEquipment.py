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

class ContingencyContingencyEquipment(CoreIdentifiedObject):

    def __init__(self, Equipment=None, *args, **kw_args):
        """Initialises a new 'ContingencyContingencyEquipment' instance.

        @param Equipment: 
        """
        self._Equipment = None
        self.Equipment = Equipment

        super(ContingencyContingencyEquipment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Equipment"]
    _many_refs = []

    def getEquipment(self):
        """
        """
        return self._Equipment

    def setEquipment(self, value):
        if self._Equipment is not None:
            filtered = [x for x in self.Equipment.ContingencyEquipment if x != self]
            self._Equipment._ContingencyEquipment = filtered

        self._Equipment = value
        if self._Equipment is not None:
            if self not in self._Equipment._ContingencyEquipment:
                self._Equipment._ContingencyEquipment.append(self)

    Equipment = property(getEquipment, setEquipment)

