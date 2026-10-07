# 搜尋批次 S45：官方生成基準中的高系統任務與實際作品篩選

**查核日期：**2026-10-07（台北時間）  
**研究方向：**從已確認可重跑的 GameASG-Bench 與 GameCraft-Bench 中逐題篩出真正具有高系統密度、可觀察完整遊戲輸出、又適合新模型重跑的任務。此輪不重查 corpus 是否釋出，不把 benchmark 的成品分數當成使用者美術驗收。

## 先讀索引與查重

依研究流程先讀 [研究索引](../../ai-game-one-shot-index.md)、[候選摘要](../../ai-game-one-shot-candidates.md)、[搜尋索引](INDEX.md) 及 S44。S24／S33／S44 已確認兩項正式題庫及 runner；原紀錄已有 [G0018 Armor Alley](../records/G0018.md)、[G0072 Grand Theft Astro](../records/G0072.md)、[G0056 Fast Food Tycoon](../records/G0056.md)、[G0014 Airship Trader](../records/G0014.md)。這次避免重複建檔，改逐題檢查 specification、test contract、公開遊戲輸出及現有 rubric 分數。

另讀 GameCraft-Bench 官方示範頁的當前分項成績，發現除完整 benchmark leaderboard 外，它也公開 GPT-5.5 的單題 Submarine Pressure Rescue playable build／影片，以及 Seele02-pro 和 Opus-4.7 的 Garden Ecosystem Keeper 影片／分項成績；因此這兩個現成 run 可補充成品與視覺證據，仍需明確標出模型舊、run timestamp/完整聊天紀錄不在單題卡上。

## 實際使用的查詢與來源

