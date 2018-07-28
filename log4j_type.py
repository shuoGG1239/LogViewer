import re

import color_util

__cmd_queue = []


def colorize(frame):
    """
    对单行进行着色
    :param frame:
    :return:
    """
    frame = re.sub(r'(admin\d?\.log)', color_util.bold(color_util.colorize('\\1', 'orange')), frame)
    frame = re.sub(r'\s:\s(.+)', color_util.colorize(' : \\1', 'blue'), frame)
    frame = frame.replace('INFO', color_util.colorize('INFO', color_util.LIGHT_BLUE))
    frame = frame.replace('ERROR', color_util.colorize('ERROR', 'red'))
    frame = frame.replace('WARN', color_util.colorize('WARN', 'orange'))
    frame = re.sub(r'(\w+Exception)', color_util.colorize('\\1', 'red'), frame)
    frame = re.sub(r'(\([\w_]+\.java:\d+\))', color_util.colorize(color_util.underline('\\1'), 'red'), frame)
    return frame


def frame_pack(ip, frame):
    """
    整合包 (单次log被分成多段传到logViewer, 因此需要将其拼成一个完整的log包)
    :param ip:
    :param frame:
    :return:
    """
    global __cmd_queue
    if len(__cmd_queue) == 0:
        __cmd_queue.append(frame)
        return ''
    else:
        is_head = start_with_date(frame)
        if is_head:
            pack_text = ''.join(__cmd_queue)
            __cmd_queue.clear()
            __cmd_queue.append(frame)
            # 39.108.208.108
            pack_text = pack_text.replace(ip + ':', '<br>')
            return pack_text
        else:
            __cmd_queue.append(frame)
            return ''


def exclude(ex_list, frame):
    """
    过滤含ex_list中元素的包
    :param ex_list:
    :param frame:
    :return:
    exp: ex_list = ('PushUtil', 'pushUtil', 'Jdbc', 'jdbc', 'HostServiceImpl')
    """
    for t in ex_list:
        if t in frame:
            return ''
    return frame


def include(inc_list, frame):
    """
    过滤不含inc_list中元素的包
    :param inc_list:
    :param frame:
    :return:
    exp: inc_list = ('DeviceModel_Lock', 'DeviceModel_Light')
    """
    for t in inc_list:
        if t in frame:
            return frame
    return ''


def start_with_date(text):
    return re.match(r'^\d+-\d+-\d+\s\d+:\d+:\d+\.\d+\s', text)
