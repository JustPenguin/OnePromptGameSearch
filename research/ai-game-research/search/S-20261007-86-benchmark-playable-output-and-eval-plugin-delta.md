# 搜尋批次：正式遊戲基準的可玩輸出與評測工具釋出差異

**日期／範圍：**2026-10-07。沿 S85 下一方向，逐項核實 OpenGameEval 與 PlaytestArena／GUI Agents for Continual Game Generation 的近期釋出：有沒有新增可玩的完整遊戲成品、可對應的原始任務與模型版本、或可直接重跑的完整評分材料。這是第三個相對 S83 不同的無增益方向；不是重做 S47 搜尋。

## 實際查詢與查看來源

| query／來源 | 結果及檢視 | 納入／排除理由 |
|---|---|---|
| GitHub API `GET /repos/Roblox/open-game-eval/commits?per_page=8`；[repo commits](https://github.com/Roblox/open-game-eval/commits/main) | 最新 commit `8001cac2`（2026-10-05）只把論文連結與 citation 加到 README。前一項 `9070ee70`（2026-08-28）新增 Studio Eval Runner plugin；[使用手冊](https://github.com/Roblox/open-game-eval/blob/main/EvalPlugin/README.md) 說明作者在 Roblox Studio 建立 prompt、reference solution、edit-mode assertions 與 play-mode checks，再用 plugin 執行 checks。 | 是評測作者驗證自身 eval 的工具，不能當成新增遊戲生成 build、模型 run 或 benchmark 成績。只補充 B0050 的重跑／工具界線。 |
| [OpenGameEval README](https://github.com/Roblox/open-game-eval)、[官方 leaderboard](https://github.com/Roblox/open-game-eval/blob/main/LLM_LEADERBOARD.md)、S85 已查論文及 repo release tree | 現行 eval set／榜單仍是 Roblox Studio stateful modification/debugging 任務；多數從既有 place 開始，少量空場景任務也不要求交付完整遊戲。此次 commit 沒新增具名 playable output、完整空白專案任務或 GPT-6.1 Sol／GPT-6 Astra 實測。 | 不把既有場景修改分數外推為完整遊戲一次生成能力；無新強候選或新輸出證據。 |
| GitHub API `GET /repos/RunRiotComeOn/gui-agents-for-continual-game-generation/commits?per_page=5`；[PlaytestArena 官方 repo](https://github.com/RunRiotComeOn/gui-agents-for-continual-game-generation)、[論文](https://arxiv.org/abs/2605.21493) | repo 最近提交在 2026-05-27，更新首頁連結與八款 demo gallery 文案；未見新 release、task data 或 evaluator artifact。S81/S85 已核論文：PlaytestArena 有 200 個任務／1,548 checks 的研究描述，但可公開重跑的完整 prompts／rubrics／evaluator corpus 尚未對外釋出。 | 已有作品展示與可玩 demo 不等於可追溯的單次任務 output 對照。記為追蹤線索，不新增重複案例或強候選。 |
| S85 的 GameGo／A2Z／GameXpert release 查核紀錄及本批 GitHub API commit 列表 | S79/S76/S81 已分別記錄目前 benchmark outputs、data access 與 model/task 對照的缺口；本批沒有發現新 artifact release。 | 避免重複做基準 roster audit；保留不同於已完成 release delta 的「具名成品／prompt／run 一對一對照」作後續核查方向。 |

## 結果與計數

- 本方向沒有找到新強 one-shot 候選，也沒有顯著提升現有 case 的模型版本、原始任務、凍結 build 或 no-follow-up 證據。OpenGameEval plugin 提升 eval 作者測試便利性；PlaytestArena 仍有公開 demo 和論文任務數描述，但公開 artifact 未形成可核的一對一 run trace。
- S83 後第 3 個不同無增益方向：**3／至少 3**。依研究條件，這只完成最低數量，不代表其餘候選、近期生成案例和未查線索都已覆蓋，研究繼續。
- 下一方向：回到 G0289 Historical Flight 的 creator／organization 公開發布脈絡，尋找未在 contribution repo 公開的原始專案、建置任務／session 或同步發布的可信製作紀錄；若仍無資料，精確記下已查帳號與可追查窗口，不將 repo 的缺件誤寫成全網不存在。
<!-- record-meta: {"id":"S-20261007-86","type":"search","updated":"2026-10-07"} -->
