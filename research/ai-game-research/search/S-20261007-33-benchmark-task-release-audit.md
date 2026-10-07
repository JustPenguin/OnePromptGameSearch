# S33｜正式遊戲生成基準最新結果與可重跑題規格核對

**日期：**2026-10-07（台北時間）  
**研究問題：**檢查既有正式遊戲生成基準有沒有新模型結果、可重跑題庫釋出進展；深入找出能直接交給當前模型、符合一次任務與自主 QA 要求、又具足夠遊戲系統密度的公開任務。  
**先前查重：**重讀研究索引、候選摘要、search/index、S24 和紀錄 B0010（GameASG）、B0011（GameCraft）、B0012（GameDevBench）、B0017（GameXpert），再查 G0056 Fast Food Tycoon。該項此前只在舊台帳提到「與 Airship Trader 重疊、低優先」，本次取得官方任務全文與測試契約後重評。

## 實際搜尋與查閱

搜尋文字：

- `site:github.com GameASG-Bench GPT-6.1 Sol GPT-6 Astra leaderboard 2026`
- `site:arxiv.org game generation benchmark 2026 GPT-6.1 Sol benchmark playable task`
- `GameCraft-Bench GPT-6.1 Sol results 2026 game generation leaderboard`
- `GameXpert benchmark dataset release tasks GPT-6 Astra game coding benchmark 2026`
- `"GameXpert-Bench" GitHub dataset task download`
- `site:github.com/areal-project/GameASG-Bench "Fast Food Tycoon" "target.md"`
- `"Fast Food Tycoon" GameASG benchmark target prompt`

