# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.CPSM.Topology.Element import Element

class IdentifiedObject(Element):
    """This is a root class to provide common naming attributes for all classes needing naming attributes
    """

    def __init__(self, name='', description='', *args, **kw_args):
        """Initialises a new 'IdentifiedObject' instance.

        @param name: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy. 
        @param description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. 
        """
        #: The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
        self.name = name

        #: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
        self.description = description

        super(IdentifiedObject, self).__init__(*args, **kw_args)

    _attrs = ["name", "description"]
    _attr_types = {"name": str, "description": str}
    _defaults = {"name": '', "description": ''}
    _enums = {}
    _refs = []
    _many_refs = []

