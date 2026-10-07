# 搜尋批次 S65：近期 AI 遊戲 jam 的高視覺 build 與一次委託證據

**日期／範圍：**2026-10-07；查有新 roster、可玩輸出和明確 visual evaluation 的 2026 AI game jam，挑具名高視覺 build 核對內部 gameplay 畫面、AI attribution、是否一份使用者任務完成及人類美術介入。已看過 S30／S31 AI Browser Game Jam、S51 通用競賽及 S57 生成平台 gallery，不重做這些方向。

## 研究問題與查重

先讀研究索引、候選摘要、搜尋索引及 [E0005 Slapjam](../records/E0005.md)；歷史資料提過 Slapjam 48 小時 AI jam 和 Tiny Necromancer／Bastion／Chainmate，但未對照目前官方 #1 roster／評分規則。查資料庫沒有 `Aethel Fold`、`ASHEN RAMPART` 或 `Ultimate AI-Powered Game Jam #4` 紀錄。此批找 artwork 真實出現在 gameplay 的作品；jam 參賽和「AI-assisted」不會自動變成 one-shot 證據。

## 實際搜尋與查閱

| 實際 query／網址 | 查核與結果 | 關聯項目 | 判斷／重查條件 |
|---|---|---|---|
| DuckDuckGo：`2026 AI game jam playable games source repository AI generated art task prompt winners`；`2026 generative AI game art jam game playable source prompt submission`；`AI generated game showcase playable browser 2026 coding model visual art direction original source game`；`site:itch.io "AI-generated" game 2026 AI game jam playable`；`site:github.com AI game showcase playable visual assets 2026 game jam coding agent`；`one prompt game development AI game jam visual style playable output 2026` | 命中 Slapjam #1（與已存在 E0005 相同活動），2026 Ultimate AI-Powered Game Jam #4、新的 2026 AI Game Bundle jam、以及官方 AI game jam 作品；本批集中核 Slapjam #1 及有具名 art/gameplay evidence 的作品。沒有結果可證明 AI jam entries 普遍是一份使用者任務產物。 | 更新 E0005、新增 E0010 | jam-level AI tool use／48-hour human-directed project 與一次委託必須分開。|
| [Slapjam 官方頁](https://slapjam.ai/)；[itch jam 規則](https://itch.io/jam/slapjam-ai-1)；[142 entries 清單](https://itch.io/jam/slapjam-ai-1/entries)；[entries JSON](https://itch.io/jam/419724/entries.json)；[results path](https://itch.io/jam/slapjam-ai-1/results) | itch jam page 顯示 48 小時（2026-09-28 至 09-30）、手機直式 HTML5 browser game、允許 AI 生成 code／art／music／voices／3D；規則沒有單 prompt／無人追加的限制。itch 頁和 JSON 共列 142 entries；slapjam.ai 首頁說 Play all 145 games，有 3 款 count 差異。主辦者說評審實際玩每款，按 Fun、Visual Appeal、Theme Following 評分，結果於 Oct 7 公布；本次 `results` path 轉回 jam overview，未取得實際排名／評語／visual 分數。 | 更新 [E0005](../records/E0005.md) | event rubric 可用作人類實玩評美術的方法參照；沒有公開分項結果可證候選達標。jam 時間允許多輪人工引導，不能作 one-shot 成績。需要主辦方結果頁／score list 才能引用官方視覺排序。|
| [Aethel Fold 作者頁及 HTML5 build](https://konstantinsteinmiller.itch.io/aethel-fold)；兩張[實際 ravine gameplay 截圖](https://img.itch.zone/aW1hZ2UvNTA3MzYxNS8zMDQzOTg0MS5qcGc=/original/y37f1H.jpg)、[書頁／關卡畫面](https://img.itch.zone/aW1hZ2UvNTA3MzYxNS8zMDQzOTg0NC5qcGc=/original/O7LgZf.jpg)；[embedded build](https://html-classic.itch.zone/html/19486028/index.html?v=1790779752) | 作者 AI disclosure 明說完整遊戲由 Claude Code 在數個 cloud sessions 實作；人類提供 game design、art／sound direction；Claude Code 做遊戲內 art／sound／text；Gemini 做封面和頁面 art。頁面描述 3 冊、18 頁和摺紙操作，發布為 HTML5。研究者看了 gameplay screenshots：手繪繪本框架、暖紙色底、摺紙／低多邊形森林、清楚大 UI，畫風統一；作品是 stylized 2D，不是 3A 寫實，human art direction 明確。頁面稱 Published 7 days ago、Updated 5 days ago，當前版本未必等於 jam 截止凍結版。 | 新增 [G0274](../records/G0274.md)、E0005 | 值得留作 AI 遊戲內美術參照供使用者判定；多輪和人類設計／art direction、不見 prompt/session，故明確排除一次委託成績。使用者美術評價待定。|
| [ASHEN RAMPART 作者頁](https://haruka-apps-games.itch.io/ashen-rampart)；[jam entry roster](https://itch.io/jam/slapjam-ai-1/entries) | 3D dark-fantasy tower defense、作者頁標 AI Code／Graphics／Sounds／Text，宣稱 6 nights × 3 waves、四塔與 boss；entry/source page 未給原始 prompt、模型版本或 session。未取得獨立 hands-on／透明 artifact history，也未將 jam 中途版本與 itch 現版分開。 | Slapjam E0005 | 可在新任務取得 build history／source 後重查；本次不因宣稱功能和標籤列為 strong one-shot。|
| [Ultimate AI-Powered Game Jam #4](https://itch.io/jam/ultimate-ai-powered-game-jam-4)及[entries](https://itch.io/jam/ultimate-ai-powered-game-jam-4/entries) | 活動頁列 44 entries、2026-09-17 至 09-30，說明為 long-term edition、主題可選，鼓勵人類指揮 AI 工具做創意原型；無 one-user-task protocol。 | 新增 [E0010](../records/E0010.md) | 保存為 AI-assisted jam event／排除一次委託規格，不把未逐項審的 entries 當候選。|
| [AI Game Bundle 2026 jam](https://itch.io/jam/ai-game-jam-2026)及[Slapjam 2026 overview](https://slapjam.ai/) | 新 jam 入口／商品 bundle 提交集合，但頁面資料未提供每款的 single task、model/session、AI contribution freeze 或可比 visual rubric；Slapjam overview 已回到 E0005 同活動。 | E0005；不建新 game record | 無逐件一手任務證據；若有清楚 AI attribution＋playable build 的作品再做題目查核。|

## 結論與更新去向

- 從 142 個 itch entry（主辦首頁宣稱 145）未找到可稽核的一次委託賽制；48 小時 jam 明確容許參賽者使用 AI 製作任何素材，沒有初始 prompt／禁止 user follow-up 的規則。
- Slapjam 提供了實際 panel scoring protocol：Fun、Visual Appeal、Theme Following；本批未取到結果頁的評分／排名，不能稱某 entry 通過 Visual Appeal，也不能用 jam 參賽排名判定美術。
- Aethel Fold 新增為高質感 2D AI-assisted gameplay-art reference：Claude Code 多 sessions 產生遊戲內素材，人類主導 art direction；系統與畫風值得用來給使用者看，但不是一次委託成績，且官方頁已有 jam 結束後更新。其美術待使用者評價。
- 新增 E0010 保存另一個 44 entries 的 long-term AI game jam，規則同樣不符合一份 user task 且零追加要求。ASHEN RAMPART 是有 3D 標籤和功能自述的目標，但缺原始任務／模型／trace，未升強候選。
- S54 後第 **11** 個不同無新增強候選／無顯著 one-shot evidence 提升的方向。研究仍持續；下一批改查有可追溯作者 task/session、具 AI gameplay 美術的跨模型或 model showcase 的近期 build，避免泛搜 jam roster。
