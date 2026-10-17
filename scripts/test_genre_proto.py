# -*- coding: utf-8 -*-
"""
Prototype test to verify 50 genres x 4 cycles = 200 scenarios generation
"""
import json
import re

with open('src/data/genres.ts', 'r', encoding='utf-8') as f:
    text = f.read()

genre_names = re.findall(r"nameEn:\s*'([^']+)'", text)
print(f"Total genres: {len(genre_names)}")
assert len(genre_names) == 50
