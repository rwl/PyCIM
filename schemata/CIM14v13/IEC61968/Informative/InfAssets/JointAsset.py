# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61968.Informative.InfAssets.ElectricalAsset import ElectricalAsset

class JointAsset(ElectricalAsset):
    """Physical asset connecting two or more cable assets. It includes the portion of cable under wipes, welds, or other seals.
    """

    def __init__(self, configurationKind='wires2to1', fillKind='bluefill254', insulation='', *args, **kw_args):
        """Initializes a new 'JointAsset' instance.

        @param configurationKind: Configuration of joint. Values are: "wires2to1", "wires1to1", "other", "wires3to1"
        @param fillKind: Material used to fill the joint. Values are: "bluefill254", "airNoFilling", "epoxy", "insoluseal", "noVoid", "noFillPrefab", "asphaltic", "other", "oil", "petrolatum"
        @param insulation: The type of insulation around the joint, classified according to the utility's asset management standards and practices. 
        """
        #: Configuration of joint.Values are: "wires2to1", "wires1to1", "other", "wires3to1"
        self.configurationKind = configurationKind

        #: Material used to fill the joint.Values are: "bluefill254", "airNoFilling", "epoxy", "insoluseal", "noVoid", "noFillPrefab", "asphaltic", "other", "oil", "petrolatum"
        self.fillKind = fillKind

        #: The type of insulation around the joint, classified according to the utility's asset management standards and practices.
        self.insulation = insulation

        super(JointAsset, self).__init__(*args, **kw_args)

