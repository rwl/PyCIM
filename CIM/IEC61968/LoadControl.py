#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" This package is an extension of the Metering package and contains the information classes that support specialized applications such as demand-side management using load control equipment. These classes are generally associated with the point where a service is delivered to the customer.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Metering import DeviceFunction
from CIM import Element
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import RealEnergy
from CIM.IEC61970.Domain import Seconds



from enthought.traits.api import Instance, List, Property, Bool, Int, Date
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ConnectDisconnectFunction" class:
#------------------------------------------------------------------------------

class ConnectDisconnectFunction(DeviceFunction):
    """ A function that will disconnect or reconnect the customer's load under defined conditions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Information on remote connect disconnect switch.
    rcdInfo = Instance("CIM.IEC61968.LoadControl.RemoteConnectDisconnectInfo",
        desc="Information on remote connect disconnect switch.",
        transient=True,
        editor=InstanceEditor(name="_remoteconnectdisconnectinfos"))

    def _get_remoteconnectdisconnectinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.LoadControl.RemoteConnectDisconnectInfo" ]
        else:
            return []

    _remoteconnectdisconnectinfos = Property(fget=_get_remoteconnectdisconnectinfos)

    Switches = List(Instance("CIM.IEC61970.Wires.Switch"))

    # If set true, the switch may disconnect the service at the end of a specified time delay after the disconnect signal had been given. If set false, the switch may disconnect the service immediately after the disconnect signal had been given. This is typically the case for over current circuit-breakers which are classified as either instantaneous or slow acting.
    isDelayedDiscon = Bool(desc="If set true, the switch may disconnect the service at the end of a specified time delay after the disconnect signal had been given. If set false, the switch may disconnect the service immediately after the disconnect signal had been given. This is typically the case for over current circuit-breakers which are classified as either instantaneous or slow acting.")

    # True if this function is in the connected state.
    isConnected = Bool(desc="True if this function is in the connected state.")

    # Running cumulative count of (connect or disconnect) events, for the lifetime of this function or until the value is cleared.
    eventCount = Int(desc="Running cumulative count of (connect or disconnect) events, for the lifetime of this function or until the value is cleared.")

    # (if disconnection can be operated locally) If set true, the operation happens automatically, otherwise it happens manually.
    isLocalAutoDisconOp = Bool(desc="(if disconnection can be operated locally) If set true, the operation happens automatically, otherwise it happens manually.")

    # If set true and if disconnection can be operated remotely, then the operation happens automatically. If set false and if disconnection can be operated remotely, then the operation happens manually.
    isRemoteAutoDisconOp = Bool(desc="If set true and if disconnection can be operated remotely, then the operation happens automatically. If set false and if disconnection can be operated remotely, then the operation happens manually.")

    # If set true and if reconnection can be operated remotely, then the operation happens automatically. If false and if reconnection can be operated remotely, then the operation happens manually.
    isRemoteAutoReconOp = Bool(desc="If set true and if reconnection can be operated remotely, then the operation happens automatically. If false and if reconnection can be operated remotely, then the operation happens manually.")

    # If set true and if reconnection can be operated locally, then the operation happens automatically. Otherwise, it is manually.
    isLocalAutoReconOp = Bool(desc="If set true and if reconnection can be operated locally, then the operation happens automatically. Otherwise, it is manually.")

    #--------------------------------------------------------------------------
    #  Begin "ConnectDisconnectFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID", "disabled", "isDelayedDiscon", "isConnected", "eventCount", "isLocalAutoDisconOp", "isRemoteAutoDisconOp", "isRemoteAutoReconOp", "isLocalAutoReconOp",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel", "ComEquipmentAsset", "EndDeviceAsset", "Registers", "EndDeviceEvents", "rcdInfo", "Switches",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.LoadControl.ConnectDisconnectFunction",
        title="ConnectDisconnectFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConnectDisconnectFunction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RemoteConnectDisconnectInfo" class:
#------------------------------------------------------------------------------

class RemoteConnectDisconnectInfo(Element):
    """ Details of remote connect disconnect function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # True if the RCD switch must be armed before a connect action can be initiated.
    isArmConnect = Bool(desc="True if the RCD switch must be armed before a connect action can be initiated.")

    # Voltage limit on customer side of RCD switch above which the connect should not be made.
    customerVoltageLimit = Voltage(desc="Voltage limit on customer side of RCD switch above which the connect should not be made.")

    # Load limit above which the connect should either not take place or should cause an immediate disconnect.
    powerLimit = ActivePower(desc="Load limit above which the connect should either not take place or should cause an immediate disconnect.")

    # True if the energy usage is limited and the customer will be disconnected if they go over the limit.
    isEnergyLimiting = Bool(desc="True if the energy usage is limited and the customer will be disconnected if they go over the limit.")

    # Warning energy limit, used to trigger event code that energy usage is nearing limit.
    energyUsageWarning = RealEnergy(desc="Warning energy limit, used to trigger event code that energy usage is nearing limit.")

    # True if the RCD switch must be armed before a disconnect action can be initiated.
    isArmDisconnect = Bool(desc="True if the RCD switch must be armed before a disconnect action can be initiated.")

    # Start date and time to accumulate energy for energy usage limiting.
    energyUsageStartDateTime = Date(desc="Start date and time to accumulate energy for energy usage limiting.")

    # True if voltage limit must be checked to prevent connect if voltage is over the limit.
    needsVoltageLimitCheck = Bool(desc="True if voltage limit must be checked to prevent connect if voltage is over the limit.")

    # Limit of energy before disconnect.
    energyLimit = RealEnergy(desc="Limit of energy before disconnect.")

    # Setting of the timeout elapsed time.
    armedTimeout = Seconds(desc="Setting of the timeout elapsed time.")

    # True if load limit must be checked to issue an immediate disconnect (after a connect) if load is over the limit.
    needsPowerLimitCheck = Bool(desc="True if load limit must be checked to issue an immediate disconnect (after a connect) if load is over the limit.")

    # True if pushbutton must be used for connect.
    usePushbutton = Bool(desc="True if pushbutton must be used for connect.")

    #--------------------------------------------------------------------------
    #  Begin "RemoteConnectDisconnectInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "isArmConnect", "customerVoltageLimit", "powerLimit", "isEnergyLimiting", "energyUsageWarning", "isArmDisconnect", "energyUsageStartDateTime", "needsVoltageLimitCheck", "energyLimit", "armedTimeout", "needsPowerLimitCheck", "usePushbutton",
                label="Attributes", columns=1),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.LoadControl.RemoteConnectDisconnectInfo",
        title="RemoteConnectDisconnectInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RemoteConnectDisconnectInfo" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
