from hashlib import sha256
from .block import Block

class BlockSave:
  def __init__(self,textData:str):
    self.textData = textData
  def _upload(self,id):
    return Block(id,self.textData).addChain()
  def _get(self,id):
    return Block(id,self.textData).getBlock(id)


__all__ = ["BlockSave"]
