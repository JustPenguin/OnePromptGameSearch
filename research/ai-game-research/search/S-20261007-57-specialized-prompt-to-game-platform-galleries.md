# 搜尋批次 S57：專用 prompt-to-game 產品、作品庫與成品來源

**日期／範圍：**2026-10-07；查 Rosebud、Astrocade、GDevelop、Ludo.ai 等遊戲專用生成／建置產品及公開 gallery。與 S55 的通用 coding-agent SaaS showcase 分開；本批重點是產品是否能給出可核的具名一次任務與實際成品 provenance。

## 研究問題與查重

開始前重讀 `ai-game-one-shot-index.md`、`ai-game-one-shot-candidates.md`、`search/index.md`；查 Bash Fighter 與 Night Patrol 以外的新增近期可玩證據。使用 `manage.py lookup` 檢查 Rosebud、Astrocade、GDevelop、Ludo，均無既有平台紀錄。既有資料庫已有多項專用遊戲平台／agent 研究，但沒有本批四個名稱命中。平台能力宣傳或 gallery 名稱不能代替逐個遊戲的原始 task、版本及人工介入證據。

## 實際搜尋與查閱

| 實際 query／來源 | 查核結果與判斷 | 關聯紀錄 | 後續／重查條件 |
|---|---|---|---|
| DuckDuckGo HTML：`AI game generator platform gallery Rosebud AI games prompt generated playable 2026 source`；[Rosebud AI Game Creator](https://rosebud.ai/ai-game-creator)；[Rosebud AI Game Generator](https://lab.rosebud.ai/ai-game-generator) | 兩官方頁 HTTP 200。creator 頁介紹以文字描述產生 2D／3D／voxel playable game，接著 browser playtest、聊天迭代及發布；頁面成功案例是產品宣傳，沒有具名 run 的凍結原始 prompt、模型版本／session、人工介入界線或 hash。產品允許並直接鼓勵迭代，不能從 playable gallery 倒推 one-shot。| — | 若某一個具名作品公開 generation history、首版與 frozen build，另建作品紀錄。|
| DuckDuckGo HTML：`Astrocade AI generated games public games gallery prompt game creation 2026`；[Astrocade 2.0 official announcement](https://www.astrocade.com/blog/astrocade-2-worlds-first-agentic-ai-game-creation-platform)；[Astrocade Game Gallery](https://astrocade.homes/) | 官網與 gallery HTTP 200。公告說明專用 AI 遊戲創作產品內部使用一組各司視覺、UI、gameplay／feel 的 agent；提供依作品變化的 editor，並鼓勵 remix。gallery 是大量社群 playable games，但查不到可逐款對應到一個初始 user task、agent/model/session 與無後續使用者指示的 trace。平台使用多代理不等於它的任一成品符合本研究一次委託規則。| — | 遇到公開 generation history、可辨 build hash、task 與 run boundary 的具名高系統作品時再核。|
| DuckDuckGo HTML：`GDevelop AI agent generated game public example game from one prompt`；[GDevelop AI Agent 公告](https://gdevelop.io/blog/make-games-with-ai-agent-gdevelop-automated-prompt)；[GDevelop AI docs](https://wiki.gdevelop.io/gdevelop5/interface/ai/)；[itch.io GDevelop／AI Generated 標籤](https://itch.io/games/newest/free/made-with-gdevelop/tag-ai-generated) | 官方頁 HTTP 200。公告將 agent 定位為建立 gameplay features、menu、score 或 effects 的遊戲開發助手，說明可以即時測試後反覆迭代；AI docs 同樣是既有 GDevelop editor 的協作功能，不是凍結完整遊戲 generation benchmark。itch.io 標籤頁 HTTP 403，本輪無法逐款檢視；即使可見，tag 也不能證明任務／版本／介入條件。未新增作品。| — | 若 tag page 可讀且有明確 one-shot task／source，再逐項核對；目前只記存取阻礙。|
| DuckDuckGo HTML：`Ludo AI game generator playable game generated from prompt showcase`；[Ludo.ai features](https://ludo.ai/features)；DuckDuckGo 另命中 Ludo Playable Generator demo video | 官方 feature page HTTP 200；其自我定位為遊戲創意、設計研究與 sprite／2D／3D／audio/video 素材生成工具，未見交付完整遊戲 source/build 的具名 run；影片是工具展示，不提供任務文字、模型版本、保存成品或 session。故按範圍排除成品候選。| — | 若之後出現可玩的完整遊戲 generator 與具名 run，再按個案 provenance 查。|
| DuckDuckGo HTML：`site:rosebud.ai/game RPG AI generated game playable showcase`；`site:astrocade.homes/game RPG AI generated game playable`；`site:astrocade.com/blog game built created with AI prompt playable game example` | 三個精確 site query 無結果；不將上批官方 gallery 描述誤寫為查到特定遊戲的 task artifact。| — | 新公開 indexed artifact 命中時查 task/model/build/version。|
| DuckDuckGo HTML：`Rosebud AI game builder generated full game prompt first attempt game showcase`；[Rosebud tutorial](https://rosebud.ai/tutorial) | 教學定位為使用平台建置／發布作品，無指定高系統作品的一次 run、模型/session 及凍結成果，排除成績證據。| — | — |

## 結論與更新去向

- 本方向沒有帶來新強 one-shot 候選或對現有案例的顯著證據補強；S54 後無增益方向累計 **3／至少 3**（S55、S56、S57）。
- 目前仍有兩項具名線索值得做一次針對性公開來源覆查：Bash Fighter 缺 AI agent 到 commit／run 歷史；Night Patrol 缺最初 prompt、Codex 版本及原型到多輪最終版的逐次時間線。下一批先重讀三份索引，查原作者公開帖、repo release／commit、文件與可索引 archive，不重做本批平台搜尋。若原始 run 記錄不公開，就把精確缺口寫清楚，不將聯絡作者或猜測當成已核證據。
