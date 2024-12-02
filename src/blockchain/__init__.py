from hashlib import sha256
from base64 import b64encode,b64decode

class BlockSave:
  def __init__(self,imageData:str=None,textData:str=None):
    self.imageData = imageData
    self.textData = textData
    self.bimage = ""
    if self.imageData != None or self.imageData != "":
      self.bimage = b64encode(self.imageData.encode())
