import traceback
import paramiko
import json
from paramiko_expect import SSHClientInteraction


class User:
    def __init__(self, host, name, password, cmd):
        self.host = host
        self.name = name
        self.password = password
        self.cmd = cmd


def load_user_info():
    with open('userinfo.json') as f:
        info = json.load(f)
        return User(info.get('host'), info.get('name'), info.get('password'), info.get('cmd'))


def run_conn_log():
    user = load_user_info()
    host = user.host
    name = user.name
    password = user.password
    host = '39.108.226.252'
    password = '123qwertGg/'
    prompt = '.+'

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=name, password=password)
        interact = SSHClientInteraction(client, timeout=10, display=False)
        interact.expect(prompt)
        interact.send(user.cmd)
        interact.tail(line_prefix=host + ': ', timeout=65535)

    except KeyboardInterrupt:
        print('Ctrl+C interruption detected, stopping tail')
    except Exception:
        traceback.print_exc()
    finally:
        try:
            client.close()
        except:
            pass
