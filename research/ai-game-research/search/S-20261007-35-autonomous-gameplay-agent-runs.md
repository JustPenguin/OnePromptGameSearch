# S35 · 近期自主遊玩既有遊戲的 AI agent runs

**日期：**2026-10-07　**研究方向：**長流程 agent gameplay 實測與可觀測性方法

## 研究問題

在近期 GPT-6 Astra 自主操控既有遊戲的案例中，是否有可核查的單次指令、長流程目標、工具／狀態 trace、影片和完成條件，能為一次生成遊戲測試提供可用方法？嚴格區分「AI 玩遊戲」與「AI 寫遊戲」。

## 實際搜尋

- `site:github.com agent-wow GPT-6 Astra autonomous World of Warcraft agent run repository`
- `GPT-6 Astra completes Portal 24 hours full run source code trace GitHub single prompt`
- `2026 AI agent benchmark autonomous gameplay long horizon game completion screenshots trajectory GPT-6 Astra`
- `site:github.com autonomous AI agent game benchmark gameplay task trajectory 2026 open source`
- `site:github.com/asp67/when-agents-rule autonomous model gameplay transcript benchmark`

近期 GPT-6 Astra Portal／WoW 新聞是線索來源；結論改以 run 作者自己的文章、公開 repo、trace 文件和 game harness repo 核實。

## 核對結果

| 項目 | 公開證據 | 與研究目標的關係 |
|---|---|---|
| GPT-6 Astra Portal run | [作者 repo](https://github.com/cozyblaze/portal-agent)公開控制器、SourcePauseTool patch、設定與 sanitized log；[evidence README](https://github.com/cozyblaze/portal-agent/tree/main/evidence)稱保留 6,925 筆、原始 26,460 筆記錄，刪除 3,263 個圖片 occurrences。作者記錄 GPT-6 Astra Max，約 23h43m；遇容量中斷後續跑並切 Fast，過程中唯一額外遊戲指令為讓片尾字幕繼續播放。初始目標「通關到片尾字幕，不查攻略」。模型讀畫面／角色座標與鏡頭、下達分組動作，再看結果。 | 可研究如何記錄觀測、動作與工具結果；不是 strict no-intervention，也不是單模式 run；它測通關 Portal，不是生成遊戲。作者沒有將它宣稱為正式 benchmark。 |
| GPT-6 Astra agent-wow | [作者文章](https://agent-wow.sh/gpt-6-astra-plays-world-of-warcraft-for-the-first-time-with-agent-wow/)公開一則初始 prompt：「create an orc character and complete all quests in the starting zone」；GPT-6 Astra xhigh 約 40 分鐘、零死亡，並連結完整 gameplay video；[agent-wow repo](https://github.com/agent-wow/agent-wow)提供 AzerothCore client／agent workspace。run 從 server 封包與 SQL 資料抽取資訊，自行寫 C++/Detour 尋路工具。 | 清楚高階任務和真實長流程行為，可借鑑任務終點與工具證據；但為自主遊玩舊遊戲，不是 coding game-generation；作者文章非完整逐訊息 Codex log，無同 harness 模型對照。 |
| When Agents Rule | [公開 repo](https://github.com/asp67/when-agents-rule)提供多模型 RTS agent testbed、固定 map seed／資源、tool-call transcript、JSONL 及結束結果；可同時評估行動有效、延遲、格式遵循等。作者明確稱它是 hands-on testbed、不是 benchmark；公開對局頁截至本輪看到 2026-10-03，未見 GPT-6 Astra／GPT-6.1 Sol。 | 可借固定條件和完整決策紀錄的設計；不能作為正式 benchmark 排名，更不能代表 AI 建置遊戲的能力。 |

## 排除理由／結論

本方向確認有具 trace／錄影的最新長流程 AI gameplay run，但沒有把遊戲從零做出來的案例。若納入 game-generation 候選，會把模型玩既有產品的能力誤當成設計和交付新產品的能力，因此不新增 G 生成候選。新增 M0027 作鄰接方法參考。

Portal 有人工恢復操作、模式切換及片尾指示；其 sanitized log 非完整原始軌跡，無法做逐像素重播。WoW 作者稱單 prompt，但沒有公開逐訊息原始 transcript。When Agents Rule 是個人測試台，尚未見最新目標模型 run 和經多回合驗證的評分程序。這些限制都保留，避免把新聞標題／作者描述直接提升成 benchmark 成績。

## 下次重查條件

- Portal Agent 若公開多模型、多次 run 及原始視覺軌跡，可重核自主遊戲評測方法；它仍不是遊戲生成測試。
- agent-wow 若有 GPT-6.1 Sol／Astra 多次重跑、公開原始 session／機器可讀任務成功檢核，再看能否支持跨模型 agent gameplay 比較。
- When Agents Rule 若加入最新 frontier 模型並提供可重播、多 seed 對局及正式評分，再評估其 game-playing benchmark 身份；仍與 game generation 分表。
- 主要研究接下來轉回近期從零生成 game build 與其原始 session，優先找美術達使用者門檻、系統足夠複雜的例子。
