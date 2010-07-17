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

""" This package provides the capability to schedule and account for transactions for the exchange of electric power between companies. It includes transations for megawatts which are generated, consumed, lost, passed through, sold and purchased. These classes are used by Accounting and Billing for Energy, Generation Capacity, Transmission, and Ancillary Services.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Common import Document
from CIM.IEC61970.Core import Curve
from CIM import Element
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.ControlArea import ControlArea
from CIM.IEC61970.Core import PowerSystemResource
from CIM.IEC61968.Common import Agreement
from CIM.IEC61970.Core import RegularIntervalSchedule
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import Money
from CIM.IEC61970.Domain import RealEnergy
from CIM.IEC61970.Domain import Frequency



from enthought.traits.api import Instance, List, Property, Enum, Bool, Str, Date, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


AreaControlMode = Enum("OFF", "TLB", "CF", "CTL")

#------------------------------------------------------------------------------
#  "EnergyTransaction" class:
#------------------------------------------------------------------------------

class EnergyTransaction(Document):
    """ Specifies the schedule for energy transfers between interchange areas that are necessary to satisfy the associated interchange transaction.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # { Approve | Deny | Study }
    state = Instance("CIM.EnumeratedType",
        desc="{ Approve | Deny | Study }",
        transient=True,
        editor=InstanceEditor(name="_enumeratedtypes"))

    def _get_enumeratedtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.EnumeratedType" ]
        else:
            return []

    _enumeratedtypes = Property(fget=_get_enumeratedtypes)

    # An EnergyTransaction may be curtailed by any of the participating entities.
    CurtailmentProfiles = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.CurtailmentProfile"),
        desc="An EnergyTransaction may be curtailed by any of the participating entities.")

    # Energy is transferred between interchange areas
    Export_SubControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.SubControlArea",
        desc="Energy is transferred between interchange areas",
        transient=True,
        opposite="Export_EnergyTransactions",
        editor=InstanceEditor(name="_subcontrolareas"))

    def _get_subcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.SubControlArea" ]
        else:
            return []

    _subcontrolareas = Property(fget=_get_subcontrolareas)

    EnergyTransId = List(Instance("CIM.IEC61968.Informative.MarketOperations.TransactionBid"))

    # Energy is transferred between interchange areas
    Import_SubControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.SubControlArea",
        desc="Energy is transferred between interchange areas",
        transient=True,
        opposite="Import_EnergyTransactions",
        editor=InstanceEditor(name="_subcontrolareas"))

    def _get_subcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.SubControlArea" ]
        else:
            return []

    _subcontrolareas = Property(fget=_get_subcontrolareas)

    EnergyPriceCurves = List(Instance("CIM.IEC61968.Informative.MarketOperations.EnergyPriceCurve"))

    # An EnergyTransaction may have a LossProfile.
    LossProfiles = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.LossProfile"),
        desc="An EnergyTransaction may have a LossProfile.")

    # An EnergyTransaction must have at least one EnergyProfile.
    EnergyProfiles = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyProfile"),
        desc="An EnergyTransaction must have at least one EnergyProfile.")

    # The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.
    EnergyProduct = Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyProduct",
        desc="The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.",
        transient=True,
        opposite="EnergyTransactions",
        editor=InstanceEditor(name="_energyproducts"))

    def _get_energyproducts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.EnergyProduct" ]
        else:
            return []

    _energyproducts = Property(fget=_get_energyproducts)

    # Receipt point active power
    receiptPointP = ActivePower(desc="Receipt point active power")

    # Transaction minimum active power if dispatchable
    energyMin = ActivePower(desc="Transaction minimum active power if dispatchable")

    # Firm interchange flag indicates whether or not this energy transaction can be changed without potential financial consequences.
    firmInterchangeFlag = Bool(desc="Firm interchange flag indicates whether or not this energy transaction can be changed without potential financial consequences.")

    # Maximum congestion charges in monetary units
    congestChargeMax = Money(desc="Maximum congestion charges in monetary units")

    reason = Str

    # Delivery point active power
    deliveryPointP = ActivePower(desc="Delivery point active power")

    #--------------------------------------------------------------------------
    #  Begin "EnergyTransaction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "receiptPointP", "energyMin", "firmInterchangeFlag", "congestChargeMax", "reason", "deliveryPointP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "state", "CurtailmentProfiles", "Export_SubControlArea", "EnergyTransId", "Import_SubControlArea", "EnergyPriceCurves", "LossProfiles", "EnergyProfiles", "EnergyProduct",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction",
        title="EnergyTransaction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyTransaction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AvailableTransmissionCapacity" class:
