from subprocess import call, check_output

from settings import JPG_PATH, JPG_FILENAME


__author__ = 'laurogama'


def camera_enabled():
    result = check_output(["vcgencmd", "get_camera"])
    return "detected=1" in result


def take_picture():
    if camera_enabled():
        call(["raspistill", "-o", JPG_PATH + "/" + JPG_FILENAME])
