# 搜尋批次 S48：固定完整任務的公開模型盲測與可玩交付集

**查核日期：**2026-10-07（台北時間）  
**搜尋方向：**尋找公開、同一完整遊戲生成任務、多模型、盲評或獨立評分、且保留可玩凍結交付物的比較組。這是依 S47 留下的方向；不重做 Hill Climb、GameDevBench 或 S47 模型作品搜尋。  
**收尾計數：**S47 對 G0077 的任務、測量及流程證據有實質補強，因此本批開始前計數為 0；本批未找到新強候選，也未顯著補強既有完整遊戲生成案例，計數增至 1／至少 3。

## 開始前查重

先讀研究索引、候選摘要、搜尋索引及 S47。查過全目錄的對照題、prompt、作者與基準名稱，特別核對 G0077（Hill Climb）、G0137／B0036（Single HTML Game Bench）、B0009（Game Bench）、B0022（LMGame-Bench）、B0043（WebGameBench）、B0052（A2Z GameSpec-Bench）、B0053（目前最新正式 benchmark 條目）及最近 S30–S47。重複或已覆蓋的同題頁不另建候選。

## 實際搜尋查詢

使用 DuckDuckGo HTML 搜尋，2026-10-07 執行：

1. `"blind" "game generation" benchmark playable AI agent 2026` — 無結果。
2. `"same task" game coding agents blind evaluation playable build 2026` — 無結果。
3. `"same prompt" AI game agent evaluation benchmark playtest score 2025 2026` — 無結果。
4. `"game generation" "blind evaluation" AI agents playable game one prompt` — 無結果。
5. `AI coding agent game benchmark identical brief frozen build blind judge 2026` — 回傳一般 coding-agent leaderboard／榜單文章，未見遊戲生成的同題盲測組。
6. `AI generated video game agents benchmark human evaluation blind playtest 2026` — 回傳 GameWorld、LMGame-Bench／GamingAgent 等遊戲操作 agent benchmark，以及泛用 benchmark 頁。
7. `one prompt video games AI coding benchmark human ratings same task agent 2026` — 主要是泛用 coding-agent 對照文，未見符合條件的完整遊戲盲測。
8. `playable same prompt game generation AI agents compare` — 主要是 prompt-to-game 產品清單、通用生成器文章及既有模型比較線索，未見公開的凍結多模型交件集。
9. `large language model generated games benchmark player study game quality coding agents` — 回傳 LMGame-Bench 等「遊玩既有遊戲」研究，非「生成新遊戲」。
10. `AI game development agent competition same prompt tasks human judge games 2026` — 找到 IEEE CoG 2026 competitions 與 GDMC 2026 聚落生成競賽，進一步核對規格。
11. `"GameWorld" "170 tasks" benchmark github multimodal game agents`、`"GameWorld-RT" benchmark github` — 找到 GameWorld 官方 repo、project page 及 arXiv 全文。
12. `"2604.07429" benchmark code` — 搜尋頁無結果；改由官方 GameWorld repo 與 project page 查核。
13. `GDMC 2026 AI settlement generation challenge rules Minecraft competition` — 找到 GDMC 2026 itch.io 頁、年度規則頁和歷屆 GDMC 網站。
14. `site:gdmc.cs.mcgill.ca 2026 settlement generation competition` — 無結果；改以主辦方 CoG 頁和 GDMC wiki 核實。

## 查閱來源與處置

| 來源 | 直接核對結果 | 判斷／去向 |
|---|---|---|
| [IEEE CoG 2026 competitions](https://cog2026.org/competitions) | 官方頁列出 Planet Wars、Tales of Tribute、BotPrize、GDMC、DareFightingICE、StarCraft 及 Neurogame Jam 等競賽；多數是建立 agent 操作現成遊戲或提交遊戲生成演算法。 | 頁面沒有同一個完整新遊戲 brief 的多模型交付集、one-shot/無 follow-up 規則、playable build 冻結規則或盲評協定；不符合新強候選條件。GDMC 子項另建 [E0009](../records/E0009.md) 作具名排除。 |
| [GDMC 2026 官方規則與結果](https://gendesignmc.wikidot.com/wiki:2026-settlement-generation-competition)；[CoG listing](https://cog2026.org/competitions#gdmc)；[itch.io 活動頁](https://itch.io/jam/gdmc2026) | 任務是提交生成器，對未知 Minecraft 地圖產生 settlement；不限生成方法，使用 Minecraft Java 1.21.11。2026-07-01 截止，每隊一份投稿；由人類評審環境適應、功能性、敘事及美術，結果頁列十組輸出地圖。 | 是高價值程序式世界／聚落生成素材，但提交演算法可自行開發迭代，沒有一次使用者委託或自主 agent trace；輸出是既有 Minecraft 內的 settlement，不是完整可玩新遊戲。作子題／方法參考，排除嚴格生成候選。 |
| [GameWorld paper](https://arxiv.org/abs/2604.07429)；[全文](https://arxiv.org/html/2604.07429)；[官方 GitHub](https://github.com/gameworld-project/gameworld)；[專案頁](https://gameworld-project.github.io/) | 論文與 repo 說明 34 款既有 browser games、5 類、170 個操作任務及 18 組模型／介面結果；以 `gameAPI` state 作 deterministic outcome evaluator，另有持續時間運轉的 GameWorld-RT。 | 評估 agent 玩既有遊戲，不評估 agent 寫／建置／測試／交付新遊戲；固定 roster 及遊玩 evaluator 也不是任意生成 build 的通用 evaluator。收作 [B0054](../records/B0054.md) 鄰接方法參考，排除核心候選。 |
| [LMGame-Bench／GamingAgent repo](https://github.com/lmgame-org/GamingAgent)；既有 [B0022](../records/B0022.md) | 官方 repo 自述為 LLM/VLM gaming agents，提供多遊戲操作任務與 benchmark 比較。 | 這是另一項操作既有遊戲的 benchmark，與既有 B0022 重複且不測新遊戲生成；不新增紀錄。 |
| 既有 [Game Bench](https://game-bench.piccini.app/)（B0009／S10）、[WebGameBench](../records/B0043.md)、A2Z／GameCraft／GameASG 等 | 對照已有資料確認其固定提示、agent turn、gameplay 驗收或生成任務內容；這些已在 S10、S40、S44–S45 等批次覆查。 | 本方向沒有找到新公開盲測組、凍結版本集合或顯著新證據；不重建既有資料。 |

## 結論

本方向未找到同一高系統完整遊戲任務由多個模型完成、以可玩凍結 build 作盲評或有獨立評分的公開比較集。命中最接近的是 GDMC 程序聚落生成挑戰與 GameWorld／LMGame 既有遊戲操作 benchmark；前者輸出範圍不是新遊戲，後兩者測 gameplay agent。沒有新強候選，也沒有顯著補強既有案例；無增益方向累計 **1／至少 3**。

## 待查與下一個不同方向

- GDMC 公開地圖可供未來研究程序關卡／場景生成，但本研究若不擴展到「完整遊戲中的單一內容生成子題」，不需繼續追該競賽。
- GameWorld 可參考狀態驗收設計；除非未來有生成遊戲通用 API／自動化建置的研究，否則不再重查。
- 下一方向：逐一查近期正式生成 benchmark 的資料、runner 和 evaluator 是否已釋出／新增當前模型結果，優先針對 S44 當時仍未釋出的 A2Z GameSpec-Bench、GameXpert-Bench 與 PlaytestArena，並核對 GameASG／GameCraft 的新 roster；不要把 agent 玩既有遊戲的分數算成遊戲生成成績。
