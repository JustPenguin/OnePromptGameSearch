# S22 · 最新遊戲基準與高複雜度可玩 build

**日期：**2026-10-06　**研究方向：**找最新公開 benchmark 的單一請求／長篇任務資料，以及回到模型公開遊戲 showcase 核對有無可重跑的高系統成品；本輪特別查近週社群 run 和一次委託 benchmark dataset 是否已釋出。

## 實際搜尋詞

- `2026 AI coding agent built complete game one prompt playable game autonomous testing release Claude Opus 5.5 GPT-6 game showcase`
- `site:github.com "one prompt" "game" "Opus 5.5" browser playable 2026 AI game built`
- `AI game generation benchmark full game development agent long horizon playable game build task benchmark 2026 research paper`
- `AI game generation showcase autonomous agent game development one prompt self playtest full game 2026`
- `site:a2z-gamespec-bench.github.io A2Z GameSpec Bench tasks dataset GDD images demo github`
- `site:github.com A2Z GameSpec-Bench krafton-ai a2z-gamespec-bench`
- `site:github.com GameXpert-Bench 2608.21833 GameGen 97 tasks game benchmark`
- `site:github.com/frostsource/8bit-ai-arena Opus 5.5 Astra 6 Luna prompt game runs`
- `"Tidewater" "Opus 5.5" fishing game 8 hours prompt playable`
- `"3D zombie FPS" "49 minutes" "Sonnet 5.5" one prompt playable`
- `site:reddit.com/r/aigamedev "fishing game" "Opus 5.5" "Tidewater"`
- `site:reddit.com/r/aigamedev "zombie FPS" "Sonnet 5.5" 49 minutes`
- `site:reddit.com "This interactive island was built in 8 hours with Opus 5.5"`
- `site:reddit.com/r/singularity Tidewater fishing island Opus 5.5 Dan Greenheck`
- `site:github.com/dgreenheck/tidewater prompt history Opus 5.5 every commit co-authored iterative prompts`
- `"BridgeMind" "DEAD SIGNAL: EXCLUSION ZONE" Sonnet 5.5 single prompt`
- `"2104662073561264283"`
- `site:bridgemind.ai Sonnet 5.5 zombie FPS one prompt 49 minutes`

## 查閱來源與結果

### 有新可重跑價值／重要證據升級

