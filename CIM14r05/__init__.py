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

    Parent = Instance("CIM14r05.CommonInformationModel",
        transient=True,
        opposite="Elements",
        editor=InstanceEditor(name="_commoninformationmodels"))

    def _get_commoninformationmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.CommonInformationModel" ]
        else:
            return []

    _commoninformationmodels = Property(fget=_get_commoninformationmodels)

    #--------------------------------------------------------------------------
    #  Begin "Element" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM14r05.Element",
        title="Element",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

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

    Elements = List(Instance("CIM14r05.Element"))

    #--------------------------------------------------------------------------
    #  Begin "CommonInformationModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("Elements",
                label="References"),
            dock="tab"),
        id="CIM14r05.CommonInformationModel",
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

    # The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008.
    date = Str(desc="The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008.")

    # Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.
    version = Str(desc="Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.")

    #--------------------------------------------------------------------------
    #  Begin "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("date", "version",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM14r05.IEC61970CIMVersion",
        title="IEC61970CIMVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
