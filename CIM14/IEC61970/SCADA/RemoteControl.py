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

class RemoteControl(RemotePoint):
    """Remote controls are ouputs that are sent by the remote unit to actuators in the process.
    """

    def __init__(self, actuatorMinimum=0.0, remoteControlled=False, actuatorMaximum=0.0, Control=None, *args, **kw_args):
        """Initialises a new 'RemoteControl' instance.

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

        super(RemoteControl, self).__init__(*args, **kw_args)

    _attrs = ["actuatorMinimum", "remoteControlled", "actuatorMaximum"]
    _attr_types = {"actuatorMinimum": float, "remoteControlled": bool, "actuatorMaximum": float}
    _defaults = {"actuatorMinimum": 0.0, "remoteControlled": False, "actuatorMaximum": 0.0}
    _enums = {}
    _refs = ["Control"]
    _many_refs = []

    def getControl(self):
        """The Control for the RemoteControl point.
        """
        return self._Control

    def setControl(self, value):
        if self._Control is not None:
            self._Control._RemoteControl = None

        self._Control = value
        if self._Control is not None:
            self._Control.RemoteControl = None
            self._Control._RemoteControl = self

    Control = property(getControl, setControl)

