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


from dynamics import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Loads"

class AggregateLoad(Element):
    """ Aggregate loads are used to represent all or part of the real and reactive load from a load in the static (power flow) data. This load is usually the aggregation of many individual load devices. The load models are approximate representation of the aggregate response of the load devices to system disturbances.   Models of loads for dynamic analysis may themselves be either static or dynamic. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.   Large industrial motors or groups of similar motors may be represented by individual motor models (synchronous or asynchronous) which are usually represented as generators with negative Pgen in the static (power flow) data.
    """
    pass
    # <<< aggregate_load
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'AggregateLoad' instance.

        """


        super(AggregateLoad, self).__init__(*args, **kw_args)
    # >>> aggregate_load



class LoadStatic(AggregateLoad):
    """ General Static Load Model. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.
    """
    # <<< load_static
    # @generated
    def __init__(self, ep2=0.0, ep1=0.0, kp2=0.0, ep3=0.0, kp1=0.0, kq4=0.0, kq3=0.0, kq2=0.0, kq1=0.0, eq1=0.0, eq2=0.0, kp4=0.0, kp3=0.0, eq3=0.0, kqf=0.0, kpf=0.0, *args, **kw_args):
        """ Initialises a new 'LoadStatic' instance.

        @param ep2: 
        @param ep1: 
        @param kp2: 
        @param ep3: 
        @param kp1: 
        @param kq4: 
        @param kq3: 
        @param kq2: 
        @param kq1: 
        @param eq1: 
        @param eq2: 
        @param kp4: 
        @param kp3: 
        @param eq3: 
        @param kqf: 
        @param kpf: 
        """
 
        self.ep2 = ep2

 
        self.ep1 = ep1

 
        self.kp2 = kp2

 
        self.ep3 = ep3

 
        self.kp1 = kp1

 
        self.kq4 = kq4

 
        self.kq3 = kq3

 
        self.kq2 = kq2

 
        self.kq1 = kq1

 
        self.eq1 = eq1

 
        self.eq2 = eq2

 
        self.kp4 = kp4

 
        self.kp3 = kp3

 
        self.eq3 = eq3

 
        self.kqf = kqf

 
        self.kpf = kpf



        super(LoadStatic, self).__init__(*args, **kw_args)
    # >>> load_static



class LoadMotor(AggregateLoad):
    """ Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as 'induction motor load'.  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  Either a 'one-cage' or 'two-cage' model of the induction machine can be modeled.  Magnetic saturation is not modeled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors.
    """
    # <<< load_motor
    # @generated
    def __init__(self, lfac=0.0, ra=0.0, d=0.0, ls=0.0, tppo=0.0, tbkr=0.0, lpp=0.0, tpo=0.0, lp=0.0, h=0.0, vt=0.0, pfrac=0.0, tv=0.0, *args, **kw_args):
        """ Initialises a new 'LoadMotor' instance.

        @param lfac: Loading factor &ndash; ratio of initial P to motor MVA base 
        @param ra: Stator resistance 
        @param d: Damping factor 
        @param ls: Synchronous reactance 
        @param tppo: Sub-transient rotor time constant 
        @param tbkr: Circuit breaker operating time (default = 999) 
        @param lpp: Sub-transient reactance 
        @param tpo: Transient rotor time constant 
        @param lp: Transient reactance 
        @param h: Inertia constant 
        @param vt: Voltage threshold for tripping (default = 0) 
        @param pfrac: Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0) 
        @param tv: Voltage trip pickup time (default = 999) 
        """
        # Loading factor &ndash; ratio of initial P to motor MVA base 
        self.lfac = lfac

        # Stator resistance 
        self.ra = ra

        # Damping factor 
        self.d = d

        # Synchronous reactance 
        self.ls = ls

        # Sub-transient rotor time constant 
        self.tppo = tppo

        # Circuit breaker operating time (default = 999) 
        self.tbkr = tbkr

        # Sub-transient reactance 
        self.lpp = lpp

        # Transient rotor time constant 
        self.tpo = tpo

        # Transient reactance 
        self.lp = lp

        # Inertia constant 
        self.h = h

        # Voltage threshold for tripping (default = 0) 
        self.vt = vt

        # Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0) 
        self.pfrac = pfrac

        # Voltage trip pickup time (default = 999) 
        self.tv = tv



        super(LoadMotor, self).__init__(*args, **kw_args)
    # >>> load_motor



class LoadStaticBus(LoadStatic):
    """ Static load model associated with a single bus.
    """
    pass
    # <<< load_static_bus
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'LoadStaticBus' instance.

        """


        super(LoadStaticBus, self).__init__(*args, **kw_args)
    # >>> load_static_bus



class LoadStaticZone(LoadStatic):
    """ Static load associated with a zone.
    """
    pass
    # <<< load_static_zone
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'LoadStaticZone' instance.

        """


        super(LoadStaticZone, self).__init__(*args, **kw_args)
    # >>> load_static_zone



class LoadStaticArea(LoadStatic):
    """ Static load associated with an Area.
    """
    pass
    # <<< load_static_area
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'LoadStaticArea' instance.

        """


        super(LoadStaticArea, self).__init__(*args, **kw_args)
    # >>> load_static_area



class LoadStaticSystem(LoadStatic):
    """ Static load associated with a specific system.
    """
    pass
    # <<< load_static_system
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'LoadStaticSystem' instance.

        """


        super(LoadStaticSystem, self).__init__(*args, **kw_args)
    # >>> load_static_system



class LoadStaticOwner(LoadStatic):
    """ Static load associated with a single owner.
    """
    pass
    # <<< load_static_owner
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'LoadStaticOwner' instance.

        """


        super(LoadStaticOwner, self).__init__(*args, **kw_args)
    # >>> load_static_owner



# <<< loads
# @generated
# >>> loads
