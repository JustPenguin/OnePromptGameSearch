# 搜尋批次 S-20261006-06：一次交辦基準與最新模型實測核對

**日期：**2026-10-06（台北時間）  
**問題：**最近公開的遊戲生成 benchmark 是否已有更接近「一次委託、途中不介入、AI 自測修正、最後驗收」的協定與實際 build？是否有足夠深度的新成品可列候選？

## 開始前查重

先讀研究根索引、候選摘要、搜尋批次索引及 S-20261006-05。確認 Kart Blitz 的 Nathan Onn Max run 和原 Reddit High run 已分開記錄於 G0080/G0165；SWE-Game（B0038）、GameXpert-Bench（B0017）及 GameDevBench（相關基準紀錄）都已列入目錄，舊批次要求只有新模型 run、釋出資料或評估器更新時才重查。故本批只核對可見網頁上新增／更新的協定、榜單和 run 證據，不重做一般 showcase 搜尋。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `2026 AI agent built complete game autonomous one prompt playable game benchmark Claude GPT game October 2026`；`2026 AI generated game long-running coding agent game playable artifact no human intervention benchmark`；`AI game development agent leaderboard benchmark game creation 2026 agent generated playable games`；`site:github.com "one prompt" "game" "Claude Opus 5.5" playable 2026` | 搜尋結果重遇已記錄的 Sonnet 5.5/Kart Blitz 與既有 benchmark。未發現可升級的新高複雜度 one-shot 成品。新有用線索是公開 Game Bench one-shot protocol 與近期 25-build 榜；Itsy Bitsy Spider 是單一爬牆生存循環，任務完整但明確為 small game，不符合上限題複雜度。 | [B0009](../records/B0009.md)、[G0080](../records/G0080.md)、[G0165](../records/G0165.md) | 如果增加更複雜 frozen brief、可直接遊玩新模型 build，或公布逐次 blind evaluation 原始表，再重查。 |
| [Game Bench frozen prompt](https://game-bench.piccini.app/frozen-prompt.md)、[leaderboard](https://game-bench.piccini.app/)、[GPT-6 Astra build](https://game-bench.piccini.app/games/gpt-6-astra-20260924/) | 直接核對凍結 prompt：清楚列一次交付、允許自測修正、完全瀏覽器通關測試和移動端要求；公開可玩的 Astra 2026-09-24 build。頁面列 25 runs、四軸權重 45/15/25/15，並披露部分分數使用 AI 評分／作者評閱。工具抓取不能讀 markdown 檔，但本機網路讀取確認 frozen prompt 全文可用。此題適合作流程與 rubric 參照，不是複雜度候選。 | [B0009](../records/B0009.md) | 有較複雜但同樣凍結、多模型、逐 run 可玩且零引導的題目時，再比較。 |
| `"GPT-6.1 Sol" game generated playable game one prompt 2026`；Agent Games [Crowd Rush](https://agentgames.dev/play/crowd-rush) | 直接複核早先記錄的 G0042：線上 v4.1.0 是 30 關、六區、路線分岔與持久升級的豐富 3D runner；但公開 prompt 是保留 campaign 後調整 boss fight 的 revision。沒有 blank-workspace 原始 prompt、全程使用者訊息、凍結首版或 no-follow-up 證據。將它從備選調為待核實，保留為高系統長流程參照，不列一次委託成績。 | [G0042](../records/G0042.md) | 找到最初 prompt、完整 user-message trace、首輪 build/hash 或作者的 no-follow-up 直接證據才重評。 |
| [Opus 5.5 one-prompt / one-hour 線索](https://www.reddit.com/r/ClaudeAI/comments/1wnzcbg/i_gave_opus_55_one_prompt_and_one_hour_to_make_a_game_then_actually_played_the_thing/)；[作者通關評論影片](https://youtu.be/56oLTK1Jseo)；[指定最新模型同題 blind test](https://www.reddit.com/r/ClaudeAI/comments/1wxfh4c/same_game_prompt_to_opus_55_sonnet_55_and_gpt61/) | 重查 Ink Field 的原貼／評論區後發現作者實際先要求模型提出遊戲構想、收到構想後再請它建置；雖未提供玩法方向，仍是第二則使用者指示，故從方法參考改列排除。只看到評論影片與作者文字，沒有 exact prompt、source 或 playable build；作者自評美術好、玩法無聊不當獨立品質結論。同日 Locust Arena 以一個「躲落下蝗蟲、支援手機」簡短 prompt 對照 Opus 5.5、Sonnet 5.5、GPT-6.1 Sol；作者稱每款一次、無重擲，但 GPT-6.1 首次達 usage limit，幾小時後才自行續跑。題目只有單一閃避 arcade loop，留言也認為適合加難機制；不符合上限深度。這是作者自製桌面程式的盲看投票，尚無固定 rubric、盲測結果或可重跑原文 beyond summarized prompt。 | [G0079](../records/G0079.md) | Ink Field 需原始 message trace／prompt 或 playable build 才有補查價值；Locust 只有加入有深度的題目並公開完整 rubric/attempt data 後才重查。 |
| [SWE-Game arXiv](https://arxiv.org/abs/2609.33678) | 2026-09-27 論文：41 款 executable Godot reference games、247 tasks、13 genres；construction / repair / port 共五類任務。brief-to-game 分項最高 50.38；提出引擎狀態／可重播輸入與視覺 rubric 組合。屬正式任務 benchmark，非任意完整遊戲 showcase。 | [B0038](../records/B0038.md) | 等官方資料／artifact 和 GPT-6.1、Sonnet 5.5 等當前型號新分數公開後重查。 |
| [GameDevBench leaderboard](https://waynechi.com/gamedevbench/)；`GameDevBench Leaderboard October 2026 GPT-6.1 Sol` | 官方頁 2026-10-01 更新：333 tasks，最佳多模態回饋配置與各模型最佳 harness；GPT-6.1 Sol xhigh 69.97% ±4.9、GPT-6 Astra high 68.8% ±5.0、Claude Fable 5 xhigh 67.3% ±5.0。不是純模型對比，也不是整款一-shot 成品對比；可作標準化 harness 和視覺回饋的最新校準資料。 | [B0038](../records/B0038.md)、[B0009](../records/B0009.md) | 模型版本或官方重跑榜單變化時更新，保留 effort、harness、視覺輸入和 confinement 條件。 |
| [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | 重核論文摘要：GameGen 是空 workspace 的 single request 生成 track；另有修復、多輪最佳化。作為方法線索已列 B0017；目前未找到本輪有新模型或可供玩家檢閱的新 build。 | [B0017](../records/B0017.md) | 只在任務集／結果更新，或新型號進入生成 track 時重查。 |

## 結論與更新去向

- 本輪未新增遊戲編號。更新既有 G0042 Crowd Rush 為高系統規模、一次委託證據待核實的遊戲；修訂 prompt 不能代替首次建置證據。G0079 Ink Field 因作者留言揭露實際有第二則「開始建置」指示，改列 strict one-shot 排除。最新 GPT-6.1 Sol/Opus 5.5/Sonnet 5.5 Locust 同題試跑有盲看，但題目過小，不升候選。
- 更新 B0009，把 Game Bench 由模糊「規模有限」補成可追溯的流程、精確題目、可玩 GPT-6 Astra build、評分方式及主測排除理由；更新 G0042 的狀態和來源證據。
- 更新 B0038，記錄 SWE-Game 新論文證據及 GameDevBench 最新公開模型／harness 成績。候選推薦未變，因此不改根目錄精選摘要與檢閱 HTML。
- 方法結論：使用者自訂上限測試應採 benchmark 的固定 prompt、空白工作區、零途中介入、AI 自主 QA；行為用可重播操作／狀態斷言，畫面與美術另行人評。Game Bench 的 spider prompt 不升主題，GameDevBench 分數不能混作單一遊戲作品分數。
- 下一輪改走公開實作 repo／session transcript／版本更新搜尋，聚焦最近三週的新模型高複雜度建置，避免重複本批的 benchmark 搜尋式。優先找尚未有穩定建檔的一次委託 run；對已收錄作品僅補原始 session、零介入、首份 build 或使用者美術驗收的直接證據。
