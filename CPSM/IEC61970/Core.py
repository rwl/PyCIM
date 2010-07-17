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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CPSM import Element
from CPSM.IEC61970.Domain import Voltage
from CPSM.IEC61970.Domain import Seconds
from CPSM.IEC61970.Domain import UnitSymbol



from enthought.traits.api import Instance, List, Property, Enum, Str, Date, Float, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


CurveStyle = Enum("rampYValue", "formula", "constantYValue", "straightLineYValues")

#------------------------------------------------------------------------------
#  "IdentifiedObject" class:
#------------------------------------------------------------------------------

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributesThis is a root class to provide common naming attributes for all classes needing naming attributes
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.
    pathName = Str(desc="The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.The pathname is a system unique name composed from all IdentifiedObject.localNames in a naming hierarchy path from the object to the root.")

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = Str(desc="The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.")

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
    aliasName = Str(desc="The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.")

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
    name = Str(desc="The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "IdentifiedObject" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.IdentifiedObject",
        title="IdentifiedObject",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IdentifiedObject" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegularTimePoint" class:
#------------------------------------------------------------------------------

class RegularTimePoint(Element):
    """ TimePoints for a schedule where the time between the points is constant.TimePoints for a schedule where the time between the points is constant.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A RegularTimePoint belongs to a RegularIntervalSchedule.A RegularTimePoint belongs to a RegularIntervalSchedule.
    IntervalSchedule = Instance("CPSM.IEC61970.Core.RegularIntervalSchedule", allow_none=False,
        desc="A RegularTimePoint belongs to a RegularIntervalSchedule.A RegularTimePoint belongs to a RegularIntervalSchedule.",
        transient=True,
        opposite="TimePoints",
        editor=InstanceEditor(name="_regularintervalschedules"))

    def _get_regularintervalschedules(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.RegularIntervalSchedule" ]
        else:
            return []

    _regularintervalschedules = Property(fget=_get_regularintervalschedules)

    # The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value1 = Float(desc="The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.The first value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.")

    # The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.
    sequenceNumber = Int(desc="The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.The position of the RegularTimePoint in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the RegularIntervalSchedule.timeStep with the RegularTimePoint.sequenceNumber and add the BasicIntervalSchedule.startTime.")

    # The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.
    value2 = Float(desc="The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.The second value at the time. The meaning of the value is defined by the class inhering the RegularIntervalSchedule.")

    #--------------------------------------------------------------------------
    #  Begin "RegularTimePoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "value1", "sequenceNumber", "value2",
                label="Attributes"),
            VGroup("Model", "IntervalSchedule",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.RegularTimePoint",
        title="RegularTimePoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegularTimePoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurveData" class:
#------------------------------------------------------------------------------

class CurveData(Element):
    """ Data point values for defining a curve or scheduleData point values for defining a curve or schedule
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Curve defined by this CurveData.The Curve defined by this CurveData.
    CurveSchedule = Instance("CPSM.IEC61970.Core.Curve", allow_none=False,
        desc="The Curve defined by this CurveData.The Curve defined by this CurveData.",
        transient=True,
        opposite="CurveScheduleDatas",
        editor=InstanceEditor(name="_curves"))

    def _get_curves(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.Curve" ]
        else:
            return []

    _curves = Property(fget=_get_curves)

    # The data value of the second Y-axis variable (if present), depending on the Y-axis unitsThe data value of the second Y-axis variable (if present), depending on the Y-axis units
    y2value = Float(desc="The data value of the second Y-axis variable (if present), depending on the Y-axis unitsThe data value of the second Y-axis variable (if present), depending on the Y-axis units")

    # The data value of the X-axis variable,  depending on the X-axis unitsThe data value of the X-axis variable,  depending on the X-axis units
    xvalue = Float(desc="The data value of the X-axis variable,  depending on the X-axis unitsThe data value of the X-axis variable,  depending on the X-axis units")

    # The data value of the  first Y-axis variable, depending on the Y-axis unitsThe data value of the  first Y-axis variable, depending on the Y-axis units
    y1value = Float(desc="The data value of the  first Y-axis variable, depending on the Y-axis unitsThe data value of the  first Y-axis variable, depending on the Y-axis units")

    #--------------------------------------------------------------------------
    #  Begin "CurveData" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "y2value", "xvalue", "y1value",
                label="Attributes"),
            VGroup("Model", "CurveSchedule",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.CurveData",
        title="CurveData",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurveData" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Terminal" class:
#------------------------------------------------------------------------------

class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
    Measurements = List(Instance("CPSM.IEC61970.Meas.Measurement"),
        desc="One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.")

    # The terminal is regulated by a control.The terminal is regulated by a control.
    RegulatingControl = List(Instance("CPSM.IEC61970.Wires.RegulatingControl"),
        desc="The terminal is regulated by a control.The terminal is regulated by a control.")

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    ConnectivityNode = Instance("CPSM.IEC61970.Topology.ConnectivityNode",
        desc="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.",
        transient=True,
        opposite="Terminals",
        editor=InstanceEditor(name="_connectivitynodes"))

    def _get_connectivitynodes(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Topology.ConnectivityNode" ]
        else:
            return []

    _connectivitynodes = Property(fget=_get_connectivitynodes)

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    ConductingEquipment = Instance("CPSM.IEC61970.Core.ConductingEquipment", allow_none=False,
        desc="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes",
        transient=True,
        opposite="Terminals",
        editor=InstanceEditor(name="_conductingequipments"))

    def _get_conductingequipments(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.ConductingEquipment" ]
        else:
            return []

    _conductingequipments = Property(fget=_get_conductingequipments)

    #--------------------------------------------------------------------------
    #  Begin "Terminal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Measurements", "RegulatingControl", "ConnectivityNode", "ConductingEquipment",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.Terminal",
        title="Terminal",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Terminal" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BaseVoltage" class:
#------------------------------------------------------------------------------

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.
    ConductingEquipment = List(Instance("CPSM.IEC61970.Core.ConductingEquipment"),
        desc="Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.")

    # The VoltageLevels having this BaseVoltage.The VoltageLevels having this BaseVoltage.
    VoltageLevel = List(Instance("CPSM.IEC61970.Core.VoltageLevel"),
        desc="The VoltageLevels having this BaseVoltage.The VoltageLevels having this BaseVoltage.")

    # The PowerSystemResource's base voltage.The PowerSystemResource's base voltage.
    nominalVoltage = Voltage(desc="The PowerSystemResource's base voltage.The PowerSystemResource's base voltage.")

    #--------------------------------------------------------------------------
    #  Begin "BaseVoltage" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "nominalVoltage",
                label="Attributes"),
            VGroup("Model", "ConductingEquipment", "VoltageLevel",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.BaseVoltage",
        title="BaseVoltage",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BaseVoltage" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Unit" class:
#------------------------------------------------------------------------------

class Unit(IdentifiedObject):
    """ Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Measurements having the UnitThe Measurements having the Unit
    Measurements = List(Instance("CPSM.IEC61970.Meas.Measurement"),
        desc="The Measurements having the UnitThe Measurements having the Unit")

    #--------------------------------------------------------------------------
    #  Begin "Unit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Measurements",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.Unit",
        title="Unit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Unit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubGeographicalRegion" class:
#------------------------------------------------------------------------------

class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.A subset of a geographical region of a power system network model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Region = Instance("CPSM.IEC61970.Core.GeographicalRegion", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Regions",
        editor=InstanceEditor(name="_geographicalregions"))

    def _get_geographicalregions(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.GeographicalRegion" ]
        else:
            return []

    _geographicalregions = Property(fget=_get_geographicalregions)

    # A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.
    Lines = List(Instance("CPSM.IEC61970.Wires.Line"),
        desc="A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.")

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Substations = List(Instance("CPSM.IEC61970.Core.Substation"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "SubGeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Region", "Lines", "Substations",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.SubGeographicalRegion",
        title="SubGeographicalRegion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubGeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Curve" class:
#------------------------------------------------------------------------------

class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curveThe point data values that define a curve
    CurveScheduleDatas = List(Instance("CPSM.IEC61970.Core.CurveData"),
        desc="The point data values that define a curveThe point data values that define a curve")

    # The Y2-axis units of measure.The Y2-axis units of measure.
    y2Unit = UnitSymbol(desc="The Y2-axis units of measure.The Y2-axis units of measure.")

    # The X-axis units of measure.The X-axis units of measure.
    xUnit = UnitSymbol(desc="The X-axis units of measure.The X-axis units of measure.")

    # The style or shape of the curve.The style or shape of the curve.
    curveStyle = CurveStyle(desc="The style or shape of the curve.The style or shape of the curve.")

    # The Y1-axis units of measure.The Y1-axis units of measure.
    y1Unit = UnitSymbol(desc="The Y1-axis units of measure.The Y1-axis units of measure.")

    #--------------------------------------------------------------------------
    #  Begin "Curve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "y2Unit", "xUnit", "curveStyle", "y1Unit",
                label="Attributes"),
            VGroup("Model", "CurveScheduleDatas",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.Curve",
        title="Curve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Curve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PowerSystemResource" class:
#------------------------------------------------------------------------------

class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Measurements that are included in the naming hierarchy where the PSR is the containing objectThe Measurements that are included in the naming hierarchy where the PSR is the containing object
    Contains_Measurements = List(Instance("CPSM.IEC61970.Meas.Measurement"),
        desc="The Measurements that are included in the naming hierarchy where the PSR is the containing objectThe Measurements that are included in the naming hierarchy where the PSR is the containing object")

    #--------------------------------------------------------------------------
    #  Begin "PowerSystemResource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.PowerSystemResource",
        title="PowerSystemResource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerSystemResource" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BasicIntervalSchedule" class:
#------------------------------------------------------------------------------

class BasicIntervalSchedule(IdentifiedObject):
    """ Schedule of values at points in time.Schedule of values at points in time.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The time for the first time point.The time for the first time point.
    startTime = Date(desc="The time for the first time point.The time for the first time point.")

    # Value1 units of measure.Value1 units of measure.
    value1Unit = UnitSymbol(desc="Value1 units of measure.Value1 units of measure.")

    # Value2 units of measure.Value2 units of measure.
    value2Unit = UnitSymbol(desc="Value2 units of measure.Value2 units of measure.")

    #--------------------------------------------------------------------------
    #  Begin "BasicIntervalSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "startTime", "value1Unit", "value2Unit",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.BasicIntervalSchedule",
        title="BasicIntervalSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BasicIntervalSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeographicalRegion" class:
#------------------------------------------------------------------------------

class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.A geographical region of a power system network model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Regions = List(Instance("CPSM.IEC61970.Core.SubGeographicalRegion"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "GeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Regions",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.GeographicalRegion",
        title="GeographicalRegion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegularIntervalSchedule" class:
#------------------------------------------------------------------------------

class RegularIntervalSchedule(BasicIntervalSchedule):
    """ The schedule has TimePoints where the time between them is constant.The schedule has TimePoints where the time between them is constant.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curveThe point data values that define a curve
    TimePoints = List(Instance("CPSM.IEC61970.Core.RegularTimePoint"),
        desc="The point data values that define a curveThe point data values that define a curve")

    # The time for the last time point.The time for the last time point.
    endTime = Date(desc="The time for the last time point.The time for the last time point.")

    # The time between each pair of subsequent RegularTimePoints.The time between each pair of subsequent RegularTimePoints.
    timeStep = Seconds(desc="The time between each pair of subsequent RegularTimePoints.The time between each pair of subsequent RegularTimePoints.")

    #--------------------------------------------------------------------------
    #  Begin "RegularIntervalSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "startTime", "value1Unit", "value2Unit", "endTime", "timeStep",
                label="Attributes"),
            VGroup("Model", "TimePoints",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.RegularIntervalSchedule",
        title="RegularIntervalSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegularIntervalSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConnectivityNodeContainer" class:
#------------------------------------------------------------------------------

class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes.A base class for all objects that may contain ConnectivityNodes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Connectivity nodes contained by this container.Connectivity nodes contained by this container.
    ConnectivityNodes = List(Instance("CPSM.IEC61970.Topology.ConnectivityNode"),
        desc="Connectivity nodes contained by this container.Connectivity nodes contained by this container.")

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNodeContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "ConnectivityNodes",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.ConnectivityNodeContainer",
        title="ConnectivityNodeContainer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConnectivityNodeContainer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquipmentContainer" class:
#------------------------------------------------------------------------------

class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classesA modeling construct to provide a root class for all Equipment classes
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Contains_Equipments = List(Instance("CPSM.IEC61970.Core.Equipment"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "EquipmentContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "ConnectivityNodes", "Contains_Equipments",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.EquipmentContainer",
        title="EquipmentContainer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquipmentContainer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VoltageLevel" class:
#------------------------------------------------------------------------------

class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    MemberOf_Substation = Instance("CPSM.IEC61970.Core.Substation", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Contains_VoltageLevels",
        editor=InstanceEditor(name="_substations"))

    def _get_substations(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.Substation" ]
        else:
            return []

    _substations = Property(fget=_get_substations)

    # The base voltage used for all equipment within the VoltageLevel.The base voltage used for all equipment within the VoltageLevel.
    BaseVoltage = Instance("CPSM.IEC61970.Core.BaseVoltage", allow_none=False,
        desc="The base voltage used for all equipment within the VoltageLevel.The base voltage used for all equipment within the VoltageLevel.",
        transient=True,
        opposite="VoltageLevel",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Contains_Bays = List(Instance("CPSM.IEC61970.Core.Bay"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    # The bus bar's low voltage limitThe bus bar's low voltage limit
    lowVoltageLimit = Voltage(desc="The bus bar's low voltage limitThe bus bar's low voltage limit")

    # The bus bar's high voltage limitThe bus bar's high voltage limit
    highVoltageLimit = Voltage(desc="The bus bar's high voltage limitThe bus bar's high voltage limit")

    #--------------------------------------------------------------------------
    #  Begin "VoltageLevel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "lowVoltageLimit", "highVoltageLimit",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "ConnectivityNodes", "Contains_Equipments", "MemberOf_Substation", "BaseVoltage", "Contains_Bays",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.VoltageLevel",
        title="VoltageLevel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageLevel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Bay" class:
#------------------------------------------------------------------------------

class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    MemberOf_VoltageLevel = Instance("CPSM.IEC61970.Core.VoltageLevel", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Contains_Bays",
        editor=InstanceEditor(name="_voltagelevels"))

    def _get_voltagelevels(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.VoltageLevel" ]
        else:
            return []

    _voltagelevels = Property(fget=_get_voltagelevels)

    #--------------------------------------------------------------------------
    #  Begin "Bay" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "ConnectivityNodes", "Contains_Equipments", "MemberOf_VoltageLevel",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.Bay",
        title="Bay",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Bay" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Equipment" class:
#------------------------------------------------------------------------------

class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanicalThe parts of a power system that are physical devices, electronic or mechanical
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    MemberOf_EquipmentContainer = Instance("CPSM.IEC61970.Core.EquipmentContainer", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Contains_Equipments",
        editor=InstanceEditor(name="_equipmentcontainers"))

    def _get_equipmentcontainers(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.EquipmentContainer" ]
        else:
            return []

    _equipmentcontainers = Property(fget=_get_equipmentcontainers)

    # The equipment limit sets associated with the equipment.The equipment limit sets associated with the equipment.
    OperationalLimitSet = List(Instance("CPSM.IEC61970.OperationalLimits.OperationalLimitSet"),
        desc="The equipment limit sets associated with the equipment.The equipment limit sets associated with the equipment.")

    #--------------------------------------------------------------------------
    #  Begin "Equipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.Equipment",
        title="Equipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Equipment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Substation" class:
#------------------------------------------------------------------------------

class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Region = Instance("CPSM.IEC61970.Core.SubGeographicalRegion", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Substations",
        editor=InstanceEditor(name="_subgeographicalregions"))

    def _get_subgeographicalregions(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.SubGeographicalRegion" ]
        else:
            return []

    _subgeographicalregions = Property(fget=_get_subgeographicalregions)

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Contains_VoltageLevels = List(Instance("CPSM.IEC61970.Core.VoltageLevel"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "Substation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "ConnectivityNodes", "Contains_Equipments", "Region", "Contains_VoltageLevels",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.Substation",
        title="Substation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Substation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConductingEquipment" class:
#------------------------------------------------------------------------------

class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.
    BaseVoltage = Instance("CPSM.IEC61970.Core.BaseVoltage", allow_none=False,
        desc="Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.",
        transient=True,
        opposite="ConductingEquipment",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    Terminals = List(Instance("CPSM.IEC61970.Core.Terminal"),
        desc="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes")

    #--------------------------------------------------------------------------
    #  Begin "ConductingEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Core.ConductingEquipment",
        title="ConductingEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductingEquipment" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
