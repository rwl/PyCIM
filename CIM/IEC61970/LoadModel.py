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

""" This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import PowerSystemResource
from CIM.IEC61970.Core import RegularIntervalSchedule
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.Wires import EnergyConsumer
from CIM import Element
from CIM.IEC61970.Domain import PerCent



from enthought.traits.api import Instance, List, Property, Enum, Date, Float, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Name of season
SeasonName = Enum("spring", "fall", "winter", "summer", desc="Name of season")

#------------------------------------------------------------------------------
#  "PowerCutZone" class:
#------------------------------------------------------------------------------

class PowerCutZone(PowerSystemResource):
    """ An area or zone of the power system which is used for load shedding purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An energy consumer is assigned to a power cut zone
    EnergyConsumers = List(Instance("CIM.IEC61970.Wires.EnergyConsumer"),
        desc="An energy consumer is assigned to a power cut zone")

    # First level (amount) of load to cut as a percentage of total zone load
    cutLevel1 = PerCent(desc="First level (amount) of load to cut as a percentage of total zone load")

    # Second level (amount) of load to cut as a percentage of total zone load
    cutLevel2 = PerCent(desc="Second level (amount) of load to cut as a percentage of total zone load")

    #--------------------------------------------------------------------------
    #  Begin "PowerCutZone" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "cutLevel1", "cutLevel2",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "EnergyConsumers",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.PowerCutZone",
        title="PowerCutZone",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerCutZone" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeasonDayTypeSchedule" class:
#------------------------------------------------------------------------------

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """ The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # DayType for the Schedule.
    DayType = Instance("CIM.IEC61970.LoadModel.DayType",
        desc="DayType for the Schedule.",
        transient=True,
        opposite="SeasonDayTypeSchedules",
        editor=InstanceEditor(name="_daytypes"))

    def _get_daytypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.DayType" ]
        else:
            return []

    _daytypes = Property(fget=_get_daytypes)

    # Season for the Schedule.
    Season = Instance("CIM.IEC61970.LoadModel.Season",
        desc="Season for the Schedule.",
        transient=True,
        opposite="SeasonDayTypeSchedules",
        editor=InstanceEditor(name="_seasons"))

    def _get_seasons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.Season" ]
        else:
            return []

    _seasons = Property(fget=_get_seasons)

    #--------------------------------------------------------------------------
    #  Begin "SeasonDayTypeSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "DayType", "Season",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.SeasonDayTypeSchedule",
        title="SeasonDayTypeSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeasonDayTypeSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DayType" class:
#------------------------------------------------------------------------------

class DayType(IdentifiedObject):
    """ Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Schedules that use this DayType.
    SeasonDayTypeSchedules = List(Instance("CIM.IEC61970.LoadModel.SeasonDayTypeSchedule"),
        desc="Schedules that use this DayType.")

    #--------------------------------------------------------------------------
    #  Begin "DayType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "SeasonDayTypeSchedules",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.DayType",
        title="DayType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DayType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyArea" class:
#------------------------------------------------------------------------------

class EnergyArea(IdentifiedObject):
    """ The class describes an area having energy production or consumption. The class is the basis for further specialization.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The control area specification that is used for the load forecast.
    ControlArea = Instance("CIM.IEC61970.ControlArea.ControlArea",
        desc="The control area specification that is used for the load forecast.",
        transient=True,
        opposite="EnergyArea",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    #--------------------------------------------------------------------------
    #  Begin "EnergyArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.EnergyArea",
        title="EnergyArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StationSupply" class:
#------------------------------------------------------------------------------

class StationSupply(EnergyConsumer):
    """ Station supply with load derived from the station output.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "StationSupply" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "qfixedPct", "pfixed", "customerCount", "qfixed", "pfixedPct",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "PowerCutZone", "ServiceDeliveryPoints", "LoadResponse",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.StationSupply",
        title="StationSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StationSupply" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoad" class:
#------------------------------------------------------------------------------

