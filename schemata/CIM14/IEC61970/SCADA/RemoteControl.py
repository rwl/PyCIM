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

class RemoteControl(RemotePoint):
    """Remote controls are ouputs that are sent by the remote unit to actuators in the process.
    """

    def __init__(self, actuatorMinimum=0.0, remoteControlled=False, actuatorMaximum=0.0, Control=None, **kw_args):
        """Initializes a new 'RemoteControl' instance.

        @param actuatorMinimum: The minimum set point value accepted by the remote control point. 
        @param remoteControlled: Set to true if the actuator is remotely controlled. 
        @param actuatorMaximum: The maximum set point value accepted by the remote control point. 
        @param Control: The Control for the RemoteControl point.
        """
        #: The minimum set point value accepted by the remote control point.
        self.actuatorMinimum = actuatorMinimum

        #: Set to true if the actuator is remotely controlled.
        self.remoteControlled = remoteControlled

        #: The maximum set point value accepted by the remote control point.
        self.actuatorMaximum = actuatorMaximum

        self._Control = None
        self.Control = Control

        super(RemoteControl, self).__init__(**kw_args)

    def getControl(self):
        """The Control for the RemoteControl point.
        """
        return self._Control

    def setControl(self, value):
        if self._Control is not None:
            self._Control._RemoteControl = None

        self._Control = value
        if self._Control is not None:
            self._Control._RemoteControl = self

    Control = property(getControl, setControl)

