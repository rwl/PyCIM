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

from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment

class RegulatingCondEq(ConductingEquipment):
    """A type of conducting equipment that can regulate a quanity (i.e. voltage or flow) at a specific point in the network.
    """

    def __init__(self, Controls=None, RegulatingControl=None, *args, **kw_args):
        """Initialises a new 'RegulatingCondEq' instance.

        @param Controls: The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator.
        @param RegulatingControl: The regulating control scheme in which this equipment participates.
        """
        self._Controls = []
        self.Controls = [] if Controls is None else Controls

        self._RegulatingControl = None
        self.RegulatingControl = RegulatingControl

        super(RegulatingCondEq, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Controls", "RegulatingControl"]
    _many_refs = ["Controls"]

    def getControls(self):
        """The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator.
        """
        return self._Controls

    def setControls(self, value):
        for x in self._Controls:
            x.RegulatingCondEq = None
        for y in value:
            y._RegulatingCondEq = self
        self._Controls = value

    Controls = property(getControls, setControls)

    def addControls(self, *Controls):
        for obj in Controls:
            obj.RegulatingCondEq = self

    def removeControls(self, *Controls):
        for obj in Controls:
            obj.RegulatingCondEq = None

    def getRegulatingControl(self):
        """The regulating control scheme in which this equipment participates.
        """
        return self._RegulatingControl

    def setRegulatingControl(self, value):
        if self._RegulatingControl is not None:
            filtered = [x for x in self.RegulatingControl.RegulatingCondEq if x != self]
            self._RegulatingControl._RegulatingCondEq = filtered

        self._RegulatingControl = value
        if self._RegulatingControl is not None:
            if self not in self._RegulatingControl._RegulatingCondEq:
                self._RegulatingControl._RegulatingCondEq.append(self)

    RegulatingControl = property(getRegulatingControl, setRegulatingControl)

