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

""" An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.
"""

from cpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_IEC61970"

class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.This is the IEC 61970 CIM version number assigned to this UML model file.
    """
    # <<< iec61970_cimversion
    # @generated
    def __init__(self, version='', date='', **kw_args):
        """ Initialises a new 'IEC61970CIMVersion' instance.
        """
 
        self.version = version

 
        self.date = date



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

        s += '%s<%s:IEC61970CIMVersion.version>%s</%s:IEC61970CIMVersion.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)
        s += '%s<%s:IEC61970CIMVersion.date>%s</%s:IEC61970CIMVersion.date>' % \
            (indent, ns_prefix, self.date, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "IEC61970CIMVersion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> iec61970_cimversion.serialize


# <<< iec61970
# @generated
# >>> iec61970
