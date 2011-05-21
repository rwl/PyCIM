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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class LimitSet(IdentifiedObject):
    """Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.
    """

    def __init__(self, isPercentageLimits=False, *args, **kw_args):
        """Initialises a new 'LimitSet' instance.

        @param isPercentageLimits: Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. 
        """
        #: Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.
        self.isPercentageLimits = isPercentageLimits

        super(LimitSet, self).__init__(*args, **kw_args)

    _attrs = ["isPercentageLimits"]
    _attr_types = {"isPercentageLimits": bool}
    _defaults = {"isPercentageLimits": False}
    _enums = {}
    _refs = []
    _many_refs = []

