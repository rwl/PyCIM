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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BranchGroup(IdentifiedObject):
    """A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network.A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network.
    """

    def __init__(self, minimumReactivePower=0.0, maximumReactivePower=0.0, maximumActivePower=0.0, minimumActivePower=0.0, monitorActivePower=False, monitorReactivePower=False, BranchGroupTerminal=None, *args, **kw_args):
        """Initialises a new 'BranchGroup' instance.

        @param minimumReactivePower: The minimum reactive power flow. 
        @param maximumReactivePower: The maximum reactive power flow. 
        @param maximumActivePower: The maximum active power flow. 
        @param minimumActivePower: The minimum active power flow. 
        @param monitorActivePower: Monitor the active power flow. 
        @param monitorReactivePower: Monitor the reactive power flow. 
        @param BranchGroupTerminal: The directed branch group terminals to be summed.
        """
        #: The minimum reactive power flow.
        self.minimumReactivePower = minimumReactivePower

        #: The maximum reactive power flow.
        self.maximumReactivePower = maximumReactivePower

        #: The maximum active power flow.
        self.maximumActivePower = maximumActivePower

        #: The minimum active power flow.
        self.minimumActivePower = minimumActivePower

        #: Monitor the active power flow.
        self.monitorActivePower = monitorActivePower

        #: Monitor the reactive power flow.
        self.monitorReactivePower = monitorReactivePower

        self._BranchGroupTerminal = []
        self.BranchGroupTerminal = [] if BranchGroupTerminal is None else BranchGroupTerminal

        super(BranchGroup, self).__init__(*args, **kw_args)

    _attrs = ["minimumReactivePower", "maximumReactivePower", "maximumActivePower", "minimumActivePower", "monitorActivePower", "monitorReactivePower"]
    _attr_types = {"minimumReactivePower": float, "maximumReactivePower": float, "maximumActivePower": float, "minimumActivePower": float, "monitorActivePower": bool, "monitorReactivePower": bool}
    _defaults = {"minimumReactivePower": 0.0, "maximumReactivePower": 0.0, "maximumActivePower": 0.0, "minimumActivePower": 0.0, "monitorActivePower": False, "monitorReactivePower": False}
    _enums = {}
    _refs = ["BranchGroupTerminal"]
    _many_refs = ["BranchGroupTerminal"]

    def getBranchGroupTerminal(self):
        """The directed branch group terminals to be summed.
        """
        return self._BranchGroupTerminal

    def setBranchGroupTerminal(self, value):
        for x in self._BranchGroupTerminal:
            x.BranchGroup = None
        for y in value:
            y._BranchGroup = self
        self._BranchGroupTerminal = value

    BranchGroupTerminal = property(getBranchGroupTerminal, setBranchGroupTerminal)

    def addBranchGroupTerminal(self, *BranchGroupTerminal):
        for obj in BranchGroupTerminal:
            obj.BranchGroup = self

    def removeBranchGroupTerminal(self, *BranchGroupTerminal):
        for obj in BranchGroupTerminal:
            obj.BranchGroup = None

