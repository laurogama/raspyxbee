from subprocess import call

JPG_FILENAME = "image.jpg"
JPG_PATH = "/home/pi/projetos/rest/static"

__author__ = 'laurogama'


def take_picture():
    call(["raspistill", "-o", JPG_PATH + "/" + JPG_FILENAME])
