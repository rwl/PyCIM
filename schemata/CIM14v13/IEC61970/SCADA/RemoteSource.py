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

from CIM14v13.IEC61970.SCADA.RemotePoint import RemotePoint

class RemoteSource(RemotePoint):
    """Remote sources are state variables that are telemetered or calculated within the remote unit.
    """

    def __init__(self, sensorMinimum=0.0, deadband=0.0, sensorMaximum=0.0, scanInterval=0.0, MeasurementValue=None, **kw_args):
        """Initializes a new 'RemoteSource' instance.

        @param sensorMinimum: The minimum value the telemetry item can return. 
        @param deadband: The smallest change in value to be reported. 
        @param sensorMaximum: The maximum value the telemetry item can return. 
        @param scanInterval: The time interval between scans. 
        @param MeasurementValue: Link to the physical telemetered point associated with this measurement.
        """
        #: The minimum value the telemetry item can return.
        self.sensorMinimum = sensorMinimum

        #: The smallest change in value to be reported.
        self.deadband = deadband

        #: The maximum value the telemetry item can return.
        self.sensorMaximum = sensorMaximum

        #: The time interval between scans.
        self.scanInterval = scanInterval

        self._MeasurementValue = None
        self.MeasurementValue = MeasurementValue

        super(RemoteSource, self).__init__(**kw_args)

    def getMeasurementValue(self):
        """Link to the physical telemetered point associated with this measurement.
        """
        return self._MeasurementValue

    def setMeasurementValue(self, value):
        if self._MeasurementValue is not None:
            self._MeasurementValue._RemoteSource = None

        self._MeasurementValue = value
        if self._MeasurementValue is not None:
            self._MeasurementValue._RemoteSource = self

    MeasurementValue = property(getMeasurementValue, setMeasurementValue)

