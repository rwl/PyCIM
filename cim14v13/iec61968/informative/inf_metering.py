# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA


from cim14v13.iec61970.core import IdentifiedObject
from cim14v13.iec61968.metering import DeviceFunction

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimInfMetering"

ns_uri = "http://iec.ch/TC57/CIM-generic#InfMetering"

class ComPort(IdentifiedObject):
    """ Port information used for communication connectivity purposes. The 'port' names the physical association to another device from the perspective of the parent asset. For example, a communications module may need to list the meters which it can talk to as meter serial number '123' is on 'port 0', S/N '456' is on port '1', etc. A meter or load control device may need to know that a hot-water heater load is on 'port 0', and an air-conditioner on 'port 1'.
    """
    pass
    # <<< com_port
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ComPort' instance.

        """


        super(ComPort, self).__init__(*args, **kw_args)
    # >>> com_port



class WaterMeteringFunction(DeviceFunction):
    """ Functionality performed by a water meter. It's entirely possible that the metering system would carry information to/from water meters even though it was built primarily to carry the higher-value electric meter data.
    """
    pass
    # <<< water_metering_function
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'WaterMeteringFunction' instance.

        """


        super(WaterMeteringFunction, self).__init__(*args, **kw_args)
    # >>> water_metering_function



class GasMeteringFunction(DeviceFunction):
    """ Functionality performed by a gas meter. It's entirely possible that the metering system would carry information to/from gas meters even though it was built primarily to carry the higher-value electric meter data.
    """
    pass
    # <<< gas_metering_function
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GasMeteringFunction' instance.

        """


        super(GasMeteringFunction, self).__init__(*args, **kw_args)
    # >>> gas_metering_function



class MeteringFunctionConfiguration(IdentifiedObject):
    """ The configuration of data for a given meter function.
    """
    # <<< metering_function_configuration
    # @generated
    def __init__(self, electric_metering_functions=None, *args, **kw_args):
        """ Initialises a new 'MeteringFunctionConfiguration' instance.

        @param electric_metering_functions: All electric metering functions with this configuration.
        """

        self._electric_metering_functions = []
        if electric_metering_functions is not None:
            self.electric_metering_functions = electric_metering_functions
        else:
            self.electric_metering_functions = []


        super(MeteringFunctionConfiguration, self).__init__(*args, **kw_args)
    # >>> metering_function_configuration

    # <<< electric_metering_functions
    # @generated
    def get_electric_metering_functions(self):
        """ All electric metering functions with this configuration.
        """
        return self._electric_metering_functions

    def set_electric_metering_functions(self, value):
        for x in self._electric_metering_functions:
            x._metering_function_configuration = None
        for y in value:
            y._metering_function_configuration = self
        self._electric_metering_functions = value

    electric_metering_functions = property(get_electric_metering_functions, set_electric_metering_functions)

    def add_electric_metering_functions(self, *electric_metering_functions):
        for obj in electric_metering_functions:
            obj._metering_function_configuration = self
            self._electric_metering_functions.append(obj)

    def remove_electric_metering_functions(self, *electric_metering_functions):
        for obj in electric_metering_functions:
            obj._metering_function_configuration = None
            self._electric_metering_functions.remove(obj)
    # >>> electric_metering_functions



# <<< inf_metering
# @generated
# >>> inf_metering
