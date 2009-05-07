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

""" Defines adapters for implementing the ITreeNode interface.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasTraits, Property, Instance, adapts

from enthought.traits.ui.api \
    import View, Item, Group, ITreeNode, ITreeNodeAdapter, TreeEditor

from enthought.traits.ui.menu \
    import Action, Menu

from CIM13 import *
from CIM13.Wires import *
from CIM13.Generation import *
from CIM13.Meas import *
from CIM13.LoadModel import *
from CIM13.Core import *
from CIM13.Contingency import *
from CIM13.Outage import *
from CIM13.SCADA import *
from CIM13.Domain import *
from CIM13.OperationalLimits import *
from CIM13.ControlArea import *
from CIM13.Equivalents import *
from CIM13.Topology import *
from CIM13.Protection import *
from CIM13.Generation.Production import *
from CIM13.Generation.GenerationDynamics import *

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

IMAGE_PATH = ""

#------------------------------------------------------------------------------
#  "RootAdapter" class:
#------------------------------------------------------------------------------

class RootAdapter(ITreeNodeAdapter):
    """ Adapts a Root to implement the ITreeNode interface.
    """

    adapts(Root, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return ""


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Root'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ModelAdapter" class:
#------------------------------------------------------------------------------

class ModelAdapter(ITreeNodeAdapter):
    """ Adapts a Model to implement the ITreeNode interface.
    """

    adapts(Model, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contains", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contains", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return ""


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Model'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Root, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contains", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "IEC61970CIMVersionAdapter" class:
#------------------------------------------------------------------------------

class IEC61970CIMVersionAdapter(ITreeNodeAdapter):
    """ Adapts a IEC61970CIMVersion to implement the ITreeNode interface.
    """

    adapts(IEC61970CIMVersion, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "This is the IEC 61970 CIM version number assigned to this UML model file."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'IEC61970CIMVersion'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RegulationScheduleAdapter" class:
#------------------------------------------------------------------------------

class RegulationScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a RegulationSchedule to implement the ITreeNode interface.
    """

    adapts(RegulationSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["RegulatingControl", "VoltageControlZones", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["RegulatingControl", "VoltageControlZones", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'RegulatingControl',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'VoltageControlZones',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'RegulatingControl',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'VoltageControlZones',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A pre-established pattern over time for a controlled variable, e.g., busbar voltage."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RegulationSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (RegulatingControl, VoltageControlZone, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["RegulatingControl", "VoltageControlZones", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "GroundDisconnectorAdapter" class:
#------------------------------------------------------------------------------

class GroundDisconnectorAdapter(ITreeNodeAdapter):
    """ Adapts a GroundDisconnector to implement the ITreeNode interface.
    """

    adapts(GroundDisconnector, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A manually operated or motor operated mechanical switching device used for isolating a circuit or equipment from Ground."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'GroundDisconnector'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "TransformerWindingAdapter" class:
#------------------------------------------------------------------------------

class TransformerWindingAdapter(ITreeNodeAdapter):
    """ Adapts a TransformerWinding to implement the ITreeNode interface.
    """

    adapts(TransformerWinding, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["To_WindingTest", "From_WindingTest", "TapChangers", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["To_WindingTest", "From_WindingTest", "TapChangers", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'To_WindingTest',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'From_WindingTest',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TapChangers',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'To_WindingTest',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'From_WindingTest',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TapChangers',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A winding is associated with each defined terminal of a transformer (or phase shifter)."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'TransformerWinding'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (WindingTest, WindingTest, TapChanger, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["To_WindingTest", "From_WindingTest", "TapChangers", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EnergySourceAdapter" class:
#------------------------------------------------------------------------------

class EnergySourceAdapter(ITreeNodeAdapter):
    """ Adapts a EnergySource to implement the ITreeNode interface.
    """

    adapts(EnergySource, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A generic equivalent for an energy supplier on a transmission or distribution voltage level."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'EnergySource'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SeriesCompensatorAdapter" class:
#------------------------------------------------------------------------------

class SeriesCompensatorAdapter(ITreeNodeAdapter):
    """ Adapts a SeriesCompensator to implement the ITreeNode interface.
    """

    adapts(SeriesCompensator, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SeriesCompensator'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "WireTypeAdapter" class:
#------------------------------------------------------------------------------

class WireTypeAdapter(ITreeNodeAdapter):
    """ Adapts a WireType to implement the ITreeNode interface.
    """

    adapts(WireType, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["WireArrangements", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["WireArrangements", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'WireArrangements',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'WireArrangements',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'WireType'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (WireArrangement, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["WireArrangements", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "BreakerAdapter" class:
#------------------------------------------------------------------------------

class BreakerAdapter(ITreeNodeAdapter):
    """ Adapts a Breaker to implement the ITreeNode interface.
    """

    adapts(Breaker, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Breaker'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "VoltageControlZoneAdapter" class:
#------------------------------------------------------------------------------

class VoltageControlZoneAdapter(ITreeNodeAdapter):
    """ Adapts a VoltageControlZone to implement the ITreeNode interface.
    """

    adapts(VoltageControlZone, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'VoltageControlZone'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "FrequencyConverterAdapter" class:
#------------------------------------------------------------------------------

class FrequencyConverterAdapter(ITreeNodeAdapter):
    """ Adapts a FrequencyConverter to implement the ITreeNode interface.
    """

    adapts(FrequencyConverter, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'FrequencyConverter'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RegulatingCondEqAdapter" class:
#------------------------------------------------------------------------------

class RegulatingCondEqAdapter(ITreeNodeAdapter):
    """ Adapts a RegulatingCondEq to implement the ITreeNode interface.
    """

    adapts(RegulatingCondEq, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Controls", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Controls", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Controls',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Controls',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RegulatingCondEq'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Control, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Controls", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ConductorAdapter" class:
#------------------------------------------------------------------------------

class ConductorAdapter(ITreeNodeAdapter):
    """ Adapts a Conductor to implement the ITreeNode interface.
    """

    adapts(Conductor, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Conductor'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "LoadBreakSwitchAdapter" class:
#------------------------------------------------------------------------------

class LoadBreakSwitchAdapter(ITreeNodeAdapter):
    """ Adapts a LoadBreakSwitch to implement the ITreeNode interface.
    """

    adapts(LoadBreakSwitch, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'LoadBreakSwitch'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ProtectedSwitchAdapter" class:
#------------------------------------------------------------------------------

class ProtectedSwitchAdapter(ITreeNodeAdapter):
    """ Adapts a ProtectedSwitch to implement the ITreeNode interface.
    """

    adapts(ProtectedSwitch, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["OperatedBy_ProtectionEquipments", "RecloseSequences", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["OperatedBy_ProtectionEquipments", "RecloseSequences", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperatedBy_ProtectionEquipments',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'RecloseSequences',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperatedBy_ProtectionEquipments',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'RecloseSequences',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ProtectedSwitch'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ProtectionEquipment, RecloseSequence, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["OperatedBy_ProtectionEquipments", "RecloseSequences", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "LineAdapter" class:
#------------------------------------------------------------------------------

class LineAdapter(ITreeNodeAdapter):
    """ Adapts a Line to implement the ITreeNode interface.
    """

    adapts(Line, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Line'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "GroundAdapter" class:
#------------------------------------------------------------------------------

class GroundAdapter(ITreeNodeAdapter):
    """ Adapts a Ground to implement the ITreeNode interface.
    """

    adapts(Ground, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Ground'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "JumperAdapter" class:
#------------------------------------------------------------------------------

class JumperAdapter(ITreeNodeAdapter):
    """ Adapts a Jumper to implement the ITreeNode interface.
    """

    adapts(Jumper, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A short section of conductor with negligible impedance which can be manually removed and replaced if the circuit is de-energized. Note that zero-impedance branches can be modelled by an ACLineSegment with a zero impedance ConductorType"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Jumper'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "DCLineSegmentAdapter" class:
#------------------------------------------------------------------------------

class DCLineSegmentAdapter(ITreeNodeAdapter):
    """ Adapts a DCLineSegment to implement the ITreeNode interface.
    """

    adapts(DCLineSegment, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'DCLineSegment'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "TapChangerAdapter" class:
#------------------------------------------------------------------------------

class TapChangerAdapter(ITreeNodeAdapter):
    """ Adapts a TapChanger to implement the ITreeNode interface.
    """

    adapts(TapChanger, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Mechanism for changing transformer winding tap positions."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'TapChanger'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CompositeSwitchAdapter" class:
#------------------------------------------------------------------------------

class CompositeSwitchAdapter(ITreeNodeAdapter):
    """ Adapts a CompositeSwitch to implement the ITreeNode interface.
    """

    adapts(CompositeSwitch, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Switches", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Switches", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Switches',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Switches',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CompositeSwitch'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Switch, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Switches", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "WireArrangementAdapter" class:
#------------------------------------------------------------------------------

class WireArrangementAdapter(ITreeNodeAdapter):
    """ Adapts a WireArrangement to implement the ITreeNode interface.
    """

    adapts(WireArrangement, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Identification, spacing and configuration of the wires of a ConductorType, with reference to their type."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'WireArrangement'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "PowerTransformerAdapter" class:
#------------------------------------------------------------------------------

class PowerTransformerAdapter(ITreeNodeAdapter):
    """ Adapts a PowerTransformer to implement the ITreeNode interface.
    """

    adapts(PowerTransformer, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contains_TransformerWindings", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contains_TransformerWindings", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains_TransformerWindings',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains_TransformerWindings',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow)."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'PowerTransformer'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (TransformerWinding, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contains_TransformerWindings", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "BusbarSectionAdapter" class:
#------------------------------------------------------------------------------

class BusbarSectionAdapter(ITreeNodeAdapter):
    """ Adapts a BusbarSection to implement the ITreeNode interface.
    """

    adapts(BusbarSection, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'BusbarSection'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ACLineSegmentAdapter" class:
#------------------------------------------------------------------------------

class ACLineSegmentAdapter(ITreeNodeAdapter):
    """ Adapts a ACLineSegment to implement the ITreeNode interface.
    """

    adapts(ACLineSegment, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["HasFirst_MutualCoupling", "HasSecond_MutualCoupling", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["HasFirst_MutualCoupling", "HasSecond_MutualCoupling", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'HasFirst_MutualCoupling',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'HasSecond_MutualCoupling',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'HasFirst_MutualCoupling',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'HasSecond_MutualCoupling',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ACLineSegment'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (MutualCoupling, MutualCoupling, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["HasFirst_MutualCoupling", "HasSecond_MutualCoupling", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "MutualCouplingAdapter" class:
#------------------------------------------------------------------------------

class MutualCouplingAdapter(ITreeNodeAdapter):
    """ Adapts a MutualCoupling to implement the ITreeNode interface.
    """

    adapts(MutualCoupling, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "This class represents the zero sequence line mutual coupling."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'MutualCoupling'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ShuntCompensatorAdapter" class:
#------------------------------------------------------------------------------

class ShuntCompensatorAdapter(ITreeNodeAdapter):
    """ Adapts a ShuntCompensator to implement the ITreeNode interface.
    """

    adapts(ShuntCompensator, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ShuntCompensator'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "FuseAdapter" class:
#------------------------------------------------------------------------------

class FuseAdapter(ITreeNodeAdapter):
    """ Adapts a Fuse to implement the ITreeNode interface.
    """

    adapts(Fuse, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Fuse'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RectifierInverterAdapter" class:
#------------------------------------------------------------------------------

class RectifierInverterAdapter(ITreeNodeAdapter):
    """ Adapts a RectifierInverter to implement the ITreeNode interface.
    """

    adapts(RectifierInverter, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RectifierInverter'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "HeatExchangerAdapter" class:
#------------------------------------------------------------------------------

class HeatExchangerAdapter(ITreeNodeAdapter):
    """ Adapts a HeatExchanger to implement the ITreeNode interface.
    """

    adapts(HeatExchanger, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Equipment for the cooling of electrical equipment and the extraction of heat"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'HeatExchanger'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EnergyConsumerAdapter" class:
#------------------------------------------------------------------------------

class EnergyConsumerAdapter(ITreeNodeAdapter):
    """ Adapts a EnergyConsumer to implement the ITreeNode interface.
    """

    adapts(EnergyConsumer, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Generic user of energy - a  point of consumption on the power system model"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'EnergyConsumer'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SwitchAdapter" class:
#------------------------------------------------------------------------------

class SwitchAdapter(ITreeNodeAdapter):
    """ Adapts a Switch to implement the ITreeNode interface.
    """

    adapts(Switch, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["SwitchingOperations", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["SwitchingOperations", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SwitchingOperations',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SwitchingOperations',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A generic device designed to close, or open, or both, one or more electric circuits."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Switch'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (SwitchingOperation, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["SwitchingOperations", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SynchronousMachineAdapter" class:
#------------------------------------------------------------------------------

class SynchronousMachineAdapter(ITreeNodeAdapter):
    """ Adapts a SynchronousMachine to implement the ITreeNode interface.
    """

    adapts(SynchronousMachine, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["ReactiveCapabilityCurves", "DrivenBy_PrimeMover", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["ReactiveCapabilityCurves", "DrivenBy_PrimeMover", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ReactiveCapabilityCurves',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'DrivenBy_PrimeMover',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ReactiveCapabilityCurves',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'DrivenBy_PrimeMover',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SynchronousMachine'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ReactiveCapabilityCurve, PrimeMover, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["ReactiveCapabilityCurves", "DrivenBy_PrimeMover", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RegulatingControlAdapter" class:
#------------------------------------------------------------------------------

class RegulatingControlAdapter(ITreeNodeAdapter):
    """ Adapts a RegulatingControl to implement the ITreeNode interface.
    """

    adapts(RegulatingControl, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["RegulatingCondEq", "TapChanger", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["RegulatingCondEq", "TapChanger", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'RegulatingCondEq',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TapChanger',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'RegulatingCondEq',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TapChanger',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Specifies a set of equipment that works together to control a power system quantity such as voltage or flow."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RegulatingControl'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (RegulatingCondEq, TapChanger, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["RegulatingCondEq", "TapChanger", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ConnectorAdapter" class:
#------------------------------------------------------------------------------

class ConnectorAdapter(ITreeNodeAdapter):
    """ Adapts a Connector to implement the ITreeNode interface.
    """

    adapts(Connector, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation and are modelled with a single logical terminal."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Connector'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "StaticVarCompensatorAdapter" class:
#------------------------------------------------------------------------------

class StaticVarCompensatorAdapter(ITreeNodeAdapter):
    """ Adapts a StaticVarCompensator to implement the ITreeNode interface.
    """

    adapts(StaticVarCompensator, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'StaticVarCompensator'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "JunctionAdapter" class:
#------------------------------------------------------------------------------

class JunctionAdapter(ITreeNodeAdapter):
    """ Adapts a Junction to implement the ITreeNode interface.
    """

    adapts(Junction, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A point where one or more conducting equipments are connected with zero resistance."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Junction'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "WindingTestAdapter" class:
#------------------------------------------------------------------------------

class WindingTestAdapter(ITreeNodeAdapter):
    """ Adapts a WindingTest to implement the ITreeNode interface.
    """

    adapts(WindingTest, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Physical winding test data for the winding/tap pairs of a transformer (or phase shifter). This test data can be used to derive other attributes of specific transformer or phase shifter models."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'WindingTest'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "DisconnectorAdapter" class:
#------------------------------------------------------------------------------

class DisconnectorAdapter(ITreeNodeAdapter):
    """ Adapts a Disconnector to implement the ITreeNode interface.
    """

    adapts(Disconnector, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Disconnector'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ConductorTypeAdapter" class:
#------------------------------------------------------------------------------

class ConductorTypeAdapter(ITreeNodeAdapter):
    """ Adapts a ConductorType to implement the ITreeNode interface.
    """

    adapts(ConductorType, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Conductors", "WireArrangements", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Conductors", "WireArrangements", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Conductors',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'WireArrangements',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Conductors',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'WireArrangements',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Wire or cable conductor (per IEEE specs). A specific type of wire or combination of wires not insulated from one another, suitable for carrying electric current. It may be bare or insulated."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ConductorType'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Conductor, WireArrangement, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Conductors", "WireArrangements", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "PlantAdapter" class:
#------------------------------------------------------------------------------

class PlantAdapter(ITreeNodeAdapter):
    """ Adapts a Plant to implement the ITreeNode interface.
    """

    adapts(Plant, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A Plant is a collection of equipment for purposes of generation."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Plant'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ReactiveCapabilityCurveAdapter" class:
#------------------------------------------------------------------------------

class ReactiveCapabilityCurveAdapter(ITreeNodeAdapter):
    """ Adapts a ReactiveCapabilityCurve to implement the ITreeNode interface.
    """

    adapts(ReactiveCapabilityCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["SynchronousMachines", "InitiallyUsedBySynchronousMachine", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["SynchronousMachines", "InitiallyUsedBySynchronousMachine", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SynchronousMachines',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'InitiallyUsedBySynchronousMachine',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SynchronousMachines',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'InitiallyUsedBySynchronousMachine',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ReactiveCapabilityCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (SynchronousMachine, SynchronousMachine, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["SynchronousMachines", "InitiallyUsedBySynchronousMachine", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "NuclearGeneratingUnitAdapter" class:
#------------------------------------------------------------------------------

class NuclearGeneratingUnitAdapter(ITreeNodeAdapter):
    """ Adapts a NuclearGeneratingUnit to implement the ITreeNode interface.
    """

    adapts(NuclearGeneratingUnit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A nuclear generating unit."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'NuclearGeneratingUnit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "GeneratingUnitAdapter" class:
#------------------------------------------------------------------------------

class GeneratingUnitAdapter(ITreeNodeAdapter):
    """ Adapts a GeneratingUnit to implement the ITreeNode interface.
    """

    adapts(GeneratingUnit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["ControlAreaGeneratingUnit", "GrossToNetActivePowerCurves", "Contains_SynchronousMachines", "GenUnitOpCostCurves", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["ControlAreaGeneratingUnit", "GrossToNetActivePowerCurves", "Contains_SynchronousMachines", "GenUnitOpCostCurves", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ControlAreaGeneratingUnit',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'GrossToNetActivePowerCurves',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Contains_SynchronousMachines',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'GenUnitOpCostCurves',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ControlAreaGeneratingUnit',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'GrossToNetActivePowerCurves',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Contains_SynchronousMachines',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'GenUnitOpCostCurves',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'GeneratingUnit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ControlAreaGeneratingUnit, GrossToNetActivePowerCurve, SynchronousMachine, GenUnitOpCostCurve, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["ControlAreaGeneratingUnit", "GrossToNetActivePowerCurves", "Contains_SynchronousMachines", "GenUnitOpCostCurves", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "StartIgnFuelCurveAdapter" class:
#------------------------------------------------------------------------------

class StartIgnFuelCurveAdapter(ITreeNodeAdapter):
    """ Adapts a StartIgnFuelCurve to implement the ITreeNode interface.
    """

    adapts(StartIgnFuelCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'StartIgnFuelCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "HydroGeneratingEfficiencyCurveAdapter" class:
#------------------------------------------------------------------------------

class HydroGeneratingEfficiencyCurveAdapter(ITreeNodeAdapter):
    """ Adapts a HydroGeneratingEfficiencyCurve to implement the ITreeNode interface.
    """

    adapts(HydroGeneratingEfficiencyCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'HydroGeneratingEfficiencyCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "TargetLevelScheduleAdapter" class:
#------------------------------------------------------------------------------

class TargetLevelScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a TargetLevelSchedule to implement the ITreeNode interface.
    """

    adapts(TargetLevelSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Reservoir water level targets from advanced studies or 'rule curves'. Typically in one hour increments for up to 10 days"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'TargetLevelSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "GrossToNetActivePowerCurveAdapter" class:
#------------------------------------------------------------------------------

class GrossToNetActivePowerCurveAdapter(ITreeNodeAdapter):
    """ Adapts a GrossToNetActivePowerCurve to implement the ITreeNode interface.
    """

    adapts(GrossToNetActivePowerCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'GrossToNetActivePowerCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "IncrementalHeatRateCurveAdapter" class:
#------------------------------------------------------------------------------

class IncrementalHeatRateCurveAdapter(ITreeNodeAdapter):
    """ Adapts a IncrementalHeatRateCurve to implement the ITreeNode interface.
    """

    adapts(IncrementalHeatRateCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between unit incremental heat rate in (delta energy/time) per (delta active power) and unit output in active power. The IHR curve represents the slope of the HeatInputCurve. Note that the 'incremental heat rate' and the 'heat rate' have the same engineering units."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'IncrementalHeatRateCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "HeatInputCurveAdapter" class:
#------------------------------------------------------------------------------

class HeatInputCurveAdapter(ITreeNodeAdapter):
    """ Adapts a HeatInputCurve to implement the ITreeNode interface.
    """

    adapts(HeatInputCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'HeatInputCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "StartRampCurveAdapter" class:
#------------------------------------------------------------------------------

class StartRampCurveAdapter(ITreeNodeAdapter):
    """ Adapts a StartRampCurve to implement the ITreeNode interface.
    """

    adapts(StartRampCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'StartRampCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AirCompressorAdapter" class:
#------------------------------------------------------------------------------

class AirCompressorAdapter(ITreeNodeAdapter):
    """ Adapts a AirCompressor to implement the ITreeNode interface.
    """

    adapts(AirCompressor, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'AirCompressor'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ShutdownCurveAdapter" class:
#------------------------------------------------------------------------------

class ShutdownCurveAdapter(ITreeNodeAdapter):
    """ Adapts a ShutdownCurve to implement the ITreeNode interface.
    """

    adapts(ShutdownCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ShutdownCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CombinedCyclePlantAdapter" class:
#------------------------------------------------------------------------------

class CombinedCyclePlantAdapter(ITreeNodeAdapter):
    """ Adapts a CombinedCyclePlant to implement the ITreeNode interface.
    """

    adapts(CombinedCyclePlant, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contain_ThermalGeneratingUnits", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contain_ThermalGeneratingUnits", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_ThermalGeneratingUnits',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_ThermalGeneratingUnits',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CombinedCyclePlant'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ThermalGeneratingUnit, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contain_ThermalGeneratingUnits", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "StartupModelAdapter" class:
#------------------------------------------------------------------------------

class StartupModelAdapter(ITreeNodeAdapter):
    """ Adapts a StartupModel to implement the ITreeNode interface.
    """

    adapts(StartupModel, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Unit start up characteristics depending on how long the unit has been off line"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'StartupModel'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "HydroPumpAdapter" class:
#------------------------------------------------------------------------------

class HydroPumpAdapter(ITreeNodeAdapter):
    """ Adapts a HydroPump to implement the ITreeNode interface.
    """

    adapts(HydroPump, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A synchronous motor-driven pump, typically associated with a pumped storage plant"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'HydroPump'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EmissionCurveAdapter" class:
#------------------------------------------------------------------------------

class EmissionCurveAdapter(ITreeNodeAdapter):
    """ Adapts a EmissionCurve to implement the ITreeNode interface.
    """

    adapts(EmissionCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'EmissionCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "GenUnitOpCostCurveAdapter" class:
#------------------------------------------------------------------------------

class GenUnitOpCostCurveAdapter(ITreeNodeAdapter):
    """ Adapts a GenUnitOpCostCurve to implement the ITreeNode interface.
    """

    adapts(GenUnitOpCostCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between unit operating cost (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'GenUnitOpCostCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "HydroPowerPlantAdapter" class:
#------------------------------------------------------------------------------

class HydroPowerPlantAdapter(ITreeNodeAdapter):
    """ Adapts a HydroPowerPlant to implement the ITreeNode interface.
    """

    adapts(HydroPowerPlant, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contain_HydroGeneratingUnits", "Contain_HydroPumps", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contain_HydroGeneratingUnits", "Contain_HydroPumps", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_HydroGeneratingUnits',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Contain_HydroPumps',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_HydroGeneratingUnits',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Contain_HydroPumps',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'HydroPowerPlant'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (HydroGeneratingUnit, HydroPump, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contain_HydroGeneratingUnits", "Contain_HydroPumps", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "HydroGeneratingUnitAdapter" class:
#------------------------------------------------------------------------------

class HydroGeneratingUnitAdapter(ITreeNodeAdapter):
    """ Adapts a HydroGeneratingUnit to implement the ITreeNode interface.
    """

    adapts(HydroGeneratingUnit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["HydroGeneratingEfficiencyCurves", "TailbayLossCurve", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["HydroGeneratingEfficiencyCurves", "TailbayLossCurve", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'HydroGeneratingEfficiencyCurves',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TailbayLossCurve',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'HydroGeneratingEfficiencyCurves',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TailbayLossCurve',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'HydroGeneratingUnit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (HydroGeneratingEfficiencyCurve, TailbayLossCurve, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["HydroGeneratingEfficiencyCurves", "TailbayLossCurve", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CAESPlantAdapter" class:
#------------------------------------------------------------------------------

class CAESPlantAdapter(ITreeNodeAdapter):
    """ Adapts a CAESPlant to implement the ITreeNode interface.
    """

    adapts(CAESPlant, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Compressed air energy storage plant"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CAESPlant'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "LevelVsVolumeCurveAdapter" class:
#------------------------------------------------------------------------------

class LevelVsVolumeCurveAdapter(ITreeNodeAdapter):
    """ Adapts a LevelVsVolumeCurve to implement the ITreeNode interface.
    """

    adapts(LevelVsVolumeCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'LevelVsVolumeCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "InflowForecastAdapter" class:
#------------------------------------------------------------------------------

class InflowForecastAdapter(ITreeNodeAdapter):
    """ Adapts a InflowForecast to implement the ITreeNode interface.
    """

    adapts(InflowForecast, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Natural water inflow to a reservoir, usually forecasted from predicted rain and snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in average cubic meters per second over the time increment."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'InflowForecast'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SteamSendoutScheduleAdapter" class:
#------------------------------------------------------------------------------

class SteamSendoutScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a SteamSendoutSchedule to implement the ITreeNode interface.
    """

    adapts(SteamSendoutSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The cogeneration plant's steam sendout schedule in volume per time unit."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SteamSendoutSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ThermalGeneratingUnitAdapter" class:
#------------------------------------------------------------------------------

class ThermalGeneratingUnitAdapter(ITreeNodeAdapter):
    """ Adapts a ThermalGeneratingUnit to implement the ITreeNode interface.
    """

    adapts(ThermalGeneratingUnit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["FuelAllocationSchedules", "EmissionCurves", "EmmissionAccounts", "FossilFuels", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["FuelAllocationSchedules", "EmissionCurves", "EmmissionAccounts", "FossilFuels", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'FuelAllocationSchedules',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'EmissionCurves',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'EmmissionAccounts',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'FossilFuels',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'FuelAllocationSchedules',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'EmissionCurves',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'EmmissionAccounts',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'FossilFuels',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ThermalGeneratingUnit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (FuelAllocationSchedule, EmissionCurve, EmissionAccount, FossilFuel, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["FuelAllocationSchedules", "EmissionCurves", "EmmissionAccounts", "FossilFuels", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "FossilFuelAdapter" class:
#------------------------------------------------------------------------------

class FossilFuelAdapter(ITreeNodeAdapter):
    """ Adapts a FossilFuel to implement the ITreeNode interface.
    """

    adapts(FossilFuel, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["FuelAllocationSchedule", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["FuelAllocationSchedule", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'FuelAllocationSchedule',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'FuelAllocationSchedule',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'FossilFuel'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (FuelAllocationSchedule, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["FuelAllocationSchedule", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "FuelAllocationScheduleAdapter" class:
#------------------------------------------------------------------------------

class FuelAllocationScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a FuelAllocationSchedule to implement the ITreeNode interface.
    """

    adapts(FuelAllocationSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The amount of fuel of a given type which is allocated for consumption over a specified period of time"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'FuelAllocationSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EmissionAccountAdapter" class:
#------------------------------------------------------------------------------

class EmissionAccountAdapter(ITreeNodeAdapter):
    """ Adapts a EmissionAccount to implement the ITreeNode interface.
    """

    adapts(EmissionAccount, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Accounts for tracking emissions usage and credits for thermal generating units. A unit may have zero or more emission accounts, and will typically have one for tracking usage and one for tracking credits."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'EmissionAccount'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "TailbayLossCurveAdapter" class:
#------------------------------------------------------------------------------

class TailbayLossCurveAdapter(ITreeNodeAdapter):
    """ Adapts a TailbayLossCurve to implement the ITreeNode interface.
    """

    adapts(TailbayLossCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between tailbay head loss hight (y-axis) and the total discharge into the power station's tailbay volume per time unit (x-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'TailbayLossCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "PenstockLossCurveAdapter" class:
#------------------------------------------------------------------------------

class PenstockLossCurveAdapter(ITreeNodeAdapter):
    """ Adapts a PenstockLossCurve to implement the ITreeNode interface.
    """

    adapts(PenstockLossCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'PenstockLossCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "StartMainFuelCurveAdapter" class:
#------------------------------------------------------------------------------

class StartMainFuelCurveAdapter(ITreeNodeAdapter):
    """ Adapts a StartMainFuelCurve to implement the ITreeNode interface.
    """

    adapts(StartMainFuelCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'StartMainFuelCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ReservoirAdapter" class:
#------------------------------------------------------------------------------

class ReservoirAdapter(ITreeNodeAdapter):
    """ Adapts a Reservoir to implement the ITreeNode interface.
    """

    adapts(Reservoir, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["LevelVsVolumeCurve", "InflowForecast", "SpillsInto", "HydroPowerPlants", "UpstreamFrom", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["LevelVsVolumeCurve", "InflowForecast", "SpillsInto", "HydroPowerPlants", "UpstreamFrom", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'LevelVsVolumeCurve',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'InflowForecast',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'SpillsInto',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'HydroPowerPlants',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'UpstreamFrom',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'LevelVsVolumeCurve',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'InflowForecast',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'SpillsInto',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'HydroPowerPlants',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'UpstreamFrom',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Reservoir'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (LevelVsVolumeCurve, InflowForecast, Reservoir, HydroPowerPlant, HydroPowerPlant, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["LevelVsVolumeCurve", "InflowForecast", "SpillsInto", "HydroPowerPlants", "UpstreamFrom", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "HydroPumpOpScheduleAdapter" class:
#------------------------------------------------------------------------------

class HydroPumpOpScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a HydroPumpOpSchedule to implement the ITreeNode interface.
    """

    adapts(HydroPumpOpSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'HydroPumpOpSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "HeatRateCurveAdapter" class:
#------------------------------------------------------------------------------

class HeatRateCurveAdapter(ITreeNodeAdapter):
    """ Adapts a HeatRateCurve to implement the ITreeNode interface.
    """

    adapts(HeatRateCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between unit heat rate per active power (Y-axis) and  unit output (X-axis). The heat input is from all fuels."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'HeatRateCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "GenUnitOpScheduleAdapter" class:
#------------------------------------------------------------------------------

class GenUnitOpScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a GenUnitOpSchedule to implement the ITreeNode interface.
    """

    adapts(GenUnitOpSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'GenUnitOpSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CogenerationPlantAdapter" class:
#------------------------------------------------------------------------------

class CogenerationPlantAdapter(ITreeNodeAdapter):
    """ Adapts a CogenerationPlant to implement the ITreeNode interface.
    """

    adapts(CogenerationPlant, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contain_ThermalGeneratingUnits", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contain_ThermalGeneratingUnits", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_ThermalGeneratingUnits',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_ThermalGeneratingUnits',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CogenerationPlant'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ThermalGeneratingUnit, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contain_ThermalGeneratingUnits", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SupercriticalAdapter" class:
#------------------------------------------------------------------------------

class SupercriticalAdapter(ITreeNodeAdapter):
    """ Adapts a Supercritical to implement the ITreeNode interface.
    """

    adapts(Supercritical, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Once-through supercritical boiler"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Supercritical'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SteamTurbineAdapter" class:
#------------------------------------------------------------------------------

class SteamTurbineAdapter(ITreeNodeAdapter):
    """ Adapts a SteamTurbine to implement the ITreeNode interface.
    """

    adapts(SteamTurbine, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["SteamSupplys", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["SteamSupplys", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SteamSupplys',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SteamSupplys',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Steam turbine"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SteamTurbine'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (SteamSupply, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["SteamSupplys", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CTTempActivePowerCurveAdapter" class:
#------------------------------------------------------------------------------

class CTTempActivePowerCurveAdapter(ITreeNodeAdapter):
    """ Adapts a CTTempActivePowerCurve to implement the ITreeNode interface.
    """

    adapts(CTTempActivePowerCurve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CTTempActivePowerCurve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "PrimeMoverAdapter" class:
#------------------------------------------------------------------------------

class PrimeMoverAdapter(ITreeNodeAdapter):
    """ Adapts a PrimeMover to implement the ITreeNode interface.
    """

    adapts(PrimeMover, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Drives_SynchronousMachines", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Drives_SynchronousMachines", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Drives_SynchronousMachines',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Drives_SynchronousMachines',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The machine used to develop mechanical energy used to drive a generator."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'PrimeMover'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (SynchronousMachine, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Drives_SynchronousMachines", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "PWRSteamSupplyAdapter" class:
#------------------------------------------------------------------------------

class PWRSteamSupplyAdapter(ITreeNodeAdapter):
    """ Adapts a PWRSteamSupply to implement the ITreeNode interface.
    """

    adapts(PWRSteamSupply, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Pressurized water reactor used as a steam supply to a steam turbine"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'PWRSteamSupply'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CombustionTurbineAdapter" class:
#------------------------------------------------------------------------------

class CombustionTurbineAdapter(ITreeNodeAdapter):
    """ Adapts a CombustionTurbine to implement the ITreeNode interface.
    """

    adapts(CombustionTurbine, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A prime mover that is typically fueled by gas or light oil"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CombustionTurbine'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "HeatRecoveryBoilerAdapter" class:
#------------------------------------------------------------------------------

class HeatRecoveryBoilerAdapter(ITreeNodeAdapter):
    """ Adapts a HeatRecoveryBoiler to implement the ITreeNode interface.
    """

    adapts(HeatRecoveryBoiler, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["CombustionTurbines", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["CombustionTurbines", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'CombustionTurbines',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'CombustionTurbines',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'HeatRecoveryBoiler'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (CombustionTurbine, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["CombustionTurbines", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "BWRSteamSupplyAdapter" class:
#------------------------------------------------------------------------------

class BWRSteamSupplyAdapter(ITreeNodeAdapter):
    """ Adapts a BWRSteamSupply to implement the ITreeNode interface.
    """

    adapts(BWRSteamSupply, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Boiling water reactor used as a steam supply to a steam turbine"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'BWRSteamSupply'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "HydroTurbineAdapter" class:
#------------------------------------------------------------------------------

class HydroTurbineAdapter(ITreeNodeAdapter):
    """ Adapts a HydroTurbine to implement the ITreeNode interface.
    """

    adapts(HydroTurbine, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'HydroTurbine'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "DrumBoilerAdapter" class:
#------------------------------------------------------------------------------

class DrumBoilerAdapter(ITreeNodeAdapter):
    """ Adapts a DrumBoiler to implement the ITreeNode interface.
    """

    adapts(DrumBoiler, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Drum boiler"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'DrumBoiler'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "FossilSteamSupplyAdapter" class:
#------------------------------------------------------------------------------

class FossilSteamSupplyAdapter(ITreeNodeAdapter):
    """ Adapts a FossilSteamSupply to implement the ITreeNode interface.
    """

    adapts(FossilSteamSupply, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Fossil fueled boiler (e.g., coal, oil, gas)"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'FossilSteamSupply'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SubcriticalAdapter" class:
#------------------------------------------------------------------------------

class SubcriticalAdapter(ITreeNodeAdapter):
    """ Adapts a Subcritical to implement the ITreeNode interface.
    """

    adapts(Subcritical, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Once-through subcritical boiler"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Subcritical'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SteamSupplyAdapter" class:
#------------------------------------------------------------------------------

class SteamSupplyAdapter(ITreeNodeAdapter):
    """ Adapts a SteamSupply to implement the ITreeNode interface.
    """

    adapts(SteamSupply, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["SteamTurbines", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["SteamTurbines", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SteamTurbines',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SteamTurbines',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Steam supply for steam turbine"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SteamSupply'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (SteamTurbine, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["SteamTurbines", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "DiscreteAdapter" class:
#------------------------------------------------------------------------------

class DiscreteAdapter(ITreeNodeAdapter):
    """ Adapts a Discrete to implement the ITreeNode interface.
    """

    adapts(Discrete, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contain_MeasurementValues", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contain_MeasurementValues", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_MeasurementValues',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_MeasurementValues',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Discrete'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (DiscreteValue, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contain_MeasurementValues", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "MeasurementAdapter" class:
#------------------------------------------------------------------------------

class MeasurementAdapter(ITreeNodeAdapter):
    """ Adapts a Measurement to implement the ITreeNode interface.
    """

    adapts(Measurement, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Measurement'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SetPointAdapter" class:
#------------------------------------------------------------------------------

class SetPointAdapter(ITreeNodeAdapter):
    """ Adapts a SetPoint to implement the ITreeNode interface.
    """

    adapts(SetPoint, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A SetPoint is an analog control used for supervisory control."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SetPoint'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ControlAdapter" class:
#------------------------------------------------------------------------------

class ControlAdapter(ITreeNodeAdapter):
    """ Adapts a Control to implement the ITreeNode interface.
    """

    adapts(Control, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Control'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ControlTypeAdapter" class:
#------------------------------------------------------------------------------

class ControlTypeAdapter(ITreeNodeAdapter):
    """ Adapts a ControlType to implement the ITreeNode interface.
    """

    adapts(ControlType, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Controls", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Controls", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Controls',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Controls',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ControlType'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Control, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Controls", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "DiscreteValueAdapter" class:
#------------------------------------------------------------------------------

class DiscreteValueAdapter(ITreeNodeAdapter):
    """ Adapts a DiscreteValue to implement the ITreeNode interface.
    """

    adapts(DiscreteValue, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "DiscreteValue represents a discrete MeasurementValue."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'DiscreteValue'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AccumulatorAdapter" class:
#------------------------------------------------------------------------------

class AccumulatorAdapter(ITreeNodeAdapter):
    """ Adapts a Accumulator to implement the ITreeNode interface.
    """

    adapts(Accumulator, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contain_MeasurementValues", "LimitSets", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contain_MeasurementValues", "LimitSets", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_MeasurementValues',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'LimitSets',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_MeasurementValues',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'LimitSets',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Accumulator represents a accumulated (counted) Measurement, e.g. an energy value."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Accumulator'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (AccumulatorValue, AccumulatorLimitSet, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contain_MeasurementValues", "LimitSets", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "LimitSetAdapter" class:
#------------------------------------------------------------------------------

class LimitSetAdapter(ITreeNodeAdapter):
    """ Adapts a LimitSet to implement the ITreeNode interface.
    """

    adapts(LimitSet, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'LimitSet'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AnalogLimitAdapter" class:
#------------------------------------------------------------------------------

class AnalogLimitAdapter(ITreeNodeAdapter):
    """ Adapts a AnalogLimit to implement the ITreeNode interface.
    """

    adapts(AnalogLimit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Limit values for Analog measurements"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'AnalogLimit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "MeasurementValueAdapter" class:
#------------------------------------------------------------------------------

class MeasurementValueAdapter(ITreeNodeAdapter):
    """ Adapts a MeasurementValue to implement the ITreeNode interface.
    """

    adapts(MeasurementValue, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'MeasurementValue'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ValueAliasSetAdapter" class:
#------------------------------------------------------------------------------

class ValueAliasSetAdapter(ITreeNodeAdapter):
    """ Adapts a ValueAliasSet to implement the ITreeNode interface.
    """

    adapts(ValueAliasSet, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Values", "Commands", "Measurements", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Values", "Commands", "Measurements", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Values',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Commands',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Values',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Commands',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ValueAliasSet'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ValueToAlias, Command, Discrete, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Values", "Commands", "Measurements", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "StringMeasurementValueAdapter" class:
#------------------------------------------------------------------------------

class StringMeasurementValueAdapter(ITreeNodeAdapter):
    """ Adapts a StringMeasurementValue to implement the ITreeNode interface.
    """

    adapts(StringMeasurementValue, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "StringMeasurementValue represents a measurement value of type string."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'StringMeasurementValue'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "Quality61850Adapter" class:
#------------------------------------------------------------------------------

class Quality61850Adapter(ITreeNodeAdapter):
    """ Adapts a Quality61850 to implement the ITreeNode interface.
    """

    adapts(Quality61850, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Quality61850'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "LimitAdapter" class:
#------------------------------------------------------------------------------

class LimitAdapter(ITreeNodeAdapter):
    """ Adapts a Limit to implement the ITreeNode interface.
    """

    adapts(Limit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Limit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "MeasurementTypeAdapter" class:
#------------------------------------------------------------------------------

class MeasurementTypeAdapter(ITreeNodeAdapter):
    """ Adapts a MeasurementType to implement the ITreeNode interface.
    """

    adapts(MeasurementType, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Measurements", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Measurements", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'MeasurementType'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Measurement, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Measurements", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AccumulatorLimitAdapter" class:
#------------------------------------------------------------------------------

class AccumulatorLimitAdapter(ITreeNodeAdapter):
    """ Adapts a AccumulatorLimit to implement the ITreeNode interface.
    """

    adapts(AccumulatorLimit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Limit values for Accumulator measurements"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'AccumulatorLimit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "StringMeasurementAdapter" class:
#------------------------------------------------------------------------------

class StringMeasurementAdapter(ITreeNodeAdapter):
    """ Adapts a StringMeasurement to implement the ITreeNode interface.
    """

    adapts(StringMeasurement, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contains_MeasurementValues", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contains_MeasurementValues", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains_MeasurementValues',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains_MeasurementValues',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "StringMeasurement represents a measurement with values of type string."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'StringMeasurement'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (StringMeasurementValue, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contains_MeasurementValues", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ValueToAliasAdapter" class:
#------------------------------------------------------------------------------

class ValueToAliasAdapter(ITreeNodeAdapter):
    """ Adapts a ValueToAlias to implement the ITreeNode interface.
    """

    adapts(ValueToAlias, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Describes the translation of one particular value into a name, e.g. 1->'Open'"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ValueToAlias'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AnalogValueAdapter" class:
#------------------------------------------------------------------------------

class AnalogValueAdapter(ITreeNodeAdapter):
    """ Adapts a AnalogValue to implement the ITreeNode interface.
    """

    adapts(AnalogValue, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["AltGeneratingUnit", "AltTieMeas", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["AltGeneratingUnit", "AltTieMeas", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'AltGeneratingUnit',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'AltTieMeas',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'AltGeneratingUnit',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'AltTieMeas',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "AnalogValue represents an analog MeasurementValue."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'AnalogValue'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (AltGeneratingUnitMeas, AltTieMeas, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["AltGeneratingUnit", "AltTieMeas", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "MeasurementValueQualityAdapter" class:
#------------------------------------------------------------------------------

class MeasurementValueQualityAdapter(ITreeNodeAdapter):
    """ Adapts a MeasurementValueQuality to implement the ITreeNode interface.
    """

    adapts(MeasurementValueQuality, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'MeasurementValueQuality'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "MeasurementValueSourceAdapter" class:
#------------------------------------------------------------------------------

class MeasurementValueSourceAdapter(ITreeNodeAdapter):
    """ Adapts a MeasurementValueSource to implement the ITreeNode interface.
    """

    adapts(MeasurementValueSource, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["MeasurementValues", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["MeasurementValues", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'MeasurementValues',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'MeasurementValues',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'MeasurementValueSource'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (MeasurementValue, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["MeasurementValues", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AccumulatorLimitSetAdapter" class:
#------------------------------------------------------------------------------

class AccumulatorLimitSetAdapter(ITreeNodeAdapter):
    """ Adapts a AccumulatorLimitSet to implement the ITreeNode interface.
    """

    adapts(AccumulatorLimitSet, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Measurements", "Limits", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Measurements", "Limits", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Limits',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Limits',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'AccumulatorLimitSet'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Accumulator, AccumulatorLimit, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Measurements", "Limits", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AnalogLimitSetAdapter" class:
#------------------------------------------------------------------------------

class AnalogLimitSetAdapter(ITreeNodeAdapter):
    """ Adapts a AnalogLimitSet to implement the ITreeNode interface.
    """

    adapts(AnalogLimitSet, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Limits", "Measurements", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Limits", "Measurements", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Limits',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Limits',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'AnalogLimitSet'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (AnalogLimit, Analog, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Limits", "Measurements", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CommandAdapter" class:
#------------------------------------------------------------------------------

class CommandAdapter(ITreeNodeAdapter):
    """ Adapts a Command to implement the ITreeNode interface.
    """

    adapts(Command, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A Command is a discrete control used for supervisory control."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Command'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AnalogAdapter" class:
#------------------------------------------------------------------------------

class AnalogAdapter(ITreeNodeAdapter):
    """ Adapts a Analog to implement the ITreeNode interface.
    """

    adapts(Analog, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contain_MeasurementValues", "LimitSets", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contain_MeasurementValues", "LimitSets", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_MeasurementValues',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'LimitSets',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_MeasurementValues',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'LimitSets',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Analog represents an analog Measurement."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Analog'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (AnalogValue, AnalogLimitSet, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contain_MeasurementValues", "LimitSets", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AccumulatorValueAdapter" class:
#------------------------------------------------------------------------------

class AccumulatorValueAdapter(ITreeNodeAdapter):
    """ Adapts a AccumulatorValue to implement the ITreeNode interface.
    """

    adapts(AccumulatorValue, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "AccumulatorValue represents a accumulated (counted) MeasurementValue."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'AccumulatorValue'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SubLoadAreaAdapter" class:
#------------------------------------------------------------------------------

class SubLoadAreaAdapter(ITreeNodeAdapter):
    """ Adapts a SubLoadArea to implement the ITreeNode interface.
    """

    adapts(SubLoadArea, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["LoadGroups", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["LoadGroups", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'LoadGroups',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'LoadGroups',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SubLoadArea'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (LoadGroup, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["LoadGroups", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "LoadAdapter" class:
#------------------------------------------------------------------------------

class LoadAdapter(ITreeNodeAdapter):
    """ Adapts a Load to implement the ITreeNode interface.
    """

    adapts(Load, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Load'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "LoadResponseCharacteristicAdapter" class:
#------------------------------------------------------------------------------

class LoadResponseCharacteristicAdapter(ITreeNodeAdapter):
    """ Adapts a LoadResponseCharacteristic to implement the ITreeNode interface.
    """

    adapts(LoadResponseCharacteristic, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["EnergyConsumer", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["EnergyConsumer", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'EnergyConsumer',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'EnergyConsumer',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'LoadResponseCharacteristic'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (EnergyConsumer, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["EnergyConsumer", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SeasonAdapter" class:
#------------------------------------------------------------------------------

class SeasonAdapter(ITreeNodeAdapter):
    """ Adapts a Season to implement the ITreeNode interface.
    """

    adapts(Season, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["SeasonDayTypeSchedules", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["SeasonDayTypeSchedules", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SeasonDayTypeSchedules',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SeasonDayTypeSchedules',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A specified time period of the year, e.g., Spring, Summer, Fall, Winter"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Season'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (SeasonDayTypeSchedule, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["SeasonDayTypeSchedules", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ConformLoadGroupAdapter" class:
#------------------------------------------------------------------------------

class ConformLoadGroupAdapter(ITreeNodeAdapter):
    """ Adapts a ConformLoadGroup to implement the ITreeNode interface.
    """

    adapts(ConformLoadGroup, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["EnergyConsumers", "ConformLoadSchedules", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["EnergyConsumers", "ConformLoadSchedules", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'EnergyConsumers',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ConformLoadSchedules',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'EnergyConsumers',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ConformLoadSchedules',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Load that follows a daily and seasonal load variation pattern."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ConformLoadGroup'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ConformLoad, ConformLoadSchedule, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["EnergyConsumers", "ConformLoadSchedules", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ConformLoadAdapter" class:
#------------------------------------------------------------------------------

class ConformLoadAdapter(ITreeNodeAdapter):
    """ Adapts a ConformLoad to implement the ITreeNode interface.
    """

    adapts(ConformLoad, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ConformLoad'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "LoadAreaAdapter" class:
#------------------------------------------------------------------------------

class LoadAreaAdapter(ITreeNodeAdapter):
    """ Adapts a LoadArea to implement the ITreeNode interface.
    """

    adapts(LoadArea, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["SubLoadAreas", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["SubLoadAreas", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SubLoadAreas',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SubLoadAreas',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'LoadArea'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (SubLoadArea, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["SubLoadAreas", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "PowerCutZoneAdapter" class:
#------------------------------------------------------------------------------

class PowerCutZoneAdapter(ITreeNodeAdapter):
    """ Adapts a PowerCutZone to implement the ITreeNode interface.
    """

    adapts(PowerCutZone, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["EnergyConsumers", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["EnergyConsumers", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'EnergyConsumers',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'EnergyConsumers',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An area or zone of the power system which is used for load shedding purposes."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'PowerCutZone'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (EnergyConsumer, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["EnergyConsumers", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ConformLoadScheduleAdapter" class:
#------------------------------------------------------------------------------

class ConformLoadScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a ConformLoadSchedule to implement the ITreeNode interface.
    """

    adapts(ConformLoadSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ConformLoadSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "StationSupplyAdapter" class:
#------------------------------------------------------------------------------

class StationSupplyAdapter(ITreeNodeAdapter):
    """ Adapts a StationSupply to implement the ITreeNode interface.
    """

    adapts(StationSupply, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Station supply with load derived from the station output."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'StationSupply'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "DayTypeAdapter" class:
#------------------------------------------------------------------------------

class DayTypeAdapter(ITreeNodeAdapter):
    """ Adapts a DayType to implement the ITreeNode interface.
    """

    adapts(DayType, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["SeasonDayTypeSchedules", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["SeasonDayTypeSchedules", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SeasonDayTypeSchedules',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SeasonDayTypeSchedules',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'DayType'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (SeasonDayTypeSchedule, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["SeasonDayTypeSchedules", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "NonConformLoadScheduleAdapter" class:
#------------------------------------------------------------------------------

class NonConformLoadScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a NonConformLoadSchedule to implement the ITreeNode interface.
    """

    adapts(NonConformLoadSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'NonConformLoadSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CustomerLoadAdapter" class:
#------------------------------------------------------------------------------

class CustomerLoadAdapter(ITreeNodeAdapter):
    """ Adapts a CustomerLoad to implement the ITreeNode interface.
    """

    adapts(CustomerLoad, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CustomerLoad'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "LoadGroupAdapter" class:
#------------------------------------------------------------------------------

class LoadGroupAdapter(ITreeNodeAdapter):
    """ Adapts a LoadGroup to implement the ITreeNode interface.
    """

    adapts(LoadGroup, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'LoadGroup'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "NonConformLoadGroupAdapter" class:
#------------------------------------------------------------------------------

class NonConformLoadGroupAdapter(ITreeNodeAdapter):
    """ Adapts a NonConformLoadGroup to implement the ITreeNode interface.
    """

    adapts(NonConformLoadGroup, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["NonConformLoadSchedules", "EnergyConsumers", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["NonConformLoadSchedules", "EnergyConsumers", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'NonConformLoadSchedules',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'EnergyConsumers',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'NonConformLoadSchedules',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'EnergyConsumers',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Loads that do not follow a daily and seasonal load variation pattern."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'NonConformLoadGroup'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (NonConformLoadSchedule, NonConformLoad, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["NonConformLoadSchedules", "EnergyConsumers", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EnergyAreaAdapter" class:
#------------------------------------------------------------------------------

class EnergyAreaAdapter(ITreeNodeAdapter):
    """ Adapts a EnergyArea to implement the ITreeNode interface.
    """

    adapts(EnergyArea, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The class describes an area having energy production or consumption. The class is the basis for further specialization."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'EnergyArea'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SeasonDayTypeScheduleAdapter" class:
#------------------------------------------------------------------------------

class SeasonDayTypeScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a SeasonDayTypeSchedule to implement the ITreeNode interface.
    """

    adapts(SeasonDayTypeSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SeasonDayTypeSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "NonConformLoadAdapter" class:
#------------------------------------------------------------------------------

class NonConformLoadAdapter(ITreeNodeAdapter):
    """ Adapts a NonConformLoad to implement the ITreeNode interface.
    """

    adapts(NonConformLoad, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'NonConformLoad'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "InductionMotorLoadAdapter" class:
#------------------------------------------------------------------------------

class InductionMotorLoadAdapter(ITreeNodeAdapter):
    """ Adapts a InductionMotorLoad to implement the ITreeNode interface.
    """

    adapts(InductionMotorLoad, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage)."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'InductionMotorLoad'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CurveAdapter" class:
#------------------------------------------------------------------------------

class CurveAdapter(ITreeNodeAdapter):
    """ Adapts a Curve to implement the ITreeNode interface.
    """

    adapts(Curve, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["CurveScheduleDatas", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["CurveScheduleDatas", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'CurveScheduleDatas',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'CurveScheduleDatas',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Curve'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (CurveData, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["CurveScheduleDatas", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "VoltageLevelAdapter" class:
#------------------------------------------------------------------------------

class VoltageLevelAdapter(ITreeNodeAdapter):
    """ Adapts a VoltageLevel to implement the ITreeNode interface.
    """

    adapts(VoltageLevel, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contains_Bays", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contains_Bays", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains_Bays',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains_Bays',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'VoltageLevel'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Bay, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contains_Bays", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ReportingGroupAdapter" class:
#------------------------------------------------------------------------------

class ReportingGroupAdapter(ITreeNodeAdapter):
    """ Adapts a ReportingGroup to implement the ITreeNode interface.
    """

    adapts(ReportingGroup, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["PowerSystemResource", "BusNameMarker", "TopologicalNode", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["PowerSystemResource", "BusNameMarker", "TopologicalNode", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'PowerSystemResource',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'BusNameMarker',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TopologicalNode',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'PowerSystemResource',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'BusNameMarker',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TopologicalNode',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A reporting group is used for various ad-hoc groupings used for reporting."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ReportingGroup'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (PowerSystemResource, BusNameMarker, TopologicalNode, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["PowerSystemResource", "BusNameMarker", "TopologicalNode", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ModelingAuthoritySetAdapter" class:
#------------------------------------------------------------------------------

class ModelingAuthoritySetAdapter(ITreeNodeAdapter):
    """ Adapts a ModelingAuthoritySet to implement the ITreeNode interface.
    """

    adapts(ModelingAuthoritySet, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["IdentifiedObjects", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["IdentifiedObjects", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'IdentifiedObjects',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'IdentifiedObjects',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ModelingAuthoritySet'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (IdentifiedObject, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["IdentifiedObjects", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "OperatingParticipantAdapter" class:
#------------------------------------------------------------------------------

class OperatingParticipantAdapter(ITreeNodeAdapter):
    """ Adapts a OperatingParticipant to implement the ITreeNode interface.
    """

    adapts(OperatingParticipant, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["OperatingShare", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["OperatingShare", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperatingShare',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperatingShare',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'OperatingParticipant'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (OperatingShare, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["OperatingShare", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ReportingSuperGroupAdapter" class:
#------------------------------------------------------------------------------

class ReportingSuperGroupAdapter(ITreeNodeAdapter):
    """ Adapts a ReportingSuperGroup to implement the ITreeNode interface.
    """

    adapts(ReportingSuperGroup, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["ReportingGroup", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["ReportingGroup", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ReportingGroup',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ReportingGroup',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A reporting super group, groups reporting groups for a higher level report."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ReportingSuperGroup'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ReportingGroup, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["ReportingGroup", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SubstationAdapter" class:
#------------------------------------------------------------------------------

class SubstationAdapter(ITreeNodeAdapter):
    """ Adapts a Substation to implement the ITreeNode interface.
    """

    adapts(Substation, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contains_VoltageLevels", "Contains_Bays", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contains_VoltageLevels", "Contains_Bays", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains_VoltageLevels',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Contains_Bays',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains_VoltageLevels',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Contains_Bays',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Substation'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (VoltageLevel, Bay, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contains_VoltageLevels", "Contains_Bays", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ConductingEquipmentAdapter" class:
#------------------------------------------------------------------------------

class ConductingEquipmentAdapter(ITreeNodeAdapter):
    """ Adapts a ConductingEquipment to implement the ITreeNode interface.
    """

    adapts(ConductingEquipment, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Terminals", "ProtectionEquipments", "ClearanceTags", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Terminals", "ProtectionEquipments", "ClearanceTags", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Terminals',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ProtectionEquipments',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ClearanceTags',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Terminals',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ProtectionEquipments',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ClearanceTags',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ConductingEquipment'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Terminal, ProtectionEquipment, ClearanceTag, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Terminals", "ProtectionEquipments", "ClearanceTags", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "IrregularTimePointAdapter" class:
#------------------------------------------------------------------------------

class IrregularTimePointAdapter(ITreeNodeAdapter):
    """ Adapts a IrregularTimePoint to implement the ITreeNode interface.
    """

    adapts(IrregularTimePoint, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "TimePoints for a schedule where the time between the points varies."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'IrregularTimePoint'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ConnectivityNodeContainerAdapter" class:
#------------------------------------------------------------------------------

class ConnectivityNodeContainerAdapter(ITreeNodeAdapter):
    """ Adapts a ConnectivityNodeContainer to implement the ITreeNode interface.
    """

    adapts(ConnectivityNodeContainer, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["TopologicalNode", "ConnectivityNodes", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["TopologicalNode", "ConnectivityNodes", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'TopologicalNode',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ConnectivityNodes',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'TopologicalNode',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ConnectivityNodes',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A base class for all objects that may contain ConnectivityNodes or TopologicalNodes."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ConnectivityNodeContainer'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (TopologicalNode, ConnectivityNode, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["TopologicalNode", "ConnectivityNodes", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "GeographicalRegionAdapter" class:
#------------------------------------------------------------------------------

class GeographicalRegionAdapter(ITreeNodeAdapter):
    """ Adapts a GeographicalRegion to implement the ITreeNode interface.
    """

    adapts(GeographicalRegion, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Regions", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Regions", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Regions',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Regions',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A geographical region of a power system network model."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'GeographicalRegion'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (SubGeographicalRegion, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Regions", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "UnitAdapter" class:
#------------------------------------------------------------------------------

class UnitAdapter(ITreeNodeAdapter):
    """ Adapts a Unit to implement the ITreeNode interface.
    """

    adapts(Unit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Controls", "ProtectionEquipments", "Measurements", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Controls", "ProtectionEquipments", "Measurements", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Controls',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ProtectionEquipments',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Controls',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ProtectionEquipments',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Unit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Control, ProtectionEquipment, Measurement, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Controls", "ProtectionEquipments", "Measurements", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EquipmentContainerAdapter" class:
#------------------------------------------------------------------------------

class EquipmentContainerAdapter(ITreeNodeAdapter):
    """ Adapts a EquipmentContainer to implement the ITreeNode interface.
    """

    adapts(EquipmentContainer, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contains_Equipments", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contains_Equipments", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains_Equipments',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contains_Equipments',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A modeling construct to provide a root class for all Equipment classes"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'EquipmentContainer'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Equipment, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contains_Equipments", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ModelingAuthorityAdapter" class:
#------------------------------------------------------------------------------

class ModelingAuthorityAdapter(ITreeNodeAdapter):
    """ Adapts a ModelingAuthority to implement the ITreeNode interface.
    """

    adapts(ModelingAuthority, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["ModelingAuthoritySets", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["ModelingAuthoritySets", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ModelingAuthoritySets',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ModelingAuthoritySets',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ModelingAuthority'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ModelingAuthoritySet, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["ModelingAuthoritySets", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "BaseVoltageAdapter" class:
#------------------------------------------------------------------------------

class BaseVoltageAdapter(ITreeNodeAdapter):
    """ Adapts a BaseVoltage to implement the ITreeNode interface.
    """

    adapts(BaseVoltage, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["ConductingEquipment", "VoltageLevel", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["ConductingEquipment", "VoltageLevel", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ConductingEquipment',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'VoltageLevel',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ConductingEquipment',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'VoltageLevel',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'BaseVoltage'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ConductingEquipment, VoltageLevel, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["ConductingEquipment", "VoltageLevel", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "OperatingShareAdapter" class:
#------------------------------------------------------------------------------

class OperatingShareAdapter(ITreeNodeAdapter):
    """ Adapts a OperatingShare to implement the ITreeNode interface.
    """

    adapts(OperatingShare, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Specifies the contract relationship between a PowerSystemResource and a contract participant."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'OperatingShare'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "BasicIntervalScheduleAdapter" class:
#------------------------------------------------------------------------------

class BasicIntervalScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a BasicIntervalSchedule to implement the ITreeNode interface.
    """

    adapts(BasicIntervalSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Schedule of values at points in time."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'BasicIntervalSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CurveDataAdapter" class:
#------------------------------------------------------------------------------

class CurveDataAdapter(ITreeNodeAdapter):
    """ Adapts a CurveData to implement the ITreeNode interface.
    """

    adapts(CurveData, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Data point values for defining a curve or schedule"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CurveData'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EquipmentAdapter" class:
#------------------------------------------------------------------------------

class EquipmentAdapter(ITreeNodeAdapter):
    """ Adapts a Equipment to implement the ITreeNode interface.
    """

    adapts(Equipment, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["OperationalLimitSet", "ContingencyEquipment", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["OperationalLimitSet", "ContingencyEquipment", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperationalLimitSet',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ContingencyEquipment',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperationalLimitSet',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ContingencyEquipment',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The parts of a power system that are physical devices, electronic or mechanical"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Equipment'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (OperationalLimitSet, ContingencyEquipment, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["OperationalLimitSet", "ContingencyEquipment", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RegularIntervalScheduleAdapter" class:
#------------------------------------------------------------------------------

class RegularIntervalScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a RegularIntervalSchedule to implement the ITreeNode interface.
    """

    adapts(RegularIntervalSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["TimePoints", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["TimePoints", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'TimePoints',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'TimePoints',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The schedule has TimePoints where the time between them is constant."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RegularIntervalSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (RegularTimePoint, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["TimePoints", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "IrregularIntervalScheduleAdapter" class:
#------------------------------------------------------------------------------

class IrregularIntervalScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a IrregularIntervalSchedule to implement the ITreeNode interface.
    """

    adapts(IrregularIntervalSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["TimePoints", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["TimePoints", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'TimePoints',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'TimePoints',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The schedule has TimePoints where the time between them varies."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'IrregularIntervalSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (IrregularTimePoint, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["TimePoints", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "BayAdapter" class:
#------------------------------------------------------------------------------

class BayAdapter(ITreeNodeAdapter):
    """ Adapts a Bay to implement the ITreeNode interface.
    """

    adapts(Bay, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Bay'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RegularTimePointAdapter" class:
#------------------------------------------------------------------------------

class RegularTimePointAdapter(ITreeNodeAdapter):
    """ Adapts a RegularTimePoint to implement the ITreeNode interface.
    """

    adapts(RegularTimePoint, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "TimePoints for a schedule where the time between the points is constant."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RegularTimePoint'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "TerminalAdapter" class:
#------------------------------------------------------------------------------

class TerminalAdapter(ITreeNodeAdapter):
    """ Adapts a Terminal to implement the ITreeNode interface.
    """

    adapts(Terminal, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["TieFlow", "OperationalLimitSet", "BranchGroupTerminal", "RegulatingControl", "Measurements", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["TieFlow", "OperationalLimitSet", "BranchGroupTerminal", "RegulatingControl", "Measurements", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'TieFlow',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'OperationalLimitSet',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'BranchGroupTerminal',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'RegulatingControl',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'TieFlow',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'OperationalLimitSet',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'BranchGroupTerminal',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'RegulatingControl',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Measurements',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Terminal'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (TieFlow, OperationalLimitSet, BranchGroupTerminal, RegulatingControl, Measurement, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["TieFlow", "OperationalLimitSet", "BranchGroupTerminal", "RegulatingControl", "Measurements", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SubGeographicalRegionAdapter" class:
#------------------------------------------------------------------------------

class SubGeographicalRegionAdapter(ITreeNodeAdapter):
    """ Adapts a SubGeographicalRegion to implement the ITreeNode interface.
    """

    adapts(SubGeographicalRegion, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Lines", "Substations", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Lines", "Substations", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Lines',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Substations',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Lines',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Substations',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A subset of a geographical region of a power system network model."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SubGeographicalRegion'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Line, Substation, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Lines", "Substations", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "PowerSystemResourceAdapter" class:
#------------------------------------------------------------------------------

class PowerSystemResourceAdapter(ITreeNodeAdapter):
    """ Adapts a PowerSystemResource to implement the ITreeNode interface.
    """

    adapts(PowerSystemResource, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "Contains_Measurements", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "Contains_Measurements", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperatedBy_Companies',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ReportingGroup',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'OperatingShare',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'PsrLists',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Contains_Measurements',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperatedBy_Companies',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ReportingGroup',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'OperatingShare',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'PsrLists',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Contains_Measurements',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'PowerSystemResource'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Company, ReportingGroup, OperatingShare, PsrList, Measurement, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "Contains_Measurements", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "BasePowerAdapter" class:
#------------------------------------------------------------------------------

class BasePowerAdapter(ITreeNodeAdapter):
    """ Adapts a BasePower to implement the ITreeNode interface.
    """

    adapts(BasePower, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The BasePower class defines the base power used in the per unit calculations."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'BasePower'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "PSRTypeAdapter" class:
#------------------------------------------------------------------------------

class PSRTypeAdapter(ITreeNodeAdapter):
    """ Adapts a PSRType to implement the ITreeNode interface.
    """

    adapts(PSRType, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["PowerSystemResource", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["PowerSystemResource", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'PowerSystemResource',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'PowerSystemResource',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'PSRType'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (PowerSystemResource, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["PowerSystemResource", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "PsrListAdapter" class:
#------------------------------------------------------------------------------

class PsrListAdapter(ITreeNodeAdapter):
    """ Adapts a PsrList to implement the ITreeNode interface.
    """

    adapts(PsrList, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["PowerSystemResources", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["PowerSystemResources", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'PowerSystemResources',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'PowerSystemResources',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'PsrList'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (PowerSystemResource, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["PowerSystemResources", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CompanyAdapter" class:
#------------------------------------------------------------------------------

class CompanyAdapter(ITreeNodeAdapter):
    """ Adapts a Company to implement the ITreeNode interface.
    """

    adapts(Company, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Operates_PSRs", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Operates_PSRs", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Operates_PSRs',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Operates_PSRs',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A company is a legal entity that owns and operates power system resources and is a party to interchange and transmission contracts."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Company'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (PowerSystemResource, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Operates_PSRs", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "IdentifiedObjectAdapter" class:
#------------------------------------------------------------------------------

class IdentifiedObjectAdapter(ITreeNodeAdapter):
    """ Adapts a IdentifiedObject to implement the ITreeNode interface.
    """

    adapts(IdentifiedObject, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "This is a root class to provide common naming attributes for all classes needing naming attributes"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'IdentifiedObject'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ContingencyAdapter" class:
#------------------------------------------------------------------------------

class ContingencyAdapter(ITreeNodeAdapter):
    """ Adapts a Contingency to implement the ITreeNode interface.
    """

    adapts(Contingency, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["ContingencyElement", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["ContingencyElement", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ContingencyElement',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ContingencyElement',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An event threatening system reliability, consisting of one or more contingency elements."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'Contingency'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ContingencyElement, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["ContingencyElement", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ContingencyEquipmentAdapter" class:
#------------------------------------------------------------------------------

class ContingencyEquipmentAdapter(ITreeNodeAdapter):
    """ Adapts a ContingencyEquipment to implement the ITreeNode interface.
    """

    adapts(ContingencyEquipment, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A equipment to which the in service status is to change such as a power transformer or AC line segment."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ContingencyEquipment'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ContingencyElementAdapter" class:
#------------------------------------------------------------------------------

class ContingencyElementAdapter(ITreeNodeAdapter):
    """ Adapts a ContingencyElement to implement the ITreeNode interface.
    """

    adapts(ContingencyElement, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ContingencyElement'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ClearanceTagTypeAdapter" class:
#------------------------------------------------------------------------------

class ClearanceTagTypeAdapter(ITreeNodeAdapter):
    """ Adapts a ClearanceTagType to implement the ITreeNode interface.
    """

    adapts(ClearanceTagType, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["ClearanceTags", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["ClearanceTags", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ClearanceTags',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ClearanceTags',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ClearanceTagType'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ClearanceTag, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["ClearanceTags", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SwitchingOperationAdapter" class:
#------------------------------------------------------------------------------

class SwitchingOperationAdapter(ITreeNodeAdapter):
    """ Adapts a SwitchingOperation to implement the ITreeNode interface.
    """

    adapts(SwitchingOperation, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Switches", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Switches", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Switches',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Switches',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SwitchingOperation'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Switch, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Switches", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "OutageScheduleAdapter" class:
#------------------------------------------------------------------------------

class OutageScheduleAdapter(ITreeNodeAdapter):
    """ Adapts a OutageSchedule to implement the ITreeNode interface.
    """

    adapts(OutageSchedule, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["SwitchingOperations", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["SwitchingOperations", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SwitchingOperations',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'SwitchingOperations',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'OutageSchedule'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (SwitchingOperation, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["SwitchingOperations", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ClearanceTagAdapter" class:
#------------------------------------------------------------------------------

class ClearanceTagAdapter(ITreeNodeAdapter):
    """ Adapts a ClearanceTag to implement the ITreeNode interface.
    """

    adapts(ClearanceTag, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ClearanceTag'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RemotePointAdapter" class:
#------------------------------------------------------------------------------

class RemotePointAdapter(ITreeNodeAdapter):
    """ Adapts a RemotePoint to implement the ITreeNode interface.
    """

    adapts(RemotePoint, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RemotePoint'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RemoteControlAdapter" class:
#------------------------------------------------------------------------------

class RemoteControlAdapter(ITreeNodeAdapter):
    """ Adapts a RemoteControl to implement the ITreeNode interface.
    """

    adapts(RemoteControl, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Remote controls are ouputs that are sent by the remote unit to actuators in the process."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RemoteControl'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RemoteSourceAdapter" class:
#------------------------------------------------------------------------------

class RemoteSourceAdapter(ITreeNodeAdapter):
    """ Adapts a RemoteSource to implement the ITreeNode interface.
    """

    adapts(RemoteSource, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Remote sources are state variables that are telemetered or calculated within the remote unit."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RemoteSource'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CommunicationLinkAdapter" class:
#------------------------------------------------------------------------------

class CommunicationLinkAdapter(ITreeNodeAdapter):
    """ Adapts a CommunicationLink to implement the ITreeNode interface.
    """

    adapts(CommunicationLink, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Contain_RemoteUnits", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Contain_RemoteUnits", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_RemoteUnits',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Contain_RemoteUnits',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CommunicationLink'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (RemoteUnit, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Contain_RemoteUnits", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RemoteUnitAdapter" class:
#------------------------------------------------------------------------------

class RemoteUnitAdapter(ITreeNodeAdapter):
    """ Adapts a RemoteUnit to implement the ITreeNode interface.
    """

    adapts(RemoteUnit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["MemberOf_CommunicationLinks", "Contains_RemotePoints", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["MemberOf_CommunicationLinks", "Contains_RemotePoints", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'MemberOf_CommunicationLinks',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Contains_RemotePoints',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'MemberOf_CommunicationLinks',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Contains_RemotePoints',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RemoteUnit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (CommunicationLink, RemotePoint, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["MemberOf_CommunicationLinks", "Contains_RemotePoints", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "OperationalLimitAdapter" class:
#------------------------------------------------------------------------------

class OperationalLimitAdapter(ITreeNodeAdapter):
    """ Adapts a OperationalLimit to implement the ITreeNode interface.
    """

    adapts(OperationalLimit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A value associated with a specific kind of limit."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'OperationalLimit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "BranchGroupAdapter" class:
#------------------------------------------------------------------------------

class BranchGroupAdapter(ITreeNodeAdapter):
    """ Adapts a BranchGroup to implement the ITreeNode interface.
    """

    adapts(BranchGroup, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["BranchGroupTerminal", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["BranchGroupTerminal", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'BranchGroupTerminal',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'BranchGroupTerminal',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'BranchGroup'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (BranchGroupTerminal, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["BranchGroupTerminal", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "OperationalLimitTypeAdapter" class:
#------------------------------------------------------------------------------

class OperationalLimitTypeAdapter(ITreeNodeAdapter):
    """ Adapts a OperationalLimitType to implement the ITreeNode interface.
    """

    adapts(OperationalLimitType, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["OperationalLimit", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["OperationalLimit", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperationalLimit',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperationalLimit',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A type of limit.  The meaning of a specific limit is described in this class."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'OperationalLimitType'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (OperationalLimit, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["OperationalLimit", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ActivePowerLimitAdapter" class:
#------------------------------------------------------------------------------

class ActivePowerLimitAdapter(ITreeNodeAdapter):
    """ Adapts a ActivePowerLimit to implement the ITreeNode interface.
    """

    adapts(ActivePowerLimit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Limit on active power flow."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ActivePowerLimit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CurrentLimitAdapter" class:
#------------------------------------------------------------------------------

class CurrentLimitAdapter(ITreeNodeAdapter):
    """ Adapts a CurrentLimit to implement the ITreeNode interface.
    """

    adapts(CurrentLimit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Operational limit on current."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CurrentLimit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "OperationalLimitSetAdapter" class:
#------------------------------------------------------------------------------

class OperationalLimitSetAdapter(ITreeNodeAdapter):
    """ Adapts a OperationalLimitSet to implement the ITreeNode interface.
    """

    adapts(OperationalLimitSet, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["OperationalLimitValue", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["OperationalLimitValue", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperationalLimitValue',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'OperationalLimitValue',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'OperationalLimitSet'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (OperationalLimit, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["OperationalLimitValue", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "VoltageLimitAdapter" class:
#------------------------------------------------------------------------------

class VoltageLimitAdapter(ITreeNodeAdapter):
    """ Adapts a VoltageLimit to implement the ITreeNode interface.
    """

    adapts(VoltageLimit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Operational limit applied to voltage."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'VoltageLimit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "BranchGroupTerminalAdapter" class:
#------------------------------------------------------------------------------

class BranchGroupTerminalAdapter(ITreeNodeAdapter):
    """ Adapts a BranchGroupTerminal to implement the ITreeNode interface.
    """

    adapts(BranchGroupTerminal, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A specific directed terminal flow for a branch group."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'BranchGroupTerminal'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ApparentPowerLimitAdapter" class:
#------------------------------------------------------------------------------

class ApparentPowerLimitAdapter(ITreeNodeAdapter):
    """ Adapts a ApparentPowerLimit to implement the ITreeNode interface.
    """

    adapts(ApparentPowerLimit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Apparent power limit."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ApparentPowerLimit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ControlAreaGeneratingUnitAdapter" class:
#------------------------------------------------------------------------------

class ControlAreaGeneratingUnitAdapter(ITreeNodeAdapter):
    """ Adapts a ControlAreaGeneratingUnit to implement the ITreeNode interface.
    """

    adapts(ControlAreaGeneratingUnit, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["AltGeneratingUnitMeas", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["AltGeneratingUnitMeas", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'AltGeneratingUnitMeas',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'AltGeneratingUnitMeas',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ControlAreaGeneratingUnit'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (AltGeneratingUnitMeas, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["AltGeneratingUnitMeas", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ControlAreaAdapter" class:
#------------------------------------------------------------------------------

class ControlAreaAdapter(ITreeNodeAdapter):
    """ Adapts a ControlArea to implement the ITreeNode interface.
    """

    adapts(ControlArea, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["BusNameMarker", "TopologicalNode", "ControlAreaGeneratingUnit", "TieFlow", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["BusNameMarker", "TopologicalNode", "ControlAreaGeneratingUnit", "TieFlow", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'BusNameMarker',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TopologicalNode',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ControlAreaGeneratingUnit',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TieFlow',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'BusNameMarker',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TopologicalNode',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ControlAreaGeneratingUnit',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'TieFlow',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ControlArea'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (BusNameMarker, TopologicalNode, ControlAreaGeneratingUnit, TieFlow, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["BusNameMarker", "TopologicalNode", "ControlAreaGeneratingUnit", "TieFlow", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AltGeneratingUnitMeasAdapter" class:
#------------------------------------------------------------------------------

class AltGeneratingUnitMeasAdapter(ITreeNodeAdapter):
    """ Adapts a AltGeneratingUnitMeas to implement the ITreeNode interface.
    """

    adapts(AltGeneratingUnitMeas, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A prioritized measurement to be used for the generating unit in the control area specificaiton."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'AltGeneratingUnitMeas'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "TieFlowAdapter" class:
#------------------------------------------------------------------------------

class TieFlowAdapter(ITreeNodeAdapter):
    """ Adapts a TieFlow to implement the ITreeNode interface.
    """

    adapts(TieFlow, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["AltTieMeas", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["AltTieMeas", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'AltTieMeas',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'AltTieMeas',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A flow specification in terms of location and direction for a control area."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'TieFlow'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (AltTieMeas, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["AltTieMeas", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "AltTieMeasAdapter" class:
#------------------------------------------------------------------------------

class AltTieMeasAdapter(ITreeNodeAdapter):
    """ Adapts a AltTieMeas to implement the ITreeNode interface.
    """

    adapts(AltTieMeas, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A prioritized measurement to be used for the tie flow as part of the control area specification."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'AltTieMeas'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EquivalentBranchAdapter" class:
#------------------------------------------------------------------------------

class EquivalentBranchAdapter(ITreeNodeAdapter):
    """ Adapts a EquivalentBranch to implement the ITreeNode interface.
    """

    adapts(EquivalentBranch, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The class represents equivalent branches."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'EquivalentBranch'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EquivalentShuntAdapter" class:
#------------------------------------------------------------------------------

class EquivalentShuntAdapter(ITreeNodeAdapter):
    """ Adapts a EquivalentShunt to implement the ITreeNode interface.
    """

    adapts(EquivalentShunt, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The class represents equivalent shunts."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'EquivalentShunt'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EquivalentNetworkAdapter" class:
#------------------------------------------------------------------------------

class EquivalentNetworkAdapter(ITreeNodeAdapter):
    """ Adapts a EquivalentNetwork to implement the ITreeNode interface.
    """

    adapts(EquivalentNetwork, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["EquivalentEquipments", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["EquivalentEquipments", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'EquivalentEquipments',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'EquivalentEquipments',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'EquivalentNetwork'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (EquivalentEquipment, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["EquivalentEquipments", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "EquivalentEquipmentAdapter" class:
#------------------------------------------------------------------------------

class EquivalentEquipmentAdapter(ITreeNodeAdapter):
    """ Adapts a EquivalentEquipment to implement the ITreeNode interface.
    """

    adapts(EquivalentEquipment, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'EquivalentEquipment'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "TopologicalNodeAdapter" class:
#------------------------------------------------------------------------------

class TopologicalNodeAdapter(ITreeNodeAdapter):
    """ Adapts a TopologicalNode to implement the ITreeNode interface.
    """

    adapts(TopologicalNode, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["ConnectivityNodes", "Terminal", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["ConnectivityNodes", "Terminal", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ConnectivityNodes',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Terminal',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ConnectivityNodes',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'Terminal',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state)."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'TopologicalNode'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ConnectivityNode, Terminal, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["ConnectivityNodes", "Terminal", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "TopologicalIslandAdapter" class:
#------------------------------------------------------------------------------

class TopologicalIslandAdapter(ITreeNodeAdapter):
    """ Adapts a TopologicalIsland to implement the ITreeNode interface.
    """

    adapts(TopologicalIsland, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["TopologicalNodes", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["TopologicalNodes", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'TopologicalNodes',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'TopologicalNodes',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state)."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'TopologicalIsland'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (TopologicalNode, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["TopologicalNodes", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ConnectivityNodeAdapter" class:
#------------------------------------------------------------------------------

class ConnectivityNodeAdapter(ITreeNodeAdapter):
    """ Adapts a ConnectivityNode to implement the ITreeNode interface.
    """

    adapts(ConnectivityNode, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Terminals", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Terminals", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Terminals',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Terminals',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ConnectivityNode'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (Terminal, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Terminals", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "BusNameMarkerAdapter" class:
#------------------------------------------------------------------------------

class BusNameMarkerAdapter(ITreeNodeAdapter):
    """ Adapts a BusNameMarker to implement the ITreeNode interface.
    """

    adapts(BusNameMarker, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["ConnectivityNode", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["ConnectivityNode", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ConnectivityNode',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'ConnectivityNode',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'BusNameMarker'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ConnectivityNode, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["ConnectivityNode", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "SynchrocheckRelayAdapter" class:
#------------------------------------------------------------------------------

class SynchrocheckRelayAdapter(ITreeNodeAdapter):
    """ Adapts a SynchrocheckRelay to implement the ITreeNode interface.
    """

    adapts(SynchrocheckRelay, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'SynchrocheckRelay'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "ProtectionEquipmentAdapter" class:
#------------------------------------------------------------------------------

class ProtectionEquipmentAdapter(ITreeNodeAdapter):
    """ Adapts a ProtectionEquipment to implement the ITreeNode interface.
    """

    adapts(ProtectionEquipment, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return True

    def has_children(self):
        """ Returns whether the object has children.
        """
        attrs = ["Operates_Breakers", "ConductingEquipments", ]
        children = [len( getattr(self.adaptee, attr) ) for attr in attrs]
        return ( max(children) > 0 )


    def get_children(self):
        """ Gets the object's children.
        """
        attrs = ["Operates_Breakers", "ConductingEquipments", ]
        children = [getattr(self.adaptee, attr) for attr in attrs]
        return [x for c in children for x in c]


    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Operates_Breakers',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ConductingEquipments',
            remove=remove, dispatch='ui')


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """
        self.adaptee.on_trait_change(listener, 'Operates_Breakers',
            remove=remove, dispatch='ui')
        self.adaptee.on_trait_change(listener, 'ConductingEquipments',
            remove=remove, dispatch='ui')


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<open>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'ProtectionEquipment'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = (ProtectedSwitch, ConductingEquipment, )
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return True

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return ["Operates_Breakers", "ConductingEquipments", ]


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "CurrentRelayAdapter" class:
#------------------------------------------------------------------------------

class CurrentRelayAdapter(ITreeNodeAdapter):
    """ Adapts a CurrentRelay to implement the ITreeNode interface.
    """

    adapts(CurrentRelay, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A device that checks current flow values in any direction or designated direction"


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'CurrentRelay'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")
#------------------------------------------------------------------------------
#  "RecloseSequenceAdapter" class:
#------------------------------------------------------------------------------

class RecloseSequenceAdapter(ITreeNodeAdapter):
    """ Adapts a RecloseSequence to implement the ITreeNode interface.
    """

    adapts(RecloseSequence, ITreeNode)

    #--------------------------------------------------------------------------
    #  "ITreeNodeAdapter" interface:
    #--------------------------------------------------------------------------

    def allows_children(self):
        """ Returns whether this object can have children.
        """
        return False



    def when_children_replaced(self, listener, remove):
        """ Sets up or removes a listener for children being replaced on a
            specified object.
        """


    def when_children_changed ( self, listener, remove ):
        """ Sets up or removes a listener for children being changed on a
            specified object.
        """


    def get_label(self):
        """ Gets the label to display for a specified object.
        """
        if hasattr(self.adaptee, "name"):
            return self.adaptee.name
        else:
            return ""


#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[Action(name='Create',
#            action='node.adapter.append_child')])


    def get_tooltip(self):
        """ Gets the tooltip to display for a specified object.
        """
        return "A reclose sequence (open and close) is defined for each possible reclosure of a breaker."


    def get_icon(self, is_expanded):
        """ Returns the icon for a specified object.
        """
        return '<item>'

    def get_icon_path ( self ):
        """ Returns the path used to locate an object's icon.
        """
        return IMAGE_PATH


    def get_name ( self ):
        """ Returns the name to use when adding a new object instance
            (displayed in the "New" submenu).
        """
        return 'RecloseSequence'


    def get_view ( self ):
        """ Gets the view to use when editing an object.
        """
        return None


    def can_rename(self):
        """ Returns whether the object's children can be renamed.
        """
        return True


    def can_copy(self):
        """ Returns whether the object's children can be copied.
        """
        return True


#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True


    def can_delete_me ( self ):
        """ Returns whether the object can be deleted.
        """
        return True


    def confirm_delete(self):
        """ Checks whether a specified object can be deleted.

          Returns
          -------
          * **True** if the object should be deleted with no further prompting.
          * **False** if the object should not be deleted.
          * Anything else: Caller should take its default action (which might
            include prompting the user to confirm deletion).
        """
        return True


#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        pass


    def can_add ( self, add_object ):
        """ Returns whether a given object is droppable on the node.
        """
        valid = ()
        return isinstance(add_object, valid)


    def can_insert ( self ):
        """ Returns whether the object's children can be inserted (vs.
            appended).
        """
        return False

    def append_child ( self, child ):
        """ Appends a child to the object's children.
        """
        pass


    def insert_child ( self, index, child ):
        """ Inserts a child into the object's children.
        """
        pass


    def get_add ( self ):
        """ Returns the list of classes that can be added to the object.
        """
        return []


    def dclick ( self ):
        """ Handles an object being double-clicked.
        """
        self.adaptee.edit_traits(kind="livemodal")

# EOF -------------------------------------------------------------------------
