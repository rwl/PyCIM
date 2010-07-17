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




from enthought.traits.api import HasTraits, Instance, List, Property, Str, Date
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
    Model = Instance("UCTE.Model", allow_none=False,
        transient=True,
        opposite="Elements",
        editor=InstanceEditor(name="_models"))

    def _get_models(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Model" ]
        else:
            return []

    _models = Property(fget=_get_models)

    URI = Str

    #--------------------------------------------------------------------------
    #  Begin "Element" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="UCTE.Element",
        title="Element",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Element" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Model" class:
#------------------------------------------------------------------------------

class Model(HasTraits):
    Elements = List(Instance("UCTE.Element"))

    URI = Str

    #--------------------------------------------------------------------------
    #  Begin "Model" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Elements",
                label="References"),
            dock="tab"),
        id="UCTE.Model",
        title="Model",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Model" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IEC61970CIMVersion" class:
#------------------------------------------------------------------------------

class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.This is the UCTE profile.     We have been using file naming conventions, the profile namespace, and comments here in the profile under IEC61970CIMVersion class.  Profile1_v9 - dated 2009-01-27   - removed SeriesCompensator and ApparentPowerLimit, added TopologicalNode.equivalent  Profile1_v10 - dated 2009-01-29  - documentation added on Terminal.sequenceNumber.  Added notes to GeneratingUnit.normalPF attribute in profile.  Profile1_v11 - dated 2009-02-04  - Made optional SynchronousMachine.InitialReactiveCapabilityCurve, minQ, maxQ.    Rename of SvTapStep.tapRatio to SvTapStep.continuousPosition.   Multiplicity for SvShuntCompensatorSections.continuousSections made manditory.   Removed SvShuntCompensatorSections.sections and SvTapStep.position from profile.  Profile 1_v12 - dated 2009-03-17 - Made all Short Circuit classes and Attributes Optional, made all voltage dependency / coeficient model attributes Optional, added notes from the UCTE Mapping Spreadsheet and added a few clarification notes.  Profile 1_v13 - dated 2009-03-19 - Made the GeneratingUnit.maximumAllowableSpinningReserve Optional and made all of the PhaseTapChanger attributes Optional.  Profile 1_v14 - dated 2009-05-10 - Added some comments to classes based on input from IOP test and added BusBarSection and Line Classes.This is the IEC 61970 CIM version number assigned to this UML model file.This is the UCTE profile.     We have been using file naming conventions, the profile namespace, and comments here in the profile under IEC61970CIMVersion class.  Profile1_v9 - dated 2009-01-27   - removed SeriesCompensator and ApparentPowerLimit, added TopologicalNode.equivalent  Profile1_v10 - dated 2009-01-29  - documentation added on Terminal.sequenceNumber.  Added notes to GeneratingUnit.normalPF attribute in profile.  Profile1_v11 - dated 2009-02-04  - Made optional SynchronousMachine.InitialReactiveCapabilityCurve, minQ, maxQ.    Rename of SvTapStep.tapRatio to SvTapStep.continuousPosition.   Multiplicity for SvShuntCompensatorSections.continuousSections made manditory.   Removed SvShuntCompensatorSections.sections and SvTapStep.position from profile.  Profile 1_v12 - dated 2009-03-17 - Made all Short Circuit classes and Attributes Optional, made all voltage dependency / coeficient model attributes Optional, added notes from the UCTE Mapping Spreadsheet and added a few clarification notes.  Profile 1_v13 - dated 2009-03-19 - Made the GeneratingUnit.maximumAllowableSpinningReserve Optional and made all of the PhaseTapChanger attributes Optional.  Profile 1_v14 - dated 2009-05-10 - Added some comments to classes based on input from IOP test and added BusBarSection and Line Classes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008.The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008.
    date = Date(desc="The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008.The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008.")

    # Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.Please see the profile comments on the IEC61970CIMVersion class for the profile version comments. Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.Please see the profile comments on the IEC61970CIMVersion class for the profile version comments. 
    version = Str(desc="Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.Please see the profile comments on the IEC61970CIMVersion class for the profile version comments. Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.Please see the profile comments on the IEC61970CIMVersion class for the profile version comments. ")

    #--------------------------------------------------------------------------
    #  Begin "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "date", "version",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="UCTE.IEC61970CIMVersion",
        title="IEC61970CIMVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
