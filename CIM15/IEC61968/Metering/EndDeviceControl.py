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

class EndDeviceControl(IdentifiedObject):
    """Instructs an end device (or an end device group) to perform a specified action.Instructs an end device (or an end device group) to perform a specified action.
    """

    def __init__(self, drProgramLevel=0, drProgramMandatory=False, type='', priceSignal=0.0, DemandResponseProgram=None, CustomerAgreement=None, scheduledInterval=None, EndDeviceGroup=None, EndDevice=None, *args, **kw_args):
        """Initialises a new 'EndDeviceControl' instance.

        @param drProgramLevel: Level of a demand response program request, where 0=emergency. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it). 
        @param drProgramMandatory: Whether a demand response program request is mandatory. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it). 
        @param type: Type of control. 
        @param priceSignal: (if applicable) Price signal used as parameter for this end device control. 
        @param DemandResponseProgram: Demand response program for this end device control.
        @param CustomerAgreement: Could be deprecated in the future.
        @param scheduledInterval: (if control has scheduled duration) Date and time interval the control has been scheduled to execute within.
        @param EndDeviceGroup: End device group receiving commands from this end device control.
        @param EndDevice: End device receiving commands from this end device control.
        """
        #: Level of a demand response program request, where 0=emergency. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it).
        self.drProgramLevel = drProgramLevel

        #: Whether a demand response program request is mandatory. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it).
        self.drProgramMandatory = drProgramMandatory

        #: Type of control.
        self.type = type

        #: (if applicable) Price signal used as parameter for this end device control.
        self.priceSignal = priceSignal

        self._DemandResponseProgram = None
        self.DemandResponseProgram = DemandResponseProgram

        self._CustomerAgreement = None
        self.CustomerAgreement = CustomerAgreement

        self.scheduledInterval = scheduledInterval

        self._EndDeviceGroup = None
        self.EndDeviceGroup = EndDeviceGroup

        self._EndDevice = None
        self.EndDevice = EndDevice

        super(EndDeviceControl, self).__init__(*args, **kw_args)

    _attrs = ["drProgramLevel", "drProgramMandatory", "type", "priceSignal"]
    _attr_types = {"drProgramLevel": int, "drProgramMandatory": bool, "type": str, "priceSignal": float}
    _defaults = {"drProgramLevel": 0, "drProgramMandatory": False, "type": '', "priceSignal": 0.0}
    _enums = {}
    _refs = ["DemandResponseProgram", "CustomerAgreement", "scheduledInterval", "EndDeviceGroup", "EndDevice"]
    _many_refs = []

    def getDemandResponseProgram(self):
        """Demand response program for this end device control.
        """
        return self._DemandResponseProgram

    def setDemandResponseProgram(self, value):
        if self._DemandResponseProgram is not None:
            filtered = [x for x in self.DemandResponseProgram.EndDeviceControls if x != self]
            self._DemandResponseProgram._EndDeviceControls = filtered

        self._DemandResponseProgram = value
        if self._DemandResponseProgram is not None:
            if self not in self._DemandResponseProgram._EndDeviceControls:
                self._DemandResponseProgram._EndDeviceControls.append(self)

    DemandResponseProgram = property(getDemandResponseProgram, setDemandResponseProgram)

    def getCustomerAgreement(self):
        """Could be deprecated in the future.
        """
        return self._CustomerAgreement

    def setCustomerAgreement(self, value):
        if self._CustomerAgreement is not None:
            filtered = [x for x in self.CustomerAgreement.EndDeviceControls if x != self]
            self._CustomerAgreement._EndDeviceControls = filtered

        self._CustomerAgreement = value
        if self._CustomerAgreement is not None:
            if self not in self._CustomerAgreement._EndDeviceControls:
                self._CustomerAgreement._EndDeviceControls.append(self)

    CustomerAgreement = property(getCustomerAgreement, setCustomerAgreement)

    # (if control has scheduled duration) Date and time interval the control has been scheduled to execute within.
    scheduledInterval = None

    def getEndDeviceGroup(self):
        """End device group receiving commands from this end device control.
        """
        return self._EndDeviceGroup

    def setEndDeviceGroup(self, value):
        if self._EndDeviceGroup is not None:
            filtered = [x for x in self.EndDeviceGroup.EndDeviceControls if x != self]
            self._EndDeviceGroup._EndDeviceControls = filtered

        self._EndDeviceGroup = value
        if self._EndDeviceGroup is not None:
            if self not in self._EndDeviceGroup._EndDeviceControls:
                self._EndDeviceGroup._EndDeviceControls.append(self)

    EndDeviceGroup = property(getEndDeviceGroup, setEndDeviceGroup)

    def getEndDevice(self):
        """End device receiving commands from this end device control.
        """
        return self._EndDevice

    def setEndDevice(self, value):
        if self._EndDevice is not None:
            filtered = [x for x in self.EndDevice.EndDeviceControls if x != self]
            self._EndDevice._EndDeviceControls = filtered

        self._EndDevice = value
        if self._EndDevice is not None:
            if self not in self._EndDevice._EndDeviceControls:
                self._EndDevice._EndDeviceControls.append(self)

    EndDevice = property(getEndDevice, setEndDevice)

