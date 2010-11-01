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

class ProcedureDataSet(Document):
    """A data set recorded each time a procedure is executed. Observed results are captured in associated measurement values and/or values for properties relevant to the type of procedure performed.
    """

    def __init__(self, completedDateTime='', Procedure=None, Properties=None, MeasurementValues=None, TransformerObservations=None, *args, **kw_args):
        """Initializes a new 'ProcedureDataSet' instance.

        @param completedDateTime: Date and time procedure was completed. 
        @param Procedure:
        @param Properties: UserAttributes used to specify further properties of this procedure data set. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        @param MeasurementValues:
        @param TransformerObservations:
        """
        #: Date and time procedure was completed. 
        self.completedDateTime = completedDateTime

        self._Procedure = None
        self.Procedure = Procedure

        self._Properties = []
        self.Properties = [] if Properties is None else Properties

        self._MeasurementValues = []
        self.MeasurementValues = [] if MeasurementValues is None else MeasurementValues

        self._TransformerObservations = []
        self.TransformerObservations = [] if TransformerObservations is None else TransformerObservations

        super(ProcedureDataSet, self).__init__(*args, **kw_args)

    def getProcedure(self):
        
        return self._Procedure

    def setProcedure(self, value):
        if self._Procedure is not None:
            filtered = [x for x in self.Procedure.ProcedureDataSets if x != self]
            self._Procedure._ProcedureDataSets = filtered

        self._Procedure = value
        if self._Procedure is not None:
            self._Procedure._ProcedureDataSets.append(self)

    Procedure = property(getProcedure, setProcedure)

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

