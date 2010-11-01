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

from CIM14v13.IEC61968.Common.Document import Document

class SafetyDocument(Document):
    """A document restricting or authorising works on electrical equipment (for example a permit to work, sanction for test, limitation of access, or certificate of isolation), defined based upon organisational practices. Note: SafetyDocument may refer to ClearanceTag-s associated with ConductingEquipment for which the SafetyDocument is issued.
    """

    def __init__(self, PowerSystemResource=None, ScheduleSteps=None, ClearanceTags=None, *args, **kw_args):
        """Initializes a new 'SafetyDocument' instance.

        @param PowerSystemResource:
        @param ScheduleSteps:
        @param ClearanceTags:
        """
        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._ScheduleSteps = []
        self.ScheduleSteps = [] if ScheduleSteps is None else ScheduleSteps

        self._ClearanceTags = []
        self.ClearanceTags = [] if ClearanceTags is None else ClearanceTags

        super(SafetyDocument, self).__init__(*args, **kw_args)

    def getPowerSystemResource(self):
        
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.SafetyDocuments if x != self]
            self._PowerSystemResource._SafetyDocuments = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._SafetyDocuments.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getScheduleSteps(self):
        
        return self._ScheduleSteps

    def setScheduleSteps(self, value):
        for x in self._ScheduleSteps:
            x._SafetyDocument = None
        for y in value:
            y._SafetyDocument = self
        self._ScheduleSteps = value

    ScheduleSteps = property(getScheduleSteps, setScheduleSteps)

    def addScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            obj._SafetyDocument = self
            self._ScheduleSteps.append(obj)

    def removeScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            obj._SafetyDocument = None
            self._ScheduleSteps.remove(obj)

    def getClearanceTags(self):
        
        return self._ClearanceTags

    def setClearanceTags(self, value):
        for x in self._ClearanceTags:
            x._SafetyDocument = None
        for y in value:
            y._SafetyDocument = self
        self._ClearanceTags = value

    ClearanceTags = property(getClearanceTags, setClearanceTags)

    def addClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj._SafetyDocument = self
            self._ClearanceTags.append(obj)

    def removeClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj._SafetyDocument = None
            self._ClearanceTags.remove(obj)

