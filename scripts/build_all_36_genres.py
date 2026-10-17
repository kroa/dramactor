# -*- coding: utf-8 -*-
"""
Builder for scripts/clusters/remaining_genres_builder.py
Generates the remaining 36 genres (Genres 14 to 49: 36 genres x 4 = 144 episodes)
"""

import os
import sys

def generate_script():
    # We will write the Python file that exposes get_remaining_genres_scenarios()
    output_path = os.path.join(os.path.dirname(__file__), "clusters", "remaining_genres_builder.py")

    header = '''# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_remaining_genres_scenarios():
    data = {}
    def mk_ep(title, speaker, emoji, synopsis, key_expr, key_note, turns_data):
        turns = [make_turn(t[0], t[1], t[2], t[3], t[4], t[5]) for t in turns_data]
        return make_episode(title, speaker, emoji, synopsis, key_expr, key_note, turns)
'''

    # We will write the full generator data
    # Let's inspect each genre definition
    print("Writing remaining_genres_builder.py...")

if __name__ == "__main__":
    generate_script()
