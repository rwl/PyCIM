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

from CIM14.IEC61970.SCADA.RemotePoint import RemotePoint

class RemoteSource(RemotePoint):
    """Remote sources are state variables that are telemetered or calculated within the remote unit.
    """

    def __init__(self, scanInterval=0.0, sensorMaximum=0.0, deadband=0.0, sensorMinimum=0.0, MeasurementValue=None, *args, **kw_args):
        """Initialises a new 'RemoteSource' instance.

        @param scanInterval: The time interval between scans. 
        @param sensorMaximum: The maximum value the telemetry item can return. 
        @param deadband: The smallest change in value to be reported. 
        @param sensorMinimum: The minimum value the telemetry item can return. 
        @param MeasurementValue: Link to the physical telemetered point associated with this measurement.
        """
        #: The time interval between scans.
        self.scanInterval = scanInterval

        #: The maximum value the telemetry item can return.
        self.sensorMaximum = sensorMaximum

        #: The smallest change in value to be reported.
        self.deadband = deadband

        #: The minimum value the telemetry item can return.
        self.sensorMinimum = sensorMinimum

        self._MeasurementValue = None
        self.MeasurementValue = MeasurementValue

        super(RemoteSource, self).__init__(*args, **kw_args)

    _attrs = ["scanInterval", "sensorMaximum", "deadband", "sensorMinimum"]
    _attr_types = {"scanInterval": float, "sensorMaximum": float, "deadband": float, "sensorMinimum": float}
    _defaults = {"scanInterval": 0.0, "sensorMaximum": 0.0, "deadband": 0.0, "sensorMinimum": 0.0}
    _enums = {}
    _refs = ["MeasurementValue"]
    _many_refs = []

    def getMeasurementValue(self):
        """Link to the physical telemetered point associated with this measurement.
        """
        return self._MeasurementValue

    def setMeasurementValue(self, value):
        if self._MeasurementValue is not None:
            self._MeasurementValue._RemoteSource = None

        self._MeasurementValue = value
        if self._MeasurementValue is not None:
            self._MeasurementValue.RemoteSource = None
            self._MeasurementValue._RemoteSource = self

    MeasurementValue = property(getMeasurementValue, setMeasurementValue)

