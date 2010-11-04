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

from CIM14v13.Element import Element

class RemoteConnectDisconnectInfo(Element):
    """Details of remote connect disconnect function.
    """

    def __init__(self, isArmConnect=False, customerVoltageLimit=0.0, powerLimit=0.0, isEnergyLimiting=False, energyUsageWarning=0.0, isArmDisconnect=False, energyUsageStartDateTime='', needsVoltageLimitCheck=False, energyLimit=0.0, armedTimeout=0.0, needsPowerLimitCheck=False, usePushbutton=False, **kw_args):
        """Initializes a new 'RemoteConnectDisconnectInfo' instance.

        @param isArmConnect: True if the RCD switch must be armed before a connect action can be initiated. 
        @param customerVoltageLimit: Voltage limit on customer side of RCD switch above which the connect should not be made. 
        @param powerLimit: Load limit above which the connect should either not take place or should cause an immediate disconnect. 
        @param isEnergyLimiting: True if the energy usage is limited and the customer will be disconnected if they go over the limit. 
        @param energyUsageWarning: Warning energy limit, used to trigger event code that energy usage is nearing limit. 
        @param isArmDisconnect: True if the RCD switch must be armed before a disconnect action can be initiated. 
        @param energyUsageStartDateTime: Start date and time to accumulate energy for energy usage limiting. 
        @param needsVoltageLimitCheck: True if voltage limit must be checked to prevent connect if voltage is over the limit. 
        @param energyLimit: Limit of energy before disconnect. 
        @param armedTimeout: Setting of the timeout elapsed time. 
        @param needsPowerLimitCheck: True if load limit must be checked to issue an immediate disconnect (after a connect) if load is over the limit. 
        @param usePushbutton: True if pushbutton must be used for connect. 
        """
        #: True if the RCD switch must be armed before a connect action can be initiated.
        self.isArmConnect = isArmConnect

        #: Voltage limit on customer side of RCD switch above which the connect should not be made.
        self.customerVoltageLimit = customerVoltageLimit

        #: Load limit above which the connect should either not take place or should cause an immediate disconnect.
        self.powerLimit = powerLimit

        #: True if the energy usage is limited and the customer will be disconnected if they go over the limit.
        self.isEnergyLimiting = isEnergyLimiting

        #: Warning energy limit, used to trigger event code that energy usage is nearing limit.
        self.energyUsageWarning = energyUsageWarning

        #: True if the RCD switch must be armed before a disconnect action can be initiated.
        self.isArmDisconnect = isArmDisconnect

        #: Start date and time to accumulate energy for energy usage limiting.
        self.energyUsageStartDateTime = energyUsageStartDateTime

        #: True if voltage limit must be checked to prevent connect if voltage is over the limit.
        self.needsVoltageLimitCheck = needsVoltageLimitCheck

        #: Limit of energy before disconnect.
        self.energyLimit = energyLimit

        #: Setting of the timeout elapsed time.
        self.armedTimeout = armedTimeout

        #: True if load limit must be checked to issue an immediate disconnect (after a connect) if load is over the limit.
        self.needsPowerLimitCheck = needsPowerLimitCheck

        #: True if pushbutton must be used for connect.
        self.usePushbutton = usePushbutton

        super(RemoteConnectDisconnectInfo, self).__init__(**kw_args)

