# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from dynamics import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Loads"

class AggregateLoad(Element):
    """ Aggregate loads are used to represent all or part of the real and reactive load from a load in the static (power flow) data. This load is usually the aggregation of many individual load devices. The load models are approximate representation of the aggregate response of the load devices to system disturbances.   Models of loads for dynamic analysis may themselves be either static or dynamic. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.   Large industrial motors or groups of similar motors may be represented by individual motor models (synchronous or asynchronous) which are usually represented as generators with negative Pgen in the static (power flow) data.Aggregate loads are used to represent all or part of the real and reactive load from a load in the static (power flow) data. This load is usually the aggregation of many individual load devices. The load models are approximate representation of the aggregate response of the load devices to system disturbances.   Models of loads for dynamic analysis may themselves be either static or dynamic. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.   Large industrial motors or groups of similar motors may be represented by individual motor models (synchronous or asynchronous) which are usually represented as generators with negative Pgen in the static (power flow) data.
    """
    pass
    # <<< aggregate_load
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'AggregateLoad' instance.
        """


        super(AggregateLoad, self).__init__(**kw_args)
    # >>> aggregate_load


    def __str__(self):
        """ Returns a string representation of the AggregateLoad.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< aggregate_load.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AggregateLoad.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AggregateLoad", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AggregateLoad")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> aggregate_load.serialize


