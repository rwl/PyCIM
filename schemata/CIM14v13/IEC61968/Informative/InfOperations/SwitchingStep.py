# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class SwitchingStep(IdentifiedObject):
    """A single step within a SwitchingSchedule. Could be a switching operation (applying a network alteration), or issuing a safety document. Note: Inherited attribute IdentifiedObject.name is used to hold the sequence number.
    """

    def __init__(self, statusKind='confirmed', desiredEndState='', text='', requiredControlAction='', requiredControlActionInterval=None, SafetyDocument=None, SwitchingSchedule=None, ErpPersonRole=None, PowerSystemResources=None, *args, **kw_args):
        """Initializes a new 'SwitchingStep' instance.

        @param statusKind: Status of this SwitchingStep. Values are: "confirmed", "skipped", "aborted", "instructed", "proposed"
        @param desiredEndState: Desired end state for the associated PowerSystemResource as a result of this schedule step. 
        @param text: Information regarding this switching schedule step. 
        @param requiredControlAction: Control actions required to perform this step. 
        @param requiredControlActionInterval: Interval between 'requiredControlAction' was issued and completed.
        @param SafetyDocument:
        @param SwitchingSchedule:
        @param ErpPersonRole:
        @param PowerSystemResources:
        """
        #: Status of this SwitchingStep. Values are: "confirmed", "skipped", "aborted", "instructed", "proposed"
        self.statusKind = statusKind

        #: Desired end state for the associated PowerSystemResource as a result of this schedule step. 
        self.desiredEndState = desiredEndState

        #: Information regarding this switching schedule step. 
        self.text = text

        #: Control actions required to perform this step. 
        self.requiredControlAction = requiredControlAction

        self.requiredControlActionInterval = requiredControlActionInterval

        self._SafetyDocument = None
        self.SafetyDocument = SafetyDocument

        self._SwitchingSchedule = None
        self.SwitchingSchedule = SwitchingSchedule

        self._ErpPersonRole = None
        self.ErpPersonRole = ErpPersonRole

        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        super(SwitchingStep, self).__init__(*args, **kw_args)

    # Interval between 'requiredControlAction' was issued and completed.
    requiredControlActionInterval = None

    def getSafetyDocument(self):
        
        return self._SafetyDocument

    def setSafetyDocument(self, value):
        if self._SafetyDocument is not None:
            filtered = [x for x in self.SafetyDocument.ScheduleSteps if x != self]
            self._SafetyDocument._ScheduleSteps = filtered

        self._SafetyDocument = value
        if self._SafetyDocument is not None:
            self._SafetyDocument._ScheduleSteps.append(self)

    SafetyDocument = property(getSafetyDocument, setSafetyDocument)

    def getSwitchingSchedule(self):
        
        return self._SwitchingSchedule

    def setSwitchingSchedule(self, value):
        if self._SwitchingSchedule is not None:
            filtered = [x for x in self.SwitchingSchedule.ScheduleSteps if x != self]
            self._SwitchingSchedule._ScheduleSteps = filtered

        self._SwitchingSchedule = value
        if self._SwitchingSchedule is not None:
            self._SwitchingSchedule._ScheduleSteps.append(self)

    SwitchingSchedule = property(getSwitchingSchedule, setSwitchingSchedule)

    def getErpPersonRole(self):
        
        return self._ErpPersonRole

    def setErpPersonRole(self, value):
        if self._ErpPersonRole is not None:
            self._ErpPersonRole._SwitchingStep = None

        self._ErpPersonRole = value
        if self._ErpPersonRole is not None:
            self._ErpPersonRole._SwitchingStep = self

    ErpPersonRole = property(getErpPersonRole, setErpPersonRole)

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

