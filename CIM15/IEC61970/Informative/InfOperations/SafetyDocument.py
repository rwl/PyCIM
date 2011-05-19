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

from CIM15.IEC61968.Common.Document import Document

class SafetyDocument(Document):
    """A document restricting or authorising works on electrical equipment (for example a permit to work, sanction for test, limitation of access, or certificate of isolation), defined based upon organisational practices. Note: SafetyDocument may refer to ClearanceTag-s associated with ConductingEquipment for which the SafetyDocument is issued.A document restricting or authorising works on electrical equipment (for example a permit to work, sanction for test, limitation of access, or certificate of isolation), defined based upon organisational practices. Note: SafetyDocument may refer to ClearanceTag-s associated with ConductingEquipment for which the SafetyDocument is issued.
    """

    def __init__(self, ClearanceTags=None, ScheduleSteps=None, PowerSystemResource=None, *args, **kw_args):
        """Initialises a new 'SafetyDocument' instance.

        @param ClearanceTags:
        @param ScheduleSteps:
        @param PowerSystemResource:
        """
        self._ClearanceTags = []
        self.ClearanceTags = [] if ClearanceTags is None else ClearanceTags

        self._ScheduleSteps = []
        self.ScheduleSteps = [] if ScheduleSteps is None else ScheduleSteps

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        super(SafetyDocument, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ClearanceTags", "ScheduleSteps", "PowerSystemResource"]
    _many_refs = ["ClearanceTags", "ScheduleSteps"]

    def getClearanceTags(self):
        
        return self._ClearanceTags

    def setClearanceTags(self, value):
        for x in self._ClearanceTags:
            x.SafetyDocument = None
        for y in value:
            y._SafetyDocument = self
        self._ClearanceTags = value

    ClearanceTags = property(getClearanceTags, setClearanceTags)

    def addClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj.SafetyDocument = self

    def removeClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj.SafetyDocument = None

    def getScheduleSteps(self):
        
        return self._ScheduleSteps

    def setScheduleSteps(self, value):
        for x in self._ScheduleSteps:
            x.SafetyDocument = None
        for y in value:
            y._SafetyDocument = self
        self._ScheduleSteps = value

    ScheduleSteps = property(getScheduleSteps, setScheduleSteps)

    def addScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            obj.SafetyDocument = self

    def removeScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            obj.SafetyDocument = None

    def getPowerSystemResource(self):
        
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.SafetyDocuments if x != self]
            self._PowerSystemResource._SafetyDocuments = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            if self not in self._PowerSystemResource._SafetyDocuments:
                self._PowerSystemResource._SafetyDocuments.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

