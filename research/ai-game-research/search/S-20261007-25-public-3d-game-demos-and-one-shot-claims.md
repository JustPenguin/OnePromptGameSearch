# 搜尋批次：S-20261007-25-public-3d-game-demos-and-one-shot-claims

**日期／範圍：**2026-10-07；正式基準之外的近期公開作品、AI game jam、3D 遊戲生成成果。特別檢查：高複雜度 3D 任務是否真的 blank-start／一則委託、是否公布模型與版本、任務資料／首版成品／建置證據是否可取得。

## 研究問題與先前查重

先讀既有 [B0038 SWE-Game](../records/B0038.md)、[B0004 AutoUE](../records/B0004.md)、[B0031 PlayGen-20](../records/B0031.md)、[G0035 Claude of Duty](../records/G0035.md)、[G0207 Shift Zero](../records/G0207.md)，以及 S22–S24 的高難度成品與 benchmark 搜尋。此輪不重查學術 task-bank 結構，而是驗證 SWE-Game 最近論文中的 brief-to-game／3D 作品能否取得，以及一般公開「AI 做遊戲」貼文是否滿足使用者的無介入交件條件。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `2026 AI coding agent game jam full game generated Unity Godot one prompt playable agent benchmark high quality model results` | 找到 game-jam 與代理生成展示線索；公開競賽常允許人與 AI 協作或數日開發，須逐條看賽規，不能把成果當成一次委託成績。 | E0008、S25 排除項 | 有賽規明訂一個初始 brief、開發者不介入，且公布模型／完整 build 時再升級。 |
| `2026 AI game development competition coding agents generated game demos Unity full project model version evaluation` | 找到 Codex Game Jam 2026 等活動頁；賽制是人類與 AI 合作、72 小時完成，未固定模型及 run 條件，不符合本研究交件協定。 | — | 不需重查，除非主辦另發布可隔離的一次委託實驗資料。 |
| `site:github.com 2026 game jam "AI agent" game generation playable Unity Codex Claude complete game benchmark` | 無找到同時具備近期模型、凍結單次交件與可檢閱高複雜 playable build 的獨立官方資料集。命中多為專案／活動宣傳，缺一項以上關鍵證據。 | — | 有公開 prompt、run transcript／commit 時間線與 build 後重查。 |
| `3D game generation coding agent benchmark playable Unity Unreal full game autonomous coding agent 2026 results` | 命中 SWE-Game 近期 benchmark 與 Code4Scene 場景生成評估。前者含 17 款 3D 參考遊戲和 brief-to-game；後者只測 Unreal 場景建構／編輯，不是完整遊戲。 | B0038、M0026 | SWE-Game 官方 task package、參考 assets/video、可玩 target 首版一旦出現，檢查能否抽出同題重跑。 |
| `"SWE-Game" "github.com" 2609.33678 benchmark`；`"SWE-Game" 247 tasks official project data download Godot`；`"SWE-Game" benchmark 41 executable reference Godot games dataset repo`；`site:huggingface.co SWE-Game 247 game benchmark` | 查閱[論文摘要](https://arxiv.org/abs/2609.33678)及[論文全文](https://arxiv.org/html/2609.33678)。論文列 41 款可執行 Godot 參考遊戲、247 任務，含 41 個 Brief-to-Game、41 個 GDD-to-Game、41 個 Skeleton Completion、83 個 Bug Repair、41 個 Godot-to-Unity；其中 24 款 2D、17 款 3D。Brief-to-Game 從短要求開始，agent 自行寫 GDD、交付 Godot 專案與功能展示；另外提供 assets、reference video（若有）與測試介面契約。沒有在以上精確搜尋找到官方 task/data repo 或可供重跑的完整任務包；只記錄「本輪未找到」，不宣稱確定未發布。 | B0038 | 取得官方 dataset、build、assets/video 或明確重現指引時，評估一款 3D 題是否能遵守相同初始資訊並直接玩。 |
| 同上，查閱 SWE-Game 全文模型表、任務介面及附錄 | 論文日期 2026-09-27；6 款 model+agent framework 組合。Brief-to-Game 最佳報告分數為 Opus 5 的 50.38，GPT-5.6 Luna 34.18，Grok 4.6 39.01；模型各自搭配不同 framework／工具，因此不是純模型單變因比較。論文描述 Beacon Relay 有三個關卡、11 個 energy cells、三類敵人、七種 device、完整流程約 6–9 分鐘；另有 DOGWALK、Terraforge 等大型 3D 例子。這些是 benchmark paper 給的任務／複雜度線索，不能冒稱該論文公開了每個模型的可玩首版輸出。 | B0038 | 找到該題原始 `statement.md`、assets/video、interface 與 target build 後，可將 Beacon Relay 評為具體重跑候選；只憑附錄任務描述不建立「已有 AI 成品」紀錄。 |
| `"Code4Scene" official project github 190 Unreal Engine cases benchmark`；查閱[論文摘要](https://arxiv.org/abs/2609.36777)及[全文](https://arxiv.org/html/2609.36777) | 2026-09-29 的 190 個 Unreal Engine 場景案例：30 text-to-scene construction、160 image-to-scene editing，並評估空間推理、場景結構與物理合理性。它沒有完整玩法閉環、任務進度或可玩的遊戲系統；只作 3D 場景能力鄰接方法參考。未找到已發布的官方可重跑 task package。 | M0026 | 若後續發布可重跑案例可研究畫面／場景評分；不因「Unreal 3D」字樣升為整遊戲候選。 |
| 查閱[AutoUE 官方 repo](https://github.com/Pluto156/AutoUE)及[PlayGen-20 Hugging Face dataset](https://huggingface.co/datasets/Pluto156/AutoUE_DataSet) | 官方 repo 稱系統產出 20 款 UE5 demo game，使用多代理、資產檢索及多項服務組成固定 pipeline。dataset 頁面可見 imagefolder、614 rows、約 19.2 GB，作者 repo 說明 demos/assets/實驗資料另於該資料集；可作成果／方法材料，但沒有從 dataset 頁面確認每款遊戲的可重建完整專案、凍結初始 prompt 和逐次模型配置。不是可直接替換任意模型的同 harness 排名。 | B0004、B0031 | 作者公開逐款 prompt、完整 project/build、可鎖單一模型且保留全程 trace 時再評估重跑性。 |
| `AutoUE PlayGen-20 3D games Unreal Engine official project github benchmark tasks demos`；`site:github.com AutoUE PlayGen-20 automated generation 3D games Unreal Engine multi agent` | 重複確認 AutoUE 固定多服務、多角色 agent 架構；找不到模型逐款單變因比較或可獨立驗證的乾淨 one-shot transcript。 | B0004、B0031 | 不新增重複遊戲紀錄；保留方法／成品集參考。 |
| Codex Game Jam 2026 itch.io 活動頁與 `Project Aegis AI game no Unity editor interaction` | Jam 規則允許 human+AI 協作與 72 小時製作；Project Aegis 為開發日誌類宣稱，未提供足夠模型版本、凍結初始任務／session 與產品評估證據。兩者均不作一次交件成績。 | — | 除非另有原始 transcript、模型版號和凍結成果，否則不再追。 |
| `GameEngineBench UE5 C++ 110 tasks benchmark` | 找到的題庫偏 UE5/C++ 工程修補／功能增量，沒有從空專案生成完整遊戲，不符合本研究核心。 | — | 若研究「遊戲工程 agent」另開方向，不納入目前推薦候選。 |

## 結論與更新去向

- 更新 [B0038 SWE-Game](../records/B0038.md)：明確記錄這是近期含真正 brief-to-game 任務與 3D reference games 的高價值研究基準，但模型/framework 混雜；完整 task package 和指定範例輸出在本輪尚未找到。不可把 50.38 分或論文遊戲規模當成現成可玩的 AI build。
- 更新 [B0004 AutoUE](../records/B0004.md) 與 [B0031 PlayGen-20](../records/B0031.md)：保存當前官方 repo／資料集實際可見內容、固定 pipeline 限制，不重複建項。
- 新增 [M0026 Code4Scene](../records/M0026.md)：只保存 Unreal 場景能力方法線索並清楚排除完整遊戲候選。
- 暫不新增 Beacon Relay 的 G 紀錄：目前取得的是論文 task/GDD 描述，未確認任務資產包或模型輸出 build；待任務包或真實 build 可查時再拆成具體重跑題。
- Codex Game Jam、Project Aegis、GameEngineBench 保留為有明確排除理由的查找結果，不列入候選。
- 本輪沒有找到較現有候選更強、又具備可直接檢閱實際成品及清楚單次委託證據的新推薦；因此未改精選候選排序。下一方向轉向釐清 SWE-Game task package 是否可取得及其可視化輸出，再查可公開重跑的 3D 自主生成任務。
