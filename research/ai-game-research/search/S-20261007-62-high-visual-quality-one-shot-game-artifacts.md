# 搜尋批次 S62：高視覺品質的一次委託遊戲與 3D 藝術輸出

**日期／範圍：**2026-10-07；優先找近期 coding model 產出的高完成度遊戲畫面，核對原作者貼文、玩法與 one-shot 說法。美術為獨立高權重軸，3A 呈現是搜尋優先級；本批不把 3D 世界展示自動當作遊戲。

## 研究問題與先前查重

新一輪先閱讀 `ai-game-one-shot-index.md`、候選摘要、`search/index.md`，並查 `catalog.md`／既有記錄中的 Claude of Duty、Opus 5 作品、one-shot 與視覺參照。Claude of Duty 已由 [G0035](../records/G0035.md) 收錄；不重建同一作品紀錄。上一批 S61 後無增益方向累計為 7；本批尋找可見高質感 gameplay、原始任務／run provenance，或能顯著補強既有案例的新證據。

## 實際搜尋與查閱

| 實際 query／來源 | 結果與證據 | 關聯紀錄 | 判斷／後續 |
|---|---|---|---|
| DuckDuckGo HTML：`AI generated game playable 3D visual quality benchmark 2026 game generation coding agent`；`one prompt AI generated game 3D visual style game demo 2026`；`AI coding agent created 3D game high quality graphics playable build 2026`；`AI game generation benchmark art quality playable 3D visuals` | 命中 2026-07-26 Min Choi 策展串及 SaaSCity、MindStudio 二手整理；找到 Opus 5 遊戲／世界視覺線索。兩篇整理不是每個作品的原始 prompt 或 session。 | [G0035](../records/G0035.md)、本批新記錄 [G0272](../records/G0272.md) | 以作者原始貼文逐項核實；文章稱 AAA 的描述不作美術結論。|
| DuckDuckGo：`"Opus 5" "single prompt" "FPS" Matt Shumer game 2026`；`"Lentils80" game 3D grass world one prompt`；`"0xRishi" Opus 5 game playable zombies`；`"saturadev" Opus 5 game one prompt Unity`；`"Opus 5" "snowboarding" game prompt playable`；`"Claude Opus 5" "one-shot" game build github playable` | 回傳原始 X 來源與同一作品線索。Claude of Duty 是既有 G0035；SaturaDev 原文稱「我一直要求模型改善各方面並檢查 bug」，明確不符合一次委託；Rishi 是以 Opus 5 修改 Kimi K3 舊遊戲，並非空專案生成；其餘命中不能僅依策展標題視為 one-shot 遊戲。 | G0035；不新增被排除作品紀錄 | 不重複登錄 Claude of Duty。Rishi 的既有程式碼起點、SaturaDev 多輪改進，排除於嚴格 one-shot 成績；若找到新 frozen first build 再重查。|
| [Min Choi 原始 X 串](https://x.com/minchoi/status/2081414653146460668)；串內 [Lentils 原始貼文](https://x.com/Lentils80/status/2081136109778538917)；[作者 CodePen](https://codepen.io/lentils801/pen/019f9b4b-10d7-7f77-817f-f4eb83fdb289) | 作者稱 Claude Opus 5 單次輸入產生單一 HTML、程序式繪畫風草原及風動草葉；原貼文含 71 秒影片。CodePen 訪客存取 HTTP 403。研究者直接檢視 X 影片：有一致風格的山丘／草地／河橋、暖光與霧景；未見可辨遊戲目標或機制。 | 新增 [G0272](../records/G0272.md) | 保留作視覺參照；不列完整遊戲候選。原始 prompt、source、session、可操作 build 和一個遊戲循環均未核。使用者美術評價待定。|
| [SaaSCity 二手整理](https://saascity.io/blog/claude-opus-5-one-shot-3d-games-worlds-blender-2026)；[MindStudio 二手整理](https://www.mindstudio.ai/blog/claude-opus-5-ai-game-generation)；串中 [New Amsterdam 作者貼文](https://x.com/levelsio/status/2081339304752640137)與[可探索頁](https://skunkworks.levels.io/newamsterdam) | 兩文列出 CoD FPS、Brawl Stars 類 Unity 戰鬥、繪畫式草原、New Amsterdam 歷史城市等。New Amsterdam 作者稱「mostly one-shotted」並留有不完美處；可探索城市和視覺有價值，但未核遊戲循環、任務全文或 session。Brawl Stars 類案例原作者明示連續要求改善／查錯；FPS 已是 G0035。 | G0035、G0272 | 不把 world walkthrough 或 iterative game 改稱完整 one-shot 遊戲；城市作品可在原始任務／有勝負玩法公開後重查。|

## 結論與更新去向

- 沒有找到同時有高視覺品質實際 gameplay、可核完整遊戲範圍及足夠一次委託 evidence 的新強候選，也沒有取得能顯著補強既有主要候選的 session／任務證據。
- 新增 G0272 留存繪畫式程序草原視覺參照；純環境展示沒有已核遊戲機制，並非主候選。Claude of Duty 命中已去重到 G0035；SaturaDev 自述多輪改善、Rishi 從既有遊戲改造，均不算嚴格一次交付。
- 作者影片由 X 可直接檢視；CodePen visitor page 回 HTTP 403，不能確認其可玩性／完整內容。New Amsterdam 有探索頁和作者貼文，仍欠原 prompt、session 及遊戲系統證據。
- 這是 S54 後第 **8** 個彼此不同且無新增強候選／無顯著 one-shot evidence 增益的方向。完成 S62 的「視覺輸出／原始貼文」方向後，下一批應改查具高美術完成度的正式 benchmark 成品與 player-facing art rubric，勿再泛搜 Opus 5 showcase。
- 本批尚未達整體研究告一段落條件：有未解來源線索（G0269 Bolt session、S56 CSDN 原文 URL），且整體搜尋方向仍持續覆蓋。維持「持續研究中」。
