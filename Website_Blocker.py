import time
from datetime import datetime as dt

host_path = "/private/etc/hosts"
redirect = "127.0.0.1"
websites_block = ["www.instagram.com", "www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 15, 36):
        with open(host_path, "r+") as host:
            contents = host.read()
            for websites in websites_block:
                if websites in contents:
                    pass
                else:
                    host.write(redirect + "\t" + websites + "\n")
    else:
        with open(host_path, "r+") as host:
            contents = host.readlines()
            host.seek(0)
            for line in contents:
                if not any(websites in line for websites in websites_block):
                    host.write(line)
                host.truncate()
    time.sleep(5)