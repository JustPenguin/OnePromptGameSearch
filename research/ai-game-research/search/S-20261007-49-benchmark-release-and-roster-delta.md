# 搜尋批次 S49：正式遊戲生成基準釋出及近期 roster 變化覆查

**日期／範圍：**2026-10-07；檢查 S44 後相關官方 repo 是否新增長規格任務包、評測器、runner、近期模型 run，並確認 A2Z、GameXpert、PlaytestArena、GameASG、GameCraft 的目前公開狀態。這批聚焦「最近一次官方釋出／commit 是否改變可重跑性或榜單」，不重做任務逐題篩選，也不把搜尋引擎摘要當證據。

## 研究問題與先前查重

先讀 [S44](S-20261007-44-formal-benchmark-artifact-and-roster-audit.md) 及 [B0002](../records/B0002.md)、[B0010](../records/B0010.md)、[B0011](../records/B0011.md)、[B0017](../records/B0017.md)、[B0032](../records/B0032.md)、[B0052](../records/B0052.md)。S44 已完成各基準的 task/evaluator 可用性盤點，本批只查官方 repo 的最新 commit 與現行 README／project page，確認是否出現可改變既有結論的新 artifact 或結果；不再重述基準規格本身。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `"A2Z GameSpec-Bench" dataset released code github October 2026`；官方 [GitHub API repo](https://api.github.com/repos/krafton-ai/a2z-gamespec-bench)、[commit API](https://api.github.com/repos/krafton-ai/a2z-gamespec-bench/commits?per_page=5)、[README](https://raw.githubusercontent.com/krafton-ai/a2z-gamespec-bench/main/README.md) | API 顯示最新 commit 仍為 2026-09-30（`c023786f`）；根目錄僅 `.gitignore`、LICENSE、README、assets。README badge 和 news 仍寫 code/data “coming soon”。沒有 GDD、contract、runner/evaluator 或新模型 run。 | [B0002](../records/B0002.md)、[B0052](../records/B0052.md) | 官方 repo 加入可下載 100 GDD／contracts／harness 或 frozen generation outputs 時，先確認授權與實際完整性。 |
| `"GameXpert-Bench" dataset released code 2026`；官方 [GitHub API repo](https://api.github.com/repos/Kwen-Chen/GameXpert-Bench)、[commit API](https://api.github.com/repos/Kwen-Chen/GameXpert-Bench/commits?per_page=5)、[README](https://raw.githubusercontent.com/Kwen-Chen/GameXpert-Bench/main/README.md) | 最新 commit 仍為 2026-08-22，root 只有 `.gitignore`、README、docs。README 說 repo 正準備公開，paper、benchmark data、evaluation code 和 model artifacts 會陸續加入；沒有本批可確認的新釋出。 | [B0017](../records/B0017.md) | 看到 task files、evaluation code 或模型輸出正式入 repo 再重查。 |
| `"PlaytestArena" prompts rubrics release github 2026`；[作者 repo](https://api.github.com/repos/RunRiotComeOn/gui-agents-for-continual-game-generation)、[README](https://raw.githubusercontent.com/RunRiotComeOn/gui-agents-for-continual-game-generation/main/README.md)、[官方網站](https://continual-game-generation.vercel.app/)、[v2 論文](https://arxiv.org/html/2605.28258v2) | repo 最新 commit 仍為 2026-05-27，README 定位為八款可玩 browser demo gallery。未見完整 200 prompts/rubrics、judge code 或 frozen multi-model generation set 新增；官方網站和論文方法參考不改變 S44 的可重跑判斷。 | [B0032](../records/B0032.md) | 完整題目／rubric／evaluator 或單次交辦協定釋出時重查；Play2Code 多輪人機互饋不能當 one-shot run。 |
| `site:github.com/areal-project/GameASG-Bench "GPT-6.1 Sol"`；官方 [repo API](https://api.github.com/repos/areal-project/GameASG-Bench)、[最新 README](https://raw.githubusercontent.com/areal-project/GameASG-Bench/main/README.md) | 精確 roster query 無模型 run 命中。最新 README 仍含公開任務、Docker runner、隔離式評測及可指定 model/harness 的命令；GitHub 最新 commit 仍為 2026-09-18 首次釋出 `6427cb65`。沒有 GPT-6.1 Sol / Sonnet 5.5 / Opus 5.5 新 run 或新 benchmark 版本。 | [B0010](../records/B0010.md)、[G0056](../records/G0056.md) | 有可查的 output、完整 model ID、任務覆蓋與時間戳的新 run 時新增實測個案；runner 可替換模型不代表已有 run。 |
| `GameCraft-Bench leaderboard 2026-10 GPT-6.1 Sol repo`；官方 [GitHub API repo](https://api.github.com/repos/FreedomIntelligence/gamecraft-bench)、[commit API](https://api.github.com/repos/FreedomIntelligence/gamecraft-bench/commits?per_page=5)、[README](https://raw.githubusercontent.com/FreedomIntelligence/gamecraft-bench/main/README.md)、[project page](https://tongxuluo.github.io/gamecraft-bench-website/) | 精確搜尋未找到 GPT-6.1 Sol run。最新模型表仍以 2026-07-31 DeepSeek-V4-Flash 為最近日期，榜首仍列 Opus 5 xhigh 68.44（2026-07-24）；README repo 最新 commit 為 2026-08-13 `a4334753`，project page 可訪問但沒有新 roster 證據。 | [B0011](../records/B0011.md)、[G0014](../records/G0014.md) | 新模型出現在官方完整榜表或結果 artifact 時，記錄其日期、coverage、提交與 evaluator 版本，並查摘要分數與逐列數字是否一致。 |

## 結論與更新去向

- 五組來源均沒有新正式 task release 或最新模型 run，也沒有比 S44 更強的可核實證據；A2Z／GameXpert／PlaytestArena 的公開資料缺口未解，GameASG／GameCraft 仍可重跑而缺近期公開成績。
- 本批無新候選、無顯著證據補強，屬 G0077 證據增補後第二個無增益搜尋方向（S48=1，S49=2，至少還需一個不同方向）。未另建重複項目或改動推薦排序；S44 已保存完整基準內容，這批記錄官方現況差異與重查條件。
- 下一個方向不沿用 benchmark repo roster 查法：查近期公開原始碼／遊戲作品庫中，具完整 playable build 的高系統遊戲，優先針對最新 coding model 官方或作者級 artifact，確認初始任務、首版時間線、是否有 follow-up、build/source 與可重現 QA 證據。先以既有索引查重，避免重查 S36–S42 已有項目。
