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

from CIM15.CDPSM.Balanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ProtectedSwitch(IdentifiedObject):
    """A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.
    """

    def __init__(self, breakingCapacity=0.0, *args, **kw_args):
        """Initialises a new 'ProtectedSwitch' instance.

        @param breakingCapacity: The maximum fault current a breaking device can break safely under prescribed conditions of use. 
        """
        #: The maximum fault current a breaking device can break safely under prescribed conditions of use.
        self.breakingCapacity = breakingCapacity

        super(ProtectedSwitch, self).__init__(*args, **kw_args)

    _attrs = ["breakingCapacity"]
    _attr_types = {"breakingCapacity": float}
    _defaults = {"breakingCapacity": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

