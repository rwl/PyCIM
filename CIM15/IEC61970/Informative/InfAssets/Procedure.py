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

class Procedure(Document):
    """A documented procedure for various types of Work or Work Tasks. One or more procedures guide a compatible unit, a standard way of performing a unit of work. The type of procedure is defined in Procedure.type. For example, when type=Inspection, this procedure coupled with Schedule and other information provides the key items of an inspection plan. Another type of Procedure is a Diagnosis. Note that each specific values and settings to be used in a procedure is intended to be described in an instance of ProcedureValue. A maintenance ticket, a type of Work, is generated whenever maintenance is determined to be needed as a result of an inspection or diagnosis.A documented procedure for various types of Work or Work Tasks. One or more procedures guide a compatible unit, a standard way of performing a unit of work. The type of procedure is defined in Procedure.type. For example, when type=Inspection, this procedure coupled with Schedule and other information provides the key items of an inspection plan. Another type of Procedure is a Diagnosis. Note that each specific values and settings to be used in a procedure is intended to be described in an instance of ProcedureValue. A maintenance ticket, a type of Work, is generated whenever maintenance is determined to be needed as a result of an inspection or diagnosis.
    """

    def __init__(self, corporateCode='', sequenceNumber='', kind="test", instruction='', ProcedureValues=None, ProcedureDataSets=None, CompatibleUnits=None, Limits=None, *args, **kw_args):
        """Initialises a new 'Procedure' instance.

        @param corporateCode: Code for this kind of procedure. 
        @param sequenceNumber: Sequence number in a sequence of procedures being performed. 
        @param kind: Kind of this procedure. Values are: "test", "maintenance", "other", "inspection", "diagnosis"
        @param instruction: The textual description of the procedure, which references instances of ProcedureValue as appropriate. 
        @param ProcedureValues: UserAttributes used to specify procedure values. An example is to have an instance for each of the following settings when conducting a test: voltage, current, frequency, temperature specified in 'name' attribute, and the corresponding value and units in 'value' attribute.
        @param ProcedureDataSets:
        @param CompatibleUnits:
        @param Limits:
        """
        #: Code for this kind of procedure.
        self.corporateCode = corporateCode

        #: Sequence number in a sequence of procedures being performed.
        self.sequenceNumber = sequenceNumber

        #: Kind of this procedure. Values are: "test", "maintenance", "other", "inspection", "diagnosis"
        self.kind = kind

        #: The textual description of the procedure, which references instances of ProcedureValue as appropriate.
        self.instruction = instruction

        self._ProcedureValues = []
        self.ProcedureValues = [] if ProcedureValues is None else ProcedureValues

        self._ProcedureDataSets = []
        self.ProcedureDataSets = [] if ProcedureDataSets is None else ProcedureDataSets

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self._Limits = []
        self.Limits = [] if Limits is None else Limits

        super(Procedure, self).__init__(*args, **kw_args)

    _attrs = ["corporateCode", "sequenceNumber", "kind", "instruction"]
    _attr_types = {"corporateCode": str, "sequenceNumber": str, "kind": str, "instruction": str}
    _defaults = {"corporateCode": '', "sequenceNumber": '', "kind": "test", "instruction": ''}
    _enums = {"kind": "ProcedureKind"}
    _refs = ["ProcedureValues", "ProcedureDataSets", "CompatibleUnits", "Limits"]
    _many_refs = ["ProcedureValues", "ProcedureDataSets", "CompatibleUnits", "Limits"]

    def getProcedureValues(self):
        """UserAttributes used to specify procedure values. An example is to have an instance for each of the following settings when conducting a test: voltage, current, frequency, temperature specified in 'name' attribute, and the corresponding value and units in 'value' attribute.
        """
        return self._ProcedureValues

    def setProcedureValues(self, value):
        for x in self._ProcedureValues:
            x.Procedure = None
        for y in value:
            y._Procedure = self
        self._ProcedureValues = value

    ProcedureValues = property(getProcedureValues, setProcedureValues)

    def addProcedureValues(self, *ProcedureValues):
        for obj in ProcedureValues:
            obj.Procedure = self

    def removeProcedureValues(self, *ProcedureValues):
        for obj in ProcedureValues:
            obj.Procedure = None

    def getProcedureDataSets(self):
        
        return self._ProcedureDataSets

    def setProcedureDataSets(self, value):
        for x in self._ProcedureDataSets:
            x.Procedure = None
        for y in value:
            y._Procedure = self
        self._ProcedureDataSets = value

    ProcedureDataSets = property(getProcedureDataSets, setProcedureDataSets)

    def addProcedureDataSets(self, *ProcedureDataSets):
        for obj in ProcedureDataSets:
            obj.Procedure = self

    def removeProcedureDataSets(self, *ProcedureDataSets):
        for obj in ProcedureDataSets:
            obj.Procedure = None

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for p in self._CompatibleUnits:
            filtered = [q for q in p.Procedures if q != self]
            self._CompatibleUnits._Procedures = filtered
        for r in value:
            if self not in r._Procedures:
                r._Procedures.append(self)
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self not in obj._Procedures:
                obj._Procedures.append(self)
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self in obj._Procedures:
                obj._Procedures.remove(self)
            self._CompatibleUnits.remove(obj)

    def getLimits(self):
        
        return self._Limits

    def setLimits(self, value):
        for p in self._Limits:
            filtered = [q for q in p.Procedures if q != self]
            self._Limits._Procedures = filtered
        for r in value:
            if self not in r._Procedures:
                r._Procedures.append(self)
        self._Limits = value

    Limits = property(getLimits, setLimits)

    def addLimits(self, *Limits):
        for obj in Limits:
            if self not in obj._Procedures:
                obj._Procedures.append(self)
            self._Limits.append(obj)

    def removeLimits(self, *Limits):
        for obj in Limits:
            if self in obj._Procedures:
                obj._Procedures.remove(self)
            self._Limits.remove(obj)

