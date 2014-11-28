from subprocess import call

from flask import send_from_directory


__author__ = 'laurogama'


def take_picture():
    call(["raspistill", "-o", "/tmp/image.jpg"])
    send_from_directory('/tmp', 'image.jpg')


def get_last_picture():
    send_from_directory('/tmp', 'image.jpg')