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

from CIM14.Element import Element

class RemoteConnectDisconnectInfo(Element):
    """Details of remote connect disconnect function.
    """

    def __init__(self, needsPowerLimitCheck=False, isEnergyLimiting=False, isArmConnect=False, energyUsageWarning=0.0, armedTimeout=0.0, energyUsageStartDateTime='', isArmDisconnect=False, needsVoltageLimitCheck=False, powerLimit=0.0, usePushbutton=False, customerVoltageLimit=0.0, energyLimit=0.0, *args, **kw_args):
        """Initialises a new 'RemoteConnectDisconnectInfo' instance.

        @param needsPowerLimitCheck: True if load limit must be checked to issue an immediate disconnect (after a connect) if load is over the limit. 
        @param isEnergyLimiting: True if the energy usage is limited and the customer will be disconnected if they go over the limit. 
        @param isArmConnect: True if the RCD switch must be armed before a connect action can be initiated. 
        @param energyUsageWarning: Warning energy limit, used to trigger event code that energy usage is nearing limit. 
        @param armedTimeout: Setting of the timeout elapsed time. 
        @param energyUsageStartDateTime: Start date and time to accumulate energy for energy usage limiting. 
        @param isArmDisconnect: True if the RCD switch must be armed before a disconnect action can be initiated. 
        @param needsVoltageLimitCheck: True if voltage limit must be checked to prevent connect if voltage is over the limit. 
        @param powerLimit: Load limit above which the connect should either not take place or should cause an immediate disconnect. 
        @param usePushbutton: True if pushbutton must be used for connect. 
        @param customerVoltageLimit: Voltage limit on customer side of RCD switch above which the connect should not be made. 
        @param energyLimit: Limit of energy before disconnect. 
        """
        #: True if load limit must be checked to issue an immediate disconnect (after a connect) if load is over the limit.
        self.needsPowerLimitCheck = needsPowerLimitCheck

        #: True if the energy usage is limited and the customer will be disconnected if they go over the limit.
        self.isEnergyLimiting = isEnergyLimiting

        #: True if the RCD switch must be armed before a connect action can be initiated.
        self.isArmConnect = isArmConnect

        #: Warning energy limit, used to trigger event code that energy usage is nearing limit.
        self.energyUsageWarning = energyUsageWarning

        #: Setting of the timeout elapsed time.
        self.armedTimeout = armedTimeout

        #: Start date and time to accumulate energy for energy usage limiting.
        self.energyUsageStartDateTime = energyUsageStartDateTime

        #: True if the RCD switch must be armed before a disconnect action can be initiated.
        self.isArmDisconnect = isArmDisconnect

        #: True if voltage limit must be checked to prevent connect if voltage is over the limit.
        self.needsVoltageLimitCheck = needsVoltageLimitCheck

        #: Load limit above which the connect should either not take place or should cause an immediate disconnect.
        self.powerLimit = powerLimit

        #: True if pushbutton must be used for connect.
        self.usePushbutton = usePushbutton

        #: Voltage limit on customer side of RCD switch above which the connect should not be made.
        self.customerVoltageLimit = customerVoltageLimit

        #: Limit of energy before disconnect.
        self.energyLimit = energyLimit

        super(RemoteConnectDisconnectInfo, self).__init__(*args, **kw_args)

    _attrs = ["needsPowerLimitCheck", "isEnergyLimiting", "isArmConnect", "energyUsageWarning", "armedTimeout", "energyUsageStartDateTime", "isArmDisconnect", "needsVoltageLimitCheck", "powerLimit", "usePushbutton", "customerVoltageLimit", "energyLimit"]
    _attr_types = {"needsPowerLimitCheck": bool, "isEnergyLimiting": bool, "isArmConnect": bool, "energyUsageWarning": float, "armedTimeout": float, "energyUsageStartDateTime": str, "isArmDisconnect": bool, "needsVoltageLimitCheck": bool, "powerLimit": float, "usePushbutton": bool, "customerVoltageLimit": float, "energyLimit": float}
    _defaults = {"needsPowerLimitCheck": False, "isEnergyLimiting": False, "isArmConnect": False, "energyUsageWarning": 0.0, "armedTimeout": 0.0, "energyUsageStartDateTime": '', "isArmDisconnect": False, "needsVoltageLimitCheck": False, "powerLimit": 0.0, "usePushbutton": False, "customerVoltageLimit": 0.0, "energyLimit": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

