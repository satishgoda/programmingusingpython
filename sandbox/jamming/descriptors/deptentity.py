from collections import OrderedDict


class Entity(object):
    def __init__(self, namespace):
        self._namespace = namespace
    
    @property
    def namespace(self):
        return self._namespace

class Entities(OrderedDict):
    def add(self, entity):
        if not isinstance(entity, self.__class__.vtype):
            raise ValueError("Cannot add this value")
        self[entity.namespace] = entity

class ShotEntity(Entity):
    pass

class ShotEntities(Entities):
    vtype = ShotEntity
    pass

class SharedShotEntity(Entity):
    pass

class SharedShotEntities(Entities):
    vtype = SharedShotEntity
    pass

class SharedShotSiblingEntity(Entity):
    pass

class SharedShotSiblingEntities(Entities):
    vtype = SharedShotSiblingEntity
    pass

class EntitiesProperty(object):
    def __init__(self, id, idtype):
        self.id = id
        self.idtype = idtype
    
    def init(self, inst):
        inst.__dict__[self.id] = self.idtype()
    
    def __get__(self, inst, cls):
        if inst is None:
            return self
        return inst.__dict__[self.id]

class ShotManager(object):
    def __init__(self):
        self._initProperties(self)
    
    @classmethod
    def _initProperties(cls, inst):
        for value in cls.__dict__.itervalues():
            if isinstance(value, EntitiesProperty):
                value.init(inst)

    def gatherEntities(self):
        pass
    
    def initializeEntities(self):
        pass

class DeptShotManager(ShotManager):
    entities = EntitiesProperty('shot', ShotEntities)
    
    def __init__(self):
        super(DeptShotManager, self).__init__()
    
    
class DeptSharedShotManager(ShotManager):
    entities = EntitiesProperty('shot', SharedShotEntities)
    siblings = EntitiesProperty('siblings', SharedShotSiblingEntities)

    def __init__(self):
        super(DeptSharedShotManager, self).__init__()

ashmgr = DeptShotManager()

ashmgr.entities

ashshmgr = DeptSharedShotManager()

ashshmgr.entities
ashshmgr.siblings

bam = SharedShotEntity('bam')

ashshmgr.entities.add(bam)

ashshmgr.entities
ashshmgr.siblings
