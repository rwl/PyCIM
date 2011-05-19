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

from CIM15.IEC61968.Assets.Asset import Asset

class SubstationAsset(Asset):
    """Substation asset.Substation asset.
    """

    def __init__(self, function="transmission", *args, **kw_args):
        """Initialises a new 'SubstationAsset' instance.

        @param function: Function of this substation asset. Values are: "transmission", "distribution", "other", "generation", "subTransmission", "industrial"
        """
        #: Function of this substation asset. Values are: "transmission", "distribution", "other", "generation", "subTransmission", "industrial"
        self.function = function

        super(SubstationAsset, self).__init__(*args, **kw_args)

    _attrs = ["function"]
    _attr_types = {"function": str}
    _defaults = {"function": "transmission"}
    _enums = {"function": "SubstationFunctionKind"}
    _refs = []
    _many_refs = []

