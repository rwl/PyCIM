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

""" Defines TreeNodes interface for the model.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasTraits, Str, Property, Instance

from enthought.traits.ui.api \
    import View, Item, Group, TreeEditor, TreeNode

from enthought.traits.ui.menu \
    import Action, Menu

from CIM13r19 import *
from CIM13r19.Wires import *
from CIM13r19.Generation import *
from CIM13r19.Meas import *
from CIM13r19.LoadModel import *
from CIM13r19.Core import *
from CIM13r19.Contingency import *
from CIM13r19.Outage import *
from CIM13r19.SCADA import *
from CIM13r19.Domain import *
from CIM13r19.OperationalLimits import *
from CIM13r19.ControlArea import *
from CIM13r19.Equivalents import *
from CIM13r19.Topology import *
from CIM13r19.Protection import *
from CIM13r19.Generation.Production import *
from CIM13r19.Generation.GenerationDynamics import *

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------
# <<< constants
# @generated
IMAGE_PATH = ""
# >>> constants

#------------------------------------------------------------------------------
#  "ElementTreeNode" class:
#------------------------------------------------------------------------------

class ElementTreeNode(TreeNode):
    """ Defines a tree node for a Element.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Base class for Common Information Model elements.")

    # Name to use for a new instance.
    name = Str("Element")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Element]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ElementTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ElementTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Parent") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CommonInformationModelTreeNode" class:
#------------------------------------------------------------------------------

class CommonInformationModelTreeNode(TreeNode):
    """ Defines a tree node for a CommonInformationModel.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Defines a container of model elements conforming to IEC standard 61970.")

    # Name to use for a new instance.
    name = Str("CommonInformationModel")

    # List of object classes than can be added or copied.
    add = [Element, ]

    # List of object classes that can be moved.
    move = [Element, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CommonInformationModel]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CommonInformationModelTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "CommonInformationModelTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Elements") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "IEC61970CIMVersionTreeNode" class:
#------------------------------------------------------------------------------

class IEC61970CIMVersionTreeNode(TreeNode):
    """ Defines a tree node for a IEC61970CIMVersion.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=This is the IEC 61970 CIM version number assigned to this UML model file.")

    # Name to use for a new instance.
    name = Str("IEC61970CIMVersion")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [IEC61970CIMVersion]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "IEC61970CIMVersionTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "IEC61970CIMVersionTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RegulationScheduleTreeNode" class:
#------------------------------------------------------------------------------

class RegulationScheduleTreeNode(TreeNode):
    """ Defines a tree node for a RegulationSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A pre-established pattern over time for a controlled variable, e.g., busbar voltage.")

    # Name to use for a new instance.
    name = Str("RegulationSchedule")

    # List of object classes than can be added or copied.
    add = [RegulatingControl, VoltageControlZone, ]

    # List of object classes that can be moved.
    move = [RegulatingControl, VoltageControlZone, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RegulationSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RegulationScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "RegulationScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "RegulatingControl") )
        children.extend( getattr(object, "VoltageControlZones") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "GroundDisconnectorTreeNode" class:
#------------------------------------------------------------------------------

class GroundDisconnectorTreeNode(TreeNode):
    """ Defines a tree node for a GroundDisconnector.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A manually operated or motor operated mechanical switching device used for isolating a circuit or equipment from Ground.")

    # Name to use for a new instance.
    name = Str("GroundDisconnector")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [GroundDisconnector]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "GroundDisconnectorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "GroundDisconnectorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "TransformerWindingTreeNode" class:
#------------------------------------------------------------------------------

class TransformerWindingTreeNode(TreeNode):
    """ Defines a tree node for a TransformerWinding.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A winding is associated with each defined terminal of a transformer (or phase shifter).")

    # Name to use for a new instance.
    name = Str("TransformerWinding")

    # List of object classes than can be added or copied.
    add = [WindingTest, WindingTest, TapChanger, ]

    # List of object classes that can be moved.
    move = [WindingTest, WindingTest, TapChanger, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [TransformerWinding]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "TransformerWindingTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "TransformerWindingTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "To_WindingTest") )
        children.extend( getattr(object, "From_WindingTest") )
        children.extend( getattr(object, "TapChangers") )

        children.append( getattr(object, "MemberOf_PowerTransformer") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EnergySourceTreeNode" class:
#------------------------------------------------------------------------------

class EnergySourceTreeNode(TreeNode):
    """ Defines a tree node for a EnergySource.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A generic equivalent for an energy supplier on a transmission or distribution voltage level.")

    # Name to use for a new instance.
    name = Str("EnergySource")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [EnergySource]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EnergySourceTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "EnergySourceTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SeriesCompensatorTreeNode" class:
#------------------------------------------------------------------------------

class SeriesCompensatorTreeNode(TreeNode):
    """ Defines a tree node for a SeriesCompensator.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.")

    # Name to use for a new instance.
    name = Str("SeriesCompensator")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SeriesCompensator]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SeriesCompensatorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "SeriesCompensatorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "WireTypeTreeNode" class:
#------------------------------------------------------------------------------

class WireTypeTreeNode(TreeNode):
    """ Defines a tree node for a WireType.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.")

    # Name to use for a new instance.
    name = Str("WireType")

    # List of object classes than can be added or copied.
    add = [WireArrangement, ]

    # List of object classes that can be moved.
    move = [WireArrangement, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [WireType]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "WireTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "WireTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "WireArrangements") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "BreakerTreeNode" class:
#------------------------------------------------------------------------------

class BreakerTreeNode(TreeNode):
    """ Defines a tree node for a Breaker.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.")

    # Name to use for a new instance.
    name = Str("Breaker")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Breaker]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "BreakerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "BreakerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "VoltageControlZoneTreeNode" class:
#------------------------------------------------------------------------------

class VoltageControlZoneTreeNode(TreeNode):
    """ Defines a tree node for a VoltageControlZone.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.")

    # Name to use for a new instance.
    name = Str("VoltageControlZone")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [VoltageControlZone]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "VoltageControlZoneTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "VoltageControlZoneTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "RegulationSchedule") )
        children.append( getattr(object, "BusbarSection") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "FrequencyConverterTreeNode" class:
#------------------------------------------------------------------------------

class FrequencyConverterTreeNode(TreeNode):
    """ Defines a tree node for a FrequencyConverter.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2.")

    # Name to use for a new instance.
    name = Str("FrequencyConverter")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [FrequencyConverter]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "FrequencyConverterTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "FrequencyConverterTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RegulatingCondEqTreeNode" class:
#------------------------------------------------------------------------------

class RegulatingCondEqTreeNode(TreeNode):
    """ Defines a tree node for a RegulatingCondEq.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.")

    # Name to use for a new instance.
    name = Str("RegulatingCondEq")

    # List of object classes than can be added or copied.
    add = [Control, ]

    # List of object classes that can be moved.
    move = [Control, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RegulatingCondEq]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RegulatingCondEqTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "RegulatingCondEqTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Controls") )

        children.append( getattr(object, "RegulatingControl") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ConductorTreeNode" class:
#------------------------------------------------------------------------------

class ConductorTreeNode(TreeNode):
    """ Defines a tree node for a Conductor.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.")

    # Name to use for a new instance.
    name = Str("Conductor")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Conductor]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ConductorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ConductorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ConductorType") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "LoadBreakSwitchTreeNode" class:
#------------------------------------------------------------------------------

class LoadBreakSwitchTreeNode(TreeNode):
    """ Defines a tree node for a LoadBreakSwitch.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.")

    # Name to use for a new instance.
    name = Str("LoadBreakSwitch")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [LoadBreakSwitch]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "LoadBreakSwitchTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "LoadBreakSwitchTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ProtectedSwitchTreeNode" class:
#------------------------------------------------------------------------------

class ProtectedSwitchTreeNode(TreeNode):
    """ Defines a tree node for a ProtectedSwitch.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.")

    # Name to use for a new instance.
    name = Str("ProtectedSwitch")

    # List of object classes than can be added or copied.
    add = [ProtectionEquipment, RecloseSequence, ]

    # List of object classes that can be moved.
    move = [ProtectionEquipment, RecloseSequence, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ProtectedSwitch]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ProtectedSwitchTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ProtectedSwitchTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "OperatedBy_ProtectionEquipments") )
        children.extend( getattr(object, "RecloseSequences") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "LineTreeNode" class:
#------------------------------------------------------------------------------

class LineTreeNode(TreeNode):
    """ Defines a tree node for a Line.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.")

    # Name to use for a new instance.
    name = Str("Line")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Line]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "LineTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "LineTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Region") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "GroundTreeNode" class:
#------------------------------------------------------------------------------

class GroundTreeNode(TreeNode):
    """ Defines a tree node for a Ground.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground.")

    # Name to use for a new instance.
    name = Str("Ground")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Ground]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "GroundTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "GroundTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "JumperTreeNode" class:
#------------------------------------------------------------------------------

class JumperTreeNode(TreeNode):
    """ Defines a tree node for a Jumper.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A short section of conductor with negligible impedance which can be manually removed and replaced if the circuit is de-energized. Note that zero-impedance branches can be modelled by an ACLineSegment with a zero impedance ConductorType")

    # Name to use for a new instance.
    name = Str("Jumper")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Jumper]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "JumperTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "JumperTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "DCLineSegmentTreeNode" class:
#------------------------------------------------------------------------------

class DCLineSegmentTreeNode(TreeNode):
    """ Defines a tree node for a DCLineSegment.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.")

    # Name to use for a new instance.
    name = Str("DCLineSegment")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [DCLineSegment]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "DCLineSegmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "DCLineSegmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "TapChangerTreeNode" class:
#------------------------------------------------------------------------------

class TapChangerTreeNode(TreeNode):
    """ Defines a tree node for a TapChanger.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Mechanism for changing transformer winding tap positions.")

    # Name to use for a new instance.
    name = Str("TapChanger")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [TapChanger]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "TapChangerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "TapChangerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "TransformerWinding") )
        children.append( getattr(object, "RegulatingControl") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CompositeSwitchTreeNode" class:
#------------------------------------------------------------------------------

class CompositeSwitchTreeNode(TreeNode):
    """ Defines a tree node for a CompositeSwitch.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.")

    # Name to use for a new instance.
    name = Str("CompositeSwitch")

    # List of object classes than can be added or copied.
    add = [Switch, ]

    # List of object classes that can be moved.
    move = [Switch, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CompositeSwitch]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CompositeSwitchTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "CompositeSwitchTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Switches") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "WireArrangementTreeNode" class:
#------------------------------------------------------------------------------

class WireArrangementTreeNode(TreeNode):
    """ Defines a tree node for a WireArrangement.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Identification, spacing and configuration of the wires of a ConductorType, with reference to their type.")

    # Name to use for a new instance.
    name = Str("WireArrangement")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [WireArrangement]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "WireArrangementTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "WireArrangementTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ConductorType") )
        children.append( getattr(object, "WireType") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "PowerTransformerTreeNode" class:
#------------------------------------------------------------------------------

class PowerTransformerTreeNode(TreeNode):
    """ Defines a tree node for a PowerTransformer.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).")

    # Name to use for a new instance.
    name = Str("PowerTransformer")

    # List of object classes than can be added or copied.
    add = [TransformerWinding, ]

    # List of object classes that can be moved.
    move = [TransformerWinding, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [PowerTransformer]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "PowerTransformerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "PowerTransformerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contains_TransformerWindings") )

        children.append( getattr(object, "HeatExchanger") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "BusbarSectionTreeNode" class:
#------------------------------------------------------------------------------

class BusbarSectionTreeNode(TreeNode):
    """ Defines a tree node for a BusbarSection.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.")

    # Name to use for a new instance.
    name = Str("BusbarSection")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [BusbarSection]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "BusbarSectionTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "BusbarSectionTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "VoltageControlZone") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ACLineSegmentTreeNode" class:
#------------------------------------------------------------------------------

class ACLineSegmentTreeNode(TreeNode):
    """ Defines a tree node for a ACLineSegment.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.")

    # Name to use for a new instance.
    name = Str("ACLineSegment")

    # List of object classes than can be added or copied.
    add = [MutualCoupling, MutualCoupling, ]

    # List of object classes that can be moved.
    move = [MutualCoupling, MutualCoupling, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ACLineSegment]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ACLineSegmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ACLineSegmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "HasFirst_MutualCoupling") )
        children.extend( getattr(object, "HasSecond_MutualCoupling") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "MutualCouplingTreeNode" class:
#------------------------------------------------------------------------------

class MutualCouplingTreeNode(TreeNode):
    """ Defines a tree node for a MutualCoupling.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=This class represents the zero sequence line mutual coupling.")

    # Name to use for a new instance.
    name = Str("MutualCoupling")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [MutualCoupling]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "MutualCouplingTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "MutualCouplingTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "First_ACLineSegment") )
        children.append( getattr(object, "Second_ACLineSegment") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ShuntCompensatorTreeNode" class:
#------------------------------------------------------------------------------

class ShuntCompensatorTreeNode(TreeNode):
    """ Defines a tree node for a ShuntCompensator.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.")

    # Name to use for a new instance.
    name = Str("ShuntCompensator")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ShuntCompensator]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ShuntCompensatorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ShuntCompensatorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "FuseTreeNode" class:
#------------------------------------------------------------------------------

class FuseTreeNode(TreeNode):
    """ Defines a tree node for a Fuse.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.")

    # Name to use for a new instance.
    name = Str("Fuse")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Fuse]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "FuseTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "FuseTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RectifierInverterTreeNode" class:
#------------------------------------------------------------------------------

