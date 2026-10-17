# -*- coding: utf-8 -*-
"""
Helper utilities for creating standardized 3-turn drama episodes
"""

def make_turn(dialogue, korean, hint, killer, mediocre, konglish):
    """
    killer: (english_text, korean_meaning, feedback)
    mediocre: (english_text, korean_meaning, feedback)
    konglish: (english_text, korean_meaning, feedback)
    """
    return {
        "dialogue": dialogue,
        "korean": korean,
        "hint": hint,
        "choices": [
            (killer[0], killer[1], "native_killer", killer[2]),
            (mediocre[0], mediocre[1], "mediocre", mediocre[2]),
            (konglish[0], konglish[1], "wrong_konglish", konglish[2]),
        ]
    }

def make_episode(title, speaker, emoji, synopsis, key_expr, key_note, turns):
    assert len(turns) == 3, f"Episode '{title}' must have exactly 3 turns, got {len(turns)}"
    return {
        "title": title,
        "speaker": speaker,
        "emoji": emoji,
        "synopsis": synopsis,
        "key_expr": key_expr,
        "key_note": key_note,
        "turns": turns
    }
