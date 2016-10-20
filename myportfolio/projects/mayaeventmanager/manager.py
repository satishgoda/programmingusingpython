from collections import OrderedDict
import pymel.core as pm

class io(object):
    @staticmethod
    def write(msg):
        print(msg)

    @staticmethod
    def warn(msg):
        pm.warning(msg)

    @staticmethod
    def wrror(msg):
        pm.error(msg)

class MayaEventData(object):
    def __init__(self, event):
        self.event = event
        self.jid = None
        self.observers = []

    def __repr__(self):
        return "{0} {1} {2}".format(self.__class__, self.event, self.jid)
 
    def startJob(self):
        if self.jid:
            io.warn("Already running {0}".format(self))
            return
        
        self.jid = pm.scriptJob(event=(self.event, self.notify))
        io.warn("Started {0} job: {1}".format(self.event, self.jid))
    
    def killJob(self):
        try:
            pm.scriptJob(kill=self.jid)
            io.warn("Killed {0} job: {1}".format(self.event, self.jid))
            self.jid = None
        except Exception:
            raise
    
    @property
    def callbackName(self):
        """
        Name of the callback method that all the observers 
        of this event must implement
        """
        return 'on{0}CB'.format(self.event)

    def addObserver(self, observer):        
        if not hasattr(observer, self.callbackName):
            raise RuntimeError("{0} must implement {1}".format(observer, self.callbackName))

        self.observers.append(observer)

    def removeObserver(self, observer):
        if not observer in self.observers:
            raise ValueError("{0} is not registered with {1} event".format(observer, self.event))
        self.observers.remove(observer)

    def notify(self):
        if not self.observers:
            io.warn("Nobody to notify about {0}".format(self.event))
            return
        
        for observer in self.observers:
            callback = getattr(observer, self.callbackName)
            try:
                callback()
            except Exception as e:
                traceback.print_exc()

class MayaEventManager(object):
    def __init__(self):
        self.events = OrderedDict([('SelectionChanged', None),
                                  ('ChannelBoxLabelSelected', None),
                                 ])
        self._initialized = False

    def initializeEvents(self):
        events = self.events
        for event in events:
            events[event] = MayaEventData(event)
        self._initialized = True

    def debug(self):
        print evtmgr.events['SelectionChanged'].observers
        print evtmgr.events['ChannelBoxLabelSelected'].observers

    def startEvents(self):
        assert self._initialized == True, "Event Manager has not been initialized"
        events = self.events
        for event in events:
            events[event].startJob()         

    def stopEvents(self):
        assert self._initialized == True, "Event Manager has not been initialized"
        events = self.events
        for event in events:
            events[event].killJob()

    def addEventObserver(self, event, observer):
        assert self._initialized == True, "Event Manager has not been initialized"
        
        try:
            self.events[event].addObserver(observer)
        except KeyError as e:
            eventTypes = ", ".join(self.events.keys())
            raise ValueError("Unsupported event type. Supported types are \n{0}".format(eventTypes))
        except Exception as e:
            raise 

    def removeEventObserver(self, event, observer):
        assert self._initialized == True, "Event Manager has not been initialized"
        
        try:
            self.events[event].removeObserver(observer)
        except KeyError:
            eventTypes = ", ".join(self.events.keys())
            raise ValueError("Unsupported event type. Supported types are \n{0}".format(eventTypes))
        except Exception:
            raise 
