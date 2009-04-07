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




from enthought.traits.api import HasTraits, Instance, List, Str
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "Root" class:
#------------------------------------------------------------------------------

class Root(HasTraits):
    ContainedBy = Instance("CIM13.Model")

    URI = Str

    #--------------------------------------------------------------------------
    #  Begin root user definitions:
    #--------------------------------------------------------------------------

    def __init__(self, **traits):
        super(Root, self).__init__(**traits)

        opposed = self.traits(opposite = lambda val: bool(val))

        for name, trait in opposed.iteritems():
            if trait.is_trait_type( Instance ):
                self.on_trait_change(self._on_instance, name)

            elif trait.is_trait_type( List ):# and \
#                trait.inner_traits[0].is_trait_type( Instance ):
                self.on_trait_change(self._on_list, name)
                self.on_trait_change(self._on_list, name + "_items")


    def _on_instance(self, obj, name, old, new):
        opposite = obj.trait(name).opposite

        if old is not None:
            opposite_trait = old.trait(opposite)

            if opposite_trait.is_trait_type( Instance ):
                setattr(old, opposite, None)

            elif opposite_trait.is_trait_type( List ) and \
                (obj in getattr(old, opposite)):
                    getattr(old, opposite).remove(obj)

        if new is not None:
            opposite_trait = new.trait(opposite)

            if opposite_trait.is_trait_type( Instance ):
                setattr(new, opposite, obj)

            elif opposite_trait.is_trait_type( List ) and \
                (obj not in getattr(new, opposite)):
                    getattr(new, opposite).append(obj)


    def _on_list(self, obj, name, old, new):

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

            if opposite_trait.is_trait_type( Instance ):
                setattr(old_obj, opposite, None)

            elif opposite_trait.is_trait_type( List ) and \
                (old_obj in getattr(old_obj, opposite)):
                    getattr(old_obj, opposite).remove(obj)

        for new_obj in new:
            opposite_trait = new_obj.trait(opposite)

            if opposite_trait.is_trait_type( Instance ):
                setattr(new_obj, opposite, obj)

            elif opposite_trait.is_trait_type( List ) and \
                (new_obj not in getattr(new_obj, opposite)):
                    getattr(new_obj, opposite).append(obj)

    #--------------------------------------------------------------------------
    #  End root user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Model" class:
#------------------------------------------------------------------------------

class Model(HasTraits):
    Contains = List(Instance("CIM13.Root"))

    #--------------------------------------------------------------------------
    #  Begin model user definitions:
    #--------------------------------------------------------------------------

    def load(self, fileName):
        """ Loads a model from a CIM RDF/XML file.
        """
        pass

    #--------------------------------------------------------------------------
    #  End model user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IEC61970CIMVersion" class:
#------------------------------------------------------------------------------

class IEC61970CIMVersion(Root):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version.   For ecample IEC61970CIM13v18.
    version = Str

    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date = Str

    #--------------------------------------------------------------------------
    #  Begin iEC61970CIMVersion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End iEC61970CIMVersion user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Package" class:
#------------------------------------------------------------------------------

class Package(Root):
    pass
    #--------------------------------------------------------------------------
    #  Begin package user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End package user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Stereotype" class:
#------------------------------------------------------------------------------

class Stereotype(Root):
    pass
    #--------------------------------------------------------------------------
    #  Begin stereotype user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End stereotype user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
