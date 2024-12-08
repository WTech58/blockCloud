# blockCloud 區塊雲

blockcloud-CLI支持命令式上傳至主網

首先，沒有git的話，可以輸入一下指令(WindowOS)
``` bash
  winget install --id Git.Git -e --source winget
```
下載及安裝後，開始初始化及設置
``` bash
  cd blockCloud/src/install && chmod +x ./blockcloud && ./blockcloud init
```
如果成功的話，恭喜你已經完成設置。以下為blockcloud-cli指令
確認工作目錄
``` bash
  cd blockCloud/src/install
```
添加資料並上傳至區塊鏈(BloudCloud)主網（記得改成適當的值）
``` bash
  ./blockcloud addchain -k <key> -d <data>
```
查看資料（記得改成適當的值）
``` bash
  ./blockcloud getchain -t <all/one> -k <key/null>
```
