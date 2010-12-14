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

