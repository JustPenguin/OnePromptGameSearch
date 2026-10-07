# 搜尋批次 S46：長時程自主完成遊戲的公開 run 與獨立證據

**查核日期：**2026-10-07（台北時間）  
**研究方向：**追查既有高上限任務與基準是否已出現「使用者只給一則任務、AI 自主多輪建置／測試／修正、最後留下遊戲成品」的實際長時程案例；核對案例的底模、工具、人類介入、真實遊戲畫面和可公開追溯材料。此輪延續 S45 的 frontier run 線索，但改查多日自主長程 run，不重複掃 GameASG／GameCraft 單題規格。

## 先讀索引與查重

已先讀 [研究索引](../../ai-game-one-shot-index.md)、[候選摘要](../../ai-game-one-shot-candidates.md)、[搜尋索引](index.md) 與 [S45](S-20261007-45-benchmark-task-screening.md)。用 Fusepoint、Harness-of-Harness、論文編號及 GitHub 作者／repo 關鍵字查既有 records、search batches、候選摘要和研究 log；沒有現存同名紀錄。已知 S40 有 HoH-adjacent benchmark/method leads、S45 查 GameCraft 結果，故本輪專注作者正式發布的 HoH 方法及 Fusepoint；不把 benchmark 45 題分數誤記成 Fusepoint 分數。

## 實際 query 與查閱來源

| 實際搜尋／來源 | 查得內容與判斷 | 入帳／待查 |
|---|---|---|
| Web query：`site:flesymeb.github.io/HarnessOfHarness Fusepoint model GPT-5.5 prompt PRD 70 iterations`；`site:arxiv.org/html/2609.01481 Fusepoint GPT-5.5 model PRD`；`site:github.com/Flesymeb/HarnessOfHarness Fusepoint commit model transcript`；`"Fusepoint" "GPT-5.5" game` | 搜尋詞以 GPT-5.5 起查，但官方論文區分：主 benchmark 的一組是 GPT-5.5；Fusepoint 長程 case 的底模其實是 GPT-5.6-Sol high。命中 HoH 官方專案頁與 arXiv 正式論文。 | 新增 [G0263 Fusepoint](../records/G0263.md) 與 [M0028 HoH 方法](../records/M0028.md)。保留精確的型號更正，避免把受控 3-loop benchmark roster 和 70-loop Fusepoint roster 混淆。 |
| 官方研究：[HoH project page](https://flesymeb.github.io/HarnessOfHarness/)；[arXiv paper](https://arxiv.org/html/2609.01481)，特別核對 §§ 5.1–5.2、Appendix B | 論文明載空工作區只有使用者 PRD；五分鐘單人拆彈 FPS、兩個依序據點、三階段炸彈、3／5／10 配置的 18 敵人、兩種結局；Codex CLI＋GPT-5.6-Sol high；70 輪；人類只在網路/API 可用性問題時介入。工具含 Godot 4.7、Godot MCP、外部合法再利用素材、asset/UI/UX/testing skills。測 live keyboard response、audio 和 3D asset integration。 | 一次使用者任務＋無內容性人類介入的證據很強，契合本研究的自主自修定義。完整原始 PRD、精確 wall-clock／token、Fusepoint 專屬 rubric score 沒在讀到的論文內容中找到。 |
| [官方 Fusepoint gameplay video](https://flesymeb.github.io/HarnessOfHarness/assets/video/fusepoint-real-gameplay-preview.mp4)、[官方 playable game download folder](https://drive.google.com/drive/folders/1gch3D5HKa3n3gxM0LNrzubcJxlFFLaXy?usp=sharing)、[官方 project source repo](https://github.com/Flesymeb/fusepoint) | 有真實遊戲錄影、下載入口與可追溯 source repo。paper 在 Loop 70 記錄 81 issues 中 65 關閉、16 未解、17 回歸重開；聲稱 human-playable，但非無缺陷。公開主分支後來已到 Loop 96，README 顯示 101 issues 中 94 關閉、7 開啟；最新循環也列出仍未解 QA 缺口。Repo API 顯示 default branch `gameloop`，更新日 2026-09-22。 | 納入長時程成品案例；不把 Loop 96 後續主分支冒充 Loop 70 凍結成品。尚未找到 Loop 70 immutable tag / frozen build；paper 的 70-loop version 與目前 repo 演化版須分開標明。使用者美術未評價。 |
| GitHub tree / raw README：`https://api.github.com/repos/Flesymeb/fusepoint/git/trees/gameloop?recursive=1`；`https://raw.githubusercontent.com/Flesymeb/fusepoint/gameloop/README.md`；project page HTML；官方 HoH repo | 掃描公開樹及 README，找到 `.gameloop` 多輪 receipt／event 檔和最新 Loop 96 摘要、Godot game source、官方 mp4／poster；未找到命名清楚的原 PRD 檔。Paper 說匿名 benchmark reproducibility package 不含 raw run artifacts，但 Fusepoint repo 另保留 selected development records。 | PRD exact wording 和完整私有 runtime audit 不宣稱已公開。可從視頻、README、issue history、commit history檢驗部分聲稱，不能復刻原始條件的所有細節。 |
| 補充 Web queries：`site:github.com/Flesymeb/fusepoint "PRD"`；`site:github.com/Flesymeb/fusepoint "Loop 70" issue evidence`；`site:github.com/Flesymeb/fusepoint "GPT-5.6-Sol"`；`"Harness-of-Harness" Fusepoint screenshot download Godot 4.7` | 公開 search indexing 沒直接索引到 PRD 正文；透過官方論文正文才核實底模為 GPT-5.6-Sol、high effort、70 循環與工具界線。 | PRD 原文與 exact 70-loop build 保持未核實；若日後 Drive 釋出固定版本、PRD 或 hash，更新 G0263。 |

## 納入判斷

Fusepoint 是本輪找到的**強長程自主實作候選**：一個初始 PRD、後續無人類內容介入、由 AI 跨 70 輪規劃／建置／QA、自行處理回歸問題，且有遊戲輸出、遊戲下載入口和開源歷程可供檢查。它可直接改善研究對「使用者退出、AI 自主修正」的候選範圍，不只是題型線索。

但它不是最新模型對照：Fusepoint 用 GPT-5.6-Sol，且不是單次模型呼叫；原始 PRD 和 70 輪凍結 build 尚缺。論文 cutoff 仍有 16 個 issue 未解；主 repo 後來走到 Loop 96 仍有開啟缺口，且與 70-loop candidate 版本關係未完全鎖定。故列強參照／新模型重跑題，不把研究團隊自述成品完成度當作獨立通關分數或使用者美術驗收。

HoH 的 45-task GameCraft-Bench 實驗用 Codex + GPT-5.5、OpenCode + DeepSeek-V4-Pro、Pi + MiniMax-M3，對照 vanilla 和三個循環；這是方法控制實驗，不是 Fusepoint 的多模型 run。新增 [M0028](../records/M0028.md) 記錄其可用方法資訊與複現限制。

## 下一個明確搜尋方向

轉查**研究機構／官方 coding agent showcase 的最新完整長程遊戲案例**：優先 GPT-6.1 Sol、Claude Sonnet 5.5／Opus 5.5、Gemini 3.8 等最新可用模型的單一初始任務後 autonomous game project；要求有明確底模、是否無人介入、可看成品影片/build 及規格／run evidence。對 Fusepoint 類舊案例，只補查固定 PRD、frozen 70-loop build、精確成本／耗時，不重複已取得的 70／96 loops 摘要。
