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

from CIM15.IEC61970.Core.Equipment import Equipment

class CompositeSwitch(Equipment):
    """A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.
    """

    def __init__(self, compositeSwitchType='', Switches=None, *args, **kw_args):
        """Initialises a new 'CompositeSwitch' instance.

        @param compositeSwitchType: An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any 
        @param Switches: Switches contained in this Composite switch.
        """
        #: An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any
        self.compositeSwitchType = compositeSwitchType

        self._Switches = []
        self.Switches = [] if Switches is None else Switches

        super(CompositeSwitch, self).__init__(*args, **kw_args)

    _attrs = ["compositeSwitchType"]
    _attr_types = {"compositeSwitchType": str}
    _defaults = {"compositeSwitchType": ''}
    _enums = {}
    _refs = ["Switches"]
    _many_refs = ["Switches"]

    def getSwitches(self):
        """Switches contained in this Composite switch.
        """
        return self._Switches

    def setSwitches(self, value):
        for x in self._Switches:
            x.CompositeSwitch = None
        for y in value:
            y._CompositeSwitch = self
        self._Switches = value

    Switches = property(getSwitches, setSwitches)

    def addSwitches(self, *Switches):
        for obj in Switches:
            obj.CompositeSwitch = self

    def removeSwitches(self, *Switches):
        for obj in Switches:
            obj.CompositeSwitch = None