| 實際查找方式／來源 | 檢閱範圍及查得結果 | 判斷／入帳 |
|---|---|---|
| GitHub REST tree API：`GET https://api.github.com/repos/areal-project/GameASG-Bench/git/trees/main?recursive=1`；`GET https://api.github.com/repos/FreedomIntelligence/gamecraft-bench/git/trees/main?recursive=1` | 取得 GameASG 47 個 `game-spec.md` task path 與 GameCraft 公開 task inventory；對照 category metadata，再深入讀取 GameASG 所有 15 個標為 3D 的候選及代表性 target/GDD/TDD。 | 高系統 3D 初選為 Astroman、Fast Food Tycoon、Grand Theft Astro、Tankor Arena、William Afton Life；另比對 city-racer-x-neon-rush、Bikini Bottom Survivor、Kick Skills、Impact Pong、Colossal Runner、City Rider 等較窄玩法。新增 [G0259 Astroman](../records/G0259.md)、[G0260 Tankor Arena](../records/G0260.md)；更新既有 G0056／G0072 作相互比較。 |
| 網頁搜尋：`GameASG high-systems 3D game-generation task game-spec target TDD`；`site:github.com/areal-project/GameASG-Bench task 3D astroman grand-theft-astro tankor-arena fast-food-tycoon`；官方 repo 與各 task 的 `target.md`、`game-spec.md`、`tdd.md` | [Astroman](https://github.com/areal-project/GameASG-Bench/blob/main/task/astroman/game-spec.md) 是步行／飛行／駕車、多種能力、NPC／車流、救援／運送／追逐／搶劫／Boss 任務、商店、通緝、死亡重開共用一個 3D 城市的最高廣度候選；[Grand Theft Astro](https://github.com/areal-project/GameASG-Bench/blob/main/task/grand-theft-astro/game-spec.md) 範圍較收斂，仍要求真正 3D，不接受俯視 2D 或偽 3D；[Tankor Arena](https://github.com/areal-project/GameASG-Bench/blob/main/task/tankor-arena/game-spec.md) 有坦克操控／慣性、射擊、敵人、掩體、可破壞障礙與首領，但尺度較易控制；[Fast Food Tycoon](https://github.com/areal-project/GameASG-Bench/blob/main/task/fast-food-tycoon/game-spec.md) 讓 3D 手動生產／供餐／收款逐步接上排隊 NPC、設備升級、雇員自動化、服務分支及長期成長。 | 官方每次 GameASG run 預設單次、3,600 秒，獨立生成與 evaluation container。target 是 initial request，但模型也會讀工作區 GDD/TDD，其中有公開 `window.__gameTest` 驗收契約；整個固定資料包可視為使用者一次提交的任務 bundle，報告須寫明，不可稱「只有一段純文字 prompt」。runner 的行為分數不評使用者美術門檻。 |
| 網頁搜尋：`GameCraft-Bench tasks high system density official playable game demo model rubric`；`site:github.com/FreedomIntelligence/gamecraft-bench "Tycoon Submarine Pressure Rescue"`；`site:tongxuluo.github.io/gamecraft-bench-website "Garden Ecosystem Keeper"`；官方 repo task instruction/rubric、官方 demos 頁及引用的 playable/video links | [Submarine Pressure Rescue](https://github.com/FreedomIntelligence/gamecraft-bench/blob/main/tasks/tycoon-submarine-pressure-rescue/instruction.md) 有艙室水位／壓力／氧氣／損壞與船員決策等互相牽動系統，公開 GPT-5.5/Codex build/video 和項目分數；[Garden Ecosystem Keeper](https://github.com/FreedomIntelligence/gamecraft-bench/blob/main/tasks/tycoon-garden-ecosystem-keeper/instruction.md) 有可見園藝／生態經營閉環和兩種不同風格模型輸出，是更強的視覺校準例子。官方 Benchmark 當前範圍仍是 2D Godot，不是 3D 上限題。 | 新增 [G0261 Submarine Pressure Rescue](../records/G0261.md) 與 [G0262 Garden Ecosystem Keeper](../records/G0262.md)；前者供系統上限／新模型視覺改善重跑，後者供實際視覺輸出比較。兩者使用者美術均未判定。 |
| [GameCraft-Bench 官方 demos 與 leaderboard](https://tongxuluo.github.io/gamecraft-bench-website/)；官方任務與 rubric：`tasks/<slug>/instruction.md`、`tests/rubric.json` | Submarine GPT-5.5/Codex：整體 68.70、mechanics 90、depth 85、visuals 75、art 41。Garden Ecosystem Keeper：Seele02-pro 整體 80.23、M 90.63、D 70.76、V 80.70、A 85.04；Opus-4.7 整體 70.50、M 100、D 82、V 58、A 51。單題 demo 卡未附精確生成時間與完整原聊天逐字稿；Seele Garden 卡提供遊戲錄影，Opus Garden 卡另有可玩 build。 | GameCraft 分數是 benchmark 自有 rubric，不等於使用者美術判定。記錄維度分數而不把 art85 當「美術合格」；實際錄影／build 保留給使用者直接查看。此結果也證明分開呈現 system/perception/art 能避免單一總分掩蓋成品外觀。 |

## 篩選結果與排序

### 適合作新模型高上限重跑的任務

1. **Astroman（G0259）：**已檢視的 GameASG 3D 題中跨系統範圍最廣、最接近 3D 開放世界高上限壓力題；主要差距是許多深層功能屬 P2，且一小時上限可能導致任務範圍收縮或整合失敗。當模型差距是焦點且接受高失敗率時排第一。無 AI 作品可供展示，規格要求 readable 3D 不代表使用者會判定美術合格。
2. **Fast Food Tycoon（G0056）：**目前最完整的 3D 模擬閉環與因果狀態測試，手動操作、資源守恆、排隊、現金、場景擴張及自動化互相接續。比 Astroman 更容易看出哪些系統真正接通；是更可控的模擬型主測。無 AI build／視覺輸出，藝術未核實。
3. **Grand Theft Astro（G0072）：**真正 3D 城市、步行／駕車、射擊／商店／通緝／任務／死亡重生；比 Astroman 廣度小，仍有跨系統與導航高風險。任務文件已有明確 P1/P2 分層，對一次輸出是否保住核心循環容易驗收。
4. **Tankor Arena（G0260）：**霓虹 3D 坦克場景、戰鬥、敵人、環境破壞和首領系統；可作第三方對照題，完成機率高於城市 sandbox，但系統面較窄。沒有已核實 AI build。

### 適合直接查看現成模型輸出的案例

- **Tycoon Garden Ecosystem Keeper（G0262）：**本輪查得最值得直接對照使用者美術偏好的公開實測畫面之一，因官方模型 art 分數 85.04；模型為較舊的 Seele02-pro，而且這只是量表結果，尚未由使用者判定。它的經營與生態系統整合值得看，但它是 2D 模擬，不是整體 3D 上限主題。Seele02-pro [實際遊戲錄影](https://tongxuluo.github.io/gamecraft-bench-website/static/videos/seele02pro__tycoon-garden-ecosystem-keeper.mp4)；另有 [Opus-4.7 playable build](https://tongxuluo.github.io/gamecraft-bench-website/static/godot/opus47__tycoon-garden-ecosystem-keeper/index.html) 與 [錄影](https://tongxuluo.github.io/gamecraft-bench-website/static/videos/opus47__tycoon-garden-ecosystem-keeper.mp4)。
- **Tycoon Submarine Pressure Rescue（G0261）：**現成 GPT-5.5/Codex run 展示系統完成度相對高（mechanics90/depth85/visuals75），但 art 僅 41，是系統品質與藝術品質分離的實例，可作新模型重跑前基線。使用者可看[官方錄影](https://tongxuluo.github.io/gamecraft-bench-website/static/videos/codex55__tycoon-submarine-pressure-rescue.mp4)並[直接玩](https://tongxuluo.github.io/gamecraft-bench-website/static/godot/codex55__tycoon-submarine-pressure-rescue/index.html)。分數低不代替使用者美術判定；它不能當美術好看的參照。
- **GameCraft 的其他高系統任務：**Open-World Airship Trader（G0014）是探索／交易／燃料／海盜／升級的可玩完整閉環，現成 GPT-5.5/Codex art67、depth53；Ant Colony／WildRealm／Robot Factory 的系統耦合也強，但未在官方 gallery 找到可對照的模型成品，長循環以最多 20 秒一段的 replay trace 證明會更難。故不新增多個任務紀錄或把缺 demo 說成沒有資料。

## 排除與限制

- GameASG 的原始 `target.md` 是 initial prompt，完整 `game-spec.md` 和 `tdd.md` 同時在工作區可讀。這符合一個初始任務包、AI 自行建置的形狀，但必須如實稱為「單次任務 bundle」，不能說原始實驗完全只給一段 prompt。
- GameASG 的 3D 任務要求渲染和功能可見性，未提供使用者美術門檻級別的獨立藝術驗收。已有模型輸出前，新題美術都保持待評。
- GameCraft-Bench 的遊戲類任務是 **2D Godot**，不能冒充 3D 城市／飛行／即時大場景壓力題；它仍是完整 project、可重播輸入及隱藏 rubric 的高價值系統／交付基準。
- Submarine 的藝術量表 41，未以此取代使用者主觀驗收；Garden 的 85.04 亦不是使用者通過章。
- 無新一款已由最新模型（GPT-6.1 Sol、Sonnet 5.5、Opus 5.5）完成且公開的 one-shot build 被核實。此次成果是為既有兩個 benchmark 選出更具體的高難度重跑任務、並補入同基準中的實際模型成品證據。

## 下一個明確搜尋方向

S46 查核近期可重跑任務是否已有新的 frontier model autonomous result／first-delivery artifact：只追 Astroman、Fast Food Tycoon、Grand Theft Astro、Tankor Arena 等 GameASG 新短名單，以及 Submarine/Garden 的新模型 GameCraft run；查官方 model showcase／agent repo 的原始 task、模型完整 ID、工具設定、版本／日期、首版交付、prompt continuation 和实玩成品。若仍無 run，轉做與本輪獨立的新方向：正式 benchmark 之外的高品質原創 3D one-shot showcases，優先要求上傳 prompt、成品與一段影片。
