# http://traitlets.readthedocs.io/en/stable/using_traitlets.html


import getpass

from traitlets import HasTraits, Unicode, default
from traitlets import observe, Integer

class Identity(HasTraits):
    username = Unicode()
    num = Integer(5, help="a number").tag(config=True)

    @default('username')
    def _username_default(self):
        return getpass.getuser()
    
    @observe('num')
    def _num_changed(self, change):
        print("{name} changed from {old} to {new}".format(**change))

i = Identity()

i.username

i.num

i.num = 10

Identity.traits(i)

Identity.class_own_traits()

Identity.trait_names(i)