#------------------------------------------------------------------------------

class AvailableTransmissionCapacity(Curve):
    """ Amount of possible flow by direction.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transmission schedule posts the available transmission capacity for a transmission line.
    ScheduleFor = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionService"),
        desc="A transmission schedule posts the available transmission capacity for a transmission line.")

    #--------------------------------------------------------------------------
    #  Begin "AvailableTransmissionCapacity" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "ScheduleFor",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.AvailableTransmissionCapacity",
        title="AvailableTransmissionCapacity",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AvailableTransmissionCapacity" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProfileData" class:
#------------------------------------------------------------------------------

class ProfileData(Element):
    """ Data for profile.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A profile has profile data associated with it.
    Profile = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.Profile"),
        desc="A profile has profile data associated with it.")

    # Stop date/time for this profile.
    stopDateTime = Date(desc="Stop date/time for this profile.")

    # Energy level for the profile
    energyLevel = RealEnergy(desc="Energy level for the profile")

    # Start date/time for this profile.
    startDateTime = Date(desc="Start date/time for this profile.")

    # Active power capacity level for the profile.
    capacityLevel = ActivePower(desc="Active power capacity level for the profile.")

    # Sequence to provide item numbering for the profile. { greater than or equal to 1 }
    sequenceNumber = Int(desc="Sequence to provide item numbering for the profile. { greater than or equal to 1 }")

    #--------------------------------------------------------------------------
    #  Begin "ProfileData" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "stopDateTime", "energyLevel", "startDateTime", "capacityLevel", "sequenceNumber",
                label="Attributes"),
            VGroup("Parent", "Profile",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.ProfileData",
        title="ProfileData",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProfileData" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Profile" class:
#------------------------------------------------------------------------------

class Profile(IdentifiedObject):
    """ A profile is a simpler curve type.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A profile has profile data associated with it.
    ProfileDatas = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.ProfileData"),
        desc="A profile has profile data associated with it.")

    #--------------------------------------------------------------------------
    #  Begin "Profile" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ProfileDatas",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.Profile",
        title="Profile",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Profile" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubControlArea" class:
#------------------------------------------------------------------------------

class SubControlArea(ControlArea):
    """ SubControlArea replacement classed moved into EnergySchedulingPackage.  An area defined for the purpose of tracking interchange with surrounding areas via tie points; may or may not serve as a control area.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area
    Flowgate = List(Instance("CIM.IEC61968.Informative.MarketOperations.Flowgate"),
        desc="A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area")

    # Energy is transferred between interchange areas
    Export_EnergyTransactions = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction"),
        desc="Energy is transferred between interchange areas")

    # Energy is transferred between interchange areas
    Import_EnergyTransactions = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction"),
        desc="Energy is transferred between interchange areas")

    # The interchange area  may operate as a control area
    HostControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.HostControlArea",
        desc="The interchange area  may operate as a control area",
        transient=True,
        opposite="SubControlAreas",
        editor=InstanceEditor(name="_hostcontrolareas"))

    def _get_hostcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.HostControlArea" ]
        else:
            return []

    _hostcontrolareas = Property(fget=_get_hostcontrolareas)

    # A transmission path's service point is part of an interchange area
    PartOf = List(Instance("CIM.IEC61968.Informative.Reservation.ServicePoint"),
        desc="A transmission path's service point is part of an interchange area")

    # The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
    SideA_TieLines = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.TieLine"),
        desc="The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.")

    # A GeneratingUnit injects energy into a SubControlArea.
    GeneratingUnits = List(Instance("CIM.IEC61970.Generation.Production.GeneratingUnit"),
        desc="A GeneratingUnit injects energy into a SubControlArea.")

    # The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
    SideB_TieLines = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.TieLine"),
        desc="The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.")

    #--------------------------------------------------------------------------
    #  Begin "SubControlArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "type", "pTolerance", "netInterchange",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "EnergyArea", "ControlAreaGeneratingUnit", "TieFlow", "Flowgate", "Export_EnergyTransactions", "Import_EnergyTransactions", "HostControlArea", "PartOf", "SideA_TieLines", "GeneratingUnits", "SideB_TieLines",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.SubControlArea",
        title="SubControlArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubControlArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransmissionRightOfWay" class:
