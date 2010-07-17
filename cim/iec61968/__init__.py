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

""" This package contains the core information classes that support work management and network extension planning applications.
"""

from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.iec61968"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968"

class IEC61968CIMVersion(Element):
    """ IEC 61968 version number assigned to this UML model.
    """
    # <<< iec61968_cimversion
    # @generated
    def __init__(self, version='', date='', **kw_args):
        """ Initialises a new 'IEC61968CIMVersion' instance.
        """
        # Form is IEC61968CIMXXvYY where XX is the major CIM package version and the YY is the minor version.  For example IEC61968CIM10v17. 
        self.version = version

        # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. 
        self.date = date



        super(IEC61968CIMVersion, self).__init__(**kw_args)
    # >>> iec61968_cimversion


    def __str__(self):
        """ Returns a string representation of the IEC61968CIMVersion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< iec61968_cimversion.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the IEC61968CIMVersion.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "IEC61968CIMVersion", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:IEC61968CIMVersion.version>%s</%s:IEC61968CIMVersion.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)
        s += '%s<%s:IEC61968CIMVersion.date>%s</%s:IEC61968CIMVersion.date>' % \
            (indent, ns_prefix, self.date, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "IEC61968CIMVersion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> iec61968_cimversion.serialize


# <<< iec61968
# @generated
# >>> iec61968
