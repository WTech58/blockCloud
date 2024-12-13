from hashlib import sha256
from .block import Block

class BlockSave:
  def __init__(self,textData:str):
    self.textData = textData
  def _upload(self,id):
    return Block(id,self.textData).addChain()
  def _get(self,id):
    result = Block.getBlock(id)
    if result != None:
      return result
    else:
      return "找不到該Locker"
  def _clear_all(self):
    return Block._clear()
  def get_all(self):
    return Block.get_all()
  @staticmethod
  def get_with_hash(hash):
    return Block._get_with_hash(hash)

__all__ = ["BlockSave"]
