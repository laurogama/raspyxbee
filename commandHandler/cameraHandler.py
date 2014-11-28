from subprocess import call, check_output

JPG_FILENAME = "image.jpg"
JPG_PATH = "/home/pi/projetos/rest/static"

__author__ = 'laurogama'


def camera_enabled():
    result = check_output(["vcgencmd", "get_camera"])
    print result
    return "detected=1" in result


def take_picture():
    if camera_enabled():
        call(["raspistill", "-o", JPG_PATH + "/" + JPG_FILENAME])
