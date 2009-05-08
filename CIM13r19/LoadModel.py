#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM13r19.Core import IdentifiedObject
from CIM13r19 import Element
from CIM13r19.Wires import EnergyConsumer
from CIM13r19.Core import PowerSystemResource
from CIM13r19.Core import RegularIntervalSchedule



from enthought.traits.api import Instance, List, Property, Enum, Float, Bool, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


SeasonName = Enum("summer", "fall", "winter", "spring")

#------------------------------------------------------------------------------
#  "LoadResponseCharacteristic" class:
#------------------------------------------------------------------------------

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    EnergyConsumer = List(Instance("CIM13r19.Wires.EnergyConsumer"))

    # Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantPower = Float(desc="Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.")

    # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.
    pVoltageExponent = Float(desc="Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.")

    # Exponent of per unit frequency effecting active power
    pFrequencyExponent = Float(desc="Exponent of per unit frequency effecting active power")

    # Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantImpedance = Float(desc="Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.")

    # Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantPower = Float(desc="Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.")

    # Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantImpedance = Float(desc="Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.")

    # Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
    qConstantCurrent = Float(desc="Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.")

    # Exponent of per unit frequency effecting reactive power
    qFrequencyExponent = Float(desc="Exponent of per unit frequency effecting reactive power")

    # Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.
    exponentModel = Bool(desc="Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.")

    # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.
    qVoltageExponent = Float(desc="Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.")

    # Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
    pConstantCurrent = Float(desc="Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.")

    #--------------------------------------------------------------------------
    #  Begin "LoadResponseCharacteristic" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "qConstantPower", "pVoltageExponent", "pFrequencyExponent", "qConstantImpedance", "pConstantPower", "pConstantImpedance", "qConstantCurrent", "qFrequencyExponent", "exponentModel", "qVoltageExponent", "pConstantCurrent",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "EnergyConsumer",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.LoadResponseCharacteristic",
        title="LoadResponseCharacteristic",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadResponseCharacteristic" user definitions:
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

    # Load demand models can be based on seasons
    SeasonDayTypeSchedules = List(Instance("CIM13r19.LoadModel.SeasonDayTypeSchedule"),
        desc="Load demand models can be based on seasons")

    # Date season ends
    endDate = Str(desc="Date season ends")

    # Name of the Season
    name = SeasonName(desc="Name of the Season")

    # Date season starts
    startDate = Str(desc="Date season starts")

    #--------------------------------------------------------------------------
    #  Begin "Season" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("endDate", "name", "startDate",
                label="Attributes"),
            VGroup("Parent", "SeasonDayTypeSchedules",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.Season",
        title="Season",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Season" user definitions:
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

    # Consumers may be assigned to a load area.
    LoadGroup = Instance("CIM13r19.LoadModel.ConformLoadGroup",
        desc="Consumers may be assigned to a load area.",
        transient=True,
        opposite="EnergyConsumers",
        editor=InstanceEditor(name="_conformloadgroups"))

    def _get_conformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.ConformLoadGroup" ]
        else:
            return []

    _conformloadgroups = Property(fget=_get_conformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "customerCount", "qfixed", "pfixed", "qfixedPct", "pfixedPct",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "PowerCutZone", "LoadResponse", "LoadGroup",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.LoadModel.ConformLoad",
        title="ConformLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoad" user definitions:
    #--------------------------------------------------------------------------

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
    EnergyConsumers = List(Instance("CIM13r19.Wires.EnergyConsumer"),
        desc="An energy consumer is assigned to a power cut zone")

    # First level (amount) of load to cut as a percentage of total zone load
    cutLevel1 = Float(desc="First level (amount) of load to cut as a percentage of total zone load")

    # Second level (amount) of load to cut as a percentage of total zone load
    cutLevel2 = Float(desc="Second level (amount) of load to cut as a percentage of total zone load")

    #--------------------------------------------------------------------------
    #  Begin "PowerCutZone" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "cutLevel1", "cutLevel2",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "EnergyConsumers",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.PowerCutZone",
        title="PowerCutZone",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerCutZone" user definitions:
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "customerCount", "qfixed", "pfixed", "qfixedPct", "pfixedPct",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "PowerCutZone", "LoadResponse",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.LoadModel.StationSupply",
        title="StationSupply",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StationSupply" user definitions:
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

    # Load demand models can be based on day type
    SeasonDayTypeSchedules = List(Instance("CIM13r19.LoadModel.SeasonDayTypeSchedule"),
        desc="Load demand models can be based on day type")

    #--------------------------------------------------------------------------
    #  Begin "DayType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "SeasonDayTypeSchedules",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.DayType",
        title="DayType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DayType" user definitions:
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

    SubLoadArea = Instance("CIM13r19.LoadModel.SubLoadArea",
        transient=True,
        opposite="LoadGroups",
        editor=InstanceEditor(name="_subloadareas"))

    def _get_subloadareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.SubLoadArea" ]
        else:
            return []

    _subloadareas = Property(fget=_get_subloadareas)

    #--------------------------------------------------------------------------
    #  Begin "LoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "SubLoadArea",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.LoadGroup",
        title="LoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadGroup" user definitions:
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

    ControlArea = Instance("CIM13r19.ControlArea.ControlArea",
        transient=True,
        opposite="EnergyArea",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    #--------------------------------------------------------------------------
    #  Begin "EnergyArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.EnergyArea",
        title="EnergyArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyArea" user definitions:
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

    # Load demand models can be based on day type
    DayType = Instance("CIM13r19.LoadModel.DayType",
        desc="Load demand models can be based on day type",
        transient=True,
        opposite="SeasonDayTypeSchedules",
        editor=InstanceEditor(name="_daytypes"))

    def _get_daytypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.DayType" ]
        else:
            return []

    _daytypes = Property(fget=_get_daytypes)

    # Load demand models can be based on seasons
    Season = Instance("CIM13r19.LoadModel.Season",
        desc="Load demand models can be based on seasons",
        transient=True,
        opposite="SeasonDayTypeSchedules",
        editor=InstanceEditor(name="_seasons"))

    def _get_seasons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.Season" ]
        else:
            return []

    _seasons = Property(fget=_get_seasons)

    #--------------------------------------------------------------------------
    #  Begin "SeasonDayTypeSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "DayType", "Season",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.SeasonDayTypeSchedule",
        title="SeasonDayTypeSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeasonDayTypeSchedule" user definitions:
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

    LoadGroup = Instance("CIM13r19.LoadModel.NonConformLoadGroup",
        transient=True,
        opposite="EnergyConsumers",
        editor=InstanceEditor(name="_nonconformloadgroups"))

    def _get_nonconformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.NonConformLoadGroup" ]
        else:
            return []

    _nonconformloadgroups = Property(fget=_get_nonconformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "customerCount", "qfixed", "pfixed", "qfixedPct", "pfixedPct",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "PowerCutZone", "LoadResponse", "LoadGroup",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.LoadModel.NonConformLoad",
        title="NonConformLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoad" user definitions:
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

    # The SubLoadAreas in the LoadArea.
    LoadArea = Instance("CIM13r19.LoadModel.LoadArea",
        desc="The SubLoadAreas in the LoadArea.",
        transient=True,
        opposite="SubLoadAreas",
        editor=InstanceEditor(name="_loadareas"))

    def _get_loadareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.LoadArea" ]
        else:
            return []

    _loadareas = Property(fget=_get_loadareas)

    LoadGroups = List(Instance("CIM13r19.LoadModel.LoadGroup"))

    #--------------------------------------------------------------------------
    #  Begin "SubLoadArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ControlArea", "LoadArea", "LoadGroups",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.SubLoadArea",
        title="SubLoadArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubLoadArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Load" class:
#------------------------------------------------------------------------------

class Load(ConformLoad):
    """ A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The feeder's contribution to load management.
    feederLoadMgtFactor = Float(desc="The feeder's contribution to load management.")

    # The rated individual phase current.
    phaseRatedCurrent = Float(desc="The rated individual phase current.")

    # The amount of nominal feeder active power that is picked up cold.
    coldPickUpFactorP = Float(desc="The amount of nominal feeder active power that is picked up cold.")

    # The amount of nominal feeder reactive power that is picked up cold.
    coldPickUpFactorQ = Float(desc="The amount of nominal feeder reactive power that is picked up cold.")

    # Permit assignment of loads on a participation factor basis. Given three equivalent loads with factors of 10, 25 and 15, a feeder load of 100 amps could be allocated on the feeder as 20, 50 and 30 amps.
    loadAllocationFactor = Float(desc="Permit assignment of loads on a participation factor basis. Given three equivalent loads with factors of 10, 25 and 15, a feeder load of 100 amps could be allocated on the feeder as 20, 50 and 30 amps.")

    #--------------------------------------------------------------------------
    #  Begin "Load" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "customerCount", "qfixed", "pfixed", "qfixedPct", "pfixedPct", "feederLoadMgtFactor", "phaseRatedCurrent", "coldPickUpFactorP", "coldPickUpFactorQ", "loadAllocationFactor",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "PowerCutZone", "LoadResponse", "LoadGroup",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.LoadModel.Load",
        title="Load",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Load" user definitions:
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

    # Consumers may be assigned to a load area.
    EnergyConsumers = List(Instance("CIM13r19.LoadModel.ConformLoad"),
        desc="Consumers may be assigned to a load area.")

    ConformLoadSchedules = List(Instance("CIM13r19.LoadModel.ConformLoadSchedule"))

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "SubLoadArea", "EnergyConsumers", "ConformLoadSchedules",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.ConformLoadGroup",
        title="ConformLoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoadGroup" user definitions:
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
    SubLoadAreas = List(Instance("CIM13r19.LoadModel.SubLoadArea"),
        desc="The SubLoadAreas in the LoadArea.")

    #--------------------------------------------------------------------------
    #  Begin "LoadArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ControlArea", "SubLoadAreas",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.LoadArea",
        title="LoadArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadArea" user definitions:
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

    ConformLoadGroup = Instance("CIM13r19.LoadModel.ConformLoadGroup",
        transient=True,
        opposite="ConformLoadSchedules",
        editor=InstanceEditor(name="_conformloadgroups"))

    def _get_conformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.ConformLoadGroup" ]
        else:
            return []

    _conformloadgroups = Property(fget=_get_conformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "DayType", "Season", "ConformLoadGroup",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.ConformLoadSchedule",
        title="ConformLoadSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConformLoadSchedule" user definitions:
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

    NonConformLoadGroup = Instance("CIM13r19.LoadModel.NonConformLoadGroup",
        transient=True,
        opposite="NonConformLoadSchedules",
        editor=InstanceEditor(name="_nonconformloadgroups"))

    def _get_nonconformloadgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.NonConformLoadGroup" ]
        else:
            return []

    _nonconformloadgroups = Property(fget=_get_nonconformloadgroups)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "DayType", "Season", "NonConformLoadGroup",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.NonConformLoadSchedule",
        title="NonConformLoadSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoadSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CustomerLoad" class:
#------------------------------------------------------------------------------

class CustomerLoad(ConformLoad):
    """ A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "CustomerLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "customerCount", "qfixed", "pfixed", "qfixedPct", "pfixedPct",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "PowerCutZone", "LoadResponse", "LoadGroup",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.LoadModel.CustomerLoad",
        title="CustomerLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CustomerLoad" user definitions:
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

    NonConformLoadSchedules = List(Instance("CIM13r19.LoadModel.NonConformLoadSchedule"))

    EnergyConsumers = List(Instance("CIM13r19.LoadModel.NonConformLoad"))

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "SubLoadArea", "NonConformLoadSchedules", "EnergyConsumers",
                label="References"),
            dock="tab"),
        id="CIM13r19.LoadModel.NonConformLoadGroup",
        title="NonConformLoadGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonConformLoadGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "InductionMotorLoad" class:
#------------------------------------------------------------------------------

class InductionMotorLoad(NonConformLoad):
    """ Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "InductionMotorLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "customerCount", "qfixed", "pfixed", "qfixedPct", "pfixedPct",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "PowerCutZone", "LoadResponse", "LoadGroup",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.LoadModel.InductionMotorLoad",
        title="InductionMotorLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "InductionMotorLoad" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