class LoadStatic(AggregateLoad):
    """ General Static Load Model. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.General Static Load Model. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.
    """
    # <<< load_static
    # @generated
    def __init__(self, ep2=0.0, ep1=0.0, kp2=0.0, ep3=0.0, kp1=0.0, kq4=0.0, kq3=0.0, kq2=0.0, kq1=0.0, eq1=0.0, eq2=0.0, kp4=0.0, kp3=0.0, eq3=0.0, kqf=0.0, kpf=0.0, **kw_args):
        """ Initialises a new 'LoadStatic' instance.
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



        super(LoadStatic, self).__init__(**kw_args)
    # >>> load_static


    def __str__(self):
        """ Returns a string representation of the LoadStatic.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_static.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadStatic.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadStatic", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:LoadStatic.ep2>%s</%s:LoadStatic.ep2>' % \
            (indent, ns_prefix, self.ep2, ns_prefix)
        s += '%s<%s:LoadStatic.ep1>%s</%s:LoadStatic.ep1>' % \
            (indent, ns_prefix, self.ep1, ns_prefix)
        s += '%s<%s:LoadStatic.kp2>%s</%s:LoadStatic.kp2>' % \
            (indent, ns_prefix, self.kp2, ns_prefix)
        s += '%s<%s:LoadStatic.ep3>%s</%s:LoadStatic.ep3>' % \
            (indent, ns_prefix, self.ep3, ns_prefix)
        s += '%s<%s:LoadStatic.kp1>%s</%s:LoadStatic.kp1>' % \
            (indent, ns_prefix, self.kp1, ns_prefix)
        s += '%s<%s:LoadStatic.kq4>%s</%s:LoadStatic.kq4>' % \
            (indent, ns_prefix, self.kq4, ns_prefix)
        s += '%s<%s:LoadStatic.kq3>%s</%s:LoadStatic.kq3>' % \
            (indent, ns_prefix, self.kq3, ns_prefix)
        s += '%s<%s:LoadStatic.kq2>%s</%s:LoadStatic.kq2>' % \
            (indent, ns_prefix, self.kq2, ns_prefix)
        s += '%s<%s:LoadStatic.kq1>%s</%s:LoadStatic.kq1>' % \
            (indent, ns_prefix, self.kq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq1>%s</%s:LoadStatic.eq1>' % \
            (indent, ns_prefix, self.eq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq2>%s</%s:LoadStatic.eq2>' % \
            (indent, ns_prefix, self.eq2, ns_prefix)
        s += '%s<%s:LoadStatic.kp4>%s</%s:LoadStatic.kp4>' % \
            (indent, ns_prefix, self.kp4, ns_prefix)
        s += '%s<%s:LoadStatic.kp3>%s</%s:LoadStatic.kp3>' % \
            (indent, ns_prefix, self.kp3, ns_prefix)
        s += '%s<%s:LoadStatic.eq3>%s</%s:LoadStatic.eq3>' % \
            (indent, ns_prefix, self.eq3, ns_prefix)
        s += '%s<%s:LoadStatic.kqf>%s</%s:LoadStatic.kqf>' % \
            (indent, ns_prefix, self.kqf, ns_prefix)
        s += '%s<%s:LoadStatic.kpf>%s</%s:LoadStatic.kpf>' % \
            (indent, ns_prefix, self.kpf, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadStatic")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_static.serialize


class LoadMotor(AggregateLoad):
    """ Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as 'induction motor load'.  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  Either a 'one-cage' or 'two-cage' model of the induction machine can be modeled.  Magnetic saturation is not modeled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors.Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as 'induction motor load'.  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  Either a 'one-cage' or 'two-cage' model of the induction machine can be modeled.  Magnetic saturation is not modeled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors.
    """
    # <<< load_motor
    # @generated
    def __init__(self, lfac=0.0, ra=0.0, d=0.0, ls=0.0, tppo=0.0, tbkr=0.0, lpp=0.0, tpo=0.0, lp=0.0, h=0.0, vt=0.0, pfrac=0.0, tv=0.0, **kw_args):
        """ Initialises a new 'LoadMotor' instance.
        """
        # Loading factor &ndash; ratio of initial P to motor MVA baseLoading factor &ndash; ratio of initial P to motor MVA base 
        self.lfac = lfac

        # Stator resistanceStator resistance 
        self.ra = ra

        # Damping factorDamping factor 
        self.d = d

        # Synchronous reactanceSynchronous reactance 
        self.ls = ls

        # Sub-transient rotor time constantSub-transient rotor time constant 
        self.tppo = tppo

        # Circuit breaker operating time (default = 999)Circuit breaker operating time (default = 999) 
        self.tbkr = tbkr

        # Sub-transient reactanceSub-transient reactance 
        self.lpp = lpp

        # Transient rotor time constantTransient rotor time constant 
        self.tpo = tpo

        # Transient reactanceTransient reactance 
        self.lp = lp

        # Inertia constantInertia constant 
        self.h = h

        # Voltage threshold for tripping (default = 0)Voltage threshold for tripping (default = 0) 
        self.vt = vt

        # Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0)Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0) 
        self.pfrac = pfrac

        # Voltage trip pickup time (default = 999)Voltage trip pickup time (default = 999) 
        self.tv = tv



        super(LoadMotor, self).__init__(**kw_args)
    # >>> load_motor


    def __str__(self):
        """ Returns a string representation of the LoadMotor.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_motor.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadMotor.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadMotor", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:LoadMotor.lfac>%s</%s:LoadMotor.lfac>' % \
            (indent, ns_prefix, self.lfac, ns_prefix)
        s += '%s<%s:LoadMotor.ra>%s</%s:LoadMotor.ra>' % \
            (indent, ns_prefix, self.ra, ns_prefix)
        s += '%s<%s:LoadMotor.d>%s</%s:LoadMotor.d>' % \
            (indent, ns_prefix, self.d, ns_prefix)
        s += '%s<%s:LoadMotor.ls>%s</%s:LoadMotor.ls>' % \
            (indent, ns_prefix, self.ls, ns_prefix)
        s += '%s<%s:LoadMotor.tppo>%s</%s:LoadMotor.tppo>' % \
            (indent, ns_prefix, self.tppo, ns_prefix)
        s += '%s<%s:LoadMotor.tbkr>%s</%s:LoadMotor.tbkr>' % \
            (indent, ns_prefix, self.tbkr, ns_prefix)
        s += '%s<%s:LoadMotor.lpp>%s</%s:LoadMotor.lpp>' % \
            (indent, ns_prefix, self.lpp, ns_prefix)
        s += '%s<%s:LoadMotor.tpo>%s</%s:LoadMotor.tpo>' % \
            (indent, ns_prefix, self.tpo, ns_prefix)
        s += '%s<%s:LoadMotor.lp>%s</%s:LoadMotor.lp>' % \
            (indent, ns_prefix, self.lp, ns_prefix)
        s += '%s<%s:LoadMotor.h>%s</%s:LoadMotor.h>' % \
            (indent, ns_prefix, self.h, ns_prefix)
        s += '%s<%s:LoadMotor.vt>%s</%s:LoadMotor.vt>' % \
            (indent, ns_prefix, self.vt, ns_prefix)
        s += '%s<%s:LoadMotor.pfrac>%s</%s:LoadMotor.pfrac>' % \
            (indent, ns_prefix, self.pfrac, ns_prefix)
        s += '%s<%s:LoadMotor.tv>%s</%s:LoadMotor.tv>' % \
            (indent, ns_prefix, self.tv, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadMotor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_motor.serialize


class LoadStaticBus(LoadStatic):
    """ Static load model associated with a single bus.Static load model associated with a single bus.
    """
    pass
    # <<< load_static_bus
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'LoadStaticBus' instance.
        """


        super(LoadStaticBus, self).__init__(**kw_args)
    # >>> load_static_bus


    def __str__(self):
        """ Returns a string representation of the LoadStaticBus.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_static_bus.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadStaticBus.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadStaticBus", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:LoadStatic.ep2>%s</%s:LoadStatic.ep2>' % \
            (indent, ns_prefix, self.ep2, ns_prefix)
        s += '%s<%s:LoadStatic.ep1>%s</%s:LoadStatic.ep1>' % \
            (indent, ns_prefix, self.ep1, ns_prefix)
        s += '%s<%s:LoadStatic.kp2>%s</%s:LoadStatic.kp2>' % \
            (indent, ns_prefix, self.kp2, ns_prefix)
        s += '%s<%s:LoadStatic.ep3>%s</%s:LoadStatic.ep3>' % \
            (indent, ns_prefix, self.ep3, ns_prefix)
        s += '%s<%s:LoadStatic.kp1>%s</%s:LoadStatic.kp1>' % \
            (indent, ns_prefix, self.kp1, ns_prefix)
        s += '%s<%s:LoadStatic.kq4>%s</%s:LoadStatic.kq4>' % \
            (indent, ns_prefix, self.kq4, ns_prefix)
        s += '%s<%s:LoadStatic.kq3>%s</%s:LoadStatic.kq3>' % \
            (indent, ns_prefix, self.kq3, ns_prefix)
        s += '%s<%s:LoadStatic.kq2>%s</%s:LoadStatic.kq2>' % \
            (indent, ns_prefix, self.kq2, ns_prefix)
        s += '%s<%s:LoadStatic.kq1>%s</%s:LoadStatic.kq1>' % \
            (indent, ns_prefix, self.kq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq1>%s</%s:LoadStatic.eq1>' % \
            (indent, ns_prefix, self.eq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq2>%s</%s:LoadStatic.eq2>' % \
            (indent, ns_prefix, self.eq2, ns_prefix)
        s += '%s<%s:LoadStatic.kp4>%s</%s:LoadStatic.kp4>' % \
            (indent, ns_prefix, self.kp4, ns_prefix)
        s += '%s<%s:LoadStatic.kp3>%s</%s:LoadStatic.kp3>' % \
            (indent, ns_prefix, self.kp3, ns_prefix)
        s += '%s<%s:LoadStatic.eq3>%s</%s:LoadStatic.eq3>' % \
            (indent, ns_prefix, self.eq3, ns_prefix)
        s += '%s<%s:LoadStatic.kqf>%s</%s:LoadStatic.kqf>' % \
            (indent, ns_prefix, self.kqf, ns_prefix)
        s += '%s<%s:LoadStatic.kpf>%s</%s:LoadStatic.kpf>' % \
            (indent, ns_prefix, self.kpf, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadStaticBus")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_static_bus.serialize


class LoadStaticZone(LoadStatic):
    """ Static load associated with a zone.Static load associated with a zone.
    """
    pass
    # <<< load_static_zone
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'LoadStaticZone' instance.
        """


        super(LoadStaticZone, self).__init__(**kw_args)
    # >>> load_static_zone


    def __str__(self):
        """ Returns a string representation of the LoadStaticZone.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_static_zone.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadStaticZone.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadStaticZone", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:LoadStatic.ep2>%s</%s:LoadStatic.ep2>' % \
            (indent, ns_prefix, self.ep2, ns_prefix)
        s += '%s<%s:LoadStatic.ep1>%s</%s:LoadStatic.ep1>' % \
            (indent, ns_prefix, self.ep1, ns_prefix)
        s += '%s<%s:LoadStatic.kp2>%s</%s:LoadStatic.kp2>' % \
            (indent, ns_prefix, self.kp2, ns_prefix)
        s += '%s<%s:LoadStatic.ep3>%s</%s:LoadStatic.ep3>' % \
            (indent, ns_prefix, self.ep3, ns_prefix)
        s += '%s<%s:LoadStatic.kp1>%s</%s:LoadStatic.kp1>' % \
            (indent, ns_prefix, self.kp1, ns_prefix)
        s += '%s<%s:LoadStatic.kq4>%s</%s:LoadStatic.kq4>' % \
            (indent, ns_prefix, self.kq4, ns_prefix)
        s += '%s<%s:LoadStatic.kq3>%s</%s:LoadStatic.kq3>' % \
            (indent, ns_prefix, self.kq3, ns_prefix)
        s += '%s<%s:LoadStatic.kq2>%s</%s:LoadStatic.kq2>' % \
            (indent, ns_prefix, self.kq2, ns_prefix)
        s += '%s<%s:LoadStatic.kq1>%s</%s:LoadStatic.kq1>' % \
            (indent, ns_prefix, self.kq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq1>%s</%s:LoadStatic.eq1>' % \
            (indent, ns_prefix, self.eq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq2>%s</%s:LoadStatic.eq2>' % \
            (indent, ns_prefix, self.eq2, ns_prefix)
        s += '%s<%s:LoadStatic.kp4>%s</%s:LoadStatic.kp4>' % \
            (indent, ns_prefix, self.kp4, ns_prefix)
        s += '%s<%s:LoadStatic.kp3>%s</%s:LoadStatic.kp3>' % \
            (indent, ns_prefix, self.kp3, ns_prefix)
        s += '%s<%s:LoadStatic.eq3>%s</%s:LoadStatic.eq3>' % \
            (indent, ns_prefix, self.eq3, ns_prefix)
        s += '%s<%s:LoadStatic.kqf>%s</%s:LoadStatic.kqf>' % \
            (indent, ns_prefix, self.kqf, ns_prefix)
        s += '%s<%s:LoadStatic.kpf>%s</%s:LoadStatic.kpf>' % \
            (indent, ns_prefix, self.kpf, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadStaticZone")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_static_zone.serialize


class LoadStaticArea(LoadStatic):
    """ Static load associated with an Area.Static load associated with an Area.
    """
    pass
    # <<< load_static_area
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'LoadStaticArea' instance.
        """


        super(LoadStaticArea, self).__init__(**kw_args)
    # >>> load_static_area


    def __str__(self):
        """ Returns a string representation of the LoadStaticArea.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_static_area.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadStaticArea.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadStaticArea", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:LoadStatic.ep2>%s</%s:LoadStatic.ep2>' % \
            (indent, ns_prefix, self.ep2, ns_prefix)
        s += '%s<%s:LoadStatic.ep1>%s</%s:LoadStatic.ep1>' % \
            (indent, ns_prefix, self.ep1, ns_prefix)
        s += '%s<%s:LoadStatic.kp2>%s</%s:LoadStatic.kp2>' % \
            (indent, ns_prefix, self.kp2, ns_prefix)
        s += '%s<%s:LoadStatic.ep3>%s</%s:LoadStatic.ep3>' % \
            (indent, ns_prefix, self.ep3, ns_prefix)
        s += '%s<%s:LoadStatic.kp1>%s</%s:LoadStatic.kp1>' % \
            (indent, ns_prefix, self.kp1, ns_prefix)
        s += '%s<%s:LoadStatic.kq4>%s</%s:LoadStatic.kq4>' % \
            (indent, ns_prefix, self.kq4, ns_prefix)
        s += '%s<%s:LoadStatic.kq3>%s</%s:LoadStatic.kq3>' % \
            (indent, ns_prefix, self.kq3, ns_prefix)
        s += '%s<%s:LoadStatic.kq2>%s</%s:LoadStatic.kq2>' % \
            (indent, ns_prefix, self.kq2, ns_prefix)
        s += '%s<%s:LoadStatic.kq1>%s</%s:LoadStatic.kq1>' % \
            (indent, ns_prefix, self.kq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq1>%s</%s:LoadStatic.eq1>' % \
            (indent, ns_prefix, self.eq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq2>%s</%s:LoadStatic.eq2>' % \
            (indent, ns_prefix, self.eq2, ns_prefix)
        s += '%s<%s:LoadStatic.kp4>%s</%s:LoadStatic.kp4>' % \
            (indent, ns_prefix, self.kp4, ns_prefix)
        s += '%s<%s:LoadStatic.kp3>%s</%s:LoadStatic.kp3>' % \
            (indent, ns_prefix, self.kp3, ns_prefix)
        s += '%s<%s:LoadStatic.eq3>%s</%s:LoadStatic.eq3>' % \
            (indent, ns_prefix, self.eq3, ns_prefix)
        s += '%s<%s:LoadStatic.kqf>%s</%s:LoadStatic.kqf>' % \
            (indent, ns_prefix, self.kqf, ns_prefix)
        s += '%s<%s:LoadStatic.kpf>%s</%s:LoadStatic.kpf>' % \
            (indent, ns_prefix, self.kpf, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadStaticArea")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_static_area.serialize


class LoadStaticSystem(LoadStatic):
    """ Static load associated with a specific system.Static load associated with a specific system.
    """
    pass
    # <<< load_static_system
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'LoadStaticSystem' instance.
        """


        super(LoadStaticSystem, self).__init__(**kw_args)
    # >>> load_static_system


    def __str__(self):
        """ Returns a string representation of the LoadStaticSystem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_static_system.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadStaticSystem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadStaticSystem", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:LoadStatic.ep2>%s</%s:LoadStatic.ep2>' % \
            (indent, ns_prefix, self.ep2, ns_prefix)
        s += '%s<%s:LoadStatic.ep1>%s</%s:LoadStatic.ep1>' % \
            (indent, ns_prefix, self.ep1, ns_prefix)
        s += '%s<%s:LoadStatic.kp2>%s</%s:LoadStatic.kp2>' % \
            (indent, ns_prefix, self.kp2, ns_prefix)
        s += '%s<%s:LoadStatic.ep3>%s</%s:LoadStatic.ep3>' % \
            (indent, ns_prefix, self.ep3, ns_prefix)
        s += '%s<%s:LoadStatic.kp1>%s</%s:LoadStatic.kp1>' % \
            (indent, ns_prefix, self.kp1, ns_prefix)
        s += '%s<%s:LoadStatic.kq4>%s</%s:LoadStatic.kq4>' % \
            (indent, ns_prefix, self.kq4, ns_prefix)
        s += '%s<%s:LoadStatic.kq3>%s</%s:LoadStatic.kq3>' % \
            (indent, ns_prefix, self.kq3, ns_prefix)
        s += '%s<%s:LoadStatic.kq2>%s</%s:LoadStatic.kq2>' % \
            (indent, ns_prefix, self.kq2, ns_prefix)
        s += '%s<%s:LoadStatic.kq1>%s</%s:LoadStatic.kq1>' % \
            (indent, ns_prefix, self.kq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq1>%s</%s:LoadStatic.eq1>' % \
            (indent, ns_prefix, self.eq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq2>%s</%s:LoadStatic.eq2>' % \
            (indent, ns_prefix, self.eq2, ns_prefix)
        s += '%s<%s:LoadStatic.kp4>%s</%s:LoadStatic.kp4>' % \
            (indent, ns_prefix, self.kp4, ns_prefix)
        s += '%s<%s:LoadStatic.kp3>%s</%s:LoadStatic.kp3>' % \
            (indent, ns_prefix, self.kp3, ns_prefix)
        s += '%s<%s:LoadStatic.eq3>%s</%s:LoadStatic.eq3>' % \
            (indent, ns_prefix, self.eq3, ns_prefix)
        s += '%s<%s:LoadStatic.kqf>%s</%s:LoadStatic.kqf>' % \
            (indent, ns_prefix, self.kqf, ns_prefix)
        s += '%s<%s:LoadStatic.kpf>%s</%s:LoadStatic.kpf>' % \
            (indent, ns_prefix, self.kpf, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadStaticSystem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_static_system.serialize


class LoadStaticOwner(LoadStatic):
    """ Static load associated with a single owner.Static load associated with a single owner.
    """
    pass
    # <<< load_static_owner
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'LoadStaticOwner' instance.
        """


        super(LoadStaticOwner, self).__init__(**kw_args)
    # >>> load_static_owner


    def __str__(self):
        """ Returns a string representation of the LoadStaticOwner.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_static_owner.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadStaticOwner.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadStaticOwner", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:LoadStatic.ep2>%s</%s:LoadStatic.ep2>' % \
            (indent, ns_prefix, self.ep2, ns_prefix)
        s += '%s<%s:LoadStatic.ep1>%s</%s:LoadStatic.ep1>' % \
            (indent, ns_prefix, self.ep1, ns_prefix)
        s += '%s<%s:LoadStatic.kp2>%s</%s:LoadStatic.kp2>' % \
            (indent, ns_prefix, self.kp2, ns_prefix)
        s += '%s<%s:LoadStatic.ep3>%s</%s:LoadStatic.ep3>' % \
            (indent, ns_prefix, self.ep3, ns_prefix)
        s += '%s<%s:LoadStatic.kp1>%s</%s:LoadStatic.kp1>' % \
            (indent, ns_prefix, self.kp1, ns_prefix)
        s += '%s<%s:LoadStatic.kq4>%s</%s:LoadStatic.kq4>' % \
            (indent, ns_prefix, self.kq4, ns_prefix)
        s += '%s<%s:LoadStatic.kq3>%s</%s:LoadStatic.kq3>' % \
            (indent, ns_prefix, self.kq3, ns_prefix)
        s += '%s<%s:LoadStatic.kq2>%s</%s:LoadStatic.kq2>' % \
            (indent, ns_prefix, self.kq2, ns_prefix)
        s += '%s<%s:LoadStatic.kq1>%s</%s:LoadStatic.kq1>' % \
            (indent, ns_prefix, self.kq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq1>%s</%s:LoadStatic.eq1>' % \
            (indent, ns_prefix, self.eq1, ns_prefix)
        s += '%s<%s:LoadStatic.eq2>%s</%s:LoadStatic.eq2>' % \
            (indent, ns_prefix, self.eq2, ns_prefix)
        s += '%s<%s:LoadStatic.kp4>%s</%s:LoadStatic.kp4>' % \
            (indent, ns_prefix, self.kp4, ns_prefix)
        s += '%s<%s:LoadStatic.kp3>%s</%s:LoadStatic.kp3>' % \
            (indent, ns_prefix, self.kp3, ns_prefix)
        s += '%s<%s:LoadStatic.eq3>%s</%s:LoadStatic.eq3>' % \
            (indent, ns_prefix, self.eq3, ns_prefix)
        s += '%s<%s:LoadStatic.kqf>%s</%s:LoadStatic.kqf>' % \
            (indent, ns_prefix, self.kqf, ns_prefix)
        s += '%s<%s:LoadStatic.kpf>%s</%s:LoadStatic.kpf>' % \
            (indent, ns_prefix, self.kpf, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadStaticOwner")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_static_owner.serialize


# <<< loads
# @generated
# >>> loads
