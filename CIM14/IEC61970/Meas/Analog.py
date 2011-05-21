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

from CIM14.IEC61970.Meas.Measurement import Measurement

class Analog(Measurement):
    """Analog represents an analog Measurement.
    """

    def __init__(self, positiveFlowIn=False, minValue=0.0, maxValue=0.0, normalValue=0.0, LimitSets=None, SetPoint=None, AnalogValues=None, *args, **kw_args):
        """Initialises a new 'Analog' instance.

        @param positiveFlowIn: If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. 
        @param minValue: Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values 
        @param maxValue: Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        @param normalValue: Normal measurement value, e.g., used for percentage calculations. 
        @param LimitSets: A measurement may have zero or more limit ranges defined for it.
        @param SetPoint: The Control variable associated with the Measurement
        @param AnalogValues: The values connected to this measurement.
        """
        #: If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
        self.positiveFlowIn = positiveFlowIn

        #: Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
        self.minValue = minValue

        #: Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
        self.maxValue = maxValue

        #: Normal measurement value, e.g., used for percentage calculations.
        self.normalValue = normalValue

        self._LimitSets = []
        self.LimitSets = [] if LimitSets is None else LimitSets

        self._SetPoint = None
        self.SetPoint = SetPoint

        self._AnalogValues = []
        self.AnalogValues = [] if AnalogValues is None else AnalogValues

        super(Analog, self).__init__(*args, **kw_args)

    _attrs = ["positiveFlowIn", "minValue", "maxValue", "normalValue"]
    _attr_types = {"positiveFlowIn": bool, "minValue": float, "maxValue": float, "normalValue": float}
    _defaults = {"positiveFlowIn": False, "minValue": 0.0, "maxValue": 0.0, "normalValue": 0.0}
    _enums = {}
    _refs = ["LimitSets", "SetPoint", "AnalogValues"]
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

