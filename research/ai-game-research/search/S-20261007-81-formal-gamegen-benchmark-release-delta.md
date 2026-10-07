# 搜尋批次：正式遊戲生成 benchmark 的近期 release／新模型輸出覆查

**日期／範圍：**2026-10-07。跨主要正式 benchmark 核對近期公開 release、leaderboard 新模型、可玩 build／輸出、完整任務與評測材料是否有更新。此方向與 S79 單獨調查 GameGo corpus 不同：這輪橫查 GameGo、A2Z、GameASG、GameCraft、GameDevBench 的官方入口，目標找 S79 後的新 release delta 或具足夠一次委託證據的新近期實物。開始前重讀研究索引、候選摘要、搜尋索引，並查重五個基準的固定編號 B0058、B0052、B0010、B0009、B0012。

## 實際查詢與查閱

| query／來源 | 結果與證據 | 判斷與後續 |
|---|---|---|
| Web query：`AI game generation benchmark 2026 latest model playable outputs dataset release`; `site:github.com game generation benchmark release 2026 game agent tasks`; `Game generation benchmark game artifact model leaderboard October 2026` | 命中上述正式基準和非一手 benchmark 彙整頁。只採用 official repository、paper、leaderboard、dataset API；不以聚合站摘要當 release 證據。 | 橫向逐項核對官方 upstream、release list、最新 commit 和可取素材。 |
| [GameGo repo](https://github.com/Haoyue-Yang/GameGo)、[README](https://github.com/Haoyue-Yang/GameGo/blob/main/README.md)、[published gallery](https://haoyue-yang.github.io/GameGo/games/)、[HF dataset](https://huggingface.co/datasets/Y36521478Y/GameGo) | GitHub API default branch main 最後 push 2026-10-02，無 GitHub release；仍有 12 個 GameGoCoder 3.8 成功子集 playable/sample，README 說 124 held-out tasks 和 55,060 trajectories，但 raw query corpus／trajectory 不在該 repo。HF dataset anonymous API 仍回 401。相較 S79，本輪未看到新的 corpus/build release。 | B0058 原記錄已充分涵蓋；無新個案或 significant evidence delta。 |
| [A2Z official repo](https://github.com/krafton-ai/a2z-gamespec-bench)、[README](https://github.com/krafton-ai/a2z-gamespec-bench/blob/main/README.md)、[HF dataset](https://huggingface.co/datasets/KRAFTON/A2Z-GameSpec-Bench)、[leaderboard/method page](https://a2z-gamespec-bench.github.io/at-a-glance.html) | GitHub API 顯示最近一次有效內容提交為 2026-09-30 README/assets、無 releases；README 仍寫 code/data forthcoming。此前可見的 leaderboard 與三張 3D screenshot 狀態無本輪更新。 | B0052 仍是高價值題庫／輸出線索，但不能完整重跑或從 repo 取得原始 build；不重複增加 entries。 |
| [GameASG-Bench repo](https://github.com/areal-project/GameASG-Bench)、[paper](https://arxiv.org/html/2609.21293v1)、官方 task bundle | API 顯示 repo 最近更新 2026-09-18、無 release；47 tasks、單一 initial task bundle、fresh container、隱藏測試與官方 runner 已在 B0010／S45 記錄。沒有找到更新 roster 或新公開 frontier-model build。 | 題庫能重跑但無新成果；規格包內有 target/GDD/TDD，應精確稱任務 bundle，不能縮寫成只有一段純文字。 |
| [GameCraft repo](https://github.com/FreedomIntelligence/gamecraft-bench)、[paper/code gallery](https://tongxuluo.github.io/gamecraft-bench-website/)、task/rubric | API 顯示 repo 最近更新 2026-08-13、無 release；README 對公開 2D Godot tasks、hidden rubric、可玩 artifacts 的狀態與 S45/S63 相符。未找到新的 3D split 或最新模型 output。 | B0009/B0011 與 G0261/G0262 已涵蓋；其 2D 任務可作系統／評測重跑，不能代表 3D／3A 上限。 |
| [GameDevBench repo](https://github.com/waynchi/gamedevbench)、[official leaderboard](https://waynechi.com/gamedevbench/)、[README](https://github.com/waynchi/gamedevbench/blob/main/README.md)、[paper](https://arxiv.org/abs/2602.11103) | 最新 commit 2026-10-01 提供 GPT-6.1 Sol xhigh 69.97% ±4.9（榜首），GPT-6 Astra high 68.8% ±5.0；榜列 333 題 pass@1。已核分數與既存 B0012/S26 內容一致，沒有新完整遊戲成品或 benchmark 任務。其測試是修改既有 Godot 專案，不是空白專案生成。 | 保留作 current model coding-agent / multimodal methodology reference，不可將局部 feature-edit score 算作 complete-game one-shot 成績；本輪確認既有記錄無需改分。 |
| [arXiv query](https://export.arxiv.org/api/query?search_query=all:%22game%20generation%22%20AND%20all:benchmark&start=0&max_results=30) 與 GitHub release endpoint 查詢；`manage.py lookup` 核對上述名稱／別名 | 新近 paper hits 已由 S76 GameSpec、S79 GameGo 及既有正式基準紀錄涵蓋；官方 repo release endpoints 沒有比現行 entries 更新、又帶完整任務與新 playable output 的項目。 | 未發現值得新增的 benchmark 或強候選；排除搜尋聚合列表、缺 build 的 abstracts 及只改既有專案的 task score。 |

## 結果與計數

- 本批沒有新強候選，也沒有使現有案例的模型／任務／無介入／凍結輸出證據顯著提升的公開 release。
- 新模型最高的 GameDevBench 成績仍是既有專案局部修改；GameGo/A2Z corpus release 邊界仍未解除；GameASG/GameCraft 沒有本輪新增 roster／output。
- S79 後第二個不同無增益方向：**2／至少 3**。下一個方向查非 benchmark paper／curator catalog 的一手創作者公開任務或 coding-agent session，優先實際 3D gameplay build 與高品質視覺，使用與 S80 不同的直接作者／repo 搜尋路徑。