| 查閱來源／項目 | 取得的證據與判斷 | 關聯紀錄 | 重查條件 |
|---|---|---|---|
| [GameDevBench 官方頁](https://waynechi.com/gamedevbench/) | 官方頁已有 GPT-6.1 Sol xhigh/Codex 69.97% ±4.9 與 GPT-6 Astra high/Codex 68.8% ±5.0，333 項任務，每模型列最高多模態 feedback 配置的 pass@1。任務是在既有 Godot 專案內處理 shader、sprite、animation、scene、UI 或玩法改動，約 20% gameplay、27% 3D graphics，並非由空資料夾生成完整遊戲。資料屬新版 frontier agent 能力線索，不可當完整遊戲交付能力排名；S26 已收錄相同當前分數，未重複改寫成新成果。 | [B0012](../records/B0012.md) | 新增空白起始完整遊戲 track，或發布模型 artifacts／更細 task outputs 時再重核。 |
| [GameASG-Bench 官方 repo](https://github.com/areal-project/GameASG-Bench)；[2026-09-18 論文](https://arxiv.org/abs/2609.21293) | 官方 repository 有 47 個 browser-native 題（12 類、32 個 2D／15 個 3D）、每題的 target/game-spec/TDD、L1 靜態檢查、L2 Chromium 行為測試和生成／隔離評測 runner。generation container 只收任務文件、不收測試及過往結果；agent 單次產出 `index.html`，再由隔離 evaluator 測試。論文中最高嚴格成功率為 GPT-6 Astra + Codex CLI 26/47（55.3%），平均 L2 通過率 93.2%；這些是每題必要條件全過的指標，且不是 GPT-6.1 Sol 最新結果。此協定精確測「一次任務後自行用工具建置，再以外部驗收」，可換當前模型重跑。 | [B0010](../records/B0010.md) | 新 frontiers 透過官方 runner 發布 run artifacts／模型結果時更新。 |
| [Fast Food Tycoon 初始任務](https://github.com/areal-project/GameASG-Bench/blob/main/task/fast-food-tycoon/target.md)、[完整 GDD](https://github.com/areal-project/GameASG-Bench/blob/main/task/fast-food-tycoon/game-spec.md)、[TDD](https://github.com/areal-project/GameASG-Bench/blob/main/task/fast-food-tycoon/tdd.md) | 任務只有一個 `target.md` 作為 agent 初始任務，要求交付單頁 playable game；模型可自行使用工具與階段式迭代，不需使用者補充。GDD 規格把 3D 斜俯視餐廳的生產、食物搬運、顧客排隊、服務點庫存、收款、招募與地塊解鎖串成經濟閉環；也列出雇員 AI、清潔、drive-through、自助、rush、save/offline gains、vault/prestige。TDD 用真實玩家輸入及 state snapshot 查操作、資源守恆、相機旋轉後方向、可見回饋、非法操作拒絕和長期成長；公開測試 API 不可直接替遊戲完成核心行動。屬於高系統密度 3D 經營題，不只抽象小型點子。 | [G0056](../records/G0056.md)、[B0010](../records/B0010.md) | 若釋出更多模型 build／美術輸出或無介入 run trace，新增結果和使用者美術判定；目前只有任務／評測，不要推測視覺品質。 |
| [GameXpert-Bench 官方 repo](https://github.com/Kwen-Chen/GameXpert-Bench)；[官方 project page](https://github.com/Kwen-Chen/GameXpert-Bench/blob/main/docs/index.html)；[論文](https://arxiv.org/abs/2608.21833) | 論文主張 GameGen 有 97 個 single-request、empty-workspace 遊戲生成題，另有 GameFix 與 GameOpt。但本次官方 repo README 仍寫「public-release scaffold」，paper/data/evaluation code/model artifacts 會陸續補；官方網站 Paper/Code/Dataset 仍是 Coming soon。故它仍不能直接下載重跑。 | [B0017](../records/B0017.md) | 任務集、rubric、runner 或生成 artifacts 實際出現在官方 repo 時再重核。 |
| [GameCraft-Bench 官方 leaderboard](https://tongxuluo.github.io/gamecraft-bench-website/) | 目前榜單 GPT-5.6 Sol、Claude Opus 5、Fable 5 等，最早公開結果日期至 2026-07，沒有 GPT-6.1 Sol/Astra。雖有 140 個 Godot 任務與高密度任務規格，最新模型比較需要重跑；本輪未找到較 S24 新的 model artifact／分數。 | [B0011](../records/B0011.md) | 加入新模型結果，或公布其空白 workspace、長時 agentic 生成 run。 |

### 《Fast Food Tycoon》的候選判斷

相較舊台帳的簡略描述，本輪核到的任務文件把關鍵系統和行為 oracle 寫得很清楚：

- **開局到收入閉環：**移動至廚房製作食物、把食物送進服務庫存、滿足顧客、產生現金，再走到現金堆收款。
- **資源與操作一致性：**食物容量、服務庫存上限、資金非負、購買扣款、解鎖、員工狀態、相機旋轉後的螢幕方向及 UI 關閉後可繼續操作，都有明確觀察條件和拒絕規則。
- **長程深度：**擴張店面、雇員自動化、服務分支、save/offline 收益和 prestige 讓遊戲不會停在單一短循環。
- **可重現性：**基準預設 3,600 秒；正式模型 run 仍須記錄模型、effort、Codex/Claude harness 和當前版本。若比較一般消費者工具而不沿用其單頁/API 限制，需複製 GDD 的玩家規格而把公開 `window.__gameTest` API 留在隱藏評測層，避免測試接線本身混淆遊戲品質。
- **未解缺口：**沒有任何目前可看的 AI 生成成品、截圖／影片或模型最新 run。規格只要求可讀 3D 場景，沒有明確藝術風格，因此不能因任務難度高便說美術可能合格；必須先看新模型 build。

結論：把 G0056 從「因與 Airship Trader 相似而低優先」改為**高系統密度商業模擬重跑題／副主測**。它與 Airship Trader 的經濟題材雖相近，但核心驗收方式不同：此題同時測 3D 可控角色、空間路線、搬運／顧客服務、NPC 工作狀態、資源守恆、外觀可見變化及自動化，而非以交易規劃為主。它足以測系統整合，但不是已生成遊戲成果或使用者美術驗收通過。

## 更新去向與待查

- 擴寫 [G0056 Fast Food Tycoon](../records/G0056.md)，列為商業模擬重跑題並保留美術未核實界線。
- 更新 [B0010 GameASG-Bench](../records/B0010.md) 指向該題及本批；重核 [B0017 GameXpert-Bench](../records/B0017.md) 未發布狀態。
- 追加精選摘要的題型建議，但不更新 HTML：本題尚無模型成品圖可看，且不取代現有主要推薦。
- GameDevBench 新版 frontier roster 已在 S26 記錄；GameCraft 最新可公開的模型 run 仍舊；GameASG 沒有目前最新 Sol run；GameXpert 未釋出 task corpus。本輪無其他新正式 benchmark 成品候選。
- **下一方向：**搜尋其他正式／半正式發布的可重跑完整遊戲規格與自主工具軌跡，優先找已有高視覺成品和固定任務、或新 frontier 的 blank-start run；不要重複抽查已核對的 benchmark roster，除非官方有更新。
