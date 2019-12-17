import pdb


class Property(object):
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, self.default)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __repr__(self):
        s = super(Property, self).__repr__()
        return self.name + " " + s


class IntProperty(Property):
    default = 0


class FloatProperty(Property):
    default = 0.0


class StringProperty(Property):
    default = "You did not specify anything"


class PropertiesBased(type):

    def __new__(mcs, name, bases, namespace):
        properties = []
        for var, value in namespace.iteritems():
            try:
                if value.__class__.mro()[-2].__name__ in ('Property',):
                    value.name = var
                    properties.append(value)
            except TypeError:
                continue
        namespace['properties'] = tuple(properties[:])
        cls = super(mcs, mcs).__new__(mcs, name, bases, namespace)
        return cls


class PropertyGroup(Property):
    __metaclass__ = PropertiesBased

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            per_instance_group = instance.__dict__.get(self.name)
            if per_instance_group is None:
                instance.__dict__[self.name] = per_instance_group = self.__class__()
                per_instance_group.name = self.name
            return per_instance_group

    def __set__(self, instance, value):
        raise ValueError("You cannot set a PropertyGroup")


class RenderGlobals(PropertyGroup):
    threads = IntProperty()
    flags = StringProperty()


# class Layer(PropertyGroup):
#     objects = StringProperty()

# class MainLayer(Layer):
class MainLayer(PropertyGroup):
    lights = StringProperty()
    objects = StringProperty()


# class OcclusionLayer(Layer):
class OcclusionLayer(PropertyGroup):
    material = StringProperty()
    objects = StringProperty()


class LayerBlocks(PropertyGroup):
    main = MainLayer()
    occ = OcclusionLayer()


class AppClass(object):
    __metaclass__ = PropertiesBased

    def _printLeaf(self, parent, prop_path, prop):
        try:
            value = parent.__dict__[prop.name]
        except:
            value = prop.default
        dotted_path = '.'.join(prop_path)
        print "{0} = {1}".format(dotted_path, value)

    def _printGroup(self, prop_path, group):
        for prop in group.properties:
            prop_path.append(prop.name)
            if isinstance(prop, PropertyGroup):
                # self._printGroup(prop_path, group.__dict__[prop.name])
                self._printGroup(prop_path, getattr(group, prop.name))
            else:
                self._printLeaf(group, prop_path, prop)
            prop_path.pop()

    def printFromRoot(self):
        prop_base_path = [self.__class__.__name__]

        for prop in self.properties:
            prop_path = prop_base_path[:]
            prop_path.append(prop.name)
            if isinstance(prop, PropertyGroup):
                # self._printGroup(prop_path, self.__dict__[prop.name])
                self._printGroup(prop_path, getattr(self, prop.name))
            else:
                self._printLeaf(self, prop_path, prop)


class RootNode(AppClass):
    frame_start = IntProperty()
    frame_end = IntProperty()
    shutter = FloatProperty()
    description = StringProperty()
    renderGlobals = RenderGlobals()
    layerBlocks = LayerBlocks()
