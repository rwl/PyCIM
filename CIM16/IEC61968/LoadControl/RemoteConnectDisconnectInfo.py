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


class RemoteConnectDisconnectInfo(object):
    """Details of remote connect disconnect function.Details of remote connect disconnect function.
    """

    def __init__(self, isArmConnect=False, energyUsageWarning=0.0, needsVoltageLimitCheck=False, customerVoltageLimit=0.0, isArmDisconnect=False, isEnergyLimiting=False, armedTimeout=0.0, powerLimit=0.0, needsPowerLimitCheck=False, usePushbutton=False, energyLimit=0.0, energyUsageStartDateTime=''):
        """Initialises a new 'RemoteConnectDisconnectInfo' instance.

        @param isArmConnect: True if the RCD switch must be armed before a connect action can be initiated. 
        @param energyUsageWarning: Warning energy limit, used to trigger event code that energy usage is nearing limit. 
        @param needsVoltageLimitCheck: True if voltage limit must be checked to prevent connect if voltage is over the limit. 
        @param customerVoltageLimit: Voltage limit on customer side of RCD switch above which the connect should not be made. 
        @param isArmDisconnect: True if the RCD switch must be armed before a disconnect action can be initiated. 
        @param isEnergyLimiting: True if the energy usage is limited and the customer will be disconnected if they go over the limit. 
        @param armedTimeout: Setting of the timeout elapsed time. 
        @param powerLimit: Load limit above which the connect should either not take place or should cause an immediate disconnect. 
        @param needsPowerLimitCheck: True if load limit must be checked to issue an immediate disconnect (after a connect) if load is over the limit. 
        @param usePushbutton: True if pushbutton must be used for connect. 
        @param energyLimit: Limit of energy before disconnect. 
        @param energyUsageStartDateTime: Start date and time to accumulate energy for energy usage limiting. 
        """
        #: True if the RCD switch must be armed before a connect action can be initiated.
        self.isArmConnect = isArmConnect

        #: Warning energy limit, used to trigger event code that energy usage is nearing limit.
        self.energyUsageWarning = energyUsageWarning

        #: True if voltage limit must be checked to prevent connect if voltage is over the limit.
        self.needsVoltageLimitCheck = needsVoltageLimitCheck

        #: Voltage limit on customer side of RCD switch above which the connect should not be made.
        self.customerVoltageLimit = customerVoltageLimit

        #: True if the RCD switch must be armed before a disconnect action can be initiated.
        self.isArmDisconnect = isArmDisconnect

        #: True if the energy usage is limited and the customer will be disconnected if they go over the limit.
        self.isEnergyLimiting = isEnergyLimiting

        #: Setting of the timeout elapsed time.
        self.armedTimeout = armedTimeout

        #: Load limit above which the connect should either not take place or should cause an immediate disconnect.
        self.powerLimit = powerLimit

        #: True if load limit must be checked to issue an immediate disconnect (after a connect) if load is over the limit.
        self.needsPowerLimitCheck = needsPowerLimitCheck

        #: True if pushbutton must be used for connect.
        self.usePushbutton = usePushbutton

        #: Limit of energy before disconnect.
        self.energyLimit = energyLimit

        #: Start date and time to accumulate energy for energy usage limiting.
        self.energyUsageStartDateTime = energyUsageStartDateTime


    _attrs = ["isArmConnect", "energyUsageWarning", "needsVoltageLimitCheck", "customerVoltageLimit", "isArmDisconnect", "isEnergyLimiting", "armedTimeout", "powerLimit", "needsPowerLimitCheck", "usePushbutton", "energyLimit", "energyUsageStartDateTime"]
    _attr_types = {"isArmConnect": bool, "energyUsageWarning": float, "needsVoltageLimitCheck": bool, "customerVoltageLimit": float, "isArmDisconnect": bool, "isEnergyLimiting": bool, "armedTimeout": float, "powerLimit": float, "needsPowerLimitCheck": bool, "usePushbutton": bool, "energyLimit": float, "energyUsageStartDateTime": str}
    _defaults = {"isArmConnect": False, "energyUsageWarning": 0.0, "needsVoltageLimitCheck": False, "customerVoltageLimit": 0.0, "isArmDisconnect": False, "isEnergyLimiting": False, "armedTimeout": 0.0, "powerLimit": 0.0, "needsPowerLimitCheck": False, "usePushbutton": False, "energyLimit": 0.0, "energyUsageStartDateTime": ''}
    _enums = {}
    _refs = []
    _many_refs = []

