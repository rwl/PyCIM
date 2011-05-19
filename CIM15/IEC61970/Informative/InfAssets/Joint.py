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

class Joint(Asset):
    """Joint connects two or more cables. It includes the portion of cable under wipes, welds, or other seals.Joint connects two or more cables. It includes the portion of cable under wipes, welds, or other seals.
    """

    def __init__(self, insulation='', fillKind="epoxy", configurationKind="other", *args, **kw_args):
        """Initialises a new 'Joint' instance.

        @param insulation: The type of insulation around the joint, classified according to the utility's asset management standards and practices. 
        @param fillKind: Material used to fill the joint. Values are: "epoxy", "noFillPrefab", "airNoFilling", "other", "asphaltic", "insoluseal", "oil", "noVoid", "petrolatum", "bluefill254"
        @param configurationKind: Configuration of joint. Values are: "other", "wires2to1", "wires3to1", "wires1to1"
        """
        #: The type of insulation around the joint, classified according to the utility's asset management standards and practices.
        self.insulation = insulation

        #: Material used to fill the joint. Values are: "epoxy", "noFillPrefab", "airNoFilling", "other", "asphaltic", "insoluseal", "oil", "noVoid", "petrolatum", "bluefill254"
        self.fillKind = fillKind

        #: Configuration of joint. Values are: "other", "wires2to1", "wires3to1", "wires1to1"
        self.configurationKind = configurationKind

        super(Joint, self).__init__(*args, **kw_args)

    _attrs = ["insulation", "fillKind", "configurationKind"]
    _attr_types = {"insulation": str, "fillKind": str, "configurationKind": str}
    _defaults = {"insulation": '', "fillKind": "epoxy", "configurationKind": "other"}
    _enums = {"fillKind": "JointFillKind", "configurationKind": "JointConfigurationKind"}
    _refs = []
    _many_refs = []

