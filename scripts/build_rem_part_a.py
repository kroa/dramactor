# -*- coding: utf-8 -*-
"""
Builder for scripts/clusters/rem_part_a.py (Genres 12 to 24: 13 genres x 4 = 52 episodes)
"""
import sys
import os

code_header = '''# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_rem_part_a():
    d = {}
    def mk(t, s, e, syn, ke, kn, turns):
        return make_episode(t, s, e, syn, ke, kn, [make_turn(x[0], x[1], x[2], x[3], x[4], x[5]) for x in turns])
'''

# We will write out each genre cleanly
with open("scripts/clusters/rem_part_a.py", "w", encoding="utf-8") as f:
    f.write(code_header)

print("Started rem_part_a.py")
