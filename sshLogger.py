import traceback
import paramiko
from paramiko_expect import SSHClientInteraction


def run_conn_log():
    hostname = '39.108.226.252'
    username = 'root'
    password = 'qwert123/'
    prompt = '.+'

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname, username=username, password=password)
        interact = SSHClientInteraction(client, timeout=10, display=False)
        interact.expect(prompt)
        interact.send('tail -f /home/admin.log')
        interact.tail(line_prefix=hostname + ': ', timeout=65535)

    except KeyboardInterrupt:
        print('Ctrl+C interruption detected, stopping tail')
    except Exception:
        traceback.print_exc()
    finally:
        try:
            client.close()
        except:
            pass
