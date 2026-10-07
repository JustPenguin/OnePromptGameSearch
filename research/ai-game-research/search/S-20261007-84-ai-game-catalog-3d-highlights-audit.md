# 搜尋批次：AI 遊戲目錄近期高評分 3D 條目與原始提交核查

**日期／範圍：**2026-10-07。從 Hugging Face `Games made with AI` 2026-10-03 snapshot 抽查近期可玩、Three.js、catalog rating ≥4.5 的 3D 遊戲；回到目錄遊戲頁、creator submission issue 和原始可玩頁核實遊戲範圍、模型／工具申報及人類介入。此方向不同於 S80 curated GPT-6 Astra gallery，且不把資料集星等當成研究評分。

## 實際查詢與查看來源

| query／來源 | 實際結果 | 納入／排除理由 |
|---|---|---|
| Hugging Face datasets API `GET /api/datasets?search=game%20generation&limit=100`、`...?search=game%20benchmark&limit=100`、`...?search=AI%20games&limit=100` | `games-made-with-ai` 為相關且更新於 2026-10-03 的公開 snapshot。下載並查看 `README.md`、`games.json`、`games.csv`；JSON 列 536 games，資料由 GamesByAI 整理，AI 工具／模型來源為 creator statement。`LKForge/game-ai-vs-llm-benchmark` 測 Tic-Tac-Toe／2048 的傳統 AI 與 stochastic LLM-sim，非生成遊戲；其他返回項是 AI 玩遊戲／談判資料集，不符合範圍。 | 更新既有 [C0013](../records/C0013.md) 作 discovery catalog；不是生成能力 benchmark。 |
| dataset filter: `engine in {threejs,babylonjs,unity,unreal,godot}`, added ≥2026-09-01, rating mean ≥4.5；[JellyBlob directory page](https://gamesbyai.win/games/jellyblob/) 與 [live build](https://jellyblob.win) | Dataset row 記 GPT-6 Astra／Claude Opus 5.5、Codex／Claude Code、Three.js、multiplayer。頁面可直接看 browser build 和兩張 gameplay screenshot，creator statement 稱 AI 寫全部 code，起始是 GPT-6 Astra，後由 Opus 5.5 remake，過程有「hundreds of iterations from my input and instructions」。 | 有當前 3D 成品／畫面參照，但明確有人類數百次指示與迭代，排除 strict one-shot。兩個模型和版本不是一個 frozen run。 |
| [Rimehold GamesByAI page](https://gamesbyai.win/games/rimehold/)、[creator submission issue #54](https://github.com/gamesbyai/catalog/issues/54)、[itch.io playable page](https://malnourishd.itch.io/rimehold) | Issue 提交人申報 Claude Opus 5.5、Claude Sonnet 5.5、Claude Code、Three.js、all code AI；說「left all decisions to claude, yolo-d the whole thing referencing wc3 maps」。遊戲描述防守 frozen pass，40 waves／4 bosses；可玩 HTML build，頁面顯示 Rimehold banner。沒有原始 task/prompt、模型 run 對應、session、no-follow-up trace 或 gameplay capture。 | 題型可作 tower-defense 重跑靈感，但「留給 Claude 決定」不等於一次委託已核實；banner 是宣傳／title image，不能當作遊戲畫面或 3A 驗收證據。暫不新增獨立候選。 |
| [Sumo Boulders GamesByAI page](https://gamesbyai.win/games/sumo-boulders/)、[creator submission issue #94](https://github.com/gamesbyai/catalog/issues/94)、[live build](https://danger.academy/Sumo-Boulders/) | Issue 申報 Claude Code／Three.js、all code AI，但模型名稱空白，沒有 prompt／session／source。Creator 描述 8 個物理不同競技場、6 個 AI 個性、Ladder、Battle、boulder builder、P2P multiplayer 及 gamepad；directory 有 build。 | 玩法系統值得另行查，但證據不足以支持單次任務或視覺評級；不新增 case，避免用未核 creator claim 湊候選。 |
| GitHub repository search API: `"game generation" benchmark 3D`、`text to game benchmark playable` | 兩個精確 query 均回 zero repository results；因此改走可下載的 HF directory 與其原始 issue 提交。 | 零結果只記為該兩個 API query 的搜尋結果，不推論全網沒有案例。 |

## 結果與計數

- 沒有新增可核的一次委託強候選。JellyBlob 的數百次人類迭代已被 creator 明確披露；Rimehold／Sumo Boulders 是近期可玩題材線索，但只見申報，缺原始任務與 run trace。
- 更新 C0013，記錄 536-entry snapshot 和代表性抽查結果；不把 directory star、creator submission、promotional art 當作性能／美術評測。暫不為上述排除案例建立個別 G record。
- S83 後第 1 個不同無增益方向：**1／至少 3**。本輪未找到新的強候選或可顯著提升現有案例之 one-shot 證據。
- 下一方向：沿此目錄之外查 2026 Q3/Q4 可核的獨立生成 evaluation protocol／video benchmark release，特別找具 raw gameplay recording、模型版本、任務文本、judge rubric 的實際 3D outputs；不重複 S81 的官方 benchmark release roster，也不重複 S84 的 curated game directory。
