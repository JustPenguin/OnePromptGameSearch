# 搜尋批次 S58：Bash Fighter 與 Night Patrol 公開 provenance 線索追查

**日期／範圍：**2026-10-07；只查既有 G0267、G0268 的作者原始貼文、repo commit／release 時間線及可讀轉載，尋找先前缺少的 initial task、model/session 與人類 follow-up 證據；不重做 S55–S57 平台／語言搜尋。

## 研究問題與查重

本批前先讀 `ai-game-one-shot-index.md`、`ai-game-one-shot-candidates.md`、`search/index.md`，並查重 `manage.py lookup 'Bash Fighter'`、`manage.py lookup 'Night Patrol'`；分別已有 G0267、G0268。關鍵問題是公開時間線能否把持續維護產品或由原型迭代成 release 的過程拆出一個可稽核、無使用者 follow-up 的單一成品 run。

## 實際搜尋與查閱

| 實際 query／來源 | 結果與判斷 | 關聯紀錄 | 待查條件 |
|---|---|---|---|
| DuckDuckGo HTML：`"Bash Fighter" agent commit AI session prompt Bash Entertainment`；`"Bash-Entertainment/bash-fighter" agent log model`；[README](https://github.com/Bash-Entertainment/bash-fighter)、[commit history](https://github.com/Bash-Entertainment/bash-fighter/commits/main)、[GitHub API commits](https://api.github.com/repos/Bash-Entertainment/bash-fighter/commits?per_page=20) | README 第一手自述稱日常開發（大部分 source 和帳號貼文）由代表 owner 的 AI agent 持續完成，AI agent 也 review PR／issue。API 可見連續提交：2026-09-28 至 2026-10-03 涵蓋控制提示、新手場次、match telemetry、手機攻擊流程等；提交文字提及真實新手場次觀察及據此修正。這些證據支持持續營運／迭代中的 agent-maintained product，但未識別 agent 底模、哪條 code 屬哪一次 user request、原始 brief 或 complete transcript。commit log 是 source-change history，不是 agent trajectory。| 更新 [G0267](../records/G0267.md) | 若 repo 加入 run/task logs、agent/model attribution 或 initial commission，再拆出具體 run。|
| DuckDuckGo HTML：`"Night-Patrol" Codex prompt session 歸藏`；`"夜巡录：荒庙篇" Codex 最初 提示詞 迭代`；`op7418 Night Patrol Codex GPT model prompt`；作者 [X 原始長文](https://x.com/op7418/status/2050023375746285747)、[素材流程貼文](https://x.com/op7418/status/2050030364018819581)、[GitHub commits](https://github.com/op7418/Night-Patrol/commits/main)、[release](https://github.com/op7418/Night-Patrol/releases)、[英文轉載](https://en.kocpc.com.tw/archives/3487) | 原作者 X 長文 HTTP 200，確認最初是向 Codex 提出類似《殺戮尖塔》的短 kickoff；首個 demo 後再請 Codex 用 GPT-Image 2.0 做素材，另有從千張資源挑圖及後續工具規劃。它支持 Codex 工具能力和首輪起點，但沒有逐字首 prompt、Codex model ID／版本或完整後續對話。Git history 顯示 2026-04-30 `Initial playable night patrol prototype` 後，當日有勝利過場、敵人立繪、音效／cinematic、難度選擇、HUD 等提交，release v0.2.1-demo 發布於當日 14:51 UTC。這更直接證實公開 release 不是首個原型凍結版；無法由 commit 知道人類每一輪指示細節或哪一版何時可交付。| 更新 [G0268](../records/G0268.md) | 若要判 strict one-shot，仍需逐條 follow-up transcript、Codex 版本、initial prototype／final build freeze 點和作者說明哪些改動由誰提出。|
| 同上查詢；[X 另一貼文](https://x.com/op7418/status/2050030364018819581) | 只說明作者為素材搜尋任務提供了上千張遊戲素材，Codex 自行拼圖索引再挑選檔案；它是任務內部的 AI 自主能力，不是玩家交付遊戲的獨立 run 或無 follow-up 證明。| [G0268](../records/G0268.md) | 保留為工具規劃例子，不列模型成品成績。|

## 結論與更新去向

- 未找到 Bash Fighter 的具名 initial user task／model session；它的連續新手 telemetry 修正反而支持維持「持續開發產品 lead」，不當一次交付案例。
- Night Patrol 第一手 X 和 commit chronology 補足了開場文字、GPT-Image follow-up、prototype 到 release 的同日迭代證據；這顯著提高了**判斷其非 one-shot 最終成品**的來源可靠度，但沒有提高它作為一次交付候選的證據，也未帶來新強候選。S54 後未找到新強候選／顯著 one-shot evidence gain 的累計仍為 4（S55–S58）。
- G0267、G0268 已分別加上 commit-history／作者 X 原始來源和本批回鏈。短名單不變。精確待件：Bash Fighter task/model/trace；Night Patrol exact prompt/model/follow-up transcript及 prototype/final freeze 對照。
