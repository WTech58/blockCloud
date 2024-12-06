from hashlib import sha256
from .block import Block

class BlockSave:
  def __init__(self,textData:str):
    self.textData = textData
  def _upload(self,id):
    return Block(id,self.textData).addChain()
  def _get(self,id):
    return Block(id,self.textData).getBlock(id)
  def _clear_all(self):
    return Block._clear()
  def get_all(self):
    return Block.get_all()

__all__ = ["BlockSave"]
