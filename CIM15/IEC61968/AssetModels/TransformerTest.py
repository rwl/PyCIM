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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TransformerTest(IdentifiedObject):
    """Test result for transformer ends, such as short-circuit, open-circuit (excitation) or no-load test.Test result for transformer ends, such as short-circuit, open-circuit (excitation) or no-load test.
    """

    def __init__(self, basePower=0.0, temperature=0.0, *args, **kw_args):
        """Initialises a new 'TransformerTest' instance.

        @param basePower: Base power at which the tests are conducted, usually equal to the rateds of one of the involved transformer ends. 
        @param temperature: Temperature at which the test is conducted. 
        """
        #: Base power at which the tests are conducted, usually equal to the rateds of one of the involved transformer ends.
        self.basePower = basePower

        #: Temperature at which the test is conducted.
        self.temperature = temperature

        super(TransformerTest, self).__init__(*args, **kw_args)

    _attrs = ["basePower", "temperature"]
    _attr_types = {"basePower": float, "temperature": float}
    _defaults = {"basePower": 0.0, "temperature": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