#------------------------------------------------------------------------------

class TransmissionRightOfWay(PowerSystemResource):
    """ A collection of transmission lines that are close proximity to each other.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transmission right-of-way is a member of a transmission corridor
    TransmissionCorridor = Instance("CIM.IEC61968.Informative.EnergyScheduling.TransmissionCorridor",
        desc="A transmission right-of-way is a member of a transmission corridor",
        transient=True,
        opposite="TransmissionRightOfWays",
        editor=InstanceEditor(name="_transmissioncorridors"))

    def _get_transmissioncorridors(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.TransmissionCorridor" ]
        else:
            return []

    _transmissioncorridors = Property(fget=_get_transmissioncorridors)

    # A transmission line can be part of a transmission corridor
    Lines = List(Instance("CIM.IEC61970.Wires.Line"),
        desc="A transmission line can be part of a transmission corridor")

    #--------------------------------------------------------------------------
    #  Begin "TransmissionRightOfWay" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TransmissionCorridor", "Lines",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.TransmissionRightOfWay",
        title="TransmissionRightOfWay",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransmissionRightOfWay" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergySchedulingVersion" class:
#------------------------------------------------------------------------------

class EnergySchedulingVersion(Element):
    date = Date

    # v 4 moved SubControlArea
    version = Str(desc="v 4 moved SubControlArea")

    #--------------------------------------------------------------------------
    #  Begin "EnergySchedulingVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "date", "version",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.EnergySchedulingVersion",
        title="EnergySchedulingVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergySchedulingVersion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HostControlArea" class:
#------------------------------------------------------------------------------

class HostControlArea(IdentifiedObject):
    """ A HostControlArea has a set of tie points and a set of generator controls (i.e., AGC). It also has a total load, including transmission and distribution losses.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A control area can have one or more net inadvertent interchange accounts
    InadvertentAccounts = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.InadvertentAccount"),
        desc="A control area can have one or more net inadvertent interchange accounts")

    # A control area has one or more area reserve specifications
    AreaReserveSpec = Instance("CIM.IEC61968.Informative.EnergyScheduling.AreaReserveSpec",
        desc="A control area has one or more area reserve specifications",
        transient=True,
        opposite="HostControlAreas",
        editor=InstanceEditor(name="_areareservespecs"))

    def _get_areareservespecs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.AreaReserveSpec" ]
        else:
            return []

    _areareservespecs = Property(fget=_get_areareservespecs)

    # The control area's frequency bias factor, in active power per frequency, for automatic generation control (AGC)
    frequencyBiasFactor = Instance("CIM.FreqBiasFactor",
        desc="The control area's frequency bias factor, in active power per frequency, for automatic generation control (AGC)",
        transient=True,
        editor=InstanceEditor(name="_freqbiasfactors"))

    def _get_freqbiasfactors(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.FreqBiasFactor" ]
        else:
            return []

    _freqbiasfactors = Property(fget=_get_freqbiasfactors)

    # A HostControlArea can have zero or more tie lines.
    SideA_TieLines = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.TieLine"),
        desc="A HostControlArea can have zero or more tie lines.")

    # The interchange area  may operate as a control area
    SubControlAreas = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.SubControlArea"),
        desc="The interchange area  may operate as a control area")

    # A HostControlArea can have zero or more tie lines.
    SideB_TieLines = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.TieLine"),
        desc="A HostControlArea can have zero or more tie lines.")

    # A control area can receive dynamic schedules from other control areas
    Receive_DynamicSchedules = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.DynamicSchedule"),
        desc="A control area can receive dynamic schedules from other control areas")

    # A control area can send dynamic schedules to other control areas
    Send_DynamicSchedules = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.DynamicSchedule"),
        desc="A control area can send dynamic schedules to other control areas")

    # A ControlAreaCompany controls a ControlArea.
    Controls = Instance("CIM.IEC61968.Informative.Financial.ControlAreaOperator",
        desc="A ControlAreaCompany controls a ControlArea.",
        transient=True,
        opposite="ControlledBy",
        editor=InstanceEditor(name="_controlareaoperators"))

    def _get_controlareaoperators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.ControlAreaOperator" ]
        else:
            return []

    _controlareaoperators = Property(fget=_get_controlareaoperators)

    # The area's present control mode: (CF = constant frequency) or (CTL = constant tie-line) or (TLB = tie-line bias) or (OFF = off control)
    areaControlMode = AreaControlMode(desc="The area's present control mode: (CF = constant frequency) or (CTL = constant tie-line) or (TLB = tie-line bias) or (OFF = off control)")

    # The present power system frequency set point for automatic generation control
    freqSetPoint = Frequency(desc="The present power system frequency set point for automatic generation control")

    #--------------------------------------------------------------------------
    #  Begin "HostControlArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "areaControlMode", "freqSetPoint",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "InadvertentAccounts", "AreaReserveSpec", "frequencyBiasFactor", "SideA_TieLines", "SubControlAreas", "SideB_TieLines", "Receive_DynamicSchedules", "Send_DynamicSchedules", "Controls",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.HostControlArea",
        title="HostControlArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HostControlArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "InadvertentAccount" class:
