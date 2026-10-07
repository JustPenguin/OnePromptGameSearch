# 搜尋批次 S61：CSDN Codex 遊戲教程 canonical URL 與可讀來源追查

**日期／範圍：**2026-10-07；針對 S56/S59 暫存的 CSDN「Codex + GPT Image 2.0 完成可玩遊戲」文章，查 canonical URL、站內索引、搜索引擎摘要及可讀代理；不依標題假定它有高系統遊戲或 one-shot run。

## 研究問題與查重

新一輪前先重讀研究索引、候選摘要、搜尋索引；`manage.py lookup 'AI全流程制作游戏教程'` 及 `lookup 'Codex GPT Image 2.0 game tutorial'` 皆無項目。S56 只有文章標題／搜尋命中而沒有保存 canonical URL；S59 直接原文一度回 HTTP 521。只有找回可讀一手頁、mirror、作者 repo 或成品時才新增記錄。

## 實際搜尋與查閱

| 實際 query／來源 | 結果與判斷 | 關聯紀錄 | 阻礙／解除條件 |
|---|---|---|---|
| Bing HTML：`"AI全流程制作游戏教程分享：Codex + GPT Image 2.0"`；`"AI全流程制作游戏教程分享" Codex GPT Image`；`"从0开始完成一个可试玩游戏" Codex` | 精確標題與句段查詢未找到該 CSDN article；主要回傳泛用 Codex／AI 首頁，沒有可確認 canonical URL。| S56 未確認線索 | 需要原 S56 DuckDuckGo 命中的 article URL、文章作者／ID，或可索引的鏡像連結。|
| Bing HTML：`AI全流程制作游戏教程分享 Codex GPT Image 2.0 从0 可试玩 CSDN`；`AI全流程制作游戏 Codex GPT Image 2.0 完整思路 CSDN`；`Codex + GPT Image 2.0 从0开始 可试玩游戏 site:blog.csdn.net`；`AI游戏 tutorial Codex GPT Image 2.0 夜巡录 CSDN` | 四個 query 未找到可辨識同篇教程的條目。Bing 回傳結果混有 OpenAI 首頁、Gemini、DeepAI 和舊 Codex 說明，沒有對應該文章或同作品。未將泛用工具頁當相關證據。| S56 未確認線索 | 有 canonical URL 後直接查該 URL／可讀 mirror。|
| Sogou HTML：同上四個中文 query | 返回約 5.4 KB 站殼，未取得可見搜尋命中；不記作該文不存在的證據。| S56 未確認線索 | 搜尋頁若能取得實際結果，檢查標題、作者及網址。|
| CSDN 站內：`https://so.csdn.net/so/search?q=%22AI全流程制作游戏教程分享：Codex + GPT Image 2.0%22&t=blog`；並試 `https://so.csdn.net/so/search?q=%22Codex + GPT Image 2.0%22 游戏 可试玩&t=blog`；[專站代理首頁](https://r.jina.ai/http://blog.csdn.net/) | 站內查詢回傳只有 app shell／WAF CAPTCHA 載入，沒有 server-rendered results；專站代理只可讀首頁。查詢本身受站內 anti-bot gate 阻擋，不代表文章不存在。| S56 未確認線索 | 需 canonical article URL，或人類可通過 CAPTCHA 的查詢／文章頁公開 mirror；本研究不能猜解 challenge。|
| S56 已記錄的原始 CSDN article 直達（URL 未留在資料） | 當時 HTTP 521；現在無 canonical URL 可重試同一頁，也沒有可核網址可列入項目 sources。| S56 未確認線索 | 使用者若保有原搜尋結果／瀏覽器歷史，提供網址即可重查；或作者公開 GitHub／Demo／替代文章。|

## 結論、阻礙與後續

- 本批沒有找回 canonical CSDN URL 或文章內容，故不新增遊戲／案例紀錄，不從標題或過期摘要推斷玩法、模型／版本或 one-shot 流程。
- 已嘗試 Bing exact/title variants、Bing 關鍵詞、Sogou、CSDN 站內搜尋和 CSDN readable proxy；證據狀態是「來源未確認，CSDN 站內受 WAF CAPTCHA 阻擋」，不是「已排除文章」。
- S54 後本批是第 **7** 個彼此不同、沒有新增強候選或顯著提升既有 one-shot evidence 的方向（S55–S61）；主要 benchmark 和近期可玩模型輸出已在 S24/S33/S40/S44–S54 等批次複核。
- **尚未能完全關閉的具名來源線索：**此 CSDN article 的 canonical URL 缺失；G0269 Bolt Tower 的 Bolt session 連結訪客導向登入，故 prompt/model/transcript 不可讀。解除條件分別是原文網址／作者 repo，及可匿名讀取的 session transcript 或作者提供的 task/model/build trace。若無其一，兩者維持未確認，不得宣稱研究內容已排除或 Bolt run 已稽核。
- 本工作區研究狀態維持「持續研究中」。若後續未取得解除資料，可從有第一手來源的現存 shortlist 繼續覆查近期模型 output；本批不重做 S47，下一個獨立方向需先讀三份索引再選擇。
