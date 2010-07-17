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

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------




from enthought.traits.api import HasTraits, Date, Str
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
    UUID = Str

    #--------------------------------------------------------------------------
    #  Begin "Element" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            
            dock="tab"),
        id="CIM.Element",
        title="Element",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Element" user definitions:
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
    date = Date(desc="The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008.")

    # Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.
    version = Str(desc="Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.")

    #--------------------------------------------------------------------------
    #  Begin "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "date", "version",
                label="Attributes"),
            
            dock="tab"),
        id="CIM.IEC61970CIMVersion",
        title="IEC61970CIMVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
