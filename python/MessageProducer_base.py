#!/usr/bin/env python
#
# AUTO-GENERATED CODE.  DO NOT MODIFY!
#
# Source: ex.MessageProducer.spd.xml
from ossie.cf import CF
from ossie.cf import CF__POA
from ossie.utils import uuid

from ossie.component import Component
from ossie.threadedcomponent import *
from ossie.properties import simple_property
from ossie.properties import simpleseq_property
from ossie.properties import struct_property

import Queue, copy, time, threading
from ossie.resource import usesport, providesport
from ossie.events import MessageSupplierPort

class MessageProducer_base(CF__POA.Resource, Component, ThreadedComponent):
        # These values can be altered in the __init__ of your derived class

        PAUSE = 0.0125 # The amount of time to sleep if process return NOOP
        TIMEOUT = 5.0 # The amount of time to wait for the process thread to die when stop() is called
        DEFAULT_QUEUE_SIZE = 100 # The number of BulkIO packets that can be in the queue before pushPacket will block

        def __init__(self, identifier, execparams):
            loggerName = (execparams['NAME_BINDING'].replace('/', '.')).rsplit("_", 1)[0]
            Component.__init__(self, identifier, execparams, loggerName=loggerName)
            ThreadedComponent.__init__(self)

            # self.auto_start is deprecated and is only kept for API compatibility
            # with 1.7.X and 1.8.0 components.  This variable may be removed
            # in future releases
            self.auto_start = False
            # Instantiate the default implementations for all ports on this component
            self.port_geo_out = MessageSupplierPort()

        def start(self):
            Component.start(self)
            ThreadedComponent.startThread(self, pause=self.PAUSE)

        def stop(self):
            Component.stop(self)
            if not ThreadedComponent.stopThread(self, self.TIMEOUT):
                raise CF.Resource.StopError(CF.CF_NOTSET, "Processing thread did not die")

        def releaseObject(self):
            try:
                self.stop()
            except Exception:
                self._log.exception("Error stopping")
            Component.releaseObject(self)

        ######################################################################
        # PORTS
        # 
        # DO NOT ADD NEW PORTS HERE.  You can add ports in your derived class, in the SCD xml file, 
        # or via the IDE.

        port_geo_out = usesport(name="geo_out",
                                repid="IDL:ExtendedEvent/MessageEvent:1.0",
                                type_="data")

        ######################################################################
        # PROPERTIES
        # 
        # DO NOT ADD NEW PROPERTIES HERE.  You can add properties in your derived class, in the PRF xml file
        # or by using the IDE.
        update_rate = simple_property(id_="update_rate",
                                      name="update_rate",
                                      type_="float",
                                      defvalue=1.0,
                                      mode="readwrite",
                                      action="external",
                                      kinds=("property",))


        class Geolocation(object):
            lat = simple_property(
                                  id_="geolocation::lat",
                                  
                                  name="lat",
                                  type_="double")
        
            lon = simple_property(
                                  id_="geolocation::lon",
                                  
                                  name="lon",
                                  type_="double")
        
            majoraxis = simple_property(
                                        id_="geolocation::majoraxis",
                                        
                                        name="majoraxis",
                                        type_="double")
        
            minoraxis = simple_property(
                                        id_="geolocation::minoraxis",
                                        
                                        name="minoraxis",
                                        type_="double")
        
            confidence = simple_property(
                                         id_="geolocation::confidence",
                                         
                                         name="confidence",
                                         type_="string")
        
            def __init__(self, **kw):
                """Construct an initialized instance of this struct definition"""
                for classattr in type(self).__dict__.itervalues():
                    if isinstance(classattr, (simple_property, simpleseq_property)):
                        classattr.initialize(self)
                for k,v in kw.items():
                    setattr(self,k,v)
        
            def __str__(self):
                """Return a string representation of this structure"""
                d = {}
                d["lat"] = self.lat
                d["lon"] = self.lon
                d["majoraxis"] = self.majoraxis
                d["minoraxis"] = self.minoraxis
                d["confidence"] = self.confidence
                return str(d)
        
            @classmethod
            def getId(cls):
                return "geolocation"
        
            @classmethod
            def isStruct(cls):
                return True
        
            def getMembers(self):
                return [("lat",self.lat),("lon",self.lon),("majoraxis",self.majoraxis),("minoraxis",self.minoraxis),("confidence",self.confidence)]

        geolocation = struct_property(id_="geolocation",
                                      name="geolocation",
                                      structdef=Geolocation,
                                      configurationkind=("message",),
                                      mode="readwrite")




