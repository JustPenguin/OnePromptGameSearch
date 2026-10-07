# S24 · 學術／開源遊戲生成基準與可重跑任務庫

**日期：**2026-10-07　**研究方向：**從正式遊戲生成基準與公開開源評測環境查找目前真正可下載／可重跑的高難度一次委託任務，逐一分辨「論文聲稱有多少題」、「題目與 evaluator 是否公開」及「模型 run／實際成品是否能檢閱」。主查 GameCraft-Bench、GameASG-Bench、GameXpert-Bench、PlaytestArena；另記錄搜尋中發現的新 GameForge Harness，評估其任務難度和跨模型可用性。

## 實際搜尋詞

- `site:arxiv.org GameASG-Bench 2609.21293 official task benchmark 47 tasks`
- `site:github.com/areal-project/GameASG-Bench README docker_run hidden tests model`
- `site:arxiv.org GameXpert-Bench 2608.21833 github benchmark 97 tasks`
- `site:github.com GameXpert-Bench 97 task game generation benchmark`
- `site:arxiv.org/abs/2605.28258 PlaytestArena 200 games continual generation code dataset`
- `site:github.com/RunRiotComeOn/gui-agents-for-continual-game-generation PlaytestArena tasks release`
- `site:github.com/FreedomIntelligence/gamecraft-bench benchmark 140 tasks open source prompts demos`
- `site:arxiv.org/html/2609.39045 GameCraft-Bench 140 tasks task dataset 2026`
- `GameXpert-Bench arxiv 2608.21833 GameGen single request 97 task release repository`
- `GameCraft-Bench official GitHub 140 tasks README current results 2026`
- `GameASG-Bench official task documents L1 L2 clean generation container CLI latest results`
- `GameForge Harness game development agent independent evaluator open-ended game creation benchmark GPT-5.6`
- `site:github.com/AlbusChen/GameForge-Harness open20 task manifest solver independent evaluator release`

## 覆核來源與判斷

### GameCraft-Bench（B0011；既有 Airship Trader G0014）——本輪最完整的高難度、可重跑正式任務庫

