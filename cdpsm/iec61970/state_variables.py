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

""" State variables for analysis solutions such as powerflow.State variables for analysis solutions such as powerflow.
"""

from cdpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_StateVariables"

class SvTapStep(Element):
    """ State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.
    """
    # <<< sv_tap_step
    # @generated
    def __init__(self, continuous_position=0.0, position=0, tap_changer=None, **kw_args):
        """ Initialises a new 'SvTapStep' instance.
        """
        # The floating point tap position.The floating point tap position. 
        self.continuous_position = continuous_position

        # The integer tap position.The integer tap position. 
        self.position = position


        self._tap_changer = None
        self.tap_changer = tap_changer


        super(SvTapStep, self).__init__(**kw_args)
    # >>> sv_tap_step

    # <<< tap_changer
    # @generated
    def get_tap_changer(self):
        """ The tap changer associated with the tap step state.The tap changer associated with the tap step state.
        """
        return self._tap_changer

    def set_tap_changer(self, value):
        if self._tap_changer is not None:
            self._tap_changer._sv_tap_step = None

        self._tap_changer = value
        if self._tap_changer is not None:
            self._tap_changer._sv_tap_step = self

    tap_changer = property(get_tap_changer, set_tap_changer)
    # >>> tap_changer


    def __str__(self):
        """ Returns a string representation of the SvTapStep.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sv_tap_step.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SvTapStep.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SvTapStep", self.uri)
        if format:
            indent += ' ' * depth

        if self.tap_changer is not None:
            s += '%s<%s:SvTapStep.tap_changer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.tap_changer.uri)
        s += '%s<%s:SvTapStep.continuous_position>%s</%s:SvTapStep.continuous_position>' % \
            (indent, ns_prefix, self.continuous_position, ns_prefix)
        s += '%s<%s:SvTapStep.position>%s</%s:SvTapStep.position>' % \
            (indent, ns_prefix, self.position, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvTapStep")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_tap_step.serialize


# <<< state_variables
# @generated
# >>> state_variables
