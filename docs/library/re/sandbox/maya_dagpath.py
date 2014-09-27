__author__ = 'satish goda'

import re

assetName = 'cat'
lods = ('anim', 'base', 'cans', 'cage')
prefixes = tuple('LMR')

lods = '|'.join(lods)
prefixes = '|'.join(prefixes)

kwargs = {key: eval(key) for key in ('assetName', 'lods', 'prefixes')}

pattern = "\\\|{assetName}\\\|[{lods}]\\\|[{prefixes}]_.+grp".format(**kwargs)

rec = re.compile(pattern)

print rec.search('|cat|anim|L_arm_gro') is not None