- **Ruinseed／8-Bit AI Arena（G0134）：**[README](https://github.com/FrostSource/8bit-ai-arena)、[518 行 prompt](https://github.com/FrostSource/8bit-ai-arena/blob/master/PROMPT.md)、[四款 browser builds](https://frostsource.github.io/8bit-ai-arena/)、[作者的 Reddit 說明](https://www.reddit.com/r/aigamedev/comments/1wpokkj/testing_a_game_prompt_with_opus_55_and/)。README 記錄 2026-09-24 將同題 prompt 交給 Opus 5.5、GPT-6 Astra、GPT-6 Sol、GPT-6 Luna；四者均有 source 與 playable build，從 blank folder 起跑。作者稱 Opus、Sol、Luna 各用一則 prompt；Astra 42 分鐘用盡額度後另收到 `continue`，故 Astra 不符合零追問。用時／effort／五小時額度均為作者自述，沒有逐輪 trace。證據升級為近期三個符合 single-prompt 聲稱的 current frontier runs；與嚴格任務匹配之處仍須分開表述。
- **DEAD SIGNAL Sonnet 5.5 run（G0236；連結 G0047 任務族）：**[GitHub source／README／tests](https://github.com/bridge-mind/sonnet-5-5-zombies-game)、[Reddit 轉貼與原始 X 連結](https://www.reddit.com/r/singularity/comments/1wswpv6/claude_sonnet_55_is_one_day_old_and_already/)。repo 稱 Sonnet 5.5 在 Claude Code 使用 subagents、single prompt，Three.js＋TS＋Vite，提供可本機啟動的 FPS、測試程式與 optional headless Chrome QA scripts。社群傳播數據稱 49 分鐘／約 US$177，但原始 X 工具呼叫 403，未有 prompt／session trace／frozen hash；也不確定該 run 是否使用 BridgeBench 438 行 community brief。證據已從「無此模型 build」升為「同系列真實 source build 可重現」，仍不可當已驗證的同規格或全流程 QA 通關案例。

### 排除嚴格 one-shot、保存視覺／技術成品參照

- **Tidewater（G0160）：**[官方 repo／feature 和 test 說明](https://github.com/dgreenheck/tidewater)、[官方 playable](https://dgreenheck.github.io/tidewater/)、[建置流程報導](https://aifrontierpost.com/articles/opus-5-5-built-tidewater-island-game/)。系統深度很高（釣魚張力／魚種與水域／時段、船艇、販售升級、晝夜、海洋與 18 種魚）；但報導明確將它分類為約八小時、多次「add X」「make it better」的 iterative nudging，不是 one prompt。$1,874.40 是作者申報。由於已在舊庫，以 G0160 更新嚴格排除狀態。
- **Sonnet zombie FPS 的網路影片：**轉貼可確認作者所稱 one-shot，repo 可試；但原始 X 403、無精確 prompt、無獨立 QA trace。保存為 G0236 候選但不把費用／耗時宣稱作實證。

### 方法參考（新預印本，但尚無可現成抽用的公開任務庫）

- **A2Z GameSpec-Bench（B0002）：**[2026-09-30 arXiv](https://arxiv.org/abs/2609.39564)、[官方 repo](https://github.com/krafton-ai/a2z-gamespec-bench)。100 份長篇 GDD、50 個 Big 每份平均約 26k tokens／84 outcome requirements；Phaser 起始專案、跨程式碼／畫面 replay／adaptive playtest 的固定依賴契約適合做遊戲任務忠實度參考。paper 的論證含 requirement feedback 後的多輪 revision；官方 repo 此時仍說 code/data forthcoming，未能直接取得 task corpus。保留方法項，不升為可立即重跑題庫。
- **GameXpert-Bench（B0017）：**[2026-08-22 arXiv](https://arxiv.org/abs/2608.21833)、[官方 repo scaffold](https://github.com/Kwen-Chen/GameXpert-Bench)。GameGen 有 97 個從 empty workspace 起始的單次自然語言生成任務、11 類，53 個 2D／44 個 3D；與用戶流程極相符。GameFix、GameOpt 是非目標的修復／多輪 track。官方 repo 明示 benchmark data、runner、model artifacts 都待公開，現有頁面未能提供可逐項交付的 97 任務或 AI build，所以仍只作方法追蹤。

### 無新強候選／查詢排除

- AI Frontier Post 的一 prompt 教學、OrigoZero engine 文章主要是流程教學／廠商平台介紹，沒有足夠資料證明代表性的單次模型 build；其示範有作者繼續給遊戲手感建議，不能直接當零追問成績。
- App-store／泛搜尋重複命中舊有模型、舊文或非遊戲條目；名稱查重後不另開重複紀錄。
- Tidewater 品質高但確認為迭代作品，依目標排除，不以畫面漂亮度替代 one-shot 證據。

## 判斷與後續

Ruinseed 是這輪最重要的模型實物證據升級：三個 current frontier 的同題可玩輸出可供橫向目視／遊玩，但 Astra 有 follow-up，其餘流程仍靠作者自述。DEAD SIGNAL Sonnet 5.5 source build 加強了最新 FPS 系統案例與可建置性，與公開長 prompt 規格的對應關係未能證明。A2Z、GameXpert 的單次生成評估方法都很有用，但任務資料還未釋出，本輪不虛報為可直接重跑題庫。後續從「手工代理平台／含專用引擎」方向接續（S23），並查 Tesana Atomos/LOOP 線索和其他未用過的自動遊玩平台；不重複本輪泛搜尋詞。
