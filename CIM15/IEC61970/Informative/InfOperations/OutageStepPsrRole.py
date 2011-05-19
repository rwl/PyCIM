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

from CIM15.IEC61970.Informative.InfCommon.Role import Role

class OutageStepPsrRole(Role):
    """Roles played between Power System Resources and Outage Steps. Examples roles include: normal supply, actual supply, interrupting device, restoration device.Roles played between Power System Resources and Outage Steps. Examples roles include: normal supply, actual supply, interrupting device, restoration device.
    """

    def __init__(self, OutageStep=None, ConductingEquipment=None, *args, **kw_args):
        """Initialises a new 'OutageStepPsrRole' instance.

        @param OutageStep:
        @param ConductingEquipment:
        """
        self._OutageStep = None
        self.OutageStep = OutageStep

        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        super(OutageStepPsrRole, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["OutageStep", "ConductingEquipment"]
    _many_refs = []

    def getOutageStep(self):
        
        return self._OutageStep

    def setOutageStep(self, value):
        if self._OutageStep is not None:
            filtered = [x for x in self.OutageStep.ConductingEquipmentRoles if x != self]
            self._OutageStep._ConductingEquipmentRoles = filtered

        self._OutageStep = value
        if self._OutageStep is not None:
            if self not in self._OutageStep._ConductingEquipmentRoles:
                self._OutageStep._ConductingEquipmentRoles.append(self)

    OutageStep = property(getOutageStep, setOutageStep)

    def getConductingEquipment(self):
        
        return self._ConductingEquipment

    def setConductingEquipment(self, value):
        if self._ConductingEquipment is not None:
            filtered = [x for x in self.ConductingEquipment.OutageStepRoles if x != self]
            self._ConductingEquipment._OutageStepRoles = filtered

        self._ConductingEquipment = value
        if self._ConductingEquipment is not None:
            if self not in self._ConductingEquipment._OutageStepRoles:
                self._ConductingEquipment._OutageStepRoles.append(self)

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

