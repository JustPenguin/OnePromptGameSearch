# 搜尋批次 S59：Bolt Tower Devpost one-shot 塔防作品查核

**日期／範圍：**2026-10-07；追查 S55 曾因 Devpost 403 未確認的 Bolt Tower，以及 S56 無 canonical URL 的 CSDN 教程；先驗證題目／作品是否仍可讀、是否有可用作者 session 或正式 challenge rules。

## 研究問題與查重

開始前重讀研究索引、候選摘要、search index，並查 `manage.py lookup 'Bolt Tower'` 與 `manage.py lookup 'Codex GPT Image game tutorial'`（均無命中）。本輪不重做通用平台搜尋；若 Bolt Tower 的 session／官方規則能補足一次輸入條件，將其記為具名副候選；CSDN 命中只在找到 canonical source 或可讀 mirror 時才判斷內容。

## 實際搜尋與查閱

| 實際 query／來源 | 查核結果與判斷 | 關聯紀錄 | 待查／排除條件 |
|---|---|---|---|
| S55 原始查詢重核：DuckDuckGo HTML `Bolt Tower Devpost AI game Bolt.new playable`；`"Bolt Tower" Devpost AI game Bolt.new playable`；`"Bolt Tower" "Devpost" game generated AI` | 命中 [Bolt Tower Devpost](https://devpost.com/software/bolt-tower)。Devpost 原頁 HTTP 403，但 [Jina readable mirror](https://r.jina.ai/http://devpost.com/software/bolt-tower) HTTP 200，完整列出 track `1-Shot Prompt Challenge`、single-prompt 自述、遊戲 features、live demo、Bolt session、影片與程式建置摘要。這首次讓具名作品內容可核；Devpost 文字仍是提交者自述。新增 G0269 為待核實副候選，不稱 winner 或稽核通過。| 新增 [G0269](../records/G0269.md) | 需取得原始 task／session/model version、author follow-up trace 和 build freeze 才可能作 strict result。|
| [Bolt 官方 hackathon rules](https://worldslargesthackathon.devpost.com/rules)；查詢 `Bolt.new AI Coding Hackathon 1-Shot Prompt Challenge official rules` | 透過 Jina readable mirror HTTP 200 讀到 2025 官方規則：One-Shot Competition 對應單一 prompt；可修錯，但初始 prompt 後新增／編輯功能或 UI 會使專案失格。這提高任務規則和使用者驗收條件的可信度，不等於主辦者稽核了 Bolt Tower 的對話。| [G0269](../records/G0269.md) | 找該作品提交的正式規則版本／比賽結果；目前未見 winner 資訊。|
| [Bolt Tower live demo](https://bolt-tower.netlify.app/)、[Bolt session](https://bolt.new/~/sb1-czijj5rv) | Demo 網站及 Vite JS/CSS assets HTTP 200；程式 bundle 含 tower/wave/upgrade/victory/game-over/level/path 實作字串，支持存在 browser artifact，但本研究未完整遊玩。Bolt session link 將訪客導向登入，不能讀 prompt 或歷史修改；Devpost 的原始 source/session 佐證缺口仍在。| [G0269](../records/G0269.md) | 若登入授權或作者公開靜態 session transcript／repo，重查 exact prompt、model、後續互動和 build hash。|
| DuckDuckGo HTML：`site:github.com "Bolt Tower" game AI`；`site:itch.io "Bolt Tower" AI game` | 除 Devpost／新聞式泛化命中外，沒有找到可認定為同一作品的 GitHub 或 itch 原始碼 mirror；不把相似塔防作品合併。| — | 同一 Netlify source repo 若公開再查重。|
| DuckDuckGo HTML：`"AI全流程制作游戏教程分享" Codex GPT Image 2.0`；`"从0开始完成一个可试玩游戏" Codex`；`site:blog.csdn.net Codex GPT Image 2.0 游戏 完整流程 可试玩`；[CSDN 專站鏡像首頁](https://r.jina.ai/http://blog.csdn.net/) | 精確 title／句段 query 本批無結果；CSDN domain proxy 可讀首頁但未定位該 article 的 canonical URL 或 mirror，原直達頁此前 HTTP 521。因此不新增紀錄、不延伸搜尋 snippet。內容仍未確認，需 canonical URL 或作者 repo 才能重查。| 未確認線索（不是已排除項） | 來源 URL／文章鏡像出現時確認是否同於 G0268 或另一實際成品。|

## 結論與更新去向

- 新增 [G0269 Bolt Tower](../records/G0269.md)：中等系統短篇塔防作品、Devpost 自列 Bolt one-shot track、live demo 可載入；原 session 登入受限、底層模型不明、無 exact prompt／無獨立 playthrough，暫作待核副候選，不放主要 shortlist。美術待使用者評價。
- 2025 hackathon official one-shot rules 與作者所選 track 相互吻合，但只能證明規則內容和提交者聲稱，不證明 Bolt Tower 的 session 合規。此線索仍未達「新強候選」或「顯著補強既有案例」門檻，因此 S54 後無增益方向累計由 4 增為 **5**；也沒有改善既有強候選。
- CSDN 線索仍因 URL 不明、521、精確搜尋未命中而未確認；保持為查找阻礙，沒有排除文章內容。
- 本批新增 game / lead evidence 後，下一輪先重讀三份索引，再查**one-shot hackathon roster／得獎名錄與獨立評測痕跡**，尋找是否另有完整 tower defense／sim game 同類 artifact 或 Bolt Tower 的獲獎／評分，不重搜通用 AI builder 平台頁。
