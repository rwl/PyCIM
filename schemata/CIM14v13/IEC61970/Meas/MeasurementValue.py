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

class MeasurementValue(IdentifiedObject):
    """The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """

    def __init__(self, sensorAccuracy=0.0, timeStamp='', GmlValues=None, MeasurementValueSource=None, ErpPerson=None, ProcedureDataSets=None, RemoteSource=None, MeasurementValueQuality=None, *args, **kw_args):
        """Initializes a new 'MeasurementValue' instance.

        @param sensorAccuracy: The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions. 
        @param timeStamp: The time when the value was last updated 
        @param GmlValues:
        @param MeasurementValueSource: A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
        @param ErpPerson:
        @param ProcedureDataSets:
        @param RemoteSource: Link to the physical telemetered point associated with this measurement.
        @param MeasurementValueQuality: A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        #: The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.
        self.sensorAccuracy = sensorAccuracy

        #: The time when the value was last updated
        self.timeStamp = timeStamp

        self._GmlValues = []
        self.GmlValues = [] if GmlValues is None else GmlValues

        self._MeasurementValueSource = None
        self.MeasurementValueSource = MeasurementValueSource

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        self._ProcedureDataSets = []
        self.ProcedureDataSets = [] if ProcedureDataSets is None else ProcedureDataSets

        self._RemoteSource = None
        self.RemoteSource = RemoteSource

        self._MeasurementValueQuality = None
        self.MeasurementValueQuality = MeasurementValueQuality

        super(MeasurementValue, self).__init__(*args, **kw_args)

    def getGmlValues(self):
        
        return self._GmlValues

    def setGmlValues(self, value):
        for x in self._GmlValues:
            x._MeasurementValue = None
        for y in value:
            y._MeasurementValue = self
        self._GmlValues = value

    GmlValues = property(getGmlValues, setGmlValues)

    def addGmlValues(self, *GmlValues):
        for obj in GmlValues:
            obj._MeasurementValue = self
            self._GmlValues.append(obj)

    def removeGmlValues(self, *GmlValues):
        for obj in GmlValues:
            obj._MeasurementValue = None
            self._GmlValues.remove(obj)

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
            self._ErpPerson._MeasurementValues.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

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

    def getRemoteSource(self):
        """Link to the physical telemetered point associated with this measurement.
        """
        return self._RemoteSource

    def setRemoteSource(self, value):
        if self._RemoteSource is not None:
            self._RemoteSource._MeasurementValue = None

        self._RemoteSource = value
        if self._RemoteSource is not None:
            self._RemoteSource._MeasurementValue = self

    RemoteSource = property(getRemoteSource, setRemoteSource)

    def getMeasurementValueQuality(self):
        """A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        return self._MeasurementValueQuality

    def setMeasurementValueQuality(self, value):
        if self._MeasurementValueQuality is not None:
            self._MeasurementValueQuality._MeasurementValue = None

        self._MeasurementValueQuality = value
        if self._MeasurementValueQuality is not None:
            self._MeasurementValueQuality._MeasurementValue = self

    MeasurementValueQuality = property(getMeasurementValueQuality, setMeasurementValueQuality)

