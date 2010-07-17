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



# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#"

class Element(object):
    # <<< element
    # @generated
    def __init__(self, uri='', model=None, **kw_args):
        """ Initialises a new 'Element' instance.
        """
 
        self.uri = uri


        self._model = None
        self.model = model


        super(Element, self).__init__(**kw_args)
    # >>> element

    # <<< model
    # @generated
    def get_model(self):
        """ 
        """
        return self._model

    def set_model(self, value):
        if self._model is not None:
            filtered = [x for x in self.model.elements if x != self]
            self._model._elements = filtered

        self._model = value
        if self._model is not None:
            self._model._elements.append(self)

    model = property(get_model, set_model)
    # >>> model


    def __str__(self):
        """ Returns a string representation of the Element.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< element.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Element.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Element", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Element")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> element.serialize


class Model(object):
    # <<< model
    # @generated
    def __init__(self, uri='', elements=None, **kw_args):
        """ Initialises a new 'Model' instance.
        """
 
        self.uri = uri


        self._elements = []
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []


        super(Model, self).__init__(**kw_args)
    # >>> model

    # <<< elements
    # @generated
    def get_elements(self):
        """ 
        """
        return self._elements

    def set_elements(self, value):
        for x in self._elements:
            x._model = None
        for y in value:
            y._model = self
        self._elements = value

    elements = property(get_elements, set_elements)

    def add_elements(self, *elements):
        for obj in elements:
            obj._model = self
            self._elements.append(obj)

    def remove_elements(self, *elements):
        for obj in elements:
            obj._model = None
            self._elements.remove(obj)
    # >>> elements


    def __str__(self):
        """ Returns a string representation of the Model.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< model.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Model.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Model", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.elements:
            s += '%s<%s:Model.elements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Model.uri>%s</%s:Model.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Model")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> model.serialize


class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.This is the UCTE profile.     We have been using file naming conventions, the profile namespace, and comments here in the profile under IEC61970CIMVersion class.  Profile1_v9 - dated 2009-01-27   - removed SeriesCompensator and ApparentPowerLimit, added TopologicalNode.equivalent  Profile1_v10 - dated 2009-01-29  - documentation added on Terminal.sequenceNumber.  Added notes to GeneratingUnit.normalPF attribute in profile.  Profile1_v11 - dated 2009-02-04  - Made optional SynchronousMachine.InitialReactiveCapabilityCurve, minQ, maxQ.    Rename of SvTapStep.tapRatio to SvTapStep.continuousPosition.   Multiplicity for SvShuntCompensatorSections.continuousSections made manditory.   Removed SvShuntCompensatorSections.sections and SvTapStep.position from profile.  Profile 1_v12 - dated 2009-03-17 - Made all Short Circuit classes and Attributes Optional, made all voltage dependency / coeficient model attributes Optional, added notes from the UCTE Mapping Spreadsheet and added a few clarification notes.  Profile 1_v13 - dated 2009-03-19 - Made the GeneratingUnit.maximumAllowableSpinningReserve Optional and made all of the PhaseTapChanger attributes Optional.  Profile 1_v14 - dated 2009-05-10 - Added some comments to classes based on input from IOP test and added BusBarSection and Line Classes.This is the IEC 61970 CIM version number assigned to this UML model file.This is the UCTE profile.     We have been using file naming conventions, the profile namespace, and comments here in the profile under IEC61970CIMVersion class.  Profile1_v9 - dated 2009-01-27   - removed SeriesCompensator and ApparentPowerLimit, added TopologicalNode.equivalent  Profile1_v10 - dated 2009-01-29  - documentation added on Terminal.sequenceNumber.  Added notes to GeneratingUnit.normalPF attribute in profile.  Profile1_v11 - dated 2009-02-04  - Made optional SynchronousMachine.InitialReactiveCapabilityCurve, minQ, maxQ.    Rename of SvTapStep.tapRatio to SvTapStep.continuousPosition.   Multiplicity for SvShuntCompensatorSections.continuousSections made manditory.   Removed SvShuntCompensatorSections.sections and SvTapStep.position from profile.  Profile 1_v12 - dated 2009-03-17 - Made all Short Circuit classes and Attributes Optional, made all voltage dependency / coeficient model attributes Optional, added notes from the UCTE Mapping Spreadsheet and added a few clarification notes.  Profile 1_v13 - dated 2009-03-19 - Made the GeneratingUnit.maximumAllowableSpinningReserve Optional and made all of the PhaseTapChanger attributes Optional.  Profile 1_v14 - dated 2009-05-10 - Added some comments to classes based on input from IOP test and added BusBarSection and Line Classes.
    """
    # <<< iec61970_cimversion
    # @generated
    def __init__(self, date='', version='', **kw_args):
        """ Initialises a new 'IEC61970CIMVersion' instance.
        """
        # The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008.The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008. 
        self.date = date

        # Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.Please see the profile comments on the IEC61970CIMVersion class for the profile version comments. Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.Please see the profile comments on the IEC61970CIMVersion class for the profile version comments.  
        self.version = version



        super(IEC61970CIMVersion, self).__init__(**kw_args)
    # >>> iec61970_cimversion


    def __str__(self):
        """ Returns a string representation of the IEC61970CIMVersion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< iec61970_cimversion.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the IEC61970CIMVersion.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "IEC61970CIMVersion", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:IEC61970CIMVersion.date>%s</%s:IEC61970CIMVersion.date>' % \
            (indent, ns_prefix, self.date, ns_prefix)
        s += '%s<%s:IEC61970CIMVersion.version>%s</%s:IEC61970CIMVersion.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "IEC61970CIMVersion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> iec61970_cimversion.serialize


# <<< ucte
# @generated
# >>> ucte
