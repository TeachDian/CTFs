![截圖 2022-04-14 下午9 09 01](https://user-images.githubusercontent.com/74231280/163399582-dfdbc6b8-f986-4f64-9854-c6965ac2d5e7.png)

Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag in the same directory too.

> Hint  
> 1.Does that encoding look familiar?
> 2.The str_xor function does not need to be reverse engineered for this challenge.

附檔：1.level2.py  2.level2.flag.txt.enc
# 解法
這題跟第一題幾乎一樣 只有密碼的地方不一樣！

<img width="964" alt="截圖 2022-04-14 下午9 10 16" src="https://user-images.githubusercontent.com/74231280/163400470-08f535b0-3bfa-42b0-b184-b2d5c965ed07.png">

我們只要在空白處多一行

<img width="515" alt="截圖 2022-04-14 下午9 11 05" src="https://user-images.githubusercontent.com/74231280/163400031-b46915e7-6f7b-4d6b-b766-88e13f632592.png">



按執行 輸入文中密碼 flag就出來了

<img width="520" alt="截圖 2022-04-14 下午9 25 15" src="https://user-images.githubusercontent.com/74231280/163400600-f2f57810-1db7-4a05-85ad-55a9d120ee0d.png">
