class _SSS(object):
    @property
    def handle(self):
        o = pm.nt.ObjectSet('_SESSSELSETS')
        return o

    def __getattr__(self, attr):
        if hasattr(self.handle, attr):
            att = getattr(self.handle, attr)
            if callable(att):
                return att()
            return None

sss = _SSS()

class _Context():
    @property
    def sss(self):
        o = sss
        return o
    
    @property
    def active(self):
        o = pm.selected()[0]
        return o
    
    @property
    def clear(self):
        print "clearing model"
        clear()
    
    @property
    def reload(self):
        print "reloading model"
        reload()

    @property
    def restart(self):
        print "restarting model"
        restart()   

c = _Context()
