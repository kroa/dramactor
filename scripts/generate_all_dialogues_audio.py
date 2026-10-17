# -*- coding: utf-8 -*-
"""
Generate Studio Neural Dialogue Audio for all 100 Dramactor episodes.
Uses Microsoft Edge Neural voices tailored to each character and genre.
"""

import asyncio
import json
import os
import edge_tts

GENRE_VOICES = {
    "Legal": {"voice": "en-US-GuyNeural", "rate": "-2%", "pitch": "-2Hz"},
    "Startup": {"voice": "en-US-JennyNeural", "rate": "+1%", "pitch": "+1Hz"},
    "Corporate": {"voice": "en-US-ChristopherNeural", "rate": "-4%", "pitch": "-4Hz"},
    "Medical": {"voice": "en-US-AriaNeural", "rate": "+1%", "pitch": "+0Hz"},
    "Dating": {"voice": "en-US-EricNeural", "rate": "-2%", "pitch": "-1Hz"},
    "Wall Street": {"voice": "en-US-GuyNeural", "rate": "-1%", "pitch": "-4Hz"},
    "Tech": {"voice": "en-US-RogerNeural", "rate": "-2%", "pitch": "-2Hz"},
    "FBI": {"voice": "en-US-ChristopherNeural", "rate": "-3%", "pitch": "-3Hz"},
    "Politics": {"voice": "en-US-AndrewNeural", "rate": "-2%", "pitch": "-2Hz"},
    "Culinary": {"voice": "en-US-GuyNeural", "rate": "+2%", "pitch": "+1Hz"},
    "Espionage": {"voice": "en-US-JennyNeural", "rate": "-1%", "pitch": "+0Hz"},
    "Aviation": {"voice": "en-US-SteffanNeural", "rate": "-2%", "pitch": "-3Hz"},
    "Sports Management": {"voice": "en-US-GuyNeural", "rate": "+1%", "pitch": "+0Hz"},
    "Haute Couture": {"voice": "en-US-AriaNeural", "rate": "-2%", "pitch": "+2Hz"},
    "Crisis PR": {"voice": "en-US-MichelleNeural", "rate": "-1%", "pitch": "+0Hz"},
    "Luxury Real Estate": {"voice": "en-US-AndrewNeural", "rate": "+1%", "pitch": "+0Hz"},
    "Hollywood Agency": {"voice": "en-US-GuyNeural", "rate": "+2%", "pitch": "-1Hz"},
    "5-Star Hotel": {"voice": "en-US-EricNeural", "rate": "-2%", "pitch": "-1Hz"},
    "Fine Art Auction": {"voice": "en-US-RogerNeural", "rate": "-2%", "pitch": "-2Hz"},
    "Investigative Journalism": {"voice": "en-US-ChristopherNeural", "rate": "-2%", "pitch": "-3Hz"},
}

DEFAULT_VOICE = {"voice": "en-US-GuyNeural", "rate": "-2%", "pitch": "-2Hz"}

async def generate_single(text: str, voice_cfg: dict, out_path: str, sem: asyncio.Semaphore):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        return
    async with sem:
        try:
            communicate = edge_tts.Communicate(
                text,
                voice_cfg["voice"],
                rate=voice_cfg["rate"],
                pitch=voice_cfg["pitch"]
            )
            await communicate.save(out_path)
            print(f"[OK] {os.path.basename(out_path)} ({os.path.getsize(out_path)} bytes)")
        except Exception as e:
            print(f"[ERR] {out_path}: {e}")

async def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    episodes_file = os.path.join(base_dir, "src", "data", "episodes.json")
    dialogues_dir = os.path.join(base_dir, "public", "audio", "dialogues")
    os.makedirs(dialogues_dir, exist_ok=True)

    with open(episodes_file, "r", encoding="utf-8") as f:
        episodes = json.load(f)

    # Concurrency limit of 8 for edge-tts
    sem = asyncio.Semaphore(8)
    tasks = []

    for ep in episodes:
        ep_num = ep["episodeNumber"]
        genre = ep.get("genre", "")
        voice_cfg = GENRE_VOICES.get(genre, DEFAULT_VOICE)

        for turn in ep["turns"]:
            t_idx = turn["turnIndex"]
            out_file = os.path.join(dialogues_dir, f"ep{ep_num}_turn{t_idx}.mp3")
            tasks.append(generate_single(turn["dialogue"], voice_cfg, out_file, sem))

    print(f"Queued {len(tasks)} dialogue audio files. Starting batch generation...")
    await asyncio.gather(*tasks)
    print("All dialogue audio files generated successfully!")

if __name__ == '__main__':
    asyncio.run(main())
