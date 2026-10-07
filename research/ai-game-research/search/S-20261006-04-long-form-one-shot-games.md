# 搜尋批次 S-20261006-04：近期長時 one-shot 遊戲

**日期：**2026-10-06（台北時間）  
**問題：**已找到的新版遊戲裡，是否有比短篇生成展示更能測試「一則使用者委託後，AI 長時間自主建置、測試、修正，最後交出可玩成品」的強候選？模型比較不是入選前提；優先查近期型號、原始任務、可玩 build、自主 QA 證據和真實畫面。

## 搜尋方向與實際查詢

- `site:github.com/tanuu5/nova-lancer one request Claude Opus 5.5 prompt`
- `site:github.com/Nipale-ai/opus-5-5-overnight-builds Fall Line prompt one brief`
- `site:senko.net/vibecode-bench Fogbound Frontier one-shot prompt benchmark Opus 5.5`
- `site:x.com/LexnLin/status/2102834362530079093 Arkenfall prompt one shot`
- 開啟並搜尋近期策展集 [Frontier Games](https://github.com/theolundqvist/frontier-games) 的 `Arkenfall`、`Fall Line`、`Nova Lancer`、`Fogbound Frontier`、`Turbo Kart Rally`；該集收錄 2026 年 9–10 月可玩遊戲與作者影片／截圖，僅當探索索引，不將策展文案當作 one-shot 的直接證明。
- 直接閱讀 [Nova Lancer repo](https://github.com/tanuu5/nova-lancer)、[Fall Line 原始 prompt](https://raw.githubusercontent.com/Nipale-ai/opus-5-5-overnight-builds/main/briefs/fall-line-prompt-as-sent.md) 及其模型輸出的遊戲說明、[Turbo Kart Rally repo](https://github.com/bridge-mind/turbo-kart-rally)；另檢查 [Vibecode Bench](https://senko.net/vibecode-bench/) 固定 prompt 與結果說明。

## 新增及更新

### [G0194 · NOVA LANCER](../records/G0194.md) — 強候選

Opus 5.5 MAX、一次一句 prompt、約 100 分鐘；提供 3D 軌道射擊全關、三區段、僚機／武器／升級、Boss、保存分數與控制器支援。作者公開原始任務並稱有逐幀推進和 bot 從頭到尾試玩，另有兩個平行子代理處理音訊與肖像。重要限制：作者公開更新歷史確認發佈後人工修過子彈顯示與手機 UI bug，因此**現行公開 build 不是未改動的生成時交件**；若採用此題比較模型，要保存 AI 停止時的 frozen build。美術未由使用者確認。

來源：[原始任務與 repo](https://github.com/tanuu5/nova-lancer)、[可玩 build](https://tanuu5.github.io/nova-lancer/)。repo 的開發說明同時記錄最初一句委託、完成時長、模型、工具、兩代理工作和自動通關機制。

### [G0195 · FALL LINE](../records/G0195.md) — 強候選

Opus 5.5 xhigh、Claude Code headless、新工作階段、六小時時限；作者稱 339 分鐘後自行停止、111 commits、全程無人回答問題或改碼。它將山域、滑雪／單板、雪地物理、技巧／Combo 計分、三種活動、AI 示範、回放／鏡頭、手把和 Playwright 自我檢查整合。詳盡 prompt 指定固定時點截圖／短片、畫面檢查、物理與 FPS 數值、console 錯誤及修正迴圈；可玩 build 和任務全文公開。這是目前最強的長時自主 QA 任務之一。限制：brief 已非常具體，不是只給模糊創意讓模型自由發想；以《Steep》玩法作參照；run 條件很長且偏 Claude 的工具環境；美術還需使用者看 build 判斷。

來源：[公開 run 條件和時間紀錄](https://github.com/Nipale-ai/opus-5-5-overnight-builds)、[原始 prompt](https://raw.githubusercontent.com/Nipale-ai/opus-5-5-overnight-builds/main/briefs/fall-line-prompt-as-sent.md)、[模型輸出的遊戲與操作說明](https://raw.githubusercontent.com/Nipale-ai/opus-5-5-overnight-builds/main/briefs/fall-line-model-readme.md)、[可玩 build](https://nipale-ai.github.io/opus-5-5-overnight-builds/fall-line/)。

### 更新舊線索

- [G0164 · Turbo Kart Rally](../records/G0164.md)：以原始 repo 核實為 Opus 5.5 五代理、單一 prompt、無追問；包含七名 AI 車手、甩尾／mini-turbo、八種道具、一條賽道及合成音訊。代理分模組測試，整合階段也實玩。列備選，與 Kart Blitz 題型高度重疊，不作本輪主推。
- [G0017 · Arkenfall](../records/G0017.md)：策展來源指向可玩開放世界動作遊戲與作者貼文；尚未查得可引用的原始 prompt、無人介入和自主 QA 證據，維持待核實，不列嚴格候選。

## 已查但不納入強候選

- [Fogbound Frontier](https://senko.net/vibecode-bench/2026/rts-opus-5.5.html)：近期 Opus 5.5 約 47 分鐘的一次 RTS 固定題，有可玩 build 和 prompt；指令特地要求「simple but functional」RTS，目標是建築、生產、資源、地圖開拓與 AI，適合一致性回歸／基礎跨系統子測，但相較本批 NOVA LANCER、FALL LINE 和現有 Ruinseed／Fable Cities，難度不足以成為主要上限題。
- [Over the Lines](https://senko.net/vibecode-bench/2026/flysim-opus-5.5.html)：同作者另一固定 prompt 一次飛行模擬，有真實 build；任務廣度為地形與 WWI 雙翼機戰鬥，適合技術副測。先前已知有同類更詳細 Airship Trader、Armor Alley、NEON BAY 題，故本批不重複新增。
- Tidewater：實際玩法含 18 種魚、釣線張力、船隻／天候與升級，畫面題材豐富；公開建置被描述為 8 小時 Opus 5.5 Claude Code session，對話／commit 顯示逐步追加需求，未證實一則委託全程無人介入，排除嚴格候選。
- Embervale：成品含約一小時 RPG 劇情、支線、隊伍戰鬥與 Boss，但作者坦言兩天使用 60–70 prompts，主要由作者遊玩版本並引導，非使用者定義的一次委託。
- Ink Field：作者稱單 prompt、一小時 hands-off，但留言描述模型先提出玩法、使用者再指示「build it」，而且作者主觀評 gameplay boring，無 playable link；不納入嚴格候選。
- Drowned Gambit：有可玩 roguelike chess 作品和單次生成宣稱，但題目規模窄，製作者說模型用量用完，沒足夠的長程系統整合或自主修正證據；只作輕量參照。
- Dropday「3D Space Game」：有成片和一句 prompt 的說法，頁面自述模型來源不確定且作者警告模型 attribution 可能是 AI 推斷；「ship/asteroids/particles/score」任務也偏小，排除。
- PowerHub kart test：見到 Opus 5.5／Sonnet 5.5 同 prompt 賽車摘要，但沒有完整 prompt、source、freeze build 或充分 run log；Kart Blitz 與 Turbo Kart Rally 證據更直接。
- Voxel Musou、CrossFire Transport Ship、QQ Speed Drift、Pelican Bike Ride 等策展條目有可玩 build 與程序畫面，部分甚至標示單句 prompt，但相較本批兩強候選，其玩法深度較窄；已存為後續查重線索，不因「zero edits」宣稱一律升主候選。

## 重查條件

若有新的 Opus／GPT 系列模型可用，重跑 Fall Line 和 Nova Lancer 任務後保存停止時原始 build、agent 自修正過程與獨立行為驗收；若 Arkenfall 作者公開原始 prompt、run timeline 或無人介入證據，重評 G0017。只有使用者看過真實遊戲 build 後，才更新其美術評價。
