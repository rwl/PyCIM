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

from CIM14.IEC61970.Meas.Measurement import Measurement

class Discrete(Measurement):
    """Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.
    """

    def __init__(self, normalValue=0, minValue=0, maxValue=0, Command=None, DiscreteValues=None, ValueAliasSet=None, **kw_args):
        """Initializes a new 'Discrete' instance.

        @param normalValue: Normal measurement value, e.g., used for percentage calculations. 
        @param minValue: Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values 
        @param maxValue: Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values. 
        @param Command: The Control variable associated with the Measurement.
        @param DiscreteValues: The values connected to this measurement.
        @param ValueAliasSet: The ValueAliasSet used for translation of a MeasurementValue.value to a name
        """
        #: Normal measurement value, e.g., used for percentage calculations.
        self.normalValue = normalValue

        #: Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
        self.minValue = minValue

        #: Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
        self.maxValue = maxValue

        self._Command = None
        self.Command = Command

        self._DiscreteValues = []
        self.DiscreteValues = [] if DiscreteValues is None else DiscreteValues

        self._ValueAliasSet = None
        self.ValueAliasSet = ValueAliasSet

        super(Discrete, self).__init__(**kw_args)

    def getCommand(self):
        """The Control variable associated with the Measurement.
        """
        return self._Command

    def setCommand(self, value):
        if self._Command is not None:
            self._Command._Discrete = None

        self._Command = value
        if self._Command is not None:
            self._Command._Discrete = self

    Command = property(getCommand, setCommand)

    def getDiscreteValues(self):
        """The values connected to this measurement.
        """
        return self._DiscreteValues

    def setDiscreteValues(self, value):
        for x in self._DiscreteValues:
            x._Discrete = None
        for y in value:
            y._Discrete = self
        self._DiscreteValues = value

    DiscreteValues = property(getDiscreteValues, setDiscreteValues)

    def addDiscreteValues(self, *DiscreteValues):
        for obj in DiscreteValues:
            obj._Discrete = self
            self._DiscreteValues.append(obj)

    def removeDiscreteValues(self, *DiscreteValues):
        for obj in DiscreteValues:
            obj._Discrete = None
            self._DiscreteValues.remove(obj)

    def getValueAliasSet(self):
        """The ValueAliasSet used for translation of a MeasurementValue.value to a name
        """
        return self._ValueAliasSet

    def setValueAliasSet(self, value):
        if self._ValueAliasSet is not None:
            filtered = [x for x in self.ValueAliasSet.Discretes if x != self]
            self._ValueAliasSet._Discretes = filtered

        self._ValueAliasSet = value
        if self._ValueAliasSet is not None:
            self._ValueAliasSet._Discretes.append(self)

    ValueAliasSet = property(getValueAliasSet, setValueAliasSet)

