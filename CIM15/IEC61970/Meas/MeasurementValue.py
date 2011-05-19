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

class MeasurementValue(IdentifiedObject):
    """The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """

    def __init__(self, sensorAccuracy=0.0, timeStamp='', GmlValues=None, MeasurementValueQuality=None, ProcedureDataSets=None, MeasurementValueSource=None, ErpPerson=None, RemoteSource=None, *args, **kw_args):
        """Initialises a new 'MeasurementValue' instance.

        @param sensorAccuracy: The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions. 
        @param timeStamp: The time when the value was last updated 
        @param GmlValues:
        @param MeasurementValueQuality: A MeasurementValue has a MeasurementValueQuality associated with it.
        @param ProcedureDataSets:
        @param MeasurementValueSource: A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
        @param ErpPerson:
        @param RemoteSource: Link to the physical telemetered point associated with this measurement.
        """
        #: The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.
        self.sensorAccuracy = sensorAccuracy

        #: The time when the value was last updated
        self.timeStamp = timeStamp

        self._GmlValues = []
        self.GmlValues = [] if GmlValues is None else GmlValues

        self._MeasurementValueQuality = None
        self.MeasurementValueQuality = MeasurementValueQuality

        self._ProcedureDataSets = []
        self.ProcedureDataSets = [] if ProcedureDataSets is None else ProcedureDataSets

        self._MeasurementValueSource = None
        self.MeasurementValueSource = MeasurementValueSource

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        self._RemoteSource = None
        self.RemoteSource = RemoteSource

        super(MeasurementValue, self).__init__(*args, **kw_args)

    _attrs = ["sensorAccuracy", "timeStamp"]
    _attr_types = {"sensorAccuracy": float, "timeStamp": str}
    _defaults = {"sensorAccuracy": 0.0, "timeStamp": ''}
    _enums = {}
    _refs = ["GmlValues", "MeasurementValueQuality", "ProcedureDataSets", "MeasurementValueSource", "ErpPerson", "RemoteSource"]
    _many_refs = ["GmlValues", "ProcedureDataSets"]

    def getGmlValues(self):
        
        return self._GmlValues

    def setGmlValues(self, value):
        for x in self._GmlValues:
            x.MeasurementValue = None
        for y in value:
            y._MeasurementValue = self
        self._GmlValues = value

    GmlValues = property(getGmlValues, setGmlValues)

    def addGmlValues(self, *GmlValues):
        for obj in GmlValues:
            obj.MeasurementValue = self

    def removeGmlValues(self, *GmlValues):
        for obj in GmlValues:
            obj.MeasurementValue = None

    def getMeasurementValueQuality(self):
        """A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        return self._MeasurementValueQuality

    def setMeasurementValueQuality(self, value):
        if self._MeasurementValueQuality is not None:
            self._MeasurementValueQuality._MeasurementValue = None

        self._MeasurementValueQuality = value
        if self._MeasurementValueQuality is not None:
            self._MeasurementValueQuality.MeasurementValue = None
            self._MeasurementValueQuality._MeasurementValue = self

    MeasurementValueQuality = property(getMeasurementValueQuality, setMeasurementValueQuality)

    def getProcedureDataSets(self):
        
        return self._ProcedureDataSets

    def setProcedureDataSets(self, value):
        for p in self._ProcedureDataSets:
            filtered = [q for q in p.MeasurementValues if q != self]
            self._ProcedureDataSets._MeasurementValues = filtered
        for r in value:
            if self not in r._MeasurementValues:
                r._MeasurementValues.append(self)
        self._ProcedureDataSets = value

    ProcedureDataSets = property(getProcedureDataSets, setProcedureDataSets)

    def addProcedureDataSets(self, *ProcedureDataSets):
        for obj in ProcedureDataSets:
            if self not in obj._MeasurementValues:
                obj._MeasurementValues.append(self)
            self._ProcedureDataSets.append(obj)

    def removeProcedureDataSets(self, *ProcedureDataSets):
        for obj in ProcedureDataSets:
            if self in obj._MeasurementValues:
                obj._MeasurementValues.remove(self)
            self._ProcedureDataSets.remove(obj)

    def getMeasurementValueSource(self):
        """A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
        """
        return self._MeasurementValueSource

    def setMeasurementValueSource(self, value):
        if self._MeasurementValueSource is not None:
            filtered = [x for x in self.MeasurementValueSource.MeasurementValues if x != self]
            self._MeasurementValueSource._MeasurementValues = filtered

        self._MeasurementValueSource = value
        if self._MeasurementValueSource is not None:
            if self not in self._MeasurementValueSource._MeasurementValues:
                self._MeasurementValueSource._MeasurementValues.append(self)

    MeasurementValueSource = property(getMeasurementValueSource, setMeasurementValueSource)

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.MeasurementValues if x != self]
            self._ErpPerson._MeasurementValues = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            if self not in self._ErpPerson._MeasurementValues:
                self._ErpPerson._MeasurementValues.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

    def getRemoteSource(self):
        """Link to the physical telemetered point associated with this measurement.
        """
        return self._RemoteSource

    def setRemoteSource(self, value):
        if self._RemoteSource is not None:
            self._RemoteSource._MeasurementValue = None

        self._RemoteSource = value
        if self._RemoteSource is not None:
            self._RemoteSource.MeasurementValue = None
            self._RemoteSource._MeasurementValue = self

    RemoteSource = property(getRemoteSource, setRemoteSource)

