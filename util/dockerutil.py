# coding=utf-8
import json

import docker
import requests


class DockerManager():

    def __init__(self):
        pass

    def list_all_images(self):
        client = docker.from_env()
        for image in client.images.list():
            print(image.id)

    def version(self):
        return requests.get('http://localhost:2376/version').content


if __name__ == '__main__':
    dockerm = DockerManager()
    print(json.dumps(dockerm.version()))
