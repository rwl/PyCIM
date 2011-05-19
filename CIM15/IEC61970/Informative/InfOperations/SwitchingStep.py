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

class SwitchingStep(IdentifiedObject):
    """A single step within a SwitchingSchedule. Could be a switching operation (applying a network alteration), or issuing a safety document. Note: Inherited attribute IdentifiedObject.name is used to hold the sequence number.A single step within a SwitchingSchedule. Could be a switching operation (applying a network alteration), or issuing a safety document. Note: Inherited attribute IdentifiedObject.name is used to hold the sequence number.
    """

    def __init__(self, statusKind="instructed", text='', requiredControlAction='', desiredEndState='', SafetyDocument=None, requiredControlActionInterval=None, SwitchingSchedule=None, PowerSystemResources=None, ErpPersonRole=None, *args, **kw_args):
        """Initialises a new 'SwitchingStep' instance.

        @param statusKind: Status of this SwitchingStep. Values are: "instructed", "confirmed", "proposed", "aborted", "skipped"
        @param text: Information regarding this switching schedule step. 
        @param requiredControlAction: Control actions required to perform this step. 
        @param desiredEndState: Desired end state for the associated PowerSystemResource as a result of this schedule step. 
        @param SafetyDocument:
        @param requiredControlActionInterval: Interval between 'requiredControlAction' was issued and completed.
        @param SwitchingSchedule:
        @param PowerSystemResources:
        @param ErpPersonRole:
        """
        #: Status of this SwitchingStep. Values are: "instructed", "confirmed", "proposed", "aborted", "skipped"
        self.statusKind = statusKind

        #: Information regarding this switching schedule step.
        self.text = text

        #: Control actions required to perform this step.
        self.requiredControlAction = requiredControlAction

        #: Desired end state for the associated PowerSystemResource as a result of this schedule step.
        self.desiredEndState = desiredEndState

        self._SafetyDocument = None
        self.SafetyDocument = SafetyDocument

        self.requiredControlActionInterval = requiredControlActionInterval

        self._SwitchingSchedule = None
        self.SwitchingSchedule = SwitchingSchedule

        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        self._ErpPersonRole = None
        self.ErpPersonRole = ErpPersonRole

        super(SwitchingStep, self).__init__(*args, **kw_args)

    _attrs = ["statusKind", "text", "requiredControlAction", "desiredEndState"]
    _attr_types = {"statusKind": str, "text": str, "requiredControlAction": str, "desiredEndState": str}
    _defaults = {"statusKind": "instructed", "text": '', "requiredControlAction": '', "desiredEndState": ''}
    _enums = {"statusKind": "SwitchingStepStatusKind"}
    _refs = ["SafetyDocument", "requiredControlActionInterval", "SwitchingSchedule", "PowerSystemResources", "ErpPersonRole"]
    _many_refs = ["PowerSystemResources"]

    def getSafetyDocument(self):
        
        return self._SafetyDocument

    def setSafetyDocument(self, value):
        if self._SafetyDocument is not None:
            filtered = [x for x in self.SafetyDocument.ScheduleSteps if x != self]
            self._SafetyDocument._ScheduleSteps = filtered

        self._SafetyDocument = value
        if self._SafetyDocument is not None:
            if self not in self._SafetyDocument._ScheduleSteps:
                self._SafetyDocument._ScheduleSteps.append(self)

    SafetyDocument = property(getSafetyDocument, setSafetyDocument)

    # Interval between 'requiredControlAction' was issued and completed.
    requiredControlActionInterval = None

    def getSwitchingSchedule(self):
        
        return self._SwitchingSchedule

    def setSwitchingSchedule(self, value):
        if self._SwitchingSchedule is not None:
            filtered = [x for x in self.SwitchingSchedule.ScheduleSteps if x != self]
            self._SwitchingSchedule._ScheduleSteps = filtered

        self._SwitchingSchedule = value
        if self._SwitchingSchedule is not None:
            if self not in self._SwitchingSchedule._ScheduleSteps:
                self._SwitchingSchedule._ScheduleSteps.append(self)

    SwitchingSchedule = property(getSwitchingSchedule, setSwitchingSchedule)

    def getPowerSystemResources(self):
        
        return self._PowerSystemResources

    def setPowerSystemResources(self, value):
        for p in self._PowerSystemResources:
            filtered = [q for q in p.ScheduleSteps if q != self]
            self._PowerSystemResources._ScheduleSteps = filtered
        for r in value:
            if self not in r._ScheduleSteps:
                r._ScheduleSteps.append(self)
        self._PowerSystemResources = value

    PowerSystemResources = property(getPowerSystemResources, setPowerSystemResources)

    def addPowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self not in obj._ScheduleSteps:
                obj._ScheduleSteps.append(self)
            self._PowerSystemResources.append(obj)

    def removePowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self in obj._ScheduleSteps:
                obj._ScheduleSteps.remove(self)
            self._PowerSystemResources.remove(obj)

    def getErpPersonRole(self):
        
        return self._ErpPersonRole

    def setErpPersonRole(self, value):
        if self._ErpPersonRole is not None:
            self._ErpPersonRole._SwitchingStep = None

        self._ErpPersonRole = value
        if self._ErpPersonRole is not None:
            self._ErpPersonRole.SwitchingStep = None
            self._ErpPersonRole._SwitchingStep = self

    ErpPersonRole = property(getErpPersonRole, setErpPersonRole)

