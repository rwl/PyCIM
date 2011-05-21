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

class DemandResponseProgram(IdentifiedObject):
    """Demand response program.
    """

    def __init__(self, type='', CustomerAgreements=None, EndDeviceControls=None, validityInterval=None, EndDeviceGroups=None, *args, **kw_args):
        """Initialises a new 'DemandResponseProgram' instance.

        @param type: Type of demand response program; examples are CPP (critical-peak pricing), RTP (real-time pricing), DLC (direct load control), DBP (demand bidding program), BIP (base interruptible program). Note that possible types change a lot and it would be impossible to enumerate them all. 
        @param CustomerAgreements: All customer agreements with this demand response program.
        @param EndDeviceControls: All end device controls with this demand response program.
        @param validityInterval: Interval within which the program is valid.
        @param EndDeviceGroups: All groups of end devices with this demand response program.
        """
        #: Type of demand response program; examples are CPP (critical-peak pricing), RTP (real-time pricing), DLC (direct load control), DBP (demand bidding program), BIP (base interruptible program). Note that possible types change a lot and it would be impossible to enumerate them all.
        self.type = type

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._EndDeviceControls = []
        self.EndDeviceControls = [] if EndDeviceControls is None else EndDeviceControls

        self.validityInterval = validityInterval

        self._EndDeviceGroups = []
        self.EndDeviceGroups = [] if EndDeviceGroups is None else EndDeviceGroups

        super(DemandResponseProgram, self).__init__(*args, **kw_args)

    _attrs = ["type"]
    _attr_types = {"type": str}
    _defaults = {"type": ''}
    _enums = {}
    _refs = ["CustomerAgreements", "EndDeviceControls", "validityInterval", "EndDeviceGroups"]
    _many_refs = ["CustomerAgreements", "EndDeviceControls", "EndDeviceGroups"]

    def getCustomerAgreements(self):
        """All customer agreements with this demand response program.
        """
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for x in self._CustomerAgreements:
            x.DemandResponseProgram = None
        for y in value:
            y._DemandResponseProgram = self
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj.DemandResponseProgram = self

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj.DemandResponseProgram = None

    def getEndDeviceControls(self):
        """All end device controls with this demand response program.
        """
        return self._EndDeviceControls

    def setEndDeviceControls(self, value):
        for x in self._EndDeviceControls:
            x.DemandResponseProgram = None
        for y in value:
            y._DemandResponseProgram = self
        self._EndDeviceControls = value

    EndDeviceControls = property(getEndDeviceControls, setEndDeviceControls)

    def addEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj.DemandResponseProgram = self

    def removeEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj.DemandResponseProgram = None

    # Interval within which the program is valid.
    validityInterval = None

    def getEndDeviceGroups(self):
        """All groups of end devices with this demand response program.
        """
        return self._EndDeviceGroups

    def setEndDeviceGroups(self, value):
        for x in self._EndDeviceGroups:
            x.DemandResponseProgram = None
        for y in value:
            y._DemandResponseProgram = self
        self._EndDeviceGroups = value

    EndDeviceGroups = property(getEndDeviceGroups, setEndDeviceGroups)

    def addEndDeviceGroups(self, *EndDeviceGroups):
        for obj in EndDeviceGroups:
            obj.DemandResponseProgram = self

    def removeEndDeviceGroups(self, *EndDeviceGroups):
        for obj in EndDeviceGroups:
            obj.DemandResponseProgram = None

