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


from dynamics.iec61970.dynamics import AsynchronousMachine
from dynamics import Element
from dynamics.iec61970.dynamics import RotatingMachine

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Motors"

class MotorAsync(AsynchronousMachine):
    """ An asynchronous (induction) motor with no external connection to the rotor windings, e.g., a squirrel-cage induction motor.
    """
    pass
    # <<< motor_async
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MotorAsync' instance.

        """


        super(MotorAsync, self).__init__(*args, **kw_args)
    # >>> motor_async



class MechanicalLoad(Element):
    """ A mechanical load represents the variation in a motor's shaft torque or power as a function of shaft speed.
    """
    pass
    # <<< mechanical_load
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MechanicalLoad' instance.

        """


        super(MechanicalLoad, self).__init__(*args, **kw_args)
    # >>> mechanical_load



class SynchronousMotorType(Element):
    """ Type of synchronous motor
    """
    pass
    # <<< synchronous_motor_type
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'SynchronousMotorType' instance.

        """


        super(SynchronousMotorType, self).__init__(*args, **kw_args)
    # >>> synchronous_motor_type



class MotorSync(RotatingMachine):
    """ A large industrial motor or group of similar motors.  They are represented as <b>generators with negative Pgen</b> in the static (power flow) data.
    """
    pass
    # <<< motor_sync
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'MotorSync' instance.

        """


        super(MotorSync, self).__init__(*args, **kw_args)
    # >>> motor_sync



class MechLoad1(MechanicalLoad):
    """ Mechanical load model 1
    """
    # <<< mech_load1
    # @generated
    def __init__(self, b=0.0, a=0.0, d=0.0, e=0.0, *args, **kw_args):
        """ Initialises a new 'MechLoad1' instance.

        @param b: Speed squared coefficient 
        @param a: Speed squared coefficient 
        @param d: Speed to the exponent coefficient 
        @param e: Exponent 
        """
        # Speed squared coefficient 
        self.b = b

        # Speed squared coefficient 
        self.a = a

        # Speed to the exponent coefficient 
        self.d = d

        # Exponent 
        self.e = e



        super(MechLoad1, self).__init__(*args, **kw_args)
    # >>> mech_load1



# <<< motors
# @generated
# >>> motors