#------------------------------------------------------------------------------

class InadvertentAccount(Curve):
    """ An account for tracking inadvertent interchange versus time for each control area. A control area may have more than one inadvertent account in order to track inadvertent over one or more specific tie points in addition to the usual overall net inadvertent. Separate accounts would also be used to track designated time periods, such as on-peak and off-peak.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A control area can have one or more net inadvertent interchange accounts
    HostControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.HostControlArea",
        desc="A control area can have one or more net inadvertent interchange accounts",
        transient=True,
        opposite="InadvertentAccounts",
        editor=InstanceEditor(name="_hostcontrolareas"))

    def _get_hostcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.HostControlArea" ]
        else:
            return []

    _hostcontrolareas = Property(fget=_get_hostcontrolareas)

    #--------------------------------------------------------------------------
    #  Begin "InadvertentAccount" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "HostControlArea",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.InadvertentAccount",
        title="InadvertentAccount",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "InadvertentAccount" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransmissionCorridor" class:
#------------------------------------------------------------------------------

class TransmissionCorridor(PowerSystemResource):
    """ A corridor containing one or more rights of way
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transmission right-of-way is a member of a transmission corridor
    TransmissionRightOfWays = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.TransmissionRightOfWay"),
        desc="A transmission right-of-way is a member of a transmission corridor")

    # A TransmissionPath is contained in a TransmissionCorridor.
    ContainedIn = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionPath"),
        desc="A TransmissionPath is contained in a TransmissionCorridor.")

    #--------------------------------------------------------------------------
    #  Begin "TransmissionCorridor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TransmissionRightOfWays", "ContainedIn",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.TransmissionCorridor",
        title="TransmissionCorridor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransmissionCorridor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AreaReserveSpec" class:
#------------------------------------------------------------------------------