- 查看[官方 GitHub README](https://github.com/FreedomIntelligence/gamecraft-bench)、[基準網站與模型表](https://tongxuluo.github.io/gamecraft-bench-website/)、[arXiv 論文](https://arxiv.org/abs/2606.17861)及已在目錄登錄的[Airship Trader 任務](https://github.com/FreedomIntelligence/gamecraft-bench/blob/main/tasks/openworld-airship-trader/instruction.md)。
- README 現列 140 個 Godot 題、15 個 game families；需交完整 Godot project 和可重播操作軌跡，再由獨立 verifier 啟動、重播、錄製畫面並用 hidden rubric／multimodal judge 評分。任務覆蓋平台、策略、模擬、open-world、roguelike、tycoon 等；Airship Trader 可留作既有開放世界／經濟候選，不另建同名項目。
- 最新公開模型表截至 2026-07-31，含 GPT-5.6 Sol、Claude Opus 5 等，但對 2026-10 當前模型比較已非最新；把價值放在公開 task corpus、build gallery 和可換新模型重跑，不將其舊 leaderboard 說成當前前沿成績。官方摘要的「strongest configuration 65.70%」與同頁 Opus 5 xhigh 表列 68.44% 不一致；本輪紀錄表格逐列數值並揭露摘要矛盾，不替來源猜解。
- 邊界：官方範圍聚焦 2D Godot，不含 3D、多人網路、大規模物理或長期製作流程；rubric 有 mechanics/depth/visuals/art，但不測主觀遊戲樂趣。相較短篇 browser mini-game benchmark，已公開 140 題的內容與環境更適合選高系統題重跑。更新 [B0011](../records/B0011.md)，保留 [G0014](../records/G0014.md) 作已選任務。

### GameASG-Bench（B0010）——最清楚的單次任務與行為合約／隔離 evaluator

- 查看[arXiv 論文](https://arxiv.org/abs/2609.21293)、[官方 GitHub](https://github.com/areal-project/GameASG-Bench)及 `armor-alley`／`grand-theft-astro` 的任務文件和 check suites。
- Repo 現列 47 個 browser-native 任務、12 類型（32 個 2D、15 個 3D）；每題有 `target.md`、`game-spec.md`、`tdd.md`。初始 target 作唯一委託；agent 在乾淨生成容器得到任務規格及公開行為介面，不得到 hidden test files，輸出單一 `index.html`；generation 停止後由另一容器執行靜態 L1、headless Chromium 真實輸入／狀態 L2。官方支援明確傳入模型 ID、harness、時間／turn 設定；預設一 attempt、3600 秒、120 Claude turns。這符合 AI 可自主自測／修正、最後另行驗收的條件，但公開測試 API 合約是額外規格要求，單頁交付也限制輸出形式。
- 論文測九個 agent stacks，GPT-6-Astra／Codex CLI 最高 strict task success 26/47（55.3%）；平均 L2 93.2% 不代表每題完全成功，故推薦成績同時報全必要檢查成功率和各檢查通過率。已公開模型 roster 仍需用最新模型重跑。此 benchmark 確實有可下載的 prompts／checks，不只是論文任務數字；功能驗收很強，美術／趣味不由其自動分數代替。更新 [B0010](../records/B0010.md)，重查 [G0018](../records/G0018.md)、[G0072](../records/G0072.md) 等既有具體題，無新增重複 G。

### GameXpert-Bench（B0017）——一次任務定義很好，但未開放 corpus

- 看[論文](https://arxiv.org/abs/2608.21833)、[官方 repo README](https://github.com/Kwen-Chen/GameXpert-Bench)與[project page](https://github.com/Kwen-Chen/GameXpert-Bench/blob/main/docs/index.html)。GameGen 定義 97 個 empty-workspace、單一自然語言 request 任務（11 類，53 個 2D／44 個 3D），與使用者一次委託條件吻合；另外 100 GameFix 和 17 條六輪 GameOpt chains 不直接當 one-shot 成績。
- 官方 README 仍說 repo is being prepared; paper、task data、evaluator、model artifacts 將陸續加入；project page 的 Paper/Code/Dataset 按鈕仍 Coming soon。因此不是可直接抽任務重跑的 97 題庫，模型榜／samples也無法獨立核實。更新 [B0017](../records/B0017.md)，維持方法追蹤，不升推薦。

### PlaytestArena／Play2Code（B0032）——有 200 題研究主張，但可見 repo 不是題庫

- 查看[arXiv 論文](https://arxiv.org/abs/2605.28258)、[官方 GitHub demo repo](https://github.com/RunRiotComeOn/gui-agents-for-continual-game-generation)、[專案頁](https://continual-game-generation.vercel.app/)。論文稱 PlaytestArena 200 browser tasks／八類型，每題 pairing prompt 和 in-play behavior rubric，由 GUI agent 視覺操作評分。公開 repo README 實際只列八款 Play2Code browser games 的靜態 gallery，沒有此次查核可取用的 200 task/rubric corpus。
- PlaytestArena 是生成後 GUI 評測；Play2Code 則讓 coding agent 與 GUI player 在共享記憶中持續互動、反覆改版。前者的方法與最後產品盲看／實玩評價相近，後者明確屬多輪生成，不能把其 66.8% rubric pass rate 說成一次交辦結果。更新 [B0032](../records/B0032.md)，不新建遊戲候選。

### GameForge Harness（新增 B0047）——可供自治開發與外部驗收的方法，不是高難題本身

- 查看[官方 repo](https://github.com/AlbusChen/GameForge-Harness)、[Godot Open20 frozen manifest](https://github.com/AlbusChen/GameForge-Harness/blob/main/benchmarks/godot-open-game-creation20-v1.json)、[20-task evaluation report](https://github.com/AlbusChen/GameForge-Harness/blob/main/docs/godot-open20-unified-native-open-evaluation-2026-08-24.md)、[GameCraft Full140 report](https://github.com/AlbusChen/GameForge-Harness/blob/main/docs/gamecraft-bench-full140-unified-native-open-evaluation-2026-08-28.md)及[可玩證據索引](https://github.com/AlbusChen/GameForge-Harness/blob/main/showcases/README.md)。
- 適用流程：模型一次收到 brief，在 disposable workspace 中自主使用引擎、截圖／測試並修改；完成後 solver 看不到的獨立 evaluator 建置、輸入回放、錄影和核對。Open20 有 20 個空白 Godot task 和 freeze manifest（GPT-5.6 Sol medium、900s、一次、Godot 4.4.1、無網路、無 harness repair）；report 作者稱 20/20 import/runtime hard gates，提供匿名 build/交互品質評審。另對官方 GameCraft 140 題做 GPT-5.6 Sol high 一次 session 重跑，作者稱 140 builds、732 replays 完成，但分數用 subscription judge approximation，明確不是 official leaderboard submission。
- Open20 brief 每題都要求 `compact` 小型遊戲，故即使流程嚴謹也不符合使用者的上限題型要求；GameCraft full corpus 才有高系統題，但它已在 B0011/G0014 記錄。GameForge solver 目前 README 支援 Codex subscription／OpenAI Responses API；跨模型廠商接入尚待確認。報告作者自述且 Open20 n=1、品質 judge 與 solver 同屬 GPT-5.6 家族。故新建 [B0047](../records/B0047.md) 作為有用的自治 harness／獨立評測方法參考，不新增 Open20 mini-game 作主候選，也不將其分數當第三方核實結果。

## 本批未納入／後續查證

- 未把 GameXpert/PlaytestArena 的「論文有 97／200 題」當成可下載 task corpus；官方資源缺口是本輪明確查證結果。
- 未新建 GameCraft 的 demo 個案，避免把已登錄 Airship Trader 及其他 sample gallery 重複拆成每圖一個候選。
- GameForge 有用於驗收流程與可重跑環境，但其新 Open20 題目明確是小遊戲；這不滿足本研究「高難度測上限」的入選標準。
- 下一方向：查可更換多廠商 solver 的公開長流程／高系統題庫與近期實際 run traces，尤其是 3D、多人或高畫質成品；只查比 GameCraft 2D 題庫更具上限的來源，並先查重 G0047、G0206、G0193、B0011、B0010、B0047。

## 更新去向

- 更新 [B0010](../records/B0010.md)、[B0011](../records/B0011.md)、[B0017](../records/B0017.md)、[B0032](../records/B0032.md) 的現況、適用範圍和重查條件。
- 新增 [B0047](../records/B0047.md) GameForge Harness 方法參考。
- 精選摘要／研究索引同步說明 GameCraft 和 GameASG 是可取得題庫、GameXpert/PlaytestArena 尚未釋出題庫、GameForge Open20 題型偏小且只作驗收方法；美術判斷維持逐項由使用者評定，不因 benchmark rubric 調整。
