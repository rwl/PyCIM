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

class Agreement(Document):
    """Formal agreement between two parties defining the terms and conditions for a set of services. The specifics of the services are, in turn, defined via one or more service agreements.Formal agreement between two parties defining the terms and conditions for a set of services. The specifics of the services are, in turn, defined via one or more service agreements.
    """

    def __init__(self, signDate='', validityInterval=None, *args, **kw_args):
        """Initialises a new 'Agreement' instance.

        @param signDate: Date this agreement was consummated among associated persons and/or organisations. 
        @param validityInterval: Date and time interval this agreement is valid (from going into effect to termination).
        """
        #: Date this agreement was consummated among associated persons and/or organisations.
        self.signDate = signDate

        self.validityInterval = validityInterval

        super(Agreement, self).__init__(*args, **kw_args)

    _attrs = ["signDate"]
    _attr_types = {"signDate": str}
    _defaults = {"signDate": ''}
    _enums = {}
    _refs = ["validityInterval"]
    _many_refs = []

    # Date and time interval this agreement is valid (from going into effect to termination).
    validityInterval = None

