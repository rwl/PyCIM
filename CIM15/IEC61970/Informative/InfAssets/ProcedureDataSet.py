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

class ProcedureDataSet(Document):
    """A data set recorded each time a procedure is executed. Observed results are captured in associated measurement values and/or values for properties relevant to the type of procedure performed.A data set recorded each time a procedure is executed. Observed results are captured in associated measurement values and/or values for properties relevant to the type of procedure performed.
    """

    def __init__(self, completedDateTime='', Properties=None, TransformerObservations=None, Procedure=None, MeasurementValues=None, *args, **kw_args):
        """Initialises a new 'ProcedureDataSet' instance.

        @param completedDateTime: Date and time procedure was completed. 
        @param Properties: UserAttributes used to specify further properties of this procedure data set. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        @param TransformerObservations:
        @param Procedure:
        @param MeasurementValues:
        """
        #: Date and time procedure was completed.
        self.completedDateTime = completedDateTime

        self._Properties = []
        self.Properties = [] if Properties is None else Properties

        self._TransformerObservations = []
        self.TransformerObservations = [] if TransformerObservations is None else TransformerObservations

        self._Procedure = None
        self.Procedure = Procedure

        self._MeasurementValues = []
        self.MeasurementValues = [] if MeasurementValues is None else MeasurementValues

        super(ProcedureDataSet, self).__init__(*args, **kw_args)

    _attrs = ["completedDateTime"]
    _attr_types = {"completedDateTime": str}
    _defaults = {"completedDateTime": ''}
    _enums = {}
    _refs = ["Properties", "TransformerObservations", "Procedure", "MeasurementValues"]
    _many_refs = ["Properties", "TransformerObservations", "MeasurementValues"]

    def getProperties(self):
        """UserAttributes used to specify further properties of this procedure data set. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        """
        return self._Properties

    def setProperties(self, value):
        for p in self._Properties:
            filtered = [q for q in p.ProcedureDataSets if q != self]
            self._Properties._ProcedureDataSets = filtered
        for r in value:
            if self not in r._ProcedureDataSets:
                r._ProcedureDataSets.append(self)
        self._Properties = value

    Properties = property(getProperties, setProperties)

    def addProperties(self, *Properties):
        for obj in Properties:
            if self not in obj._ProcedureDataSets:
                obj._ProcedureDataSets.append(self)
            self._Properties.append(obj)

    def removeProperties(self, *Properties):
        for obj in Properties:
            if self in obj._ProcedureDataSets:
                obj._ProcedureDataSets.remove(self)
            self._Properties.remove(obj)

    def getTransformerObservations(self):
        
        return self._TransformerObservations

    def setTransformerObservations(self, value):
        for p in self._TransformerObservations:
            filtered = [q for q in p.ProcedureDataSets if q != self]
            self._TransformerObservations._ProcedureDataSets = filtered
        for r in value:
            if self not in r._ProcedureDataSets:
                r._ProcedureDataSets.append(self)
        self._TransformerObservations = value

    TransformerObservations = property(getTransformerObservations, setTransformerObservations)

    def addTransformerObservations(self, *TransformerObservations):
        for obj in TransformerObservations:
            if self not in obj._ProcedureDataSets:
                obj._ProcedureDataSets.append(self)
            self._TransformerObservations.append(obj)

    def removeTransformerObservations(self, *TransformerObservations):
        for obj in TransformerObservations:
            if self in obj._ProcedureDataSets:
                obj._ProcedureDataSets.remove(self)
            self._TransformerObservations.remove(obj)

    def getProcedure(self):
        
        return self._Procedure

    def setProcedure(self, value):
        if self._Procedure is not None:
            filtered = [x for x in self.Procedure.ProcedureDataSets if x != self]
            self._Procedure._ProcedureDataSets = filtered

        self._Procedure = value
        if self._Procedure is not None:
            if self not in self._Procedure._ProcedureDataSets:
                self._Procedure._ProcedureDataSets.append(self)

    Procedure = property(getProcedure, setProcedure)

    def getMeasurementValues(self):
        
        return self._MeasurementValues

    def setMeasurementValues(self, value):
        for p in self._MeasurementValues:
            filtered = [q for q in p.ProcedureDataSets if q != self]
            self._MeasurementValues._ProcedureDataSets = filtered
        for r in value:
            if self not in r._ProcedureDataSets:
                r._ProcedureDataSets.append(self)
        self._MeasurementValues = value

    MeasurementValues = property(getMeasurementValues, setMeasurementValues)

    def addMeasurementValues(self, *MeasurementValues):
        for obj in MeasurementValues:
            if self not in obj._ProcedureDataSets:
                obj._ProcedureDataSets.append(self)
            self._MeasurementValues.append(obj)

    def removeMeasurementValues(self, *MeasurementValues):
        for obj in MeasurementValues:
            if self in obj._ProcedureDataSets:
                obj._ProcedureDataSets.remove(self)
            self._MeasurementValues.remove(obj)

