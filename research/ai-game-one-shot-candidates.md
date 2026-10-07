# AI 一次委託遊戲評測｜精選候選

本頁集中列出值得選題討論的候選，不是全部研究項目。待核實、排除、搜尋線索與方法參考皆可在[全項目目錄](ai-game-research/catalog.html)查找；每項有固定編號與完整歷史段落。後續詳細更新以獨立紀錄為準，重要候選變更同步本頁。

**證據標記**

**使用者美術驗收（2026-10-07；完整逐項範圍見 [檢閱頁評價表](ai-game-one-shot-review.html#user-art-evaluations) 及 [E0008](ai-game-research/records/E0008.md)）：**合格：Kart Blitz、Pelican Bicycle、Void Explorer、Fusepoint。**勉強合格：**OneShotGTA：Palm Bay／Golden Hour、Rubberhose Ruckus；Rubberhose 的畫素解析度不足由美術設計補足。**不合格：**BioNeural、B0055 六款同題輸出、Itsy Bitsy Spider、DUNGEONFALL、Open-World Survival、Crossy Road、Voxel Sandbox、Ridge Run、Fortnite-style Battle Royale、THE NINTH BELL、已檢視舊作品及新畫面 Sonic、Rocket League、Turbo Kart Rally、Neural Sight、Wayforge。**無法確認：**Fable Cities。Diablo Cathedral 缺可供評價的遊戲畫面，仍待評。美術結論與玩法／系統重跑價值分開評估。


### 待使用者評價的近期 3D gameplay 視覺參照：Historical Flight｜G0289

創作者將公開可玩的 1918 Amiens 雙翼機旅程歸因 GPT-6 Astra，包含編隊、偵察照片／日誌、鐵路空戰和六段主線；可看[實機任務畫面](https://github.com/itsleon21/historical-flight-contribute/blob/main/docs/images/showcase/flight-mission.jpg)與[可玩版](https://itsleon21.github.io/historical-flight-contribute/)。原始 prompt、model snapshot、session、零介入與完整可重建 assets 未公開，**不列 strict one-shot 成績**。畫面已收進檢閱頁待評；美術、玩法和流程證據分開判斷。[G0289](ai-game-research/records/G0289.md) · [S82 查核](ai-game-research/search/S-20261007-82-firsthand-game-prompt-and-session-source-audit.md)

美術在本研究中是**獨立高權重軸**，以實際 gameplay 畫面評估風格、場景與資產細節、光照／材質、動畫／特效和介面；3A 呈現是優先搜尋目標，高品質風格化作品也可評。作者或 benchmark 的美術分數只保留為來源自述，不取代使用者評價；未經使用者評價一律標「待使用者評價」。純 3D 世界／畫面展示可作視覺參照，若沒有玩法證據便不列遊戲候選。

- **A｜可重跑的實際成品案例：**有任務文字或清楚委託描述，以及實際可玩 AI build；作者流程紀錄仍屬作者自述，除非有獨立核實。
- **B｜正式規格任務：**有可重用的遊戲規格和驗收材料；目前未確認 AI 生成成品圖廊。可作共同任務交給不同模型重跑。
- **C｜題材／成品參考：**遊戲系統有價值，但 one-task 條件、原始 prompt 或迭代過程尚未證實；先借用題材或等補證據。

是否已發布多模型比較不是入選門檻。成品圖只有在確知來自 AI build 時才標為 AI 輸出；原作畫面會另行註明。

### Blocky Realm: Cloud Parkour — SeaVerse「GPT-6」一行 prompt 短題副候選｜C（平台聲明待核）

完整紀錄：[G0281](ai-game-research/records/G0281.md) · [原始一行任務與 SeaVerse 說明](https://seaverse.ai/ai-game-maker/gpt-6-game) · [託管輸出頁](https://seaverse.ai/apps/dnNPmjzaU0EMPNT2) · [平台分享畫面](https://image.cdn2.seaart.me/upload/static/20260907/ddc8883821137f74048ee434845c1540.png)

- **為何保留：**頁面公開 prompt「Make a 3D parkour platformer HTML game with Minecraft-inspired art」，並聲稱是 GPT-6 的 first-pass、single-prompt、unedited playable output；畫面有一致 voxel 浮島與 HUD，值得使用者評價美術。
- **限制：**模型供應者／snapshot、session、source、凍結 build 和實際操作通關均未核；本次 app HTTP 只確認載入殼頁。21 平台、3 biome、18 水晶、checkpoint 的系統規模屬短 parkour loop，不是高系統長流程主測。列為待核高視覺副候選，不作已確認 one-shot 排名。

### GPT-6.1 Sol light 七題 source／prompt collection｜近期模型任務組（作者申報；session 未公開）

完整紀錄：[C0024](ai-game-research/records/C0024.md) · [原始 prompt pack](https://github.com/PromptEngineer48/gpt-6.1-sol-light-games/tree/main/prompt-pack) · [七款 source builds](https://github.com/PromptEngineer48/gpt-6.1-sol-light-games)

- **值得保留：**同一公開 repo 有七份原始任務文字、七款可本機 build 的 Three.js/Vite 成品與 README，標示由 GPT-6.1 Sol light 建立。系統範圍最值得抽查的是商場殭屍生存 DEAD HOURS、城市 sandbox NOVA DISTRICT、潛行關卡 SHADOW PROTOCOL 與城堡攻防 LAST KINGDOM；完整 prompt 和 source 可以直接作新模型重跑題。
- **證據界線：**repo 說每題各由一份 prompt 產生，但沒有模型 session、實際模型 ID／工具設定、build hash 或自主 QA trace。Games 的首次 Git commit 早於 prompt pack 四分鐘，這不足以推翻作者聲明，也不足以獨立證明任務原文先於 build。README 中列出的自動測試不能證明模型曾執行它們。七題美術均待使用者親自看成品。
- **定位：**高價值近期模型輸出／任務組，不作已核實 one-shot 成績或一份正式盲測基準。完整查詢和分題範圍見 [S50](ai-game-research/search/S-20261007-50-gpt61-sol-light-game-builds.md)。

### GPT-6.1 Sol × Sonnet 5.5 同題 RPG／Kart／FPS 六個 playable build｜B0055

[六款直接遊玩與模型並排頁](https://haruka8846.github.io/newmodel-games/) · [共同任務](https://github.com/haruka8846/newmodel-games/tree/main/tasks) · [完整研究紀錄](ai-game-research/records/B0055.md) · [S53 查核](ai-game-research/search/S-20261007-53-frontier-model-github-game-artifacts.md)

- **比較價值：**兩個近期 coding model 以 xhigh effort、不同 agent CLI，各自從空白專案完成同三題：2D 地城 RPG、3D 卡丁車、3D FPS。六個 source projects、六個 hosted playable builds 和各題原始 prompt／機器 acceptance tests 都公開；作者報告六款都是 10/10，並有實際畫面截圖。
- **看交付成品要注意：**作者手動遊玩又發現 Sol FPS 敵人不會開火、Sol 卡丁車左右操控相反且只有單一橢圓賽道、Sonnet 卡丁車對手過弱、兩款 RPG 都有引導／亮度問題。這顯示 10 項狀態測試不代表玩家體驗完整；規格也沒有替使用者評美術。
- **流程界線：**每個模型／任務 N=1；不同 harness 和工具令速度不能當純模型對照。測試失敗可回饋最多五輪，repo 沒原始 session 或 grader JSON，不能核實 feedback 是否全自動、使用者是否完全退出。六款美術皆待你檢視，不因通過功能測試而預先合格。
- **獨立重跑：**本研究在 Linux Chromium 用作者原版 grader 重跑兩款 RPG，Sonnet／Sol 都 10/10、沒有 browser errors；Kart／FPS 重跑受 CDN 憑證及 D3D11/SwiftShader 資源限制阻礙，未產生有效結果。這只補強 RPG test reproducibility，不是長流程玩家驗收。

### Game Bench《Itsy Bitsy Spider》｜GPT-6 Astra 2026-09-24 可玩輸出；短循環副測，不列上限主測

完整紀錄：[G0266](ai-game-research/records/G0266.md) · 方法紀錄：[B0009](ai-game-research/records/B0009.md) · [直接玩](https://game-bench.piccini.app/games/gpt-6-astra-20260924/) · [凍結原 prompt](https://game-bench.piccini.app/frozen-prompt.md) · [盲玩介面](https://game-bench.piccini.app/blind-tests/) · [S54 核查](ai-game-research/search/S-20261007-54-player-facing-evaluation-coverage.md)

- **任務與成品：**GPT-6 Astra high，頁面標示 2026-09-24，16m06s、1.84M tokens、$4.95；成品可直接開啟。完整 prompt 要求蜘蛛爬無盡牆、耐力與飛蟲、預告暴雨及避難洞、逐步難度、程序音效、桌機與真手機輸入、UI／死亡／重開，並要求 AI 自己完整遊玩、看畫面、測效能、修 bug 後交付。
- **為何只當副測：**玩法機制不少，但作者把它明確叫 small game，主要仍是一條短循環，沒有多區域、長程進度或大型內容系統；不符合拿來代表完整遊戲上限的標準。適合另外測 agent 自主 playtest、行動控制、聲音與迴圈可讀性。
- **評分及證據界線：**作者榜列總分 95.5（Gameplay 92.6、Adherence 99.8、Engineering 96.2、Art 98.5）；其中 Astra 分數由作者提供，使用者已判定該 build 美術不合格。該 run 的資料又明示 `processStatus: review`、第三次嘗試通過但 VM-host containment canary 未解，故不宣稱 strict one-shot 稽核完成。匿名試玩頁目前有 25 builds 的評分流程，但未找到實際盲評樣本或彙總。使用者已判定美術不合格；作者 Art 分不能代替你的判斷。

### Fusepoint — 單一 PRD 後 70+ 輪自主完成敘事 FPS｜A（高度符合使用者退出流程；版本仍有 QA 缺口）

完整紀錄：[G0263](ai-game-research/records/G0263.md) · [HoH 方法紀錄 M0028](ai-game-research/records/M0028.md) · [論文](https://arxiv.org/abs/2609.01481) · [真實遊戲影片](https://flesymeb.github.io/HarnessOfHarness/assets/video/fusepoint-real-gameplay-preview.mp4) · [官方下載入口](https://drive.google.com/drive/folders/1gch3D5HKa3n3gxM0LNrzubcJxlFFLaXy?usp=sharing) · [Source](https://github.com/Flesymeb/fusepoint)

- **委託／執行：**從空工作區與單一使用者 PRD 出發；Codex CLI＋GPT-5.6-Sol high、Godot 4.7／Godot MCP；研究記錄 70 輪 Planner／Developer／QA 循環。人類只恢復網路/API 連線，沒有提供內容指示。這直接吻合「輸入任務後不再介入、AI 自行修正」的流程，但不是單次模型呼叫。
- **實際題目：**五分鐘單人拆彈 FPS，需依序攻下兩處控制點，在最終目標完成三階段拆彈，配置 18 名敵人並能走成功或爆炸失敗結局；3D 場景、戰鬥、敘事、介面、音效與穩定性互相依賴。
- **證據與缺口：**論文附實玩影片、模型／工具／人類介入界線及 Loop 70 issue 統計；遊戲 source 可檢視，另有下載入口。原始 PRD 全文與 Loop 70 凍結版未找到。Loop 70 時 81 個 issue 有 16 個尚未解決；公開 repo 已演進到 Loop 96，仍列 QA 缺口，因此不把作者「human-playable」或「polished visuals」當作無缺陷、也不當成你的美術驗收。
- **選題建議：**用當前模型從同一份初始任務重新生成，保存完整自主 run、停止時 frozen build 和完整遊戲通關錄影。Fusepoint 原模型 GPT-5.6-Sol 並非本輪最新 roster；它的價值是已公開實測「一次委託後長期自我修正」這個流程，而不是模型新舊排名。

### Ridge Run — GPT-6.1 Sol 單檔爬坡物理遊戲｜A（新模型可玩副測；不代表完整遊戲上限）

完整紀錄：[G0077](ai-game-research/records/G0077.md) · [實際輸出截圖](https://www.bitsminds.com/buildoff-2026-09/hillclimb_sol61_play.jpg) · [直接玩 GPT-6.1 Sol build](https://www.bitsminds.com/buildoff-2026-09/hillclimb_sol61.html) · [作者完整同題 hands-on 測試](https://www.bitsminds.com/news/claude-opus-5-5-vs-gpt-6-1-sol-hill-climb-2026)

- **為何值得保留：**作者給 GPT-6.1 Sol 一則單檔 HTML brief，要求車輛懸吊和坡地物理、鍵盤／觸控、菜單／遊戲／結果閉環、翻車失敗及重玩；模型據稱自行測試修正，57 分 38 秒後交付可玩的 build。可直接檢查實際輸出和完整關卡，不需要看示意圖。
- **限制：**它是單關技術副測，不含大型內容量或多系統長流程。評分由單一作者 hands-on、非盲評；Opus 5.5 沿用先前 build、agent/harness 不同，原始 prompt 和 session 未公開；GPT-6.1 還讀了先前一般 one-shot build 的 Codex memory。作者以 13/20 評分，不是使用者美術判定。此項依你直接看 build 後再標美術結果。

## 最適合重跑「一則委託，AI 自主修正」的高難度題

### DEAD SIGNAL: EXCLUSION ZONE — 殭屍撤離 FPS｜B（流程最貼近；成品證據不足）

完整紀錄：[G0047](ai-game-research/records/G0047.md) · [完整 438 行任務規格](https://www.bridgebench.ai/prompts/30220eea-7128-4a4f-abb6-eba65412eb68) · [舊 Opus 5.5 source](https://github.com/bridge-mind/claude-opus-5.5-zombies-game)

- **我會優先讓新模型重跑這題。**完整 brief 明確定義單人 8–10 分鐘撤離任務、三個威脅區、守點／狩獵合約、殭屍尋路、三種槍、武器升級、彈藥與裝甲經濟、污染倒數和需要實際登機的直升機結局；還要求 AI 在一則任務內自行跑 browser、玩測、看錯誤、修正及視覺檢閱。
- **為何能測差距：**功能不能只存在於 HUD；牆要能擋子彈，殭屍要能繞路，任務獎勵只能一次，升級要改變武器，撤離必須由玩家到場完成。規格要求把槍械手感、敵人行為、地圖美術和閉環接起來，較難用漂亮標題頁蒙混過關。
- **與你的流程吻合：**使用者只交付一次 brief；AI 可在同一任務中自主實作、測試和修正。重跑時直接凍結 AI 最後交件，再由你驗收。這份規格較長且列得細，測的是複雜規格下的自主完成，不是完全開放的遊戲創意。
- **證據限制：**這份 BridgeBench 規格是後來另行整理的 challenge，不等於 Opus 5.5 或 Sonnet 5.5 Dead Signal 作者 run 的原 prompt。Sonnet 5.5 現已有可在本機建置的同系列 source build，但未找到同規格的 hosted playable 首版或 session transcript。因此它是**強重跑題**，不是已有模型按這份規格通過的證明。見 [G0236](ai-game-research/records/G0236.md)。

### Claude of Duty — 短 prompt 長程 FPS／Gauntlet Loop｜A（自主迭代案例；現存 repo 非首版）

完整紀錄：[G0035](ai-game-research/records/G0035.md) · [原始 prompt](https://github.com/mshumer/Claude-of-Duty/blob/main/prompt.md) · [原始碼與評測](https://github.com/mshumer/Claude-of-Duty) · [作者建置文章](https://mattpaige68.substack.com/p/claude-opus-5-built-a-playable-call)

- **實際 run：**作者稱 Claude Opus 5 收到一則「做出 COD 級 FPS」的 prompt 後，自行拆工作、多代理完成、反覆 /loop 和請視覺評審找錯；遊戲含 3D 街區、可進入建築、原創武器、後座／ADS、敵人掩體與 flank、ragdoll、程序材質與音效。這個任務開放度比 Dead Signal 高，能看 AI 如何自行補全規則。
- **測試價值：**作者留下與真實 COD 遊戲盲比的分數，成績遠未到 prompt 誇大的「最新 COD」目標；這提醒我們把作者目標與實際成品分開，也提供高難度長程 FPS 的測題起點。
- **限制：**Opus 5 已不是目前最新模型；GitHub 現有 repo 收錄提交後的優化、測試 harness 和多輪工程變更，不能冒充原始交件。最佳用途是從空專案把短 prompt 交給當前模型重跑，並保存 run trace／final build。

### Hollowflux — 水系統影響戰鬥的程序地城 RPG｜C（最新官方 playable；多輪人類引導）

完整紀錄：[G0225](ai-game-research/records/G0225.md) · [官方階段紀錄](https://developers.openai.com/showcase/hollowflux) · [直接玩 GPT-6 Astra 成品](https://tideglass-drowned-vein.openai.chatgpt.site/)

- **玩法與難點：**七層地城、即時戰鬥、六類武器、裝備和成長、Boss 及交易避難所；水位、流向、泡沫與電荷又會影響移動、敵人、拾取物和攻擊結果。
- **為什麼值得看：**這是當前較容易直接檢視的真實高系統成品；可以觀察程序畫面、攻擊、水的反應、敵人和成長系統是否整合成一致玩法。原官方開發文章也公開 gameplay 與迭代歷程。
- **證據界線：**GPT-6 Astra 作品頁明載從短 encounter 多輪加入樓層、物品、Boss、商店、難度、音效等。它不是一次輸入成果；把玩法 brief 交給新模型重跑才符合你的測試。

### Void Explorer — 太空到地表無縫探索｜C（高難度 3D 副測；多輪人類引導）

完整紀錄：[G0226](ai-game-research/records/G0226.md) · [官方任務與逐階段紀錄](https://developers.openai.com/showcase/void-explorer) · [直接玩 GPT-6 Astra 成品](https://void-explorer.openai.chatgpt.site/) · [官方遊戲錄影與系統文章](https://developers.openai.com/blog/how-to-build-games-with-astra)

- **玩法與難點：**官方文章列出 2,048 個星系、超過 10,000 顆程序星球；玩家從太空飛行、進大氣、降落、下船步行探索再回船起飛。位置精度、軌道、地形串流、視距細節、碰撞和渲染須在一趟旅程內維持一致。
- **測試定位：**適合作為高風險 3D 空間連續性副測；傳統敵人／任務／勝負循環較少，不建議單獨代表完整遊戲上限。
- **美術：**你已判定合格，並補充主要原因是原任務提示詞含美術精修指引；此理由只記錄此作品，不作其他作品的通用判定規則。

### No Man’s Sky Planet Landing — 單檔、無引擎的球面行星無縫降落｜A（技術上限副主測）

完整紀錄：[G0233](ai-game-research/records/G0233.md) · [2026-10-05 原測試：三款可玩成品、逐項實際截圖、任務與分數](https://www.bitsminds.com/news/claude-opus-5-5-vs-gpt-6-astra-vs-grok-4-7-planet-landing-2026)

- **實際考題：**在沒有第三方引擎、library 或圖片的單一 HTML 內，模型要從太空手動駕駛，穿越大氣層連續降到真正球形行星、著陸、下船步行，飛船留在原地，還要能回船再升空；鍵盤、滑鼠和觸控都須有提示，地形不能跳動、穿地或依賴幀率。
- **近期真實輸出：**Claude Opus 5.5、GPT-6 Astra、Grok 4.7 各自一次交件，可在原測試頁直接玩三份凍結 build；頁面有多張由實際遊戲擷取的場景畫面。作者測試 Opus 約 193 分鐘、Astra 約 59 分、Grok 約 153 分；按圖形／物理／音效／玩法共 20 分，分數為 18／11／7。這是同一作者的 hands-on 評分，不是模型獨立盲評。
- **模型新舊性：**測試發佈日為 2026-10-05，是目前查到的最新一批多模型可玩成果；但 roster 沒包含同期可用的 Sonnet 5.5、GPT-6.1 Sol 或 Gemini 3.8。重跑時按當日能用的前沿程式模型補齊，不應照抄舊 roster。
- **為何有辨別力：**不是多做一層 HUD 就能交差；一趟操作必須維持飛行位置、球體地形、大氣／地面轉換、玩家與飛船狀態一致。題目也要求 AI 先自行跑完整流程找錯再修正，符合「使用者不插手，AI 自己把交件補到位」的測試方式。
- **範圍限制：**難在 3D 技術與無縫感，並非長篇完整遊戲。它沒有敵人、任務、經濟、存檔或多小時進度；建議當高難度技術副測，再配一題真正的長流程系統整合主測。
- **比較公平性：**原測試同 prompt，但 Claude Code、Codex、Grok Build 三套 harness 不同，Codex 用 max 而非含自動委派的 ultra；不能把既有名次當純模型定論。你若重跑，固定工具、可用函式庫及時間／token／自我修正方式。
- **證據界線：**2026-09-04 的 GPT-6 Astra 官方文章含 gameplay supercut 和真實畫面，但也明確描述多輪人類指示、重構與 Playwright 自測。這是高價值重跑題和成品參照，不是一次輸入成績。概念圖不是遊戲內截圖；請看遊戲／錄影判斷畫面。

### Phantasy Codex Adventure — 自主長流程動作 RPG｜A（最值得以最新模型重跑）

完整紀錄：[G0242](ai-game-research/records/G0242.md) · [官方初始任務及每階段建置紀錄](https://developers.openai.com/showcase/phantasy-codex-adventure) · [GPT-5.6 Codex 可玩成品](https://phantasy-codex-adventure.openai.chatgpt.site/) · [官方最終成品圖](https://developers.openai.com/showcase/gpt-5-6-phantasy-codex-adventure.webp)

- **它為何適合測上限：**初始任務明確要求 AI 自行建立持續目標、創作補全、迭代到 polish／驗證／發佈；最後是八種生態區域、旅程與 Boss、三種職業、武器精通、契約、獨立生存模式和持續進度，不是只做一段戰鬥畫面。
- **原作品的限制：**展示成果是 GPT-5.6 Codex，不能當成目前最新模型結果；官方公開的是階段摘要而非逐訊息 session，因此不能獨立排除作者期間追加指示。重跑應交付原始初始 brief，由當前模型自主處理，並保存完整 trace、最終凍結 build 與通關錄影。
- **美術狀態：**使用者已判定不合格（2026-10-07；詳見 [E0008](ai-game-research/records/E0008.md)）。它仍是值得以最新模型重跑的長流程 RPG 題型；美術評價與其任務及系統測試價值分開。

## 近期前沿模型實測畫面參照

### Neural Sight — GPT-6 Astra captured-world FPS｜高寫實視覺與資產流程參照（非 one-shot 候選）

完整紀錄：[G0286](ai-game-research/records/G0286.md) · [公開 demo](https://monstercameron.github.io/Neural-Sight/) · [實機截圖](https://github.com/monstercameron/Neural-Sight/blob/main/docs/images/nelson-ghost-town.jpg) · [source／作者說明](https://github.com/monstercameron/Neural-Sight) · [S77 來源查核](ai-game-research/search/S-20261007-77-recent-model-visual-builds.md)

- **視覺與系統：**作者稱以 GPT-6 Astra 約 24 小時建成 browser FPS playground；有四個可進入環境、移動／瞄準／射擊、後座、換彈、蹲跳、球體互動和試驗性殭屍。可見實機圖有寫實日照、鏽蝕車輛與木質水塔。AgentsLoop 策展者對最佳截圖評 9.7/10，是 curator visual review，不是本研究實玩分或 AAA 認證。
- **美術來源：**場景主要是外部作者的 Gaussian-splat captures，手部及武器另用預生成 AI 影格；不能把寫實場景直接算作 GPT-6 Astra 原創美術。來源分層及四軸界線見 G0286。**美術已由使用者判定不合格。**
- **流程限制：**公開 source、demo、README 和模型歸因，但原始任務、session、工具軌跡、零使用者介入和凍結首版未核。作視覺與資產流程參照，不納入 one-shot 排名。

### Muse Spark 1.3 實際一次生成樣本｜G0255、G0257（新作品美術均已由使用者判定不合格）

- **我建議先看 DUNGEONFALL，再決定是否當高上限主題。**[原任務、文章內可玩 build 和多張遊戲內截圖](https://www.mdaakibansari.com.np/articles/meta-muse-spark-1-3-dungeon-crawler)：8–11 個程序房間及連通迴圈、三種敵人、近戰、掉落／藥水／寶箱成長、Boss 房、小地圖、死亡後可重開。文章稱 Muse Spark 1.3 xhigh 單 prompt 產出 736 行，零 follow-up；其證據屬同一位測試作者的申報，並非獨立稽核。頁面也揭露轉角追敵可能卡牆等缺點。它是本批「有勝負循環、程序地圖及成品可看」的最佳重跑候選，但使用者已判定美術不合格；保留其系統題與重跑價值。[G0255](ai-game-research/records/G0255.md)
- **互補題：程序 3D 開放世界生存。**[原始規格與 playable 輸出](https://www.mdaakibansari.com.np/articles/meta-muse-spark-1-3-open-world-survival-game)要求五種生態區、採集、飢餓／體力、配方、放置物、日夜光照和死亡重開；有足夠系統相依，可測探索／生存閉環。它缺敵對生物與跨刷新持久進度，故規模看似大不代表長程完整度已達標。作者宣稱 793 行、單 shot／零修正；使用者已判定美術不合格。[G0257](ai-game-research/records/G0257.md)
- **畫面校準題：Meta 官方 Crossy Road one-shot cookbook。**有 Meta 公布的[一次生成實際遊戲畫面](https://dev.meta.ai/docs-assets/one-shot-game-dev/02_gameplay.png)與[開始選角畫面](https://dev.meta.ai/docs-assets/one-shot-game-dev/01_start_screen.png)，採用 Kenney 角色／載具素材並展示 3D 環境；但遊戲範圍和循環較短，只建議當畫面與測試設定參考，不列上限主測。須注意官方一 shot 使用預置 `AGENTS.md` 和外部資產。[完整官方流程](https://dev.meta.ai/docs/cookbook/one-shot-game-dev) · [G0254](ai-game-research/records/G0254.md)
- **排在技術副測而非完整遊戲名單：Voxel Sandbox。**[原任務與 live demo](https://www.mdaakibansari.com.np/articles/meta-muse-spark-1-3-voxel-sandbox)要求約六萬方塊、區塊化重建、射線挖掘／放置及第一人稱物理，技術難點強；但沒有資源消耗、敵人、任務或明確遊戲終點。[G0256](ai-game-research/records/G0256.md)
- Muse Spark 1.3 於 2026-09-02 公開，是近期一代模型，但不是 2026-10-07 可比較的全市場最新型號。重跑時要重新查型號並把型號／版本、reasoning effort、可用工具及模型自主修正方式記下；這些公開案例的價值在任務與畫面可重用，不在它們已代表今天最新模型的成績。

### Sonnet 5.5 Fortnite-style Battle Royale｜G0258（高系統重跑題種子；one-shot 待核）

- **先看原 prompt 和遊戲錄影：**[創作者收錄頁](https://jasonzhu.ai/en/prompts/claude-opus-5-5/2104779190277181699)有 445 字元英文 prompt 及約 42 秒實玩影片；任務包含第三人稱操作、瞄準／射擊／換彈、敵方 bot、武器拾取、生命／護盾、背包、小地圖、牆與斜坡建造、安全區縮小及彩色島嶼。能直接檢視的影片比只看宣傳圖更有用，但沒有 playable build 或 source。
- **為何值得重跑：**射擊、補給、建造和縮圈壓力必須共同形成一局可玩的閉環；這是一份短而高密度的 brief，可讓不同模型在使用者不追加指示、允許 AI 自主測試修正的協定下重跑。驗收時要實測建造是否生效、bot 是否可交戰、縮圈是否傷害玩家、是否能達成勝負並重新開始，不能因原 prompt 列出功能就視為完成。
- **證據界線：**curator 頁面把模型記為 Claude Sonnet 5.5、日期 2026-09-29，並轉載作者稱 one-shot／約 2h54m；這仍屬創作者申報，無法從短片核對零人工介入或所有系統。列高複雜度重跑題種子，不當已核實的一次交付 benchmark。美術已由使用者判定不合格。[完整研究紀錄](ai-game-research/records/G0258.md) · [S42 查詢與排除紀錄](ai-game-research/search/S-20261007-42-frontier-model-high-complexity-runs.md)

### Brendan Jowett 五題 UE5 對照：GPT-6 Astra × Claude Opus 5.5｜C（實玩影片；原始題目未公開）

完整紀錄：[B0049](ai-game-research/records/B0049.md) · [原始影片](https://www.youtube.com/watch?v=w4JMLjnY1xY) · [創作者說明](https://www.skool.com/brendan/new-opus-55-is-insane-for-building-video-games-full-test)

- **影片展示內容：**兩個近期模型各做五種 UE5 遊戲：2D 平台、3D 賽車、六軸太空戰、雪地生存 FPS、石巨人 Boss 戰；影片逐題播出短實玩片段，也展示工時和成本面板。它能讓你直接看模型畫面及題型，而非只看作者挑選的成品圖。
- **為何值得檢視：**五種操作型遊戲可初步比較視覺呈現與互動完成度；賽車、射擊和 Boss 戰也提供不同系統壓力。影片特別適合先判斷哪些畫面值得深入查原始材料。
- **先講清楚限制：**創作者稱每個 build 都從同一個 single prompt 起始，但五份逐字 prompt、完整 session、source／build 和獨立評分 rubric 未公開；因此不視為已核實的「一次輸入後完全無人介入」案例或可逐字重跑基準。影片未經你檢視，**五款美術均待使用者判定**，不能套用 E0008 舊作品結論。
- **目前建議：**可先看影片畫面；如有一題的視覺／玩法方向合適，再把它當研究線索，等待原作者公開 prompt，或明確標示自行重寫的新測試 brief。時間／成本細項目前僅有影音二手轉錄，不能用來下模型勝負結論。

### TIDAL RUSH — Paradise GP｜GPT-6 Astra 官方連結的互動卡丁車｜C（視覺／物理副測；one-shot 待核）

完整紀錄：[G0250](ai-game-research/records/G0250.md) · [OpenAI 官方 Astra 發布頁及作品 credit](https://openai.com/index/gpt-6-astra/) · [直接玩](https://tidal-rush-paradise-gp.skirano.chatgpt.site/) · [原始 build 畫面來源](https://github.com/MartinDelophy/awesome-gpt-6-astra/blob/main/assets/screenshots/tidal-rush/SOURCE.md)

- **值得你看什麼：**OpenAI 官方頁把它作為 Astra 互動卡丁車作品連結並標註 Pietro Schirano。公開 build 有熱帶海岸賽道、三圈、八位車手、漂移與道具、賽後結果及重賽；可直接檢查遊戲畫面、賽道可讀性與競速手感。
- **任務與系統限制：**目前可見的是短賽事循環；沒有公開原始 prompt、session／追問紀錄、source 或固定版本資訊，也未核實 AI 如何自我修正。它適合畫面／競速物理副測，不取代長流程及多系統主測。
- **美術狀態：**使用者待判定；這是新項目，不套用舊檢閱頁美術評價。社群有連按漂移導致卡丁車升空的問題回報，可當物理邊界檢查線索，不視為獨立 QA 結果。

### Slipstream｜GPT-6.1 Sol 3D 水上滑道競速｜A（自主 QA／物理副題；美術待判定）

完整紀錄：[G0143](ai-game-research/records/G0143.md) · [作者 repo](https://github.com/KJLKurt/waterslide-game-gpt-6.1-sol) · [直接玩](https://kjlkurt.github.io/waterslide-game-gpt-6.1-sol/) · [S37 來源查核](ai-game-research/search/S-20261007-37-current-model-physics-game-audit.md)

- **目前可確認的任務：**作者保存的 `progress.md` 把原委託描述為製作 mobile-first 3D waterslide racing PWA；須包括 13 名賽車手、兩條坡道、彎道與缺口捷徑、NPC 個性 AI、觸控／桌面控制、直橫屏、暫停與賽果、路徑隔離的離線快取及本機存檔。該段是作者存檔的原 prompt 摘要，非原始聊天匯出。
- **近期 run 資料：**GPT-6.1 Sol Extra-high；repo 約於 2026-09-30 建立，僅作生成日期代理。作者把 run 稱為 0-shot，progress 記錄空白起始 workspace；README 列 51 分 58 秒、49 API 呼叫、約 4.82M tokens，以及 main run＋一個 auto-review child。未公開完整 trajectory，因此「無人追問」仍是作者申報；自動 reviewer 與自行修正則符合本研究允許的 AI 自主流程。
- **系統／可玩性與測試：**Race 模式完成／摔落 DNF，Practice 有 checkpoint respawn；玩家需操作轉向、跳躍並在缺口捷徑調整落點，12 名 NPC 依不同風險／能力嘗試超車、抄捷徑及跳躍。repo 記載 Playwright Chromium 測試正式建置、桌面／觸控、坡道著陸、摔落、checkpoint、捷徑、賽果、NPC 差異、響應式版面與離線重載。測試結果與修正歷程是作者 repo 記錄，尚未由本研究獨立重跑。
- **題型定位：**值得測最新模型的 3D 路面物理、競速 AI、手機操作和自主回歸 QA 整合；規模集中在單一賽道的 Race／Practice，沒有生涯模式或長期成長，不取代 Ruinseed／DEAD SIGNAL 等完整長流程主測。
- **美術與策展分數：**美術尚待使用者判定。來源策展頁尚無 Slipstream gameplay 圖片，8.5/10 評分的是 source／mechanics／run path／tests／attribution，不是美術或 runtime 實測。新增作品不繼承使用者舊頁面美術判定。

## 優先讓使用者檢視美術的嚴格一次輸入候選

### Shift Zero — 3D 組裝展示接工廠防守 FPS｜A（美術不合格；使用者判定）

完整紀錄：[G0207](ai-game-research/records/G0207.md) · [原始任務及 run](https://adam.holter.com/tests/rifle-factory-alien-invasion/)

- **實際成品：**[直接開啟 Shift Zero playable](https://adam.holter.com/tests/runs/2026-09-04-gpt-6-astra-rifle-factory-alien-invasion/index.html)。這是一個可操作的連續網頁：往下看 AK-47／AR-15 零件分段組裝、選擇與檢視模型，再由組裝介紹轉進工廠 FPS。使用者已判定美術不合格；畫面仍可用來檢視遊戲系統與射擊流程。
- **遊戲目標：**救出工廠同伴、維持電力、抵擋三波外星人攻勢；支援移動、瞄準、射擊、換彈、切槍、跑步、跳躍、暫停及重新開始。
- **實測資訊：**頁面標明 GPT-6 Astra、Codex high effort、2026-09-04、1 prompt／1 run；作者 prompt 要求自主完成並驗證面向使用者的結果。公開[實際 build](https://adam.holter.com/tests/runs/2026-09-04-gpt-6-astra-rifle-factory-alien-invasion/index.html)和[遊戲錄影](https://adam.holter.com/tests/runs/2026-09-04-gpt-6-astra-rifle-factory-alien-invasion/published-x-2095986388663439614.mp4)。
- **任務難點：**兩段互動體驗要共用槍械資產；前段要展示 3D 零件結構、材質與組裝動畫，後段要成為能玩的 FPS；同時有開場、操作、敵人、NPC 同伴、供電目標、三波進攻、勝負與 restart。
- **證據限制：**Model test page 的「1 prompt／1 run」是作者的測試記錄，尚無可逐訊息驗證的 session transcript 或原始碼；網站目前 playable。高畫質是 task 要求，不代表成品通過；使用者已判定美術不合格。

### THE NINTH BELL（GPT-6.1 Sol Max／GPT-6 Astra Max）— 近期 3D 恐怖 Roguelike｜A

完整紀錄：[G0137](ai-game-research/records/G0137.md) · 評測方法：[Single HTML Game Bench](ai-game-research/records/B0036.md)

- **先看成品：**[GPT-6.1 Sol Max build](https://chojondocho.github.io/single-html-game-bench/codex-gpt-6-1-sol-max.html) · [GPT-6 Astra Max build](https://chojondocho.github.io/single-html-game-bench/codex-gpt-6-astra-max.html)。同場參照 [Kart Blitz](https://claude.ai/artifact/PFZaJiiXukDjHaU9Nbv65m) 及 [THE TALLOW DEEP（Opus 5.5 Max）](https://chojondocho.github.io/single-html-game-bench/claudecode-opus-5-5-max.html)。這些是同一 prompt 的不同模型產物，不應只用作者主觀排行下結論。
- **任務／協定：**所有模型收到同一段 prompt，做單檔 3D 恐怖遊戲並融合 RPG 與 roguelike。bench 公開規則明確要求 zero-shot、one-pass、不得在生成後手動調整 gameplay/system；符合「一次給任務，AI 自行交付」的限制。
- **系統難點：**第一人稱 3D 場景探索、戰鬥與防禦、角色資源、地圖／日誌、多層下降、roguelike 成長與死亡回響，需把視覺、操作、HUD、戰鬥和循環整成同一款能玩的遊戲。
- **美術界線：**研究代理實際檢視的是 Astra 版，觀察到修道院構圖、鐘主題、藍綠氣氛光、字體與 HUD 有整體設計；場景也偏暗，模型與材質簡化。使用者已判定 Sol 與 Astra 兩版美術均不合格；仍可比較其遊戲系統與成品差異。
- **限制：**作者提供的是個人主觀排序，不是正式盲測；沒有 run 時間／成本及完整 session 記錄，不能拿排行榜當作模型能力的定論。

**保留用途：**它同時有清楚的一次輸入規則、足夠深的遊戲類型、實際可玩的新模型 3D build。使用者已判定美術不合格；仍可保留為 one-shot 系統題，不列為視覺合格主測。

### Drone Backlash — GPT-6 Astra 行動射擊遊戲｜高價值重跑候選（美術不合格；使用者判定）

完整紀錄：[G0230](ai-game-research/records/G0230.md) · [App Store 成品與實際商店截圖](https://apps.apple.com/au/app/drone-backlash/id6809423584) · [作者流程說明](https://www.linkedin.com/posts/horoko_yesterday-i-built-a-game-with-gpt-6-astra-activity-7503131024671825920-OFWX)

- **玩法規模：**六個 90 秒任務、五分鐘自由巡邏、三階段合約、12 軍階、九種武器、八種敵機、武器升級與持久成長；需要整合不同敵機、彈道／瞄準方式、升級經濟、跨任務進度和手機操作。
- **成品證據：**可從 App Store 頁直接查看實際商店圖並安裝目前 iPhone 版本。它已經是可公開交付的產品；但頁面顯示上市後更新，不能用現版反推最初交付內容。
- **一次委託證據：**作者稱第一個 prompt 產生遊戲，第二則 prompt 做預告和送審。原 prompt、session trace、推理設定及首版凍結 build 未公開，所以只列重跑候選，不說成已驗證的一次交付 run。
- **視覺判定與用途：**使用者已判定美術不合格；若重跑，目的限於測試手機射擊與跨任務成長系統，不把它當視覺門檻候選。可從乾淨專案讓現行模型自行規劃、測試、修正，再凍結最後交件。

## 可重跑的獨特系統題

### DASH / DINNER — 城市外送職涯模擬｜A（系統題備選，one-shot provenance 待核）

完整紀錄：[G0209](ai-game-research/records/G0209.md) · [作者任務與模型頁](https://agentgames.dev/play/dash-dinner)

- **實際畫面：**[作者公開的可玩版](https://play.agentgames.dev/g/g_Gkna3a8DsdOR3NCL/index.html) · [2026-09-21 實際遊玩截圖](https://github.com/MartinDelophy/awesome-gpt-6-astra/blob/main/assets/screenshots/dash-dinner/gameplay.jpg)。截圖記錄的是研究員實際進入遊戲取得訂單後的第一人稱踏板車畫面，不是 AI 生成的替代示意圖；美術品質仍等你親自判斷。支援 WebGL 時應看 3D 畫面；相容模式可能切為 2D。
- **任務可重跑：**作者頁逐字提供原始 prompt；設定喜劇風格的第一人稱 3D 外送遊戲，需建立複雜城市、限時訂單、超速加成、門禁碼記憶懲罰、疲勞、宿舍睡到隔天，並讓交通工具從踏板車進階到電動自行車及可升級汽車。
- **為什麼不是簡單遊戲：**完整任務須同步處理步行與駕駛操控、城市路線、取餐／送達互動、計時與食物完整度、小費和金錢、門禁記憶、疲勞上限、每日重置、載具購買／升級及存檔；任何一環壞掉都會截斷跨日外送循環。
- **證據界線：**作者頁標 GPT-6 Astra／Codex 並稱公開 prompt 生成了它，列 Node.js tests；未提供 session transcript、明確無 follow-up 聲明、首版凍結檔或測試報告。現行公開成品不可當已稽核的單 prompt 成績；它適合作為**統一 brief 重跑**，每個新模型用同一 prompt，讓模型無人介入地自行驗證、修正後交付。

### Afterlight — GPT-6.1 Sol 九遭遇動作 Roguelite｜A（新模型輸出，先看實際遊戲畫面）

完整紀錄：[G0211](ai-game-research/records/G0211.md) · [作者任務原文及 run 資料](https://agentgames.dev/play/afterlight)

- **直接檢閱：**[玩目前 Afterlight build](https://play.agentgames.dev/g/g_5bDBTNoVMJLfPNeZ/index.html)。作者頁附的是設定 key art；它和實際遊戲畫面不同。遊戲使用程序 Canvas 2D visuals，因此請進實際 build 判斷畫面水準，不以封面圖代替。
- **近期模型：**GPT-6.1 Sol、Codex desktop、high effort；頁面列 2026-10-01、約 41 分鐘。其 $1.52 為 hypothetical Standard API text-token estimate，含 4.78M logged tokens（多數 cached）；不是實際收費。
- **遊戲系統：**三名差異角色打九場遭遇、三個 boss；每勝一場三選一取得 15 種可疊加 run upgrade；蒐集資源取得局內 cache，過關 ember 可以買永久能力；有 Sanctuary 章節、觸控支援、local save 和持續 run。
- **為何值得重跑：**作者原文要求模型自行挑選玩法、創作完成版 progression game、自行驗證戰鬥／升級／獎勵／持久化／離線，再發布；可直接用原 brief 測當前模型的系統設計和自主 QA。
- **證據限制：**公開 prompt、模型標籤與目前可玩輸出，但沒有逐訊息 session 或明確無人 follow-up 稽核；平台數據／QA 僅有作者申報。這是新近可玩參照，不是已驗證模型排行榜或已由你判定美術合格的作品。

### BioNeural — 開放選題、多人網路與部署｜A（極限工具鏈副測）

完整紀錄：[G0026](ai-game-research/records/G0026.md) · [原始委託及作者說明](https://www.reddit.com/r/ChatGPT/comments/1wqd0gg/houston_we_have_a_problem_opus_55/) · [目前可玩版](https://bioneural.de/)

- **任務規模：**原始 prompt 只要求 Three.js 線上多人遊戲、玩家輸入名字加入現有玩家、模型自行決定玩法並部署到作者網域；作者自述 Opus 5.5 Medium 在單一最多五小時 session 自主規劃、寫作、測試與上線。網站 1.0 首版列出六張地圖、破壞場景、武器、空襲／核彈、觀戰與 bots；目前版本另有後續增加的 5v5、clans、商店等內容，不應將 1.8 當初版。
- **真正考驗：**模型要自行選擇合適玩法，跨 Three.js、網路同步、房間與 bot、語音、部署／Cloudflare 與既有 hosting 工具把它完成。適合測高度開放委託的自主決策和系統整合，與固定規格的 Ruinseed／MALL ACTION 分開評分。
- **重跑條件：**作者給了完整 PC 權限和既有 Blender／PHP／Unreal／Node／FileZilla、Suno、Cloudflare 等資源。若要比模型本身，須固定工具、帳號、外部生成服務及部署目標；保留停止時首版 build。現有成品是持續更新版，作者自述流程未獨立稽核。使用者已判定其美術不合格。

### DEAD AHEAD — 物理駕駛、經濟與長程自我測試｜A（系統整合重跑題）

完整紀錄：[G0223](ai-game-research/records/G0223.md) · [原始 prompt 及可玩版](https://agentgames.dev/play/dead-ahead)

- **遊戲循環：**駕駛車輛穿越固定 seed 的殭屍荒漠長路，燃料耗盡後按距離及擊殺結算，回車庫升級引擎／變速／油箱／輪胎／車載武器，逐日推進到直升機逃生點。三種車、六條升級線、剛體懸吊、燃料、坡道／坑洞與殭屍碰撞會一起影響能否走得更遠。
- **自主 QA 題型：**作者稱使用 Node bot 玩完整經濟循環，校準約第 25 日逃脫，並修正火箭穿牆、車輛撞牆與卡住問題。Fable 5.1 Max、約 415 分鐘／10.07M tokens 是作者／平台申報；沒有 session transcript 或 first-build hash，所以是強重跑 brief，不是已證明無人介入的成績。
- **檢閱：**可直接操作目前瀏覽器 build；畫面品質不預先代你評分。

### FROM ZERO — 極短提示下的 RPG 自主設計｜A（創作自主性強候選）

完整紀錄：[G0221](ai-game-research/records/G0221.md) · [原始 prompt 與可玩版](https://agentgames.dev/play/from-zero)

- **可玩結果：**Fable 5.1／High；作者頁列 337 分鐘與 3.08M tokens。以八分鐘固定 seed 的時間循環為核心：死亡後金錢與裝備歸零但保留地圖／筆記／部分世界知識；擊敗三首領後移動重生點，繼續章節。另有夥伴、商店、投擲道具與多輪計分。
- **測試價值：**原 prompt 只給異世界轉生／《Re:Zero》題材、兔耳角色和自由創作，玩法循環與首領／保留規則由模型自行發明。它測模型把寬泛想法整理成可玩的核心系統，而非照詳細規格填空。
- **證據限制：**作者說這是「another game」「第五或第六款」，表示同一對話或工作區可能帶有前文；目前 build 為 1.6，不是凍結首版。頁面稱使用 headless Chrome 自動模擬，但無 trace／harness。適合在乾淨上下文下重跑，不能把現版直接當 verified one-shot。美術不合格（使用者判定）。

### Tank Rush — 多關坦克戰鬥的經濟平衡｜A（較窄副測）

完整紀錄：[G0224](ai-game-research/records/G0224.md) · [原始 prompt 與可玩版](https://agentgames.dev/play/tank-rush)

- 俯視坦克戰鬥有 29 個程序關卡及 endless arena；關卡需摧毀敵坦克、砲塔和 spawner，撿取硬幣後逐步提升裝甲、視野、炮塔／機動及六種武器。
- 作者所貼任務包含長 play-test loop：用可購買升級推算後續敵人耐久和傷害、維持關卡難度、修正尋路／穿牆火箭／卡住坦克、完成 loot phase。Fable 5.1 Max、101K tokens／169 分鐘及 v1.27 都是作者頁資料；沒有原始 session transcript，不能確認無人工跟進。
- 系統價值高於一般單回合射擊，但題型範圍低於長流程 RPG／多人專案；保留作重跑副題，美術不合格（使用者判定）。

## 長流程與多系統整合

### Ruinseed: The Shattered World — 長流程／系統上限題｜A（美術不合格；使用者判定）

完整紀錄：[G0134](ai-game-research/records/G0134.md)

- **玩法與難點：**程序生成連通世界、森林／濕地／峽谷等區域、三座地城、戰鬥、符印、最終 Boss 與結局；要求多 seed 可達性及約 10–15 分鐘通關閉環。
- **為何值得留：**同時測世界生成、關卡可達、敵人、戰鬥、進度與長流程完成，不會只靠漂亮標題畫面過關。這代表系統上限用途；美術不合格（使用者判定）。
- **證據／限制：**518 行 prompt；有四個模型可玩 build。Opus 5.5、GPT-6 Sol、GPT-6 Luna 作者稱一個 prompt；Astra 中途收到 continue，不符嚴格零追問條件。重跑應統一工具與時間條件。
- **來源：**[任務 prompt](https://github.com/FrostSource/8bit-ai-arena/blob/master/PROMPT.md) · [成品集合](https://frostsource.github.io/8bit-ai-arena/) · [Opus build](https://frostsource.github.io/8bit-ai-arena/play.html?game=opus)

### MALL ACTION — 長規格與雙視角切換｜A

完整紀錄：[G0092](ai-game-research/records/G0092.md)

- **玩法與難點：**六層商場、電梯／手扶梯、走廊橫向動作、商店俯視探索、敵人、包裹收集、逃脫與逐輪升難度。
- **為何值得測：**平台操作和俯視玩法切換，並連動關卡、敵人、物品與遊戲狀態；規格也涵蓋輸入、模擬、美術音訊與測試。
- **證據／限制：**488 行 prompt；有 GPT-6.1 Sol、Sonnet 5.5、Opus 5.5 等可玩分支及部分測試紀錄；各分支條件不完全一致，重跑時應固定 harness。
- **來源：**[repo 與模型分支](https://github.com/rlorca/mall-action) · [完整 prompt](https://github.com/rlorca/mall-action/blob/main/one-shot-prompt.md) · [GPT-6.1 Sol build](https://rlorca.github.io/mall-action/gpt-6.1-sol/)

### Kart Blitz — 賽車與競賽完整度｜A

完整紀錄：[G0080](ai-game-research/records/G0080.md)

- **玩法與難點：**8 條賽道、8 位車手、三種模式、甩尾加速、13 種道具、11 位 AI 對手及鍵盤／手把／觸控。
- **美術驗收：**使用者已明確判定合格（2026-10-06）。
- **證據／限制：**Sonnet 5.5 Max 單一 user prompt 後自主使用代理與 Playwright，約五小時；有 prompt、實玩影片、結果畫面與可玩 build。作者報告的測試並非獨立審核。
- **來源：**[實測文章與 prompt](https://www.nathanonn.com/sonnet-5-5-one-prompt-game/) · [遊玩影片](https://youtu.be/k7oO3ZLmPwE) · [成品](https://claude.ai/artifact/PFZaJiiXukDjHaU9Nbv65m)

### Smash Karts Arena — 多人網路、伺服器狀態與武器對戰｜A（最強系統新候選）

完整紀錄：[G0206](ai-game-research/records/G0206.md)

![作者上傳的遊玩影片縮圖；請點開影片檢視實際片段，縮圖不作遊戲截圖判定](https://img.youtube.com/vi/3laRe_z_gbI/hqdefault.jpg)

- **任務與模型：**GPT-6 Astra（Codex CLI 0.153.4）收到一則韓文 task，要求仿照 Smash Karts 做 multiplayer 3D、保留規則／道具／按鍵並查資料。模型在 2026-09-05 約 42 分鐘完成核心作品；主 trajectory 385 個事件，逐筆查到一則真正任務訊息、沒有中途 user 修改。它有 spawn 一個 subagent，child transcript 未公開。
- **系統難點：**最多八人房間、11 種武器、bot 補位、三分鐘 free-for-all、server-authoritative movement/hits/scores、WebSocket 同步、掉線恢復、排行榜、重生與下輪、鍵盤／觸控、音訊及 Discord Activity。這不是單機 kart 賽道題，而是全棧多人遊戲。
- **實物證據：**公開[遊戲錄影](https://youtu.be/3laRe_z_gbI)、[原始碼與本機啟動方式](https://github.com/amsminn/gpt-6-astra-smash-karts)、[完整主 session trajectory](https://huggingface.co/datasets/amsminn/smash-karts-multiplayer-trajectory/blob/main/traces/rollout-2026-09-05T17-40-19-01a070b9-c9b8-7d00-8cbf-8fd0416df521.jsonl)。沒有一鍵 hosted demo，需要 Node/npm 起 server；repo 的 23 項工程測試是作者報告，不代替真多人獨立測試。
- **建議用途：**如果想測模型能否交付多系統遊戲和真實多人 server，可把這題當高難度副主測。各模型要同樣能使用 server、工具、網路及多人測試者；把 AI bot 模式結果與兩個真實客戶端連線結果分開。美術仍需你看影片／本機成品判斷；它不自動取代你唯一認可的 Kart Blitz。

### OneShotGTA：Palm Bay／Golden Hour — 低多邊形畫面與駕駛物理｜A（強副測；美術勉強合格）

完整紀錄：[G0188](ai-game-research/records/G0188.md)

- **任務與難點：**小型開放城市中步行、偷車、超速駕駛、撞毀、換車，反覆完成短循環。主要壓駕駛控制、車輛物理／車損、城市可讀性和視覺完整度。
- **視覺標準與自主修正：**固定 prompt 清楚指定乾淨平塗低多邊形、強輪廓、誇張比例與暖色長陰影；並要求模型規劃、遊玩、截圖、苛刻評論、修正和重跑。作者同題公開 Fable 5.1 High、GPT-6 Astra、Fable 5.1 Extra High 及 Opus 5.5 Max build。
- **美術驗收：**使用者後續修正為勉強合格（2026-10-07）。
- **適用限制：**題目刻意沒有任務、武器、警察、行人、故事或音樂，系統廣度遠小於 Ruinseed、Fable Theft Auto。它是目前較有機會讓你先判斷美術水準的實際 one-prompt 副題，不是唯一上限主測。
- **來源：**[四個同題 build、精確 prompt 及時間資料](https://nitzan.games/OneShotGTA.html) · [Opus 5.5 Golden Hour 可玩版](https://nitzan.games/experiments/one-shot-gta/opus/index.html) · [build source](https://github.com/nitzangames/joyride)

### Fable Theft Auto 5.1 — 射擊、駕駛與城市追捕｜A（美術不合格）

完整紀錄：[G0191](ai-game-research/records/G0191.md)

- **任務與難點：**一個 voxel 城市任務串起第三人稱槍戰、換彈、劫車、駕駛／碰撞、車流／行人、通緝星與警察追捕、任務 HUD／小地圖和重生。要求單檔，城市和角色全部程序生成。
- **一次委託證據：**單作 README 明記 Claude Fable 5.1、單一非互動 turn、no follow-up、54 turns／約72分鐘、原始輸出雜湊。沒有公開充分的自主遊戲測試紀錄。
- **適合怎麼用：**它比小型 sandbox 多出多個必須彼此連動的系統，可以原 prompt 作固定題交給當前模型，允許模型在任務內自行測試修正。
- **視覺判斷：**使用者於 2026-10-06 判定其美術不合格；若仍用於重跑，只取其跨系統 brief 價值。
- **來源：**[原始 prompt 與 run 證據](https://raw.githubusercontent.com/sorrycc/fable-arcade/main/games/voxel-gta-city/README.md) · [可玩 build](https://sorrycc.github.io/fable-arcade/games/voxel-gta-city/)

### Fable Cities — 超大型城市模擬與長時自主 QA｜A（極限壓力參照）

完整紀錄：[G0193](ai-game-research/records/G0193.md)

- **任務與難點：**城市地形、天候／日夜、道路網、分區建築、車流、人口／工作／經濟、市政服務、HUD、音效與效能需整成可玩的模擬遊戲。
- **自主流程：**公開 prompt 從空資料夾開工，要求先設模組架構，再由多代理分工；headless Chrome 截圖與效能驗證、獨立評論、多輪返工和盲測都寫入工作流程。
- **目前結果：**作者明確揭露三輪視覺盲測均落敗、初次體驗 5.5/10，部分情境未達效能預算。使用者對該遊戲的美術無法確認，列為特例；不把使用者的其他判定套用至此。
- **比較限制：**屬於多代理、長時間 agentic run，不適合與單代理、短預算結果混合排名。若採為高限測試，所有模型需拿到同等代理數、工具及時間／token 預算。
- **來源：**[真實成品、截圖與 QA repo](https://github.com/rawprogress/fable-cities) · [完整 prompt](https://github.com/rawprogress/fable-cities/blob/main/PROMPT.md) · [可玩版](https://fablecities.rawscollections.com)

### 單句開放委託的三款 3D 實物 — 角色／物理、FPS、漂移｜A（適合重跑；目前三者美術均未通過）

原始紀錄：[Pelican Bike](ai-game-research/records/G0117.md) · [CrossFire: Transport Ship](ai-game-research/records/G0203.md) · [QQ Speed 3D Drift](ai-game-research/records/G0204.md)

同一個近期 Opus 5.5 repo 公開三句逐字任務、source 和可玩 build，並描述單一 session、自動測試與自主修正；未提供可獨立核對的 session transcript，所以 no-follow-up 條件屬作者自述。

- [Pelican Bicycle playable](https://claude-opus-5-5.riba2534.cn/)：短 prompt 要模型把能力用在「鵜鶘騎單車」3D 頁面。交付自行拓展為海岸騎行、動態日夜海景、追魚、布料圍巾物理、五個鏡頭、成就、合成配樂與自動巡航。偏角色／視覺／物理整合，沒有很重的勝負或長流程；使用者已判定美術合格。
- [CrossFire Transport Ship playable](https://claude-opus-5-5-cf-transport-ship.pages.dev/)：第一人稱 bot 團隊槍戰，貨輪地圖、四種武器、後座／散布、路徑 AI、計分和難度選項；適合看 FPS 系統與自動 QA，不等於多人網路對戰。
- [QQ Speed playable](https://claude-opus-5-5-qqfeiche3d.pages.dev/)：四種不同 3D 賽道、漂移回正加速、氮氣、連續 boost、AI 車手與重置；在這三款中最適合做駕駛物理與多關卡視覺一致性的副題，但仍沒有賽季／調車等更大系統。
- Repo 列 11–18 個 JS 模組、約 700–840 KB 單檔 build，作者稱模型自己做 headless 輸入、320 秒 soak test、子代理 code review 和部署修正。這些 QA/流程是 repo 內作者生成文件的說法，不視為第三方實測結果。
- **美術判斷：**CrossFire: Transport Ship 和 QQ Speed 3D Drift 美術不合格；只有 Pelican Bicycle 通過（使用者判定）。可保留各自題型交給現行模型重跑。
- **來源：**[原始碼與三句 prompt](https://github.com/chandan0000001/by_opus)

### Happy Wheels Pogo 長關卡 — 物理專項副測｜C（公開 run 證據有限）

完整紀錄：[G0205](ai-game-research/records/G0205.md)

作者稱 Fable 5 Max reasoning 以 `/goal` 單一委託做一關 Pogo stickman 遊戲，約兩小時自主工作；作者第一次完整通關約 25 分鐘，並附自己遊玩影片。此案例突出 ragdoll／車體物理、長關卡可玩性和人工長時間操作才發現的手感 bug，但未找到逐字 prompt、source 或公開可玩版；一關的窄題型也不適合作完整遊戲主測。可把它擴成物理副測：要求可測試的長關卡、速度極限／碰撞回歸、自動 bot 操作，最後凍結 build。作者的「約原作 80%」是主觀評價，不是品質分數。見[原貼與遊玩影片](https://www.reddit.com/r/ClaudeAI/comments/1u29zj2/i_have_created_a_happy_wheels_replica_oneshot/)。

### FALL LINE — 長時自主開發與反覆自我驗收｜A（視覺待檢）

完整紀錄：[G0195](ai-game-research/records/G0195.md)

![FALL LINE 的實際遊戲預覽截圖；由近期遊戲作品集保存，成品本身仍請開啟作者 build 檢閱](https://raw.githubusercontent.com/theolundqvist/frontier-games/main/media/fall-line/preview.webp)

- **玩法與難點：**大型連續雪山、自由選落點、滑雪／單板物理、雪面差異、技巧與落地評分、競速／技巧賽／自由路線、多鏡頭、天候、存檔及手把支援。
- **為何是高上限題：**原始 brief 要求 AI 自己規劃，在最多六小時內長程工作；Playwright 自動試跑、定點截圖錄影、檢查物理／FPS／console、反覆找最弱處並修正。作者公開 prompt 和可玩結果，並稱全程無人回覆或改碼，模型 339 分鐘後自行停止。
- **限制：**這是一份非常細、含明確品質與工具要求的長 brief，測「照高標完成複雜規格」而非完全自由設計；採《Steep》作玩法參照，run 預算長、實驗環境需公平對齊。作者的無人介入聲明未經第三方稽核；美術不合格（使用者判定）。
- **來源：**[實際可玩版](https://nipale-ai.github.io/opus-5-5-overnight-builds/fall-line/) · [完整 prompt](https://raw.githubusercontent.com/Nipale-ai/opus-5-5-overnight-builds/main/briefs/fall-line-prompt-as-sent.md) · [建置條件與時間紀錄](https://github.com/Nipale-ai/opus-5-5-overnight-builds)

### NOVA LANCER — 一句委託做完整 3D 軌道射擊｜A（現行 build 有後修）

完整紀錄：[G0194](ai-game-research/records/G0194.md)

![NOVA LANCER 的實際遊戲預覽截圖；由近期遊戲作品集保存，成品本身仍請開啟作者 build 檢閱](https://raw.githubusercontent.com/theolundqvist/frontier-games/main/media/nova-lancer/preview.webp)

- **玩法與難點：**三種環境串成完整軌道射擊關卡，有救援僚機、蓄力鎖定、炸彈、護盾升級、障礙與檢查點、機械海龍 Boss、成績存檔、難度及多種操作方式。
- **一次委託與自主 QA：**Claude Opus 5.5 MAX 約 100 分鐘；原始輸入只有一句要求「做一款盡可能豐富的 Star Fox 類遊戲」。作者公布 bot 和逐幀方式從頭到尾自動試玩，也公布兩個子代理與模型／工具／token 使用資料。
- **要特別區分的 build：**作者在公開後修了子彈未顯示和手機 UI bug；現在的線上版不是完全未改的原始交件。若採來比較模型，保留 AI 自主完成時的 frozen build 再評分。美術不合格（使用者判定）。
- **來源：**[實際可玩版](https://tanuu5.github.io/nova-lancer/) · [完整 run 與 prompt](https://github.com/tanuu5/nova-lancer)

### Backrooms — 第一人稱 3D 氛圍與追逐｜A

完整紀錄：[G0023](ai-game-research/records/G0023.md)

- **玩法與難點：**程序迷宮、第一人稱操作、聲音線索、怪物追逐、死亡與逃脫；可測 3D 場景、音效、敵人感知及完整逃脫流程。
- **證據／限制：**有共同 prompt、五款模型 build、實際圖片與作者遊玩影片；作者稱一個 user prompt、不追問、不重跑。Claude 與 GPT 使用不同原廠 coding agent，沒有統一數值品質 rubric。
- **來源：**[實測文章、prompt 與影片](https://www.aiformortals.co/blog/sonnet-5-5) · [Sonnet build](https://www.aiformortals.co/builds/backrooms-sonnet-5-5)

### Armor Alley — 即時空戰與地面戰線｜B

完整紀錄：[G0018](ai-game-research/records/G0018.md)

- **玩法與難點：**駕駛直升機與偵察／攻擊／空降，同時調度資源、生產地面部隊並保護運補車；飛行、補給、生產、地面 AI、雷達 HUD 和勝敗條件同步。
- **證據／限制：**GameASG-Bench 有完整規格與行為測試介面；可用原作畫面理解玩法，但未確認近期 AI build 圖廊。官方單檔交付與測試介面是額外工程要求。
- **來源：**[完整遊戲規格](https://github.com/areal-project/GameASG-Bench/blob/main/task/armor-alley/game-spec.md) · [任務／測試](https://github.com/areal-project/GameASG-Bench/tree/main/task/armor-alley) · [原作示範](https://www.schillmania.com/content/entries/2013/armor-alley-web-prototype/)

## 多模態資產作品與角色成長遊戲

### NEON WARDEN／VESPERA — 大型 3D 多模態遊戲製作｜A（工具鏈案例；美術不合格）

完整紀錄：[G0100](ai-game-research/records/G0100.md) · [G0168](ai-game-research/records/G0168.md)

- **玩法與難點：**Fable 5.1 與 GLM-5.3 依同一份開放式 3D 遊戲 prompt 產生兩款完整作品；公開 build、畫面、成本／時間／token 資料與自動遊玩證據。
- **適用情境：**直觀看 AI 能否串起遊戲程式、美術、動畫／影片、音樂與測試工具，適合評估整套 agent＋工具鏈的上限。
- **限制：**兩個 run 使用 RTX 5090、Blender、ComfyUI 及圖像／影片／音樂生成工具；不能當作隔離裸模型或公平單模型比較。需要相近的多模態資產工具環境才能重跑。
- **來源：**[Fable／NEON WARDEN 原始專案](https://nipale-ai.github.io/fable-5-1-one-prompt-game/) · [GLM／VESPERA 原始專案](https://nipale-ai.github.io/glm-5-3-one-prompt-game/)

### Diablo-style ARPG — 程序地城、角色成長與自動通關｜B（重跑題目）

完整紀錄：[G0049](ai-game-research/records/G0049.md)

- **為什麼值得重跑：**任務把城鎮、四層隨機地城、五種敵人行為、技能／升級、掉落詞綴、商店、存檔、死亡懲罰與多階段 Boss 接成完整 ARPG 循環；還要求 agent 自動打通 Boss、修錯並校準玩家通關時間。可同時測遊戲系統、狀態一致性、平衡與自主 QA。
- **實物證據界線：**作者公開 Opus 5.5、Fable 5.1、GPT-6 Astra、Sonnet 5.5 的實際 build 截圖與 run 時間；頁面卻標示至少 Sonnet 成品是 native app、沒有 web version，其他分支也未提供明確 playable 連結。因此這是規格強、適合用現行模型重跑的題目，不能說成已有可直接驗收的四個可玩成品。
- **一次委託證據界線：**文章說 run 在早期一輪，未像後來測試明確承諾零追問、不重跑；strict no-follow-up 尚待補證。新跑時應由你各模型只送出同一段任務，允許模型自行規劃、測試及修正，最後只驗收凍結 build。
- **美術：**下面所列皆為 AI build 實際截圖，可用來先看大致呈現；沒有任何一張被你確認達標，也不能替代遊玩驗收。

![Sonnet 5.5 生成的 ARPG build 實際截圖](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/diablo-arpg-sonnet-5-5.jpg)
![Opus 5.5 生成的 ARPG build 實際截圖](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/diablo-arpg-opus-5-5.jpg)
![Fable 5.1 生成的 ARPG build 實際截圖](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/diablo-arpg-fable-5-1.jpg)
![GPT-6 Astra 生成的 ARPG build 實際截圖](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/diablo-arpg-gpt-6-astra.jpg)

- **來源：**[精確任務與 build 圖片](https://www.aiformortals.co/built-by-pat/build-a-diablo-style-action-rpg-5koom8) · [早期測試的流程說明、模型／時間／token／成本](https://www.aiformortals.co/blog/sonnet-5-5)
## 3D 物理與技術副測

### NEON BAY — 程序城市與駕駛物理｜A

完整紀錄：[G0099](ai-game-research/records/G0099.md)

- **玩法與難點：**約 310 個路口的程序城市、交通燈、車流、行人、警察追捕、七款車；固定步進剛體、懸吊、輪胎模型、ABS/TCS、車輛碰撞和道路橋梁生成。
- **證據／限制：**Opus 5.5 作者稱 Claude Code 單一 task 約 70 分鐘，並有自動駕車測試和修正紀錄；repo／build 可查。沒有外部盲評。僅有駕駛，沒有徒步、任務、音訊或存檔。
- **用途：**有實物和自主 QA 證據的物理副主測；不代表長流程冒險。
- **來源：**[repo 與 build log](https://github.com/L1vsun/NEONBAY) · [可玩版](https://l1vsun.github.io/NEONBAY/)

### SUNBREAK — Downhill Club — 風格化 3D 越野競速與技巧物理｜B（視覺／物理副測；one-shot 流程待核）

完整紀錄：[G0214](ai-game-research/records/G0214.md)

![SUNBREAK Downhill Club 實際遊戲畫面；來源 repo 與策展者說明標為可玩場景截圖](https://raw.githubusercontent.com/Imirushik/sunbreak-downhill-3D-game/main/media/SUNBREAK-showcase-poster.jpg)

- **玩法與視覺：**2.3 公里程序化 cel-shaded BMX 下坡賽，三名 AI 車手競賽；有地形雕刻、車手姿勢動畫、懸吊／抓地／跳躍／七種特技、雨天、粒子特效、boost、ghost 與回放。作者 repo 開源，並列 10 項瀏覽器玩法／特效檢查。
- **為何值得看：**它把畫面風格、長距離場景、車手動畫、物理、AI 路線與終點回放整合在同一趟完整賽事。與 kart 題不同，重點是高速下坡地形和技巧落地；但內容仍集中在單一 race loop，較適合作視覺／物理副測，不取代長流程主測。
- **證據界線：**作者貼文直接歸因 GPT-6 Astra，repo／實際 screenshot 可查；沒有原始任務文字或 session，所以不能說已證實是一次委託、零 follow-up。作者未提供官方 hosted build；[這個可玩版本](https://tikgame.org/game/sunbreak/)由第三方從開源碼建置，並非作者發布版本。策展者手動畫面 8.9/10 是第三方觀感，不是你的評分。
- **來源：**[作者 repo](https://github.com/Imirushik/sunbreak-downhill-3D-game) · [作者模型歸因貼文](https://x.com/Im_IrushiK/status/2096280064019353891) · [非官方遊玩鏡像與說明](https://tikgame.org/game/sunbreak/)

### Tumble — 物理建造與工具編輯器｜C

完整紀錄：[G0163](ai-game-research/records/G0163.md)

- **玩法與難點：**自製 180Hz 物理、連續碰撞、100 顆 marble 壓力、15 種互動元件、編輯器、undo／redo、demo 與 puzzle。
- **證據／限制：**任務規格很具體，適合物理專項；尚未核實可重跑的原始 prompt 與模型可玩 build，不列成品比較主題。
- **來源：**[任務分析與比較文章](https://promptslove.com/blog/claude-opus-5-5-vs-gpt-6-astra/) · [影片](https://youtu.be/cwGSDctKCbk)

## 正式任務規格：可作為共同題目重跑

**方法參考（不列上限候選）：**ProfIQ Summer Coding Challenge 2026 的正式規則核實了單次 prompt、agent 同 run 自主測試修錯、提交工具／模型設定和原始 build、評審以乾淨瀏覽器驗收，以及主辦方同 prompt 重跑。由於它限 minigame、60 分鐘和單檔，而且 20% 總分評 prompt 品質，不宜用其名次當模型遊戲能力分數；畫廊未逐件公開 prompt／模型／session。見 [E0007](ai-game-research/records/E0007.md) 與 [S43](ai-game-research/search/S-20261007-43-public-one-prompt-game-challenge-rules.md)。

目前最值得追的新增正式規格題庫是 **A2Z GameSpec-Bench**：50 份 Big GDD 平均約 26K tokens、約 84 項 outcome requirements，涵蓋互相依賴的模擬／管理、冒險、策略、RPG 和射擊系統；固定 requirement contract 用 source、scenario replay、adaptive playtest 三軸驗收，官方頁列出 9 種 agent 結果，包含 GPT-6 Astra 與 Claude Fable 5.1。論文另公開三個 GPT-6 Astra Three.js 3D build 的忠實度分數；《Sonic: Cascade Coast》和《Rocket League》各有一張標明為實際 gameplay capture 的畫面，可先供你獨立評美術：[Sonic 截圖](https://arxiv.org/html/2609.39564v1/assets/appendix/showcase/sonic_2.png) · [Rocket League 截圖](https://arxiv.org/html/2609.39564v1/assets/appendix/showcase/rocket_league_1.png)。研究觀察兩者都是簡化幾何／低多邊形呈現，這不是使用者判定；完整 GDD、contracts、source build、evaluator 仍無法下載，HF dataset 也為空，尚不能完整重跑或核實一次委託流程。詳見 [B0052](ai-game-research/records/B0052.md)、[G0283–G0285](ai-game-research/records/G0283.md) 與 [S76](ai-game-research/search/S-20261007-76-a2z-gamespec-bench-artifacts-and-release-audit.md)。

已有可重跑庫各補不同缺口：**GameCraft-Bench** 有 140 款完整 Godot 任務、agent 操作回放和隱藏多模態 rubric，較適合從中挑高系統 2D 題；**GameASG-Bench** 有 47 款 browser-native 任務、明確的狀態／輸入契約及隔離測試器，較適合嚴格核對遊戲行為。GameCraft 公開模型 run 仍沒有 GPT-6.1 Sol／Sonnet 5.5／Opus 5.5；GameASG 的現有論文結果也尚未覆蓋這些較新型號，因此都值得重跑。除了 Airship Trader／Armor Alley，GameASG 的 **Fast Food Tycoon** 是 3D 商業模擬副主測：玩家搬運與服務的經濟閉環、員工自動化、場景擴張和資源守恆都有可執行驗收；但沒有 AI build 畫面，美術未核實。S45 逐題比較後，若優先追系統廣度，**Astroman** 是目前 3D 題庫中最廣的城市英雄壓力題，失敗風險很高；**Grand Theft Astro** 較收斂；**Tankor Arena** 是較可控的戰鬥替代題。GameCraft 實物方面，GPT-5.5 Submarine Pressure Rescue 系統分數高但官方 art41；Garden Ecosystem Keeper 的 Seele02-pro 影片官方 art85.04，是值得你親自看美術的視覺參照，仍非你的通過評價。各自任務材料、模型／分數與影音見 [S45](ai-game-research/search/S-20261007-45-benchmark-task-screening.md)、[G0056](ai-game-research/records/G0056.md)、[G0259](ai-game-research/records/G0259.md)、[G0260](ai-game-research/records/G0260.md)、[G0261](ai-game-research/records/G0261.md)、[G0262](ai-game-research/records/G0262.md)。

**WebGameBench** is a useful process match: one independent generation attempt per task/agent, about 20 agent turns, then a separate browser evaluator judges the actual delivered game. Its playability and full requirement satisfaction are separate signals. The corpus/evaluator artifact is not verified public and high-difficulty cases are few; use it to borrow evaluation protocol, not as the sole long-game upper-bound task. **Spec2Game** offers robust spec/runtime scoring but mostly small games and expressly bars runtime feedback or autonomous repair during generation. OpenGameEval tests mostly editing existing Roblox place files; JAMER's complete task pack release is not verified. See [B0043](ai-game-research/records/B0043.md), [B0050](ai-game-research/records/B0050.md), [B0051](ai-game-research/records/B0051.md), [B0053](ai-game-research/records/B0053.md), and [S40](ai-game-research/search/S-20261007-40-formal-generation-benchmark-audit.md).

GameForge Harness 提供乾淨專案、單一 solver session 及 solver 看不到的外部建置／輸入回放評估，可當驗收方法參考；但它自己的 Open20 brief 每題刻意是 compact 小型遊戲，不足以當上限主題，且目前列出的 solver provider 偏 OpenAI。見 [B0047](ai-game-research/records/B0047.md)。

### Call of Duty-Style Browser FPS — 角色美術、槍械手感與比賽閉環｜B（強重跑 brief）

完整紀錄：[G0201](ai-game-research/records/G0201.md)

![GPT-6 Astra 生成的 browser FPS 實際 build 截圖](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/fps-nuketown-gpt-astra.jpg)
![Fable 5.1 生成的 browser FPS 實際 build 截圖](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/fps-nuketown-fable-5-1.jpg)

- **系統難點：**rigged／skinned 角色與動畫、個別槍械後座和 ADS、hit registration、掩體 AI、killstreak、killcam、可進入的對戰地圖與完整 match 勝負流程；並限制 1080p 60fps。
- **對美術的意義：**prompt 明確禁止 primitive 拼裝人形、滑步與無動畫，要求模型保存 loadout、第一人稱、近景角色、瞄準鏡、hitmarker、killcam 六個截圖並檢視修正。比「請畫面精緻」更能測角色動畫和視覺品質。
- **證據／限制：**頁面連出的 GPT-6 Astra、Fable 5.1 圖是真實模型 build 截圖。但原文明說這題是唯一做過 follow-up passes 的遊戲，故它是**值得交給最新模型嚴格重跑的規格題**，不是已核實的一次交付案例；圖片不是 playable demo，也沒有得到你的美術驗收。
- **來源：**[完整 prompt、模型截圖和 follow-up 說明](https://www.aiformortals.co/blog/gpt-6-astra-vs-fable-5-1)

### Grand Theft Astro — 3D 城市跨系統上限｜B

完整紀錄：[G0072](ai-game-research/records/G0072.md)

步行／駕駛切換、碰撞導航、瞄準射擊、NPC、警察通緝、商店、任務進度、小地圖、死亡重生。範圍最大、失敗風險高；目前未確認 AI 成品圖廊。

**來源：**[初始任務](https://github.com/areal-project/GameASG-Bench/blob/main/task/grand-theft-astro/target.md) · [完整規格](https://github.com/areal-project/GameASG-Bench/blob/main/task/grand-theft-astro/game-spec.md)

### Ancient Beast — 六角格戰術與規則一致性｜B

完整紀錄：[G0015](ai-game-research/records/G0015.md)

管理六角格位置、回合佇列、行動資源、召喚成本、技能範圍、狀態效果和勝負；非法行動要拒絕且不污染狀態。原作可玩並有實際畫面，但原作不是 AI 輸出。主要測戰術規則，不測即時操作或 3D 視覺。

**來源：**[規格](https://github.com/areal-project/GameASG-Bench/blob/main/task/ancient-beast/game-spec.md) · [測試契約](https://github.com/areal-project/GameASG-Bench/blob/main/task/ancient-beast/tdd.md) · [原作](https://ancientbeast.com/)

### Bikini Bottom Survivor — 3D 生存戰鬥閉環｜B

完整紀錄：[G0025](ai-game-research/records/G0025.md)

玩家移動、敵人生成追擊與接觸傷害、自動瞄準攻擊、死亡掉落經驗、升級暫停及選擇、敗北和重開；高階範圍加入 Boss、任務角色、旅行、成就與存檔。未確認 AI 成品圖廊。

**來源：**[初始任務](https://github.com/areal-project/GameASG-Bench/blob/main/task/bikini-bottom-survivor/target.md) · [完整規格](https://github.com/areal-project/GameASG-Bench/blob/main/task/bikini-bottom-survivor/game-spec.md)

### Fast Food Tycoon — 3D 餐廳營運與自動化成長｜B（高系統密度任務；無既有 AI 成品）

完整紀錄：[G0056](ai-game-research/records/G0056.md)

- **初始任務：**一則 target prompt 要求交付單檔 playable browser game；AI 可自行在該任務內規劃、寫程式、測試和修正，最後使用者不需追加指示。GameASG 的公開 runner 能保存 model/harness/run metadata，並在隔離評測容器中執行行為驗收。
- **核心循環：**玩家在 3D 餐廳移動，到廚房製餐、把食物搬至櫃台、等待顧客服務、收錢，再用收入解鎖新設施和雇員。相機旋轉、方向控制、餐點容量、隊伍、庫存、資金、購買和視覺狀態都需要保持一致。
- **上限壓力：**雇員要能實際在場景工作；擴展規格含 drive-through、自助服務、rush、存檔／離線收益和 prestige。TDD 用真實輸入與狀態快照驗收，測資源守恆、不可重複領錢／升級、攝影機轉向後控制，以及場景和 HUD 的可見變化。
- **視覺界線：**沒有公開的 AI build、模型結果圖或影片。這是高系統密度的可重跑任務，不是已證明美術品質的作品；規格也沒有指定明確畫風。若你要先看畫面，必須等實際模型輸出後再判斷，不應用 reference/task 文件替代美術驗收。
- **來源：**[初始任務](https://github.com/areal-project/GameASG-Bench/blob/main/task/fast-food-tycoon/target.md) · [完整規格](https://github.com/areal-project/GameASG-Bench/blob/main/task/fast-food-tycoon/game-spec.md) · [行為測試契約](https://github.com/areal-project/GameASG-Bench/blob/main/task/fast-food-tycoon/tdd.md) · [可重跑與成績界線](ai-game-research/search/S-20261007-33-benchmark-task-release-audit.md)

### GameCraft-Bench：Airship Trader — 經濟循環與固定操作回放｜B

完整紀錄：[G0014](ai-game-research/records/G0014.md)

浮空島間交易，管理貨物、燃料與庫存、升級船艦、處理海盜；官方提供固定操作 trace 與 rubric。GPT-5.5 有公開基線，但可重跑更新模型。單 HTML／Godot benchmark 的環境條件須一致。

**來源：**[任務 brief](https://github.com/FreedomIntelligence/gamecraft-bench/blob/main/tasks/openworld-airship-trader/instruction.md) · [GPT-5.5 build](https://tongxuluo.github.io/gamecraft-bench-website/static/godot/codex55__openworld-airship-trader/index.html) · [基準頁](https://tongxuluo.github.io/gamecraft-bench-website/)

## 可作任務素材，但流程證據不足

### Claude of Duty — 長程 FPS 整合｜C

完整紀錄：[G0035](ai-game-research/records/G0035.md)

Three.js FPS，整合武器、敵人、動畫、程序資產、音訊和渲染；公開原始 prompt、repo、build。原作為 Opus 5；作者描述使用代理與視覺檢查迴圈。作者表示由單一 task 啟動，但品質評語不是盲測，最終成果未達 prompt 所稱 AAA 水準。可把原 prompt 交給新模型重跑。

**來源：**[原始 prompt](https://github.com/mshumer/Claude-of-Duty/blob/main/prompt.md) · [repo](https://github.com/mshumer/Claude-of-Duty) · [作者說明](https://t.co/xixH3xaJGH)

### LAST COURIER — 長流程 3D 配送冒險｜C

完整紀錄：[G0086](ai-game-research/records/G0086.md)

七個據點配送；載重與摔落損壞、程序地形、搭橋架梯、雨蝕、潛行敵人、資源狀態、存檔與結局。作者提到自動 bot 以真實物理跑到 ending，有 repo 和可玩版。未明確證實單一任務且全程無人工介入，不能當已核實的一次生成案例。

**來源：**[repo](https://github.com/tanuu5/last-courier) · [可玩版](https://tanuu5.github.io/last-courier/)

### BioNeural — 開放式多人遊戲自主設計｜C

完整紀錄：[G0026](ai-game-research/records/G0026.md)

原始任務將玩法交由模型自行決定；作者稱 Opus 5.5 約五小時完成多人、bot、語音、破壞物件與天候。網站後續更新，無法由目前頁面單獨還原首次交付；伺服器、網路與工具權限也會大幅影響比較。適合另外設計開放式任務，不與固定規格題混排。

**來源：**[原始貼文](https://www.reddit.com/r/ChatGPT/comments/1wqd0gg/houston_we_have_a_problem_opus_55/) · [live site](https://bioneural.de/)

### Montanha: Zero Day — 三階段 Cyberpunk 動作平台遊戲｜C（重跑 brief；原最終 build 有人類 follow-up）

完整紀錄：[G0244](ai-game-research/records/G0244.md) · [初始任務、迭代與 QA 說明](https://dev.to/tiagovilasboas/i-built-a-full-pwa-game-in-one-day-with-claude-opus-55-and-claude-code-here-is-the-real-token-41p7) · [repo 與成品](https://github.com/tiagovilasboas/montanha-zero-day)

作者公開約三句 kickoff prompt、Opus 5.5／Claude Code 的 PWA 成品、模組架構與 bot／Playwright QA。最後遊戲有三階段、cutscene、boss 和結局；不過作者曾對角色手感給 feedback，又要求把 boss 前關卡由 7 段擴為 12 段。**所以它的最終版不算一次交付成績**，而是可讓當前模型從相同初始 brief 重跑的高價值題材，並可觀察 AI 自測能否發現 boss 復活、陷阱和雷射 bug。此新作品尚未由你判定美術。

**來源：**[作者完整文章及初始 prompt](https://dev.to/tiagovilasboas/i-built-a-full-pwa-game-in-one-day-with-claude-opus-55-and-claude-code-here-is-the-real-token-41p7) · [可玩 PWA](https://tiagovilasboas.github.io/montanha-zero-day)

### 3D Mini Golf — 碰撞物理與球洞解法｜C

完整紀錄：[G0003](ai-game-research/records/G0003.md)

Opus 與 Fable 有各自九洞 playable build，含物理求解／碰撞測試材料；題型適合 3D 碰撞與關卡可解性。原始共同 prompt 和執行條件不完整，不列已核實的一次任務結果。

**來源：**[Opus repo](https://github.com/leonvanzyl/3d-golf-opus) · [Fable repo](https://github.com/leonvanzyl/3d-golf-fable) · [比較影片](https://chooseto.ai/watch/NzyP4VjkrvM)

### Rubberhose Ruckus — 程序美術與分階段 Boss Rush｜C（高價值開放式重跑題；原 run 使用專用平台）

完整紀錄：[G0237](ai-game-research/records/G0237.md) · [作者原始起始 prompt／約九小時 run 自述](https://www.reddit.com/r/aigamedev/comments/1v9bqzx/ai_made_platformer_trying_long_horizon_prompting/) · [官方可玩成品](https://tesana.com/game/rubberhose-ruckus)

單一短 prompt 要求 1930s 橡皮管動畫風格的 2D boss-rush shooter、分階段 Boss、彈反、精準 hitbox、程序墨水質感和爵士音樂；作者稱交給 Tesana LOOP 後約九小時無人看管。貼文還稱成品有三名 Boss、合作模式和約兩小時的熟手流程。它的自主建置範圍和視覺目標值得重跑，官方可玩頁及原作者影片可供檢視。原 run 精確底模／首版版本／自我 QA trace 未公開，且 Tesana 每次自選底模，不能直接拿作不同通用模型的公平成績。把原 prompt 放到同一套可鎖模的 agent harness 裡重跑，才適合做模型比較。使用者已判定此作品美術勉強合格；畫素解析度不足由其美術設計補足。

**來源：**[Tesana LOOP 官方流程](https://docs.tesana.ai/building/loop-mode) · [Atomos／模型更新](https://tesana.com/changelog)

### OpenGame：公開 single-prompt demo gallery 與固定 agent harness｜B（可用任務與工具重跑；完整 benchmark 未釋出）

完整紀錄：[B0029](ai-game-research/records/B0029.md) · [官方 repo：framework、prompt、live builds、source archives](https://github.com/leigest519/OpenGame)

OpenGame 已能從空白遊戲資料夾接收單一 prompt，在固定 template／debug／browser QA 工具下自行產生並修到 playable，模型可由 OpenAI-compatible endpoint 替換。Repo gallery 放有多階段、多角色動作遊戲及 quiz fighter、塔防等不同 prompt 和 live build，可從中選出原創化後的高密度任務，讓不同模型共用同一 agent harness 重跑。這測的是「指定工具＋模型」端到端能力，不是裸模型；公開 150 prompt evaluation set／evaluator 仍未確認釋出，而且 gallery 不標各 build 的底模版本與 trace。新增 gallery 作品尚未有使用者美術評價。

**來源：**[OpenGame 論文](https://arxiv.org/abs/2604.18394) · [OpenGame-Bench 紀錄](ai-game-research/records/B0029.md) · [S23 搜尋批次](ai-game-research/search/S-20261006-23-agent-platforms-opengame-and-world-benchmarks.md)

### 其他暫不列入主測的題材

- **Bastion／BASTIÓN MECHA：**機甲戰鬥、城堡資源與建造有實際成品；有人工遊戲設計／HUD 美術介入，缺原始 prompt 與完整 run log。作系統參考。[來源](https://lambdaforge.itch.io/bastion)
- **Crazy Tanks — Wild Tides：**可破壞島嶼、坦克物理、風向、武器和地形災變，設計種子很強；現有規格為重建版本，沒有核實 AI build。[來源](https://www.tripo3d.ai/3d-prompts/crazy-tanks-3d-island-artillery)
- **Tiny Necromancer：**塔防／建造、骷髏工作配置、資源與三階段 boss；由多模型協作，沒有獨立 one-task prompt/session 證據。[成品](https://dylanh.itch.io/tiny-necromancer)
- **Opus 5.5 三款 FPS／漂移車／單車 demo：**有 playable source 和作者驗證說明，但各自範圍較中型，作短任務參考，不及主候選的系統廣度。[repo](https://github.com/riba2534/claude-opus-5-5-demo)
- **Sunward（GPT-6 Astra）：**Unity 開放世界賽車與原始碼有相當系統密度，但作者說明現行版來自互動開發，電台、Photo Mode、測試與發佈包裝是初版之後追加，且明言 graphics／handling 可再改。沒有精確 prompt 或 no-follow-up 證據；不列嚴格一次交付或美術候選，只保留作賽車題目設計參考。[G0213](ai-game-research/records/G0213.md) · [實際駕駛截圖](https://github.com/yjrocks712/Sunward-by-GPT-6-Astra/blob/main/docs/images/driving.png)
- **HEADQUARTERS（GPT-6 Astra）：**六章 run-and-gun、4 角色、56 敵人及 12 個 Boss，系統規模大並有實際遊戲截圖；但作者先寫 141 KB design bible、另補故事文件及六輪 feedback，排除 one-shot。[G0215](ai-game-research/records/G0215.md)
- **其他近期線索：**[Opus 5.5 town-defense RPG](ai-game-research/records/G0218.md)有任務文字但無 playable／repo 且給了參考圖；[Street Heat](ai-game-research/records/G0216.md)只有二手玩法摘要，缺原 prompt／build；[Simpsons Hit & Run browser reconstruction](ai-game-research/records/G0217.md)依賴原作資產並有後續人類指示；均不列一次委託強候選。
- **Chainmate — 3D 棋類 roguelite：**三幕九戰、Boss、分支事件、棋子成長與 18 種 relic，有實際可玩版；但作者提供四張參考圖後又回覆過燈光意見，因此不符合全程零使用者介入。[研究紀錄 G0033](ai-game-research/records/G0033.md) · [作者說明](https://www.reddit.com/r/ClaudeAI/comments/1wp8uxb/i_gave_opus_55_four_reference_images_and_build/) · [成品](https://sneid1.itch.io/chainmate)
- **GPT-6 Astra Roblox Kart Racer：**詳細 prompt 指定 Roblox／Blender／MCP、AI 車手、整場競賽與自我 playtest；尚無公開 place 或 session log 可驗收最終成果，暫不列成品候選。[研究紀錄 G0199](ai-game-research/records/G0199.md)
- **Bash Fighter — AI-agent 持續開發的 20 人線上平台格鬥遊戲：**有現行 browser／itch playable、完整 TypeScript source、server-authoritative multiplayer、deterministic 20–32 fighter simulation、bots、觀戰和大量 CI tests。repo owner 明言大部分日常 code 由 AI agent 持續完成；但沒有起始任務、模型／版本、工具紀錄、agent trace 或 no-follow-up 證據。保留為**高系統追查線索／重跑題材**，不是 one-shot 成績或 shortlist candidate。若來源釋出單一 frozen task/session，再升級研究。[G0267](ai-game-research/records/G0267.md) · [直接玩](https://bashfighter.com/) · [repo](https://github.com/Bash-Entertainment/bash-fighter)
- **夜巡录：荒庙篇（Night Patrol: Abandoned Temple Chapter）— Codex 協作的牌組 roguelike 第一幕：**公開 source 和 Windows／macOS demo 包；任務包含卡牌構築、資源連攜、地圖事件、商店、戰鬥及 Boss。作者說明最初只給模糊 kickoff，之後連續補充指示並反覆迭代數小時，另使用 GPT-Image 2.0、Seedance 與 Suno；模型精確版本、完整 session 和凍結初版未公開。最終成品明確不符 strict one-shot，僅保留為**可重跑的中高系統題目／多輪方法參照**，不作候選排名；美術已由使用者判定不合格。[G0268](ai-game-research/records/G0268.md) · [作者過程](https://toolin.ai/blog/codex-build-complete-game-in-one-afternoon) · [原始碼與 release](https://github.com/op7418/Night-Patrol) · [S56 查核](ai-game-research/search/S-20261007-56-multilingual-game-generation-evidence.md)
- **Bolt Tower — 一次 prompt 聲稱的 AI 主題塔防：**Devpost 將它列為 Bolt.new AI Coding Hackathon 的 1-Shot Prompt Challenge 作品，提供 public browser demo；波次、塔放置與升級、敵人與勝敗／重開循環比單一 arcade 小品完整。官方賽規只允許首 prompt 後修 bug、禁止加功能，但這只證明賽制要求；Bolt session link 目前須登入，精確 prompt、模型版本、凍結 build 及作者後續操作皆未核。故列為**待核副候選／中等範圍塔防樣本**，不算已確認 one-shot 成績或主測；成品未獨立通關，美術已由使用者判定不合格。[G0269](ai-game-research/records/G0269.md) · [Devpost mirror](https://r.jina.ai/http://devpost.com/software/bolt-tower) · [直接遊玩](https://bolt-tower.netlify.app/) · [官方賽規](https://worldslargesthackathon.devpost.com/rules) · [S59 查核](ai-game-research/search/S-20261007-59-bolt-tower-devpost-run-verification.md)
- **MathBombs 與 CosmicTacToe — One-Shot Hackathon 遊戲（低範圍排除）：**兩款都在 Bolt One-Shot 名錄並有 browser link；MathBombs 是算術打炸彈單循環加難度／速度設定，CosmicTacToe 是 stylized classic tic-tac-toe。前者有 one-shot bonus-prize 標籤，但都沒有 prompt／model/session 且遠低於上限所需的系統／內容複雜度，只登錄範圍排除、不進候選短名單。[G0270](ai-game-research/records/G0270.md) · [G0271](ai-game-research/records/G0271.md) · [S60 roster 紀錄](ai-game-research/search/S-20261007-60-bolt-one-shot-winners-and-game-submissions.md)
- **PATCH Territory Capture：**有 GPT-6 Astra playable 和精確 prompt，但主要是單一圈地街機循環，低於本次高上限門檻。[研究紀錄 G0200](ai-game-research/records/G0200.md) · [成品](https://agentgames.dev/play/patch)
- **Descente：**roguelite／程序美術／200 多場 bot QA 很強，但作者中途留言三、四次，排除嚴格一次委託。[研究紀錄 G0196](ai-game-research/records/G0196.md)
- **Sky Reach：**概念為無縫星球／太空，但未確認完整可玩 build、source、目標任務與自主流程。[作者貼文](https://www.reddit.com/r/aigamedev/comments/1wrstzo/i_remade_no_mans_sky_with_opus_55_threejs_on/)
- **MACH RUN：**一提示只做出視覺、谷地與飛行物理；完整遊戲其後花數週完成，不符合一次交付條件。


## 補充方法參考：V-GameGym（S72）

[V-GameGym／SKYLENAGE-GameCodeGym](ai-game-research/records/B0041.md) 提供 Pygame 短題生成與截圖／影片評分程式；現行 HF 發布含 requirements／seed code，但不含 metadata 引用的全部 generated media。其自動視覺分數衡量畫面完整、UI、功能可見和 overall completion，非使用者的風格／美術判斷；題庫和榜單也不是當前高系統 3A／stylized 完整遊戲 run。因此保留作流程和短題 rubric 參照，不列主候選。