class AreaReserveSpec(Element):
    """ The control area's reserve specification
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A control area has one or more area reserve specifications
    HostControlAreas = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.HostControlArea"),
        desc="A control area has one or more area reserve specifications")

    # A Reserve type of energy transaction can count towards an area reserve specification.
    ReserveEnergyTransaction = Instance("CIM.IEC61968.Informative.EnergyScheduling.Reserve",
        desc="A Reserve type of energy transaction can count towards an area reserve specification.",
        transient=True,
        opposite="AreaReserveSpec",
        editor=InstanceEditor(name="_reserves"))

    def _get_reserves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.Reserve" ]
        else:
            return []

    _reserves = Property(fget=_get_reserves)

    # The Identification or name of the control area's reserve specification. A particular specification could correspond to pre-defined power system conditions, e.g., emergency situations.
    areaReserveSpecName = Str(desc="The Identification or name of the control area's reserve specification. A particular specification could correspond to pre-defined power system conditions, e.g., emergency situations.")

    # Raise active power regulating margin requirement, the amount of generation that can be picked up by control in 10 minutes
    raiseRegMarginReqt = ActivePower(desc="Raise active power regulating margin requirement, the amount of generation that can be picked up by control in 10 minutes")

    # Lower active power regulating margin requirement, the amount of generation that can be dropped by control in 10 minutes
    lowerRegMarginReqt = ActivePower(desc="Lower active power regulating margin requirement, the amount of generation that can be dropped by control in 10 minutes")

    # Primary active power reserve requirement, where primary reserve is generating capability that is fully available within 10 minutes. Primary reserve is composed of spinning reserve and quick-start reserve.
    primaryReserveReqt = ActivePower(desc="Primary active power reserve requirement, where primary reserve is generating capability that is fully available within 10 minutes. Primary reserve is composed of spinning reserve and quick-start reserve.")

    # Operating active power reserve requirement, where operating reserve is the generating capability that is fully available within 30 minutes. Operating reserve is composed of primary reserve (t less than 10 min) and secondary reserve (10 less than t less than 30 min).
    opReserveReqt = ActivePower(desc="Operating active power reserve requirement, where operating reserve is the generating capability that is fully available within 30 minutes. Operating reserve is composed of primary reserve (t less than 10 min) and secondary reserve (10 less than t less than 30 min).")

    # Spinning active power reserve requirement, spinning reserve is generating capability that is presently synchronized to the network and is fully available within 10 minutes
    spinningReserveReqt = ActivePower(desc="Spinning active power reserve requirement, spinning reserve is generating capability that is presently synchronized to the network and is fully available within 10 minutes")

    #--------------------------------------------------------------------------
    #  Begin "AreaReserveSpec" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "areaReserveSpecName", "raiseRegMarginReqt", "lowerRegMarginReqt", "primaryReserveReqt", "opReserveReqt", "spinningReserveReqt",
                label="Attributes"),
            VGroup("Parent", "HostControlAreas", "ReserveEnergyTransaction",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.AreaReserveSpec",
        title="AreaReserveSpec",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AreaReserveSpec" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyProduct" class:
#------------------------------------------------------------------------------

class EnergyProduct(Agreement):
    """ An EnergyProduct is offered commercially as a ContractOrTariff.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An EnergyProduct injects energy into a service point.
    ServicePoint = List(Instance("CIM.IEC61968.Informative.Reservation.ServicePoint"),
        desc="An EnergyProduct injects energy into a service point.")

    GenerationProvider = Instance("CIM.IEC61968.Informative.Financial.GenerationProvider",
        transient=True,
        opposite="EnergyProducts",
        editor=InstanceEditor(name="_generationproviders"))

    def _get_generationproviders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.GenerationProvider" ]
        else:
            return []

    _generationproviders = Property(fget=_get_generationproviders)

    # The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.
    EnergyTransactions = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction"),
        desc="The 'Source' for an EnergyTransaction is an EnergyProduct which is injected into a ControlArea.")

    # A Marketer may resell an EnergyProduct.
    ResoldBy_Marketers = List(Instance("CIM.IEC61968.Informative.Financial.Marketer"),
        desc="A Marketer may resell an EnergyProduct.")

    # A Marketer holds title to an EnergyProduct.
    TitleHeldBy_Marketer = Instance("CIM.IEC61968.Informative.Financial.Marketer",
        desc="A Marketer holds title to an EnergyProduct.",
        transient=True,
        opposite="HoldsTitleTo_EnergyProducts",
        editor=InstanceEditor(name="_marketers"))

    def _get_marketers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.Marketer" ]
        else:
            return []

    _marketers = Property(fget=_get_marketers)

    #--------------------------------------------------------------------------
    #  Begin "EnergyProduct" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval", "ServicePoint", "GenerationProvider", "EnergyTransactions", "ResoldBy_Marketers", "TitleHeldBy_Marketer",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.EnergyProduct",
        title="EnergyProduct",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyProduct" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TieLine" class:
#------------------------------------------------------------------------------

class TieLine(Element):
    # A HostControlArea can have zero or more tie lines.
    SideA_HostControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.HostControlArea",
        desc="A HostControlArea can have zero or more tie lines.",
        transient=True,
        opposite="SideA_TieLines",
        editor=InstanceEditor(name="_hostcontrolareas"))

    def _get_hostcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.HostControlArea" ]
        else:
            return []

    _hostcontrolareas = Property(fget=_get_hostcontrolareas)

    # A HostControlArea can have zero or more tie lines.
    SideB_HostControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.HostControlArea",
        desc="A HostControlArea can have zero or more tie lines.",
        transient=True,
        opposite="SideB_TieLines",
        editor=InstanceEditor(name="_hostcontrolareas"))

    def _get_hostcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.HostControlArea" ]
        else:
            return []

    _hostcontrolareas = Property(fget=_get_hostcontrolareas)

    # The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
    SideA_SubControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.SubControlArea",
        desc="The SubControlArea is on the A side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.",
        transient=True,
        opposite="SideA_TieLines",
        editor=InstanceEditor(name="_subcontrolareas"))

    def _get_subcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.SubControlArea" ]
        else:
            return []

    _subcontrolareas = Property(fget=_get_subcontrolareas)

    # A CustomerConsumer may ring its perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.
    CustomerConsumer = Instance("CIM.IEC61968.Informative.Financial.CustomerConsumer",
        desc="A CustomerConsumer may ring its perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.",
        transient=True,
        opposite="TieLines",
        editor=InstanceEditor(name="_customerconsumers"))

    def _get_customerconsumers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.CustomerConsumer" ]
        else:
            return []

    _customerconsumers = Property(fget=_get_customerconsumers)

    # The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.
    SideB_SubControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.SubControlArea",
        desc="The SubControlArea is on the B side of a collection of metered points which define the SubControlArea's boundary for a ControlAreaOperator or CustomerConsumer.",
        transient=True,
        opposite="SideB_TieLines",
        editor=InstanceEditor(name="_subcontrolareas"))

    def _get_subcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.SubControlArea" ]
        else:
            return []

    _subcontrolareas = Property(fget=_get_subcontrolareas)

    # A dynamic energy transaction can act as a pseudo tie line.
    DynamicEnergyTransaction = Instance("CIM.IEC61968.Informative.EnergyScheduling.Dynamic",
        desc="A dynamic energy transaction can act as a pseudo tie line.",
        transient=True,
        opposite="TieLines",
        editor=InstanceEditor(name="_dynamics"))

    def _get_dynamics(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.Dynamic" ]
        else:
            return []

    _dynamics = Property(fget=_get_dynamics)

    # A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.
    ControlAreaOperators = List(Instance("CIM.IEC61968.Informative.Financial.ControlAreaOperator"),
        desc="A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.")

    #--------------------------------------------------------------------------
    #  Begin "TieLine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent", "SideA_HostControlArea", "SideB_HostControlArea", "SideA_SubControlArea", "CustomerConsumer", "SideB_SubControlArea", "DynamicEnergyTransaction", "ControlAreaOperators",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.TieLine",
        title="TieLine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TieLine" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DynamicSchedule" class:
#------------------------------------------------------------------------------

class DynamicSchedule(RegularIntervalSchedule):
    """ A continuously variable component of a control area's active power net interchange schedule. Dynamic schedules are sent and received by control areas.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A measurement is a data source for dynamic interchange schedules
    Measurement = Instance("CIM.IEC61970.Meas.Measurement",
        desc="A measurement is a data source for dynamic interchange schedules",
        transient=True,
        opposite="DynamicSchedules",
        editor=InstanceEditor(name="_measurements"))

    def _get_measurements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.Measurement" ]
        else:
            return []

    _measurements = Property(fget=_get_measurements)

    # A control area can receive dynamic schedules from other control areas
    Receive_HostControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.HostControlArea",
        desc="A control area can receive dynamic schedules from other control areas",
        transient=True,
        opposite="Receive_DynamicSchedules",
        editor=InstanceEditor(name="_hostcontrolareas"))

    def _get_hostcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.HostControlArea" ]
        else:
            return []

    _hostcontrolareas = Property(fget=_get_hostcontrolareas)

    # A control area can send dynamic schedules to other control areas
    Send_HostControlArea = Instance("CIM.IEC61968.Informative.EnergyScheduling.HostControlArea",
        desc="A control area can send dynamic schedules to other control areas",
        transient=True,
        opposite="Send_DynamicSchedules",
        editor=InstanceEditor(name="_hostcontrolareas"))

    def _get_hostcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.HostControlArea" ]
        else:
            return []

    _hostcontrolareas = Property(fget=_get_hostcontrolareas)

    # The 'active' or 'inactive' status of the dynamic schedule
    dynSchedStatus = Str(desc="The 'active' or 'inactive' status of the dynamic schedule")

    # Dynamic schedule sign reversal required (yes/no)
    dynSchedSignRev = Bool(desc="Dynamic schedule sign reversal required (yes/no)")

    #--------------------------------------------------------------------------
    #  Begin "DynamicSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime", "dynSchedStatus", "dynSchedSignRev",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "Measurement", "Receive_HostControlArea", "Send_HostControlArea",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.DynamicSchedule",
        title="DynamicSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DynamicSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Reserve" class:
#------------------------------------------------------------------------------

class Reserve(EnergyTransaction):
    # A Reserve type of energy transaction can count towards an area reserve specification.
    AreaReserveSpec = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.AreaReserveSpec"),
        desc="A Reserve type of energy transaction can count towards an area reserve specification.")

    #--------------------------------------------------------------------------
    #  Begin "Reserve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "receiptPointP", "energyMin", "firmInterchangeFlag", "congestChargeMax", "reason", "deliveryPointP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "state", "CurtailmentProfiles", "Export_SubControlArea", "EnergyTransId", "Import_SubControlArea", "EnergyPriceCurves", "LossProfiles", "EnergyProfiles", "EnergyProduct", "AreaReserveSpec",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.Reserve",
        title="Reserve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Reserve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Block" class:
#------------------------------------------------------------------------------

class Block(EnergyTransaction):
    """ A block is a simple transaction type, with no additional relationships.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Block" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "receiptPointP", "energyMin", "firmInterchangeFlag", "congestChargeMax", "reason", "deliveryPointP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "state", "CurtailmentProfiles", "Export_SubControlArea", "EnergyTransId", "Import_SubControlArea", "EnergyPriceCurves", "LossProfiles", "EnergyProfiles", "EnergyProduct",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.Block",
        title="Block",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Block" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LossProfile" class:
#------------------------------------------------------------------------------

class LossProfile(Profile):
    """ LossProfile is associated with an EnerrgyTransaction and must be completely contained within the time frame of the EnergyProfile associated with this EnergyTransaction.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An EnergyTransaction may have a LossProfile.
    EnergyTransaction = Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction",
        desc="An EnergyTransaction may have a LossProfile.",
        transient=True,
        opposite="LossProfiles",
        editor=InstanceEditor(name="_energytransactions"))

    def _get_energytransactions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction" ]
        else:
            return []

    _energytransactions = Property(fget=_get_energytransactions)

    # Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.
    HasLoss_ = Instance("CIM.IEC61968.Informative.Financial.TransmissionProvider",
        desc="Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.",
        transient=True,
        opposite="For",
        editor=InstanceEditor(name="_transmissionproviders"))

    def _get_transmissionproviders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.TransmissionProvider" ]
        else:
            return []

    _transmissionproviders = Property(fget=_get_transmissionproviders)

    #--------------------------------------------------------------------------
    #  Begin "LossProfile" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ProfileDatas", "EnergyTransaction", "HasLoss_",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.LossProfile",
        title="LossProfile",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LossProfile" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurtailmentProfile" class:
#------------------------------------------------------------------------------

class CurtailmentProfile(Profile):
    """ Curtailing entity must be providing at least one service to the EnergyTransaction. The CurtailmentProfile must be completely contained within the EnergyProfile timeframe for this EnergyTransaction.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An EnergyTransaction may be curtailed by any of the participating entities.
    EnergyTransaction = Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction",
        desc="An EnergyTransaction may be curtailed by any of the participating entities.",
        transient=True,
        opposite="CurtailmentProfiles",
        editor=InstanceEditor(name="_energytransactions"))

    def _get_energytransactions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction" ]
        else:
            return []

    _energytransactions = Property(fget=_get_energytransactions)

    #--------------------------------------------------------------------------
    #  Begin "CurtailmentProfile" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ProfileDatas", "EnergyTransaction",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.CurtailmentProfile",
        title="CurtailmentProfile",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurtailmentProfile" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Dynamic" class:
