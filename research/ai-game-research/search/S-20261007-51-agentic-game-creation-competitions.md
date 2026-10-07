# 搜尋批次 S51：代理式遊戲創作競賽與 browser-game benchmark

**日期／範圍：**2026-10-07；查近期是否有面向 autonomous coding agents 的遊戲創作競賽／benchmark，能取得完整任務、生成後 playable artifact 與 agent 自主測試 trace。此方向與 S50 的單一作者多題 source collection 不同，聚焦公開賽制及可審查結果包。

## 研究問題與先前查重

重讀索引、候選摘要和搜尋索引。S30–S31 已查 AI Browser Game Jams，S43 已查 ProfIQ / One Shot Challenge，S48 已查 CoG 2026 competition 清單，S40 / S44 已查 WebGameBench、GameCraft、GameASG 等正式 benchmark。這批不重建這些項目，只查是否另有新競賽或新版本／artifact，並對查詢中的相鄰命中做範圍判斷。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `2026 AI game development agent benchmark coding competition browser games autonomous agent evaluation submission prompt game`；`2026 agentic coding game creation competition build playable game autonomous testing coding agents`；CoG [official competitions](https://cog2026.org/competitions) | 搜尋命中 CoG 2026 官方競賽總覽。實際檢閱頁面列的是 Planet Wars、Tales of Tribute、BotPrize、GDMC settlement、Codenames、DareFightingICE、Battlesnake、VGC、StarCraft AI 等既有遊戲對戰 agent 或內容競賽；沒有從使用者 brief 生成新 playable game 的 track。CoG 已在 S48 查過，這次只確認其範圍，不重複立項。 | [S48](S-20261007-48-public-blind-full-game-delivery-comparisons.md)、[E0009](../records/E0009.md) | 若公布「從新 prompt 生成遊戲」且保留模型／session／build 的競賽 track，再評估是否符合。 |
| `site:devpost.com "AI game" agent game generation challenge 2026 coding`；搜尋命中 [Agentic AI Innovation Challenge 2026](https://agentic-ai-innovation-2026.devpost.com/) | 官方頁對自動抓取回應 HTTP 403；公開搜尋摘要只說建 autonomous AI agents，沒有足夠可核規則證明它涉及完整遊戲生成。標為未確認線索，不納入或排除任何作品。 | — | 若頁面可讀或活動有可查 source/submission archive，再核題目、獎項與 artifacts。 |
| `"browser game" "coding agent" benchmark leaderboard generation task playable game 2026`；`"game generation" "agentic coding" benchmark prompt browser 2026 paper`；[OpenGame paper](https://arxiv.org/html/2604.18394v1) | 命中既有 OpenGame agentic coding platform。論文主張 agent 分階段規劃／生成及套用 Game Skill／Debug Skill，已在 B0029 記錄；本次沒有發現新的公開競賽 submission set 或 session artifacts，故不重複建立。它能提供 rerun harness，gallery 本身不足以證明每個項目的單次委託 provenance。 | [B0029](../records/B0029.md) | 新公開 benchmark run package 或同一 frozen task 下的 model output 時再更新。 |
| `"game generation benchmark" coding agent task benchmark 2026 games`；[WebGameBench paper](https://arxiv.org/html/2605.17637v1) | 命中既有 WebGameBench：browser-native game task、coding agent generation attempt 和 browser evaluator，已記於 B0043。查閲論文確認其評測流程貼近本研究，但不是新近競賽發布，也沒有本批找到的 GPT-6.1 Sol／Sonnet 5.5 新結果、full trajectory / frozen build release update。 | [B0043](../records/B0043.md) | 有新前沿模型 run、公開完整 task/evaluator 或其 agent trace 時更新。 |
| `"AI game jam" agent generated game prompt submission 2026 competition leaderboard`；`site:github.com "game generation benchmark" coding agent task benchmark 2026 games` | 搜尋結果未找到可確認的新型「coding agent 從 prompt 建立完整遊戲」競賽或可下載結果集；多數命中是既有遊戲的玩法 agent、遊戲 AI 作品集或未附任務／trace 的泛稱 benchmark。未以搜尋結果摘要為新候選。 | 已查 [E0001–E0002](../records/E0001.md)、[E0007](../records/E0007.md)、[B0029](../records/B0029.md)、[B0043](../records/B0043.md) | 有可核任務、agent protocol、結果 artifact 和作者／模型明確連結時才建項。 |

## 結論與更新去向

- 未發現新競賽、正式 task release 或新前沿模型可查 run；CoG 方向是既有遊戲玩法 agent，OpenGame／WebGameBench 均已入帳，Devpost 命中因 403 而保留為未確認線索。
- 本批無新強候選或顯著證據提升，是 S50 後第一個無增益方向（1／至少 3）。沒有新具名成品可建項；保留查詢、來源及 access blocker。下一步轉查近期公開的 developer conference／official model showcases 的端到端 playable game artifacts，且不再查競賽或相同 benchmark。
