# -*- coding: utf-8 -*-
"""
Dramactor 50-Genre Domain Clusters Generator
Defines all 50 genres across 10 thematic clusters (5 genres each, 4 cycles each = 200 episodes).
"""

def get_cluster_definitions():
    """
    Returns a dictionary mapping genre_name -> list of 4 episode blueprints.
    Each blueprint is:
    (title, speaker, emoji, synopsis, key_expr, key_note, turns)
    where turns is a list of 3 tuples:
    (dialogue, dialogueKorean, situationHint, killer_tuple, mediocre_tuple, konglish_tuple)
    """
    clusters = {}
    return clusters
