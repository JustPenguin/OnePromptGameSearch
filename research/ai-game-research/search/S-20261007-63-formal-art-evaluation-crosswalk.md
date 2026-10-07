# 搜尋批次 S63：正式遊戲生成基準的美術評量與實際輸出

**日期／範圍：**2026-10-07；查正式 coding-agent 遊戲生成評測如何把畫面美術與功能視覺拆分、量表看什麼，以及公開的人類實玩／美術分數是否能證明近期高品質成品。避免重做 S45 逐題篩選與 S54 Game Bench 更新。

## 研究問題與先前查重

依 S62 所列下一方向，先重讀研究索引、候選摘要、搜尋索引及 [B0011 GameCraft](../records/B0011.md)、[B0009 Game Bench](../records/B0009.md)、[B0029 OpenGame](../records/B0029.md)、[G0262 Garden Keeper](../records/G0262.md)。既有 GameCraft 研究已收錄 Seele02-pro Garden Keeper art 85.04、Opus-4.7 對照與實玩影片；Game Bench 已記錄四軸 score 和盲玩流程但沒有公開盲評結果。故這次只補 rubric 操作定義／偏差與目前使用限制，不重複挑遊戲或另立既有案例。

## 實際搜尋與查閱

| 實際 query／來源 | 結果與證據 | 關聯紀錄 | 判斷／後續 |
|---|---|---|---|
| DuckDuckGo HTML：`game generation benchmark human evaluation visual quality aesthetics playable games rubric art presentation 2025 2026`；`AI generated games benchmark art score human ratings gameplay visuals video game generation benchmark visual quality`；`"Art and Presentation" game generation benchmark gamecraft human evaluation`；`game generation benchmark judge visual quality aesthetics user study playable game outputs` | 搜尋命中 GameCraft-Bench、OpenGame-Bench、Game Bench、Playable Game Generation 等既有基準；未找到公開的新一輪前沿模型高美術分數 playable build 或已發布的人類盲評結果。 | B0011、B0009、B0029、G0262 | 沒有新 build、題目或獨立 user ratings；區分既有量表的適用範圍。|
| [GameCraft-Bench 研究論文](https://arxiv.org/html/2606.17861)與官方 [Garden Keeper rubric JSON](https://github.com/FreedomIntelligence/gamecraft-bench/blob/main/tasks/tycoon-garden-ecosystem-keeper/tests/rubric.json) | rubric 明確分「Functional Visuals」和「Presentation & Art」：前者測 UI／狀態可讀、操作後有可見回饋、狀態變化可辨；A1–A4 看整體風格一致、資產／物種輪廓、場景構圖和選單／結果畫面的產品一致性。另一方面，該題 rubric 對程序幾何、純色塊或未貼圖模型設 art 子項 0.5 上限。 | 更新 [G0262](../records/G0262.md) | 這能診斷 gameplay readability 與美術 presentation 的不同，但資產管線上限是 benchmark 自訂評分規則，不可照搬為使用者美術判定。既有 art85.04 仍僅是待直接看的相對樣本，沒有新增人類評價。|
| [Game Bench 官方榜與 protocol](https://game-bench.piccini.app/)及[匿名盲玩頁](https://game-bench.piccini.app/blind-tests/) | 官方榜目前仍列 25 playable runs、Gameplay／Adherence／Engineering／Art 四軸；匿名試玩流程可讓玩家先玩再回饋。頁面沒有公開已完成盲玩數量、原始回答或彙總，也沒有可核的新 3D 大型遊戲 run。 | B0009、G0266 | Art 子分是作者／評分者資料，不能替代這位使用者的美術評價；盲玩介面只證明可評，不代表已有玩家結果。|
| [OpenGame 官方 repo](https://github.com/leigest519/OpenGame)；[Playable Game Generation 論文](https://arxiv.org/abs/2412.00887) | OpenGame README 稱其 VLM judge 的 Visual Usability、Build Health、Intent Alignment 對 150 prompts 評分；可見範圍偏能否理解、操作與符合意圖，且其完整 benchmark evaluator 是否公開仍依 B0029 已記限制。Playable Game Generation 研究涵蓋畫面品質與互動機制的生成／評估，但其任務設定不是一般 coding agent 接收一份高系統遊戲委託後交付完整作品。 | [B0029](../records/B0029.md)；排除為不相同任務的鄰接基準 | Visual Usability 不等同高美術完成度；不把 video／asset generation score 充作完整遊戲成品證據。|

## 結論與更新去向

- 沒有找到可新增的近期前沿模型強案例，也沒有取得新的人類美術／盲玩分數；S54 後第 **9** 個不同無增益方向。
- 美術評估上較可用的拆分是：功能視覺看玩家是否讀得懂狀態與回饋；美術／呈現看風格一致、角色／環境設計、構圖、材質光照和整套 UI／選單品質。不要把兩者合成「畫面分」後遮住差異。
- 新補充 G0262：GameCraft 的程序形狀低分上限反映該 benchmark 偏好 authored assets；使用者評美術應按實際畫面，不應按其資產來源規定扣分。作者／benchmark art score 仍非使用者評價。
- S64 應改查近期模型透過 AI image／3D asset 工具製作、並整合至可玩遊戲的真實工作流和 frozen build；要核對途中輸入是否有使用者追加內容，且沿用此批功能視覺／美術分開評分。研究仍持續，尚有 S56 CSDN 原文 URL 與 G0269 session 證據未解。
