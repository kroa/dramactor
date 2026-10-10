import os
import shutil
import time
from gradio_client import Client, handle_file

def main():
    print("Initializing Wav2Lip ZeroGPU Client...")
    client = Client("pragnakalp/Wav2lip-ZeroGPU")

    episodes = [1, 3, 4, 5, 6, 7] # 2 is already done

    for ep in episodes:
        face_path = os.path.abspath(f"scratch/ref_face_ep{ep}.png")
        if not os.path.exists(face_path):
            print(f"Skipping EP {ep}: face image not found")
            continue

        for turn in range(1, 4):
            dst = f"public/videos/ep{ep}_turn{turn}.mp4"
            if os.path.exists(dst) and os.path.getsize(dst) > 10000:
                print(f"Already exists: {dst}")
                continue

            audio_path = os.path.abspath(f"public/audio/dialogues/ep{ep}_turn{turn}.mp3")
            if not os.path.exists(audio_path):
                print(f"Audio not found: {audio_path}")
                continue

            print(f"Generating EP {ep} Turn {turn}...")
            for attempt in range(3):
                try:
                    res = client.predict(
                        input_image=handle_file(face_path),
                        input_audio=handle_file(audio_path),
                        api_name="/run_infrence"
                    )
                    shutil.copy2(res['video'], dst)
                    print(f"Successfully generated {dst}: {os.path.getsize(dst)} bytes")
                    break
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed for EP {ep} Turn {turn}: {e}")
                    time.sleep(3)

    print("All episodes lip-sync generation completed!")

if __name__ == '__main__':
    main()

