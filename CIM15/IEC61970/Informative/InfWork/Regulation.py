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

from CIM15.IEC61968.Common.Document import Document

class Regulation(Document):
    """Special requirements and/or regulations may pertain to certain types of assets or work. For example, fire protection and scaffolding.Special requirements and/or regulations may pertain to certain types of assets or work. For example, fire protection and scaffolding.
    """

    def __init__(self, referenceNumber='', *args, **kw_args):
        """Initialises a new 'Regulation' instance.

        @param referenceNumber: External reference to regulation, if applicable. 
        """
        #: External reference to regulation, if applicable.
        self.referenceNumber = referenceNumber

        super(Regulation, self).__init__(*args, **kw_args)

    _attrs = ["referenceNumber"]
    _attr_types = {"referenceNumber": str}
    _defaults = {"referenceNumber": ''}
    _enums = {}
    _refs = []
    _many_refs = []