#------------------------------------------------------------------------------

class Dynamic(EnergyTransaction):
    """ A dynamic energy transaction has more complex relationships than a simple block type. It behaves like a pseudo tie line.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A dynamic energy transaction can act as a pseudo tie line.
    TieLines = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.TieLine"),
        desc="A dynamic energy transaction can act as a pseudo tie line.")

    #--------------------------------------------------------------------------
    #  Begin "Dynamic" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "receiptPointP", "energyMin", "firmInterchangeFlag", "congestChargeMax", "reason", "deliveryPointP",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "state", "CurtailmentProfiles", "Export_SubControlArea", "EnergyTransId", "Import_SubControlArea", "EnergyPriceCurves", "LossProfiles", "EnergyProfiles", "EnergyProduct", "TieLines",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.Dynamic",
        title="Dynamic",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Dynamic" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyProfile" class:
#------------------------------------------------------------------------------

class EnergyProfile(Profile):
    """ Specifies the start time, stop time, level for an EnergyTransaction.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TransactionBid = Instance("CIM.IEC61968.Informative.MarketOperations.TransactionBid",
        transient=True,
        opposite="EnergyProfiles",
        editor=InstanceEditor(name="_transactionbids"))

    def _get_transactionbids(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.TransactionBid" ]
        else:
            return []

    _transactionbids = Property(fget=_get_transactionbids)

    # An EnergyTransaction must have at least one EnergyProfile.
    EnergyTransaction = Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction",
        desc="An EnergyTransaction must have at least one EnergyProfile.",
        transient=True,
        opposite="EnergyProfiles",
        editor=InstanceEditor(name="_energytransactions"))

    def _get_energytransactions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.EnergyTransaction" ]
        else:
            return []

    _energytransactions = Property(fget=_get_energytransactions)

    #--------------------------------------------------------------------------
    #  Begin "EnergyProfile" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ProfileDatas", "TransactionBid", "EnergyTransaction",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.EnergyScheduling.EnergyProfile",
        title="EnergyProfile",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyProfile" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
