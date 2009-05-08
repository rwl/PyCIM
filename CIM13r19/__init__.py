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

""" Defines IEC standard 61970.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------




from enthought.traits.api import HasTraits, Instance, List, Property, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "Element" class:
#------------------------------------------------------------------------------

class Element(HasTraits):
    """ Base class for Common Information Model elements.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Parent = Instance("CIM13r19.CommonInformationModel",
        transient=True,
        editor=InstanceEditor(name="_commoninformationmodels"))

    def _get_commoninformationmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.CommonInformationModel" ]
        else:
            return []

    _commoninformationmodels = Property(fget=_get_commoninformationmodels)

    #--------------------------------------------------------------------------
    #  Begin "Element" user definitions:
    #--------------------------------------------------------------------------

    traits_view = View(Tabbed(
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM13r19.Element",
        title="Element",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)


    def __init__(self, **traits):
        super(Element, self).__init__(**traits)
        # Dictionary of trait definitions matching the given metadata. Metadata
        # values may be lambda expressions or functions that return True
        # if the trait attribute is to be included.
        opposed = self.traits(opposite = lambda val: bool(val))

#        print "OPPOSITES:", self, opposed.keys()

        for name, trait in opposed.iteritems():
            if trait.is_trait_type( Instance ):
#                print "Instance handler:", self, name
                self.on_trait_change(self._on_instance, name)

            elif trait.is_trait_type( List ):# and \
#                trait.inner_traits[0].is_trait_type( Instance ):
#                print "List handler:", self, name
                self.on_trait_change(self._on_list, name)
                self.on_trait_change(self._on_list, name + "_items")

        # Fire trait change events for any traits specified.
        for trait_name, value in traits.iteritems():
            self.trait_property_changed(trait_name,
                getattr(self, trait_name), value)

    #--------------------------------------------------------------------------
    #  Event handlers:
    #--------------------------------------------------------------------------

    def _on_instance(self, obj, name, old, new):
        """ Handles traits of type Instance changing.
        """
        opposite = obj.trait(name).opposite

#        print "ON INSTANCE:", obj, name, old, new

        if old is not None:
            opposite_trait = old.trait(opposite)
            # Unset old one-to-one association.
            if opposite_trait.is_trait_type( Instance ):
#                print "Unsetting one-to-one:", old, opposite
                setattr(old, opposite, None)
            # Remove instance from old one-to-many association.
            elif opposite_trait.is_trait_type( List ) and \
                (obj in getattr(old, opposite)):
#                print "Removing one-to-many:", old, opposite
                getattr(old, opposite).remove(obj)

        if new is not None:
            opposite_trait = new.trait(opposite)
            # Set new one-to-one association.
            if opposite_trait.is_trait_type( Instance ):
#                print "Setting one-to-one:", new, opposite
                setattr(new, opposite, obj)
            # Set new one-to-many association.
            elif opposite_trait.is_trait_type( List ) and \
                (obj not in getattr(new, opposite)):
#                print "Setting one-to-many:", new, opposite
                getattr(new, opposite).append(obj)


    def _on_list(self, obj, name, old, new):
        """ Handles List instances changing.
        """
#        print "ON LIST:", obj, name, old, new
        # Use the same method for the list being set and for items being
        # added and removed from the list.  When individual items are changed
        # the last argument is an event with '.added' and '.removed' traits.
        if isinstance(new, TraitListEvent):
            old = new.removed
            new = new.added

        # Name of the trait on the referenced object that is the 'opposite'
        # reference back to obj.
        opposite = obj.trait(name).opposite

        for old_obj in old:
            opposite_trait = old_obj.trait(opposite)
            # Unset old many-to-one associations.
            if opposite_trait.is_trait_type( Instance ):
#                print "Unsetting many-to-one:", old_obj, opposite
                setattr(old_obj, opposite, None)
            # Remove instance from old many-to-many associtaions.
            elif opposite_trait.is_trait_type( List ) and \
                (old_obj in getattr(old_obj, opposite)):
#                print "Removing many-to-many:", old_obj, opposite
                getattr(old_obj, opposite).remove(obj)

        for new_obj in new:
            opposite_trait = new_obj.trait(opposite)
            # Set new many-to-one associations.
            if opposite_trait.is_trait_type( Instance ):
#                print "Setting many-to-one:", new_obj, opposite
                setattr(new_obj, opposite, obj)
            # Set new many-to-many associations.
            elif opposite_trait.is_trait_type( List ) and \
                (new_obj not in getattr(new_obj, opposite)):
#                print "Setting many-to-many:", getattr(new_obj, opposite)
                getattr(new_obj, opposite).append(obj)

    #--------------------------------------------------------------------------
    #  End "Element" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CommonInformationModel" class:
#------------------------------------------------------------------------------

class CommonInformationModel(HasTraits):
    """ Defines a container of model elements conforming to IEC standard 61970.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Elements = List(Instance("CIM13r19.Element"))

    #--------------------------------------------------------------------------
    #  Begin "CommonInformationModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("Elements",
                label="References"),
            dock="tab"),
        id="CIM13r19.CommonInformationModel",
        title="CommonInformationModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CommonInformationModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IEC61970CIMVersion" class:
#------------------------------------------------------------------------------

class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version.   For ecample IEC61970CIM13v18.
    version = Str(desc="Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version.   For ecample IEC61970CIM13v18.")

    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date = Str(desc="Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.")

    #--------------------------------------------------------------------------
    #  Begin "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("version", "date",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM13r19.IEC61970CIMVersion",
        title="IEC61970CIMVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
