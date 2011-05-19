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

from CIM15.IEC61970.Meas.Measurement import Measurement

class Analog(Measurement):
    """Analog represents an analog Measurement.Analog represents an analog Measurement.
    """

    def __init__(self, maxValue=0.0, normalValue=0.0, positiveFlowIn=False, minValue=0.0, LimitSets=None, AnalogValues=None, SetPoint=None, *args, **kw_args):
        """Initialises a new 'Analog' instance.

        @param maxValue: Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        @param normalValue: Normal measurement value, e.g., used for percentage calculations. 
        @param positiveFlowIn: If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. 
        @param minValue: Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values 
        @param LimitSets: A measurement may have zero or more limit ranges defined for it.
        @param AnalogValues: The values connected to this measurement.
        @param SetPoint: The Control variable associated with the Measurement
        """
        #: Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
        self.maxValue = maxValue

        #: Normal measurement value, e.g., used for percentage calculations.
        self.normalValue = normalValue

        #: If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
        self.positiveFlowIn = positiveFlowIn

        #: Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
        self.minValue = minValue

        self._LimitSets = []
        self.LimitSets = [] if LimitSets is None else LimitSets

        self._AnalogValues = []
        self.AnalogValues = [] if AnalogValues is None else AnalogValues

        self._SetPoint = None
        self.SetPoint = SetPoint

        super(Analog, self).__init__(*args, **kw_args)

    _attrs = ["maxValue", "normalValue", "positiveFlowIn", "minValue"]
    _attr_types = {"maxValue": float, "normalValue": float, "positiveFlowIn": bool, "minValue": float}
    _defaults = {"maxValue": 0.0, "normalValue": 0.0, "positiveFlowIn": False, "minValue": 0.0}
    _enums = {}
    _refs = ["LimitSets", "AnalogValues", "SetPoint"]
    _many_refs = ["LimitSets", "AnalogValues"]

    def getLimitSets(self):
        """A measurement may have zero or more limit ranges defined for it.
        """
        return self._LimitSets

    def setLimitSets(self, value):
        for p in self._LimitSets:
            filtered = [q for q in p.Measurements if q != self]
            self._LimitSets._Measurements = filtered
        for r in value:
            if self not in r._Measurements:
                r._Measurements.append(self)
        self._LimitSets = value

    LimitSets = property(getLimitSets, setLimitSets)

    def addLimitSets(self, *LimitSets):
        for obj in LimitSets:
            if self not in obj._Measurements:
                obj._Measurements.append(self)
            self._LimitSets.append(obj)

    def removeLimitSets(self, *LimitSets):
        for obj in LimitSets:
            if self in obj._Measurements:
                obj._Measurements.remove(self)
            self._LimitSets.remove(obj)

    def getAnalogValues(self):
        """The values connected to this measurement.
        """
        return self._AnalogValues

    def setAnalogValues(self, value):
        for x in self._AnalogValues:
            x.Analog = None
        for y in value:
            y._Analog = self
        self._AnalogValues = value

    AnalogValues = property(getAnalogValues, setAnalogValues)

    def addAnalogValues(self, *AnalogValues):
        for obj in AnalogValues:
            obj.Analog = self

    def removeAnalogValues(self, *AnalogValues):
        for obj in AnalogValues:
            obj.Analog = None

    def getSetPoint(self):
        """The Control variable associated with the Measurement
        """
        return self._SetPoint

    def setSetPoint(self, value):
        if self._SetPoint is not None:
            self._SetPoint._Analog = None

        self._SetPoint = value
        if self._SetPoint is not None:
            self._SetPoint.Analog = None
            self._SetPoint._Analog = self

    SetPoint = property(getSetPoint, setSetPoint)