class RectifierInverterTreeNode(TreeNode):
    """ Defines a tree node for a RectifierInverter.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.")

    # Name to use for a new instance.
    name = Str("RectifierInverter")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RectifierInverter]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RectifierInverterTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "RectifierInverterTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "HeatExchangerTreeNode" class:
#------------------------------------------------------------------------------

class HeatExchangerTreeNode(TreeNode):
    """ Defines a tree node for a HeatExchanger.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Equipment for the cooling of electrical equipment and the extraction of heat")

    # Name to use for a new instance.
    name = Str("HeatExchanger")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [HeatExchanger]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "HeatExchangerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "HeatExchangerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "PowerTransformer") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EnergyConsumerTreeNode" class:
#------------------------------------------------------------------------------

class EnergyConsumerTreeNode(TreeNode):
    """ Defines a tree node for a EnergyConsumer.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Generic user of energy - a  point of consumption on the power system model")

    # Name to use for a new instance.
    name = Str("EnergyConsumer")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [EnergyConsumer]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EnergyConsumerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "EnergyConsumerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "PowerCutZone") )
        children.append( getattr(object, "LoadResponse") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SwitchTreeNode" class:
#------------------------------------------------------------------------------

class SwitchTreeNode(TreeNode):
    """ Defines a tree node for a Switch.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A generic device designed to close, or open, or both, one or more electric circuits.")

    # Name to use for a new instance.
    name = Str("Switch")

    # List of object classes than can be added or copied.
    add = [SwitchingOperation, ]

    # List of object classes that can be moved.
    move = [SwitchingOperation, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Switch]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SwitchTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "SwitchTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "SwitchingOperations") )

        children.append( getattr(object, "CompositeSwitch") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SynchronousMachineTreeNode" class:
#------------------------------------------------------------------------------

class SynchronousMachineTreeNode(TreeNode):
    """ Defines a tree node for a SynchronousMachine.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.")

    # Name to use for a new instance.
    name = Str("SynchronousMachine")

    # List of object classes than can be added or copied.
    add = [ReactiveCapabilityCurve, PrimeMover, ]

    # List of object classes that can be moved.
    move = [ReactiveCapabilityCurve, PrimeMover, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SynchronousMachine]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SynchronousMachineTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "SynchronousMachineTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "ReactiveCapabilityCurves") )
        children.extend( getattr(object, "DrivenBy_PrimeMover") )

        children.append( getattr(object, "Drives_HydroPump") )
        children.append( getattr(object, "MemberOf_GeneratingUnit") )
        children.append( getattr(object, "InitialReactiveCapabilityCurve") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RegulatingControlTreeNode" class:
#------------------------------------------------------------------------------

class RegulatingControlTreeNode(TreeNode):
    """ Defines a tree node for a RegulatingControl.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.")

    # Name to use for a new instance.
    name = Str("RegulatingControl")

    # List of object classes than can be added or copied.
    add = [RegulatingCondEq, TapChanger, ]

    # List of object classes that can be moved.
    move = [RegulatingCondEq, TapChanger, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RegulatingControl]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RegulatingControlTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "RegulatingControlTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "RegulatingCondEq") )
        children.extend( getattr(object, "TapChanger") )

        children.append( getattr(object, "Terminal") )
        children.append( getattr(object, "RegulationSchedule") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ConnectorTreeNode" class:
#------------------------------------------------------------------------------

class ConnectorTreeNode(TreeNode):
    """ Defines a tree node for a Connector.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation and are modelled with a single logical terminal.")

    # Name to use for a new instance.
    name = Str("Connector")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Connector]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ConnectorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ConnectorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "StaticVarCompensatorTreeNode" class:
#------------------------------------------------------------------------------

class StaticVarCompensatorTreeNode(TreeNode):
    """ Defines a tree node for a StaticVarCompensator.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.")

    # Name to use for a new instance.
    name = Str("StaticVarCompensator")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [StaticVarCompensator]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "StaticVarCompensatorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "StaticVarCompensatorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "JunctionTreeNode" class:
#------------------------------------------------------------------------------

class JunctionTreeNode(TreeNode):
    """ Defines a tree node for a Junction.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A point where one or more conducting equipments are connected with zero resistance.")

    # Name to use for a new instance.
    name = Str("Junction")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Junction]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "JunctionTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "JunctionTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "WindingTestTreeNode" class:
#------------------------------------------------------------------------------

class WindingTestTreeNode(TreeNode):
    """ Defines a tree node for a WindingTest.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Physical winding test data for the winding/tap pairs of a transformer (or phase shifter). This test data can be used to derive other attributes of specific transformer or phase shifter models.")

    # Name to use for a new instance.
    name = Str("WindingTest")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [WindingTest]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "WindingTestTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "WindingTestTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "To_TransformerWinding") )
        children.append( getattr(object, "From_TransformerWinding") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "DisconnectorTreeNode" class:
#------------------------------------------------------------------------------

class DisconnectorTreeNode(TreeNode):
    """ Defines a tree node for a Disconnector.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.")

    # Name to use for a new instance.
    name = Str("Disconnector")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Disconnector]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "DisconnectorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "DisconnectorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ConductorTypeTreeNode" class:
#------------------------------------------------------------------------------

class ConductorTypeTreeNode(TreeNode):
    """ Defines a tree node for a ConductorType.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Wire or cable conductor (per IEEE specs). A specific type of wire or combination of wires not insulated from one another, suitable for carrying electric current. It may be bare or insulated.")

    # Name to use for a new instance.
    name = Str("ConductorType")

    # List of object classes than can be added or copied.
    add = [Conductor, WireArrangement, ]

    # List of object classes that can be moved.
    move = [Conductor, WireArrangement, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ConductorType]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ConductorTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ConductorTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Conductors") )
        children.extend( getattr(object, "WireArrangements") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "PlantTreeNode" class:
#------------------------------------------------------------------------------

class PlantTreeNode(TreeNode):
    """ Defines a tree node for a Plant.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A Plant is a collection of equipment for purposes of generation.")

    # Name to use for a new instance.
    name = Str("Plant")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Plant]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "PlantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "PlantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ReactiveCapabilityCurveTreeNode" class:
#------------------------------------------------------------------------------

class ReactiveCapabilityCurveTreeNode(TreeNode):
    """ Defines a tree node for a ReactiveCapabilityCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.")

    # Name to use for a new instance.
    name = Str("ReactiveCapabilityCurve")

    # List of object classes than can be added or copied.
    add = [SynchronousMachine, SynchronousMachine, ]

    # List of object classes that can be moved.
    move = [SynchronousMachine, SynchronousMachine, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ReactiveCapabilityCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ReactiveCapabilityCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ReactiveCapabilityCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "SynchronousMachines") )
        children.extend( getattr(object, "InitiallyUsedBySynchronousMachine") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "NuclearGeneratingUnitTreeNode" class:
#------------------------------------------------------------------------------

class NuclearGeneratingUnitTreeNode(TreeNode):
    """ Defines a tree node for a NuclearGeneratingUnit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A nuclear generating unit.")

    # Name to use for a new instance.
    name = Str("NuclearGeneratingUnit")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [NuclearGeneratingUnit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "NuclearGeneratingUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "NuclearGeneratingUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "GeneratingUnitTreeNode" class:
#------------------------------------------------------------------------------

class GeneratingUnitTreeNode(TreeNode):
    """ Defines a tree node for a GeneratingUnit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.")

    # Name to use for a new instance.
    name = Str("GeneratingUnit")

    # List of object classes than can be added or copied.
    add = [ControlAreaGeneratingUnit, GrossToNetActivePowerCurve, SynchronousMachine, GenUnitOpCostCurve, ]

    # List of object classes that can be moved.
    move = [ControlAreaGeneratingUnit, GrossToNetActivePowerCurve, SynchronousMachine, GenUnitOpCostCurve, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [GeneratingUnit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "GeneratingUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "GeneratingUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "ControlAreaGeneratingUnit") )
        children.extend( getattr(object, "GrossToNetActivePowerCurves") )
        children.extend( getattr(object, "Contains_SynchronousMachines") )
        children.extend( getattr(object, "GenUnitOpCostCurves") )

        children.append( getattr(object, "GenUnitOpSchedule") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "StartIgnFuelCurveTreeNode" class:
#------------------------------------------------------------------------------

class StartIgnFuelCurveTreeNode(TreeNode):
    """ Defines a tree node for a StartIgnFuelCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line")

    # Name to use for a new instance.
    name = Str("StartIgnFuelCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [StartIgnFuelCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "StartIgnFuelCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "StartIgnFuelCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "StartupModel") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "HydroGeneratingEfficiencyCurveTreeNode" class:
#------------------------------------------------------------------------------

class HydroGeneratingEfficiencyCurveTreeNode(TreeNode):
    """ Defines a tree node for a HydroGeneratingEfficiencyCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.")

    # Name to use for a new instance.
    name = Str("HydroGeneratingEfficiencyCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [HydroGeneratingEfficiencyCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "HydroGeneratingEfficiencyCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "HydroGeneratingEfficiencyCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "HydroGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "TargetLevelScheduleTreeNode" class:
#------------------------------------------------------------------------------

class TargetLevelScheduleTreeNode(TreeNode):
    """ Defines a tree node for a TargetLevelSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Reservoir water level targets from advanced studies or 'rule curves'. Typically in one hour increments for up to 10 days")

    # Name to use for a new instance.
    name = Str("TargetLevelSchedule")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [TargetLevelSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "TargetLevelScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "TargetLevelScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Reservoir") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "GrossToNetActivePowerCurveTreeNode" class:
#------------------------------------------------------------------------------

class GrossToNetActivePowerCurveTreeNode(TreeNode):
    """ Defines a tree node for a GrossToNetActivePowerCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.")

    # Name to use for a new instance.
    name = Str("GrossToNetActivePowerCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [GrossToNetActivePowerCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "GrossToNetActivePowerCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "GrossToNetActivePowerCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "GeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "IncrementalHeatRateCurveTreeNode" class:
#------------------------------------------------------------------------------

class IncrementalHeatRateCurveTreeNode(TreeNode):
    """ Defines a tree node for a IncrementalHeatRateCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between unit incremental heat rate in (delta energy/time) per (delta active power) and unit output in active power. The IHR curve represents the slope of the HeatInputCurve. Note that the 'incremental heat rate' and the 'heat rate' have the same engineering units.")

    # Name to use for a new instance.
    name = Str("IncrementalHeatRateCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [IncrementalHeatRateCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "IncrementalHeatRateCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "IncrementalHeatRateCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ThermalGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "HeatInputCurveTreeNode" class:
#------------------------------------------------------------------------------

class HeatInputCurveTreeNode(TreeNode):
    """ Defines a tree node for a HeatInputCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.")

    # Name to use for a new instance.
    name = Str("HeatInputCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [HeatInputCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "HeatInputCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "HeatInputCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ThermalGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "StartRampCurveTreeNode" class:
#------------------------------------------------------------------------------

class StartRampCurveTreeNode(TreeNode):
    """ Defines a tree node for a StartRampCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line")

    # Name to use for a new instance.
    name = Str("StartRampCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [StartRampCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "StartRampCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "StartRampCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "StartupModel") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AirCompressorTreeNode" class:
#------------------------------------------------------------------------------

class AirCompressorTreeNode(TreeNode):
    """ Defines a tree node for a AirCompressor.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant")

    # Name to use for a new instance.
    name = Str("AirCompressor")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [AirCompressor]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AirCompressorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "AirCompressorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "DrivenBy_CombustionTurbine") )
        children.append( getattr(object, "MemberOf_CAESPlant") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ShutdownCurveTreeNode" class:
#------------------------------------------------------------------------------

class ShutdownCurveTreeNode(TreeNode):
    """ Defines a tree node for a ShutdownCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)")

    # Name to use for a new instance.
    name = Str("ShutdownCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ShutdownCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ShutdownCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ShutdownCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ThermalGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CombinedCyclePlantTreeNode" class:
#------------------------------------------------------------------------------

class CombinedCyclePlantTreeNode(TreeNode):
    """ Defines a tree node for a CombinedCyclePlant.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency")

    # Name to use for a new instance.
    name = Str("CombinedCyclePlant")

    # List of object classes than can be added or copied.
    add = [ThermalGeneratingUnit, ]

    # List of object classes that can be moved.
    move = [ThermalGeneratingUnit, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CombinedCyclePlant]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CombinedCyclePlantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "CombinedCyclePlantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contain_ThermalGeneratingUnits") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "StartupModelTreeNode" class:
#------------------------------------------------------------------------------

class StartupModelTreeNode(TreeNode):
    """ Defines a tree node for a StartupModel.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Unit start up characteristics depending on how long the unit has been off line")

    # Name to use for a new instance.
    name = Str("StartupModel")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [StartupModel]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "StartupModelTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "StartupModelTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "StartIgnFuelCurve") )
        children.append( getattr(object, "StartRampCurve") )
        children.append( getattr(object, "StartMainFuelCurve") )
        children.append( getattr(object, "ThermalGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "HydroPumpTreeNode" class:
#------------------------------------------------------------------------------

class HydroPumpTreeNode(TreeNode):
    """ Defines a tree node for a HydroPump.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A synchronous motor-driven pump, typically associated with a pumped storage plant")

    # Name to use for a new instance.
    name = Str("HydroPump")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [HydroPump]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "HydroPumpTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "HydroPumpTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "MemberOf_HydroPowerPlant") )
        children.append( getattr(object, "HydroPumpOpSchedule") )
        children.append( getattr(object, "DrivenBy_SynchronousMachine") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EmissionCurveTreeNode" class:
#------------------------------------------------------------------------------

class EmissionCurveTreeNode(TreeNode):
    """ Defines a tree node for a EmissionCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.")

    # Name to use for a new instance.
    name = Str("EmissionCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [EmissionCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EmissionCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "EmissionCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ThermalGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "GenUnitOpCostCurveTreeNode" class:
#------------------------------------------------------------------------------

class GenUnitOpCostCurveTreeNode(TreeNode):
    """ Defines a tree node for a GenUnitOpCostCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between unit operating cost (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs.")

    # Name to use for a new instance.
    name = Str("GenUnitOpCostCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [GenUnitOpCostCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "GenUnitOpCostCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "GenUnitOpCostCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "GeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "HydroPowerPlantTreeNode" class:
#------------------------------------------------------------------------------

class HydroPowerPlantTreeNode(TreeNode):
    """ Defines a tree node for a HydroPowerPlant.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.")

    # Name to use for a new instance.
    name = Str("HydroPowerPlant")

    # List of object classes than can be added or copied.
    add = [HydroGeneratingUnit, HydroPump, ]

    # List of object classes that can be moved.
    move = [HydroGeneratingUnit, HydroPump, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [HydroPowerPlant]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "HydroPowerPlantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "HydroPowerPlantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contain_HydroGeneratingUnits") )
        children.extend( getattr(object, "Contain_HydroPumps") )

        children.append( getattr(object, "Reservoir") )
        children.append( getattr(object, "GenSourcePumpDischarge") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "HydroGeneratingUnitTreeNode" class:
#------------------------------------------------------------------------------

class HydroGeneratingUnitTreeNode(TreeNode):
    """ Defines a tree node for a HydroGeneratingUnit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)")

    # Name to use for a new instance.
    name = Str("HydroGeneratingUnit")

    # List of object classes than can be added or copied.
    add = [HydroGeneratingEfficiencyCurve, TailbayLossCurve, ]

    # List of object classes that can be moved.
    move = [HydroGeneratingEfficiencyCurve, TailbayLossCurve, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [HydroGeneratingUnit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "HydroGeneratingUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "HydroGeneratingUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "HydroGeneratingEfficiencyCurves") )
        children.extend( getattr(object, "TailbayLossCurve") )

        children.append( getattr(object, "MemberOf_HydroPowerPlant") )
        children.append( getattr(object, "PenstockLossCurve") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CAESPlantTreeNode" class:
#------------------------------------------------------------------------------

class CAESPlantTreeNode(TreeNode):
    """ Defines a tree node for a CAESPlant.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Compressed air energy storage plant")

    # Name to use for a new instance.
    name = Str("CAESPlant")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CAESPlant]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CAESPlantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "CAESPlantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Contain_AirCompressor") )
        children.append( getattr(object, "Contain_ThermalGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "LevelVsVolumeCurveTreeNode" class:
#------------------------------------------------------------------------------

class LevelVsVolumeCurveTreeNode(TreeNode):
    """ Defines a tree node for a LevelVsVolumeCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis.")

    # Name to use for a new instance.
    name = Str("LevelVsVolumeCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [LevelVsVolumeCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "LevelVsVolumeCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "LevelVsVolumeCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Reservoir") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "InflowForecastTreeNode" class:
#------------------------------------------------------------------------------

class InflowForecastTreeNode(TreeNode):
    """ Defines a tree node for a InflowForecast.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Natural water inflow to a reservoir, usually forecasted from predicted rain and snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in average cubic meters per second over the time increment.")

    # Name to use for a new instance.
    name = Str("InflowForecast")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [InflowForecast]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "InflowForecastTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "InflowForecastTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Reservoir") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SteamSendoutScheduleTreeNode" class:
#------------------------------------------------------------------------------

class SteamSendoutScheduleTreeNode(TreeNode):
    """ Defines a tree node for a SteamSendoutSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The cogeneration plant's steam sendout schedule in volume per time unit.")

    # Name to use for a new instance.
    name = Str("SteamSendoutSchedule")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SteamSendoutSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SteamSendoutScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "SteamSendoutScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "CogenerationPlant") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ThermalGeneratingUnitTreeNode" class:
#------------------------------------------------------------------------------

class ThermalGeneratingUnitTreeNode(TreeNode):
    """ Defines a tree node for a ThermalGeneratingUnit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.")

    # Name to use for a new instance.
    name = Str("ThermalGeneratingUnit")

    # List of object classes than can be added or copied.
    add = [FuelAllocationSchedule, EmissionCurve, EmissionAccount, FossilFuel, ]

    # List of object classes that can be moved.
    move = [FuelAllocationSchedule, EmissionCurve, EmissionAccount, FossilFuel, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ThermalGeneratingUnit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ThermalGeneratingUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ThermalGeneratingUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "FuelAllocationSchedules") )
        children.extend( getattr(object, "EmissionCurves") )
        children.extend( getattr(object, "EmmissionAccounts") )
        children.extend( getattr(object, "FossilFuels") )

        children.append( getattr(object, "MemberOf_CogenerationPlant") )
        children.append( getattr(object, "StartupModel") )
        children.append( getattr(object, "IncrementalHeatRateCurve") )
        children.append( getattr(object, "ShutdownCurve") )
        children.append( getattr(object, "HeatRateCurve") )
        children.append( getattr(object, "MemberOf_CAESPlant") )
        children.append( getattr(object, "HeatInputCurve") )
        children.append( getattr(object, "MemberOf_CombinedCyclePlant") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "FossilFuelTreeNode" class:
#------------------------------------------------------------------------------

class FossilFuelTreeNode(TreeNode):
    """ Defines a tree node for a FossilFuel.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas")

    # Name to use for a new instance.
    name = Str("FossilFuel")

    # List of object classes than can be added or copied.
    add = [FuelAllocationSchedule, ]

    # List of object classes that can be moved.
    move = [FuelAllocationSchedule, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [FossilFuel]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "FossilFuelTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "FossilFuelTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "FuelAllocationSchedule") )

        children.append( getattr(object, "ThermalGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "FuelAllocationScheduleTreeNode" class:
#------------------------------------------------------------------------------

class FuelAllocationScheduleTreeNode(TreeNode):
    """ Defines a tree node for a FuelAllocationSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The amount of fuel of a given type which is allocated for consumption over a specified period of time")

    # Name to use for a new instance.
    name = Str("FuelAllocationSchedule")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [FuelAllocationSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "FuelAllocationScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "FuelAllocationScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "FossilFuel") )
        children.append( getattr(object, "ThermalGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EmissionAccountTreeNode" class:
#------------------------------------------------------------------------------

class EmissionAccountTreeNode(TreeNode):
    """ Defines a tree node for a EmissionAccount.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Accounts for tracking emissions usage and credits for thermal generating units. A unit may have zero or more emission accounts, and will typically have one for tracking usage and one for tracking credits.")

    # Name to use for a new instance.
    name = Str("EmissionAccount")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [EmissionAccount]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EmissionAccountTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "EmissionAccountTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ThermalGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "TailbayLossCurveTreeNode" class:
#------------------------------------------------------------------------------

class TailbayLossCurveTreeNode(TreeNode):
    """ Defines a tree node for a TailbayLossCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between tailbay head loss hight (y-axis) and the total discharge into the power station's tailbay volume per time unit (x-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level")

    # Name to use for a new instance.
    name = Str("TailbayLossCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [TailbayLossCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "TailbayLossCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "TailbayLossCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "HydroGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "PenstockLossCurveTreeNode" class:
#------------------------------------------------------------------------------

class PenstockLossCurveTreeNode(TreeNode):
    """ Defines a tree node for a PenstockLossCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.")

    # Name to use for a new instance.
    name = Str("PenstockLossCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [PenstockLossCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "PenstockLossCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "PenstockLossCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "HydroGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "StartMainFuelCurveTreeNode" class:
#------------------------------------------------------------------------------

class StartMainFuelCurveTreeNode(TreeNode):
    """ Defines a tree node for a StartMainFuelCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line")

    # Name to use for a new instance.
    name = Str("StartMainFuelCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [StartMainFuelCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "StartMainFuelCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "StartMainFuelCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "StartupModel") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ReservoirTreeNode" class:
#------------------------------------------------------------------------------

class ReservoirTreeNode(TreeNode):
    """ Defines a tree node for a Reservoir.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam.")

    # Name to use for a new instance.
    name = Str("Reservoir")

    # List of object classes than can be added or copied.
    add = [LevelVsVolumeCurve, InflowForecast, Reservoir, HydroPowerPlant, HydroPowerPlant, ]

    # List of object classes that can be moved.
    move = [LevelVsVolumeCurve, InflowForecast, Reservoir, HydroPowerPlant, HydroPowerPlant, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Reservoir]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ReservoirTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ReservoirTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "LevelVsVolumeCurve") )
        children.extend( getattr(object, "InflowForecast") )
        children.extend( getattr(object, "SpillsInto") )
        children.extend( getattr(object, "HydroPowerPlants") )
        children.extend( getattr(object, "UpstreamFrom") )

        children.append( getattr(object, "SpillsFrom") )
        children.append( getattr(object, "TargetLevelSchedule") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "HydroPumpOpScheduleTreeNode" class:
#------------------------------------------------------------------------------

class HydroPumpOpScheduleTreeNode(TreeNode):
    """ Defines a tree node for a HydroPumpOpSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)")

    # Name to use for a new instance.
    name = Str("HydroPumpOpSchedule")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [HydroPumpOpSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "HydroPumpOpScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "HydroPumpOpScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "HydroPump") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "HeatRateCurveTreeNode" class:
#------------------------------------------------------------------------------

class HeatRateCurveTreeNode(TreeNode):
    """ Defines a tree node for a HeatRateCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between unit heat rate per active power (Y-axis) and  unit output (X-axis). The heat input is from all fuels.")

    # Name to use for a new instance.
    name = Str("HeatRateCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [HeatRateCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "HeatRateCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "HeatRateCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ThermalGeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "GenUnitOpScheduleTreeNode" class:
#------------------------------------------------------------------------------

class GenUnitOpScheduleTreeNode(TreeNode):
    """ Defines a tree node for a GenUnitOpSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.")

    # Name to use for a new instance.
    name = Str("GenUnitOpSchedule")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [GenUnitOpSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "GenUnitOpScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "GenUnitOpScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "GeneratingUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CogenerationPlantTreeNode" class:
#------------------------------------------------------------------------------

class CogenerationPlantTreeNode(TreeNode):
    """ Defines a tree node for a CogenerationPlant.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.")

    # Name to use for a new instance.
    name = Str("CogenerationPlant")

    # List of object classes than can be added or copied.
    add = [ThermalGeneratingUnit, ]

    # List of object classes that can be moved.
    move = [ThermalGeneratingUnit, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CogenerationPlant]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CogenerationPlantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "CogenerationPlantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contain_ThermalGeneratingUnits") )

        children.append( getattr(object, "SteamSendoutSchedule") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SupercriticalTreeNode" class:
#------------------------------------------------------------------------------

class SupercriticalTreeNode(TreeNode):
    """ Defines a tree node for a Supercritical.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Once-through supercritical boiler")

    # Name to use for a new instance.
    name = Str("Supercritical")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Supercritical]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SupercriticalTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "SupercriticalTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SteamTurbineTreeNode" class:
#------------------------------------------------------------------------------

class SteamTurbineTreeNode(TreeNode):
    """ Defines a tree node for a SteamTurbine.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Steam turbine")

    # Name to use for a new instance.
    name = Str("SteamTurbine")

    # List of object classes than can be added or copied.
    add = [SteamSupply, ]

    # List of object classes that can be moved.
    move = [SteamSupply, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SteamTurbine]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SteamTurbineTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "SteamTurbineTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "SteamSupplys") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CTTempActivePowerCurveTreeNode" class:
#------------------------------------------------------------------------------

class CTTempActivePowerCurveTreeNode(TreeNode):
    """ Defines a tree node for a CTTempActivePowerCurve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)")

    # Name to use for a new instance.
    name = Str("CTTempActivePowerCurve")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CTTempActivePowerCurve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CTTempActivePowerCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "CTTempActivePowerCurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "CombustionTurbine") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "PrimeMoverTreeNode" class:
#------------------------------------------------------------------------------

class PrimeMoverTreeNode(TreeNode):
    """ Defines a tree node for a PrimeMover.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The machine used to develop mechanical energy used to drive a generator.")

    # Name to use for a new instance.
    name = Str("PrimeMover")

    # List of object classes than can be added or copied.
    add = [SynchronousMachine, ]

    # List of object classes that can be moved.
    move = [SynchronousMachine, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [PrimeMover]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "PrimeMoverTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "PrimeMoverTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Drives_SynchronousMachines") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "PWRSteamSupplyTreeNode" class:
#------------------------------------------------------------------------------

class PWRSteamSupplyTreeNode(TreeNode):
    """ Defines a tree node for a PWRSteamSupply.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Pressurized water reactor used as a steam supply to a steam turbine")

    # Name to use for a new instance.
    name = Str("PWRSteamSupply")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [PWRSteamSupply]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "PWRSteamSupplyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "PWRSteamSupplyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CombustionTurbineTreeNode" class:
#------------------------------------------------------------------------------

class CombustionTurbineTreeNode(TreeNode):
    """ Defines a tree node for a CombustionTurbine.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A prime mover that is typically fueled by gas or light oil")

    # Name to use for a new instance.
    name = Str("CombustionTurbine")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CombustionTurbine]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CombustionTurbineTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "CombustionTurbineTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Drives_AirCompressor") )
        children.append( getattr(object, "CTTempActivePowerCurve") )
        children.append( getattr(object, "HeatRecoveryBoiler") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "HeatRecoveryBoilerTreeNode" class:
#------------------------------------------------------------------------------

class HeatRecoveryBoilerTreeNode(TreeNode):
    """ Defines a tree node for a HeatRecoveryBoiler.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants")

    # Name to use for a new instance.
    name = Str("HeatRecoveryBoiler")

    # List of object classes than can be added or copied.
    add = [CombustionTurbine, ]

    # List of object classes that can be moved.
    move = [CombustionTurbine, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [HeatRecoveryBoiler]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "HeatRecoveryBoilerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "HeatRecoveryBoilerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "CombustionTurbines") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "BWRSteamSupplyTreeNode" class:
#------------------------------------------------------------------------------

class BWRSteamSupplyTreeNode(TreeNode):
    """ Defines a tree node for a BWRSteamSupply.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Boiling water reactor used as a steam supply to a steam turbine")

    # Name to use for a new instance.
    name = Str("BWRSteamSupply")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [BWRSteamSupply]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "BWRSteamSupplyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "BWRSteamSupplyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "HydroTurbineTreeNode" class:
#------------------------------------------------------------------------------

class HydroTurbineTreeNode(TreeNode):
    """ Defines a tree node for a HydroTurbine.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.")

    # Name to use for a new instance.
    name = Str("HydroTurbine")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [HydroTurbine]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "HydroTurbineTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "HydroTurbineTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "DrumBoilerTreeNode" class:
#------------------------------------------------------------------------------

class DrumBoilerTreeNode(TreeNode):
    """ Defines a tree node for a DrumBoiler.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Drum boiler")

    # Name to use for a new instance.
    name = Str("DrumBoiler")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [DrumBoiler]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "DrumBoilerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "DrumBoilerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "FossilSteamSupplyTreeNode" class:
#------------------------------------------------------------------------------

class FossilSteamSupplyTreeNode(TreeNode):
    """ Defines a tree node for a FossilSteamSupply.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Fossil fueled boiler (e.g., coal, oil, gas)")

    # Name to use for a new instance.
    name = Str("FossilSteamSupply")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [FossilSteamSupply]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "FossilSteamSupplyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "FossilSteamSupplyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SubcriticalTreeNode" class:
#------------------------------------------------------------------------------

class SubcriticalTreeNode(TreeNode):
    """ Defines a tree node for a Subcritical.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Once-through subcritical boiler")

    # Name to use for a new instance.
    name = Str("Subcritical")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Subcritical]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SubcriticalTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "SubcriticalTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SteamSupplyTreeNode" class:
#------------------------------------------------------------------------------

class SteamSupplyTreeNode(TreeNode):
    """ Defines a tree node for a SteamSupply.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Steam supply for steam turbine")

    # Name to use for a new instance.
    name = Str("SteamSupply")

    # List of object classes than can be added or copied.
    add = [SteamTurbine, ]

    # List of object classes that can be moved.
    move = [SteamTurbine, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SteamSupply]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SteamSupplyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "SteamSupplyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "SteamTurbines") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "DiscreteTreeNode" class:
#------------------------------------------------------------------------------

class DiscreteTreeNode(TreeNode):
    """ Defines a tree node for a Discrete.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.")

    # Name to use for a new instance.
    name = Str("Discrete")

    # List of object classes than can be added or copied.
    add = [DiscreteValue, ]

    # List of object classes that can be moved.
    move = [DiscreteValue, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Discrete]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "DiscreteTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "DiscreteTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contain_MeasurementValues") )

        children.append( getattr(object, "ValueAliasSet") )
        children.append( getattr(object, "ControlledBy_Control") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "MeasurementTreeNode" class:
#------------------------------------------------------------------------------

class MeasurementTreeNode(TreeNode):
    """ Defines a tree node for a Measurement.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.")

    # Name to use for a new instance.
    name = Str("Measurement")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Measurement]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "MeasurementTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "MeasurementTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Terminal") )
        children.append( getattr(object, "MemberOf_PSR") )
        children.append( getattr(object, "Unit") )
        children.append( getattr(object, "MeasurementType") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SetPointTreeNode" class:
#------------------------------------------------------------------------------

class SetPointTreeNode(TreeNode):
    """ Defines a tree node for a SetPoint.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A SetPoint is an analog control used for supervisory control.")

    # Name to use for a new instance.
    name = Str("SetPoint")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SetPoint]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SetPointTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "SetPointTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "MeasuredBy_Measurement") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ControlTreeNode" class:
#------------------------------------------------------------------------------

class ControlTreeNode(TreeNode):
    """ Defines a tree node for a Control.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.")

    # Name to use for a new instance.
    name = Str("Control")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Control]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ControlTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ControlTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Unit") )
        children.append( getattr(object, "ControlType") )
        children.append( getattr(object, "RemoteControl") )
        children.append( getattr(object, "ControlledBy_RegulatingCondEq") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ControlTypeTreeNode" class:
#------------------------------------------------------------------------------

class ControlTypeTreeNode(TreeNode):
    """ Defines a tree node for a ControlType.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization.")

    # Name to use for a new instance.
    name = Str("ControlType")

    # List of object classes than can be added or copied.
    add = [Control, ]

    # List of object classes that can be moved.
    move = [Control, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ControlType]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ControlTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ControlTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Controls") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "DiscreteValueTreeNode" class:
#------------------------------------------------------------------------------

class DiscreteValueTreeNode(TreeNode):
    """ Defines a tree node for a DiscreteValue.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=DiscreteValue represents a discrete MeasurementValue.")

    # Name to use for a new instance.
    name = Str("DiscreteValue")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [DiscreteValue]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "DiscreteValueTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "DiscreteValueTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "MemberOf_Measurement") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AccumulatorTreeNode" class:
#------------------------------------------------------------------------------

class AccumulatorTreeNode(TreeNode):
    """ Defines a tree node for a Accumulator.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.")

    # Name to use for a new instance.
    name = Str("Accumulator")

    # List of object classes than can be added or copied.
    add = [AccumulatorValue, AccumulatorLimitSet, ]

    # List of object classes that can be moved.
    move = [AccumulatorValue, AccumulatorLimitSet, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Accumulator]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "AccumulatorTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contain_MeasurementValues") )
        children.extend( getattr(object, "LimitSets") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "LimitSetTreeNode" class:
#------------------------------------------------------------------------------

class LimitSetTreeNode(TreeNode):
    """ Defines a tree node for a LimitSet.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.")

    # Name to use for a new instance.
    name = Str("LimitSet")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [LimitSet]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "LimitSetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "LimitSetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AnalogLimitTreeNode" class:
#------------------------------------------------------------------------------

class AnalogLimitTreeNode(TreeNode):
    """ Defines a tree node for a AnalogLimit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Limit values for Analog measurements")

    # Name to use for a new instance.
    name = Str("AnalogLimit")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [AnalogLimit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AnalogLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "AnalogLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "LimitSet") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "MeasurementValueTreeNode" class:
#------------------------------------------------------------------------------

class MeasurementValueTreeNode(TreeNode):
    """ Defines a tree node for a MeasurementValue.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.")

    # Name to use for a new instance.
    name = Str("MeasurementValue")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [MeasurementValue]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValueTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "MeasurementValueTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "MeasurementValueQuality") )
        children.append( getattr(object, "RemoteSource") )
        children.append( getattr(object, "MeasurementValueSource") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ValueAliasSetTreeNode" class:
#------------------------------------------------------------------------------

class ValueAliasSetTreeNode(TreeNode):
    """ Defines a tree node for a ValueAliasSet.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.")

    # Name to use for a new instance.
    name = Str("ValueAliasSet")

    # List of object classes than can be added or copied.
    add = [ValueToAlias, Command, Discrete, ]

    # List of object classes that can be moved.
    move = [ValueToAlias, Command, Discrete, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ValueAliasSet]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ValueAliasSetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ValueAliasSetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Values") )
        children.extend( getattr(object, "Commands") )
        children.extend( getattr(object, "Measurements") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "StringMeasurementValueTreeNode" class:
#------------------------------------------------------------------------------

class StringMeasurementValueTreeNode(TreeNode):
    """ Defines a tree node for a StringMeasurementValue.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=StringMeasurementValue represents a measurement value of type string.")

    # Name to use for a new instance.
    name = Str("StringMeasurementValue")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [StringMeasurementValue]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "StringMeasurementValueTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "StringMeasurementValueTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "MemberOf_Measurement") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "Quality61850TreeNode" class:
#------------------------------------------------------------------------------

class Quality61850TreeNode(TreeNode):
    """ Defines a tree node for a Quality61850.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.")

    # Name to use for a new instance.
    name = Str("Quality61850")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Quality61850]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "Quality61850TreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "Quality61850TreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "LimitTreeNode" class:
#------------------------------------------------------------------------------

class LimitTreeNode(TreeNode):
    """ Defines a tree node for a Limit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.")

    # Name to use for a new instance.
    name = Str("Limit")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Limit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "LimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "LimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "MeasurementTypeTreeNode" class:
#------------------------------------------------------------------------------

class MeasurementTypeTreeNode(TreeNode):
    """ Defines a tree node for a MeasurementType.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.")

    # Name to use for a new instance.
    name = Str("MeasurementType")

    # List of object classes than can be added or copied.
    add = [Measurement, ]

    # List of object classes that can be moved.
    move = [Measurement, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [MeasurementType]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "MeasurementTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "MeasurementTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Measurements") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AccumulatorLimitTreeNode" class:
#------------------------------------------------------------------------------

class AccumulatorLimitTreeNode(TreeNode):
    """ Defines a tree node for a AccumulatorLimit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Limit values for Accumulator measurements")

    # Name to use for a new instance.
    name = Str("AccumulatorLimit")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [AccumulatorLimit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "AccumulatorLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "LimitSet") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "StringMeasurementTreeNode" class:
#------------------------------------------------------------------------------

class StringMeasurementTreeNode(TreeNode):
    """ Defines a tree node for a StringMeasurement.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=StringMeasurement represents a measurement with values of type string.")

    # Name to use for a new instance.
    name = Str("StringMeasurement")

    # List of object classes than can be added or copied.
    add = [StringMeasurementValue, ]

    # List of object classes that can be moved.
    move = [StringMeasurementValue, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [StringMeasurement]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "StringMeasurementTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "StringMeasurementTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contains_MeasurementValues") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ValueToAliasTreeNode" class:
#------------------------------------------------------------------------------

class ValueToAliasTreeNode(TreeNode):
    """ Defines a tree node for a ValueToAlias.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Describes the translation of one particular value into a name, e.g. 1->'Open'")

    # Name to use for a new instance.
    name = Str("ValueToAlias")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ValueToAlias]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ValueToAliasTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ValueToAliasTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ValueAliasSet") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AnalogValueTreeNode" class:
#------------------------------------------------------------------------------

class AnalogValueTreeNode(TreeNode):
    """ Defines a tree node for a AnalogValue.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=AnalogValue represents an analog MeasurementValue.")

    # Name to use for a new instance.
    name = Str("AnalogValue")

    # List of object classes than can be added or copied.
    add = [AltGeneratingUnitMeas, AltTieMeas, ]

    # List of object classes that can be moved.
    move = [AltGeneratingUnitMeas, AltTieMeas, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [AnalogValue]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AnalogValueTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "AnalogValueTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "AltGeneratingUnit") )
        children.extend( getattr(object, "AltTieMeas") )

        children.append( getattr(object, "MemberOf_Measurement") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "MeasurementValueQualityTreeNode" class:
#------------------------------------------------------------------------------

class MeasurementValueQualityTreeNode(TreeNode):
    """ Defines a tree node for a MeasurementValueQuality.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.")

    # Name to use for a new instance.
    name = Str("MeasurementValueQuality")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [MeasurementValueQuality]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValueQualityTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "MeasurementValueQualityTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "MeasurementValue") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "MeasurementValueSourceTreeNode" class:
#------------------------------------------------------------------------------

class MeasurementValueSourceTreeNode(TreeNode):
    """ Defines a tree node for a MeasurementValueSource.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.")

    # Name to use for a new instance.
    name = Str("MeasurementValueSource")

    # List of object classes than can be added or copied.
    add = [MeasurementValue, ]

    # List of object classes that can be moved.
    move = [MeasurementValue, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [MeasurementValueSource]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValueSourceTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "MeasurementValueSourceTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "MeasurementValues") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AccumulatorLimitSetTreeNode" class:
#------------------------------------------------------------------------------

class AccumulatorLimitSetTreeNode(TreeNode):
    """ Defines a tree node for a AccumulatorLimitSet.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.")

    # Name to use for a new instance.
    name = Str("AccumulatorLimitSet")

    # List of object classes than can be added or copied.
    add = [Accumulator, AccumulatorLimit, ]

    # List of object classes that can be moved.
    move = [Accumulator, AccumulatorLimit, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [AccumulatorLimitSet]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorLimitSetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "AccumulatorLimitSetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Measurements") )
        children.extend( getattr(object, "Limits") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AnalogLimitSetTreeNode" class:
#------------------------------------------------------------------------------

class AnalogLimitSetTreeNode(TreeNode):
    """ Defines a tree node for a AnalogLimitSet.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.")

    # Name to use for a new instance.
    name = Str("AnalogLimitSet")

    # List of object classes than can be added or copied.
    add = [AnalogLimit, Analog, ]

    # List of object classes that can be moved.
    move = [AnalogLimit, Analog, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [AnalogLimitSet]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AnalogLimitSetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "AnalogLimitSetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Limits") )
        children.extend( getattr(object, "Measurements") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CommandTreeNode" class:
#------------------------------------------------------------------------------

class CommandTreeNode(TreeNode):
    """ Defines a tree node for a Command.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A Command is a discrete control used for supervisory control.")

    # Name to use for a new instance.
    name = Str("Command")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Command]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CommandTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "CommandTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ValueAliasSet") )
        children.append( getattr(object, "MeasuredBy_Measurement") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AnalogTreeNode" class:
#------------------------------------------------------------------------------

class AnalogTreeNode(TreeNode):
    """ Defines a tree node for a Analog.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Analog represents an analog Measurement.")

    # Name to use for a new instance.
    name = Str("Analog")

    # List of object classes than can be added or copied.
    add = [AnalogValue, AnalogLimitSet, ]

    # List of object classes that can be moved.
    move = [AnalogValue, AnalogLimitSet, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Analog]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AnalogTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "AnalogTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contain_MeasurementValues") )
        children.extend( getattr(object, "LimitSets") )

        children.append( getattr(object, "ControlledBy_Control") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AccumulatorValueTreeNode" class:
#------------------------------------------------------------------------------

class AccumulatorValueTreeNode(TreeNode):
    """ Defines a tree node for a AccumulatorValue.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=AccumulatorValue represents a accumulated (counted) MeasurementValue.")

    # Name to use for a new instance.
    name = Str("AccumulatorValue")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [AccumulatorValue]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorValueTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "AccumulatorValueTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "MemberOf_Measurement") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SubLoadAreaTreeNode" class:
#------------------------------------------------------------------------------

class SubLoadAreaTreeNode(TreeNode):
    """ Defines a tree node for a SubLoadArea.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.")

    # Name to use for a new instance.
    name = Str("SubLoadArea")

    # List of object classes than can be added or copied.
    add = [LoadGroup, ]

    # List of object classes that can be moved.
    move = [LoadGroup, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SubLoadArea]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SubLoadAreaTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "SubLoadAreaTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "LoadGroups") )

        children.append( getattr(object, "LoadArea") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "LoadTreeNode" class:
#------------------------------------------------------------------------------

class LoadTreeNode(TreeNode):
    """ Defines a tree node for a Load.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.")

    # Name to use for a new instance.
    name = Str("Load")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Load]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "LoadTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "LoadTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "LoadResponseCharacteristicTreeNode" class:
#------------------------------------------------------------------------------

class LoadResponseCharacteristicTreeNode(TreeNode):
    """ Defines a tree node for a LoadResponseCharacteristic.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.")

    # Name to use for a new instance.
    name = Str("LoadResponseCharacteristic")

    # List of object classes than can be added or copied.
    add = [EnergyConsumer, ]

    # List of object classes that can be moved.
    move = [EnergyConsumer, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [LoadResponseCharacteristic]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "LoadResponseCharacteristicTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "LoadResponseCharacteristicTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "EnergyConsumer") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SeasonTreeNode" class:
#------------------------------------------------------------------------------

class SeasonTreeNode(TreeNode):
    """ Defines a tree node for a Season.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A specified time period of the year, e.g., Spring, Summer, Fall, Winter")

    # Name to use for a new instance.
    name = Str("Season")

    # List of object classes than can be added or copied.
    add = [SeasonDayTypeSchedule, ]

    # List of object classes that can be moved.
    move = [SeasonDayTypeSchedule, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Season]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SeasonTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "SeasonTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "SeasonDayTypeSchedules") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ConformLoadGroupTreeNode" class:
#------------------------------------------------------------------------------

class ConformLoadGroupTreeNode(TreeNode):
    """ Defines a tree node for a ConformLoadGroup.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Load that follows a daily and seasonal load variation pattern.")

    # Name to use for a new instance.
    name = Str("ConformLoadGroup")

    # List of object classes than can be added or copied.
    add = [ConformLoad, ConformLoadSchedule, ]

    # List of object classes that can be moved.
    move = [ConformLoad, ConformLoadSchedule, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ConformLoadGroup]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ConformLoadGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "EnergyConsumers") )
        children.extend( getattr(object, "ConformLoadSchedules") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ConformLoadTreeNode" class:
#------------------------------------------------------------------------------

class ConformLoadTreeNode(TreeNode):
    """ Defines a tree node for a ConformLoad.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.")

    # Name to use for a new instance.
    name = Str("ConformLoad")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ConformLoad]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ConformLoadTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "LoadGroup") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "LoadAreaTreeNode" class:
#------------------------------------------------------------------------------

class LoadAreaTreeNode(TreeNode):
    """ Defines a tree node for a LoadArea.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.")

    # Name to use for a new instance.
    name = Str("LoadArea")

    # List of object classes than can be added or copied.
    add = [SubLoadArea, ]

    # List of object classes that can be moved.
    move = [SubLoadArea, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [LoadArea]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "LoadAreaTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "LoadAreaTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "SubLoadAreas") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "PowerCutZoneTreeNode" class:
#------------------------------------------------------------------------------

class PowerCutZoneTreeNode(TreeNode):
    """ Defines a tree node for a PowerCutZone.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An area or zone of the power system which is used for load shedding purposes.")

    # Name to use for a new instance.
    name = Str("PowerCutZone")

    # List of object classes than can be added or copied.
    add = [EnergyConsumer, ]

    # List of object classes that can be moved.
    move = [EnergyConsumer, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [PowerCutZone]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "PowerCutZoneTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "PowerCutZoneTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "EnergyConsumers") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ConformLoadScheduleTreeNode" class:
#------------------------------------------------------------------------------

class ConformLoadScheduleTreeNode(TreeNode):
    """ Defines a tree node for a ConformLoadSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.")

    # Name to use for a new instance.
    name = Str("ConformLoadSchedule")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ConformLoadSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ConformLoadScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ConformLoadScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ConformLoadGroup") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "StationSupplyTreeNode" class:
#------------------------------------------------------------------------------

class StationSupplyTreeNode(TreeNode):
    """ Defines a tree node for a StationSupply.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Station supply with load derived from the station output.")

    # Name to use for a new instance.
    name = Str("StationSupply")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [StationSupply]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "StationSupplyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "StationSupplyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "DayTypeTreeNode" class:
#------------------------------------------------------------------------------

class DayTypeTreeNode(TreeNode):
    """ Defines a tree node for a DayType.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2")

    # Name to use for a new instance.
    name = Str("DayType")

    # List of object classes than can be added or copied.
    add = [SeasonDayTypeSchedule, ]

    # List of object classes that can be moved.
    move = [SeasonDayTypeSchedule, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [DayType]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "DayTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "DayTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "SeasonDayTypeSchedules") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "NonConformLoadScheduleTreeNode" class:
#------------------------------------------------------------------------------

class NonConformLoadScheduleTreeNode(TreeNode):
    """ Defines a tree node for a NonConformLoadSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)")

    # Name to use for a new instance.
    name = Str("NonConformLoadSchedule")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [NonConformLoadSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "NonConformLoadScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "NonConformLoadGroup") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CustomerLoadTreeNode" class:
#------------------------------------------------------------------------------

class CustomerLoadTreeNode(TreeNode):
    """ Defines a tree node for a CustomerLoad.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.")

    # Name to use for a new instance.
    name = Str("CustomerLoad")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CustomerLoad]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CustomerLoadTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "CustomerLoadTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "LoadGroupTreeNode" class:
#------------------------------------------------------------------------------

class LoadGroupTreeNode(TreeNode):
    """ Defines a tree node for a LoadGroup.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.")

    # Name to use for a new instance.
    name = Str("LoadGroup")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [LoadGroup]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "LoadGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "LoadGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "SubLoadArea") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "NonConformLoadGroupTreeNode" class:
#------------------------------------------------------------------------------

class NonConformLoadGroupTreeNode(TreeNode):
    """ Defines a tree node for a NonConformLoadGroup.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Loads that do not follow a daily and seasonal load variation pattern.")

    # Name to use for a new instance.
    name = Str("NonConformLoadGroup")

    # List of object classes than can be added or copied.
    add = [NonConformLoadSchedule, NonConformLoad, ]

    # List of object classes that can be moved.
    move = [NonConformLoadSchedule, NonConformLoad, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [NonConformLoadGroup]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "NonConformLoadGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "NonConformLoadSchedules") )
        children.extend( getattr(object, "EnergyConsumers") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EnergyAreaTreeNode" class:
#------------------------------------------------------------------------------

class EnergyAreaTreeNode(TreeNode):
    """ Defines a tree node for a EnergyArea.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The class describes an area having energy production or consumption. The class is the basis for further specialization.")

    # Name to use for a new instance.
    name = Str("EnergyArea")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [EnergyArea]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EnergyAreaTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "EnergyAreaTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ControlArea") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SeasonDayTypeScheduleTreeNode" class:
#------------------------------------------------------------------------------

class SeasonDayTypeScheduleTreeNode(TreeNode):
    """ Defines a tree node for a SeasonDayTypeSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.")

    # Name to use for a new instance.
    name = Str("SeasonDayTypeSchedule")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SeasonDayTypeSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SeasonDayTypeScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "SeasonDayTypeScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "DayType") )
        children.append( getattr(object, "Season") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "NonConformLoadTreeNode" class:
#------------------------------------------------------------------------------

class NonConformLoadTreeNode(TreeNode):
    """ Defines a tree node for a NonConformLoad.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.")

    # Name to use for a new instance.
    name = Str("NonConformLoad")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [NonConformLoad]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "NonConformLoadTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "NonConformLoadTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "LoadGroup") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "InductionMotorLoadTreeNode" class:
#------------------------------------------------------------------------------

class InductionMotorLoadTreeNode(TreeNode):
    """ Defines a tree node for a InductionMotorLoad.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).")

    # Name to use for a new instance.
    name = Str("InductionMotorLoad")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [InductionMotorLoad]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "InductionMotorLoadTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "InductionMotorLoadTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CurveTreeNode" class:
#------------------------------------------------------------------------------

class CurveTreeNode(TreeNode):
    """ Defines a tree node for a Curve.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.")

    # Name to use for a new instance.
    name = Str("Curve")

    # List of object classes than can be added or copied.
    add = [CurveData, ]

    # List of object classes that can be moved.
    move = [CurveData, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Curve]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "CurveTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "CurveScheduleDatas") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "VoltageLevelTreeNode" class:
#------------------------------------------------------------------------------

class VoltageLevelTreeNode(TreeNode):
    """ Defines a tree node for a VoltageLevel.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.")

    # Name to use for a new instance.
    name = Str("VoltageLevel")

    # List of object classes than can be added or copied.
    add = [Bay, ]

    # List of object classes that can be moved.
    move = [Bay, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [VoltageLevel]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "VoltageLevelTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "VoltageLevelTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contains_Bays") )

        children.append( getattr(object, "BaseVoltage") )
        children.append( getattr(object, "MemberOf_Substation") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ReportingGroupTreeNode" class:
#------------------------------------------------------------------------------

class ReportingGroupTreeNode(TreeNode):
    """ Defines a tree node for a ReportingGroup.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A reporting group is used for various ad-hoc groupings used for reporting.")

    # Name to use for a new instance.
    name = Str("ReportingGroup")

    # List of object classes than can be added or copied.
    add = [PowerSystemResource, BusNameMarker, TopologicalNode, ]

    # List of object classes that can be moved.
    move = [PowerSystemResource, BusNameMarker, TopologicalNode, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ReportingGroup]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ReportingGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ReportingGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "PowerSystemResource") )
        children.extend( getattr(object, "BusNameMarker") )
        children.extend( getattr(object, "TopologicalNode") )

        children.append( getattr(object, "ReportingSuperGroup") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ModelingAuthoritySetTreeNode" class:
#------------------------------------------------------------------------------

class ModelingAuthoritySetTreeNode(TreeNode):
    """ Defines a tree node for a ModelingAuthoritySet.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.")

    # Name to use for a new instance.
    name = Str("ModelingAuthoritySet")

    # List of object classes than can be added or copied.
    add = [IdentifiedObject, ]

    # List of object classes that can be moved.
    move = [IdentifiedObject, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ModelingAuthoritySet]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ModelingAuthoritySetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ModelingAuthoritySetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "IdentifiedObjects") )

        children.append( getattr(object, "ModelingAuthority") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "OperatingParticipantTreeNode" class:
#------------------------------------------------------------------------------

class OperatingParticipantTreeNode(TreeNode):
    """ Defines a tree node for a OperatingParticipant.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.")

    # Name to use for a new instance.
    name = Str("OperatingParticipant")

    # List of object classes than can be added or copied.
    add = [OperatingShare, ]

    # List of object classes that can be moved.
    move = [OperatingShare, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [OperatingParticipant]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "OperatingParticipantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "OperatingParticipantTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "OperatingShare") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ReportingSuperGroupTreeNode" class:
#------------------------------------------------------------------------------

class ReportingSuperGroupTreeNode(TreeNode):
    """ Defines a tree node for a ReportingSuperGroup.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A reporting super group, groups reporting groups for a higher level report.")

    # Name to use for a new instance.
    name = Str("ReportingSuperGroup")

    # List of object classes than can be added or copied.
    add = [ReportingGroup, ]

    # List of object classes that can be moved.
    move = [ReportingGroup, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ReportingSuperGroup]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ReportingSuperGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ReportingSuperGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "ReportingGroup") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SubstationTreeNode" class:
#------------------------------------------------------------------------------

class SubstationTreeNode(TreeNode):
    """ Defines a tree node for a Substation.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.")

    # Name to use for a new instance.
    name = Str("Substation")

    # List of object classes than can be added or copied.
    add = [VoltageLevel, Bay, ]

    # List of object classes that can be moved.
    move = [VoltageLevel, Bay, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Substation]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SubstationTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "SubstationTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contains_VoltageLevels") )
        children.extend( getattr(object, "Contains_Bays") )

        children.append( getattr(object, "Region") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ConductingEquipmentTreeNode" class:
#------------------------------------------------------------------------------

class ConductingEquipmentTreeNode(TreeNode):
    """ Defines a tree node for a ConductingEquipment.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.")

    # Name to use for a new instance.
    name = Str("ConductingEquipment")

    # List of object classes than can be added or copied.
    add = [Terminal, ProtectionEquipment, ClearanceTag, ]

    # List of object classes that can be moved.
    move = [Terminal, ProtectionEquipment, ClearanceTag, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ConductingEquipment]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ConductingEquipmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ConductingEquipmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Terminals") )
        children.extend( getattr(object, "ProtectionEquipments") )
        children.extend( getattr(object, "ClearanceTags") )

        children.append( getattr(object, "BaseVoltage") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "IrregularTimePointTreeNode" class:
#------------------------------------------------------------------------------

class IrregularTimePointTreeNode(TreeNode):
    """ Defines a tree node for a IrregularTimePoint.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=TimePoints for a schedule where the time between the points varies.")

    # Name to use for a new instance.
    name = Str("IrregularTimePoint")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [IrregularTimePoint]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "IrregularTimePointTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "IrregularTimePointTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "IntervalSchedule") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ConnectivityNodeContainerTreeNode" class:
#------------------------------------------------------------------------------

class ConnectivityNodeContainerTreeNode(TreeNode):
    """ Defines a tree node for a ConnectivityNodeContainer.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.")

    # Name to use for a new instance.
    name = Str("ConnectivityNodeContainer")

    # List of object classes than can be added or copied.
    add = [TopologicalNode, ConnectivityNode, ]

    # List of object classes that can be moved.
    move = [TopologicalNode, ConnectivityNode, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ConnectivityNodeContainer]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNodeContainerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ConnectivityNodeContainerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "TopologicalNode") )
        children.extend( getattr(object, "ConnectivityNodes") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "GeographicalRegionTreeNode" class:
#------------------------------------------------------------------------------

class GeographicalRegionTreeNode(TreeNode):
    """ Defines a tree node for a GeographicalRegion.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A geographical region of a power system network model.")

    # Name to use for a new instance.
    name = Str("GeographicalRegion")

    # List of object classes than can be added or copied.
    add = [SubGeographicalRegion, ]

    # List of object classes that can be moved.
    move = [SubGeographicalRegion, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [GeographicalRegion]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "GeographicalRegionTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "GeographicalRegionTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Regions") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "UnitTreeNode" class:
#------------------------------------------------------------------------------

class UnitTreeNode(TreeNode):
    """ Defines a tree node for a Unit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.")

    # Name to use for a new instance.
    name = Str("Unit")

    # List of object classes than can be added or copied.
    add = [Control, ProtectionEquipment, Measurement, ]

    # List of object classes that can be moved.
    move = [Control, ProtectionEquipment, Measurement, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Unit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "UnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "UnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Controls") )
        children.extend( getattr(object, "ProtectionEquipments") )
        children.extend( getattr(object, "Measurements") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EquipmentContainerTreeNode" class:
#------------------------------------------------------------------------------

class EquipmentContainerTreeNode(TreeNode):
    """ Defines a tree node for a EquipmentContainer.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A modeling construct to provide a root class for all Equipment classes")

    # Name to use for a new instance.
    name = Str("EquipmentContainer")

    # List of object classes than can be added or copied.
    add = [Equipment, ]

    # List of object classes that can be moved.
    move = [Equipment, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [EquipmentContainer]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EquipmentContainerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "EquipmentContainerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contains_Equipments") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ModelingAuthorityTreeNode" class:
#------------------------------------------------------------------------------

class ModelingAuthorityTreeNode(TreeNode):
    """ Defines a tree node for a ModelingAuthority.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model.")

    # Name to use for a new instance.
    name = Str("ModelingAuthority")

    # List of object classes than can be added or copied.
    add = [ModelingAuthoritySet, ]

    # List of object classes that can be moved.
    move = [ModelingAuthoritySet, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ModelingAuthority]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ModelingAuthorityTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ModelingAuthorityTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "ModelingAuthoritySets") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "BaseVoltageTreeNode" class:
#------------------------------------------------------------------------------

class BaseVoltageTreeNode(TreeNode):
    """ Defines a tree node for a BaseVoltage.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.")

    # Name to use for a new instance.
    name = Str("BaseVoltage")

    # List of object classes than can be added or copied.
    add = [ConductingEquipment, VoltageLevel, ]

    # List of object classes that can be moved.
    move = [ConductingEquipment, VoltageLevel, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [BaseVoltage]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "BaseVoltageTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "BaseVoltageTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "ConductingEquipment") )
        children.extend( getattr(object, "VoltageLevel") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "OperatingShareTreeNode" class:
#------------------------------------------------------------------------------

class OperatingShareTreeNode(TreeNode):
    """ Defines a tree node for a OperatingShare.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Specifies the contract relationship between a PowerSystemResource and a contract participant.")

    # Name to use for a new instance.
    name = Str("OperatingShare")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [OperatingShare]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "OperatingShareTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "OperatingShareTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "OperatingParticipant") )
        children.append( getattr(object, "PowerSystemResource") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "BasicIntervalScheduleTreeNode" class:
#------------------------------------------------------------------------------

class BasicIntervalScheduleTreeNode(TreeNode):
    """ Defines a tree node for a BasicIntervalSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Schedule of values at points in time.")

    # Name to use for a new instance.
    name = Str("BasicIntervalSchedule")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [BasicIntervalSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "BasicIntervalScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "BasicIntervalScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CurveDataTreeNode" class:
#------------------------------------------------------------------------------

class CurveDataTreeNode(TreeNode):
    """ Defines a tree node for a CurveData.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Data point values for defining a curve or schedule")

    # Name to use for a new instance.
    name = Str("CurveData")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CurveData]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CurveDataTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "CurveDataTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "CurveSchedule") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EquipmentTreeNode" class:
#------------------------------------------------------------------------------

class EquipmentTreeNode(TreeNode):
    """ Defines a tree node for a Equipment.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The parts of a power system that are physical devices, electronic or mechanical")

    # Name to use for a new instance.
    name = Str("Equipment")

    # List of object classes than can be added or copied.
    add = [OperationalLimitSet, ContingencyEquipment, ]

    # List of object classes that can be moved.
    move = [OperationalLimitSet, ContingencyEquipment, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Equipment]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EquipmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "EquipmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "OperationalLimitSet") )
        children.extend( getattr(object, "ContingencyEquipment") )

        children.append( getattr(object, "MemberOf_EquipmentContainer") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RegularIntervalScheduleTreeNode" class:
#------------------------------------------------------------------------------

class RegularIntervalScheduleTreeNode(TreeNode):
    """ Defines a tree node for a RegularIntervalSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The schedule has TimePoints where the time between them is constant.")

    # Name to use for a new instance.
    name = Str("RegularIntervalSchedule")

    # List of object classes than can be added or copied.
    add = [RegularTimePoint, ]

    # List of object classes that can be moved.
    move = [RegularTimePoint, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RegularIntervalSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RegularIntervalScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "RegularIntervalScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "TimePoints") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "IrregularIntervalScheduleTreeNode" class:
#------------------------------------------------------------------------------

class IrregularIntervalScheduleTreeNode(TreeNode):
    """ Defines a tree node for a IrregularIntervalSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The schedule has TimePoints where the time between them varies.")

    # Name to use for a new instance.
    name = Str("IrregularIntervalSchedule")

    # List of object classes than can be added or copied.
    add = [IrregularTimePoint, ]

    # List of object classes that can be moved.
    move = [IrregularTimePoint, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [IrregularIntervalSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "IrregularIntervalScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "IrregularIntervalScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "TimePoints") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "BayTreeNode" class:
#------------------------------------------------------------------------------

class BayTreeNode(TreeNode):
    """ Defines a tree node for a Bay.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.")

    # Name to use for a new instance.
    name = Str("Bay")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Bay]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "BayTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "BayTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "MemberOf_Substation") )
        children.append( getattr(object, "MemberOf_VoltageLevel") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RegularTimePointTreeNode" class:
#------------------------------------------------------------------------------

class RegularTimePointTreeNode(TreeNode):
    """ Defines a tree node for a RegularTimePoint.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=TimePoints for a schedule where the time between the points is constant.")

    # Name to use for a new instance.
    name = Str("RegularTimePoint")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RegularTimePoint]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RegularTimePointTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "RegularTimePointTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "IntervalSchedule") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "TerminalTreeNode" class:
#------------------------------------------------------------------------------

class TerminalTreeNode(TreeNode):
    """ Defines a tree node for a Terminal.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.")

    # Name to use for a new instance.
    name = Str("Terminal")

    # List of object classes than can be added or copied.
    add = [TieFlow, OperationalLimitSet, BranchGroupTerminal, RegulatingControl, Measurement, ]

    # List of object classes that can be moved.
    move = [TieFlow, OperationalLimitSet, BranchGroupTerminal, RegulatingControl, Measurement, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Terminal]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "TerminalTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "TerminalTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "TieFlow") )
        children.extend( getattr(object, "OperationalLimitSet") )
        children.extend( getattr(object, "BranchGroupTerminal") )
        children.extend( getattr(object, "RegulatingControl") )
        children.extend( getattr(object, "Measurements") )

        children.append( getattr(object, "ConductingEquipment") )
        children.append( getattr(object, "TopologicalNode") )
        children.append( getattr(object, "ConnectivityNode") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SubGeographicalRegionTreeNode" class:
#------------------------------------------------------------------------------

class SubGeographicalRegionTreeNode(TreeNode):
    """ Defines a tree node for a SubGeographicalRegion.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A subset of a geographical region of a power system network model.")

    # Name to use for a new instance.
    name = Str("SubGeographicalRegion")

    # List of object classes than can be added or copied.
    add = [Line, Substation, ]

    # List of object classes that can be moved.
    move = [Line, Substation, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SubGeographicalRegion]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SubGeographicalRegionTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "SubGeographicalRegionTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Lines") )
        children.extend( getattr(object, "Substations") )

        children.append( getattr(object, "Region") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "PowerSystemResourceTreeNode" class:
#------------------------------------------------------------------------------

class PowerSystemResourceTreeNode(TreeNode):
    """ Defines a tree node for a PowerSystemResource.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.")

    # Name to use for a new instance.
    name = Str("PowerSystemResource")

    # List of object classes than can be added or copied.
    add = [Company, ReportingGroup, OperatingShare, PsrList, Measurement, ]

    # List of object classes that can be moved.
    move = [Company, ReportingGroup, OperatingShare, PsrList, Measurement, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [PowerSystemResource]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "PowerSystemResourceTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "PowerSystemResourceTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "OperatedBy_Companies") )
        children.extend( getattr(object, "ReportingGroup") )
        children.extend( getattr(object, "OperatingShare") )
        children.extend( getattr(object, "PsrLists") )
        children.extend( getattr(object, "Contains_Measurements") )

        children.append( getattr(object, "PSRType") )
        children.append( getattr(object, "OutageSchedule") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "BasePowerTreeNode" class:
#------------------------------------------------------------------------------

class BasePowerTreeNode(TreeNode):
    """ Defines a tree node for a BasePower.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The BasePower class defines the base power used in the per unit calculations.")

    # Name to use for a new instance.
    name = Str("BasePower")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [BasePower]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "BasePowerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "BasePowerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "PSRTypeTreeNode" class:
#------------------------------------------------------------------------------

class PSRTypeTreeNode(TreeNode):
    """ Defines a tree node for a PSRType.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.")

    # Name to use for a new instance.
    name = Str("PSRType")

    # List of object classes than can be added or copied.
    add = [PowerSystemResource, ]

    # List of object classes that can be moved.
    move = [PowerSystemResource, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [PSRType]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "PSRTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "PSRTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "PowerSystemResource") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "PsrListTreeNode" class:
#------------------------------------------------------------------------------

class PsrListTreeNode(TreeNode):
    """ Defines a tree node for a PsrList.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation.")

    # Name to use for a new instance.
    name = Str("PsrList")

    # List of object classes than can be added or copied.
    add = [PowerSystemResource, ]

    # List of object classes that can be moved.
    move = [PowerSystemResource, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [PsrList]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "PsrListTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "PsrListTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "PowerSystemResources") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CompanyTreeNode" class:
#------------------------------------------------------------------------------

class CompanyTreeNode(TreeNode):
    """ Defines a tree node for a Company.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A company is a legal entity that owns and operates power system resources and is a party to interchange and transmission contracts.")

    # Name to use for a new instance.
    name = Str("Company")

    # List of object classes than can be added or copied.
    add = [PowerSystemResource, ]

    # List of object classes that can be moved.
    move = [PowerSystemResource, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Company]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CompanyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "CompanyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Operates_PSRs") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "IdentifiedObjectTreeNode" class:
#------------------------------------------------------------------------------

class IdentifiedObjectTreeNode(TreeNode):
    """ Defines a tree node for a IdentifiedObject.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=This is a root class to provide common naming attributes for all classes needing naming attributes")

    # Name to use for a new instance.
    name = Str("IdentifiedObject")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [IdentifiedObject]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "IdentifiedObjectTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "IdentifiedObjectTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ModelingAuthoritySet") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ContingencyTreeNode" class:
#------------------------------------------------------------------------------

class ContingencyTreeNode(TreeNode):
    """ Defines a tree node for a Contingency.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An event threatening system reliability, consisting of one or more contingency elements.")

    # Name to use for a new instance.
    name = Str("Contingency")

    # List of object classes than can be added or copied.
    add = [ContingencyElement, ]

    # List of object classes that can be moved.
    move = [ContingencyElement, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [Contingency]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ContingencyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ContingencyTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "ContingencyElement") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ContingencyEquipmentTreeNode" class:
#------------------------------------------------------------------------------

class ContingencyEquipmentTreeNode(TreeNode):
    """ Defines a tree node for a ContingencyEquipment.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A equipment to which the in service status is to change such as a power transformer or AC line segment.")

    # Name to use for a new instance.
    name = Str("ContingencyEquipment")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ContingencyEquipment]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ContingencyEquipmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ContingencyEquipmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Equipment") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ContingencyElementTreeNode" class:
#------------------------------------------------------------------------------

class ContingencyElementTreeNode(TreeNode):
    """ Defines a tree node for a ContingencyElement.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment.")

    # Name to use for a new instance.
    name = Str("ContingencyElement")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ContingencyElement]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ContingencyElementTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ContingencyElementTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Contingency") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ClearanceTagTypeTreeNode" class:
#------------------------------------------------------------------------------

class ClearanceTagTypeTreeNode(TreeNode):
    """ Defines a tree node for a ClearanceTagType.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.")

    # Name to use for a new instance.
    name = Str("ClearanceTagType")

    # List of object classes than can be added or copied.
    add = [ClearanceTag, ]

    # List of object classes that can be moved.
    move = [ClearanceTag, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ClearanceTagType]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ClearanceTagTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ClearanceTagTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "ClearanceTags") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SwitchingOperationTreeNode" class:
#------------------------------------------------------------------------------

class SwitchingOperationTreeNode(TreeNode):
    """ Defines a tree node for a SwitchingOperation.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.")

    # Name to use for a new instance.
    name = Str("SwitchingOperation")

    # List of object classes than can be added or copied.
    add = [Switch, ]

    # List of object classes that can be moved.
    move = [Switch, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SwitchingOperation]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SwitchingOperationTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "SwitchingOperationTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Switches") )

        children.append( getattr(object, "OutageSchedule") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "OutageScheduleTreeNode" class:
#------------------------------------------------------------------------------

class OutageScheduleTreeNode(TreeNode):
    """ Defines a tree node for a OutageSchedule.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.")

    # Name to use for a new instance.
    name = Str("OutageSchedule")

    # List of object classes than can be added or copied.
    add = [SwitchingOperation, ]

    # List of object classes that can be moved.
    move = [SwitchingOperation, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [OutageSchedule]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "OutageScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "OutageScheduleTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "SwitchingOperations") )

        children.append( getattr(object, "PSR") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ClearanceTagTreeNode" class:
#------------------------------------------------------------------------------

class ClearanceTagTreeNode(TreeNode):
    """ Defines a tree node for a ClearanceTag.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.")

    # Name to use for a new instance.
    name = Str("ClearanceTag")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ClearanceTag]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ClearanceTagTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ClearanceTagTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ConductingEquipment") )
        children.append( getattr(object, "ClearanceTagType") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RemotePointTreeNode" class:
#------------------------------------------------------------------------------

class RemotePointTreeNode(TreeNode):
    """ Defines a tree node for a RemotePoint.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.")

    # Name to use for a new instance.
    name = Str("RemotePoint")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RemotePoint]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RemotePointTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "RemotePointTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "MemberOf_RemoteUnit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RemoteControlTreeNode" class:
#------------------------------------------------------------------------------

class RemoteControlTreeNode(TreeNode):
    """ Defines a tree node for a RemoteControl.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Remote controls are ouputs that are sent by the remote unit to actuators in the process.")

    # Name to use for a new instance.
    name = Str("RemoteControl")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RemoteControl]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RemoteControlTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "RemoteControlTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Control") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RemoteSourceTreeNode" class:
#------------------------------------------------------------------------------

class RemoteSourceTreeNode(TreeNode):
    """ Defines a tree node for a RemoteSource.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Remote sources are state variables that are telemetered or calculated within the remote unit.")

    # Name to use for a new instance.
    name = Str("RemoteSource")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RemoteSource]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RemoteSourceTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "RemoteSourceTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "MeasurementValue") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CommunicationLinkTreeNode" class:
#------------------------------------------------------------------------------

class CommunicationLinkTreeNode(TreeNode):
    """ Defines a tree node for a CommunicationLink.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.")

    # Name to use for a new instance.
    name = Str("CommunicationLink")

    # List of object classes than can be added or copied.
    add = [RemoteUnit, ]

    # List of object classes that can be moved.
    move = [RemoteUnit, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CommunicationLink]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CommunicationLinkTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "CommunicationLinkTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Contain_RemoteUnits") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RemoteUnitTreeNode" class:
#------------------------------------------------------------------------------

class RemoteUnitTreeNode(TreeNode):
    """ Defines a tree node for a RemoteUnit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc.")

    # Name to use for a new instance.
    name = Str("RemoteUnit")

    # List of object classes than can be added or copied.
    add = [CommunicationLink, RemotePoint, ]

    # List of object classes that can be moved.
    move = [CommunicationLink, RemotePoint, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RemoteUnit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RemoteUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "RemoteUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "MemberOf_CommunicationLinks") )
        children.extend( getattr(object, "Contains_RemotePoints") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "OperationalLimitTreeNode" class:
#------------------------------------------------------------------------------

class OperationalLimitTreeNode(TreeNode):
    """ Defines a tree node for a OperationalLimit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A value associated with a specific kind of limit.")

    # Name to use for a new instance.
    name = Str("OperationalLimit")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [OperationalLimit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "OperationalLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "OperationalLimitType") )
        children.append( getattr(object, "OperationalLimitSet") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "BranchGroupTreeNode" class:
#------------------------------------------------------------------------------

class BranchGroupTreeNode(TreeNode):
    """ Defines a tree node for a BranchGroup.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network.")

    # Name to use for a new instance.
    name = Str("BranchGroup")

    # List of object classes than can be added or copied.
    add = [BranchGroupTerminal, ]

    # List of object classes that can be moved.
    move = [BranchGroupTerminal, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [BranchGroup]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "BranchGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "BranchGroupTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "BranchGroupTerminal") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "OperationalLimitTypeTreeNode" class:
#------------------------------------------------------------------------------

class OperationalLimitTypeTreeNode(TreeNode):
    """ Defines a tree node for a OperationalLimitType.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A type of limit.  The meaning of a specific limit is described in this class.")

    # Name to use for a new instance.
    name = Str("OperationalLimitType")

    # List of object classes than can be added or copied.
    add = [OperationalLimit, ]

    # List of object classes that can be moved.
    move = [OperationalLimit, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [OperationalLimitType]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "OperationalLimitTypeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "OperationalLimit") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ActivePowerLimitTreeNode" class:
#------------------------------------------------------------------------------

class ActivePowerLimitTreeNode(TreeNode):
    """ Defines a tree node for a ActivePowerLimit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Limit on active power flow.")

    # Name to use for a new instance.
    name = Str("ActivePowerLimit")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ActivePowerLimit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ActivePowerLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ActivePowerLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CurrentLimitTreeNode" class:
#------------------------------------------------------------------------------

class CurrentLimitTreeNode(TreeNode):
    """ Defines a tree node for a CurrentLimit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Operational limit on current.")

    # Name to use for a new instance.
    name = Str("CurrentLimit")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CurrentLimit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CurrentLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "CurrentLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "OperationalLimitSetTreeNode" class:
#------------------------------------------------------------------------------

class OperationalLimitSetTreeNode(TreeNode):
    """ Defines a tree node for a OperationalLimitSet.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.")

    # Name to use for a new instance.
    name = Str("OperationalLimitSet")

    # List of object classes than can be added or copied.
    add = [OperationalLimit, ]

    # List of object classes that can be moved.
    move = [OperationalLimit, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [OperationalLimitSet]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitSetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "OperationalLimitSetTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "OperationalLimitValue") )

        children.append( getattr(object, "Terminal") )
        children.append( getattr(object, "Equipment") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "VoltageLimitTreeNode" class:
#------------------------------------------------------------------------------

class VoltageLimitTreeNode(TreeNode):
    """ Defines a tree node for a VoltageLimit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Operational limit applied to voltage.")

    # Name to use for a new instance.
    name = Str("VoltageLimit")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [VoltageLimit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "VoltageLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "VoltageLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "BranchGroupTerminalTreeNode" class:
#------------------------------------------------------------------------------

class BranchGroupTerminalTreeNode(TreeNode):
    """ Defines a tree node for a BranchGroupTerminal.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A specific directed terminal flow for a branch group.")

    # Name to use for a new instance.
    name = Str("BranchGroupTerminal")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [BranchGroupTerminal]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "BranchGroupTerminalTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "BranchGroupTerminalTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "BranchGroup") )
        children.append( getattr(object, "Terminal") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ApparentPowerLimitTreeNode" class:
#------------------------------------------------------------------------------

class ApparentPowerLimitTreeNode(TreeNode):
    """ Defines a tree node for a ApparentPowerLimit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Apparent power limit.")

    # Name to use for a new instance.
    name = Str("ApparentPowerLimit")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ApparentPowerLimit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ApparentPowerLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "ApparentPowerLimitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ControlAreaGeneratingUnitTreeNode" class:
#------------------------------------------------------------------------------

class ControlAreaGeneratingUnitTreeNode(TreeNode):
    """ Defines a tree node for a ControlAreaGeneratingUnit.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.")

    # Name to use for a new instance.
    name = Str("ControlAreaGeneratingUnit")

    # List of object classes than can be added or copied.
    add = [AltGeneratingUnitMeas, ]

    # List of object classes that can be moved.
    move = [AltGeneratingUnitMeas, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ControlAreaGeneratingUnit]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ControlAreaGeneratingUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ControlAreaGeneratingUnitTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "AltGeneratingUnitMeas") )

        children.append( getattr(object, "GeneratingUnit") )
        children.append( getattr(object, "ControlArea") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ControlAreaTreeNode" class:
#------------------------------------------------------------------------------

class ControlAreaTreeNode(TreeNode):
    """ Defines a tree node for a ControlArea.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.")

    # Name to use for a new instance.
    name = Str("ControlArea")

    # List of object classes than can be added or copied.
    add = [BusNameMarker, TopologicalNode, ControlAreaGeneratingUnit, TieFlow, ]

    # List of object classes that can be moved.
    move = [BusNameMarker, TopologicalNode, ControlAreaGeneratingUnit, TieFlow, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ControlArea]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ControlAreaTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ControlAreaTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "BusNameMarker") )
        children.extend( getattr(object, "TopologicalNode") )
        children.extend( getattr(object, "ControlAreaGeneratingUnit") )
        children.extend( getattr(object, "TieFlow") )

        children.append( getattr(object, "EnergyArea") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AltGeneratingUnitMeasTreeNode" class:
#------------------------------------------------------------------------------

class AltGeneratingUnitMeasTreeNode(TreeNode):
    """ Defines a tree node for a AltGeneratingUnitMeas.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A prioritized measurement to be used for the generating unit in the control area specificaiton.")

    # Name to use for a new instance.
    name = Str("AltGeneratingUnitMeas")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [AltGeneratingUnitMeas]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AltGeneratingUnitMeasTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "AltGeneratingUnitMeasTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "ControlAreaGeneratingUnit") )
        children.append( getattr(object, "AnalogValue") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "TieFlowTreeNode" class:
#------------------------------------------------------------------------------

class TieFlowTreeNode(TreeNode):
    """ Defines a tree node for a TieFlow.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A flow specification in terms of location and direction for a control area.")

    # Name to use for a new instance.
    name = Str("TieFlow")

    # List of object classes than can be added or copied.
    add = [AltTieMeas, ]

    # List of object classes that can be moved.
    move = [AltTieMeas, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [TieFlow]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "TieFlowTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "TieFlowTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "AltTieMeas") )

        children.append( getattr(object, "Terminal") )
        children.append( getattr(object, "ControlArea") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "AltTieMeasTreeNode" class:
#------------------------------------------------------------------------------

class AltTieMeasTreeNode(TreeNode):
    """ Defines a tree node for a AltTieMeas.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A prioritized measurement to be used for the tie flow as part of the control area specification.")

    # Name to use for a new instance.
    name = Str("AltTieMeas")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [AltTieMeas]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "AltTieMeasTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "AltTieMeasTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "TieFlow") )
        children.append( getattr(object, "AnalogValue") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EquivalentBranchTreeNode" class:
#------------------------------------------------------------------------------

class EquivalentBranchTreeNode(TreeNode):
    """ Defines a tree node for a EquivalentBranch.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The class represents equivalent branches.")

    # Name to use for a new instance.
    name = Str("EquivalentBranch")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [EquivalentBranch]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EquivalentBranchTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "EquivalentBranchTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EquivalentShuntTreeNode" class:
#------------------------------------------------------------------------------

class EquivalentShuntTreeNode(TreeNode):
    """ Defines a tree node for a EquivalentShunt.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The class represents equivalent shunts.")

    # Name to use for a new instance.
    name = Str("EquivalentShunt")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [EquivalentShunt]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EquivalentShuntTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "EquivalentShuntTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EquivalentNetworkTreeNode" class:
#------------------------------------------------------------------------------

class EquivalentNetworkTreeNode(TreeNode):
    """ Defines a tree node for a EquivalentNetwork.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.")

    # Name to use for a new instance.
    name = Str("EquivalentNetwork")

    # List of object classes than can be added or copied.
    add = [EquivalentEquipment, ]

    # List of object classes that can be moved.
    move = [EquivalentEquipment, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [EquivalentNetwork]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EquivalentNetworkTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "EquivalentNetworkTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "EquivalentEquipments") )

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "EquivalentEquipmentTreeNode" class:
#------------------------------------------------------------------------------

class EquivalentEquipmentTreeNode(TreeNode):
    """ Defines a tree node for a EquivalentEquipment.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.")

    # Name to use for a new instance.
    name = Str("EquivalentEquipment")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [EquivalentEquipment]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "EquivalentEquipmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "EquivalentEquipmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "EquivalentNetwork") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "TopologicalNodeTreeNode" class:
#------------------------------------------------------------------------------

class TopologicalNodeTreeNode(TreeNode):
    """ Defines a tree node for a TopologicalNode.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).")

    # Name to use for a new instance.
    name = Str("TopologicalNode")

    # List of object classes than can be added or copied.
    add = [ConnectivityNode, Terminal, ]

    # List of object classes that can be moved.
    move = [ConnectivityNode, Terminal, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [TopologicalNode]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "TopologicalNodeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "TopologicalNodeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "ConnectivityNodes") )
        children.extend( getattr(object, "Terminal") )

        children.append( getattr(object, "ReportingGroup") )
        children.append( getattr(object, "AngleRef_TopologicalIsland") )
        children.append( getattr(object, "ConnectivityNodeContainer") )
        children.append( getattr(object, "TopologicalIsland") )
        children.append( getattr(object, "ControlArea") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "TopologicalIslandTreeNode" class:
#------------------------------------------------------------------------------

class TopologicalIslandTreeNode(TreeNode):
    """ Defines a tree node for a TopologicalIsland.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).")

    # Name to use for a new instance.
    name = Str("TopologicalIsland")

    # List of object classes than can be added or copied.
    add = [TopologicalNode, ]

    # List of object classes that can be moved.
    move = [TopologicalNode, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [TopologicalIsland]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "TopologicalIslandTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "TopologicalIslandTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "TopologicalNodes") )

        children.append( getattr(object, "AngleRef_TopologicalNode") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ConnectivityNodeTreeNode" class:
#------------------------------------------------------------------------------

class ConnectivityNodeTreeNode(TreeNode):
    """ Defines a tree node for a ConnectivityNode.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.")

    # Name to use for a new instance.
    name = Str("ConnectivityNode")

    # List of object classes than can be added or copied.
    add = [Terminal, ]

    # List of object classes that can be moved.
    move = [Terminal, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ConnectivityNode]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNodeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ConnectivityNodeTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Terminals") )

        children.append( getattr(object, "MemberOf_EquipmentContainer") )
        children.append( getattr(object, "BusNameMarker") )
        children.append( getattr(object, "TopologicalNode") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "BusNameMarkerTreeNode" class:
#------------------------------------------------------------------------------

class BusNameMarkerTreeNode(TreeNode):
    """ Defines a tree node for a BusNameMarker.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.")

    # Name to use for a new instance.
    name = Str("BusNameMarker")

    # List of object classes than can be added or copied.
    add = [ConnectivityNode, ]

    # List of object classes that can be moved.
    move = [ConnectivityNode, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [BusNameMarker]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "BusNameMarkerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "BusNameMarkerTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "ConnectivityNode") )

        children.append( getattr(object, "ControlArea") )
        children.append( getattr(object, "ReportingGroup") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "SynchrocheckRelayTreeNode" class:
#------------------------------------------------------------------------------

class SynchrocheckRelayTreeNode(TreeNode):
    """ Defines a tree node for a SynchrocheckRelay.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.")

    # Name to use for a new instance.
    name = Str("SynchrocheckRelay")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [SynchrocheckRelay]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "SynchrocheckRelayTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "SynchrocheckRelayTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "ProtectionEquipmentTreeNode" class:
#------------------------------------------------------------------------------

class ProtectionEquipmentTreeNode(TreeNode):
    """ Defines a tree node for a ProtectionEquipment.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.")

    # Name to use for a new instance.
    name = Str("ProtectionEquipment")

    # List of object classes than can be added or copied.
    add = [ProtectedSwitch, ConductingEquipment, ]

    # List of object classes that can be moved.
    move = [ProtectedSwitch, ConductingEquipment, ]

    # List of object classes and/or interfaces that the node applies to.
    node_for = [ProtectionEquipment]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "ProtectionEquipmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of group item icon.
    icon_group = Str( '<group>' )

    # Name of opened group item icon.
    icon_open = Str( '<open>' )
    #--------------------------------------------------------------------------
    #  End "ProtectionEquipmentTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []
        children.extend( getattr(object, "Operates_Breakers") )
        children.extend( getattr(object, "ConductingEquipments") )

        children.append( getattr(object, "Unit") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "CurrentRelayTreeNode" class:
#------------------------------------------------------------------------------

class CurrentRelayTreeNode(TreeNode):
    """ Defines a tree node for a CurrentRelay.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A device that checks current flow values in any direction or designated direction")

    # Name to use for a new instance.
    name = Str("CurrentRelay")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [CurrentRelay]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "CurrentRelayTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "CurrentRelayTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return False

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True
#------------------------------------------------------------------------------
#  "RecloseSequenceTreeNode" class:
#------------------------------------------------------------------------------

class RecloseSequenceTreeNode(TreeNode):
    """ Defines a tree node for a RecloseSequence.
    """

    #--------------------------------------------------------------------------
    #  "TreeNode" interface:
    #--------------------------------------------------------------------------

    # Name of trait containing children (if '', the node is a leaf).
#    children = Str("Substations")

    # Name of a trait containing a label.
    label = Str("name")

    tooltip = Str("=A reclose sequence (open and close) is defined for each possible reclosure of a breaker.")

    # Name to use for a new instance.
    name = Str("RecloseSequence")

    # List of object classes than can be added or copied.
    add = []

    # List of object classes that can be moved.
    move = []

    # List of object classes and/or interfaces that the node applies to.
    node_for = [RecloseSequence]

    # Function for handling double-clicking an object.
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")

    # Resource path used to locate the node icon.
    icon_path = Str(IMAGE_PATH)

    #--------------------------------------------------------------------------
    #  Begin "RecloseSequenceTreeNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    # Name of leaf item icon.
    icon_item = Str( '<item>' )
    #--------------------------------------------------------------------------
    #  End "RecloseSequenceTreeNode" user definitions:
    #--------------------------------------------------------------------------

    def allows_children ( self, object ):
        """ Returns whether this object can have children.
        """
        return True

    def get_children ( self, object ):
        """ Gets the object's children.
        """
        children = []

        children.append( getattr(object, "Breaker") )
        return children


    def append_child ( self, object, child ):
        """ Appends a child to the object's children.
        """
        raise NotImplmentedError


    def dclick ( self, object ):
        """ Handles an object being double-clicked.
        """
        if object is not None:
            object.edit_traits(kind="livemodal")
            return None

        return True

#------------------------------------------------------------------------------
#  Tree node list:
#------------------------------------------------------------------------------


tree_nodes = [
    ElementTreeNode(),
    CommonInformationModelTreeNode(),
    IEC61970CIMVersionTreeNode(),
    MutualCouplingTreeNode(),
    Quality61850TreeNode(),
    MeasurementValueQualityTreeNode(),
    AnalogTreeNode(),
    AccumulatorValueTreeNode(),
    SeasonTreeNode(),
    IrregularTimePointTreeNode(),
    OperatingShareTreeNode(),
    CurveDataTreeNode(),
    RegularTimePointTreeNode(),
    IdentifiedObjectTreeNode(),
    ContingencyTreeNode(),
    ContingencyElementTreeNode(),
    ClearanceTagTypeTreeNode(),
    SwitchingOperationTreeNode(),
    ClearanceTagTreeNode(),
    RemotePointTreeNode(),
    RemoteControlTreeNode(),
    RemoteSourceTreeNode(),
    OperationalLimitTreeNode(),
    BranchGroupTreeNode(),
    OperationalLimitTypeTreeNode(),
    ActivePowerLimitTreeNode(),
    CurrentLimitTreeNode(),
    OperationalLimitSetTreeNode(),
    VoltageLimitTreeNode(),
    BranchGroupTerminalTreeNode(),
    ApparentPowerLimitTreeNode(),
    ControlAreaGeneratingUnitTreeNode(),
    AltGeneratingUnitMeasTreeNode(),
    TieFlowTreeNode(),
    AltTieMeasTreeNode(),
    TopologicalNodeTreeNode(),
    TopologicalIslandTreeNode(),
    ConnectivityNodeTreeNode(),
    BusNameMarkerTreeNode(),
    RecloseSequenceTreeNode(),
    GroundDisconnectorTreeNode(),
    WireTypeTreeNode(),
    ProtectedSwitchTreeNode(),
    JumperTreeNode(),
    WireArrangementTreeNode(),
    FuseTreeNode(),
    WindingTestTreeNode(),
    DisconnectorTreeNode(),
    ConductorTypeTreeNode(),
    ReactiveCapabilityCurveTreeNode(),
    NuclearGeneratingUnitTreeNode(),
    StartIgnFuelCurveTreeNode(),
    HydroGeneratingEfficiencyCurveTreeNode(),
    TargetLevelScheduleTreeNode(),
    GrossToNetActivePowerCurveTreeNode(),
    IncrementalHeatRateCurveTreeNode(),
    HeatInputCurveTreeNode(),
    StartRampCurveTreeNode(),
    ShutdownCurveTreeNode(),
    StartupModelTreeNode(),
    EmissionCurveTreeNode(),
    GenUnitOpCostCurveTreeNode(),
    HydroGeneratingUnitTreeNode(),
    LevelVsVolumeCurveTreeNode(),
    ThermalGeneratingUnitTreeNode(),
    FossilFuelTreeNode(),
    FuelAllocationScheduleTreeNode(),
    EmissionAccountTreeNode(),
    TailbayLossCurveTreeNode(),
    PenstockLossCurveTreeNode(),
    StartMainFuelCurveTreeNode(),
    HeatRateCurveTreeNode(),
    CTTempActivePowerCurveTreeNode(),
    DiscreteTreeNode(),
    MeasurementTreeNode(),
    SetPointTreeNode(),
    ControlTreeNode(),
    ControlTypeTreeNode(),
    DiscreteValueTreeNode(),
    AccumulatorTreeNode(),
    LimitSetTreeNode(),
    AnalogLimitTreeNode(),
    MeasurementValueTreeNode(),
    ValueAliasSetTreeNode(),
    StringMeasurementValueTreeNode(),
    LimitTreeNode(),
    MeasurementTypeTreeNode(),
    AccumulatorLimitTreeNode(),
    StringMeasurementTreeNode(),
    ValueToAliasTreeNode(),
    AnalogValueTreeNode(),
    MeasurementValueSourceTreeNode(),
    AccumulatorLimitSetTreeNode(),
    AnalogLimitSetTreeNode(),
    CommandTreeNode(),
    LoadResponseCharacteristicTreeNode(),
    DayTypeTreeNode(),
    LoadGroupTreeNode(),
    NonConformLoadGroupTreeNode(),
    EnergyAreaTreeNode(),
    InductionMotorLoadTreeNode(),
    CurveTreeNode(),
    ReportingGroupTreeNode(),
    ModelingAuthoritySetTreeNode(),
    OperatingParticipantTreeNode(),
    ReportingSuperGroupTreeNode(),
    GeographicalRegionTreeNode(),
    UnitTreeNode(),
    ModelingAuthorityTreeNode(),
    BaseVoltageTreeNode(),
    BasicIntervalScheduleTreeNode(),
    RegularIntervalScheduleTreeNode(),
    IrregularIntervalScheduleTreeNode(),
    TerminalTreeNode(),
    SubGeographicalRegionTreeNode(),
    PowerSystemResourceTreeNode(),
    BasePowerTreeNode(),
    PSRTypeTreeNode(),
    PsrListTreeNode(),
    CompanyTreeNode(),
    ContingencyEquipmentTreeNode(),
    OutageScheduleTreeNode(),
    CommunicationLinkTreeNode(),
    RemoteUnitTreeNode(),
    ControlAreaTreeNode(),
    ProtectionEquipmentTreeNode(),
    CurrentRelayTreeNode(),
    RegulationScheduleTreeNode(),
    BreakerTreeNode(),
    VoltageControlZoneTreeNode(),
    LoadBreakSwitchTreeNode(),
    DCLineSegmentTreeNode(),
    TapChangerTreeNode(),
    CompositeSwitchTreeNode(),
    PowerTransformerTreeNode(),
    ACLineSegmentTreeNode(),
    HeatExchangerTreeNode(),
    RegulatingControlTreeNode(),
    GeneratingUnitTreeNode(),
    AirCompressorTreeNode(),
    CombinedCyclePlantTreeNode(),
    HydroPumpTreeNode(),
    HydroPowerPlantTreeNode(),
    CAESPlantTreeNode(),
    InflowForecastTreeNode(),
    SteamSendoutScheduleTreeNode(),
    ReservoirTreeNode(),
    HydroPumpOpScheduleTreeNode(),
    GenUnitOpScheduleTreeNode(),
    CogenerationPlantTreeNode(),
    PrimeMoverTreeNode(),
    CombustionTurbineTreeNode(),
    HydroTurbineTreeNode(),
    SteamSupplyTreeNode(),
    SubLoadAreaTreeNode(),
    LoadTreeNode(),
    ConformLoadGroupTreeNode(),
    LoadAreaTreeNode(),
    PowerCutZoneTreeNode(),
    CustomerLoadTreeNode(),
    SeasonDayTypeScheduleTreeNode(),
    ConductingEquipmentTreeNode(),
    ConnectivityNodeContainerTreeNode(),
    EquipmentContainerTreeNode(),
    EquipmentTreeNode(),
    BayTreeNode(),
    EquivalentNetworkTreeNode(),
    EquivalentEquipmentTreeNode(),
    SynchrocheckRelayTreeNode(),
    TransformerWindingTreeNode(),
    EnergySourceTreeNode(),
    SeriesCompensatorTreeNode(),
    RegulatingCondEqTreeNode(),
    ConductorTreeNode(),
    LineTreeNode(),
    GroundTreeNode(),
    ShuntCompensatorTreeNode(),
    RectifierInverterTreeNode(),
    EnergyConsumerTreeNode(),
    SwitchTreeNode(),
    SynchronousMachineTreeNode(),
    ConnectorTreeNode(),
    StaticVarCompensatorTreeNode(),
    JunctionTreeNode(),
    PlantTreeNode(),
    SteamTurbineTreeNode(),
    PWRSteamSupplyTreeNode(),
    BWRSteamSupplyTreeNode(),
    FossilSteamSupplyTreeNode(),
    SubcriticalTreeNode(),
    ConformLoadTreeNode(),
    ConformLoadScheduleTreeNode(),
    StationSupplyTreeNode(),
    NonConformLoadScheduleTreeNode(),
    NonConformLoadTreeNode(),
    VoltageLevelTreeNode(),
    SubstationTreeNode(),
    EquivalentBranchTreeNode(),
    EquivalentShuntTreeNode(),
    FrequencyConverterTreeNode(),
    BusbarSectionTreeNode(),
    SupercriticalTreeNode(),
    HeatRecoveryBoilerTreeNode(),
    DrumBoilerTreeNode(),
]
tree_nodes.reverse()

#------------------------------------------------------------------------------
#  CIM13r19 Tree Editor:
#------------------------------------------------------------------------------

cim13r19_tree_editor = TreeEditor(nodes=tree_nodes, editable=True)

# EOF -------------------------------------------------------------------------
