from hashlib import sha256
import datetime

class Block:
  def __init__(self,blockID:int,data,prevData:str=None):
    self.blockID = blockID
    self.data = data
    self.prevData = prevData
    self.proof = None
    self.hashblock = None
  def addChain(self) -> tuple:
    if not self.prevData:
      #blockChain format: (blockID)--data-timeNows-prevData
      self.proof = f"{self.blockID}--{self.data}--{datetime.datetime.now()}"
      self.hashblock = sha256(self.proof.encode()).hexdigest()
    else:
      self.proof = f"{self.blockID}--{self.data}--{datetime.datetime.now()}-{self.prevData}"
      self.hashblock = sha256(self.proof.encode()).hexdigest()
    return self.proof,self.hashblock
  def getBlock(self,id):
    if self.blockID == id:
      return self
    return None
