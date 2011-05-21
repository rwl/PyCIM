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

from CIM14.IEC61970.Contingency.ContingencyElement import ContingencyElement

class ContingencyEquipment(ContingencyElement):
    """A equipment to which the in service status is to change such as a power transformer or AC line segment.
    """

    def __init__(self, contingentStatus="outOfService", Equipment=None, *args, **kw_args):
        """Initialises a new 'ContingencyEquipment' instance.

        @param contingentStatus: The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied. Values are: "outOfService", "inService"
        @param Equipment: The single piece of equipment to which to apply the contingency.
        """
        #: The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied. Values are: "outOfService", "inService"
        self.contingentStatus = contingentStatus

        self._Equipment = None
        self.Equipment = Equipment

        super(ContingencyEquipment, self).__init__(*args, **kw_args)

    _attrs = ["contingentStatus"]
    _attr_types = {"contingentStatus": str}
    _defaults = {"contingentStatus": "outOfService"}
    _enums = {"contingentStatus": "ContingencyEquipmentStatusKind"}
    _refs = ["Equipment"]
    _many_refs = []

    def getEquipment(self):
        """The single piece of equipment to which to apply the contingency.
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

