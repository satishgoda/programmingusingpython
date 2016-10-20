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
    
    def startJob(self):
        self.jid = pm.scriptJob(event=(self.event, self.notify))
        io.warn("Started {0} job: {1}".format(self.event, self.jid))
    
    def killJob(self):
        pm.scriptJob(kill=self.jid)
        io.warn("Killed {0} job: {1}".format(self.event, self.jid))
    
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
