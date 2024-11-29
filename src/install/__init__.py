from ..app import client
from time import sleep

def images_exists(imageName):
  images = client.images.list()
  for image in images:
    if imageName in image.tags:
      return True
  return False

def install_image(target):
  if target == "basic":
    if not images_exists("bcBasic"):
      client.images.build(path=".", tag="bcBasic")
      sleep(30)
      return "bcBasic"
    return "bcBasic"
  elif target == "normal":
    if not images_exists("bcNormal"):
      client.images.build(path=".", tag="bcNormal")
      sleep(30)
      return "bcNormal"
    return "bcNormal"
  elif target == "pro":
    if not images_exists("bcPro"):
      client.images.build(path=".", tag="bcPro")
      sleep(30)
      return "bcPro"
    return "bcPro"
