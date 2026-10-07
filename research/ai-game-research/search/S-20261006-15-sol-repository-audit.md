# 搜尋批次 S-20261006-15：GPT-6.1 Sol 最新 repo 逐項查核

**日期：**2026-10-06（台北時間）  
**研究問題：**追查 S14 找到的 Space Attack 和 ORBITAL 是否有高系統任務價值，以及一次輸入、可玩 build、模型證據、成品畫面和測試資料。

## 查重與來源

先查[全目錄](../catalog.html)、[歷史索引](../history/index.md)及[搜尋索引](index.md)。S14 已將兩作列為待逐項核實，尚未建立固定紀錄；同名與 repo URL 查找沒有命中既有記錄。原始發現來源是 [AgentsLoop 作品目錄](https://github.com/AgentsLoop/awesome-gpt-astra-games)，該頁標記截至 2026-10-04 有 Space Attack、ORBITAL 兩筆 GPT-6.1 Sol 條目。其模型分數只作線索，不直接當品質結論。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯項目 | 判斷／重查條件 |
|---|---|---|---|
| `site:github.com "GPT-6.1 Sol" "Space Attack"`; [作者 repo](https://github.com/vannorman/space_attack); [作者 live build](https://vannorman.github.io/space_attack/); [策展項目紀錄](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/games/space-attack/readme.md) | 作者自述 GPT-6.1 Sol Light、約 1.5 小時，公開可玩 HTML Canvas shooter 與多輪 prompt。Prompt 1 要 AI 先問澄清問題，作者回答設計預設；Prompt 2、3 有大幅玩法／美術／平衡改動，另有測試作弊鍵。作者稱共三次 play-feedback-prompt 循環。遊戲有波次、Boss、升級、掉落、粒子、程序合成音樂；策展者未記錄截圖，未作獨立完整 playtest。 | [G0219](../records/G0219.md) | 明確排除 one-shot 成績；保留 Prompt 1 作中階 shooter 重跑 seed，但須把澄清答案合併、給新模型一次完整委託。只有作者另釋出 frozen first build／no-follow-up trace 時再核流程。 |
| `site:github.com "GPT-6.1 Sol" "ORBITAL" game`; [原作者 repo](https://github.com/SunnyWell81-ai-generated/orbital-game); [驗證文件](https://github.com/SunnyWell81-ai-generated/orbital-game/blob/main/VALIDATION.md); [原始測試](https://github.com/SunnyWell81-ai-generated/orbital-game/tree/main/tests); [策展項目紀錄](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/games/orbital/readme.md) | README 歸因 GPT-6.1 Sol，提供 source 和可下載 browser build，無 hosted demo／截圖。十色軌道增量玩法有多層升級、prestige／rebirth、8 技能、科技樹、自動化、離線收益與存檔；分層經濟使用巨大數函式庫，作者列 16 項測試與進度模擬。repo 只有一個可見 commit；未找到原始 prompt／session、實際生成日或介入情況。沒有獨立執行測試、遊玩或評畫面。 | [G0220](../records/G0220.md) | 保留作高系統密度的重跑題型線索，但不算已驗證 one-shot 或美術候選。補到原始 prompt／trace、live gameplay 或可用畫面後再評估。 |
| [近期模型目錄索引](https://github.com/AgentsLoop/awesome-gpt-astra-games)、[原始作者 repos](https://github.com/vannorman/space_attack)、[ORBITAL source](https://github.com/SunnyWell81-ai-generated/orbital-game) | 核實目錄遊戲 entry 的 model label、creator evidence 等級和材料性質。Space Attack 的 7.8/10 是策展者對來源／規格的打分且沒有 screenshot；ORBITAL 的 7.7/10 同樣不是畫面評分或獨立實玩結果。 | [G0219](../records/G0219.md)、[G0220](../records/G0220.md) | 不以第三方分數替代使用者美術判定；目錄僅作發現索引，逐項查原始 repo 後才能下結論。 |

## 本輪結論

- 兩個 GPT-6.1 Sol 新項目都已逐項回到原 repo 核查；S14 的待查事項結束。
- Space Attack 有充足可重用的 2D shooter 規格和可玩成品，但作者多輪澄清及 play-feedback 修改清楚違反「一次委託後不再由使用者介入」，也未提供足夠畫面證據支持作為美術候選；保留任務作重跑參考，不能把公開成品說成 one-shot 成績。
- ORBITAL 是高系統密度、持續進度與狀態處理的測試題型來源，且公開作者測試程式；一次生成流程、原始委託和視覺表現均未核實，故只作待查重跑線索。
- 本輪沒有足以新增現行精選成品候選的證據；未同步候選簡報與 HTML，以免把缺口未補齊的案例誤列為已驗證候選。兩筆完整紀錄及來源已進資料庫。

## 下一輪方向

1. 從作品目錄中回查 2026-10-04 排名前列、不同於純射擊／增量的 Opus 5.5 成品，優先查 Mana Wars、SELF PLAY、Odyssey of the Living Cap 是否有可用原始 brief、可玩材料及無中途人類介入證據。
2. 從獨立展示 gallery 查詢最新 Sol、Astra 的帶 prompt／session 線索，而不只依賴 curated game repositories。
3. 若候選的公開 prompt 只要求單一小 loop，繼續篩掉；尋找跨玩法／進度／存檔／自主 QA 的任務規格。
