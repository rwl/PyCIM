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

class Control(IdentifiedObject):
    """Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.
    """

    def __init__(self, timeStamp='', operationInProgress=False, RemoteControl=None, Unit=None, RegulatingCondEq=None, ControlType=None, *args, **kw_args):
        """Initializes a new 'Control' instance.

        @param timeStamp: The last time a control output was sent 
        @param operationInProgress: Indicates that a client is currently sending control commands that has not completed 
        @param RemoteControl: The remote point controlling the physical actuator.
        @param Unit: The Unit for the Control.
        @param RegulatingCondEq: Regulating device governed by this control output.
        @param ControlType: The type of Control
        """
        #: The last time a control output was sent 
        self.timeStamp = timeStamp

        #: Indicates that a client is currently sending control commands that has not completed 
        self.operationInProgress = operationInProgress

        self._RemoteControl = None
        self.RemoteControl = RemoteControl

        self._Unit = None
        self.Unit = Unit

        self._RegulatingCondEq = None
        self.RegulatingCondEq = RegulatingCondEq

        self._ControlType = None
        self.ControlType = ControlType

        super(Control, self).__init__(*args, **kw_args)

    def getRemoteControl(self):
        """The remote point controlling the physical actuator.
        """
        return self._RemoteControl

    def setRemoteControl(self, value):
        if self._RemoteControl is not None:
            self._RemoteControl._Control = None

        self._RemoteControl = value
        if self._RemoteControl is not None:
            self._RemoteControl._Control = self

    RemoteControl = property(getRemoteControl, setRemoteControl)

    def getUnit(self):
        """The Unit for the Control.
        """
        return self._Unit

    def setUnit(self, value):
        if self._Unit is not None:
            filtered = [x for x in self.Unit.Controls if x != self]
            self._Unit._Controls = filtered

        self._Unit = value
        if self._Unit is not None:
            self._Unit._Controls.append(self)

    Unit = property(getUnit, setUnit)

    def getRegulatingCondEq(self):
        """Regulating device governed by this control output.
        """
        return self._RegulatingCondEq

    def setRegulatingCondEq(self, value):
        if self._RegulatingCondEq is not None:
            filtered = [x for x in self.RegulatingCondEq.Controls if x != self]
            self._RegulatingCondEq._Controls = filtered

        self._RegulatingCondEq = value
        if self._RegulatingCondEq is not None:
            self._RegulatingCondEq._Controls.append(self)

    RegulatingCondEq = property(getRegulatingCondEq, setRegulatingCondEq)

    def getControlType(self):
        """The type of Control
        """
        return self._ControlType

    def setControlType(self, value):
        if self._ControlType is not None:
            filtered = [x for x in self.ControlType.Controls if x != self]
            self._ControlType._Controls = filtered

        self._ControlType = value
        if self._ControlType is not None:
            self._ControlType._Controls.append(self)

    ControlType = property(getControlType, setControlType)

