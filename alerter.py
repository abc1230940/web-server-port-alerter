import socket
import time
import requests 

targets = [ 
    ("google.com", 80, "TCP"), 
    ("google.com", 443, "TCP"), 
    ("8.8.8.8", 80, "TCP"),
    ("127.0.0.1", 9999, "TCP")] 

SLACK_WEBHOOK_URL = "https://discordapp.com/api/webhooks/1506893084498202694/Dca8EBNr-R3i2UZI46KF5Ds7Mxp5l8HpsqoVGTDp4Llxo8nyYQiZwGsNNqBqypAbzj8r" 

def check_port(target, port, protocol): 
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)

        if protocol == "TCP": 
            result = s.connect_ex((target, port)) 
            s.close() 
            return result == 0

    except Exception as e:
        print(f"System Error checking {target}: {e}")
        return False 

def send_slack_notification(target, port, protocol): 
    payload = {"content": f"{target}:{port}/{protocol} port not responding!"}
    print(payload) 
    requests.post(SLACK_WEBHOOK_URL, json=payload) 

while True: 
    for target, port, protocol in targets: 
        if not check_port(target, port, protocol):
           send_slack_notification(target, port, protocol)     
    time.sleep(3600)
