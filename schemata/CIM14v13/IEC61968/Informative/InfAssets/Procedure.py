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

class Procedure(Document):
    """A documented procedure for various types of Work or Work Tasks. One or more procedures guide a compatible unit, a standard way of performing a unit of work. The type of procedure is defined in Procedure.type. For example, when type=Inspection, this procedure coupled with Schedule and other information provides the key items of an inspection plan. Another type of Procedure is a Diagnosis. Note that each specific values and settings to be used in a procedure is intended to be described in an instance of ProcedureValue. A maintenance ticket, a type of Work, is generated whenever maintenance is determined to be needed as a result of an inspection or diagnosis.
    """

    def __init__(self, kind='test', instruction='', sequenceNumber='', corporateCode='', CompatibleUnits=None, ProcedureDataSets=None, ProcedureValues=None, Limits=None, **kw_args):
        """Initializes a new 'Procedure' instance.

        @param kind: Kind of this procedure. Values are: "test", "diagnosis", "inspection", "other", "maintenance"
        @param instruction: The textual description of the procedure, which references instances of ProcedureValue as appropriate. 
        @param sequenceNumber: Sequence number in a sequence of procedures being performed. 
        @param corporateCode: Code for this kind of procedure. 
        @param CompatibleUnits:
        @param ProcedureDataSets:
        @param ProcedureValues: UserAttributes used to specify procedure values. An example is to have an instance for each of the following settings when conducting a test: voltage, current, frequency, temperature specified in 'name' attribute, and the corresponding value and units in 'value' attribute.
        @param Limits:
        """
        #: Kind of this procedure.Values are: "test", "diagnosis", "inspection", "other", "maintenance"
        self.kind = kind

        #: The textual description of the procedure, which references instances of ProcedureValue as appropriate.
        self.instruction = instruction

        #: Sequence number in a sequence of procedures being performed.
        self.sequenceNumber = sequenceNumber

        #: Code for this kind of procedure.
        self.corporateCode = corporateCode

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self._ProcedureDataSets = []
        self.ProcedureDataSets = [] if ProcedureDataSets is None else ProcedureDataSets

        self._ProcedureValues = []
        self.ProcedureValues = [] if ProcedureValues is None else ProcedureValues

        self._Limits = []
        self.Limits = [] if Limits is None else Limits

        super(Procedure, self).__init__(**kw_args)

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

    def getProcedureDataSets(self):
        
        return self._ProcedureDataSets

    def setProcedureDataSets(self, value):
        for x in self._ProcedureDataSets:
            x._Procedure = None
        for y in value:
            y._Procedure = self
        self._ProcedureDataSets = value

    ProcedureDataSets = property(getProcedureDataSets, setProcedureDataSets)

    def addProcedureDataSets(self, *ProcedureDataSets):
        for obj in ProcedureDataSets:
            obj._Procedure = self
            self._ProcedureDataSets.append(obj)

    def removeProcedureDataSets(self, *ProcedureDataSets):
        for obj in ProcedureDataSets:
            obj._Procedure = None
            self._ProcedureDataSets.remove(obj)

    def getProcedureValues(self):
        """UserAttributes used to specify procedure values. An example is to have an instance for each of the following settings when conducting a test: voltage, current, frequency, temperature specified in 'name' attribute, and the corresponding value and units in 'value' attribute.
        """
        return self._ProcedureValues

    def setProcedureValues(self, value):
        for x in self._ProcedureValues:
            x._Procedure = None
        for y in value:
            y._Procedure = self
        self._ProcedureValues = value

    ProcedureValues = property(getProcedureValues, setProcedureValues)

    def addProcedureValues(self, *ProcedureValues):
        for obj in ProcedureValues:
            obj._Procedure = self
            self._ProcedureValues.append(obj)

    def removeProcedureValues(self, *ProcedureValues):
        for obj in ProcedureValues:
            obj._Procedure = None
            self._ProcedureValues.remove(obj)

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

