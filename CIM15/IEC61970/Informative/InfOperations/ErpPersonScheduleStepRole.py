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

class ErpPersonScheduleStepRole(Role):
    """Roles played between Persons and Schedule Steps.Roles played between Persons and Schedule Steps.
    """

    def __init__(self, ErpPerson=None, SwitchingStep=None, *args, **kw_args):
        """Initialises a new 'ErpPersonScheduleStepRole' instance.

        @param ErpPerson:
        @param SwitchingStep:
        """
        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        self._SwitchingStep = None
        self.SwitchingStep = SwitchingStep

        super(ErpPersonScheduleStepRole, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpPerson", "SwitchingStep"]
    _many_refs = []

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.SwitchingStepRoles if x != self]
            self._ErpPerson._SwitchingStepRoles = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            if self not in self._ErpPerson._SwitchingStepRoles:
                self._ErpPerson._SwitchingStepRoles.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

    def getSwitchingStep(self):
        
        return self._SwitchingStep

    def setSwitchingStep(self, value):
        if self._SwitchingStep is not None:
            self._SwitchingStep._ErpPersonRole = None

        self._SwitchingStep = value
        if self._SwitchingStep is not None:
            self._SwitchingStep.ErpPersonRole = None
            self._SwitchingStep._ErpPersonRole = self

    SwitchingStep = property(getSwitchingStep, setSwitchingStep)

