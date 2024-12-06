from hashlib import sha256
import datetime,os,json

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
      self.save_to_json()
    else:
      self.proof = f"{self.blockID}--{self.data}--{datetime.datetime.now()}-{self.prevData}"
      self.hashblock = sha256(self.proof.encode()).hexdigest()
      self.save_to_json()
    return self.proof,self.hashblock
  def save_to_json(self):
        # 構建區塊數據字典
        block_data = {
            "blockID": self.blockID,
            "rawData": self.proof,
            "hash": self.hashblock
        }

        # 檢查文件是否存在
        if not os.path.exists("bc.json"):
            # 如果文件不存在，創建新文件並寫入列表
            with open("bc.json", "w") as fp:
                json.dump([block_data], fp, indent=4)
        else:
            # 如果文件已存在，嘗試讀取現有數據並追加新區塊
            try:
                with open("bc.json", "r+") as fp:
                    # 讀取現有數據
                    data = json.load(fp)
                    # 將新區塊數據追加到列表中
                    data.append(block_data)
                    # 移動文件指針到文件開頭
                    fp.seek(0)
                    # 將更新後的數據寫回文件
                    json.dump(data, fp, indent=4)
            except json.JSONDecodeError:
                # 如果文件內容無法解析，則清空文件並寫入新的區塊
                with open("bc.json", "w") as fp:
                    json.dump([block_data], fp, indent=4)
  @staticmethod
  def getBlock(self,id):
    if not os.path.exists("bc.json"):
      f = open("bc.json","x")
      f.close()
      return "已建立"
    with open("bc.json", "r") as fp:
      try:
        data = json.load(fp)  # 讀取JSON數據
        for block in data:
          if block["blockID"] == id:  # 根據ID查詢
            return block  # 返回查詢到的區塊字典
      except json.JSONDecodeError:
        return "JSON 解碼錯誤，無法讀取區塊數據。"
    return None
  @staticmethod
  def get_all():
    if not os.path.exists("bc.json"):
      f = open("bc.json","x")
      f.close()
      return "已建立"
    with open("bc.json", "r") as fp:
      try:
        data = json.load(fp)  # 讀取JSON數據
        return data
      except json.JSONDecodeError:
        return "JSON 解碼錯誤，無法讀取區塊數據。"
  @staticmethod
  def _clear():
    # 清空 bc.json 文件內容
    if os.path.exists("bc.json"):
      with open("bc.json", "w") as fp:
        json.dump([], fp)  # 寫入空列表
        return "bc.json 的內容已成功清空。"
    else:
      return "bc.json 文件不存在。"
