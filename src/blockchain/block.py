from hashlib import sha256
from base64 import b64encode,b64decode
import sqlite3

conn = sqlite3.connect("bc.db")

class Block:
  def __init__(self,blockID:int,data,prevData:str=None):
    self.blockID = blockID
    self.data = data
    self.prevData = prevData
class BlockChain(Block):
  def __init__():
    pass
