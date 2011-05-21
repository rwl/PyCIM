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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Control(IdentifiedObject):
    """Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.
    """

    def __init__(self, timeStamp='', operationInProgress=False, Unit=None, RegulatingCondEq=None, ControlType=None, RemoteControl=None, *args, **kw_args):
        """Initialises a new 'Control' instance.

        @param timeStamp: The last time a control output was sent 
        @param operationInProgress: Indicates that a client is currently sending control commands that has not completed 
        @param Unit: The Unit for the Control.
        @param RegulatingCondEq: Regulating device governed by this control output.
        @param ControlType: The type of Control
        @param RemoteControl: The remote point controlling the physical actuator.
        """
        #: The last time a control output was sent
        self.timeStamp = timeStamp

        #: Indicates that a client is currently sending control commands that has not completed
        self.operationInProgress = operationInProgress

        self._Unit = None
        self.Unit = Unit

        self._RegulatingCondEq = None
        self.RegulatingCondEq = RegulatingCondEq

        self._ControlType = None
        self.ControlType = ControlType

        self._RemoteControl = None
        self.RemoteControl = RemoteControl

        super(Control, self).__init__(*args, **kw_args)

    _attrs = ["timeStamp", "operationInProgress"]
    _attr_types = {"timeStamp": str, "operationInProgress": bool}
    _defaults = {"timeStamp": '', "operationInProgress": False}
    _enums = {}
    _refs = ["Unit", "RegulatingCondEq", "ControlType", "RemoteControl"]
    _many_refs = []

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
            if self not in self._Unit._Controls:
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
            if self not in self._RegulatingCondEq._Controls:
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
            if self not in self._ControlType._Controls:
                self._ControlType._Controls.append(self)

    ControlType = property(getControlType, setControlType)

    def getRemoteControl(self):
        """The remote point controlling the physical actuator.
        """
        return self._RemoteControl

    def setRemoteControl(self, value):
        if self._RemoteControl is not None:
            self._RemoteControl._Control = None

        self._RemoteControl = value
        if self._RemoteControl is not None:
            self._RemoteControl.Control = None
            self._RemoteControl._Control = self

    RemoteControl = property(getRemoteControl, setRemoteControl)

