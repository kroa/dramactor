import json
import os
import asyncio
import edge_tts

VOICE_CONFIGS = {
    1: {"voice": "en-US-GuyNeural", "rate": "-3%", "pitch": "-3Hz"},          # Harvey Specter (Suits)
    2: {"voice": "en-US-JennyNeural", "rate": "+0%", "pitch": "+1Hz"},        # Elena (Silicon Valley VC)
    3: {"voice": "en-US-AriaNeural", "rate": "-2%", "pitch": "+0Hz"},         # Victoria (CFO, Corporate)
    4: {"voice": "en-US-ChristopherNeural", "rate": "+2%", "pitch": "+1Hz"},  # Dr. Burke (ER Surgery)
    5: {"voice": "en-US-EricNeural", "rate": "-3%", "pitch": "-2Hz"},         # Julian (Soho Art Curator)
    6: {"voice": "en-US-GuyNeural", "rate": "-2%", "pitch": "-5Hz"},          # Bobby Axelrod (Hedge Fund Titan)
    7: {"voice": "en-US-ChristopherNeural", "rate": "+1%", "pitch": "-2Hz"},  # Marcus (YC Super Angel)
}

GUIDE_VOICE = "en-US-JennyNeural"

async def generate_file(text: str, voice: str, rate: str, pitch: str, output_path: str):
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        return
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(output_path)
    print(f"Generated: {output_path}")

async def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    episodes_file = os.path.join(base_dir, "src", "data", "episodes.json")
    dialogues_dir = os.path.join(base_dir, "public", "audio", "dialogues")
    guides_dir = os.path.join(base_dir, "public", "audio", "guides")

    os.makedirs(dialogues_dir, exist_ok=True)
    os.makedirs(guides_dir, exist_ok=True)

    with open(episodes_file, "r", encoding="utf-8") as f:
        episodes = json.load(f)

    tasks = []

    for ep in episodes:
        ep_num = ep["episodeNumber"]
        voice_cfg = VOICE_CONFIGS.get(ep_num, {"voice": "en-US-GuyNeural", "rate": "-2%", "pitch": "-2Hz"})

        for turn in ep["turns"]:
            turn_idx = turn["turnIndex"]
            # 1. Counterpart Dialogue Audio
            dialogue_out = os.path.join(dialogues_dir, f"ep{ep_num}_turn{turn_idx}.mp3")
            tasks.append(
                generate_file(
                    turn["dialogue"],
                    voice_cfg["voice"],
                    voice_cfg["rate"],
                    voice_cfg["pitch"],
                    dialogue_out,
                )
            )

            # 2. Choice Target Guide Pronunciation Audio
            for choice in turn["choices"]:
                c_id = choice["id"]
                guide_out = os.path.join(guides_dir, f"ep{ep_num}_turn{turn_idx}_{c_id}.mp3")
                tasks.append(
                    generate_file(
                        choice["targetScript"],
                        GUIDE_VOICE,
                        "-2%",
                        "+0Hz",
                        guide_out,
                    )
                )

    print(f"Total audio clips to generate: {len(tasks)}")
    # Run in batches of 6 for connection stability
    batch_size = 6
    for i in range(0, len(tasks), batch_size):
        await asyncio.gather(*tasks[i : i + batch_size])

    print("All studio-quality audio clips generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())