class NonConformLoad(EnergyConsumer):
    """ NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Group of this ConformLoad.
    LoadGroup = Instance("CIM.IEC61970.LoadModel.NonConformLoadGroup",
        desc="Group of this ConformLoad.",
        transient=True,
        opposite="EnergyConsumers",
        editor=InstanceEditor(name="_nonconformloadgroups"))

    def _get_nonconformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.NonConformLoadGroup" ]
        else:
            return []

    _nonconformloadgroups = Property(fget=_get_nonconformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "qfixedPct", "pfixed", "customerCount", "qfixed", "pfixedPct",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "PowerCutZone", "ServiceDeliveryPoints", "LoadResponse", "LoadGroup",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.NonConformLoad",
        title="NonConformLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoad" class:
#------------------------------------------------------------------------------

class ConformLoad(EnergyConsumer):
    """ ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Group of this ConformLoad.
    LoadGroup = Instance("CIM.IEC61970.LoadModel.ConformLoadGroup",
        desc="Group of this ConformLoad.",
        transient=True,
        opposite="EnergyConsumers",
        editor=InstanceEditor(name="_conformloadgroups"))

    def _get_conformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.ConformLoadGroup" ]
        else:
            return []

    _conformloadgroups = Property(fget=_get_conformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "qfixedPct", "pfixed", "customerCount", "qfixed", "pfixedPct",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "PowerCutZone", "ServiceDeliveryPoints", "LoadResponse", "LoadGroup",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.ConformLoad",
        title="ConformLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Season" class:
#------------------------------------------------------------------------------

class Season(Element):
    """ A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Capacity Benefit Margin may differ based on the season
    CapacityBenefitMargin = List(Instance("CIM.IEC61968.Informative.MarketOperations.CapacityBenefitMargin"),
        desc="Capacity Benefit Margin may differ based on the season")

    # Limits may differ based on the season
    ViolationLimits = List(Instance("CIM.IEC61968.Informative.MarketOperations.ViolationLimit"),
        desc="Limits may differ based on the season")

    # Schedules that use this Season.
    SeasonDayTypeSchedules = List(Instance("CIM.IEC61970.LoadModel.SeasonDayTypeSchedule"),
        desc="Schedules that use this Season.")

    # Name of the Season
    name = SeasonName(desc="Name of the Season")

    # Date season starts
    startDate = Date(desc="Date season starts")

    # Date season ends
    endDate = Date(desc="Date season ends")

    #--------------------------------------------------------------------------
    #  Begin "Season" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "name", "startDate", "endDate",
                label="Attributes"),
            VGroup("Parent", "CapacityBenefitMargin", "ViolationLimits", "SeasonDayTypeSchedules",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.Season",
        title="Season",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Season" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadGroup" class:
#------------------------------------------------------------------------------

class LoadGroup(IdentifiedObject):
    """ The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RegisteredLoads = List(Instance("CIM.IEC61968.Informative.MarketOperations.RegisteredLoad"))

    # The SubLoadArea where the Loadgroup belongs.
    SubLoadArea = Instance("CIM.IEC61970.LoadModel.SubLoadArea",
        desc="The SubLoadArea where the Loadgroup belongs.",
        transient=True,
        opposite="LoadGroups",
        editor=InstanceEditor(name="_subloadareas"))

    def _get_subloadareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.SubLoadArea" ]
        else:
            return []

    _subloadareas = Property(fget=_get_subloadareas)

    #--------------------------------------------------------------------------
    #  Begin "LoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "RegisteredLoads", "SubLoadArea",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.LoadGroup",
        title="LoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadResponseCharacteristic" class:
#------------------------------------------------------------------------------

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The set of loads that have the response characteristics.
    EnergyConsumer = List(Instance("CIM.IEC61970.Wires.EnergyConsumer"),
        desc="The set of loads that have the response characteristics.")

    # Exponent of per unit frequency effecting active power
    pFrequencyExponent = Float(desc="Exponent of per unit frequency effecting active power")

    # Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantCurrent = Float(desc="Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.")

    # Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantPower = Float(desc="Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.")

    # Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantCurrent = Float(desc="Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.")

    # Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantImpedance = Float(desc="Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.")

    # Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.
    exponentModel = Bool(desc="Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.")

    # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.
    qVoltageExponent = Float(desc="Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.")

    # Exponent of per unit frequency effecting reactive power
    qFrequencyExponent = Float(desc="Exponent of per unit frequency effecting reactive power")

    # Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantImpedance = Float(desc="Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.")

    # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.
    pVoltageExponent = Float(desc="Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.")

    # Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantPower = Float(desc="Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.")

    #--------------------------------------------------------------------------
    #  Begin "LoadResponseCharacteristic" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "pFrequencyExponent", "pConstantCurrent", "qConstantPower", "qConstantCurrent", "pConstantImpedance", "exponentModel", "qVoltageExponent", "qFrequencyExponent", "qConstantImpedance", "pVoltageExponent", "pConstantPower",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "EnergyConsumer",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.LoadResponseCharacteristic",
        title="LoadResponseCharacteristic",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadResponseCharacteristic" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubLoadArea" class:
#------------------------------------------------------------------------------

class SubLoadArea(EnergyArea):
    """ The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The LoadArea where the SubLoadArea belongs.
    LoadArea = Instance("CIM.IEC61970.LoadModel.LoadArea",
        desc="The LoadArea where the SubLoadArea belongs.",
        transient=True,
        opposite="SubLoadAreas",
        editor=InstanceEditor(name="_loadareas"))

    def _get_loadareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.LoadArea" ]
        else:
            return []

    _loadareas = Property(fget=_get_loadareas)

    # The Loadgroups in the SubLoadArea.
    LoadGroups = List(Instance("CIM.IEC61970.LoadModel.LoadGroup"),
        desc="The Loadgroups in the SubLoadArea.")

    #--------------------------------------------------------------------------
    #  Begin "SubLoadArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ControlArea", "LoadArea", "LoadGroups",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.SubLoadArea",
        title="SubLoadArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubLoadArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoadSchedule" class:
#------------------------------------------------------------------------------

class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """ An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The NonConformLoadGroup where the NonConformLoadSchedule belongs.
    NonConformLoadGroup = Instance("CIM.IEC61970.LoadModel.NonConformLoadGroup",
        desc="The NonConformLoadGroup where the NonConformLoadSchedule belongs.",
        transient=True,
        opposite="NonConformLoadSchedules",
        editor=InstanceEditor(name="_nonconformloadgroups"))

    def _get_nonconformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.NonConformLoadGroup" ]
        else:
            return []

    _nonconformloadgroups = Property(fget=_get_nonconformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "DayType", "Season", "NonConformLoadGroup",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.NonConformLoadSchedule",
        title="NonConformLoadSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoadSchedule" class:
#------------------------------------------------------------------------------

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """ A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The ConformLoadGroup where the ConformLoadSchedule belongs.
    ConformLoadGroup = Instance("CIM.IEC61970.LoadModel.ConformLoadGroup",
        desc="The ConformLoadGroup where the ConformLoadSchedule belongs.",
        transient=True,
        opposite="ConformLoadSchedules",
        editor=InstanceEditor(name="_conformloadgroups"))

    def _get_conformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.LoadModel.ConformLoadGroup" ]
        else:
            return []

    _conformloadgroups = Property(fget=_get_conformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "DayType", "Season", "ConformLoadGroup",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.ConformLoadSchedule",
        title="ConformLoadSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonConformLoadGroup" class:
#------------------------------------------------------------------------------

class NonConformLoadGroup(LoadGroup):
    """ Loads that do not follow a daily and seasonal load variation pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Conform loads assigned to this ConformLoadGroup.
    EnergyConsumers = List(Instance("CIM.IEC61970.LoadModel.NonConformLoad"),
        desc="Conform loads assigned to this ConformLoadGroup.")

    # The NonConformLoadSchedules in the NonConformLoadGroup.
    NonConformLoadSchedules = List(Instance("CIM.IEC61970.LoadModel.NonConformLoadSchedule"),
        desc="The NonConformLoadSchedules in the NonConformLoadGroup.")

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "RegisteredLoads", "SubLoadArea", "EnergyConsumers", "NonConformLoadSchedules",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.NonConformLoadGroup",
        title="NonConformLoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadArea" class:
#------------------------------------------------------------------------------

class LoadArea(EnergyArea):
    """ The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The SubLoadAreas in the LoadArea.
    SubLoadAreas = List(Instance("CIM.IEC61970.LoadModel.SubLoadArea"),
        desc="The SubLoadAreas in the LoadArea.")

    #--------------------------------------------------------------------------
    #  Begin "LoadArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ControlArea", "SubLoadAreas",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.LoadArea",
        title="LoadArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConformLoadGroup" class:
#------------------------------------------------------------------------------

class ConformLoadGroup(LoadGroup):
    """ Load that follows a daily and seasonal load variation pattern.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The ConformLoadSchedules in the ConformLoadGroup.
    ConformLoadSchedules = List(Instance("CIM.IEC61970.LoadModel.ConformLoadSchedule"),
        desc="The ConformLoadSchedules in the ConformLoadGroup.")

    # Conform loads assigned to this ConformLoadGroup.
    EnergyConsumers = List(Instance("CIM.IEC61970.LoadModel.ConformLoad"),
        desc="Conform loads assigned to this ConformLoadGroup.")

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "RegisteredLoads", "SubLoadArea", "ConformLoadSchedules", "EnergyConsumers",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.LoadModel.ConformLoadGroup",
        title="ConformLoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
