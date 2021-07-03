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

from CIM16.IEC61968.Assets.AssetInfo import AssetInfo

class ProtectionEquipmentInfo(AssetInfo):
    """Properties of protection equipment asset.Properties of protection equipment asset.
    """

    def __init__(self, groundTrip=0.0, phaseTrip=0.0, *args, **kw_args):
        """Initialises a new 'ProtectionEquipmentInfo' instance.

        @param groundTrip: Actual ground trip for this type of relay, if applicable. 
        @param phaseTrip: Actual phase trip for this type of relay, if applicable. 
        """
        #: Actual ground trip for this type of relay, if applicable.
        self.groundTrip = groundTrip

        #: Actual phase trip for this type of relay, if applicable.
        self.phaseTrip = phaseTrip

        super(ProtectionEquipmentInfo, self).__init__(*args, **kw_args)

    _attrs = ["groundTrip", "phaseTrip"]
    _attr_types = {"groundTrip": float, "phaseTrip": float}
    _defaults = {"groundTrip": 0.0, "phaseTrip": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

