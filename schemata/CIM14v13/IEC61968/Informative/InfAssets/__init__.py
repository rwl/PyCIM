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

"""The package is used to define asset-level models for objects. Assets may be comprised of other assets and may have relationships to other assets. Assets also have owners and values. Assets may also have a relationship to a PowerSystemResource in the Wires model.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'Assets are the basic units which define a physical infrastructure. PowerSystemResources are logical objects meaningful to operations which are constructed from one or more Assets, although PowerSystemResources are not required to specifiy their component Assets. The Asset package is comprosed of several packages. The key concepts of an Asset are as follows: <ul> 	<li>Assets can have names, through inheritance to the Naming package</li> 	<li>Assets are physical entities which have a lifecycle</li> 	<li>One or more assets can be associated to create a PowerSystemResource</li> 	<li>Assets can be grouped (aggregated) with other Assets</li> 	<li>Assets are typically either 'point' or 'linear' assets, which relate to physical geometry</li> 	<li>Assets have a close relationship to Work as a consequence of their lifecycle</li> </ul> The following sections describe the packages in the Assets package. The AssetBasics package defines the relationship between Asset and other classes, such as Organization, PowerSystemResource and Document. Point assets are those assets whose physical location can be described in terms of a single coordinate, such as a pole or a switch. Linear assets are those assets whose physical location is best described in terms of a line, plyline or polygon. Asset work triggers are used to determine when inspection and/or maintenance are required for assets.'
"""

ns_prefix = "cimInfAssets"
ns_uri = "http://iec.ch/TC57/CIM-generic#InfAssets"
