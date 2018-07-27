import re


def text_filter(text):
    in_list = ['root', '.DeviceModel_Lock',
               'DeviceConfigHandler', 'device.RemoteOperHandler']
    if '2018-' in text:
        for in_str in in_list:
            if in_str in text:
                return text
        return ''
    elif '39.108.208.108:' == text.strip():
        return ''
    else:
        return text


cmd_queue = []


def text_filter_pack(text):
    global cmd_queue
    if len(cmd_queue) == 0:
        cmd_queue.append(text)
        return ''
    else:
        is_head = start_with_date(text)
        if is_head:
            pack_text = ''.join(cmd_queue)
            cmd_queue.clear()
            cmd_queue.append(text)
            pack_text = pack_text.replace('39.108.208.108:', '<br>')
            return exclude(pack_text)
        else:
            cmd_queue.append(text)
            return ''


def exclude(text):
    ex_list = ('PushUtil', 'pushUtil', 'Jdbc', 'jdbc', 'HostServiceImpl')
    for t in ex_list:
        if t in text:
            return ''
    return text


def include(text):
    inc_list = ('DeviceModel_Lock','DeviceModel_Light')
    for t in inc_list:
        if t in text:
            return text
    return ''


def start_with_date(text):
    return re.match(r'^\d+-\d+-\d+\s\d+:\d+:\d+\.\d+\s', text)
