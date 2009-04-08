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
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid
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
    #  Begin "Root" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("ContainedBy",
                label="References"),
            dock="tab"),
        id="CIM13.Root",
        title="Root",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Root" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Model" class:
#------------------------------------------------------------------------------

class Model(HasTraits):
    Contains = List(Instance("CIM13.Root"))

    #--------------------------------------------------------------------------
    #  Begin "Model" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("Contains",
                label="References"),
            dock="tab"),
        id="CIM13.Model",
        title="Model",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Model" user definitions:
    #--------------------------------------------------------------------------
    # <<< saveToFile
    @classmethod
    def saveToFile(cls, fileName, kwargs, format):
        """ Save the object to file given by filename.
            @generated
        """
        pass
    # >>> saveToFile

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
    version = Str(desc="Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version.   For ecample IEC61970CIM13v18.")

    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date = Str(desc="Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.")

    #--------------------------------------------------------------------------
    #  Begin "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "version", "date",
                label="Attributes"),
            VGroup("ContainedBy",
                label="References"),
            dock="tab"),
        id="CIM13.IEC61970CIMVersion",
        title="IEC61970CIMVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Package" class:
#------------------------------------------------------------------------------

class Package(Root):
    pass
    #--------------------------------------------------------------------------
    #  Begin "Package" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("ContainedBy",
                label="References"),
            dock="tab"),
        id="CIM13.Package",
        title="Package",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Package" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Stereotype" class:
#------------------------------------------------------------------------------

class Stereotype(Root):
    pass
    #--------------------------------------------------------------------------
    #  Begin "Stereotype" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("ContainedBy",
                label="References"),
            dock="tab"),
        id="CIM13.Stereotype",
        title="Stereotype",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Stereotype" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
