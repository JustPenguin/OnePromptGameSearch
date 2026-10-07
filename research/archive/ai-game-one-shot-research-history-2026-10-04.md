# AI 一次提示生成遊戲：案例與基準研究

**原始更新日期：** 2026-10-04（Asia/Taipei）  
**狀態：** 歷史封存；保留原始研究內容供追溯，不再追加新資料。  
**研究問題：** 如何用公開、可追溯、足以測試能力上限的遊戲生成案例，公平比較不同 AI 模型？

> 封存說明（2026-10-06）：本檔保留當時完整底稿與查詢歷史。最新評選結論請看 [研究索引](../ai-game-one-shot-index.md)，目前候選與證據狀態看 [候選名錄](../ai-game-one-shot-candidates.md)，之後新增查詢寫入 [研究紀錄與去重索引](../ai-game-one-shot-research-log.md)。本檔開頭的歷史推薦可能與現行排序不同，以研究索引為準。

### 候選短名單與目前建議（2026-10-04；依使用者澄清修訂）

**評選標準修正：**使用者將自行用同一題比較不同模型；因此「公開來源是否已做多模型對照」不是候選門檻。主要標準是任務能否測出一次使用者委託後的自主完成上限：系統深度、長流程閉環、生成／測試／修正能力，以及是否有可信的實際成品或可核對任務可供檢閱。舊模型成品只作題目範圍與歷史參考，不會因此排除重跑題。

1. **完整冒險、長流程整合主測：**[Ruinseed: The Shattered World](https://github.com/FrostSource/8bit-ai-arena/blob/master/PROMPT.md)——518 行 prompt 要求程序生成連通世界、三座地城、不同 seed 可達性驗證、戰鬥與 Boss，並有 10–15 分鐘通關閉環。先前排序過度倚重已有同題模型數量；按使用者澄清，Ruinseed 是目前最值得優先放到現行模型上重跑的高上限題。
2. **雙視角動作與狀態切換：**[MALL ACTION](https://github.com/rlorca/mall-action)——488 行規格，六層商場、橫向動作與店內俯視探索、敵人、道具、程序美術／音效與完整逃脫循環；現有新模型分支是額外參照，非入選理由。
3. **賽車物理與競賽完整度：**[Kart Blitz](https://www.nathanonn.com/sonnet-5-5-one-prompt-game/)——單次 user prompt 後由 Sonnet 5.5 Max 自主分派代理、Playwright 測試修正並交付；8 條賽道、AI 車手、道具、三種模式及多種操作方式。這是單模型實測且足以顯示高完成度的題材，不需等待更多模型先跑過。
4. **經濟循環與客觀回放：**[GameCraft-Bench Airship Trader](https://github.com/FreedomIntelligence/gamecraft-bench/blob/main/tasks/openworld-airship-trader/instruction.md)——交易、燃料、船隻升級、海盜與固定操作 traces/rubric；舊版 GPT-5.5 只是可檢視的基線，重點在題目與驗收法可重用。
5. **第一人稱 3D 氛圍與追逐：**[Backrooms 五模型案例](https://www.aiformortals.co/blog/sonnet-5-5)——程序迷宮、音訊線索、敵人追逐與逃脫；做 3D 氛圍副測很有用，長流程系統寬度較 Ruinseed 窄。

Armor Alley 也應列為強候選，但證據標籤要和其他題區分：其公開內容有高系統題規格與瀏覽器行為測試，也可用原作實際畫面理解玩法；目前缺近期 AI 生成 build 圖廊，故模型成品的視覺實證弱於 Ruinseed、MALL ACTION、Kart Blitz 和 Backrooms。這項限制影響「公開成品證據」，不影響它作為最新模型重跑題的上限價值。

**對應檢閱版：**[ai-game-one-shot-review.html](../ai-game-one-shot-review.html)。以同一 user task 啟動後，允許 agent 自主使用工具、測試與修正；只驗收最後交付的 build。若要估穩定度，再增加獨立 run，而不是要求 agent 不得自我修正。

**新增的高難度 showcase 題型線索：**Slapjam AI 48 小時遊戲 jam 的 [Tiny Necromancer](https://dylanh.itch.io/tiny-necromancer) 與 [Bastion](https://lambdaforge.itch.io/bastion) 展示塔防／資源管理／基地建造／Boss 循環如何組合成短篇完整遊戲；兩者都是近期可在 itch.io 直接玩的作品，但缺逐字 prompt、模型對稱跑次與受控工作紀錄，不納入成績比較。它們值得作為下一版固定長 prompt 的機制素材庫。另有作者可追溯的 [Chainmate](https://sneid1.itch.io/chainmate) 棋類 roguelite（Opus 5.5、四張參考圖加短回饋）適合視覺與戰略 RPG 範例，仍非 strict one-shot。

### 2026-10-04 最新核查：GameCraft-Bench 的 Airship Trader

- 官方網站、GitHub README、精確任務指示、demo gallery 和 raw rubric / reference solution 已交叉核對。Airship Trader 的 replay protocol 是 1280×720、30fps、每段最多 20 秒、最多評 10 個依檔名排序的 traces；正式 replay 可作同一成品的固定互動檢查。這些資訊可支持「一次 user task、agent 可自行工具迭代」測試，但本身不代表 strict first-output。
- GPT-5.5 / Codex 的 Airship Trader build 是唯一在官網看到的該任務模型成果，分數 60.40；它可在瀏覽器直接遊玩，也提供官方 build 的[截圖](https://tongxuluo.github.io/gamecraft-bench-website/static/godot/codex55__openworld-airship-trader/index.png)。目前榜單其他模型有 Opus 5、Fable 5、GPT-5.6-sol、Kimi-K3、Seele02-pro 等，但沒有同一 Airship Trader 任務的多模型對照，也沒有 GPT-6.1 Sol 或 Sonnet 5.5 的公開 run。榜單列模型日期截至 2026-07，故不能當作 10 月最新模型的成績。
- **重要可重現性修正：**基準介紹稱 judge 使用 hidden task rubric，但目前公開 GitHub 任務目錄同時可見 `tests/rubric.json`、`tests/test.sh` 與 `solution/solve.sh`。因此「隱藏評分」只可指公開 benchmark 的官方執行隔離方式，不能說原始碼公開後 rubric 仍對重跑模型保密。重跑時把模型隔離在乾淨工作區，只提供 `instruction.md`、固定工具和素材；不要把 tests、rubric、reference solution 或舊 build 掛給它。評估者可依公開 rubric 重播，也可另加事前固定的人工盲評。這比原先文件所寫「hidden rubric」精確。
- **選擇建議微調：**Airship Trader 仍是固定規格、完整系統及可重播驗收的強候選；但它不是最新模型同題比較，也不是 strict first-output。若目標是先看高難度實測成品並把同一題交給最新模型重跑，Backrooms 比已有 roster 的 Diablo 更合適；Diablo 作角色成長／掉寶系統的第二題。若要轉成固定 benchmark 環境，Airship Trader 適合 agentic one-prompt 口徑，不能和一次無回饋輸出混榜。

### 2026-10-04 增補：3D 物理關卡同題比較

- [影片與作者說明](https://chooseto.ai/watch/NzyP4VjkrvM)記載 Claude Code 用相同 prompt 建置 3D browser mini golf，對比 Sonnet 5.5、Opus 5.5、Fable 5.1；影片包含三款遊戲的實際操作、風車與恐龍球洞。作者提供 prompt、source 與 playable builds 的 Skool 入口，但目前公開頁本身沒有直接逐字 prompt、三款 build 清單或各模型耗時／成本表，因此來源可供看實測，尚不足以獨立重跑完整原始比較。
- 已核實的公開模型成果：[Opus 5.5 的 9 洞 Adventure Mini Golf](https://github.com/leonvanzyl/3d-golf-opus)及[Fable 5.1 的 9 洞 Puttopia](https://github.com/leonvanzyl/3d-golf-fable)都有可玩部署、可讀源碼和多種障礙。Opus build 含風車、海盜灣、彈珠台、冰面、恐龍尾巴、輸送帶／升降皮帶、loop 與 portal、熔岩跳躍；Fable build 有風車、海盜、冰面、恐龍、熔岩、輸送帶、擺錘／portal、低重力 loop。兩者都含九洞記分、輸入控制、重開／選洞、存分。
- 兩份 repo 都描述自製球體物理與關卡碰撞；Opus 使用固定 1/480 秒子步進，含坡度、反彈、移動表面、傳送門與杯口漏球；`npm run verify` 以真實遊戲物理逐洞搜尋解，並檢查地形穿插。Fable repo 有 headless bot 驗證九洞在桿數限制內通關，並以亂數射擊測碰撞穿透。這些驗收材料使它成為目前清單中罕見有實際物理／可通關自動檢查的 3D 遊戲輸出。
- **定位：**適合作為高難度 3D 物理／關卡副測，或借其 9 洞+自動求解／碰撞 fuzz 思路編自己的固定題。它比 Diablo ARPG 少經濟、角色養成和敵人 AI；比 Airship Trader 更重視 3D 幾何／連續碰撞。作者宣稱同 prompt，但未證明每模型各只收一則訊息、工具迭代是否相同，且 Sonnet repo/build 在本輪未能從公開 GitHub 確認；所以不能把影片當作嚴格公平 one-shot 排名。

### 2026-10-04 增補：PUBG 風格同 prompt 對照與 One Shot Challenge 核查

- [Yuzzy Itaba 的原始 LinkedIn 貼文](https://www.linkedin.com/posts/yuzzy_opus-55-vs-gpt-6-astra-both-built-a-activity-7508532020268998657-q7Fg)公開描述 Opus 5.5 與 GPT-6 Astra 各用一個 prompt 建立 browser PUBG-style 遊戲。貼文列出 Opus 版本的 2 km 島、8 個城鎮、可進入建築、24 個會搜物資／找掩護／交戰的 bots、30 個 mocap 動畫、槍聲，以及武器／護甲／空投飛機；Opus 約 10 小時，Astra 不到 3 小時，聲稱 Astra 有 20 個通過的 tests。這比常見單關 demo 更能壓地圖、NPC、拾取裝備和 battle loop 的整合。
- 這篇仍只算**高價值展示線索**：主文只概要描述 prompt，沒有逐字任務文字、模型精確設定、兩個公開可操作 build、source、20 tests 清單或盲評；Opus 可使用 Scenario MCP 生成素材（Gemini 3.1 Lite 圖像、Tripo 3.1 3D），Astra 用免費資產庫，工具和資產條件不對稱。其發布時間搜尋頁僅標約一週前，不能據此精確標日。只有取得逐字 prompt、build / source 和兩方實際 run evidence 才升級成可重播比較。
- 本輪重新打開 [One Shot Challenge 官方規則](https://1shotchallenge.ai/)和[benchmark 結果](https://1shotchallenge.ai/benchmark)：證實 2026-07 的 200 runs 是伺服器端單模型呼叫、無編輯／重試，含 141 個可玩輸出和失敗率、token、時間資料；但每位投稿者自選 prompt，模型／題目不均，而且評審沒有公開逐項 rubric。底稿原本列過它，現已補上 integrity 機制與「可借方法，不可當固定題模型排行榜」的明確界線。

### 2026-10-04 新增優先候選：Backrooms 五模型盲測

- [Pat Simmons 原始文章與逐字 prompt](https://www.aiformortals.co/blog/sonnet-5-5)於 2026-09-29 發布，提供 [Sonnet 5.5](https://www.aiformortals.co/builds/backrooms-sonnet-5-5)、[Sonnet 5](https://www.aiformortals.co/builds/backrooms-sonnet-5)、[Opus 5.5](https://www.aiformortals.co/builds/backrooms-opus-5-5)、[Fable 5.1](https://www.aiformortals.co/builds/backrooms-fable-5-1)、[GPT-6 Astra](https://www.aiformortals.co/builds/backrooms-gpt-6-astra)五個 browser build 和同題截圖；文章也連到作者 46:21 實測影片。五個模型[Sonnet 5.5](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/backrooms-sonnet-5-5.jpg)、[Sonnet 5](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/backrooms-sonnet-5.jpg)、[Opus 5.5](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/backrooms-opus-5-5.jpg)、[Fable 5.1](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/backrooms-fable-5-1.jpg)、[GPT-6 Astra](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/backrooms-gpt-astra.jpg)的實際輸出圖均為原作者圖片，沒有使用生成式示意圖。

| Sonnet 5.5 | Sonnet 5 | Opus 5.5 | Fable 5.1 | GPT-6 Astra |
|---|---|---|---|---|
| ![Sonnet 5.5 實際 Backrooms build](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/backrooms-sonnet-5-5.jpg) | ![Sonnet 5 實際 Backrooms build](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/backrooms-sonnet-5.jpg) | ![Opus 5.5 實際 Backrooms build](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/backrooms-opus-5-5.jpg) | ![Fable 5.1 實際 Backrooms build](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/backrooms-fable-5-1.jpg) | ![GPT-6 Astra 實際 Backrooms build](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/backrooms-gpt-astra.jpg) |
- **遊戲任務規格：**第一人稱瀏覽器恐怖遊戲；用 Blender/Cycles 製作逼真黃色 Level 0 房間、PBR 材質與光照貼圖；無縫程序生成延伸迷宮；WASD/mouse、衝刺、依速度變化的腳步；怪物依聲音追蹤玩家；找線索逃出，典型一局 5–15 分鐘；位置音效；Chrome/WebGL2 1080p 流暢；素材原創。要求模型用自動化實際走迷宮、被抓一次並成功逃出，截圖與真實照片比擬；DONE 條件列載入無錯誤、抓到與逃脫、1080p 流暢及畫面相似度。
- **比較條件與成績：**作者說五款模型各收到完全相同提示，不接受追問、不重跑、作者盲比；Claude 模型用 Claude Code、GPT-6 Astra 用 Codex，全都 high effort + goal mode，容許單一任務內長時間自主工具／測試／修正。Backrooms 各為：Sonnet 5.5 114 分／$15.35；Sonnet 5 51 分／$17.22；Opus 5.5 91 分／$20.89；Fable 5.1 151 分／$36.09；GPT-6 Astra 28 分／$7.28。這些 API-equivalent 成本由作者按實際 tokens 與公開費率估算，執行則在訂閱方案中。沒有獨立的數值化遊戲品質評分；文章是作者實玩及盲比觀感。
- **適用性判斷：**這是目前找到最接近「直接重跑最新模型」的完整題目：比 hill-climb、Pac-Man 等短題多出 3D 場景、程序內容、敵人 AI、音訊、逃脫 loop 和自我驗收；規格、outputs、成本都可查。缺口是各模型分別使用原廠 coding agent，工具鏈／agentic harness 不同，GPT 樣本是 Astra 而非 GPT-6.1 Sol，只有每模型一個 run，盲評由原作者執行且沒有公開 rubric。因此建議以同一原文重跑 GPT-6.1 Sol、Sonnet 5.5、Opus 5.5 等當前模型，固定共同工具與時間上限；將既有五版當歷史參考，不宣稱它們是純裸模型單次輸出。

### 2026-10-04 增補：近期高複雜度成品與生成基準邊界

- [Opus 5.5 海盜生存遊戲展示](https://www.reddit.com/r/aigamedev/comments/1wws7lh/after_years_of_unfinished_side_projects_claude/)是本輪找到最有系統深度的近期成品展示之一：海上掠奪與風暴返航、登船戰鬥、島嶼征服／建築升級、船艦零件可視化、要塞與動態海洋天候。貼文附實際遊玩影片與前後畫面；作者說主要美術資產是自己多年製作，模型工作約三天、近 290 commits，並由作者試玩後要求修正。因此它展示的是「人類提供資產、回饋下的長程 agentic 開發上限」，不是一次生成或公平模型比較；沒有公開 exact prompt、repo 或獨立 playable build，不能拿來排名。
- [GameDaily](https://gamedaily.ai/how-its-made)是持續產生 browser games 的公開流程案例，頁面稱 928 款／232 天（How-it-made 頁列 233 天）、每日多個候選，使用多種 mechanic／genre／input／visual constraints 組合 brief，並做桌面與手機啟動、輸入、viewport、錯誤檢查和 AI judge。其 prompt、模型身份及權重未公開，且採共用引擎元件與發布篩選；可借 QA 門檻與內容多樣性思路，不是可重現的單模型 benchmark。首頁本輪最新展示日期只到 10/01，目錄日期不可直接當成遊戲創作日。
- [MAGIC: Transition-Aware Generation of Navigable Multi-Scene Game Worlds](https://arxiv.org/abs/2607.11594)及[官方 repo](https://github.com/sereneee1201/MAGIC)是相鄰的 Unity 3D 空間生成基準：100 個多室內場景案例，測場景連接圖、門／portal 配置、可達性及 runtime scene transition；論文主模型為 GPT-4.1-mini，直接 baseline 為 GPT-4.1，報告 transition-aware F1 0.9637。完整 100 題 ground truth 需向作者索取，重現還需 Unity 6000.0.24f1 與約 23GB assets，沒有完整遊戲可玩 gallery。它測導航空間生成，不是完整遊戲迴圈，也沒有目前 frontier 模型同題成績。
- [Unity Scene Generation Failure Taxonomy](https://arxiv.org/abs/2607.10187)、[Mage companion](https://arxiv.org/abs/2605.07342)、[benchmark dataset](https://huggingface.co/datasets/anon-neurips-2026-0502/scene-level-grounding-benchmark)提供 strict no-repair 實驗參考：10,400 次 Unity C# scene-generation attempts、26 種目標型態、四種 IR 條件、20 seeds；包含 Qwen2.5-Coder-7B、DeepSeek-Coder-V2-Lite-16B、Codestral-22B、Qwen3-Coder-30B 等。研究在 compile error 後不准修復；摘要報告 10,400 次都未得到可編譯 scene。這是「一次輸出脆弱性／失敗類型」研究，不是完整遊戲 benchmark；部分 IR 條件會用兩次模型呼叫，所以 strictness 應以 no-repair 解讀，而非全部只有一個模型 call。Mage 的 858 attempts 是相關伴隨研究，不應誤算為完整遊戲結果。
- [10/02 Opus 5.5 Lander 重跑貼文](https://www.reddit.com/r/ClaudeAI/comments/1wvwipe/evidence_opus_55_today_vs_launch_regression_with/)用了相同作者任務與參考圖，比較 launch 與當日各一次 run，但當日版本失敗；沒有完整原始 prompt/repo，且每組只有 N=1。只能當同作者重跑方差案例，不足以證明模型退步。
- Deadgrid、The Big Suck、Space Federation / Star Reach、Zombie game WIP 與 MMO WIP 等近期搜尋命中，分別是無 exact prompt 的單模型 repo、既有遊戲改作、以舊遊戲為目標的重製，或持續多人回饋開發；皆不符合可比的一次生成遊戲條件，已放入搜尋台帳避免重查。

### 2026-10-04 追加核實：Backrooms 原始條件、NEXUS 與相鄰論文

- **Backrooms 原始頁再核：**[AI for Mortals 原文](https://www.aiformortals.co/blog/sonnet-5-5)日期為 2026-09-29，提供逐字 prompt、五個可玩版本與圖片。原文寫明各模型用相同提示、不追加提示、不重跑；Claude 用 Claude Code、Astra 用 Codex，全部 high reasoning effort 與 goal mode。這因此是「一則使用者任務指示、模型可自主使用 coding agent／工具持續開發」的比較，不是單模型呼叫或共同 harness 的裸模型實驗。各版成本／時間是作者根據 token usage 與公開 API 價格估算；文章沒有逐項遊戲品質量表，品質判斷是作者盲玩。這些條件讓它適合作為最新模型重跑題目，但舊排名只作參考。
- Backrooms task 自動化要求實際走迷宮、被抓一次、成功逃出，另外要求比對真實 Level 0 圖片；這是非常有用的可操作驗收方向。重跑時仍須自行留存 browser console、建置成功、死亡／逃脫紀錄、FPS／解析度，以及真人盲評的需求覆蓋、玩法成立、視覺／聲音分項，否則「作者表示做過自動化」不等於公開可審核的測試報告。
- [NEXUS Game Benchmark Agent Arena](https://github.com/specimba/NEXUS_game_benchmark_Agent_Arena)把一樣的 `BATTLE_PROMPT.md` 交給兩個 agent，隔離工作區並公開 prompt、盲評 rubric、測試計畫、啟動／崩潰／輸入／暫停／重開／持久化檢查與證據紀錄。它明確允許一個持續開發場次內規劃、原型、互動測試、除錯、反覆改善與潤飾；所以它符合「一個 user task」口徑，不符合「只准一次 model call / 第一次輸出」口徑。Repo 的 live prompt 為 v17，而 README 同時提到 v21 尚待決定是否取代，prompt 版本與每輪紀錄也有演進；目前公開 battle log 的主力模型早於這輪最前沿模型，且成品圖廊／run 可重現性不如 Backrooms 清楚。最適合借它的盲評與證據記錄法，不把其現有結果當新模型排行榜。
- [GAMED.AI](https://aclanthology.org/2026.acl-demo.84/) 是 2026-07 ACL demo 論文，非通用遊戲能力上限榜：把教師提供的問題轉成符合 Bloom 分類的教育遊戲；50 個示例、兩類模板、15 種互動機制、五領域 200 題。作者報告 90% validator pass、98.3% schema compliance、每款約 $0.46、不到 60 秒。它是 phase-based multi-agent pipeline，有確定性 quality gates；因此 90% 是系統內部 validator 通過，不可解讀為教育效果或單次模型成功率。只適合方法參考，不列最新前沿模型比較。
- [RSIGame](https://arxiv.org/html/2609.39045)（2026-09-30）是 GameCraft-Bench 的新方法結果，不是新增題庫：在原有 140 題、Godot／Phaser 上測 agentic recursive improvement，並比較內化開發經驗的訓練。論文報告 Godot 上 GPT-5.5/Codex one-shot 基線 50.26；Qwen 3.8-27B 經內化後 61.38，Phaser 58.53，並稱生成 token 約減少 11 倍。這個比較跨越不同 generator／訓練條件，方法本身含迭代開發，且 roster 不是當前 frontier；故作為 GameCraft-Bench 的後續方法論記錄，不得併入 one-shot 最新模型排名。

## 使用者意圖與搜尋標準

使用者要比較不同 AI 模型「一次生成遊戲」的能力，排除簡單小遊戲，偏好最新模型、實際遊玩成果與實測圖像。此處的「一次」暫定為：**一則使用者任務指示**；AI 可以在這則指示下自行規劃、使用開發工具、呼叫代理、測試與修正，但不能接受使用者後續提示。若要測單次原始輸出、完全禁止工具，需另列為嚴格 zero-shot 測試，不能和 agentic one-prompt 混在同一排名。

優先收錄：

1. 模型版本近期，盡量採當前可用的新模型；舊模型只為比較完整度或特殊方法價值而保留。
2. 同一遊戲規格、同一提示詞、乾淨工作區；明確記錄工具、推理強度、代理、人工介入、日期、耗時與成本。
3. 遊戲真的能玩，並盡量有源碼、精確提示詞、錄影／畫面與測試紀錄。
4. 任務有多個互相依賴的系統，能測到玩法、工程整合與測試能力，不只靠視覺包裝。
5. 把作者主觀評分、模型自述、策展人的來源核實分開標記；不將其當成客觀成績。

## 目前建議

### 如果現在只能選一題

**若要測可控、較公平的跨模型能力，我仍建議先選 Backrooms horror game 公開 prompt**，做「一則任務指示、模型可自主用工具與自我測試、不接受使用者追問／修正」的比較。它同一份逐字規格已有五款可玩的首版輸出、真實截圖、作者盲測影片，以及各模型時間／token-equivalent cost；題目整合 3D 建模、程序地圖、第一人稱操作、聲音導向敵人、逃脫流程和實際自動化驗收，比一關物理遊戲更接近完整遊戲。舊比較用 GPT-6 Astra、尚未包含 GPT-6.1 Sol；因此建議把當前最新模型用同一 prompt 重跑，並固定共同工具環境、時間預算和每模型 run 數。\n\n**若你要先看「最有上限感、畫面與完整度都直觀」的公開實測，先看 Fable 5.1 vs GLM-5.3 的 NEON WARDEN／VESPERA 配對案例。**兩者用逐字相同的開放式 3D 遊戲 prompt，成品、截圖、成本／時間／token 和自動遊玩證據都有公開；它目前是文件中最完整的一次提示同題對照。但兩個 run 都使用 RTX 5090 與 Blender、ComfyUI 及圖像／影片／音樂生成工具，故測的是整套 agent + 工具鏈，不是隔離裸模型的公平比較。建議把它當「看難度與整合能力的 showcase」，Backrooms 當「你自己重跑新模型的公平主題」。

**這仍是「公平比較」第一順位；若更重視模型自己決定要做哪一種遊戲的自主性，BioNeural 是更貼近你原始意圖的題型種子。**原題只說做一款能上線的多人遊戲，玩法交給模型，結果自選為 3D 多人射擊；但目前只有 Opus 5.5 的作者自述，且成品已經多次更新。它不適合直接比榜，卻很適合整理出一個同工具、同權限的新跨模型任務。若想用一份現成、原始 prompt 和 Playwright 驗收都完整的題目跑新模型，Fable 5.1 的 NEON WARDEN 是另一個高價值起點；其多模態資產鏈要求 RTX 5090、Blender、ComfyUI 等，因此要比較整套 agent/tool 能力，不能冒充純模型公平測試。

若更重視**角色成長、戰鬥、掉寶與多系統長流程**，第二題再選 AI for Mortals 的 Diablo-style ARPG 原始提示；它已有四個可玩版本和公開規格，玩法系統比 Backrooms 更厚，但更新模型 roster 與統一工具條件需要重跑。接著可以用 MALL ACTION 測更長規格的跨系統整合。

如果更重視**把規格完整度壓到更高**，再把 MALL ACTION 作第二題：六層商場、多視角探索、戰鬥、道具、固定模擬與不同輸入裝置都需要跨系統整合。它包含 GPT-6.1 Sol 等較新分支，但目前公開玩法影片／同一頁對比不如 Diablo ARPG 直觀。

最新查核也補上 [PacBench](https://jonclegg.github.io/pacman-bakeoff/)：它有 GPT-6.1 Sol、Sonnet 5.5、Opus 5.5、Astra 的同一句 prompt、可玩的首版 HTML 和可讀 rubric，但只生成 Pac-Man，適合作「遊戲基本規則／操作」嚴格 one-shot 校準，不是完整遊戲上限。另有 [BitsMinds Hill Climb 的 GPT-6.1 Sol vs Opus 5.5 可玩對照](https://www.bitsminds.com/news/claude-opus-5-5-vs-gpt-6-1-sol-hill-climb-2026)：任務較 Pac-Man 複雜，含物理競速，但只有一關。建議先用 PacBench 校準基本規則，再用 Hill Climb 看物理、失敗與重開，最後用 Diablo ARPG 或 MALL ACTION 測多系統長流程。

本輪的分層建議：**最新模型同題 one-prompt 主測用 Backrooms；要測更厚的角色／戰鬥／掉寶循環，用 Diablo-style ARPG；要可重現的客觀操作驗收，用 GameCraft-Bench Airship Trader；要刻意壓物理與編輯器上限，再加 Tumble。**新增的同作者 waterslide 系列有三個模型 build、來源與細緻自動測試，可當更易重跑的競速物理副測；但 prompt 不完整且未證明逐字一致。[EvalMap Jeep gallery](https://evalmap.ai/jeep/) 用於短版可玩性／失敗率校準，不取代主測。Airship Trader 現有模型結果偏舊，應作固定規格重跑，而非引用舊排名；Tumble 的物理條件最尖銳，但現有對照欠獨立 build 和硬性測試證據。

### 主測建議納入的最新模型（截至 2026-10-04）

| 模型 | 當前狀態 | 納入建議 |
|---|---|---|
| GPT-6 Astra、GPT-6.1 Sol | OpenAI 官方 API 模型頁列為旗艦與成本平衡款；GPT-6.1 Sol 也支援高／超高推理強度。 | 兩者都納入；固定同一 coding harness 和推理設定，另可將原廠 Codex 條件作第二組。 |
| Claude Opus 5.5、Sonnet 5.5、Fable 5.1 | Anthropic 官方透明度頁於 2026-09 列出這些型號；Sonnet 5.5 已於各平台提供。 | Opus／Sonnet 作主流候選，Fable 作高階補充；逐次記 model ID、effort、agent 版本。 |
| Grok 4.7 | SpaceXAI 於 2026-09-21 發布，官方稱可透過 Cursor、Grok Build、API、第三方 coding harness 使用。 | 納入可取得模型組；它比只看 GPT／Claude 的 roster 更能反映目前公開 coding model。 |
| Gemini 3.8 Flash | Google 官方 API 文件列為 GA；支援長程軟體工程、自主 agent，Antigravity Managed Agents 的預設模型。 | 加入可立即取得的 Google lane，標為 Flash 級別；不把它冒充成 Gemini 4 Argon 的前沿旗艦。 |
| Qwen3.8-Max | Qwen Code 官方更新稱於 2026-08-27 由 preview 轉為 stable，保有 low／medium／xhigh reasoning，並可在 Qwen Code 選用。 | 作可取得的中文／亞洲模型比較候選；記錄它的 harness 和 API／Token Plan 條件，與 closed-frontier 結果分開呈現。 |
| DeepSeek V4.1 Flash | DeepSeek 2026-09-10 發布，可經 `deepseek-flash` API 呼叫；官方 Hugging Face model card 標 MIT，並提供本機 serving 路徑。 | 加入預算／開放權重 lane；552B MoE 整體權重需要大型硬體，本機與託管 API 需分開標示，保持其他模型同樣的 agent 能力／工具預算。 |
| Gemini 4 Argon | Google 於 2026-09-30 公告，當時先透過 Fairwind 向可信任 cyber defenders 開放，表示之後才逐步擴大到開發者、企業與消費者。 | 列為「待開放即加入」；在實際可用前，不拿尚不可取得的型號和其他模型硬比，也不以較舊 Gemini 3.6 Flash 代替 Argon 的前沿成績。 |
| Claude Mythos 5.1 | Anthropic 官方頁列為 trusted-access only。 | 只在你具備合法可用權限時列候選；一般公開重跑名單先不納入。 |

版本／可用狀態依各廠截至 2026-10-04 官方資料整理：[OpenAI 型號頁](https://developers.openai.com/api/docs/models)、[Anthropic 透明度中心](https://www.anthropic.com/transparency)、[Grok 4.7 公告](https://x.ai/news/grok-4-7)、[Gemini 3.8 Flash 最新型號說明](https://ai.google.dev/gemini-api/docs/latest-model)、[Gemini 4 Argon 公告](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)、[Qwen3.8-Max stable 公告](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-08-27/)、[DeepSeek V4.1 Flash 發布說明](https://api-docs.deepseek.com/news/news260910/)及[官方權重/model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)。模型更新很快，實際執行日再核對 model ID 和可用性，並把截圖／API 回應中的型號版本存入結果表。

若你說的「一次生成」是**不准 agent 自行反覆測試修正**，要另外做 strict first-output 組，限制只能輸出一次結果；不建議直接把 Single HTML Game Bench 當唯一上限題，因它的單檔限制和模糊「production-ready」條件會讓結果偏向程式碼包裝而非完整遊戲能力。

### 延伸案例：MALL ACTION（長規格 agentic 開發比較）

它是清單中最適合檢查長規格逐項落實、固定模擬與大型系統整合的公開案例。對「先看最新模型同題成果」的當前主測排序在 Backrooms 之後；MALL ACTION 的優勢是需求與 QA 規格更細，缺點是各分支 harness／條件及第三方盲評資料仍不完整。

- [專案與模型分支](https://github.com/rlorca/mall-action)
- [完整 one-shot prompt](https://github.com/rlorca/mall-action/blob/main/one-shot-prompt.md)
- [執行規範](https://github.com/rlorca/mall-action/blob/main/AGENTS.md)
- 可玩版本：[GPT-6.1 Sol](https://rlorca.github.io/mall-action/gpt-6.1-sol/) · [Sonnet 5.5](https://rlorca.github.io/mall-action/sonnet-5.5/) · [Opus 5.5](https://rlorca.github.io/mall-action/opus-5.5/) · [Gemini 3.6 Flash](https://rlorca.github.io/mall-action/gemini-3.6-flash/) · [Fable 5.1](https://rlorca.github.io/mall-action/fable-5.1/)
- 遊戲是 80 年代商場背景的 8-bit 間諜動作遊戲：六層商場、13 家店、電梯與手扶梯、走廊橫向移動、商店內俯視探索、守衛與敵人、六件隱藏包裹、武器／強化、地圖、暫停、逃脫結算與逐輪升難度。
- 規格還涵蓋 60Hz 固定模擬、確定性隨機種子、鍵盤／手把合併輸入、QWERTZ/AZERTY 配列、逐鍵釋放正確性、程式生成像素素材與音訊、純遊戲規則測試、Playwright 測試及 CI 部署。可用來測複雜需求的整體落實，而不只看截圖。
- 目前有 Opus 5.5、Sonnet 5.5、GPT-6.1 Sol 等新模型的可玩分支；這是近期公開案例中很有價值的同題比較。README 的模型列表也有較舊版本。
- GPT-6.1 Sol 的驗證紀錄：[verification.md](https://raw.githubusercontent.com/rlorca/mall-action/gpt-6-1-sol/verification.md)。公開紀錄包括測試和瀏覽器驗證；部分端到端狀態使用 debug 方式孤立驗證，不等於人工不間斷通關。模型歸屬是作者回報，尚非第三方獨立審計。
- README 現列的 9 個模型分支是 Opus 5.5、Sonnet 5.5、GPT-6 Sol、GPT-6.1 Sol、Fable 5.1、Haiku 4.5、Gemini 3.6 Flash、Opus 4.6、Opus 5。GPT-6.1 Sol 分支的驗證紀錄標示 2026-09-29：約 50 分鐘、74 個單元測試、build 成功及 23 項 Playwright 檢查；部分以 debug 放置隔離狀態／結束條件，並非連續人工通關。以上是作者公開紀錄，非獨立重跑。
- 策展來源 [Mall Action 核實頁](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/games/mall-action-model-benchmark/readme.md) 說明其評分根據來源完整度、玩法與文件，不是 runtime benchmark；其截圖評分也只是人工看圖，不能當成遊玩測試或基準分數。
- 判讀限制：各模型的推理強度、執行環境和代理條件沒有完全標準化，也沒有一套公認的跨模型分數。應將它視為最好的公開起跑線，而非已有定論的模型排行榜。
- 比較題建議分工：Backrooms 作為最新同題可玩成品的主測；MALL ACTION 用於更細的長規格、輸入裝置、確定性與 CI 落實；[AI for Mortals 的 Diablo-style ARPG](https://www.aiformortals.co/blog/sonnet-5-5) 作角色成長、戰鬥、掉寶系統的第二題。這三題分開報告，不用單一總分掩蓋任務類型差異。

### 高豐富度單提示展示：Kart Blitz（Sonnet 5.5）

- [文章、精確提示詞、圖片與可玩版](https://www.nathanonn.com/sonnet-5-5-one-prompt-game/) · [影片](https://youtu.be/k7oO3ZLmPwE) · [作者的雲端工具 repo](https://github.com/nathanonn/cloudplay)
- 這是 2026-10-02 發表的另一個獨立 run（不是原 Reddit 的同一次 build）：Sonnet 5.5 Max，Claude Code on the web，單一 user prompt 後作者不再介入，約五小時；使用一個 lead 加五個 builder subagents、Three.js、Firecrawl 研究、Playwright 瀏覽器自測，並要求建立任務分工、保存到 localStorage、最後發佈 Claude Artifact。文章公開此版本的 prompt，並說明這是把原 Reddit clone prompt 改成原創 kart racer 的變體。
- Sonnet 5.5 Max 在 Claude Code 網頁工作階段中，由一則使用者訊息啟動；有五個子代理，約五小時完成。包含八條賽道、八位車手、50cc–200cc、漂移加速、13 種道具、11 位 AI 對手、Grand Prix／Versus／Time Trial，以及鍵盤、手把和觸控。
- [直接遊玩 Kart Blitz](https://claude.ai/artifact/PFZaJiiXukDjHaU9Nbv65m)；文章記載 308 個自動測試，提供截圖和影片；作品作者親自跑完一場（12 人中第一名）並回報手機觸控可用。模型自述仍列出未驗證項目，作者實玩補足一部分證據，但這不是獨立盲測。308 測試是作者報告，沒有公開測試原始碼／結果清單供獨立審核。
- 限制：另一個 Sonnet 5.5 kart run 是 High、約 67 分鐘、未報自測工具的 Reddit 版本；此 Max 版本改了提示並加入 browser / Firecrawl / Playwright，自行找到並修復四個畫面問題，還用子代理並行。不可把兩者的功能數、時間或驗證結果混算，也不是控制變因良好的跨模型 benchmark。
- 原始 Reddit run：[原帖和提示](https://www.reddit.com/r/ClaudeCode/comments/1wsx03y/sonnet_55_high_oneshot_a_full_mario_kart_from_1/) · [可玩 Turbo Karts](https://ohmygames.app/play/turbo-karts)。作者報 Sonnet 5.5 High、lead+5 builder agents、空 `/tmp` 無預載 harness、67 分鐘、424 次模型呼叫、889k 寫入 tokens（352k reasoning）、78M 讀取 tokens、API 等值 $29.28；遊戲 4 賽道、8 racers、10 道具、漂移加速、bots、Grand Prix/Skirmish，約 11,400 行 JavaScript，無圖片／音訊檔。
- 此原始 run 其實比文章的五小時 Max/加 browser、Firecrawl 變體更像「一則 user prompt 下自主多代理」重現材料；但兩個 run 條件不同不可合併。clone 任務和「AAA quality」不是有效客觀驗收，公開材料也沒有原始碼、測試套件、盲評或獨立通關記錄，作者所報 metrics 未獨立審計。

### 高複雜度單句展示：Opus 5.5 三款 3D 遊戲

- [專案、原始提示詞、原始碼、部署連結和驗證記錄](https://github.com/riba2534/claude-opus-5-5-demo)
- 三個一行提示詞案例：鵜鶘騎自行車、FPS 團隊槍戰、QQ 飛車風格漂移競速。作者稱每款在單一會話中完成，模型可自行查資料、編寫、建置、測試和部署，無人工改碼；遊戲以程式生成素材，不使用外部圖片音訊資產。
- FPS 包括地圖重建、武器與 bot 對戰；競速包括四種賽道、漂移、氮氣與重置；騎車作品含布料模擬、晝夜循環、音效與長時測試。各有直接可玩的連結。
- 適合研究「提示很短時，模型會自行選擇什麼範圍與完成度」，不適合直接比較模型，因目前這組成果是 Opus 5.5 單模型展示。注意其後續模型自測／修正屬於一次使用者任務下的自主工作，並非第一輪生成立即完成。

### 冒險玩法壓力測試：8-Bit AI Arena / Ruinseed

- [可玩成果](https://frostsource.github.io/8bit-ai-arena/) · [提示詞](https://github.com/FrostSource/8bit-ai-arena/blob/master/PROMPT.md)
- 518 行提示規格；程序化地圖、可達性檢查、多個地城、戰鬥、商店／存檔、頭目戰與完整勝利流程。比 Mall Action 更偏長流程冒險與程序生成。
- 已有 GPT-6 Astra、GPT-6 Sol、GPT-6 Luna、Opus 5.5 等版本，但未見 GPT-6.1 Sol／Sonnet 5.5 的同題更新。含生成結果與作者檢查，但不是統一的正式評分套件。
- 若想測「持續探索與關卡系統」而不是多視角動作玩法，作為第二主題候選。

### 嚴格原始輸出對照：Single HTML Game Bench

- [可玩作品、提示詞及規則](https://chojondocho.github.io/single-html-game-bench/)
- 固定提示為單一 HTML 的 3D 恐怖遊戲，混合 RPG／Roguelike，限定 one-pass、不人工調整。2026-09-30 頁面列有 Opus 5.5 Max、GPT-6 Astra Max、GPT-6.1 Sol Max 等成果；尚未見 Sonnet 5.5。
- 本輪重核 [README／model matrix](https://github.com/chojondocho/single-html-game-bench/blob/main/README.md)：同一初始 prompt、20 個 client/model 組合、公開可玩首版與 GitHub Pages；當前榜列 GPT-6.1 Sol Max（第 6）、GPT-6 Astra Max（第 5）、Opus 5.5 Max（第 1），未列 Sonnet 5.5。規則明寫 zero-shot/one-pass、單檔 HTML、不能生成後手動調整。原始 prompt 仍以「Game of the Year／production-ready」作難以客觀核驗的要求，名次為作者實玩後的個人主觀排序。
- 可直接看三款[Opus 5.5 Max](https://chojondocho.github.io/single-html-game-bench/claudecode-opus-5-5-max/)、[GPT-6 Astra Max](https://chojondocho.github.io/single-html-game-bench/codex-gpt-6-astra-max/)、[GPT-6.1 Sol Max](https://chojondocho.github.io/single-html-game-bench/codex-gpt-6-1-sol-max/)建置，頁面列出作者主觀名次 1、5、6；此處只作實物展示，不引用為客觀排名。
- 原始 prompt（來源 README）：

  > Create a complete 3D horror game in a single HTML file, incorporating RPG and roguelike elements. The quality must be high enough to win a Game of the Year award. Do not stop until you determine that it can definitely win. Every element must be production-ready for release within that single HTML file alone.

- 適合補做「不能依賴工具測試或後續修正」的嚴格基線；提示詞本身以「年度最佳／production-ready」等模糊口號要求品質，排名由作者實玩後主觀評定，且模型環境未必相同。

## 其他近期案例與校準材料

### Tumble：自製物理與建造工具上限題（優先新增）

- [同 prompt 的 Opus 5.5 vs GPT-6 Astra 測試、完整規格與作者回顧](https://promptslove.com/blog/claude-opus-5-5-vs-gpt-6-astra/) · [影片比較](https://youtu.be/cwGSDctKCbk)
- 文章日期 2026-09-24。作者把同一份詳細 brief 分別交給 Opus 5.5（high）和 GPT-6 Astra（xhigh）；任務是單一 `tumble.html` 的 3D 彈珠建造／物理遊戲，使用 Three.js、程序生成素材，禁止物理引擎，要求模型自行實作物理。這是舊於目前最新模型的案例，但保留的理由是它提供了罕見的完整高難度 prompt 和逐項驗收規格。
- 核心難度不是畫出一條軌道，而是把固定 180Hz 模擬、球與三角面碰撞、摩擦轉動、球球碰撞、連續碰撞偵測、防穿透、100 顆彈珠效能、質量差異，與 15 種可互動構件一起做好；還要有網格吸附、連接埠提示、編輯器、30 階 undo/redo、慢動作與追球鏡頭、6 個範例、8 個謎題、儲存／匯入匯出，以及依材料與撞擊速度變化的音效。
- brief 自帶很強的可驗收條件：彈珠要實際滾動並帶自轉、最高速不穿透、100 顆同場保持 50fps 以上、迴圈／蹺蹺板／轉輪／升降機行為正確、復原與存取狀態一致、8 個挑戰可解。這使它比「看起來像完整遊戲」更容易檢查核心系統是否真的工作。
- 作者實際操作後偏好 Opus：他報告 Astra 缺少自由沙盒建置控制、零件不易連接，且畫面閃爍；Opus 的拼接操作較順。這是單一作者、各模型各一次、主觀操作判斷；文章沒有提供獨立公開 playable build、逐項測試紀錄或 FPS 實測證據，故這些結果只能當案例觀察，不能當模型排名。
- **我的建議：**把這個完整 prompt 當作「物理／系統上限副測」的首選來源，補跑 GPT-6.1 Sol、Sonnet 5.5、Opus 5.5、Astra 等最新模型；統一允許的工具與自我修正政策，另以固定自動場景檢查碰撞、軌道互動、效能、謎題和存檔。完整遊戲流暢度仍用 Diablo ARPG，避免一題的遊戲類型偏差。

### GameCraft-Bench：Open-World Airship Trader（重跑最新模型的完整遊戲候選）

- [完整任務指示](https://github.com/FreedomIntelligence/gamecraft-bench/blob/main/tasks/openworld-airship-trader/instruction.md) · [GPT-5.5 / Codex 可玩版](https://tongxuluo.github.io/gamecraft-bench-website/static/godot/codex55__openworld-airship-trader/index.html) · [基準與其餘 playable demos](https://tongxuluo.github.io/gamecraft-bench-website/) · [程式與驗收框架](https://github.com/FreedomIntelligence/gamecraft-bench)
- 這個任務要求交付可發布的 2D Godot 4「浮空島商人」垂直切片：玩家在天空自由飛行、往返不同島嶼，根據產出／需求買賣貨物並面對波動價格；營利後升級引擎、貨艙、燃油效率與裝甲；航線上有會追擊的海盜，可逃跑、用砲戰鬥或付過路費；飛行消耗燃料，耗盡會失去動力，也可在島上買油或找漂浮補給。還包含標題畫面、視差雲層、島嶼辨識、靠港提示與交易介面。
- 這比單一車輛賽道更接近完整遊戲：移動、航線風險、經濟、庫存、船隻升級、敵人、燃料資源和介面必須形成同一循環。精確指示、素材目錄、Godot 版本、示範輸入格式都公開。模型交付完整 Godot 專案與 1–10 段 JSON 輸入軌跡；評估器在 1280×720 重播固定軌跡、錄下實際畫面，再按 core mechanics、content depth、functional visuals、art and presentation 四項 rubric 評分。
- 官網可直接看 / 玩各模型的代表成果；GPT-5.5 + Codex 的 Airship Trader 頁面分數為 60.40。這不是最新模型結果，也不是裸模型直接輸出：使用 Godot agent harness、共用資產庫與視覺 judge。雖然基準介紹稱 rubric hidden，目前公開任務 repo 同時放出該 task 的 rubric 與 reference solution，因此重跑要自行隔離 evaluator 檔案。當前榜單未列 GPT-6.1 Sol 或 Sonnet 5.5，且未看到其他模型的 Airship Trader 同題結果。
- **建議用途：**若希望自行驗證多個最新模型、又需要完整規格、可玩的 2D 遊戲和重複播放的固定驗收流程，這比從一張 demo 圖猜難度更可靠。可固定此一 prompt 對新模型重跑三次，保留失敗與 demo trace，分別報機制、內容、視覺功能、呈現四項；把人工盲玩趣味分開，不和基準分數混算。若希望測 3D 或物理極限，再與 Tumble／Diablo 配對。
- 重跑時讓每個新模型只收到相同 `instruction.md`、空白 workspace 和同一份只讀素材包；不要把 reference solution、hidden tests 或舊輸出交給模型。固定 Godot 4.6.2、作業系統、畫面尺寸、工具／代理權限、時間預算與 judge 版本；允許 agent 在一則任務內自主開發與測試，不接受人工後續提示。每模型 3 個獨立 workspace，照原 trace protocol 輸出 1–10 段 deterministic JSON replay。報告各次任務分和失敗率，再另做隱去模型資訊的實玩盲評。

![GameCraft-Bench 的 GPT-5.5 Airship Trader 成品截圖，取自官方 playable build](https://tongxuluo.github.io/gamecraft-bench-website/static/godot/codex55__openworld-airship-trader/index.png)

### Planet Pop / Tiny Comic Planet：重跑穩定度

- [比較頁、原提示、四次 Sonnet 結果、Opus 結果與同角度畫面](https://ohmyunicorn.com/labs/dream-loop/tinyworld-sonnet55-vs-opus55/)
- 同提示產生可旋轉／縮放的 3D 星球。Sonnet 5.5 有四次獨立生成，報告時間、token、價格並提供成品；四次都可玩，但細節差異明顯。
- **非高難度主測題**。更適合提醒要多跑幾次，並研究穩定度；頁面自己也揭露 Opus 只有一次，且會話條件不完全相同。
- 實際比較圖片（公開成品截圖）：

![Opus 5.5 一次與 Sonnet 5.5 四次生成的 3D 星球，同一視角比較](https://ohmyunicorn.com/labs/dream-loop/tinyworld-sonnet55-vs-opus55/img/exact-orbit.jpg)

### EvalMap Jeep gallery：近期同題可玩性與失敗率校準

- [One brief, 119 builds](https://evalmap.ai/jeep/)：頁面列出 2026-07-16 至 10-03 的 119 個同題 build，80 個成功作品可直接在頁面操作，39 個失敗也保留原因。公開簡述是瀏覽器內可駕駛的 3D 吉普賽車；精確原始 prompt 未公開。
- 最新名次（頁面查核日 2026-10-04）：Pareto 26.10 Preview 58/100、Claude Sonnet 5.5 xhigh 48、GPT-6.1 Sol xhigh 45、Opus 5.5 xhigh 40、GPT-6 Astra 39。GPT-6.1 Sol run 記為 2026-09-29、Codex；Sonnet 5.5 為 9/28、Claude Code。新 Pareto build 未記錄可核實的模型／harness 細節，不應當成可比的前沿模型證據。
- 評分六項是 runs/world/driving/race/look/presentation。評者實際開車約一分鐘，再從起點持續直行 90 秒找出世界邊界；翻車／卡住有分數上限，掉出地圖或解體則降至 12。每個成品可直接點玩，頁面同時附逐項評語、部分執行環境、耗時、token、成本與失敗紀錄。分數是 EvalMap 自己的成品判斷，不代表模型通用能力；頁面說明成果會受同一 brief 以外的工具／模型條件影響。
- **定位：**它是很好的中階校準題，可看能否啟動、車輛操控、賽道／對手整合，以及長時間是否掉出世界；同題數量和實玩證據遠勝只有截圖的展示。但任務單一、規格描述短、執行跨度近三個月且 harness 不完全一致，不能當完整遊戲的上限測試，也不宜把作者 0–100 分當客觀 leaderboard。

### Vibecode Bench：快速類型校準

- [四種固定提示、可玩成品、來源 gist 和模型設定](https://senko.net/vibecode-bench/)
- 類型有 RTS、Voxel/Minecraft 風格、飛行模擬和 Minesweeper。頁面顯示 Sonnet 5.5 的三種遊戲在 2026-09-28 完成；Opus 5.5、GPT-6 Sol、GPT-6 Astra、Fable 5.1 等也有可玩的同題成果。GPT-6.1 Sol 尚未出現。
- 原始題目刻意要求「simple」並限定單一 HTML：RTS 有建築、單位、資源、探索，但明確不要求 AI／多人；Voxel 需移動、方塊、採礦與 mob 戰鬥；飛行模擬需物理、地形、其他飛機和一戰雙翼機空戰。提示明確說不追高完成度，所以可用來校準類型能力，不宜作上限主題。
- 執行條件不是完全同一 harness：Codex/GPT 與 Claude Code/Claude 模型分別執行；部分條目公布耗時和成本。它有直接 playable 和 gist，適合作為候選任務池。
- Sonnet 5.5 可玩示例：[RTS](https://senko.net/vibecode-bench/2026/rts-sonnet-5.5.html) · [Voxel](https://senko.net/vibecode-bench/2026/voxel-sonnet-5.5.html) · [飛行模擬](https://senko.net/vibecode-bench/2026/flysim-sonnet-5.5.html)。

### Lunar Scream：嚴格 one-shot 對照

- [四模型成品、原始提示、影片和原始碼入口](https://ultra.dev/projects/lunar-scream)
- Opus 5.5、Fable 5.1、GPT-6 Astra、GPT-6 Sol 各自收到相同提示，沒有澄清／後續修正，保留原始 bug；四款均可在瀏覽器玩。玩家以聲音大小控制著陸器，也可使用鍵盤／觸控。
- 原提示是「做一款以尖叫推進的月球著陸遊戲，請自行決定設計並交付可執行成品」。這是一個很乾淨的 strict one-shot 核心範例，但玩法範圍很小，且不是 GPT-6.1 Sol 或 Sonnet 5.5 的最新模型比較；無統一分數。因此作為**嚴格 one-shot 的校準案例**，不能當上限主題。
- 好處是提示詞把「不可追問、不可修正」明寫出來，能作為設計嚴格測試規則的參考。

### Senko 三類遊戲同題比較：值得追蹤的多任務校準組

- 這是 Vibecode Bench 的三款 agentic one-shot 固定任務：RTS、Voxel、飛行模擬。Opus 5.5、GPT-6 Sol、Sonnet 5.5、Fable 5.1、GPT-6 Astra 等有可玩的同題版本及 gist；Sonnet 5.5 結果於 2026-09-28，Opus／GPT-6 Sol 約 2026-09-22–23。
- 有耗時、成本、推理強度資訊，且模型各自只有一個樣本。三題是簡化版，能看類型偏科和完成差異，不適合主測極限；尚缺 GPT-6.1 Sol。保留為可重現的**副測題組**，日後檢查它是否加新模型。

### Game Bench：評分方法參考

- [基準、固定提示、可玩版本和計分方式](https://game-bench.piccini.app/)
- 乾淨工作區、固定提示、無人工回饋；模型可自行規劃、建置和測試。分數權重是玩法 45%、需求符合 15%、工程 25%、美術 15%。
- 頁面最新列有 GPT-6 Astra、GPT-6 Sol、Fable 5.1、Opus 5.5 等，但尚未列 GPT-6.1 Sol／Sonnet 5.5。作者評分及題目難度有限，不當成上限測試。

### Goldie Bench：多題高量矩陣

- [全部任務](https://goldiebench.com/tasks/) · [方法說明](https://goldiebench.com/methodology) · [Dragonrealm 開放世界題](https://goldiebench.com/tasks/dragonrealm)
- 這不是只有一題的「Game 27 模型」頁面：任務庫包含 50 個固定 one-shot 創意程式題、分五類；遊戲題數在本輪查核的頁面間顯示 20 或 23，應視為動態統計不一致。不同題目列出約 27–38 個模型。模型在同一 Agent Operating System 中各自生成單一 HTML，無回饋、無迭代、不能從多次生成中挑最佳。
- 遊戲題中較接近上限測試的是 Dragonrealm：冰雪開放世界、可步入雪地、拔劍；頁面同時可玩。模型清單／已評分數在任務表與子頁有動態差異，仍未看到 GPT-6.1 Sol 或 Sonnet 5.5。
- 分數是作者 Julian 的 0–10 人工評語，三項大意為能否執行、符合 brief、畫面好看；方法頁稱 1,609 格中 1,259 格有策展評語。適合當大量同提示成果目錄，不是自動化客觀排行榜。頁尾仍標示 2026-06，與較新任務內容的更新時間不完全一致。

### OneShotLM：大型可玩作品索引

- [作品索引](https://oneshotlm.com/) · [更新紀錄](https://oneshotlm.com/whats-new/)
- 首頁約列 4,549 builds、142 models、35 prompts，其中 10 個遊戲提示，更新至 2026-09-29；但更新紀錄顯示約 4,514 builds、141 models，最後更新 2026-08-28，數字與日期不一致，需以逐筆來源再核對。
- 2026 年 7 月加入兩階段評估：先做畫面變化／輸入／錯誤等確定性檢查，再以視覺評審打分。它適合找候選成品與研究大規模收錄方式；目前可見模型清單未包括 Opus 5.5、Sonnet 5.5 或 GPT-6.x，因此不適合作為最新模型上限比較。

### One Shot Challenge：大量單次提交方法參考

- [活動資料與結果](https://oneshotchallenge.ai/benchmark) · [規則與執行架構](https://1shotchallenge.ai/) · [得獎作品](https://1shotchallenge.ai/winners) · [全部 141 個可玩作品](https://1shotchallenge.ai/entries)
- Round 01 在 2026-07-13 至 07-18 進行：101 位參賽者、200 次模型 run、25 個模型、141 個公開可玩產物；主辦方稱完整保存成功與失敗 run。伺服器代跑參賽者單一提示、單一模型呼叫；不可編輯／重試，失敗也計入，並用提示與輸出 hash 作查核。平均每次約 33,816 tokens，總計 6.76M tokens、20.2 小時 compute；官方估計 193/200（97%）返回可用 entry。資料適合研究首稿可靠度、成本／時間記錄和 artifact archive。
- 評選由盲評 jury 選五名、社群票選一名，但未見公開逐項 rubric 或所有 200 次輸出的標準化同題評分；提交者各自選 prompt，任務和模型分配不均，所以不能把得獎名次解讀成模型榜。前 12 名常用模型最高仍為 Fable 5、Opus 4.8、GPT-5.6-Sol 等，早於目前 GPT-6.1 Sol／Sonnet 5.5；它是嚴格 one-call 方法與作品目錄參考，不是最新模型的固定 prompt 上限比較。

### 策展清單

- [近期 AI 遊戲成果列表](https://github.com/AgentsLoop/awesome-opus-5.5-games/blob/main/latest-games.md) 持續收錄 9 月下旬的遊戲，含 Sonnet 5.5、Opus 5.5、GPT-6.1 Sol 等；適合作為發現新項目的入口。
- 例如 [GPT-6.1 Sol 的 Slipstream](https://github.com/KJLKurt/waterslide-game-gpt-6.1-sol) 已確認有直接 playable 和詳細驗證說明；同作者／同系列看似有 Sonnet 5.5 的 [Splash Rush](https://github.com/KJLKurt/waterslide-game-sonnet-5.5/)，但尚未核實是否相同 prompt、規格和執行條件，先不要合併成同題比較。
- 策展分數要當作人工觀感或來源核實線索，不可直接當客觀遊戲測試分數。

## 正式比較時建議記錄的資訊

| 維度 | 最低記錄內容 |
|---|---|
| 模型 | 完整版本／路由、日期、推理強度 |
| 執行條件 | IDE／agent harness、可用工具、是否允許代理、是否能上網 |
| 任務 | 完全相同提示詞、同類空白工作區、是否提供參考圖／素材 |
| 互動 | 使用者提示次數、是否給提示、是否批准工具動作 |
| 結果 | 首次可玩時間、總耗時、花費／token、建置成功、可玩連結 |
| 驗證 | 固定驗收清單、瀏覽器／引擎操作測試、完整流程、人工盲測 |
| 重複性 | 每模型建議至少 3 次；單次結果只能當樣本，不能推論穩定品質 |

建議分成兩條榜：

1. **Agentic one-prompt：** 一則使用者訊息，允許模型自主規劃、使用工具／代理、自我測試和修正。Backrooms 最適合看完整可玩成品與直觀畫面；MALL ACTION 最適合看長規格實作與測試記錄。
2. **Strict one-shot：** 只允許直接首次輸出，不給回合修正；工具限制需一致。Single HTML Game Bench 可作參照，但需要設計一份更清楚、可驗收的高難度新提示。

玩法評分可拆成：規格覆蓋／跨系統整合、能否完成一輪遊戲、操作手感、錯誤／軟鎖、視覺音訊、原始碼與可重現性、耗時成本。別把畫面品質和遊戲完整度混成單一主觀分數；最好把盲測好玩程度另列。

### Backrooms 重跑建議評分表（研究建議，不是原作者成績）

| 項目 | 權重 | 固定證據 |
|---|---:|---|
| 啟動、操作與穩定 | 15 | 全新環境可載入；Chrome console 無阻斷錯誤；WASD、滑鼠鎖定、走／跑均可用；固定 1080p 測試機記錄 FPS。 |
| 程序迷宮與可達性 | 20 | 以固定種子跑 3 個 maze；記錄連通性、出口是否存在且可達、生成接縫／穿牆／軟鎖；至少一局完整抵達出口。 |
| 聲音追蹤與潛行規則 | 20 | 同一路徑比較靜走、衝刺、撞物三情境；記錄怪物反應方向／延遲、追蹤能否脫離、聲源方位音是否可辨。 |
| 完整遊戲循環 | 20 | 自動化各完成一次被抓與逃出；開始、探索、死亡／結束、重新開始、逃脫結算皆可運作；固定時間內能理解目標。 |
| 視覺與音訊呈現 | 15 | 盲評者以同解析度截圖對照同一組真實 Level 0 參考圖；另評照明／材質／空間感、環境音／腳步／方向感。 |
| 原創性與交付品質 | 10 | 原創素材聲明可查；作品附啟動說明、版本與可玩 URL；記錄模型是否只靠假按鈕、硬編劇情或非遊戲畫面冒充完成。 |

最低門檻與連續分數分開報：若不能啟動或沒有可達出口，標記核心失敗；不要用視覺分數補回功能失敗。每模型至少 3 次獨立 run，公開全部結果。若想隔離模型差異，先統一 coding harness、工具權限與時間預算；若採原廠 coding agent，另列為「模型＋harness」比較。模型盲標後由同一批玩家操作，並公開 prompts、版本、時間、tokens／成本、console、錄影、測試結果和失敗樣本。

### Tumble 的建議評分草案（研究建議，非原作者分數）

| 面向 | 分數 | 可重跑的檢查 |
|---|---:|---|
| 可啟動與交付 | 10 | 乾淨瀏覽器載入、無致命錯誤、操作提示可理解；所有模型用同一 Three.js 版本與同一瀏覽器／機器。 |
| 物理正確性 | 30 | 斜坡上可見滾動與自轉；球－軌道及球－球碰撞；最高速無穿透；質量／摩擦／彈性差異能改變結果；固定步長下相同種子重播結果穩定。以預先固定的場景與輸入測。 |
| 構件行為 | 20 | 15 種零件各 1 分逐項檢查；另外 5 分測迴圈速度門檻、蹺蹺板受重、彈珠推動轉輪、分流和升降機回送等跨構件互動。 |
| 建造操作 | 15 | 網格吸附與接點／未接點提示 5；放置、旋轉、刪除、移動與複製 4；30 階 undo/redo 還原狀態 3；攝影機、暫停、單步與慢速控制 3。 |
| 關卡與內容 | 10 | 6 個預建示範能正確載入 4；8 個挑戰依作者公開解法／固定測試輸入可解 6。 |
| 壓力、保存與可靠性 | 10 | 100 顆彈珠同場互動且固定硬體達到 brief 的 50fps 門檻 4；複雜軌道儲存／載入／JSON 匯入匯出 round-trip 3；長時間循環不軟鎖、不丟球 3。 |
| 視聽回饋 | 5 | 材質／撞擊速度影響聲音、鐘琴音準，並有清晰可讀的程序化材質與撞擊提示。 |

每模型至少 3 次獨立 run，公開所有失敗；先按自動／確定性檢查計分，再由不知道模型身分的玩家評建造易用度與玩具手感。記錄單次分數、三次平均／範圍、耗時、成本和 harness；以固定硬體測效能，避免把動畫看起來順誤當成 50fps 驗證。若只做第一版，可先把物理、接點、迴圈、升降機、100 顆壓測、存檔 round-trip 做成 6 個核心場景，通過後再補全所有 puzzle 測試。

## 下一輪研究待辦

1. 深入核實 MALL ACTION 各新模型分支的可玩性差異、effort、耗時與是否有完整連續流程；找原作者 transcript／完整測試證據。
2. 核實 Slipstream / Splash Rush 是否同提示同規格，並搜尋最新一週是否有 GPT-6.1 Sol、Sonnet 5.5、Opus 5.5 同題競賽。
3. 從近期清單中挑出真正有長流程、多系統、提示詞、影片或可玩連結的遊戲，不把只有單張精美截圖的項目升為主案例。
4. 以 GameCraft-Bench 的 Airship Trader 規格規劃可重複的 2D 多系統最新模型重跑；另用 Tumble 公開 brief 設計「高難度、可盲測、可自動驗收」物理／建造副測。Diablo ARPG 保留為多模型完整遊戲成果對照，MALL ACTION 保留為長規格跨系統檢查。
5. 每次更新追加「日期、發現、來源、納入／排除理由」，並保留模型版本新舊資訊。使用者明確偏好最新模型；舊模型只在標明原因後納入。
6. 2026-10-04 本輪新增追蹤：AI Browser Game Jam 4 的 125 筆正式評分與作品披露；AI Browser Game Jam 5（10/17 開放投稿）、Jamference: AI Game Jam Hack 1（10/09 截止）與 Ultimate AI-Powered Game Jam #5（10/09–12）待結果頁出現後再查，不要現在重搜宣傳頁。
7. 下次恢復時先完成兩項有明確條件的回查：確認 Sky Reach 的 Tesana playable 是否能正常啟動／探索循環是否真實可玩；再核 GameXpert-Bench 是否釋出 tasks/evaluator 及是否納入 GPT-6.1 Sol、Sonnet 5.5 等新型號。GameASG / Armor Alley 已有公開 task/evaluator，若要直接開始比較，先按 strict first-output 或 agentic one-task 選定口徑，勿混榜。

## 搜尋台帳：已查項目與去重索引

**用途：** 新一輪搜尋前先對照此處。相同網址／案例除非出現新版本、新模型、原始 prompt、可玩版或更強驗證，不要重複搜尋；找到相似題材不等於同一任務。

| 案例／來源 | 已核對內容 | 判定與不再重搜的理由 |
|---|---|---|
| [MALL ACTION](https://github.com/rlorca/mall-action) | 同一長 prompt、多模型分支；可玩版本、源碼、AGENTS 執行規範；GPT-6.1 Sol 驗證紀錄 | 主測首選。再查只為模型新增、條件差異、成品遊玩或原始測試證據，不必重找基本規格。 |
| [8-Bit AI Arena / Ruinseed](https://frostsource.github.io/8bit-ai-arena/) | 長提示、程序生成冒險、Dungeon／Boss／戰鬥／存檔等；GPT-6 Astra/Sol/Luna、Opus 5.5 有成果 | 冒險玩法副主題；版本未跟到 GPT-6.1／Sonnet 5.5。只在發現新分支或更完整測試時更新。 |
| [Kart Blitz article](https://www.nathanonn.com/sonnet-5-5-one-prompt-game/) 與 [Turbo Karts 原 Reddit run](https://www.reddit.com/r/ClaudeCode/comments/1wsx03y/sonnet_55_high_oneshot_a_full_mario_kart_from_1/) | Sonnet 5.5 都是 user-level one-prompt + multi-agent showcase，但屬兩次獨立 run：Max/五小時版本改寫 prompt並給 browser/Firecrawl；High/67 分鐘版本為原始 clone prompt、lead+5 agents、424 calls、可玩建置及作者自報 tokens/cost | 能展示多代理高上限、也有真實可玩版；不能混算兩版或視為純模型單次輸出，均缺 source/共享驗收/盲評。原始 run prompt 含克隆既有作品，正式 benchmark 宜改寫為原創 kart brief。 |
| [Opus 5.5 三款一行提示遊戲](https://github.com/riba2534/claude-opus-5-5-demo) | 原句 prompt、三個 source/play links、程序生成素材、單會話自主查詢／測試／部署 | 強「極少提示、模型自定範圍」展示，但只有 Opus 5.5；已有詳細記錄。 |
| [Planet Pop 對照](https://ohmyunicorn.com/labs/dream-loop/tinyworld-sonnet55-vs-opus55/) | 同 prompt，Opus 一次、Sonnet 四次；5 個 playable、截圖、耗時／成本 | 3D 展示／重跑變異，不是高難度遊戲；Opus live session 與 Sonnet one-shot 設定不同。只作穩定度示例。 |
| [Single HTML Game Bench](https://chojondocho.github.io/single-html-game-bench/) · [README / prompt / 20-model matrix](https://github.com/chojondocho/single-html-game-bench/blob/main/README.md) | 同一 3D horror/RPG/roguelike prompt、20 client/model 組合、one-pass 未修首版 playable builds；GPT-6.1 Sol Max、GPT-6 Astra Max、Opus 5.5 Max 均在榜，尚無 Sonnet 5.5 | 目前最合適的 strict first-output 可玩素材對照；規格誇大且缺可重現客觀 rubric，作者排序為主觀實玩。只在新增模型／固定驗收／重跑時再檢查。 |
| [Game Bench](https://game-bench.piccini.app/) | 固定 prompt、空白 workspace、無人工 feedback；25 runs，四項權重；較新 GPT-6 Astra/Sol、Opus 5.5 等 | 評分方法與 agentic one-shot 參考；尚無 GPT-6.1/Sonnet 5.5。題目範圍一般，非上限。 |
| [Vibecode Bench](https://senko.net/vibecode-bench/) | 四固定 prompt（RTS／Voxel／Flysim／Minesweeper），可玩頁和 gist；Sonnet 5.5 (9/28)、Opus 5.5、GPT-6 Sol、Astra 等 | 多模型校準題組；題目明言 simple、限單 HTML，不能代替高難度主測。查過其模型日期與提示原文。 |
| [Lunar Scream](https://ultra.dev/projects/lunar-scream) | 同一「尖叫月球著陸器」提示；Opus 5.5、Fable 5.1、GPT-6 Astra、GPT-6 Sol；無修正、四款可玩、影片／源碼 | 規則最清楚的 strict one-shot 範例，但玩法小、版本略舊、無分數；只作方法校準。 |
| [One Shot Challenge](https://oneshotchallenge.ai/benchmark) | 2026-07 活動：101 builders、200 runs、25 models、141 可玩條目，盲評、不重試 | 參賽規模和記錄失敗／成本的方法參考；模型清單過舊，不重複當最新榜。 |
| [Goldie Bench](https://goldiebench.com/tasks/)；[Dragonrealm](https://goldiebench.com/tasks/dragonrealm)；[Grok 4.7 的 20 題 run](https://goldiebench.com/models/grok47) | 固定 prompt、one-shot、單一 HTML、no retries；Grok 4.7 run 在 20 題平均 7.15/10，Grok 4.6 同題 5.95，作者稱 head-to-head 勝 14/20；有 live playable demos、截圖及部分自動遊玩過程證據。可直接挑 Dragonrealm、Skyrim、RPG、Flightsim 看 build。 | 這是很新的可玩輸出庫／作者評測，不是高難度長規格題：題目 brief 短，評分者是網站作者；共用 Agent Operating System 堆疊和付費產品背景使其不等於模型裸跑。首頁任務／模型數量和子頁有差異，個別模型的日期／effort 也需逐筆核實。可作 Grok 4.7 新模型實物校準，不把 7.15 當跨站公平名次或主測成績。 |
| [OneShotLM](https://oneshotlm.com/) / [更新紀錄](https://oneshotlm.com/whats-new/) | 首頁與更新紀錄對 build/model 數量及更新日期不一致；大規模可玩成果索引，含兩階段自動／視覺評估描述 | 發現與評估方法參考；可見清單未見 Opus 5.5、Sonnet 5.5、GPT-6.x，不能代表最新前沿。後續僅在確認新模型收錄或版本數據一致時回查。 |
| [WorldBuild Bench July round](https://sandscape.app/worldbuild/rounds/ai-game-benchmark-2026-07-13) | 10 模型、3 題（arena/puzzle/racing）、29 builds；可比較和盲測 | 可玩及開放資料格式值得參考，但 7 月模型較舊且題目有限；非當前主榜。 |
| [GameASG-Bench](https://arxiv.org/abs/2609.21293) / [GitHub](https://github.com/areal-project/GameASG-Bench) | 學術 browser-native tasks、靜態與執行檢查、跨多 genres | 方法學與行為驗收參考；公開結果不含目前全部新模型，任務庫不是高複雜度完整遊戲 showcase。 |
| [A2Z GameSpec-Bench](https://arxiv.org/abs/2609.39564) / [repo](https://github.com/krafton-ai/a2z-gamespec-bench) | 長篇 GDD、需求依賴 contracts、scenario replay 與 playtesting | 最新複雜 spec／驗收方法線索，但包含迭代修復，不是只有一次生成；目前沒有 ready-to-play 新模型圖廊。 |
| [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | 97 個 2D/3D 單次 generation 題，另有修復與多輪優化 tracks | 和本題高度相關的學術設計，但結果較早、部分人評；保留方法參照，勿和公開新模型 demo 混排。 |
| [GameCraft-Bench](https://github.com/FreedomIntelligence/gamecraft-bench) / [demos](https://tongxuluo.github.io/gamecraft-bench-website/) | 140 個 Godot 2D 完整遊戲任務、15 個類型；交付完整專案和 replay traces，由 verifier 按實際操作證據及 rubric 評分。Open-World Airship Trader 有完整 prompt、GPT-5.5/Codex playable build、60.40 任務分和截圖。Repo 目前也公開該 task 的 rubric 與 reference solution。 | 是重跑最新模型、觀察完整遊戲系統如何整合的候選；不是 strict first-output，因依賴 agent harness／素材庫；現行榜單沒 GPT-6.1/Sonnet 5.5。範圍限 2D。重跑時須隔離公開的 rubric/reference solution，任務級報分，不直接引用總榜。 |
| [SWE-Game](https://arxiv.org/abs/2609.33678) | 247 個任務／41 款可執行 Godot 參考遊戲，含 brief-to-game、GDD-to-game、完成骨架、修復和移植；允許 agent 工具與素材 | 有玩家操作探針、參考輸入路徑、無輸入對照及功能／視覺分項驗證；方法可借鑑，但非原始輸出 one-shot。無公開逐模型 playable gallery／資料集，且未測 GPT-6.1/Sonnet 5.5。 |
| [AI Game Case catalog](https://aigame.zhumang.dev/) | Source-first 多類可玩遊戲索引，標記模型是否有來源佐證，也區分 playable 和 showcase | 發現候選遊戲用的索引，不是基準；每案仍需回到原貼文／repo 核對 prompt、流程和可玩性。 |
| [ohmyopus 149-case collection](https://ohmyopus.com/en) | 有原始來源連結的 Opus/Sonnet 案例整理；含 Opus/Fable/GPT-6 Astra 同題三類遊戲、Opus/GPT-6 Sol 平台跳躍與節奏遊戲等 | 用來發現案例，不保證每案都有 prompt 或 playable。已發現下列特定案例需追原始來源（下一段），不把二手摘要視為已驗證。 |
| [當日 minecart 對照](https://www.reddit.com/r/ClaudeAI/comments/1wx42fp/opus_55_vs_sonnet_55_same_prompt_a_mine_cart_ride/) | 2026-10-04 Opus 5.5 vs Sonnet 5.5；作者稱相同 prompt、兩個 fresh Godot project，以 Claude Code + MCP 讓模型自己 Play、drive、screenshot；影片展示生成遊戲。作者認為 Opus 更接近參考且地下段約一分鐘；Sonnet playtest 次數多一倍仍留下隧道破洞。兩者都沒做出物理礦車；按 API rate 成本 $7.02 vs $5.46。 | 真正近期的同題、同 harness 自述對照，但遊戲只有礦車旅程、缺原 prompt／公開 source 和 build、沒有固定共用驗收；它本身也揭示「能跑 MCP、可 playtest」不保證核心物理成立。保留校準案例，不列入上限主榜。 |
| [Promptslove Tumble brief](https://promptslove.com/blog/claude-opus-5-5-vs-gpt-6-astra/) · [影片](https://youtu.be/cwGSDctKCbk) | 2026-09-24 同一份長 prompt 比較 Opus 5.5 high 與 GPT-6 Astra xhigh；單檔 3D 彈珠建造遊戲，無物理引擎，自製 180Hz 物理、15 種構件、編輯器、8 個謎題、100 顆壓測及逐項驗收。 | 高價值的物理／系統壓力題；規格與驗收清楚，建議拿原 prompt 對最新模型重跑。現有文章只有作者描述與影片，沒有公開可獨立操作建置或 FPS／謎題測試紀錄；模型、effort 各一次，不採用作者勝負作成績。 |
| [EvalMap Jeep gallery](https://evalmap.ai/jeep/) | 2026-10-03 更新至 119 builds／80 scored／39 failed；同一短 brief，可直接操作每個成功遊戲；Sonnet 5.5 xhigh 48、GPT-6.1 Sol xhigh 45、Opus 5.5 xhigh 40、GPT-6 Astra 39；逐項記錄 1 分鐘實玩與 90 秒直行邊界測試。 | 收為最新 playable gallery 與可玩性／失敗率校準；對上限題偏簡單，精確 prompt 不公開，harness 隨模型／日期不一，主觀評分不是獨立排行榜。只在新日期／新模型／prompt 或 rubric 改變時回查。 |
| [Promptslove GPT-6.1 Sol builds](https://promptslove.com/blog/gpt-6-1-sol-review/) | 2026-09-30，GPT-6.1 Sol Ultra；3D marble-run 編輯＋物理遊玩、flight simulator；逐項 prompt 與作者親玩回饋 | 新模型單模型案例，提示與規格可借鑑，但目前是作者主觀 4/5、無同題模型／正式 playable artifact 連結；用於設計題目，不當 leaderboard。 |
| [Chase AI Sol vs Sonnet WoT test](https://codemypixel.com/es/blog/gpt-6-1-sol-vs-sonnet-5-5-real-world-tests) | 摘要稱相同 World of Tanks browser-game build job，Sol vs Sonnet 5.5；影片比較與主觀 split verdict | 尚未找到公開 exact prompt、源碼/可獨立玩的兩款 build、對稱條件；文章為二手轉述，降級，不作主基準。 |
| [Godot Opus/Sonnet kart video](https://powerhub.dev/blog/sonnet-opus-5-5-kart-game-test) | 2026-09-29 一則相同 prompt，影片稱兩款可玩，作者偏好 Opus 操控 | 有畫面但缺 exact prompt、能玩的獨立版本和細緻驗收；與 Kart Blitz 是不同實驗，不得合併成一套數據。 |
| [Dead Signal：Sonnet 5.5／Opus 5.5 zombie FPS](https://github.com/bridge-mind/sonnet-5-5-zombies-game) · [Opus 專案](https://github.com/bridge-mind/claude-opus-5.5-zombies-game) · [實況逐字稿片段](https://postcutoff.com/v/yt-bridgemind-vibe-coding-with-claude-sonnet-5-5/) | 新核對到兩個可本地執行的 source repo、Vitest gameplay rule tests、Sonnet 5.5 實況影片；Sonnet 任務有 55 秒 relay、裝備／經濟升級、需先打頭盔的 armored boss、污染倒數前直升機撤離，Opus 版有不同 relay/exfil 規格。Sonnet 作者報 49 分鐘／$177。 | 比先前 Reddit 摘要有更好的原始碼與測試證據，但尚無公開部署 playable URL、原始 prompt/session transcript，兩個模型規格也未核實相同；作者測試不證明全部撤離、受傷、庫存及重開流程。升級為可查核 showcase，仍非受控模型比較。 |
| [Sonnet 5.5 vs GPT-6.1 Sol chess game](https://www.reddit.com/r/ClaudeAI/comments/1wwz9av/i_let_sonnet_55_play_a_full_chess_game_against/) | 兩個模型對弈；同一 app 由 GPT 建置、兩模型透過 MCP 玩長盤棋；記錄時間／token | 這是「模型玩遊戲」而非「一次生成完整遊戲」基準，排除於本主題。 |
| [SWE-game-generation research paper search](https://arxiv.org/abs/2605.28258) | Play2Code 研究逐步 GUI 生成／修改，報告互動式回饋提高 rubric pass rate | 不是最新前沿模型 one-prompt leaderboard；只借鑑為何靜態畫面不足、要測互動狀態。 |
| [同作者水上競速系列：GPT-6.1 Sol](https://github.com/KJLKurt/waterslide-game-gpt-6.1-sol)／[Opus 5.5](https://github.com/KJLKurt/waterslide-game-opus-5.5)／[GPT-6 Astra](https://github.com/KJLKurt/waterslide-game-astra) | 三個相似 3D waterslide build 都可玩並有 source；GPT-6.1 Sol 約 52 分、$1.93、49 API calls，另有 auto-review child；Astra 約 35 分、$8.22；Opus 約 68 分、$18.50。三版各有碰撞／完整比賽／手機觸控／離線或 Playwright 測試資料。 | 很適合作為可比較的物理／競速副題和測試方法參照。公開 prompt 只可見摘要或被截斷，Opus prompt 為 source-derived reconstruction；因此目前能說是同一題型系列，不能證明逐字同 prompt或把三者當公平榜。
| [AI for Mortals Sonnet 5.5 review](https://www.aiformortals.co/blog/sonnet-5-5) / [Diablo ARPG outputs](https://www.aiformortals.co/builds/diablo-arpg-sonnet-5-5) | 4 模型同題高規格 ARPG，原 prompt、逐模型可玩輸出、截圖、影片、token／時間／成本皆公開；要求四層地城到 boss、建構／戰鬥／戰利品和自動化通關 | 高難度同題副測首選之一。Claude Code 與 Codex harness 不同，沒有 GPT-6.1 Sol；補新模型 run 後再考慮列主榜。 |
| [Fable 5.1 vs GLM-5.3 one-prompt games](https://github.com/Nipale-ai/fable-5-1-one-prompt-game) · [GLM result](https://nipale-ai.github.io/glm-5-3-one-prompt-game/) | 同一提示的 NEON WARDEN／VESPERA，可玩輸出、截圖、建置指標與自動遊玩記錄公開 | 高工具 agentic ceiling 參考；RTX 5090 與 Blender/ComfyUI/多模態工具造成條件綁定，兩模型各一 run；不等同純模型公平比較。 |
| [TETHER Sonnet 5.5](https://agentgames.dev/play/tether) | 低約束 prompt、81 分鐘、可玩 roguelite、逐輪升級與內部 reviewer/調參 bot | 最新低提示自選範圍案例；缺公開 repo/transcript，不能同題排名。 |
| [Mini golf three-model comparison](https://chooseto.ai/watch/NzyP4VjkrvM) · [Opus 5.5 source](https://github.com/leonvanzyl/3d-golf-opus) · [Fable 5.1 source](https://github.com/leonvanzyl/3d-golf-fable) | Sonnet 5.5、Opus 5.5、Fable 5.1 在 Claude Code 使用同一份 3D mini-golf prompt；影片逐款實玩。Opus 與 Fable 的公開 build 各有 9 個主題洞、自製 3D 球物理、 moving obstacles、記分／存檔；repo 含逐洞求解與碰撞 fuzz 驗收。原始 prompt 和三款完整 build 由作者在 Skool 提供，本輪只獨立核實 Opus/Fable 公開 repo，未找到 Sonnet 專案。 | 新增為「3D 物理＋多關卡」副測；比 ARPG 少經濟／敵人／角色進度。公開頁未證明每模型是否只有一次訊息、迭代工具條件是否一樣，也未獨立取得 exact prompt/三款成果，因此影片可看真實操作但不能算嚴格公平 one-shot 排名。 |
| [Ropilot Studio](https://ropilot.ai/) | 宣稱可用 GPT-6 Astra、GPT-6.1 Sol、Opus 5.5 等透過 Roblox Studio／Blender 一句提示生成並 playtest；官網有飛機與 UI 影片 | 工具產品展示，不是固定任務的模型對照；未找到同一公開 prompt 的多模型輸出資料，不列為 benchmark。 |
| [PUBG-style game post](https://www.linkedin.com/posts/yuzzy_opus-55-vs-gpt-6-astra-both-built-a-activity-7508532020268998657-q7Fg) | 已可讀原作者貼文：Opus 5.5 和 GPT-6 Astra 各用一個 prompt 建 browser PUBG-style game；列 2 km 島／8 城鎮／可進入建築／24 bots／30 mocap 動畫等，Astra <3h、Opus 10h，Astra 聲稱 20 tests passed。Opus 用 Scenario MCP + Gemini 3.1 Lite + Tripo 3.1 自製素材，Astra 用免費資產庫。 | 升為近期高複雜度 showcase／候選同題比較，但仍未取得 exact prompt、source、兩個 playable build 或 tests 清單；素材與工具不對稱，精確發文日期也未核實。無法公平排名。只有上述原始 artifacts 出現時再查，不重做同篇搜尋。 |
| [Moe Lueker：四模型跑步遊戲＋島嶼建造](https://moelueker.com/blog/claude-opus-5-5-vs-gpt-6-astra) | Opus 5.5、GPT-6 Astra/Sol/Luna 各在空資料夾、各自 Git repo 跑相同兩題；作者稱不協助、不修正，記錄 token 成本／耗時並附原實測截圖和影片。島建題系統較多，runner 作者自稱刻意簡單。推理設定 Luna max、其餘 runner xhigh／島建 high。 | 同題 one-shot 方法與成本透明度參考；GPT-6.1 Sol 尚未發布時所做，沒有 GPT-6.1／Sonnet 5.5；文中公開上線遊戲是 Opus 後續加四關、經 follow-up prompts 的版本，不能當首次產物。 |
| [Testing Models Coding Arena](https://testingmodels.com/coding) / [method](https://testingmodels.com/method) | 宣稱 54 challenges、148 個模型變體，同提示、即時 playable output、盲評投票；任務包含 roguelike、卡牌、塔防等約 43 種遊戲／創意編碼題 | 有利於瀏覽不同模型的可操作輸出與題庫；截至頁面 2026-09-06，模型名單未見 GPT-6.1 Sol／Sonnet 5.5，很多挑戰是單 HTML 小型任務、資料量新舊混合，不能作最新上限排行。成本由輸出檔案大小估算、不含 input/reasoning。 |
| [Cheer Self AI Sonnet 5.5 案例索引](https://cheerselfai.com/en/usecase/claude-sonnet-5-5) | 彙整 2026-09-28 左右多個 one-prompt 案例，包括 Sonnet/Opus 同 prompt 做 GTA Rio、足球與 Squid Game，以及 Mario Kart、Fortnite 等 | 索引探索入口，不是原始 benchmark；這些高複雜案例本輪未核實完整 prompt、兩邊 playable links 和對稱條件，留作線索而非採信。 |
| [Sakura Rally](https://github.com/SummerEngine/sakura-rally) | Opus 5.5 約 5 小時 agentic 生成的 Godot rally game，subagents、完整源碼與 detailed QA；作者列出後續兩輪 playtest feedback 修改 | 很強的作品／QA 示範，但「一次初始 prompt」後有玩家回饋再改、prompt 未公開，且不是線上可玩 build；勿當作 strict one-shot 成績。 |
| [SkaLab GPT-6.1 / Claude dungeon comparison](https://skalablog.com/p/gpt-6-1-sol-vs-claude-which-ai-builds-a-better-game/) | 同一 dungeon crawler 三階段，最新 Sol/Sonnet/Opus；builder-critic agent 用 Blender 和 Godot 自主迭代，報價差與畫面/遊玩判斷 | 有最新模型/高複雜度，但多輪流程、影片整理二手、沒有 exact prompt 或公開 playable；只列後續追原片／build 的線索。 |
| [Duncan Rogoff LinkedIn six-task blind test](https://www.linkedin.com/posts/duncanrogoff_i-tested-sonnet-55-vs-gpt-61-sol-on-6-activity-7511140065314701312-kVdU) | Sonnet 5.5 vs GPT-6.1 Sol，同 prompt 一次生成六種輸出，其中含從 start screen 到 game over 的 3D browser game；作者稱盲測、記成本/時間/截圖 | 最新且測試方式很接近目標，但目前貼文沒有公開 exact game prompt、artifact 或完整結果；不可根據留言投票得主下結論。 |
| [Deep20Bench](https://deep20bench.com/) | 2026-09-30 edition 1.1，18 個模型包含 GPT-6.1 Sol/Sonnet 5.5；每模型 10 hidden subjects × 3 rounds、完整 transcript、成本和 confidence interval | 這是 LLM 玩「二十問」的推理 benchmark，不是生成遊戲；記錄為排除項，但三次重跑和公開逐回合資料可作本研究的方法參照。 |
| [Fallout: New York Opus 5.5 fan game](https://www.linkedin.com/posts/chris-first_ai-gamedev-claudeai-activity-7510415971850039296-XTfE) | 宣稱有 70–117 個探索地點、角色、武器、任務／對話／VATS、約 21 MB browser output，Opus 5.5、多 agents；報導稱後來下架 | 作品宏大，但作者用多代理像小型工作室方式做，並非一次提示；原 prompt、迭代次數和可玩成品目前無法核實／已下線，不能當 benchmark。 |
| [BitsMinds Hill Climb Racing one-shot](https://www.bitsminds.com/news/gpt-6-astra-vs-claude-fable-5-1-hill-climb-2026) | 同 prompt、同為一 run、成品原樣 playable embed；Astra 28m24s、Fable 75m38s；自測含 Chrome 自動化、30+ 截圖、幀率測試。人工評分 15–14；文章定位出 Fable 大部分空中硬幣無法取得的關卡 bug | 實測與驗收方法很值得參照：模型自己跑過仍可能漏掉關卡設計錯誤。遊戲範圍僅一關、模型是 GPT-6 Astra/Fable 5.1，作者人工非盲評；不可作最新上限案例。 |
| [AI for Mortals：Astra vs Fable FPS shooter](https://www.aiformortals.co/blog/gpt-6-astra-vs-fable-5-1) | 完整 browser FPS prompt 要求敵人 AI、可破關對戰、killcam、負載畫面、動作捕捉、60fps、QA 截圖與部署；直接可看兩個模型輸出及各自 tokens/cost | 主題複雜且驗收細，但該文報告成本包含後續 build passes，不能無條件當成純 one-shot 比較；模型較舊且造價高，留作設計／QA 範本。 |
| [Rocket simulator Astra vs Fable 5.1](https://futureproofagents.com/blog/build-games-with-gpt-6-astra/) | 二手案例文章稱 Fireship 作者在同一時間給兩模型同一火箭建造／入軌 prompt，玩後發現 Astra 畫面精美但玩法窄，Fable 有更多模組與科學計算 | 找到同一長期任務可測視覺 vs 深度玩法取捨的線索；本輪未找到逐模型公開 playable/repo/完整 run metrics，先不作比較依據。 |
| [Moe Lueker：跑酷與島嶼建造](https://moelueker.com/blog/claude-opus-5-5-vs-gpt-6-astra) | 四模型（Opus 5.5、GPT-6 Astra/Sol/Luna）各跑兩個相同提示，無修正；有每題模型輸出描述、手工圖像、耗時與 API 等值價格。公開 playable 是 Opus 後續追問後擴建的版本 | 方法透明但遊戲一題刻意簡單、一題較多系統；GPT-6.1 尚未推出。保留為成本／prompt控制參考，首次模型輸出應看文章圖像，不能拿網站成品當 one-shot。 |
| [Pokemon Red play agent replay](https://www.reddit.com/r/ClaudeAI/comments/1wsu7l9/i_replayed_sonnet_55s_starter_pick_21_times_with/) | Sonnet 5.5/Opus 5.5 玩現成 Pokémon Red，讀遊戲 RAM milestone，並重跑相同起始決策 21 次觀察選擇分佈 | 測模型玩遊戲的行動策略與重跑方差，不是模型生成遊戲，排除於生成任務。 |
| [Sonnet 5.5 vs GPT-6.1 Sol GBA enemy sprite](https://www.reddit.com/r/codex/comments/1wtwyzy/test_sol_61_vs_astra_vs_opus_55_vs_sonnet_55/) | 已有遊戲專案裡，同規格做一個 GBA 16 色敵人 sprite 並比成本；不含從零生成完整遊戲。 | 這是遊戲素材／專案編輯任務，不是一次生成完整遊戲。 |
| [GameLogicBench](https://arxiv.org/abs/2609.21562) | 72 Godot logic tasks、403 scenarios、1,451 tests、逐 tick 規則驗證，測試器 mutation validated | 不測完整生成；作為本地 benchmark 驗收方法參考。 |
| [WebGameBench](https://arxiv.org/abs/2605.17637) | 111 瀏覽器任務，以真實互動區分 excellent/usable/unusable | 借鑑把「能玩」和「完成規格」拆開；模型與題目較舊。 |
| [DogLM](https://github.com/mikeushakov/doglm) | 5 款小型 browser games × cued/uncued PRD；從一則 prompt 生成自包含 HTML，以 syntax gate + LLM code judge 評「玩家能否摸狗」；排行榜 2026-09-05 含 GPT-6 Astra | 作「未明說需求／自發機制」的窄題補測和多次生成方差參照；不測大型完整遊戲，靜態讀 code 也不等於實際互動。 |
| [GameDevBench](https://waynechi.com/gamedevbench/) | 333 個 Godot 開發任務、88 篇教學；2026-10-01 新增 GPT-6.1 Sol 69.97%±4.9、GPT-6 Astra 68.8%±5.0；best harness + multimodal feedback 的 pass@1 | 最新模型遊戲開發任務參照；任務在已有教學／專案中完成，不是完整遊戲從零生成；不同 harness 與視覺回饋影響分數。 |
| [OpenGame / OpenGame-Bench](https://arxiv.org/abs/2604.18394) · [paper-linked repo](https://github.com/leigest519/OpenGame) | 150 個網頁遊戲 prompt、五類，動態 browser execution + VLM 評 Build Health／Visual Usability／Intent Alignment（每項 0–100）；每題以三個不同 random seeds 重跑。Sonnet 4.6 驅動 agentic workflow 得 72.4/67.2/65.1，baseline 亦含 Sonnet 4.6、GPT-5.1、Gemini 3.1 Pro。Repo gallery 有單提示可玩成品和 prompts；但 evaluator README 仍稱評測 pipeline 即將釋出，完整 task corpus／評測器未能獨立重跑。 | 方法上很有價值：把建置、可見互動和需求履行分開，並對每題重跑。它允許模板、debug skill、自動修復；論文消融顯示零修正（T=0）明顯較差，所以不能拿來代表 strict one-shot。模型較舊、評測流程未完整公開；可借 rubric，不能當最新模型排行榜。 |

### OhMyOpus 案例庫中新發現的待查原始案例

[索引案例庫](https://ohmyopus.com/en) 是大量案例導航，不是一次生成 benchmark。它列出幾個比一般小遊戲更適合繼續追的來源：

1. [Opus 5.5 / Fable 5.1 / GPT-6 Astra 的 RTS、Voxel、飛行模擬](https://ohmyopus.com/en/c/senko-3games)；原始任務在 [Vibecode Bench](https://senko.net/vibecode-bench/)，提示、模型日期、可玩成品已核對，見上節。
2. [Opus 5.5 / GPT-6 Sol 的平台跳躍與節奏遊戲同頁競賽](https://www.youtube.com/watch?v=JyOpqah2ogA)，摘要稱相同一頁英文 brief、一次完成、四個未改成果、記耗時／bug／API 成本並以模型盲評。不過本輪 YouTube 頁面無法載入，還沒有核實 prompt 或 playable links，暫列高價值待查，不引用其結果作結論。
3. [Fortnite 風格 battle royale](https://x.com/MiaAI_lab/status/1970134555002050966) 是另一條 Opus 5.5 showcase 線索，有空降巴士、風暴倒數 minimap、血條和物品欄；仍未核實 exact prompt／playable build。另有下列 Sonnet 5.5 案例已找到逐字 prompt 和 42 秒短片，但沒有穩定 playable 或 source。
4. [DOOM clone 加自動遊玩代理](https://github.com/vasu-devs/doom-ai-autoplay)，索引稱 AI autoplay 8/8 勝場、平均命中率 93.4%；這測出模型是否能連遊戲與自動玩家一起建，並非共同提示的跨模型生成比較。
5. 新搜尋到 [Senko Bench](https://senko.net/vibecode-bench/) 在 9/28 新增 Sonnet 5.5 同題 RTS/Voxel/Flysim，提示簡化且缺 GPT-6.1；已降為副測校準組。

## 來源與可信度提醒

公開頁面常把「一次提示」與「模型自主跑許多代理／工具」合稱 one-shot。每筆案例都要分清楚。若只有作者自述，標為自述；若有公開程式碼和測試才可說可查核；除非有第三方重跑，不要說成獨立驗證。模型版本可能在調研期間快速更新，請在每輪對話中重查日期及模型標籤。

## 2026-10-04 新增搜尋結果：最新可玩案例與正式方法

### 新增的高價值可玩案例

| 案例 | 已核對內容 | 適用位置與限制 |
|---|---|---|
| [Slipstream：GPT-6.1 Sol 水上競速](https://github.com/KJLKurt/waterslide-game-gpt-6.1-sol) · [直接遊玩](https://kjlkurt.github.io/waterslide-game-gpt-6.1-sol/) · [策展核實頁](https://github.com/AgentsLoop/awesome-opus-5.5-games/blob/main/games/slipstream/readme.md) | GPT-6.1 Sol extra-high；作者報告 51 分 58 秒、49 次 API 呼叫、約 $1.93、兩個 rollouts（主工作與自動審查 child）。3D 水上滑道競速有 12 名 NPC、捷徑、Race/Practice、checkpoint、DNF/完賽、存檔、觸控與離線/PWA；README 記錄 Playwright 測試、截圖與 QA。 | 很新的高品質單模型 demo，適合看 GPT-6.1 Sol 能力；沒有完整原始使用者 prompt，且自動審查 child 不符合「單 agent 原始輸出」嚴格定義。Splash Rush 是否同題仍未核實；不得與 Mall Action 同題榜混算。 |
| [Fable 5.1 vs GLM-5.3 one-prompt games](https://github.com/Nipale-ai/fable-5-1-one-prompt-game) · [Fable playable](https://nipale-ai.github.io/fable-5-1-one-prompt-game/) · [exact prompt](https://github.com/Nipale-ai/fable-5-1-one-prompt-game/blob/main/prompt.txt) · [GLM playable](https://nipale-ai.github.io/glm-5-3-one-prompt-game/glm/) | Fable 5.1 high：24.2 分鐘／75 turns／95,832 output tokens／$9.90／首輪 gate、無 retry、4.4 MB；GLM-5.3：27.3 分鐘／146 turns／106,966 output tokens／$9.39／13.9 MB。共同提示要求一個離線、自包含 3D HTML，使用 Blender、ComfyUI、FLUX、LTX 與 ACE-Step 等工具。GLM 頁記錄 Playwright 收齊碎片到勝利、零 console errors。 | 強「一次 user task 下自主 agent/tool 整合」展示及重跑種子；同樣 RTX 5090 與素材鏈，但仍是各一 run、作者自述 QA，工具依賴較重，不能當純模型公平排名。 |
| [TETHER：Sonnet 5.5](https://agentgames.dev/play/tether) | Sonnet 5.5 high；頁面報 81 分鐘、1,035,000 tokens；prompt 刻意開放，只要求模型自選能展示能力的遊戲並包含逐輪升級進展。成品有五個程序生成區域、18 個升級、遺物、貨幣與結局／無盡模式；頁面標示 2026-09-30 v1.1，並稱 bot 調整過經濟／難度、reviewer 找出六個 bug。 | 適合觀察低約束下模型如何界定遊戲範圍，且直接可玩；但只有 Sonnet 一個模型、使用內部 agents、缺 repo/session transcript，不是同 prompt 排名。 |
| [Sakura Rally：Opus 5.5](https://github.com/SummerEngine/sakura-rally) | 2026-09-28 起公開 Godot 4.7/Summer Engine 原始專案；README 自述約 5 小時、Opus 5.5 一次初始 prompt，使用多個 subagents 造車、場景、物理、音訊、UI；有雙季節賽道、2 公里連接道路、車輛／賽事模式、AI rivals、程序工具和大量 physics/game-flow 自動檢查。 | 極高複雜度的真遊戲專案，源碼和 QA 非常充足；但作者明說後續 playtest notes 另加第二、第三輪改版，原始 prompt 未見、沒有線上 browser playable，故只算 agentic showcase，不可把現在的完整度歸於一次原始輸出。 |
| [SkaLab：GPT-6.1 Sol / Sonnet 5.5 / Opus 5.5 地城遊戲](https://skalablog.com/p/gpt-6-1-sol-vs-claude-which-ai-builds-a-better-game/) | 2026-10-04 搜尋到的三輪 Godot dungeon crawler 比較：Blender kit、騎士和怪物、可玩遊戲；採 builder/critic agent，寫 Python 操作 headless Blender，模型決定停止；報成本與遊玩品質，Sol、Sonnet、Opus 全有結果敘述。 | 是 GPT-6.1、Sonnet 5.5、Opus 5.5 同題的近期線索，但屬多輪 agentic workflow，非一次提示無回饋；原 prompt 和直接 playable build 本輪未找到，來源是影片轉寫／二手整理，先作待查。 |
| [BitsMinds：GPT-6.1 Sol vs Opus 5.5 Hill Climb](https://www.bitsminds.com/news/claude-opus-5-5-vs-gpt-6-1-sol-hill-climb-2026) | 2026-09-30 發布；同一 Hill Climb brief、兩個可直接玩的原樣成品。作者稱 GPT-6.1 Sol 跑 57m38s、Opus 5.5 跑 98m06s（Opus 作品 9/23 已完成，這次沿用凍結版本）；人工非盲評 13/20 vs 19/20，含畫面、物理、聲音、玩法和狀態測試。 | 目前最直接的新模型同題可玩對照之一。規格有選單、二輪車懸吊、丘陵物理、鍵盤／觸控、翻車／燃料失敗、免重載重開；但只測一關，樣本各一、評分非盲，Claude Code subagent 與 Codex CLI harness 不同，模型讀各自持久記憶。適合做同題對照／方法參考，不足以代表長流程遊戲上限。 |
| [BitsMinds：GPT-6.1 Sol vs GPT-6 Astra vs GPT-6 Sol 三項互動作品](https://www.bitsminds.com/news/gpt-6-1-sol-vs-gpt-6-astra-vs-gpt-6-sol-build-off-2026) | 2026-09-30 發布；三個 brief 各一 run、單檔輸出、Codex 中禁止瀏覽器與執行程式、最高推理；成果為 SVG 交流道動畫、海濱遊樂園動畫與火箭發射頁面。GPT-6.1 Sol / Astra / GPT-6 Sol 得 9/9/4；作者報 66m51s / 70m48s / 17m39s。 | 雖含動畫與狀態序列，但沒有玩家控制或完整遊戲 loop，故不是遊戲生成比較。可借「無執行回饋的一次輸出」控制法，以及用同一任務重複呈現可觀察的幾何／動畫陷阱；評分由作者非盲評，且 Astra、GPT-6 Sol 沿用舊 run，exact prompt files 未公開。 |
| [BitsMinds：Sonnet 5.5 vs Opus 5.5 vs GPT-6 Astra vs GPT-6 Sol 三項互動作品](https://www.bitsminds.com/news/claude-sonnet-5-5-vs-opus-5-5-vs-astra-vs-sol-build-off-2026) | 2026-09-29 發布；同三項 brief、每模型各一次、Claude Code / Codex 各自最高推理、禁止瀏覽器與程式執行；分數 Opus 13、Sonnet 12、Astra 11、Sol 5。Sonnet 5.5 原始 run 為新做，其他三者沿用之前已發表的成果。 | 新模型覆蓋佳且頁面展示完整輸出圖像／動畫，可作嚴格 first-output 及跨平台 harness 控制參考；作品仍是 SVG／發射動畫而非遊戲，不能用其排名回答「AI 一次生成完整遊戲」；同樣有作者非盲評、exact prompt files 未公開、舊作品混入等限制。 |
| [Semper Phoenix：Blockworld](https://semperphoenix.com/lab/) | 2026-10-01 作者展示 Claude Opus 5.5 high 以「Can you create a Minecraft clone?」生成的瀏覽器方塊世界；作者報約 18 分鐘、無手工改碼，附可玩版與圖片。包含程序世界、洞穴、森林、海洋、雪峰、TNT、存檔；模型自行測試後，作者的自動 code review 又促使模型修一個 bug。 | 展示低約束提示下的範圍選擇與實作；不是公平同題比較，且 review 修 bug 意味最終 build 不是未觸碰的首次輸出。可借作「模糊 prompt」副測，不納入 strict first-output 成績。 |
| [Ink Field：Opus 5.5 one-prompt platformer review](https://www.reddit.com/r/ClaudeAI/comments/1wnzcbg/i_gave_opus_55_one_prompt_and_one_hour_to_make_a_game_then_actually_played_the_thing/) · [完整實玩影片](https://youtu.be/56oLTK1Jseo) | Godot 4、Opus 5.5 Max；作者稱一則提示、約 1 小時，之後 hands-off；評論影片實際走完結局並檢查 mechanics、checkpoint、聲音、操作與內建 tests。評論區只披露「完整遊戲、限一小時」的極簡原 prompt；作者自己認為 gameplay 無聊。 | 可借作人工完整通關與結局驗收例子，影片比截圖更有價值；沒有 exact task brief、source、可玩 link、成本或第三方重跑，而且任務規模不大，不納入上限比較。 |
| [Sonnet 5.5 Fortnite-style Battle Royale prompt](https://jasonzhu.ai/en/prompts/claude-opus-5-5/2104779190277181699) · [原 X 貼文](https://x.com/mdaman010/status/2104779190277181699) | 策展頁署名 Aman @mdaman010、日期 2026-09-29，收錄逐字 445 字 prompt：第三人稱相機與移動／瞄準／射擊／裝彈、bots、武器拾取、血量／護盾／背包／小地圖、牆與坡道建造、縮圈 storm、彩色小島；作者稱 Sonnet 5.5 約 2 小時 54 分完成，附 42 秒影片。原 X 貼文本輪回查遇 403，故細節只按策展頁標記。 | 新增為高系統密度、近期單模型 showcase／測試題型；逐字 prompt 是實用資產。仍未找到可穩定開啟的 playable build、source 或獨立 QA；條件／成績來自作者與策展頁自述，不能當模型比較分數。只有 source/build 或同題新模型 run 出現時才回查，不重搜相同 X status／prompt。 |
| [GPT-6.1 Sol demos：Ashen Vigil](https://ruocco.it/ai-demos/gpt-6-1-sol/) · [直接遊玩](https://ruocco.it/ai-demos/gpt-6-1-sol/ashen-vigil.html) | 2026-09-30 索引稱 GPT-6.1 Sol medium、一次 prompt、無回饋／手改；Souls-like boss fight 有輕重攻擊、閃避、格擋／招架、鎖定、法術、補給、雙階段 boss，作者報 5.5 分鐘／$0.21。 | 最新可玩單模型 showcase；缺公開原 prompt 和同題其他模型，無法當對照。 |
| [Opus 5.5 長規格提示收集](https://github.com/TripoGrowthLab/awesome-opus-5.5-prompts) | 新收錄 WebGL2 survival sandbox prompt，要求單 HTML、無第三方 library、程序生成 16×16×128 chunks、多 biome／洞穴／光照／水與熔岩／晝夜、兩種模式、crafting、furnace、chest、mob、農耕、存檔和第一／第三人稱。另有 2026-10-02 UE5.8 熱帶島 open-world prompt，包含多生態區、建物／洞穴、徒步／多種載具、動物、天候、Lumen/Nanite、Sonnet subagents 與 36 小時目標。 | 是高上限題目素材，不是已核實 benchmark：大多只有社群貼文／提示整理，未確認穩定 playable、原始 session、測試條件；UE5 題明顯是長時間 agent goal + subagents，不能冒稱一次生成。 |
| [AI Fire：GPT-6.1 Sol Browser OS + 兩款 3D 遊戲](https://www.aifire.co/p/gpt-6-1-sol-in-codex-on-3-hard-tasks) | 2026-10-01 作者提供完整 prompt：純單 HTML browser OS，桌面視窗可拖曳／縮放、至少五個 app 跨 app 持續互動，內嵌 GTA-style 城市 sandbox 與 3D 飛行 checkpoint 遊戲；作者報 33m42s，附 OS 與遊戲截圖，稱 Journal 有跨 app 遊戲事件。 | 高整合度的壓力題素材；混合 OS 與兩款遊戲，非純遊戲。無 repo／可玩 build 或逐項驗收，只有作者截圖與自述。若採用，需拆開遊戲品質與 OS 跨 app 整合分數。 |
| [Duncan Rogoff：Sonnet 5.5 vs GPT-6.1 Sol 六任務盲測](https://www.linkedin.com/posts/duncanrogoff_i-tested-sonnet-55-vs-gpt-61-sol-on-6-activity-7511140065314701312-kVdU) | 作者稱兩模型各跑六項同 prompt one-shot 任務、無 skill/reference/follow-up，其中一項是「3D browser game，start screen 到 game over」；盲測、每案記時間/token/cost/品質，工作中有截圖 timelapse。 | 是符合最新模型交叉測試的強線索，但貼文沒公開遊戲 prompt、成品連結或可讀完整結果表；本輪只能核實作者摘要，尚不能視為可重跑或可玩的比較。 |
| [AI for Mortals：Diablo-style action RPG 同題比較](https://www.aiformortals.co/blog/sonnet-5-5) | 2026-09-29 公開一份 10 條驗收條件的完整瀏覽器 ARPG prompt；同題實測 Sonnet 5.5、Opus 5.5、Fable 5.1、GPT-6 Astra（Sonnet 5 加入較晚，未跑此題）。要求城鎮、四層程序地城、頭目、至少四技能、五類敵人、掉落／裝備／商店、存檔，並以自動化實際打到頭目勝利。四個模型結果頁可點開直接遊玩，文章同頁列 token、API 等值成本、耗時及遊玩影片；Sonnet 5.5 81 分鐘／$19.54，Opus 53 分鐘／$12.69，Fable 52 分鐘／$15.82，GPT-6 Astra 36 分鐘／$7.24。 | **目前最適合作為已公開的高難度同題副測之一**：prompt 長、要求多系統和完整通關，也有實際可玩成果與成本。作者用各家 coding agent（Claude Code／Codex）和 high + goal mode，工具環境不同；模型集缺 GPT-6.1 Sol，影片盲測但非第三方重跑。與 Mall Action 相比，它更方便直接逐模型遊玩和看實測影片，Mall Action 更新模型覆蓋更好。 |
| [OhMyOpus 摘要：Opus 5.5 / GPT-6 Sol 平台跳躍與節奏遊戲](https://www.youtube.com/watch?v=JyOpqah2ogA) | 案例索引稱同一英文 brief、一次提交、四個未改成果，記錄耗時／錯誤／API 費用並盲評。 | YouTube 本輪無法載入，精確 prompt、playable/repo 尚未確認；列作待查線索，不用其成績或宣稱支持結論。 |

**AI for Mortals 原始成果入口**：[Sonnet 5.5：Ashenmoor](https://www.aiformortals.co/builds/diablo-arpg-sonnet-5-5) · [Opus 5.5：Glassmourn](https://www.aiformortals.co/builds/diablo-arpg-opus-5-5) · [Fable 5.1](https://www.aiformortals.co/builds/diablo-arpg-fable-5-1) · [GPT-6 Astra](https://www.aiformortals.co/builds/diablo-arpg-gpt-6-astra)。文章實際遊玩截圖（來源圖片）：

![Sonnet 5.5 Diablo-style ARPG 實測畫面](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/diablo-arpg-sonnet-5-5.jpg)

其他模型畫面：[Opus 5.5](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/diablo-arpg-opus-5-5.jpg) · [Fable 5.1](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/diablo-arpg-fable-5-1.jpg) · [GPT-6 Astra](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/diablo-arpg-gpt-astra.jpg)。

### 正式基準研究：該借方法，不要誤認為最新 demo 榜

| 研究 | 已查到的設計／結果 | 對本研究的用途與缺口 |
|---|---|---|
| [GameASG-Bench](https://arxiv.org/abs/2609.21293) · [repo](https://github.com/areal-project/GameASG-Bench) | 47 個 browser-native 任務、12 類（32 個 2D、15 個 3D），固定規格及單一 index.html；預設一次生成、最長 60 分鐘。產物在隔離環境跑靜態契約與 headless Chromium 行為測試。GPT-6 Astra strict success 26/47（55.3%），而平均動態檢查通過率 93.2%，說明平均分會掩蓋整題漏項。 | 最適合借 strict task success、測試介面隔離與行為檢查；不是一題超大型完整遊戲，模型表尚缺 GPT-6.1/Sonnet 5.5。 |
| [A2Z GameSpec-Bench](https://arxiv.org/abs/2609.39564) · [repo](https://github.com/krafton-ai/a2z-gamespec-bench) | 100 份長 GDD；大型 50 份平均約 26,297 tokens、84 個 outcome requirements，含互相依賴系統。Fable 5.1 77.0、GPT-6 Astra 71.6。用 source review、scenario replay、adaptive playtest 等證據。 | 借它的 dependency-aware requirements 清單，適合 Mall Action 多系統驗收；總分包含 revision/feedback，不能當一次生成分數。論文稱資料可用，但 repo 尚不完整，沒有公開可玩成果圖廊；目前沒有 GPT-6.1/Sonnet 5.5。 |
| [SWE-Game](https://arxiv.org/abs/2609.33678) | 41 款 Godot 遊戲、247 項任務、13 類，涵蓋從 brief/GDD 建立、完成、修復至引擎移植；測模型包含 Opus 5、GPT-5.6 Luna 等。使用 evaluator probes、操作路徑、agent 自示範、無輸入對照及視覺評估。 | 借它檢查操作是否真的影響玩法、結果是否由玩家輸入觸發；允許 agent 工具、輸入可能含素材／影片，不是零工具 zero-shot。未找到公開 repo/data/playable gallery，未測 GPT-6.1/Sonnet 5.5。 |
| [GameLogicBench](https://arxiv.org/abs/2609.21562) | 72 個 Godot 邏輯任務、403 個手工情境、1,451 tests，逐模擬 tick 檢查狀態轉移，並以 mutation validation 檢查測試器。 | 借逐 tick 規則斷言與測試器自身驗證；它測 gameplay logic，不測從零生成完整遊戲。 |
| [WebGameBench](https://arxiv.org/abs/2605.17637) | 111 個瀏覽器遊戲任務，真實瀏覽器分為 EXCELLENT／USABLE／UNUSABLE，含人工覆核；論文報最佳設定 usable 76.9%、excellent 20.2%。 | 借可玩性與規格品質分開評定；題目較小、模型較舊，不代表現在最強模型上限。 |
| [OpenGame / OpenGame-Bench](https://arxiv.org/abs/2604.18394) · [paper-linked repo](https://github.com/leigest519/OpenGame) | 150 題、五類；每題 3 個 random seeds；BH／VU／IA 三維 0–100；Sonnet 4.6 agent 72.4/67.2/65.1；有 prompt、gallery、live demo/source。評測 pipeline 需 headless browser + VLM，repo 表示 benchmark pipeline 將稍後釋出。 | 可借 rubric 和多次重跑；agent 有 template/debug/迭代，zero-shot 明顯較弱，故不能當 strict one-shot；完整題庫／評測器尚未公開，暫非可重現排行榜。 |
| [DogLM](https://github.com/mikeushakov/doglm) | 10 PRDs（5 小遊戲×cued/uncued）直接產生 HTML；五次 run 可看模型方差；LLM code judge 給狗互動 0–2 分，GPT-6 Astra 最新榜列 6.6/20 | 對「自發補足未說明的機制」有趣且可重跑，但小遊戲＋靜態 source judge 的限制明確；榜單沒 GPT-6.1/Sonnet 5.5，只作窄題補測。 |
| [GameDevBench](https://waynechi.com/gamedevbench/) · [repo](https://github.com/waynchi/gamedevbench) | 333 個 Godot 任務／88 tutorials；官方 2026-10-01 新增 GPT-6.1 Sol (xhigh) 69.97%±4.9、GPT-6 Astra (high) 68.8%±5.0，pass@1 但採最佳 multimodal feedback/harness | 是「在既有 Godot 專案完成開發任務」而非一 prompt 從零生成遊戲；只借其多模態任務和 error bar，模型成績不併入生成榜。 |
| [Godot LLM GameBench](https://github.com/oubakiou/godot-llm-gamebench) · [playable gallery](https://oubakiou.github.io/godot-llm-gamebench/en/) | 一款 Conveyor Courier Godot puzzle spec，Fable parent 透過 delegate skill 派 CLI 子模型實作；hidden tests/scene checks、quality and efficiency 分開，公開 prompt、測試、reference、各模型 playable median run。 | 同題、可重跑、真實作品＋自動驗收的好方法參考；任務規模小且 task/hidden tests 已公開後該輪凍結，舊模型 roster、agent delegate harness，不是完整遊戲從零上限榜。 |
| [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | 97 題單請求遊戲生成（11 genres、53 個 2D、44 個 3D），另外有修復及多輪優化；Opus 5 79.7、Fable 5.1 75.8、Kimi K3 71.3、GPT-5.6 Sol 63.4。 | 題目／分項設計值得參考，但官方資料仍標示 coming soon，模型未更新到 GPT-6.1/Sonnet 5.5。 |
| [GameCraft-Bench](https://github.com/FreedomIntelligence/gamecraft-bench) · [playable gallery](https://tongxuluo.github.io/gamecraft-bench-website/) · [Airship Trader exact prompt](https://github.com/FreedomIntelligence/gamecraft-bench/blob/main/tasks/openworld-airship-trader/instruction.md) | 140 個 Godot 2D 完整遊戲任務／15 類；完整專案加回放操作軌跡，錄製玩家互動畫面並以隱藏 rubric／多模態 judge 評 core mechanics、content depth、functional visuals、art and presentation。Airship Trader 的完整提示和 GPT-5.5/Codex 代表作品可玩；任務分 60.40。官網 leaderboard 表格目前列 Opus 5 68.44；README 摘要寫 65.70；網站摘要重覆的 41.46 實際是同表 Opus-4.7 條目，顯示摘要文案未同步更新。 | 是重跑最新模型、檢查完整可玩系統的強候選，尤其 Airship Trader 的經濟／資源／戰鬥／升級整合；依賴 agent harness 與可選共享資產、只涵蓋 2D，並非 strict first-output。重跑可採任務級規格及軌跡評分，但須自行固定模型條件；別拿摘要總榜值當作穩定最新排名。 |
| [PlaytestArena](https://arxiv.org/html/2605.28258) · [官方 project/gallery](https://continual-game-generation.vercel.app/) · [gallery source](https://github.com/RunRiotComeOn/gui-agents-for-continual-game-generation) | 2026-05-27 論文：200 個 browser-game prompt、8 類、1,548 條可觀察 rubric；每題平均 131 tokens、7.7 criteria。單 pass Direct LLM baseline 以 rubric pass-rate 評分（GPT-5.4 31.6%、Sonnet 4.6 29.7%、Kimi K2.5 27.8%）。32 題盲評與 GUI judge agreement 84.2%／κ=.64。 | 借多題任務電池＋明確遊戲內可觀察驗收 rubric；適合給新模型做 strict first-pass 廣度測試，補足單一長題。題目多為短提示而非上限長規格，模型較舊，完整 200 prompts／rubric 是否公開與可重跑性待核。文中 Play2Code 是最多五輪玩家回饋與 memory，不可與一次生成的 Direct LLM 混算。 |
| [MAGIC](https://arxiv.org/abs/2607.11594) · [official repo](https://github.com/sereneee1201/MAGIC) | 100 個 Unity 多室內場景生成案例；評場景／portal 連接圖、可達性與 runtime transition。主模型 GPT-4.1-mini，直接 baseline GPT-4.1，報 transition-aware F1 0.9637；完整 ground truth 須向作者索取，需 Unity 6000.0.24f1 與約 23GB assets。 | 只適合補測 3D 空間、導航與場景轉換能力；不是完整遊戲迴圈，沒有完整 playable gallery 或目前 frontier 模型對照。 |
| [Unity scene failure taxonomy](https://arxiv.org/abs/2607.10187) · [Mage companion](https://arxiv.org/abs/2605.07342) · [dataset](https://huggingface.co/datasets/anon-neurips-2026-0502/scene-level-grounding-benchmark) | 10,400 次 Unity C# scene generation、26 goal patterns、四種 IR 條件、20 seeds；Qwen2.5-Coder-7B、DeepSeek-Coder-V2-Lite-16B、Codestral-22B、Qwen3-Coder-30B 等。compile failure 不准 repair；研究摘要稱 0/10,400 compilable scenes。某些 IR 條件用兩次呼叫，Mage 有 858 次相關嘗試。 | 可借 strict no-repair 的失敗分類與場景結構評估；不屬完整遊戲、沒有可玩成果，且「single-pass」是不能修復而非每條件都單一 model call。勿把它的失敗率直接外推到較新 frontier 模型。 |
| [GameDaily how-it’s-made](https://gamedaily.ai/how-its-made) · [game catalog](https://gamedaily.ai/) | 公開流程稱 928 款／232 天（How-it-made 頁列 233 天） browser games，以 mechanic／genre／input／visual constraints 組合 brief，使用共用 engine components；有桌面／手機啟動、輸入、viewport、error checks 和 AI judge。prompt、模型與 judge 權重不公開；首頁目前展示到 10/01。 | 產品化生成流水線和 QA 設計參考，不是可重現的模型 benchmark；目錄 ingestion date 也不可視為遊戲創作日期。 |
| [DogLM](https://github.com/mikeushakov/doglm) · [榜單](https://mikeushakov.github.io/doglm/) · [作者說明](https://mikeushakov.com/machines-of-spontaneous-warmth/) | 5 款小型 browser game × uncued/cued 兩版 PRD；一則 PRD 提及背景有狗，但未要求玩家和狗互動，模型需輸出自包含 HTML。以 node syntax gate 後由 LLM judge 讀 HTML，看是否可「摸狗」（0–2）；PRD、程式、例子公開，支援多模型、多次 runs，manifest 記成本／token／judge evidence。榜單快照（2026-09-05）含 GPT-6 Astra 等，Astra 平均 6.6/20。 | 直接 one-prompt game-generation 的窄題補測，可看模型能否自發補全未明說的設計互動，也可做多次重跑；但遊戲刻意簡單，judge 靜態讀 code 而不實際操作遊戲，榜單沒有 GPT-6.1 Sol／Sonnet 5.5，絕不能當完整遊戲上限分數。 |
| [GameDevBench](https://waynechi.com/gamedevbench/) · [repo/tasks](https://github.com/waynchi/gamedevbench) · [paper](https://arxiv.org/abs/2602.11103) | 官方頁 2026-10-01 更新：333 個 Godot 任務／88 篇教學、2D graphics 33%／3D 27%／UI 20%／gameplay 20%。GPT-6.1 Sol Codex xhigh pass@1 69.97% ±4.9；GPT-6 Astra Codex high 68.8% ±5.0；榜單新列 Muse Spark 1.2 high/Muse Code 61.0% ±5.2。分數採每模型最佳多模態回饋設定、最佳 harness；95% CI。官方 results 目錄目前只見若干較舊 run 詳情，沒有 GPT-6.1/Muse 原始 artifact，榜上未列 Sonnet 5.5。 | 可追蹤最新模型在 Godot 圖形、UI、玩法任務上的多模態 coding 能力，也能借信賴區間與任務分層；它解的是既有專案／教學任務，不是一次從空資料夾生成完整遊戲，且結果受不同 harness 與視覺回饋影響。不可併入 generation leaderboard。 |
| [PacBench / Pac-Man bake-off](https://jonclegg.github.io/pacman-bakeoff/) · [原始碼、runner、rubric](https://github.com/jonclegg/pacman-bakeoff) · [results JSON](https://raw.githubusercontent.com/jonclegg/pacman-bakeoff/main/entries/meta.json) | 一句固定 prompt「Create a Pac-Man game in a single html page」，每 run 產一個單頁 HTML，gallery 可玩每個版本。Opus 5.5 99/100、Sonnet 5.5（實際 `anthropic/claude-sonnet-5.5-20260928`）95、GPT-6.1 Sol 91、GPT-6 Astra 87；JSON 記錄 model+harness、effort、成本／時間／tokens。Opus 5.5 於 2026-09-28 對成品做 90 秒自動遊玩＋source/maze audit：Controls 20、Ghosts 25、stuck 20、Maze 20、Sound 15。 | 新且可玩的單次輸出校準組；有透明 rubric 與逐項分數註記。但提示很短、Pac-Man 屬模型熟悉的既有遊戲，每模型僅一 run，且 Codex API／Claude Code／OpenRouter+Claude Code harness 不同。評分者 Opus 5.5 也參與了參賽 run，存在評分者與模型家族重疊疑慮。適合校準基本可玩性與驗收流程，不適合作完整遊戲上限主測。 |
| [lmarcade](https://www.lmarcade.com/) · [遊戲頁](https://www.lmarcade.com/games) | 頁面稱累積 49,597 張票；玩家先後玩同 prompt 的兩個作品再選偏好，投票前隱藏 model/harness，以 Bradley–Terry 更新 build 等級，再彙總 model、harness、model+harness 排名。作品頁可直接點玩。 | 可借用真人盲選的 pairwise fun/preference 評估，補足自動測試不會測「好不好玩」；網站同時比較不同 agentic harness，沒有證明每模型同工具、固定一次輸出。可見榜單未列 GPT-6.1 Sol／Sonnet 5.5，未見原始 challenge prompts 或 run transcript；僅作盲評方法參考，不併入 one-shot 成績。 |
| [AutoUE / PlayGen-20](https://arxiv.org/html/2603.07106) · [official repo](https://github.com/Pluto156/AutoUE) · [20 task data](https://huggingface.co/datasets/Pluto156/AutoUE_DataSet) · [demo video](https://www.bilibili.com/video/BV1bqLH6HEqF/) | 2026-04-08 v2 論文，20 個 UE5 3D task cards（5 easy／7 medium／8 hard）；自動化 agent 使用五個專職 LLM、858K asset RAG、MCP／Unreal Engine，Qwen-Plus 生成／評估任務，Scene／Gameplay／Visual 以 .35/.35/.30 加權。 | 高難度 3D 任務卡可取材，尤其互動／進度類驗收；它評的是完整 agent 系統而非 frontier 模型同條件一次生成。UE/API 環境重，適合作為題庫／rubric 來源，不併入模型排行榜。 |
| [3DGameAgentBench preview](https://suyoumo.github.io/3d-game-agent-bench/) | 2026 private research preview，目標是 Three.js 長程生成、多輪 build/edit/regression retention；列 GLM-5.3/ZCode、Opus 5、Kimi K3、GPT-5.6/Codex、DeepSeek V4 Pro、Qwen3.8/Qoder，單題約 4–5 小時。 | 非 one-shot、頁面標 PRIVATE RESEARCH PREVIEW，沒有公開任務集／排行榜／可玩對照；列為觀察項，模型也未覆蓋目前新版本。 |
| [GameHorizon Suite](https://arxiv.org/abs/2609.25001) · [official repo / leaderboard](https://github.com/TencentARC/GameHorizon) · [project page](https://gamehorizon-suite.github.io/) | 2026-09-21 論文測模型操作既有 AAA 遊戲：5,000 小時／21 款遊戲資料、5,000 道離線題、20 個線上長時程任務／62 子任務、47 個模型；其頁面列 GPT-6 Astra 線上長時程成功率 45%（9/20）。 | 是 gameplay agent benchmark，研究對象是「玩既有遊戲」，不是「從 prompt 生成遊戲」。截至 2026-10-04，官方 repo 表示程式／資料預計約 10/25 起逐步釋出；可追蹤其釋出，但不納入生成遊戲主測。 |
| [GAMED.AI](https://aclanthology.org/2026.acl-demo.84/) · [demo library](https://shivena99.github.io/GamED-AI/acl-demo/library/) | ACL 2026 demo：教育遊戲生成系統，兩類模板、15 機制、五領域 200 題，50 個示例；報 90% 內部 validator pass、98.3% schema、約 $0.46／題、少於 60 秒。 | 是帶 phase-based multi-agent 與 deterministic quality gates 的教育應用，不是通用遊戲 benchmark 或裸模型單次測試；記錄 90% 的口徑，避免誤當玩家品質／學習成效。 |
| [NEXUS Game Benchmark Agent Arena](https://github.com/specimba/NEXUS_game_benchmark_Agent_Arena) | 同一份 `BATTLE_PROMPT.md`、隔離環境，公開盲評 rubric、測試計畫、產物證據 schema 與自動啟動／輸入／暫停／重開等檢查。允許一個 user task 內長時間自主規劃、互動測試、修復、迭代、潤飾；live prompt v17，而 v21 尚待 operator 決定。 | 很適合借用「原創性＋長程執行＋設計判斷＋真人盲評＋技術驗收」方法；不能列入 single-call / first-output 排名。現有 battle log 模型與可見 artifact 尚不足作最新 frontier 比較。 |
| [RSIGame](https://arxiv.org/html/2609.39045) | 2026-09-30 工作重用 GameCraft-Bench 原有 140 tasks。報 Godot GPT-5.5/Codex one-shot 50.26；經 recursive improvement／經驗內化的 Qwen 3.8-27B 61.38，Phaser 58.53，稱 tokens 約減 11 倍。 | 記為既有 benchmark 上的迭代／訓練方法研究，不是新題庫或當前模型對照；不能拿迭代／內化後的分數與純 one-shot 新模型混榜。 |
| [Opus 5.5 Age of Empires II effort sweep](https://github.com/Barty-Bart/opus-55-effort-comparison) | 六個 fresh Claude Code project 使用固定 AoE II browser-clone prompt；五個比較 low/medium/high/xhigh/max effort，另有一個低 effort 加長需求 prompt。Repo 放 exact prompt、六份 HTML/source、results.json 和驗證方法；作者報時間／價格從 low 19m10s/$3.79 到 max 2h58m27s/$69.14。 | 很適合移植成跨模型固定高難度任務：聚落、經濟、時代、軍隊、電腦 rival 與互相依賴系統。原研究是單一 Opus 5.5 的 effort sweep，不是模型榜；樣本各一次、煙霧測試不足以證明完整戰役可通關，special prompt run 也不可與標準題混算。 |
| [GPT-6.1 Sol orchestrator + Qwen 3.8 local workers](https://www.reddit.com/r/AI_Agents/comments/1wtrix3/gpt61_sol_is_cheap_we_made_it_77_cheaper_by_never/) | 三款桌上球類小遊戲（pool／bowling／foosball），同一提示比較 Sol 自己寫碼和只規劃／委派、Qwen 3.8 27B 在 RTX 3090 寫檔；作者報總成本 $0.75 vs $0.17、時間低於 7 分鐘 vs 43 分鐘，沒有共用測試套件。 | 顯示工具權限與 worker/orchestrator 設計會大幅改變成本和時間；遊戲太小且只以「可玩」人工判定，不是能力上限題，也不比較純模型。可作 harness 控制提醒，不能放主榜。 |
| [Stefan：3D MMO town square](https://claudevideo.org/videos/old-school-mmo-town-square-with-an-elf-archer-and-quest-chat) | 2026-09-26 X 影片展示 Unity/Blender MMO 場景；頁面報 36 小時、7.85B tokens、$2,175 及額外素材生成費，場景可操作。 | 耗時和規模驚人，但無原始 prompt、source、完整 QA 或會話記錄，也無法確認是否一則指示；作為「不能用 token/耗時直接推斷一次生成」的反例，不列入成績。 |

### 本輪搜尋得到的設計結論

- 現階段公開資料沒有一個來源同時做到：GPT-6.1 Sol／Sonnet 5.5 等最新模型、同一超長複雜提示、各模型可玩成品、完整條件／成本、獨立可重跑驗收、足夠重複次數。因此應保持兩條資料線：近期作品 showcase 與可重現 benchmark，不能混成一個分數榜。
- 對使用者目前的目標，優先重跑 **Backrooms**：它有逐字高複雜度規格、五個近期可玩成品和原始畫面，並要求自動化走到死亡與逃脫。Hill Climb 仍適合校準控制與物理；Diablo ARPG 是角色成長／戰鬥／掉寶的第二題。
- 若把「上限」定義為**長時間 agentic 開發能力**，MALL ACTION／NEXUS 的長 session 口徑可以另開一組；把 A2Z 的依賴需求表、GameASG 的 strict success、SWE-Game／GameLogicBench 的輸入觸發與逐狀態驗收加上去。這一組不能和「第一次輸出」或 strict single-call 排名混合。
- 題型設計可新增 AoE II browser-clone：其 Opus 5.5 effort sweep 已公開固定長 prompt 和各 run 產物，便於把模型、effort 分開控制；PlaytestArena 的多題、短 rubric 可作 breadth battery。前者借高整合題，後者借驗收方法，兩者都不能直接提供目前 frontier 模型比較結論。
- Backrooms 與 Diablo 都有 AI for Mortals 原始 prompt 和 playable builds：前者是目前首選，因其新模型比較日期較近、具程序 3D、敵人感知與明確死／逃目標；後者保留作玩法系統更厚的第二題，補 GPT-6.1 Sol 後可獨立比較。
- 正式比較至少把建置／執行、需求覆蓋、流程可通關、規則正確、操作手感、視覺音訊分開；每模型建議 3 次獨立 run，保留失敗，不從多份成品中挑最好。報告成本、時間、token、工具與代理數、人工介入。
- 本輪補到 PacBench 的四個較新模型單次成品和可重跑評分腳本，建議只把它放在「基本操作／狀態／迷宮規則」校準題，不可因完整得分很高便當成大型原創遊戲能力上限。lmarcade 的隱藏身分玩家兩兩遊玩值得借作趣味性盲評，但需另把模型與 harness 固定，避免評成 harness 競賽。
- Tumble brief 仍是目前最清楚的高難度物理建造題：它把自製物理、編輯器、內容和可執行驗收放在同一遊戲裡，但沒有獨立 artifacts。新查的 waterslide 系列則有三個不同模型的實際 build、source 和自動測試，可先做競速物理副測；須先核對原始提示是否相同。EvalMap Jeep gallery 提供大量可玩的近期同題樣本，適合校準「能不能跑、會不會失控」，不能代替長流程主測。

### 後續查詢去重提醒

- 不再重找 Mall Action 基本 prompt、Vibecode 四題、Lunar Scream 四模型、One Shot Challenge 七月 round、Single HTML Game Bench 固定 prompt；除非新模型／新 build／新驗證出現。
- 下一輪優先只查變動項：Mall Action 新模型分支與原始驗收證據；Slipstream / Splash Rush 同題性；OneShotLM 是否補入最新模型；TETHER 是否公開 prompt/repo；Fable 專案所稱 GLM-5.3 同 prompt 後續結果；以及上述待核的 YouTube／X 高複雜度案例。
- 每個未能開啟或找不到原始 prompt 的項目仍要留在台帳，標明查核缺口，避免下輪再把它當成「新發現」。
- Tumble 舊案例已核對原文、影片與完整 brief；EvalMap Jeep 已核對同題數量、最新分數和逐項 rubric。下一輪應優先找這兩題有沒有更新模型／獨立可玩輸出，或直接把 Tumble brief 轉成一套統一重跑規則；不要再搜相同 prompt 或泛用「AI game demo」關鍵詞。

### 本輪搜尋路徑紀錄（避免重跑相同查詢）

| 查詢範圍／關鍵詞方向 | 本輪查到 | 後續處理 |
|---|---|---|
| `GPT-6.1 Sol game generation one prompt playable demo`、`Sonnet 5.5 game one prompt playable`、GitHub playable | Slipstream、Promptslove、MALL ACTION、OneShotLM；另外比對到 Splash Rush 的同系列線索但未核實相同 prompt | 不要再做一般模型名＋game demo 搜尋；只追各項新版本、prompt/QA 原始證據或新模型加入。 |
| `same prompt Sonnet 5.5 GPT-6 Astra game playable`、`Fable 5.1 same prompt game` | AI for Mortals 的 Diablo ARPG / Backrooms FPS、Mini-golf video、Kart Blitz、BitsMinds Hill Climb | Backrooms 已升為主測、ARPG 留第二題；其餘均記入 ledger。沒有新增模型或可下載 output 前不重查既有影片。 |
| `GPT-6.1 Sol same prompt Sonnet 5.5`、`Opus 5.5 one prompt game 2026` | 未找到公開的 GPT-6.1/Sonnet 5.5 同題長流程遊戲排行榜；搜尋到 Reddit/GitHub/X 摘要、Moe Lueker 舊 GPT-6 四模型對照 | Reddit / X 貼文摘要均已列待查或排除；僅在得到原 prompt、成品或對稱執行記錄時升級。 |
| `game generation benchmark 2026 playable`、formal paper keyword / arXiv | GameASG、A2Z GameSpec、SWE-Game、GameLogicBench、WebGameBench、OpenGame、GameXpert、GameCraft | 這批方法結論已整理；只有新版資料釋出或補入 GPT-6.1/Sonnet 5.5 才重查。 |
| AI game catalog / arena: Goldie, OneShotLM, Testing Models, OhMyOpus, Cheer Self AI | Goldie 頁面數量不一；OneShotLM 首頁與更新紀錄對不上；Testing Models 54 題但模型快照偏舊；策展頁帶出 Fortnite、DOOM autoplay、三遊戲比較等線索 | 目錄已確認為發現工具而非 leaderboard；下輪採「查新增條目／新增模型」方式，不重新掃全站。 |
| 排除邊界：`AI plays a game`、assets-only、產品行銷 demo | Pokémon Red 是遊戲代理操作，GBA enemy sprite 是既有專案素材編輯；Ropilot 是 agent 產品示範，非固定基準 | 已分別標明排除原因，不要把這些重新列為從零生成遊戲案例。 |
| 新追 Oct 1–4 發布線索：`GPT-6.1 Sol playable game one prompt`, `Sonnet 5.5 latest game comparison` | 新發現 Sakura Rally、SkaLab 三模型 dungeon workflow、Duncan Rogoff 六任務 blind test、Fallout: New York；另找到 Deep20Bench 1.1 | Sakura 納入高上限 showcase 但非純 one-shot；SkaLab/Duncan 等保留待取得 prompt/build；Fallout 和 Deep20Bench 記明排除理由。 |
| `GPT-6.1 Sol same prompt Sonnet 5.5 game October 2026` | 有最新同題但只有簡短任務的 3D game lead；另見 Reddit game projects 和 cost anecdote | 本輪沒有找到同時具備 long prompt、模型最新、可玩建置、完整條件和第三方可重跑性的案例；不要重查一般搜尋詞，改追已列候選原作者的 prompt/artifact。 |
| `Opus 5.5 GPT-6.1 Sol hill climb same prompt`, `latest browser game benchmark October 2026` | BitsMinds 9/30 Hill Climb playable pair；Blockworld、Ashen Vigil、Sonnet Fortnite 等單模型展示；AI Fire Browser OS+2 games；Sakura Rally、Dead Signal source audit | Hill Climb 是最新同題可玩直接比較但遊戲範圍小；其餘按本文限制分類。後續只查新 run、原始 prompt／session、repo/build 或獨立驗收，不要重跑通用搜尋。 |
| `Age of Empires II browser clone Opus 5.5 effort comparison`, `game generation benchmark PlaytestArena AutoUE` | Opus 5.5 六-run effort sweep；PlaytestArena 200 prompts／rubric；AutoUE 20 個 UE5 task cards；3DGameAgentBench private preview | AoE 題型可固定用於新模型對照；PlaytestArena 借驗收結構；AutoUE 借 3D 任務設計。後兩者模型舊或系統條件不適合直接排名；3DGameAgentBench 資料未公開。 |
| `AI GameStore game generation benchmark meaning`, `Deep20Bench game benchmark` | AI GameStore 是模型玩遊戲；Deep20Bench 1.1 是模型玩 Twenty Questions | 排除為 generation benchmark，已留名避免同名／關鍵詞誤判；除非任務範圍改變或新釋出生成測試資料，不重查。 |
| `OpenGame-Bench interactive game generation`, `OpenGame benchmark evaluator prompts` | 核對官方 arXiv 與 repo：150 prompt、五類、3 seeds、BH/VU/IA；OpenGame-Bench evaluator 仍標示即將釋出。 | 已修正文中先前較籠統的 OpenGame 說明；可借評測維度，不重查該 paper/repo，除非 benchmark assets/evaluator 正式公開或增加新模型。 |
| `single-html-game-bench README model matrix GPT-6.1`, `Sol orchestrator local coding workers game cost` | 確認 Single HTML Game Bench 的 20 個首版 outputs 與 GPT-6.1 Sol Max（仍缺 Sonnet 5.5），以及三款 mini-game 的 Sol/Qwen worker-routing 成本比較 | 前者保留 strict first-output model list；後者只留 harness/cost 研究，不作完整遊戲能力證據。僅在模型矩陣增加新版本或有共用驗收／長規格任務時追更新。 |
| `Opus 5.5 Sonnet 5.5 same prompt Godot minecart Oct 4` | 打開 Reddit 原始貼文核實：兩個新 Godot 專案、Claude Code+MCP 實際 Play；作者報價格、兩模型 playtesting 差異和影片，兩者皆未實現物理礦車 | 更新既有候選的證據狀態；仍無 exact prompt、source、獨立 playable build 或 rubric，遊戲範圍小，故不重搜一般 minecart demo，只在新 prompt/build/驗收出現時追。 |
| `DogLM benchmark generated games dog interaction` | 核對官方 README、PRDs、scoring 和榜單連結：5 種小遊戲、cued/uncued、HTML output、syntax gate + LLM source judge；目前表列 GPT-6 Astra，未有 GPT-6.1/Sonnet 5.5 | 記為自發機制／穩定度副測而非上限測試；若要新增最新模型只需重跑公開 PRDs，不需重新搜尋概念／任務。 |
| `GameDevBench October 2026 GPT-6.1 Sol leaderboard` | 官方頁 2026-10-01 加入 GPT-6.1 Sol、GPT-6 Astra 成績及 95% CI，333 個既有 Godot 專案任務 | 更新遊戲開發能力 benchmark 的最新模型狀態；與從零生成完整遊戲分開，不再搜泛用「GameDevBench game generation」。 |
| `Godot LLM GameBench Conveyor Courier benchmark delegate` | 核對相同 Godot 小型 conveyor puzzle、delegate CLI child models、hidden tests / browser gallery、quality vs efficiency 和 frozen round | 留作可重跑評測方法樣本；任務小、已公開凍結本輪，不列為完整遊戲上限。 |
| `BitsMinds GPT-6.1 Sol GPT-6 Astra build-off interchange fairground rocket`, `Sonnet 5.5 Opus 5.5 same build brief` | 核對 9/29–30 兩篇同系列原文：SVG 交流道、遊樂園、火箭發射；單次、禁 browser/code、max effort，附成品；跨文章重用舊 run，人工非盲評，無精確 prompt 檔。 | 記為相鄰互動作品／first-output 方法案例，不是完整遊戲 benchmark。毋須再搜尋同三題或重算分數；只有公開 prompt/session、新模型 fresh run，或新增真正可玩遊戲題才更新。 |
| `Pac-Bench Pac-Man bake-off latest models one-shot`, `jonclegg pacman-bakeoff entries/meta.json` | 核對官方 prompt、repo runner/rubric、逐模型 playable HTML 與 raw metadata：Opus 5.5 99、Sonnet 5.5 95、GPT-6.1 Sol 91、Astra 87；2026-09-28 Opus auto-play + source/maze audit；不同 harness 和各一 run。 | 收為基本可玩性校準與 rubric 例，不是完整遊戲上限；已核對当前 roster，除非更新 run/加複本或變更評分器，毋須重查該 benchmark。 |
| `site:waynechi.com/gamedevbench Muse Spark 1.2`, `GameDevBench latest leaderboard models Oct 2026` | 官方榜新增 Muse Spark 1.2 high/Muse Code 61.0% ±5.2；GPT-6.1 Sol 69.97% ±4.9、Astra 68.8% ±5.0；確認 333 個既有 Godot 任務，best multimodal feedback/harness；raw results 目錄未見 Muse/GPT-6.1 run 明細。 | 更新 latest-model 遊戲開發 agent 參照，但不屬於 one-prompt 從零生成；不要重搜通用 GameDevBench，除非官方釋出新模型或詳細 run artifacts。 |
| `lmarcade blind play same prompt model harness leaderboard`, `lmarcade games challenge prompts latest models` | 核對官網規則：投票者盲玩同題作品、Bradley–Terry build rank，含 model/harness 聯榜；49,597 votes，展示遊戲可玩。沒找到公開 prompts/transcripts，榜列較舊模型，並刻意允許多種 agentic harness。 | 記為真人 pairwise preference 方法參考；不作 one-shot 模型比較。除非上架 GPT-6.1/Sonnet 5.5 且公開同 harness run/prompt，否則不用重查它的基本規則。 |
| `"GPT-6.1 Sol" game "October" 2026 one prompt playable`, `"Sonnet 5.5" game Oct 2026 one prompt playable`, `new AI game one-shot playable October 2-4 2026` | 新查到 Nathan Onn 10/02 Kart Blitz Max 五小時 run（既有 Reddit Turbo Karts 的不同 prompt/tool/effort 變體）；另覆核 PacBench。Oct 2–4 沒找到新高複雜度同題跨模型 playable game 比較。 | 將 Kart Blitz 兩個獨立 run 拆開記錄，不能混算；除非新模型用相同 task+tool/harness fresh run，不重搜一般 Kart demo。 |
| `"GPT-6.1 Sol" game generation benchmark latest`, `site:github.com game generation benchmark GPT-6.1 Sol`, `game generation benchmark leaderboard October 2026`, `GameXpert-Bench leaderboard GPT-6.1 Sol Sonnet 5.5` | 無發現新正式 game-generation benchmark 對 GPT-6.1 Sol／Sonnet 5.5 的公開新增分數；GameDevBench 只新 Muse 1.2 榜列結果（詳上），其餘命中為已列 benchmark 或 game-playing eval。 | 除官方發佈新資料集、評估器或新模型 run 外，不再重複上述 generic benchmark query；以已列來源為監測清單。 |
| `"GPT-6.1 Sol" game "October" 2026 one prompt playable`, `"Sonnet 5.5" game Oct 2026 one prompt playable`, `"Opus 5.5" "GPT-6.1 Sol" game same prompt playable October 2026`, `"GPT-6 Astra" "Sonnet 5.5" game comparison playable 2026`, Reddit 10/03–10/04 | 找到 Nathan Onn 的 10/02 Sonnet 5.5 Max Kart Blitz run（已與原 67 分鐘版本分開記錄）、PacBench；SkaLab 是 builder/critic 三輪 dungeon 工作流而非 one-prompt。未找到同時具高複雜度、最新模型、同規格、可玩 builds 的新同題比較。 | 後續只追新模型在已列 Kart / Dungeon 題目的 fresh run，或新公開 prompt、session / source / QA；不重搜這批日期範圍及泛用 one-prompt demo。 |
| `Goldie Bench game one-shot leaderboard 2026 models latest`, `awesome AI-built games GPT-6.1 Sol source-verified` | Goldie 頁有 27 個同一模糊 prompt 的首版單 HTML 成品可玩，但榜列模型仍停於 GPT-5.6 Sol、Opus 5.5、Sonnet 5 等，未列 GPT-6.1 Sol / Sonnet 5.5；Awesome AI Games 收錄 source-backed catalog 872 game units／598 repos，數據最後核實 2026-09-30，不是共用 prompt benchmark。 | 可作發現 playable demo 的目錄，現在不補充最新模型上限證據；若榜單新增 GPT-6.1/Sonnet 5.5 或同題 run 再更新，否則不重掃目錄。 |
| `Claude Opus 5.5 vs GPT-6 Astra game one prompt Tumble marble run`, `Promptslove Tumble physics puzzle game prompt` | 打開 9/24 原文核對 exact brief、Opus high / Astra xhigh、兩邊作者實玩結論；任務含自製剛體物理、15 類零件、建造編輯器、6 demo／8 puzzles、100 marbles 壓測和明列驗收。另核對頁面影片 embed。 | 這是目前找到最適合轉成高難度物理／系統副測的公開 prompt；無獨立 playable/source/FPS 驗收，現有結論僅作者觀察。除非出現新模型 run 或可重現 artifacts，不再搜同一篇／同一 brief；後續工作是設計統一重跑與驗收。 |
| `EvalMap AI jeep 119 builds same brief GPT-6.1 Sol`, `site:evalmap.ai/jeep GPT-6.1 Sol Sonnet 5.5` | 核對 10/03 截止頁：119 builds、80 scored、39 failed；成功項逐一可直接 drive；GPT-6.1 Sol 45、Sonnet 5.5 48、Opus 5.5 40、Astra 39，另有 10/03 Pareto 58 但模型／harness attribution 不足。Rubric 含約一分鐘操作與 90 秒直行邊界測試。 | 收錄作近期短題可玩性／崩壞率校準；不作完整遊戲上限測試。原 brief 不完整公開且跨模型條件不一，除非新增 build、公開 exact prompt 或更改 rubric，不重做泛搜。 |
| `Single HTML Game Bench current live page GPT-6.1 Sol Opus 5.5`, `GPT-6.1 Sol game benchmark October 2026 update`, `Sonnet 5.5 game benchmark leaderboard October 2026` | 同時覆核 live page 與 GitHub README：榜仍有 Opus 5.5、GPT-6 Astra、GPT-6.1 Sol；未見 Sonnet 5.5。GameDevBench 最新官方更新停在 10/01，PacBench roster 也未變；未發現 10/03–04 新增 GPT-6.1/Sonnet 5.5 正式 game-generation 分數。 | 既有模型名單與最新更新狀態已核對；後續僅在 live roster、raw results 或官方更新日期改變時回查，不重跑相同模型名＋benchmark 搜尋。 |
| `Ornith-1.5-35B one shot browser game llm-bench.io October 3`, `October 2026 latest one-shot game builds` | 命中 10/03 Ornith-1.5-35B-A3B Uncensored OpenVINO INT4 的單檔 HTML；可玩輸出但無精確 prompt、跨模型同題成績或遊戲專項驗收。另查到 CS Brasil（多輪對話後修改）、Fallout: New York（舊作品法律下架報導）、OpenCiv3（模型操作既有遊戲）等不合格新近命中。 | 新近不等於適合作上限 benchmark；標記為邊界案例／排除，避免下輪把日期新誤當任務新。只有取得 prompt、模型條件與獨立可玩證據才重新評估。 |
| `Astra vs Opus 5.5 vs Grok 4.7 same prompt army defense game video`, [森下航 9/25 對照](https://note.com/yuru_se_kou/n/nd6c7b971df1f?hl=en) | 同一指示由 GPT-6 Astra low/high、Opus 5.5 xhigh、Grok 4.7 xhigh 各跑一次，產出 30 秒「城門增兵、攔截敵潮、打 Boss」影片與音效；YouTube 影片及作者 6 軸各 10 分評分可見，Claude 依實測數據與影片評。高 effort Astra 51、Opus 46、低 effort Astra 45、Grok 39。原 prompt 是文中圖片，不是可複製文字；報告未提供可獨立操作的遊戲。 | 保留為最新模型的視覺模擬影片比較與「同模型 effort 差異」線索；任務交付是影片而非完整可玩的遊戲，且評分仍由單一 LLM 協助，故排除於遊戲生成主榜。可借用同 prompt、固定條件、分項 rubric、實際 metrics+video 的呈現方式。 |
| `AI Game Comparison Nutlope same prompt browser game benchmark`, `Godmark Godot AI benchmark 5 runs October 2026` | [Nutlope AI Browser Games](https://github.com/Nutlope/ai-browser-games) 固定 Snake／Tetris-lite／Breakout，產出單檔 HTML，有 prompt、模型／token／成本／日期、可玩 gallery，但屬簡單熟悉小遊戲，且生成流程會 retry；[Godmark 貼文](https://www.reddit.com/r/ClaudeAI/comments/1wwt4k5/godmark_for_benching_claude_codex_and_deepseek_in/) 顯示每個較短、簡單的 Godot prompt 同時跑 5 個 agent session，測生成變異，不是完整遊戲。 | 收為簡單任務校準與重複生成方法，不是使用者要的能力上限題。已確認它們的公開 prompt／流程特徵；不再泛搜同名 benchmark，除非它們新增 frontier 模型、多系統長 brief 或完整可玩的新 round。 |
| `GameCraft-Bench Open-World Airship Trader task prompt full gameplay`, `GameCraft-Bench latest model leaderboard discrepancy 68.44 65.70 41.46`, `site:tongxuluo.github.io/gamecraft-bench-website "Open-World Airship Trader"` | 核對官方 144-line 任務指示、Godot 4 spec、GPT-5.5/Codex 可玩 build 與任務分數 60.40；每段 trace 最長 20 秒，最多評 10 段，1280×720 / 30fps replay。網站 leaderboard 表格列 Opus 5 68.44、Fable 5 65.72、GPT-5.6-sol 60.50 等；README 摘要卻寫 65.70，而摘要中的 41.46 對應表內 Opus-4.7 舊列。新增查 raw repo 發現任務 `rubric.json` 和 `solution/solve.sh` 公開，並非對公眾保密；該任務只有 GPT-5.5/Codex 一個可見代表 build，無 GPT-6.1/Sonnet 5.5 同題 run。 | 可用於把最新模型放在同一固定 prompt 下重跑；必須隔離 rubric、reference solution 和舊 build，不要把官方「hidden rubric」介紹誤解為公開 repo 也隱藏。榜單代表模型結果落後，且未涵蓋目前最新模型；後續只在新增 Airship 同題 run、更新任務或規格時回查，避免重複搜任務基本資料。 |
| `"action RPG" "Sonnet 5.5" "GPT-6.1 Sol" same prompt game build`, `"strategy game" "GPT-6.1 Sol" "Opus 5.5" game one shot playable 2026`, `"management game" AI "same prompt" "Opus 5.5" "GPT-6.1 Sol" playable`, `"physics builder" "Opus 5.5" "GPT-6.1 Sol" game prompt one-shot`, `"tower defense" "Claude Opus 5.5" "GPT-6.1 Sol" same prompt game playable`, `"management simulator" "Opus 5.5" "GPT-6.1 Sol" game comparison`, `"city builder" "Claude Opus 5.5" "GPT-6.1 Sol" one-shot prompt playable`, `"racing game" "GPT-6.1 Sol" "Sonnet 5.5" same prompt playable`, 9/24–10/04 Reddit / X / game demo queries | 沒找到在查詢期間新發布、同一高複雜遊戲 brief、兩個以上近期模型與可驗證成品同時具備的新案例。近似命中：[Ruocco](https://ruocco.it/news/gpt-6-1-sol-vs-sonnet-5-5-same-prompt-a-third-of-the-cost-tested-live/) 的 Ashen Vigil 是 Sol 單模型，兩模型對比其實是其他產物；[The Neuron](https://www.theneuron.ai/news/claude-opus-5-5-gpt-6-sol-livestream-benchmark/) 的 CatDoom／Dark Souls 有多輪 build-review-fix；Higgsfield Sol/Astra 說法只有二手材料；Promptslove 引述的 Opus/Sol 遊戲沒有可核實原貼文與 playable pair，索引日期亦可能在搜尋窗之前。 | 不新增主案例；記下並排除，避免下輪以「同 prompt」摘要誤當受控完整遊戲對照。只有原始 brief、同題兩份 build／影片和對稱執行條件到手時才升級。 |
| `site:github.com/FreedomIntelligence/gamecraft-bench "openworld-airship-trader" solution`, `site:tongxuluo.github.io/gamecraft-bench-website "codex55__openworld-airship-trader"`, `GameCraft-Bench Open-World Airship Trader Codex 5.5 trace GitHub output`, `"open-world-airship-trader" GameCraft benchmark model score`, raw `tests/rubric.json` / `solution/solve.sh` | 重新核對官網 live leaderboard、README、任務指示、build 頁及 GitHub 任務目錄。官方首頁寫 hidden rubric，但 `tests/rubric.json`、`test.sh`、reference `solution/solve.sh` 在 public repo 可見；raw rubric 含 build gate、M/D/V/A 項目及權重。搜尋結果只看到 GPT-5.5/Codex 的 Airship Trader run (60.40)，沒找到公開 traces/raw task report 或 GPT-6.1/Sonnet 5.5 對同題 run。Live leaderboard 正式表格是 Opus 5 68.44 / Fable 5 65.72 / GPT-5.6-sol 60.50；README 頂端 65.70 摘要仍不一致。 | 修正「hidden rubric」說法，記錄重跑時需把 rubric/reference 隔離於模型；public reference source 不是模型可見的前提。已查過 Airship 的任務檔、評分項、代表 build、模型 roster 與 leaderboard 數值；後續不重複這組基本查詢，只追新同題 run、官方 artifact 或 roster 更新。 |
| `2026 Unity benchmark LLM generate scenes natural language benchmark game complete playable compiler single pass Unity official dataset`, `2026 Unreal Engine benchmark LLM game generation benchmark dataset natural language playable games official repository PlayGen-20 AutoUE`, `MAGIC Transition-Aware Generation of Navigable Multi-Scene Game Worlds with Large Language Models official GitHub`, `2026 benchmark LLM generate complete playable game from prompt Unity Unreal game generation benchmark`, `Unity Unreal natural language playable game generation benchmark 2026 LLM` | 找到 MAGIC（100 Unity multi-scene navigation cases；GPT-4.1-mini/GPT-4.1）與 Unity failure-taxonomy/Mage（10,400 no-repair scene attempts；摘要報 0 compilable）。未找到上述搜尋所指的 2026 Unreal/PlayGen-20 完整可玩生成 benchmark。MAGIC ground truth 須索取、依賴大型 Unity assets；Mage 測 scene compilation 而非遊戲。 | 加入「相鄰方法」而非完整遊戲案例。已查 MAGIC/Mage 及相關 arXiv/HF/repo，不需重搜名稱；只有開放 prompt/ground truth、增加 frontier 模型或發布可玩完整遊戲資料才回查。 |
| `"GPT-6.1 Sol" game built game playable AI generated October 2026 -MALL -Kart`, `"Sonnet 5.5" "game" "one prompt" October 2026 playable -Kart`, `"Opus 5.5" "one-shot" game demo October 2026 playable -mall -kart`, `AI-generated game benchmark 2026 prompt-to-game playable model evaluation 3D`, `Leon van Zyl Sonnet Opus Fable 5.1 mini golf prompt game playable source code September 30 2026`, `"3D mini golf" "Fable 5.1" "Sonnet 5.5" game`, `"windmill" "dinosaur" hole "Sonnet 5.5" mini golf` | 找到 9/30 同 prompt mini-golf 影片：Sonnet 5.5、Opus 5.5、Fable 5.1 實際遊玩；獨立確認 Opus 與 Fable 兩個 GitHub repo 各有九洞 playable build、物理／自動逐洞驗收，沒找到 Sonnet repo 或逐字公開 prompt。另命中 GPT-6.1 Sol jungle safari post（作者改 prompt 且無成品）、簡單 Last Round sniper demo，均非完整公平測試。 | Mini golf 已加入 3D 物理副測但不作嚴格排名；記錄 repo 核實範圍，避免重搜已確認的 Opus/Fable build。若找到 Sonnet repo、原始 prompt 或對稱 session 才升級；GPT/Sonnet 近日期泛搜已查過。 |
| `"Oct 1, 2026" AI generated game survival build game model`, `"Oct 2, 2026" AI made game RPG playable model generated`, `"Oct 3, 2026" AI generated game simulation strategy playable`, `"Oct 4, 2026" AI coding game generated playable RPG`, `site:reddit.com/r/ClaudeAI game "Oct 3, 2026" generated RPG`, `site:reddit.com/r/aigamedev "Thursday October 01 2026" game AI survival RPG sim strategy`, `site:reddit.com/r/aigamedev "Friday October 02 2026" game "Claude Opus 5.5" playable`, `site:reddit.com/r/aigamedev "Saturday October 03 2026" "game" Claude Opus 5.5 browser`, `site:reddit.com/r/ClaudeAI "Oct 4, 2026" game made Opus 5.5 playable survival` | Oct 3 海盜遊戲貼文有實玩影片和多系統內容，但作者提供多年自製資產、三天長程開發、約 290 commits，並人類試玩回饋；無 exact prompt/repo。Oct 2 Lander 各一 run、無公開原始 prompt/build；Deadgrid 缺 prompt；The Big Suck 是既有遊戲轉 3D、20+5 小時；Space Federation 是既有 DOS 遊戲重製；Zombie/MMO 為持續 WIP。GameDaily 的 Oct 1 是頁面最新展示/目錄日期，不代表那天生成。 | 海盜 demo 留作「agentic 長流程上限」視覺參考，不作一次生成分數；其餘依條件排除。此輪日期窗口及列名案例已查，後續只追新原始 prompt、repo、fresh frontier model run 或獨立可玩 artifact。 |
| `"I gave Claude Opus 5.5 the idea for a pirate game" demo`, `"Magehold Fairwinds"`, `"The Ship Remembers" "Oct 1, 2026" browser game`, `"Lander" "Opus 5.5" "October 2" Godot Braben`, `"Dead Signal: Exclusion Zone" "2026" Claude Opus 5.5 single prompt`, `"Procedural Pixel Creature Workshop" Claude Opus 5.5`, `"Deadgrid" Qwen3.8 OpenCode game`, `GameDaily.ai how it’s made prompt benchmark game` | 追查海盜 post 的素材/影片、Lander 同題實驗、近日期標題和 repo 名稱；驗證 Deadgrid repo、Procedural Pixel Creature Workshop（工具/framework 非遊戲）及 GameDaily 生產流程。另以 GamesByAI new feed/JSON 核對：catalog ingest date 不能代替建立日期。 | 以上未查到可重現的一次完整遊戲測試；不把目錄日期、生成工具、既有作品改作混入比較。這些精確標題與來源均已查，除非 artifacts 或 prompt 後續釋出，不再重搜。 |

| `"Opus also took 10 hours" PUBG game`, `"A 2 km island with 8 towns" Opus 5.5`, `"24 bots that loot, take cover and fight each other" Opus`, `"only Opus used Scenario" "20 passing tests"` | 解開底稿舊的 PUBG-style battle-royale 待核條目：讀到 Yuzzy Itaba 原始 LinkedIn 貼文；確認兩模型、同一類 prompt、自述 feature scope、耗時、Astra 20 tests 及素材工具差異。仍缺 exact prompt、playable pair、source、test list。 | 由「只有摘要」修正成「原始貼文可讀、高複雜度展示已確認」，但不列公平比較分數。只在原始 prompt/build/test artifacts 可取得時重查；不重跑精確原句搜尋。 |
| `One Shot Challenge benchmark round 01 single model call no retry blind judging architecture hash`, `1shotchallenge.ai benchmark 141 playable entries model list winners prompt reveal` | 再查已收錄的 One Shot Challenge 官方規則、benchmark、winners、entry archive。確認 server side 一次 API call、無 edit/retry、prompt/output hashes、200 runs／25 models／141 可玩成果、約 97% usable、6.76M tokens／20.2h；但自由選 prompt、模型分配不均、沒有公開逐項 rubric；frontier roster 早於 GPT-6.1/Sonnet 5.5。 | 增補其作為 strict one-call 方法與 artifact archive 的價值，不升為固定 prompt 模型榜。已核官方 Round 01，不需重查相同規則；只有 Round 02 開始、加新模型或同題固定 prompt 資料發布時再查。 |
| `AI for Mortals Sonnet 5.5 realistic Backrooms prompt same build Opus Fable Astra September 29 2026`, 原文 `What I tested`／`Build a realistic Backrooms horror game`／五 build cards | 直接讀 9/29 原文、逐字 prompt、五個 build 卡片、截圖來源與時間／token／成本表；核實作者稱相同 prompt、無 follow-up／rerun，Claude Code 對 Codex、high effort + goal mode；規格含 Blender/Cycles、無盡程序迷宮、音源追蹤怪物、可逃出、自動化死／逃、1080p Chrome。 | Backrooms 維持最高優先重跑題。已查 prompt、build、圖片、條件；後續不再泛搜 Backrooms prompt，僅在新模型 fresh run、公開驗收記錄／rubric、可比 harness 出現時更新。 |
| `NEXUS game benchmark one shot complete original compelling game single sustained development session`, `site:github.com/specimba/NEXUS_game_benchmark_Agent_Arena one-shot BATTLE_PROMPT rubric playable game` | 核對 repo 的 one-shot 定義、兩側相同 prompt、版本紀錄、盲評 rubric、技術檢查與長 session workflow；確認允許大量 agentic iteration，live v17，v21 pending，battle history 不是最新 frontier 模型榜。 | 收為 user-task 口徑的高品質評估流程參考；不列 strict single-call 榜。已查 NEXUS 基礎架構／prompt 版本，後續只在 v21 正式生效、新 frontier battle 或 gallery/artifacts 明顯更新時回查。 |
| `"GPT-6.1 Sol" "game" "same prompt" October 2026 browser game`, `"Sonnet 5.5" "game" "same prompt" "October 2026" playable`, `"Opus 5.5" "game" "same prompt" "October 2026" demo`, `"Oct 4, 2026" "GPT-6.1 Sol" game demo`, `site:x.com "one prompt" "playable game" "Sonnet 5.5" October 4 2026`, `site:github.com "GPT-6.1 Sol" "game" "one-shot" October 2026`, `site:itch.io "GPT-6.1 Sol" game playable October 2026` | 截至 2026-10-04 沒有找到此日期之後的新高複雜完整遊戲跨模型比較。找到 [Pukerud Model Output Arena](https://github.com/Pukerud/model-output-arena)：三個固定 prompt（動畫車、簡單 Plants vs Zombies 單檔遊戲、Three.js Thriller 舞蹈場景）、未後製 HTML、靜態左右對照頁，已收 GPT-6.1 Sol；PvZ 原文是「make a small plant vs zombie game in a single html file...」。它記錄三題整體 tokens／wall time，不提供遊戲品質分數；README 註明不同 harness，且 Z.AI native harness 曾追問並用兩輪修復，部分 run 不符合 strict one-call。 | 記為 strict first-output 小遊戲方法案例並排除於上限題。以上精確日期搜尋已做；下一輪只有日期往後、新 build／模型加入或出現複雜遊戲 prompt 時才重查。 |
| `October 5, 2026 Opus 5.5 game one prompt`, `October 5 2026 GPT-6.1 Sol game playable`, official `GPT-6.1 Sol model`, `Grok 4.7 coding model September 2026 official`, `Gemini 4 Argon official release access developers API`, `Anthropic model transparency October 2026 Mythos 5.1 access` | 核對 OpenAI、Anthropic、SpaceXAI 與 Google 一手模型頁／公告。納入目前可實際呼叫的 GPT-6 Astra、GPT-6.1 Sol、Claude Sonnet/Opus 5.5、Fable 5.1、Grok 4.7；Gemini 4 Argon 當時僅 Fairwind 可信網安測試者 rollout，Anthropic Mythos 5.1 受 trusted-access 限制。沒有把尚未普遍開放的型號當成可立即重跑樣本。 | 每次正式跑之前再核 model ID、地區／方案可用性、coding harness 和 effort；記住 Grok 4.7 這類新候選，Gemini 4 Argon 開放後回查。模型型錄已查，不重做泛用「latest AI model」搜尋。 |
| `site:qwenlm.github.io Qwen3.8 Max stable August 2026`, `DeepSeek V4.1 Flash official release API open source 2026`, `site:ai.google.dev Gemini 3.8 Flash GA coding agent`, `Gemini 4 Argon official Google October 2026`, `Grok 4.7 official coding model availability` | 補查可立即使用的多家模型和不同硬體／API lane：Gemini 3.8 Flash 已 GA、官方稱適用長程軟體工程；Qwen3.8-Max 8/27 轉 stable；DeepSeek V4.1 Flash 9/10 上線 API 並提供 MIT model card／本機 serving；另確認 Argon 仍分階段 rollout、Grok 4.7 可用多種 coding harness。 | 新增 Gemini 3.8 Flash、Qwen3.8-Max、DeepSeek V4.1 Flash 為可跑候選；Argon 等普遍開放再加入。本輪官方可用狀態已核對，正式測試前只做 model-ID／存取資格再確認。 |
| `site:arxiv.org/abs "game generation" benchmark "2026" LLM game development`, `site:openreview.net "game generation" benchmark LLM 2026 playable`, `2026 benchmark "from natural language" "game" generation coding agent benchmark full game playable`, `2026 LLM benchmark game generation Unity Unreal full game end-to-end natural language`, `GameDevBench October 2026 GPT-6.1 Sol leaderboard`, `GameXpert-Bench leaderboard GPT-6.1 Sol Sonnet 5.5`, `Single HTML Game Bench current live page GPT-6.1 Sol Opus 5.5` | 對已列基準查新增數據，未發現 GameDevBench、GameASG、A2Z、SWE-Game、GameLogicBench、WebGameBench、OpenGame、GameXpert、GameCraft、Single HTML Game Bench 在 10/02–10/04 加入的新 frontiers run。新發現 [GameHorizon Suite](https://arxiv.org/abs/2609.25001) 是在既有 AAA 遊戲測操作與長程策略，不生成遊戲；官 repo 表示約 10/25 起才分批釋出資料／程式。 | GameHorizon 留作相鄰 gameplay benchmark 並監測 10/25 後的釋出；已查各列 benchmark 的前沿更新狀態，不重跑相同名詞與日期查詢，除非有新榜列／raw run／可重跑工具。 |
| `site:youtube.com/watch "Sonnet 5.5: No-Hype Full Review & Testing" Pat Simmons`, `"Backrooms" "GPT-6 Astra" "Fable 5.1" "Sonnet 5.5"`, `site:aiformortals.co "46:21" "Backrooms"` | 已讀原文的影片描述和 YouTube 頻道連結，再以標題／模型組合尋找 46:21 實測影片直達網址；搜尋引擎本輪沒有回傳可確認的 video URL。原文、五個 playable builds 及五張實際截圖仍可用。 | 不把影片直達連結標成已核實；已有原文與遊玩入口足以檢查作品。除非作者文章補上 video embed 或搜尋索引新增精確網址，不重跑同一影片標題查詢。 |
| `2026 benchmark dataset natural language generate complete playable games game generation benchmark LLM`, `playable games benchmark game generation LLM dataset 2025 2026`, `site:arxiv.org benchmark game generation playable game LLM natural language`, `complete playable game benchmark 2026 language prompt dataset`, `from-scratch game generation benchmark 2026 playable code LLM`, `natural-language game briefs benchmark complete games agents dataset 2026`, `site:aclanthology.org game generation benchmark playable 2026 educational prompt one-shot game` | 沒找到新、通用、固定 prompt 的高複雜 one-shot 完整遊戲 benchmark。找到 GAMED.AI 教育遊戲展示（200 題但 multi-agent／內部 validator）、RSIGame（重用 GameCraft-Bench 140 題、agentic iteration）、NEXUS（同 prompt 長 session arena）；也檢查並排除把既有 Pygame 專案重新生成的 V-GameGym／SKYLENAGE GameCodeGym，以及重用 GameCraft-Bench 的 RSIGame 作為新題庫。 | 以上各加入正式方法／排除註記，避免把相鄰工作誤標成固定題 one-shot 完整遊戲比較。已完成這組 broad query，不重跑相同泛搜尋；只有新資料集、prompt、最新模型原始結果或 playable evidence 出現才回查。 |
| `2026年9月 Claude Opus 5.5 AI 生成 游戏 一次提示 可玩 游戏 GPT-6.1 Sol`, `2026年10月 AI 编程 游戏 Claude Sonnet 5.5 完整游戏 提示词 可玩`, `GPT-6.1 Sol 游戏开发 一次提示 2026年9月 游戏 实测`, `Opus 5.5 Fable 5.1 游戏制作 实测 2026 9月 提示词`, `site:linux.do "Opus 5.5" 游戏 2026 Claude` | 找到 [LINUX DO 作者原帖](https://linux.do/t/topic/2972867?tl=en)：2026-09-30 Claude Opus 5.5 medium、一次提示做 Fez 風格 2.5D 網頁遊戲，含多場景、門傳送、旋轉視角隱藏方塊和關卡編輯器；作者連到[可玩版本](https://cc.36.re/fez/)。作者稱前兩關收集物可達、有 BGM，但關卡編輯器未找到，謎題缺乏新意且留言指出路徑／碰撞問題。V2 加「真結局」要求，故不算原始 one-shot。網頁工具未能獨立載入 playable URL。 | 新增為 Fez 類機制測試副題，不作模型排名：任務適合檢查視角旋轉下的 2D/3D 碰撞、場景連接和收集路線；但 scope 小於 Backrooms，且首版缺漏明確功能。後續不重搜原貼文；只有取得編輯器／可玩入口驗證、原始建置檔或其他模型同 prompt 新 run 時再更新。 |
| 日文 `2026年9月 AI ゲーム生成 Claude Sonnet 5.5 GPT-6.1 Sol ゲーム 開発 1プロンプト`, `2026 9月 生成AI ゲーム制作 Opus 5.5 プレイ可能 デモ 同じプロンプト`, `"Sonnet 5.5" ゲーム 制作 2026 9月 プレイ`, `"GPT-6.1 Sol" ゲーム 制作 2026`；韓文 `2026년 9월 AI 게임 제작 Claude Opus 5.5 한 프롬프트 플레이 가능한 게임`, `"Sonnet 5.5" 게임 제작 2026 플레이 데모`, `"GPT-6.1 Sol" 게임 개발 2026 한 번 프롬프트`, `"Opus 5.5" "Fable 5.1" 게임 제작 비교 2026` | 日文命中 9/29 Opus 5.5「沖洗 AI 開發者」[作者文章](https://note.com/gigabit_million/n/n5d251dcd5b20)：作者稱初版一 prompt，後續加日英版本；題型偏簡單。韓文搜尋未找到符合條件的案例，命中多是模型介紹或操作既有遊戲。 | 日文案例因難度及後續修改排除；韓文查詢目前無符合項。這組語言＋日期＋模型的泛搜已做過，除非更晚日期、新模型或原始 playable artifacts 出現，不重做相同查詢。 |
| 社群定向與排除查詢：`site:bilibili.com "Opus 5.5" 游戏 2026 游戏开发`, `site:zhihu.com "Sonnet 5.5" 游戏 2026 一句话 游戏`, `site:linux.do "Opus 5.5" 游戏 2026 Claude`, `site:x.com "Opus 5.5" "GPT-6.1 Sol" 游戏 2026`, `2026년 9월 AI 게임 제작 Claude Opus 5.5 한 프롬프트 플레이 가능한 게임`, `"Opus 5.5" "Fable 5.1" 게임 제작 비교 2026`; 另追查 Tibo simulator、karting、Rocket League/Fortnite/RPG 影片、[Create with Mark 10/1](https://www.createwithmark.co/updates/youtube-fvrv_ex8kiq/)／[10/2](https://www.createwithmark.co/updates/youtube-yd_okn0vdg4/) showcase | Tibo 討論顯示 Grok/Qwen 後續輪流修；Bilibili「五款遊戲」與三款 3D showcase 沒有可核實完整 prompt／對稱條件；Create with Mark 10/1 明確多輪修訂，10/2 雖有三個可視作品但沒有逐字 prompt／可信條件；日文案例後來有多語修改。 | 已把這些標成展示／排除而非新 benchmark。除非原始任務、每個模型對應 build 和單次輸出條件一起公開，不重查這些標題或通用社群詞。 |
| `"GPT-6.1 Sol" "game" playable September 2026 build coding agent`, `"Sonnet 5.5" game playable "Opus 5.5" September October 2026 -Backrooms -Diablo -Kart -Tumble`, `"Fable 5.1" game "GPT-6 Astra" playable 2026`, `site:x.com/adxtyahq/status "same prompt" game "GPT-6"`, `site:x.com "same prompt" "Fable 5.1" playable game "Astra"`, `site:youtube.com/watch "Claude Fable 5.1" "game" "GPT-6 Astra" same prompt build`, `"real working 3D combat flight game over the Alps"`, `"GPT-Astra 6 and Claude Fable 5.1" one-shot` | 查到 Krystian Wojtarowicz 9/12 Astra vs Fable 5.1 影片展示：3D 阿爾卑斯戰鬥飛行（熱氣球目標及會閃避的 drone）、CS-like 1v1、復古音樂播放器；影片自述同 prompt／無修訂，兩遊戲可玩，Astra 34 分鐘、Fable 22 分鐘。但影片中 Astra 先反問，作者又補「you decide for me now don't stop until you finish」，故不是純粹單提示；描述雖說 prompt 可複製，本輪未取到逐字內容。 | 新增為複雜遊戲 showcase／後續追原始 prompt 與兩份 build，不進公平 one-shot 排名。搜尋過的精確片名、作者、查詢詞不重做；只有找到原 prompt／可玩成品並確認是否對稱才升級。 |
| `"Build a polished, playable browser-based 3D flight simulator game from scratch"`, `site:x.com/adxtyahq/status "same prompt" game "GPT-6"`, `"Happy Wheels Bottle Run" GPT-6 Astra Opus 5.5`, `GPT-6 Astra Fable 5.1 flight simulator same prompt 2026` | 追查 Aditya 9/5 passenger flight simulator：有完整 prompt archive，要求機場／跑道／航廈、WASD/QE／油門／煞車、可信飛行物理、起飛—盤旋—降落、失敗重來、HUD／分數和 browser self-test；原提 GPT-6 Astra、Kimi K3、Fable 5.1、Gemini 3.8 Flash，作者主觀排序；後續社群提 Grok 4.7，但未找到對稱 playable builds／原影片。Happy Wheels Bottle Run 只有作品目錄提及，缺原始貼文與同題成品。 | Flight sim prompt 可作題型／需求清單來源，驗收流程長於單純飛行，但證據不足以做模型比較；列「待補 build」而非評分。Happy Wheels 為未核實線索。只在出現原帖、成品或新 run 時回查，不重搜已用標題／prompt 句子。 |
| `"GPT-Astra 6 and Claude Fable 5.1" one-shot`, `site:youtube.com/watch "rocket-launch simulator" "Astra" "Fable 5.1"`, `GPT-6 Astra Fable 5.1 game same prompt functional checks 2026`, `SandBase Aster Vault Astra Fable 5.1 3D game test` | 查到 SandBase 9/7 Aster Vault 三房間 3D 謎題：Astra/Fable 5.1、各三次、40k output ceiling、15 項功能檢查／鍵盤走訪／reset，有截圖與逐次成本時間，但未見完整 user payload 或 playable link；Fireship 火箭發射模擬器有影片與成本／作者玩感，卻沒有原 prompt 或公開 build。 | SandBase 可作 strict first-pass 操作校準，不符合上限規模；Fireship 僅定性展示。兩項都不併入主榜，除非完整 prompt／可玩 build 公開。 |
| Senko Vibecode Bench cards/prompts: 檢查 [official gallery](https://senko.net/vibecode-bench/) 全部已發布模型卡片、固定 RTS／voxel／flysim prompt、Opus 5.5、GPT-6 Sol、Sonnet 5.5 及 9/28 後 build | 確認本文既有 Vibecode Bench 條目可補充成本與日期：Opus 5.5 xhigh RTS／Voxel／Flysim 9/22 各約 $11–14、46–48 分；GPT-6 Sol xhigh 9/23 約 $0.57–0.74、5–23 分；Sonnet 5.5 xhigh 9/28 約 $7.60–8.70、35–45 分。原 prompt 和 gist/build 可見，支持固定任務、同題可玩校準；但 prompt 自述是 simple，不能替代高上限主測。 | Vibecode Bench 基礎資料已列在正文，這次是覆核模型 roster、固定題、可玩檔和成本／時間，不另立重複案例。只在加新模型／build 或 rubric 更新時回查。 |
| `"GPT-6.1 Sol" "playable game" 2026 game generated one prompt`, `"GPT-6.1 Sol" "game" "Opus 5.5" playable browser September 30`, `"GPT-6.1 Sol" "game" "Sonnet 5.5" playable prompt comparison`, `"Grok 4.7" "playable game" "same prompt"`; direct inspection of Goldie Grok 4.7 model card / task cards | 新核對 [Goldie Grok 4.7](https://goldiebench.com/models/grok47)：20 題同 prompt one-shot 單 HTML；平均 7.15/10、同 Grok 4.6 比 5.95、14/20 勝；作者逐題連 playable entry，且列 load／movement failure 和 playtest evidence。它補上 Grok 4.7 的新近真實輸出，不是長規格題；採 Agent OS harness 與作者主觀評分。 | 正文已更正 Goldie 舊模型 roster 描述，新增 Grok 4.7 run；只需追新增模型／新 run／rubric 變動，不重查此模型頁或 20 題數字。 |
| `JarvisUni topai Github tests Super-Mario World-Of-Tanks The-Last-Bridge`, direct inspection of [JarvisUni TopAI](https://topai.jarvisuni.com/) dated cards | 找到 9/18 Super Mario 1-1 recreation，頁面列 17 模型含 Opus/Sonnet 5.5、GPT-6.1 Sol，要求水管／磚塊／問號磚、敵人 AI、碰撞物理、道具／音效及可從頭通關；也找到 9/15 The Last Bridge 的一句方向需求（AI 佔領、孤島、人類守海橋），僅列 Claude Opus 5 V2 與 GPT-6 V2，測模型自行補完第一人稱塔防＋射擊。另有 9/13 World of Tanks 系統和 9/11 KOF XIV 固定邏輯任務，但 roster 偏舊。頁面列出 build cards；本輪瀏覽工具未能載入各 card iframe，因此只確認公開連結及任務描述，不宣稱已獨立遊玩。 | Super Mario 作為有較新模型的中高難度物理／整關通關比較，缺點是 clone 老遊戲；Last Bridge 是更貼近「給模糊題意、讓模型補玩法」的自主設計題型，但日期舊、版本名模糊、僅兩個模型；可用來重寫新模型對照題，不當現況排名。World of Tanks/KOF XIV 保留長系統題線索，無新模型 roster。後續只追新模型卡、原始完整 prompt、可實際載入的 build／錄影，不重掃站點。 |
| `"one-shot" "GPT-6.1 Sol" playable game October 2026 build browser game AI generated`, `"GPT-6.1 Sol" game generation live demo playable 2026 game benchmark October`, `"Claude Opus 5.5" "game" "single prompt" playable build September 2026 GitHub`, `2026 AI generated browser game one prompt playable model comparison October 2026 GPT-6.1 Sol Grok 4.7`; direct follow-up searches for Opus 5.5 multiplayer shooter, one-shot game RPG, and public galleries | 新增高複雜開放需求案例 [BioNeural](https://bioneural.de/)：原作者 9/26 Reddit 公開逐字 prompt，Opus 5.5 medium 一次 user task／約五小時 agentic session；原始任務讓模型自行選遊戲玩法、需多人部署，作者自述首版含網路多人、bots、語音、破壞、天氣與音訊。原貼後來加 mobile request，網站在 9/26–10/04 已多次更新；只按首輪自述，不把現版功能算作單次成果。新發現 [OneHack 48 builds](https://onehack.st/t/the-browser-games-the-newest-ai-actually-built-and-one-shelf-that-isnt-games/325491)（自稱 9/28 live-checked）與 [Frontier Games](https://github.com/theolundqvist/frontier-games) 可作新鮮可玩成品發現索引。另查 Opus 5.5 fantasy RPG 的公開 prompt，但只有截圖／參照圖，沒有可驗證 playable link；「$3.21 Opus video」是 code-generated animation，非遊戲。 | BioNeural 是目前最佳「模糊願望→模型自主設計、建置、測試、部署完整遊戲」任務原型，但只能作 agentic user-task 組，現網頁為後續版本，不能直接排名。兩個作品索引是發現用，不是 controlled benchmark。RPG 和 video 分別因無遊戲成品／不是遊戲而排除。以上站點與項目已查，後續追 fresh model rerun、原始首輪 snapshot、source/錄影即可，不必重搜名稱。 |
| `"Grok 4.7" "game" "one prompt" playable browser 2026 generated game demo`, `"GPT-6.1 Sol" "game built" "one prompt" playable live demo 2026 model output`, `"Fable 5.1" "one prompt" "playable" game multiplayer 3D 2026`, `"Opus 5.5" "one prompt" playable game multiplayer 3D October 2026`; 追查精確命中項目與額外近期貼文 | 精確查核 [Fable 5.1 NEON WARDEN](https://github.com/Nipale-ai/fable-5-1-one-prompt-game)：精確 prompt、live demo、screenshot 和 source 均公開；24 分、75 tool turns、95,832 output tokens、$9.90，high effort、RTX 5090 + Blender/ComfyUI/FLUX/LTX/ACE-Step；Playwright 已自動玩過 wave→shop→upgrade→wave，且記錄首輪無 retry。另查 Topple Pier（3D/Rapier 物理、多無限生成關卡、4 world/shop，但其 design doc 未公開）、Opus cozy game（prompt 自評分到 8.5+、overnight、多參考連結、不是一次輸出）、TopAI/ChinaAPI cards；DeepSeek V4.1 Flash/MiMo/Grok 4.7 的同題小遊戲資訊來自第三方匯總，Grok run 有 iteration，無客觀 rubric。 | Fable 一題已在上文列明；這次補核截圖、原始 prompt 和第一手 metrics，不重複建立條目。Topple Pier 可借物理與多關卡想法，但只有作者自述未公布原 brief；cozy game 因明確持續迭代排除。ChinaAPI 作為新近實測索引而非 primary benchmark，只有在找到原作者 X／影片／prompt 才可升級。以上具名作品已查，後續找新 build 或原始來源即可。 |
| `VibeGame benchmark game generation multi-agent framework 2026`, `GameEngineBench Unreal game development benchmark existing project`, `site:arxiv.org game generation benchmark playable 2026 agent evaluation` | 補列近期相鄰命中：VibeGame 是多代理生成框架／技術報告，不是同題可重跑模型比較；GameEngineBench 評既有 Unreal 專案中的 C++ 開發任務，不是從自然語言開始生成完整遊戲。其餘近似結果是代理玩遊戲、QA 或既有遊戲操作評測。 | 按研究邊界排除，避免再因名稱帶有 game/benchmark 而重新審查。僅當 VibeGame 公開固定 prompt 和對稱 playable runs，或 GameEngineBench 改成 from-scratch game generation 時回查。 |
| `site:reddit.com/r/aigamedev "Sunday October 04 2026" game one prompt playable AI generated`, `site:reddit.com/r/ClaudeCode "October 4, 2026" game Opus 5.5 playable`, `site:github.com "October 2026" "one prompt" playable game "Grok 4.7"`, `site:x.com "Oct 4, 2026" "GPT-6.1 Sol" game playable generated` | 10/03–04 社群新帖中，找到兩年自製卡牌遊戲、長期開發的農場／殭屍夢想遊戲（GPT-6.1 Sol 造素材、Opus 5.5 寫碼，作者明確說不是 one-prompt、持續數月修改），以及 AI 協作開發的六款 daily mini-games（人類定題、反覆改 UI／計分）。未找到在 10/04 新發、同時有一次任務、目前模型、可玩成品和原始條件的新合格案例。 | 依作者對多月工作／多輪修改的明確說明排除；daily mini-games 是 AI pair-programming 產品，不是一次生成比較。日期特定的 Reddit/X/GitHub 查詢已做；之後只查新日期或原文中新增的固定模型對照。 |


| `"Fortnite-style game one-shot test" Sonnet 5.5`, `site:jasonzhu.ai/en/prompts/claude-opus-5-5 Fortnite-style game one-shot`, `"mdaman010" "2104779190277181699" game prompt`, `"playable Fortnite-style battle royale" "2h54m"` | 核對 9/29 Sonnet 5.5 大逃殺案例；取得 445 字逐字 prompt、模型與 2h54m 作者自述、42 秒影片索引。X 原帖連線回查為 403；策展頁沒有穩定 playable build/source/QA。 | 在候選表升級為 high-system-density showcase，保留精確題目但不列成績。未拿同題找模型排名；只於作者公開可玩 build、source 或新增對照時查。 |

### 2026-10-04 新增：最新模型實物、同系列 build 與長規格種子

#### 同作者 Waterslide 系列：目前最值得核 prompt 的物理副測

作者公開三款可玩的原創 3D 水上競速 PWA，核心都含 13 名參賽者、彎道／跳台／捷徑、NPC 競速、練習 checkpoint、手機／鍵盤操作與 local progress：

| Run | 執行資料 | 公開驗收／限制 |
|---|---|---|
| [GPT-6.1 Sol — Slipstream](https://kjlkurt.github.io/waterslide-game-gpt-6.1-sol/) · [repo／prompt 摘要](https://github.com/KJLKurt/waterslide-game-gpt-6.1-sol/blob/main/progress.md) | extra-high；51m58s；82,245 output tokens；49 API calls；約 $1.93（含一個 auto-review child，Sol 部分估 $1.74） | Playwright 覆蓋桌面／觸控、race/practice、shortcut、離線 PWA、不同尺寸；頁面列測試與截圖報告。來源標為 0-shot，但有主模型 + reviewer child。 |
| [GPT-6 Astra — Splashline](https://kjlkurt.github.io/waterslide-game-astra/) · [repo／prompt 摘要](https://github.com/KJLKurt/waterslide-game-astra/blob/main/progress.md) | extra-high；34m59.892s；59,945 output tokens；約 $8.22 | repo 有 raycast physics、完整 race、兩次 ramp landing、elimination/checkpoint 與 10 項 browser E2E。文件說原始提示末句被截斷，並列出之後「approved for implementation」的 production brief；需釐清是模型內部自行規劃，還是人類有追加／核准。 |
| [Claude Opus 5.5 — Slide Rush](https://kjlkurt.github.io/waterslide-game-opus-5.5/) · [repo](https://github.com/KJLKurt/waterslide-game-opus-5.5) | extra-high；1h08m06s；365,717 output tokens、44.4M total processed tokens（多數為 cache）；約 $18.50 | source 有完整 race physics／NPC AI；作者標作不同 LLM 的 benchmark，但目前可見 task text 是從作品反推重建，不是原始 prompt transcript，且未查到與其他兩次相同的公開驗收報告。 |

這一組比截圖型 showcase 強很多：每版有真實 playable/source 和系統／自動測試資料，任務也明確壓連續碰撞、NPC 決策、觸控與 failure/retry loop；但尚未找到三個逐字相同的原始 user payload，也沒有統一盲評成績。**我的判斷是目前最好的「競速物理副測原型」，不是完整遊戲上限主題。**若拿來比較，先向同一 source 家族確認並固定 exact prompt、起始空專案、tools/reviewer 權限及時間上限，再做每模型至少三次；在條件未對齊前，三款只作同題材成品參照。

#### GPT-6.1 Sol 的 25 題實測：Goblin FPS 截圖

[日本作者 2026-09-30 的 Codex 實測文](https://note.com/masa_wunder/n/nd2bf3edafecb?hl=en)稱其以 xhigh effort 將同一組 25 題交給前代 Sol、GPT-6.1 Sol 和 Astra，其中 q12 是逐波增加敵種、可玩到 game over 的 goblin FPS，文內附三版實際畫面。這是目前新模型同題成果的補充線索，但 25 題完整 prompt、q12 單題 run log、可玩的遊戲輸出與數值評分未公開；故只把它當模型實物畫廊，不列 benchmark 分數。

![GPT-6.1 Sol、舊版 Sol、GPT-6 Astra 的 q12 goblin FPS 對照截圖（來源：原作者）](https://assets.st-note.com/img/1790739961-Qt0b47rh8myV9pHqxF3oSwEi.png?width=1200)

**本輪找到同作者較早的 Sonnet 5.5 25 題文章，補上同編號題型的新模型證據：**[9/29 原文](https://note.com/masa_wunder/n/nc4b72320c4f0)稱全組使用 xhigh；文中 q09 是具連段／傷害／擊倒演出的 3D 格鬥遊戲，q12 是可玩到底的第一人稱哥布林波次戰。原文附 q09、q12 真實生成畫面及影片；本輪實際開啟兩張圖確認介面與場景（q09 有雙方生命條、hit combo 和傷害數字，q12 有魔法欄、mana/HP、波次剩餘怪物數與小地圖）。q12 圖顯示可選四種魔法與哥布林波次 HUD，但不能僅靠單張圖驗證作者所稱「可玩到底」。

![Sonnet 5.5 25 題自製 benchmark 的 q09 3D 格鬥遊戲原作者截圖；有連擊／傷害顯示與雙方血條](https://assets.st-note.com/img/1790677221-Mbxsog9KumCDBhtUJlFdy5r1.png?width=1200)

![Sonnet 5.5 25 題自製 benchmark 的 q12 哥布林 FPS 原作者截圖；可見波次計數、四種魔法、HP/Mana 與小地圖](https://assets.st-note.com/img/1790677222-kvMVathwmRrCADF3SdjK4WJL.png?width=1200)

這讓同一位作者的私有 q12 題組至少在 9/29 文章出現 Sonnet 5.5、前代 Sonnet、Opus 5.5、GPT-6 Sol 的整體比較敘述，在 9/30 文章出現前代 Sol、GPT-6.1 Sol、GPT-6 Astra 的輸出圖；兩篇的共同 q12 編號顯示是同一題型家族，但文章沒有公開逐字題目或宣告跨文章逐字 identical payload，也沒有 repo/build/單題分數、seed、次數、工具及 objective rubric。故可將它列為**近期模型實物圖庫和任務範圍線索**，不能合併成七模型控制實驗，也不能聲稱各模型完全同 prompt 比賽。

#### Unreal 5.8 開放世界 /goal：適合作為高上限任務規格種子

[Tripo 收錄的完整提示](https://www.tripo3d.ai/3d-prompts/claude-opus-5-5-2105963123303747712)標示作者 Ruben TORNEY、Opus 5.5、2026-10-02。目標是 Unreal Engine 5.8 中可玩、逼真的熱帶島嶼休閒開放世界；要求多種連接生態區、第一／第三人稱移動、八類載具（含飛機物理）、可進入建築、不同動物、植被風動、日夜／天候控制、對應物理的環境特效與分區音景，並用 UE MCP、素材服務和 36 小時完成 MVP。提示明確要求把各生態區／系統委派給 Sonnet 子代理，並持久保存進度，因此是長程 agentic /goal 而非 strict first-output；本輪沒找到可玩的輸出、原作者運行報告或 QA。適合借作任務設計來源，若要公平重跑需縮減外部素材與 36 小時權限差異。

#### GPT-6.1 Sol 的 Crowd Rush：高完成度展示但 prompt 已含修訂

[Agent Games 頁面](https://agentgames.dev/play/crowd-rush)同時提供可玩版與 prompt 歷程摘要；版本 4.1.0 標示更新於 2026-10-02，GPT-6.1 Sol High、Codex desktop、約 43 分／70k tokens／$7.50。遊戲是 3D 群體跑酷 campaign：30 關、六區、多人群碰撞、算術增減門、不同區域 hazard、路線分支、guardian battle、永久升級、手機控制和排行榜。頁面顯示的提示要求移除互動 boss 操作，回復自動碰撞並用 health−1/equal/+1 測勝負；這是 revision prompt，不是可證明的原始建置 prompt。故它適合作視覺／整合展示，不能標成 strict one-shot 成績。

#### 作品索引中的新高複雜候選

- [The Duke’s Lawn](https://cnvs.dev/opusmo/)：Frontier Games 把它標為 Opus 5.5 one-shot，多人割草模擬，作者說直播觀眾曾加入遊玩；CNVS 工具鏈、逐字 prompt、成品測試和執行條件未公開，原 X 貼文本輪 403。列社群展示候選，不排名。
- [The Glass Alibi](https://www.shiptheprompt.com/vibes/the-glass-alibi--zaf4nsmtyf9glzjav1ff)：匿名 Opus 5.5 單檔分支推理故事，頁面摘要稱約五場景／三結局，有 clue notebook 與重玩；無源碼、run transcript 或被核實 playable output。
- [Pocket Metropolis](https://www.shiptheprompt.com/vibes/pocket-metropolis--bqf5sdettjez2s1hokc0)：匿名 Opus 5.5 城市建造 sandbox，提示涵蓋 12×12 等角地圖、建築／道路／水、人口與幸福、車輛移動、日夜、存檔；題目適合機制題靈感，但未有可信驗收。
- [Lethal Company: Opus Edition](https://www.shiptheprompt.com/vibes/lethal-company-opus-edition--o8czltidhbissx30dduo)：合作搜刮、怪物、配額和 extraction 看似高複雜；索引明示展示的 prompt 是依作品反向重建，不是作者原文，所以不得視為真實一次提示證據。
- [KOMOREBI](https://3d-prompt.com/prompts/wright-flyer-through-a-japanese-forest-2096467585785286808) 與 [ODYSSEY: The Cyclops’ Island](https://3d-prompt.com/prompts/cyclops-island-threejs-game)：有完整任務規格和視覺／live demo 線索，但頁面標示改編／重建 prompt 或重新製作尚未核實；可取題型，不用來算原始模型成果。
### 2026-10-04 新增：Fable 5.1 vs GLM-5.3 同提示 3D 遊戲實測

[Nipale-ai Fable 5.1 頁面](https://nipale-ai.github.io/fable-5-1-one-prompt-game/)與[GLM-5.3 頁面](https://nipale-ai.github.io/glm-5-3-one-prompt-game/)提供目前最完整的開放式 3D 遊戲同提示展示之一；兩方提示全文一致，對照、可玩版、原作者截圖與 run metrics 都可查。Fable 做出 **NEON WARDEN**：雲海上的六角競技場 3D 波次射擊，有懸浮機甲、三種敵人、商店與升級；GLM-5.3 做出 **VESPERA**：限時日蝕探索，需收齊八枚星核碎片並封印方尖碑，頁面列地形、植被、墜毀飛船、無人機、音樂與影片等內容。

| 模型 | 可見完成資訊 | 作者頁面記錄的執行量 | 成品／證據 |
|---|---|---|---|
| Fable 5.1 | NEON WARDEN；單一自包含 HTML；首輪完成、作者記錄一次 green gate、無 retry | 24.2 分鐘、75 turns、$9.90、95,832 output tokens、4.4 MB | [可玩版](https://nipale-ai.github.io/fable-5-1-one-prompt-game/)、[原作者截圖](https://nipale-ai.github.io/fable-5-1-one-prompt-game/vorschau-fable.jpg)、[prompt/source repo](https://github.com/Nipale-ai/fable-5-1-one-prompt-game) |
| GLM-5.3 | VESPERA；8 分鐘日蝕循環、收集八枚碎片後通關；作者頁面稱同樣首輪完成、無 retry | 27.3 分鐘、146 turns、$9.39、106,966 output tokens、13.9 MB | [可玩版](https://nipale-ai.github.io/glm-5-3-one-prompt-game/glm/)、[原作者截圖](https://nipale-ai.github.io/glm-5-3-one-prompt-game/vorschau-glm.jpg) |

| NEON WARDEN — Fable 5.1 | VESPERA — GLM-5.3 |
|---|---|
| ![Fable 5.1 NEON WARDEN 遊戲畫面](https://nipale-ai.github.io/fable-5-1-one-prompt-game/vorschau-fable.jpg) | ![GLM-5.3 VESPERA 遊戲畫面](https://nipale-ai.github.io/glm-5-3-one-prompt-game/vorschau-glm.jpg) |

**相同提示與執行條件：**任務要求自由選遊戲題材，製作單一離線可開啟的 3D HTML 遊戲，使用 Blender 與 ComfyUI，並生成 FLUX 圖像、LTX 影片片段及 ACE-Step 音樂；要求檢查素材、Chrome 離線運行且不依賴外部檔案，禁止追問。作者說兩次採 high effort、64k output token ceiling、相同 gate 與 RTX 5090。GLM 頁記載 Playwright 自動收齊八枚碎片並到達勝利狀態、零 console errors。Fable 專案也公開自動流程；這些是作者公布的執行記錄，並非第三方複驗。GLM 頁未找到可獨立核實的精確 run timestamp，故本文件只標本輪核對日，不把發布／執行時間猜成確定日期。

**怎麼用這組案例：**這是高視覺、跨工具整合、較高自主設計難度的展示；和 BioNeural 一樣讓模型選玩法，但它多了明確的 3D／離線／多媒體工具規格及完整交付指標。它比 Backrooms 更容易從截圖理解成品規模，也因相同 prompt、有兩個模型和可玩輸出而更適合做重跑種子。不過硬體、工具存取、權限與作者實作環境綁得很緊，且目前僅兩個模型、各一個 run；不要直接解讀為普遍模型排名。若重跑，應把「相同模型 API + 相同工具」作一組、作者原生 coding-agent + 素材工具作另一組，兩組分開報告，並至少三次重複。

### 2026-10-04 新增：近期可玩 showcase 與排除項

- **Hollow County**（[原作者 Reddit 貼文](https://www.reddit.com/r/ClaudeAI/comments/1wsrcqe/a_browser_based_doom_and_project_zomboid_blend/)、[可玩版](https://hollow-county.forfot.dev/)）：Opus 5.5 High、四個漸進關卡、故事、程式生成美術與聲音。作者稱在單一五小時 Pro 額度內完成約 98%；但過程先答兩個澄清問題，後加外觀和小地圖調整，也製作 trailer；沒有逐字 prompt 或固定評分。可當高難度 agentic 成品看，不是 one-shot 排名。
- **Roman Empire tycoon**（[原帖](https://www.reddit.com/r/aigamedev/comments/1wwjd83/opus_55_built_a_cozy_and_addictive_tycoon_game/)、[可玩版](https://empire-tycoon.com/)）：Opus 5.5、三段五小時 session，採舊規格、討論設計、AI playtest、Meshy 模型和手機調整；排除 strict one-shot。
- **Sketch RTS**（[Linux.do 原帖](https://linux.do/t/topic/2977389)、[source](https://github.com/shuxueshuxue/sketch-rts)、[可玩版](https://lexicalmathical.com/sketch-rts/)）：有雙種族科技樹、經濟、英雄、野怪、多地圖、海戰、AI、多人與 replay/SDK 等高系統範圍；repo 持續開發且沒有原始任務 prompt、起訖條件或對稱測試，只作 RTS 題型靈感。
- **Grok 4.7 GTA-style world**（[報導與影片](https://www.tweaktown.com/news/113703/forget-gta-6-ahem-grok-4-7-made-a-gta-style-game-from-one-prompt-as-musk-boasts-of-ai-developing-photo-realistic-games)、[貼文備份](https://elonmuskarchive.org/posts/2102406300303049172)）：複雜度高但發生於 9/22，沒有公開 prompt 或 playable build，僅 viral teaser，不列基準。
- **CommandCode Flappy Bird 模型展示**（[README](https://github.com/CommandCodeAI/slash-design-showcase/blob/main/flappy-bird/readme.md)）：含 Grok 4.7 等模型，但題目太簡單，部分輸出只是靜態程式檢查／Node VM 模擬，無法支持完整遊戲上限評估；只保留為簡單題 sanity check 的反例。
- **Gemini 3.8 Flash 官方遊戲展示**（[官方頁](https://deepmind.google/models/gemini/flash/)）：城堡 3D 探索／謎題使用 looping instruction 與 Nano Banana 素材，沒有逐字 prompt、可玩 build 或 score；保留官方 showcase 線索，不當 one-shot 比較。
- **Qwen 3.8 Max Sulat 索引**（[模型展示索引](https://qwen.demos.sulat.com/)、[總索引](https://demos.sulat.com/)）：列 42 個模型 demo，標題包含多種遊戲／互動作品，但本輪未核到各作品 prompt、build、驗收條件或同題評分；當發現索引用，逐案查證後再升級。
- **Qwen 官方 Snake 教學**（[prompt 與教學](https://platform.qianwenai.com/docs/token-plan/playbooks/token-plan-playbook-mini-game)）：可單提示生成可玩的 HTML/Canvas Snake；題目過簡單，排除上限測試。
- **Phaser Game Agent**（[9/22 公告](https://www.phaser.io/news/2026/09/opus-5-5-grok-4-7-and-muse-spark-1-3-in-the-phaser-game-agent)）：有 Opus 5.5、Grok 4.7、Muse Spark 1.3 等選擇，但案例短、依賴預建引擎／模板，沒有多模型同題成品和品質量表；屬工具展示，不是公平模型比較。
| `Nipale Fable 5.1 one prompt game GLM-5.3 same prompt update October 2026 NEON WARDEN`, `"NEON WARDEN" "GLM-5.3" game benchmark one prompt`, `"fable-5-1-one-prompt-game" GLM-5.3 results`, `"Build a playable 3D game. One self-contained HTML file" GLM game result`; 核對 [Fable repo](https://github.com/Nipale-ai/fable-5-1-one-prompt-game)、兩個作者頁、byte-identical prompt、截圖與 run 記錄 | 找到同一作者同 prompt 的 Fable 5.1 NEON WARDEN vs GLM-5.3 VESPERA 配對；分別公開可玩版與截圖，作者記錄 RTX 5090、相同素材工具鏈、成本／時間／token；GLM 頁有 Playwright 通關與零 console error 敘述。 | 新增正文並列 showcase／重跑種子；只在新模型、新 run、prompt 或可驗證驗收材料出現時回查，避免重搜兩個遊戲名稱及相同 prompt。不可把作者自述當第三方複驗或純模型排名。 |
| `Gemini 3.8 Flash built game looping instruction official hands-on`, `Qwen3.8-Max generated playable game one prompt demo 2026`, `"qwen.demos.sulat.com" GitHub`, `site:github.com "Ashwake" "Qwen" demo`, `DeepSeek V4.1 Flash generated game playable demo prompt October 2026`; 另查 [Phaser Game Agent 9/22 公告](https://www.phaser.io/news/2026/09/opus-5-5-grok-4-7-and-muse-spark-1-3-in-the-phaser-game-agent) 與 [Qwen Snake 教學](https://platform.qianwenai.com/docs/token-plan/playbooks/token-plan-playbook-mini-game) | Gemini 官方頁是 looping instruction + Nano Banana 的城堡探索展示，無 exact prompt/build/score；Sulat 有 Qwen 3.8 Max 的 42 個 demo，但未核到各自 prompt/build/驗收；Qwen Snake 是單模型簡單題；Phaser agent 有新模型但採預建引擎與短題；DeepSeek targeted 查詢只有先前已記錄 run，沒有新的上限型一次生成合格項。 | 各來源已在近期 showcase 區標示定位／排除原因。後續只逐項查出原始 prompt、模型版本、可玩 build 和測試證據的新 demo，不重掃索引或重跑泛搜。 |
| `site:reddit.com/r/aigamedev "Grok 4.7" game "one prompt" October 2026`, `site:reddit.com "GPT-6.1 Sol" "game" playable one prompt October 2026`, `site:github.com "Grok 4.7" "game" "one prompt" 2026`, `site:x.com "Grok 4.7" "one prompt" game playable October 2026`, `"October 4, 2026" AI game generation one-shot`; 精確追查 Hollow County、Roman Empire tycoon、Sketch RTS、Grok GTA、CommandCode Flappy Bird 及 GPT-6.1 safari/pool 範例 | Hollow County 是 Opus 5.5 High 高複雜可玩遊戲，但有澄清／後續迭代、無 exact prompt；Roman tycoon 是 3×5 小時與多輪設計；Sketch RTS 系統面很大但持續開發、無起始 prompt；Grok GTA 線索 9/22 且無 prompt/build；Flappy Bird 題太簡單；新日期社群另有多月遊戲和 daily mini-games，均非 one-shot。 | 新增合格 showcase 或具名排除項於正文。已查以上作品和該日期泛搜；只於出現首輪 snapshot、逐字 prompt、同題新模型 run 或獨立驗收證據時回查。 |
| `"Oct 1, 2026" AI generated game survival build game model`, `"Oct 2, 2026" AI made game RPG playable model generated`, `"Oct 3, 2026" AI generated game simulation strategy playable`, `"Oct 4, 2026" AI coding game generated playable RPG`, `site:reddit.com/r/aigamedev "Thursday October 01 2026" game AI survival RPG sim strategy`, `site:reddit.com/r/aigamedev "Friday October 02 2026" game "Claude Opus 5.5" playable`, `site:reddit.com/r/aigamedev "Saturday October 03 2026" "game" Claude Opus 5.5 browser`, `site:reddit.com/r/ClaudeAI "Oct 4, 2026" game made Opus 5.5 playable survival` | 增量追查確認海盜遊戲（約三天、290 commits、手作資產、作者反覆測改）、Opus 5.5 Lander launch vs 10/2 重跑（原 prompt／兩份 build 未公開、N=1）、Space Federation/Star Reach（既有 DOS 遊戲重建）、The Big Suck 2D→3D（既有 2D 專案移植），以及 Procedural Pixel Creatures（Godot 程序化內容工具、不是遊戲成品）。查 GamesByAI 10/3 資料集中的 Field of Command、Eyrie：收錄日不能證明生成日，無模型版本／prompt；Field of Command 要登入。 | 海盜、Lander、Star Reach、The Big Suck 已有正文條目，本次只補來源核對與避免把迭代／重建當 one-shot；新增 Procedural Pixel Creatures、GamesByAI data directory 作排除線索。精確作品詞已查，只有新 build、prompt、獨立驗收或明確新模型 run 才回查。 |
| `"I gave Claude Opus 5.5 the idea for a pirate game" demo`, `"Lander" "Opus 5.5" "October 2" Godot Braben`, `"Procedural Pixel Creature Workshop" Claude Opus 5.5`, `"The Ship Remembers" "Oct 1, 2026" browser game AI`, `"Magehold Fairwinds"` | 額外追查可能的高難度線索：海盜遊戲原帖無逐字 prompt／公開 playable build；Lander 有同題重跑敘述但無 repo/build；Procedural Pixel Creatures 是程序化生物創作工具；The Ship Remembers 與 Magehold Fairwinds 搜尋未取得足夠可核實的一次生成任務證據。 | 上述精確詞與項目已查；作品目錄或貼文提及不代表首輪產物。若未出現原始任務和實際輸出，不重新查相同標題。 |
| `site:note.com/masa_wunder/n/nd2bf3edafec "q12" FPS goblins game prompt`, `"FPS game fighting goblins" "GPT-6.1 Sol"`, `"25-question benchmark" "GPT-6.1 Sol" games q12`, `"まさお" GPT-6.1 Sol 25問 ベンチマーク ゲーム プロンプト` | 確認日本作者 9/30 25 任務 xhigh 對照；q12 goblin FPS 由前代 Sol、GPT-6.1 Sol、Astra 生成並有輸出截圖，作者稱波次升級、可玩至 game over；無 exact q12 prompt、遊戲檔、逐 run score。 | 補充最新模型圖像案例，不列成可重跑對照；只有公開 q12 exact payload／build／新模型 run 才回查。 |
| `site:note.com/masa_wunder "q12" "GPT-6 Astra" Fable game`、`site:note.com/masa_wunder "q12" "ゴブリン" "Opus 5.5"`、`site:note.com/masa_wunder "一人称視点" ゴブリン q12 Astra Fable`、`"僕のベンチの q12" Opus 5.5 Fable Astra`、`site:github.com "masa_wunder" "q12"` | 新找到 9/29 Sonnet 5.5 文章：同作者 25 題 xhigh 自製 bench，明確識別 q09 3D 格鬥與 q12 波次哥布林 FPS，稱 q12 可玩至最後；原圖和影片嵌入均公開。實際用瀏覽器看過 q09/q12 圖片；q09 可見 hit count/damage/health bars，q12 可見四魔法、HP/Mana、wave count/minimap。查詢沒有找到 q12 repo/build 或 exact prompt。 | 把相同編號作同題型線索，不跨 9/29 與 9/30 文章推斷完全相同 prompt；不可把模型集合拼成 controlled 7-model comparison。q09/q12 圖片已查，不再重找。只有公開原提示、可玩檔、逐題分數/跑次條件後才升級。 |
| `Ruben TORNEY Oct 2 2026 Unreal Engine 5.8 open world relaxation game Opus 5.5 playable`, `"open-world relaxation game" "Unreal Engine 5.8" playable Opus 5.5`, `site:x.com "Ruben TORNEY" "Opus 5.5" Unreal game`, `site:3d-prompt.com/prompts/gpt-6-1-sol game playable October 2026`, `site:3d-prompt.com "GPT-6.1 Sol" "Games" prompt playable`, `site:3d-prompt.com/prompts/claude-sonnet-5-5 game Oct 2026`, `site:3d-prompt.com "Qwen 3.8" games prompt` | 取得 Opus 5.5 /goal 36 小時 UE5.8 開放世界完整提示；查出 KOMOREBI 與 Cyclops Island 屬改編／重建提示或未核實重建，無可確認的 original one-shot output。 | /goal 規格可當題目種子；同目錄其他提示只按 curate evidence 等級記錄，不把改寫 prompt 誤作 run 原文。只於發現 original session/build 後追查。 |
| `site:github.com/KJLKurt waterslide-game "GPT"`, `site:github.com/KJLKurt "waterslide" game AI model`, `"Splashline" "waterslide-game" model`, `"Build a mobile-first, original 3D waterslide racing PWA"`, `site:github.com/KJLKurt/waterslide-game-opus-5.5 "Original prompt"`, `site:github.com/KJLKurt/waterslide-game-opus-5.5 "Total elapsed time"`, `site:github.com/KJLKurt/waterslide-game-opus-5.5 "Main model" "Cost"` | 追查 GPT-6.1 Sol Slipstream、GPT-6 Astra Splashline、Opus 5.5 Slide Rush；核實三個可玩/source 和各自不同測試/成本，原 prompt 只摘要或重建、未能證明逐字同一。 | 更新既有 Slipstream 案例為水上競速系列；後續只確認 prompt lineage 或新模型版本，不用「same task/benchmark」字樣直接假設公平。 |
| `AI games gallery "Gemini 4" generated playable game prompt 2026`, `AI game gallery "GPT-6.1 Sol" "play" model generated game`, `"one prompt" "GPT-6.1 Sol" game playable browser AI`, `"Gemini 4 Argon" game generated playable demo game builder`, `site:agentgames.dev/play/crowd-rush`, `site:frontiermodels.cc "The Duke's Lawn" Opus 5.5 game one-shot`, `site:shiptheprompt.com/vibes "The Glass Alibi" Opus 5.5 playable prompt`, `site:shiptheprompt.com/vibes "Pocket Metropolis" Opus 5.5`, `site:shiptheprompt.com/vibes "Lethal Company Opus Edition" prompt` | 發現 GPT-6.1 Sol Crowd Rush（頁面列 30 關、43 分/$7.50/約70k tokens、10/2更新；顯示 prompt 是 revision）、Opus The Duke's Lawn 多人直播展示但無原文、ShipThePrompt 新索引項缺可驗證 build／評測或 prompt 是逆向重建；Argon 只有二手 demo 線索。 | Crowd Rush 列完整 agentic build showcase、非 strict one-shot；其餘目錄列發現線索／排除。索引、作品、提示都已查，需等新增 original prompt／build／驗收 evidence 才重搜。 |
| `site:arxiv.org (game generation benchmark OR game development benchmark) October 2026 AI model`, `site:github.com benchmark game generation "GPT-6.1" OR "Opus 5.5" OR "Grok 4.7"`, `site:huggingface.co/spaces game generation benchmark leaderboard 2026`, `site:github.com/areal-project/GameASG-Bench commit October 2026 model runs`, `site:github.com "GameXpert-Bench" October 2026 leaderboard model results`, `site:arxiv.org/html/2610 game generation benchmark LLM`, `site:openreview.net game generation benchmark October 2026 coding agents games`, `site:tongxuluo.github.io/gamecraft-bench-website "2026-10-0"`, `site:github.com/FreedomIntelligence/gamecraft-bench "GPT-6.1 Sol" "2026-10"` | 10/1–4 官方基準核查未發現 GameCraft-Bench、GameASG-Bench、GameXpert-Bench 新 frontier runs；V-GameGym 是既有 Pygame 專案任務；GameHorizon 是玩遊戲 agent 而非生成遊戲。 | 記錄本輪無增量結果與查核界線；只於官方 leaderboard、raw run、playable artifact、repo commit 更新後回查。 |
### 2026-10-04 方法線增量：strict first-output 與 MMORPG 題型

既有基準表已記錄 SWE-Game、WebGameBench、OpenGame、GameLogicBench、A2Z 等；本輪重新查證後，重要修正僅有：A2Z repo 在查核當下仍未提供可直接重跑的完整資料／輸出，且論文成績包含兩輪修正；GameLogicBench 的逐 tick 測試器另以 mutation 驗證其能否拒絕錯誤實作。這些內容不重複建新案例，只更新表內口徑。

- **[SandBase Aster Vault](https://blog.sandbase.ai/gpt-6-astra-vs-fable-5-1-3d-game-test-2026/)** 是同 prompt 小型 3D 房間謎題，40k output cap、同機 Chrome，只評第一份輸出不修程式，各模型原始三次；Astra 3/3 通過 15 項功能檢查及鍵盤實走，Fable 有一次通過、一次初始化失敗、一次期限內無 code。它有逐次成本／延遲與畫面，但沒有可獨立玩的原 artifact，且完整 prompt/checker 未公開。可借方法：逐次保存原始輸出，crash／no-code／timeout 分開記錄；依序測狀態依賴、碰撞、通關、reset；用真實鍵盤走訪，不只看內部狀態 hook。題目太小，不是上限排名。
- **[MMORPG AI Progress archive](https://www.mmorpg-benchmark.com/)** 的 3D browser MMORPG 題型涵蓋連線／登入等高上限需求，但網站目前 leaderboard 無可核實完整資料；搜尋索引可見的 Fable 5 記錄為 2026-06-10，評分主觀且允許 continuation。只作題型參考，不列新模型比較。
### 2026-10-04 多語搜尋新增案例：Fez 風格視角旋轉平台遊戲

[LINUX DO 原作者貼文](https://linux.do/t/topic/2972867?tl=en)（2026-09-30）公開 Claude Opus 5.5 medium 的初次輸出，以及作者提供的[可玩入口](https://cc.36.re/fez/)。原始中文 prompt：

> 模仿Fez的游戏玩法做一个网页版的Fez游戏，并且附带关卡编辑器。主角的外形要贴合Fez原版游戏，场景风格也要贴合原版游戏。有多个场景，和原版游戏一样，可以通过门来在不同场景之间传送。并且根据Fez的旋转玩法设置隐藏的收集方块。

**作者自述條件與觀察：**使用 Opus 5.5、medium effort；作者稱 Claude Pro 每週額度約用 5%、五小時額度約用 25%。作者測了前兩個場景，稱收集物可達且作品抓到 Fez 的旋轉核心：Q/E 旋轉視角，在 3D 世界中採 2D 碰撞，並有背景音樂。作者也說謎題缺乏新意，未找到 prompt 要求的關卡編輯器；討論串還提到路線／門和樹木段的碰撞疑慮。這些是作者／留言的手動觀察，沒有統一驗收或獨立評分。本輪工具無法載入 playable URL，所以只確認入口被公開，沒有宣稱已親自遊玩。

**評測價值：**它是很好的機制理解副題：要求模型把視角旋轉、平台路徑、跨場景傳送、隱藏收集物連成一個可玩循環，可專門測旋轉後的碰撞／可達性和場景狀態。因任務不涵蓋長時程敵人 AI、資源經濟或多階段戰鬥，複雜度仍低於 Backrooms 主測和 Diablo／Airship Trader 系統題；再加上首版漏掉關卡編輯器，現有證據適合拿來設計測試規格，不足以給 Opus 排名。

作者另附一個加入「真結局」的 V2 入口，但那是新增要求後的版本，不能併入一次提示首版。另有作者提及曾用 GPT-6 Astra 做類似 Fez，未附相同逐字 prompt 或對稱產物，不作同題比較。

**下一步重跑規格建議：**以同一逐字 prompt、同一空白 HTML/Three.js harness、相同時間上限，至少 3 個獨立 run；要求收集物、旋轉後可達路徑、門的雙向場景轉換、關卡編輯器均須可在成品內操作。每項以實際操作路徑錄影及狀態檢查驗收；保留漏件與失敗 build，不接受後續補問或挑選最好版本。把「視角旋轉後仍能通行」與「關卡編輯器是否存在」設為硬性檢查。

### 2026-10-04 新增的高上限開放式一任務實例與作品圖庫

#### BioNeural：Opus 5.5 自行決定玩法的多人射擊遊戲

[原始 Reddit 貼文](https://www.reddit.com/r/ChatGPT/comments/1wqd0gg/houston_we_have_a_problem_opus_55/)（2026-09-26）有公開單次任務提示與[目前可玩的 BioNeural 網站](https://bioneural.de/)。提示不是指定玩法系統的長 GDD，而是要求用 Three.js 製作可上傳到作者網域／共享主機的線上多人遊戲，交代主機記憶體 250MB、最大空間 5GB，讓訪客輸入名稱就加入；玩家可自由決定作品是 shooter、策略或其他新玩法，並要求完整可玩。作者授權使用現有電腦工具及 Blender，安裝新工具要先問核准；作者說明其執行環境最後給了電腦完整權限，並使用已有 Node/PHP/Blender、瀏覽器、Suno、Cloudflare 等工具。

**原作者對首輪成品的說法：**Claude Opus 5.5 medium，在一個約五小時的連續工作 session 內完成，作者稱不用人工碰電腦；其自述初版已有多人連線、bots、近距離語音、可破壞資產、天氣、音樂與音效，並上傳部署。遊戲說明頁還列出 40 kills／7 分鐘勝負、10 張輪替地圖、20 bots、武器／拾取／空襲／核彈、車艇、地圖破壞及語音／好友等規則。這是作者的測試敘述，沒有公開獨立驗收套件或另一模型同題 run。

![原作者 Reddit 貼文附的 BioNeural 遊戲截圖](https://external-preview.redd.it/houston-we-have-a-problem-opus-5-5-v0-N2tsYXBtZnFpcnJoMcNZX-c0ln_x7hDFN76nMdStOm7YyX9OAJwaffXeNI0F.png?auto=webp&crop=smart&format=pjpg&s=59ab4b3c38a79fa62e393007361fc05e124fd39f&width=640)

**必須區分首輪和現版：**原作者在貼文後續又要求手機支援；目前網頁的更新紀錄顯示 9/26 上線後持續有 9/27–10/04 的地圖、專用伺服器、5v5、戰隊、商店等更新。因此 bioneural.de 的現況只能當作品/玩法展示，不能說整個現版都是那一次提示的產物。該案例不是「單一模型呼叫」；它比較像一次 user task 啟動的 agentic 長 session，工具與網路服務權限很寬。

**對本評測最有用的地方：**這是目前找到最貼合「把大方向丟給模型，讓它自行補完整個遊戲」的實例，比固定短題名更有上限測試價值。它適合轉成新的跨模型題目：所有模型都在同樣空白 VPS／browser 專案、同樣可用工具及部署權限下，收到同一份含部署邊界的模糊需求，限時完成後按功能循環、多人同步、bot、破壞狀態、語音、資源／部署安全分項驗收。若不提供同等伺服器與服務金鑰，就要把網路多人和外部素材生成移出硬性要求，避免測成工具/帳號差異。每模型至少三個獨立 session，錄下 prompt→計畫→build→playtest→deploy 全程，不能拿 10/04 更新版分數回推 9/26 首輪能力。

#### OneHack 與 Frontier Games：看新實物，不當作有控制條件的比較

- [OneHack 48 builds](https://onehack.st/t/the-browser-games-the-newest-ai-actually-built-and-one-shelf-that-isnt-games/325491) 自述在 2026-09-28 逐項開啟 live links 核對，混合 X 書籤、AgentsLoop/awesome-opus-5.5-games 與新搜尋，含 Opus 5.5、GPT-6 Astra、Fable 5.1 的 42 個可玩遊戲以及影片/不可直接遊玩的項目。適合按題材找圖像與成品連結，但不是完整 48 個都為遊戲或同條件測試，也未提供統一 prompt、run 條件和評分。
- [Frontier Games GitHub](https://github.com/theolundqvist/frontier-games) 是持續整理的成品索引，區分 playable、需下載/build、watch-only，部分項目列出 one-shot／原文／source。較值得深看例子包括 Turbo Kart Rally（五個 Opus 子代理）、OVERRUN Dockyard Nine（Horde FPS one-shot）、Arkenfall（開放世界動作遊戲）和 Pelican Bike Ride（單句 prompt、零人工編輯）；其中有些 agentic 多代理，有些缺 exact prompt，需逐案追原帖與 source，不能由策展標籤直接推成 benchmark 分數。

這兩個目錄能大幅擴充「可看什麼」的樣本，也可讓使用者直接從 playable link 看出視覺與複雜度；後續只追有原始 prompt／模型條件的新條目，不再整站重掃。

### 2026-10-04 新增優先候選：MALL ACTION 固定長規格、跨模型一次任務

[原始 benchmark repo](https://github.com/rlorca/mall-action)明確寫明：同一份 [488 行 one-shot prompt](https://github.com/rlorca/mall-action/blob/main/one-shot-prompt.md)，讓每個模型從空資料夾自主完成；每個模型有彼此獨立的 Git branch 和可玩部署。這比只提供「做個遊戲」的社群案例更容易固定題目，也比從程式碼反推提示可靠。repo 的 protocol 要求 fresh model session、逐字提供唯一任務、不要提示或參照其他 branch、只為 harness 必要動作介入；並記錄 model/id、日期、harness、effort、耗時和 interventions。作者的規則容許同一任務內自主工具、測試與修正，因此屬於「一次 user task 的 agentic run」，不是單一 API completion。

| Opus 5.5 | Sonnet 5.5 | GPT-6.1 Sol |
|---|---|---|
| ![Opus 5.5 成品截圖：多層商場與電梯](https://raw.githubusercontent.com/rlorca/mall-action/opus-5-5/docs/screenshots/mall.png) | ![Sonnet 5.5 成品截圖：商場、店舖與電梯](https://raw.githubusercontent.com/rlorca/mall-action/sonnet-5-5/docs/mall.png) | ![GPT-6.1 Sol 成品截圖：商店走廊與電梯中的角色](https://raw.githubusercontent.com/rlorca/mall-action/gpt-6-1-sol/public/screenshots/mall.png) |

三張均為對應 branch README 引用的原始作品截圖，已在瀏覽器實際開啟檢視。可快速看出都在呈現多層商場、店面及電梯，但遊戲狀態、截圖尺寸、場景位置並不一致，不能從這組圖直接排視覺名次；請再點上方各自的 playable 連結實玩。

**題目有多難：**遊戲名為 MALL ACTION，是 1980 年代商場裡的 8-bit 間諜動作遊戲。玩家要在六層、三個螢幕寬的橫向商場乘坐電梯／手扶梯、閃避和射擊間諜、進入俯視角商店搜尋六個包裹，最後抵達停車層逃走並進入更難的新 loop。單一 prompt 詳列 13 家 parody 店舖、10 種商店房間／9 種視覺主題、敵人與守衛、電梯與升降平台規則、搜尋互動、道具、分數、死亡／續關／Game Over、每店不同音樂、原創程式生成的精靈圖／字型／音樂／音效、CRT 後製、鍵盤／手把、固定 60Hz 模擬、確定性 seed、可除錯介面、CI、完整規則測試與真實瀏覽器 Playwright 實玩。它刻意同時壓「橫向動作＋俯視房間」兩套玩法和多個狀態系統的整合。

**目前可比較的最新公開分支：**

| 模型 | 作品／證據 | 研究時已核實 |
|---|---|---|
| Claude Opus 5.5 | [可玩版](https://rlorca.github.io/mall-action/opus-5.5/) · [source README](https://raw.githubusercontent.com/rlorca/mall-action/opus-5-5/README.md) | README 明列對應共同 one-shot prompt；13 店、6 層、兩種視角、源碼生成美術／音效、300+ 單元測試、頭less Chrome 截圖 playtest；有實際標題、商場、商店、SPYGRAM 截圖。這些是作者文件自述，沒有本輪重新執行整套測試。 |
| Claude Sonnet 5.5 | [可玩版](https://rlorca.github.io/mall-action/sonnet-5.5/) · [source README](https://raw.githubusercontent.com/rlorca/mall-action/sonnet-5-5/README.md) | README 明列相同 prompt；有商場／俯視商店／地圖／過關等實際圖，寫有固定 60Hz、原創合成音樂、測試與 build 指令。本輪未取得該 branch 的逐次 benchmark notes 和完整實際 QA 記錄。 |
| GPT-6.1 Sol | [可玩版](https://rlorca.github.io/mall-action/gpt-6.1-sol/) · [source README](https://raw.githubusercontent.com/rlorca/mall-action/gpt-6-1-sol/README.md) · [verification log](https://raw.githubusercontent.com/rlorca/mall-action/gpt-6-1-sol/verification.md) | 記為 9/29、Codex/API harness、一位 agent、約 50 分鐘；報告有 74 tests、23 項真實鍵盤／Playwright browser checks、零 console error、CRT 開啟並視覺檢查多個畫面。作者明確說其中一些 store／terminal state 使用 debug placement，並非人工不間斷完整跑六店；執行曾因 daemon restart 中斷，另有 branch 命名更正及 sandbox approvals，應列為介入／環境事件。 |
| Claude Fable 5.1 | root README 有 [branch 與 playable 入口](https://github.com/rlorca/mall-action#readme) | 同一題型及分支存在，但本輪沒有核對其 branch 專屬細節；待後續驗證。 |
| Claude Haiku 4.5、Gemini 3.6 Flash、Claude Opus 4.6、Opus 5、GPT-6 Sol | root README 有相應分支／部署連結 | 可拓寬能力跨度，也使題目不只比較最強前沿模型；仍需逐 branch 核對模型 ID、執行日期、版本及改動紀錄。 |

**對你要測的用途，我目前把它排在第一個建議親自重跑的固定題目。**理由是 prompt、每模型分支、可操作作品和至少一個新模型的詳盡 Playwright／單元測試記錄都齊，並且存在 GPT-6.1 Sol、Sonnet 5.5、Opus 5.5、Fable 5.1 等新模型產物。與 Backrooms 相比，MALL ACTION 不靠寫實 3D 畫面來呈現難度，而是透過長規格和多系統依賴測「能否把規格完整落地」；初次看圖會比 Backrooms 低調，但規格本身可以直接顯示工作量。若你主要想用實際畫面立刻辨認視覺上限，Backrooms 仍是更好的 showcase；若你要一份透明、可複製、跨多個新模型的長題目，我建議先用 MALL ACTION。兩者互補，不能互相代替。

**先不要把現有 branch 分數化排名：**共同 brief 和版本分支是強控制條件，但除了 GPT-6.1 Sol，其他分支的模型 ID／日期／effort／工具介入細節未完整交叉核實；GPT 的跑次也有 daemon 重啟和批准事件。不同 harness 可能改變結果。重跑時按 repo protocol 新增自己的獨立 run branch，保留原始 git 狀態、對話紀錄、用量／時間、每次介入、測試結果、browser 錄影和盲評；所有模型使用同一工具與權限時才能放在一組比較。建議另報「一次新鮮 session 完成」與「固定時間內驗收通過率」，不要只挑最漂亮的完成品。

#### 本輪補充查詢及去重紀錄

| 本輪查詢 | 查到／核實 | 後續避免重複 |
|---|---|---|
| `site:github.com/AgentsLoop/awesome-opus-5.5-games "Mall Action — Model Benchmark"`、`"Mall Action" "GPT-6.1 Sol" "Claude Sonnet 5.5" game benchmark` | 從 AgentsLoop 可玩作品索引發現同 repo 多模型 entry；該索引也明說列有 creator-reported / repo-level 等不同證據級別，不能只照 score 當實測排名。 | 探索入口已查；不要再用同一模型組合泛搜。只追 MALL ACTION 各 branch 的 benchmark notes、驗收附件或新模型更新。 |
| `https://github.com/rlorca/mall-action`、`one-shot-prompt.md`、`AGENTS.md` | 直接核對主 README、完整 prompt 和 benchmark protocol；確定同一 488 行 prompt、空資料夾/fresh session、每模型獨立 branch、agent 可自主迭代，以及 run 要記錄的項目。 | 核心題目與協定已核實，不重找其 benchmark 的成立與否；若主線 prompt 版本有 commit 更新才比較規格差異。 |
| `https://raw.githubusercontent.com/rlorca/mall-action/{opus-5-5,sonnet-5-5,gpt-6-1-sol}/README.md`、`.../gpt-6-1-sol/verification.md` | 核對 Opus/Sonnet/GPT-6.1 Sol 成品功能、部署、截圖／測試自述和 GPT run interventions。 | 已確認三個新模型 branch；Sonnet / Opus 詳細 run conditions 與 Fable branch 尚待核，避免重抓已讀 README。 |
| `https://raw.githubusercontent.com/rlorca/mall-action/{opus-5-5/docs/screenshots/mall.png,sonnet-5-5/docs/mall.png,gpt-6-1-sol/public/screenshots/mall.png}` | 直接逐張在瀏覽器開啟檢視三個模型 branch 的商場遊戲截圖；確認都能看到分層商場／店舖與電梯，但截圖時狀態、位置和尺寸不同。 | 三張原圖已並排加入 Mall Action 章節，供理解輸出外觀及任務範圍；只作實物展示，不能用這組不同狀態的截圖排序視覺品質。後續有新 branch 才查其對應截圖，不重找這三張。 |
| `site:github.com/rlorca/mall-action "Benchmark notes" "fable-5-1"`、`https://raw.githubusercontent.com/rlorca/mall-action/fable-5-1/README.md` | repo root 的模型表列 Fable 5.1 branch 和 playable URL，但此輪 GitHub/raw/live build 對該 branch 回應 cache miss；AgentsLoop 9/30 的索引仍只收 Opus 5.5、Sonnet 5.5、GPT-6.1 Sol 三個模型，索引不一定包含根 README 後加的 Fable。 | 把 Fable 記為 source root 列出的待查 branch，不視作已核實可玩的分支或一次 run；不要重試泛搜尋或重複相同 raw URL，待 GitHub/index 來源可載入或作者增補明確 evidence 再核實。 |

### 2026-10-04 新增高完成度作品展示：Night Courier（非一次生成基準）

[Night Courier 可玩頁](https://wavedash.com/games/night-courier)於 2026-10-02 發布，頁面記錄 10-03 更新；[AI Primer 對作者貼文的整理](https://www.ai-primer.com/creative/stories/sonnet-threejs-parcel-delivery-game)稱作品主要以 Claude Sonnet 製作，作者另說 Sonnet 5.5 以程式碼建立了遊戲中的 3D 模型。這是一個可以直接體驗的近期成果，不能把 Wavedash 現版自動等同於首個生成版本。

![Night Courier 封面圖：作品商場式霓虹雨夜城市與貓咪快遞員；這是 Wavedash 遊戲列表封面，並非遊戲內截圖](https://uploads.wavedash.com/cdn-cgi/image/dpr%3D1%2Cwidth%3D640%2Cheight%3D360%2Cfit%3Dcover%2Cbackground%3D%23FFFFFF%2Cformat%3Dwebp/jd7bqwamxfyj6j4b1zsfh5cq0h8d024h/j977xehe0w4f4ygaqw6nfwbxw98fh1hz/assets/wideCover-1790960467824-c2375492.webp)

**作品規模：**玩家騎速克達在六個區域構成的雨夜港市送包裹；城裡有電車、渡輪、人群、港邊高架道路、日夜與晴雨轉換。每次配送是一則短故事，宣傳頁稱有超過 100 則；包裹鏡頭即時顯示貨物，顛簸會造成損壞並影響小費。顧客還會邀玩家玩麻將配對、筷子抓蒼蠅、夾娃娃、卡拉 OK；送件收入用來升級車輛與外觀，另有 20 多名有聲音的角色。這些是遊戲 listing 的功能描述，尚非本輪獨立操作驗收。作者提到遊戲使用購買的音效素材，頁面也提示目前未最佳化且部分 shader 有故障，故「全部模型生成」或已達發行品質都不是已證實事實。

**評測定位：**高品質 playable showcase／長規格題材種子，值得拿來設計下一題「城市駕駛物理 + 配送任務狀態 + 貨物損壞 + 顧客 mini-games + 經濟升級」的跨模型測試。它不符合目前有證據的 strict one-shot 標準：沒有公開共同原始 prompt、空白環境、生成 transcript、首輪 build、不同模型對照或統一 rubric；作者說明 gameplay trailer 曾需要多次修訂，也只表示至少 trailer 不是一次不改便完成。把它標示為 Sonnet 5.5 的一-shot 成品會超出證據。

| 本輪查詢 | 查到／核實 | 後續避免重複 |
|---|---|---|
| `"rainy Hong Kong" "parcel game" Three.js AI`、`"Hong Kong parcel" game Three.js AI generated`、`"Night Courier" "Danny Limanseta" "Sonnet 5.5"` | 找到 AI Primer 10/02 作者案例整理及 Wavedash 原生作品頁。核對作品玩法描述、發布／更新日期、Sonnet 5.5 3D 模型歸因、購買音效資產、桌面限制、未最佳化／shader bug；直接開啟 Wavedash list cover，確認它是封面而非遊戲畫面。X 原帖在本輪無法讀取，精確 prompt 和完整原始測試條件未公開。 | 已新增為 Showcase / 題目種子，不進 one-shot 比較名單；不重跑同一標題搜尋或封面圖片查找。只有作者公開 transcript、固定 prompt、首輪 artifact 或其他模型同題 run 才重新升級證據。 |

### 鄰接題型線索：Vib3Coded 的互動式中世紀王國長 prompt

[Tripo 頁面](https://www.tripo3d.ai/3d-prompts/claude-opus-5-5-2103257687492374597)於 2026-09-24 收錄作者 Vib3Coded 的完整 Opus 5.5 prompt，並明確說它來自作者城堡比較中的 Opus 版本、內容取自 verified author comment。要求在單一 standalone HTML / Three.js/WebGL 中建置有辨識度的中世紀城堡與周邊地貌：主堡、塔樓、城牆、門樓、可運作吊橋／城門、庭院；旗幟／盾牌／王室紋章和命名；守衛巡邏、村民移動、煙、鳥、燈火；可切換總覽／庭院／城牆鏡頭、自由旋轉縮放、日落夜景、開關吊橋；要求人物待在可走地面、不穿牆、不互相穿透，並在 Chrome 逐一測試所有互動、截圖、看 console 與修渲染錯誤。這壓的是**程序化空間構成、角色移動、物件互動、鏡頭與視覺完成度整合**。

它是「互動 3D 世界生成」的高密度題目種子，不算完整遊戲：沒有玩家角色、敵我玩法、明確任務循環或勝負狀態。本輪沒有找到原作者可玩檔／獨立模型 build、模型間一致的執行紀錄或評分，因此不列進上限遊戲成果比較。頁面所述其出自 castle comparison 和本次找到的 Reddit 摘要，尚不足以認定是三次模型平行同 prompt 的受控比較；不要把 Sonnet 免費版／Team 版耗時差異或作者的主觀圖像偏好當模型成績。

| 本輪查詢 | 查到／核實 | 後續避免重複 |
|---|---|---|
| `site:reddit.com/r/ClaudeAI "interactive 3D medieval castle" "Sonnet"`、`"Build your own medieval kingdom" Claude Sonnet 5.5 Reddit`、`Tripo interactive medieval kingdom Claude Opus 5.5 prompt` | 找到 Tripo 收錄的完整作者提示與 9/24 日期；規格要求單檔世界建置、守衛／村民移動、吊橋互動、鏡頭／日夜切換和 Chrome 實測。原始 X/Reddit 比較貼文未確認，且沒有可玩 build。 | 保留為 interactive-3D task seed，與完整遊戲 benchmark 分開；不重做 castle/medieval prompt 泛搜，除非能追到原作者 build、測試及同題模型 run。 |

### 2026-10-04 新增：Strict first-output 新模型遊戲庫與可重用測試架構

#### WorldBuild Bench：可借用的統一 harness，不是最新模型成績

[WorldBuild Bench](https://github.com/sebnado/worldbuild-bench)提供 3 個同規格 browser 3D 小遊戲題：arena melee waves、物理彈珠解謎、多圈賽車。其價值不在當前 roster（2026-07 pilot，主要是 Claude 5 系、GPT-5.x、GLM-5.2、Grok 4.5、Kimi K3；未見本輪前沿型號），而是提供了一套可複製的「相同模型執行環境」：同 system prompt、Three.js + Rapier scaffold、tools/skills、Playwright 實玩 loop、相同 budget gate，直接 API adapter、不走各家 coding CLI；同一任務能產出多份 browser-playable build。每次有 transcript、結果、截圖和 resume state，並支援添加 provider model。

它同時指出幾個評測陷阱：機器測試全 pass 不代表遊戲好玩，gate 可通過但玩家仍會遇到不可解謎題、圈數不計、操控失靈；因此分開報告 objective gates 與看不到模型名稱的 pairwise 人類實玩偏好。它的 3 題規格比 MALL ACTION 或 Backrooms 小很多，適合做**成本較低的校準副測**；高品質之處是 harness 方法，不是「最新模型上限」資料。這個方法正好補足目前案例共通的 harness 不同：正式比較可用相同 API agent loop，然後另開一組各家原生 coding agent 的「產品體驗」賽道，不要混著解讀。

#### 本輪廣泛搜尋與去重紀錄

| 查詢 | 實際發現 | 後續去重界線 |
|---|---|---|
| `"one prompt, one shot, every model" game benchmark github`、`GitHub "one-shot prompt" game "model" "playable" benchmark Claude Opus GPT` | 發現 MALL ACTION：長、固定、逐字共享 GDD 的 agentic one-task benchmark；與前項「first-output」定義不同，兩種都值得分開測。 | 不重跑此類泛搜；對新案例以 exact prompt、目前模型、原始 artifact、逐次條件為篩選條件。 |

| `WorldBuild Bench same brief same tools 8 models 24 playable builds`、`site:github.com/sebnado/worldbuild-bench` | 核對 harness、三個題目、2026-07 10 模型 pilot、遊戲 playable gallery、客觀 gate + blind pairwise 人評方法與環境一致性。repo header 的 24 playable 與 README 內 27 builds 文案有不一致；不引用單一總量作重要主張。 | 已查該 harness 方法與舊 roster；不當最新模型結果重查，只有新 round/模型加入後才回查。 |

### 2026-10-04 新增高難度題目種子：Crazy Tanks — Wild Tides

[Tripo / GPT-6 Astra prompt 頁](https://www.tripo3d.ai/3d-prompts/crazy-tanks-3d-island-artillery)標示作者 jared、日期 2026-09-24，附逐段完整規格及 3D 資產圖庫。頁面明確揭露這份 prompt 是「根據 jared 原始 Crazy Tanks 原始碼、commit `bf23b8878a1c24dbfb105a227a06b4faa29d42e9` 與已驗證 v92 gameplay 重建的規格」；模型資產由 Tripo P2 生成、音樂／音效由 ElevenLabs 製作，沒有提供已發表的原始社群貼文。因此它不是 GPT-6 Astra 當時第一輪原始輸入的可核實逐字紀錄，不能拿來當一次生成成績或模型競賽；目前也未從該頁確認一個可直接操作的遊戲 build 或模型間對照。

儘管如此，這份**重建後規格很適合作為統一重跑題**，也比一般 3D 場景或單關平台跳躍更能壓整合上限：回合制三坦克大逃殺／雙坦克決鬥、玩家對 AI 與本機 pass-and-play；自由軌道鏡頭與 3D 可變形島嶼；持續風向下的瞄準、拋物線預測和每次歸零的蓄力射擊；六種武器（普通、集束、地震、反彈、單發災變、燃燒）；地形挖坑／塌陷、火區與水面淘汰；補給、護甲、AI 回合與可快轉但物理一致的模擬；固定 1/120 秒步進、掃掠碰撞、畫面頻率獨立、觸控／鍵盤、四語介面和桌機／手機版面。題目還要求完整勝負流程、重播暫停、外觀切換不重置狀態，以及大量物理與可用性驗收。它涵蓋規則正確性、數值模擬、相機／UI、AI、可變形 3D 場景與測試閉環，若將外部 3D 資產／音效生成流程當作預先給定資源或統一禁用，將是目前值得優先加入「嚴格單一長 prompt、單次交付」賽道的候選題。

**畫面參考（原遊戲參考圖，不是 Astra 跑次的獨立成果證據）：**Tripo 頁另附 [v92 gameplay 參考影片](https://cms-media-proxy.tripo.page/media/1e2c8871-c416-4f0d-9e03-511d5db6bd66.mp4)與原遊戲畫面。以下 1440×900 截圖可看出視角、介面與美術目標；媒體頁未提供可比的模型版本標籤或同場景盲測截圖。

![Crazy Tanks 原遊戲參考畫面，取自 Tripo prompt 頁引用的 v92 gameplay 素材；不是 GPT-6 Astra 產出版本](https://media.tripogrowth.space/media/9382591d-398a-491f-a330-b0ac93edae77.png)

**建議實際重跑時先固定範圍：**所有模型使用同一份重建規格、相同起始專案與素材條件、空白新工作目錄與同等時間／工具額度；先要求全部核心玩法以程序化幾何和音效完成，不讓任何模型需等待人工外部資產上傳；不追加對話修補。把「一次」界定為單一 user task/session，容許 agent 在自己工作區建置和自測，但逐字保存 transcript、耗時、工具呼叫、重啟與人工介入；若要測純首稿，再另設無迭代 first-output 賽道。評分至少要拆成可啟動／可玩、六武器與回合勝負、地形與水火邏輯、跨幀率物理穩定、AI 對手、鏡頭/UI、觸控、視覺、無障礙／語系及盲測好玩度，避免漂亮封面掩蓋不可玩的系統。外部模型生成資產版本可做第二輪，但必須各模型配同一生成工具與配額，並單獨記錄來源。

#### 本輪查詢與去重紀錄

| 查詢 | 實際發現 | 後續避免重複 |
|---|---|---|
| `"Crazy Tanks — 3D Island Artillery" GPT-6 Astra game prompt`、`"3D Island Artillery" "Wild Tides" GPT-6 Astra`、`"Crazy Tanks" "Wild Tides" playable GPT-6 Astra AI game`、原始碼 commit SHA 精確搜尋 | 找到 Tripo/Astra prompt 頁與其完整重建規格。頁面自述根據既有原始碼與 v92 gameplay，而非原始一次生成 prompt；列出高複雜玩法／技術驗收、外部資產來源與參考素材，但未核實到作者原帖、跨模型對照或可玩成品。 | 收錄為「統一重跑題目種子」，不收錄為既有 one-shot 結果。不要重做標題／SHA 泛搜；只有找到作者原始 prompt、可玩 build/commit、可讀 transcript 或新模型同規格跑次時再回查，並保留規格是否仍綁定 Tripo 的核對。 | 

### 2026-10-04 新增：Slapjam AI 遊戲徵件中的策略／基地管理案例

[Slapjam AI #1 官方徵件頁](https://itch.io/jam/slapjam-ai-1)列出 145 個作品，徵件時間為 2026-09-28 至 09-30；所有作品須以手機直向畫面在 HTML5 瀏覽器執行，主題為城堡。評審玩過所有投稿後依「好玩度、視覺吸引力、主題符合度」打分，七天評審在 10 月 7 日才公布結果；截至本研究更新時間尚無結果。這是近期可查的大型 AI 遊戲成品圖庫與可借的人工評審流程，但規則允許人類團隊、任意模型、AI 素材工具和 48 小時反覆製作，故徵件分數不能解讀成模型能力排名，也沒有控制同一任務／同一模型呼叫數。

![Tiny Necromancer 頁面的遊戲題名圖，右側可見多層塔樓與骨骸工作者的遊戲畫面；此為作者頁面圖片，不代表單一模型基準輸出](https://img.itch.zone/aW1nLzMwMzg4NDUzLnBuZw==/original/C%2B03aP.png)

#### 最值得採作新長題型參考的兩款作品

| 案例 | 原頁可核實的機制與模型歸屬 | 一次生成證據／研究用途 |
|---|---|---|
| [Tiny Necromancer](https://dylanh.itch.io/tiny-necromancer) | 8–10 分鐘直向塔防／管理遊戲；玩家擊敗敵人、選擇復活骨骸或收集資源，再把不同職業骷髏安排到房間；房間有兩種工作指令；16 種房間塞進 8 個樓層格位，玩家每波之間選建築、堆疊、升級或出售；塔樓受損需抽調工人修補；第三波選大型防禦改建，最終迎戰三階段 Boss。每種敵人保留自身特徵，房間組合造成長程決策。人類使用 Codex GPT-6 Astra medium 與 Claude Code Opus 5.5 medium 共同開發；程序化美術與聲音、無外部素材；Godot 4.7.1，HTML5/桌面版，頁面提供 10MB source zip。 | 無共同 prompt、對話紀錄或模型分工細節；雙模型參與，無法把整體品質歸給任一模型。很適合作為「短篇完整遊戲裡，多系統策略管理如何驗收」題目種子，與 Crazy Tanks 的物理核心互補。作者頁可玩遊戲與 source download 有效；展示圖是含遊戲實景的標題圖。 |
| [Bastion / BASTIÓN MECHA](https://lambdaforge.itch.io/bastion) | 約 10 分鐘等角生存策略動作遊戲。機甲可切換為城堡；機甲探索、戰鬥和踩踏敵人，城堡在金脈／資源沼澤開採並派村民採集；建造精煉廠、機庫、兵工廠、城牆，升級會改變機甲與城堡外觀；環境坑洞擴張、資源枯竭、敵人變強；完成升天引擎後再撐過 60 秒母體爬蟲攻城。另有自動砲、雷射、震地攻擊、衝刺、英西文、直向觸控。itch 作者聲明 Opus 5.5/Claude Code 負責單檔 HTML Canvas 遊戲程式、程序化視覺／音效、平衡與 autoplay bot 測試，Suno 作音樂；人類負責遊戲設計、藝術方向、概念圖、HUD 圖與音樂方向。 | 有 playable build、完整遊戲規則敘述與 autoplay bot 資訊，沒有原始 prompt、model session、耗時／成本或 bot 覆蓋報告。這是目前本輪新增案例中比較清楚地把完整遊戲程式歸給單一較新模型的 high-complexity showcase，但無法稱作「一次生成」。適合重跑成 fixed prompt，並以「雙型態狀態一致、資源循環、建造依賴、波次存活、Boss 勝利條件」作自動驗收。 |

**同主題其他有用參照：**[Castle War](https://yanfroes.itch.io/castle-war) 是 Opus 5.5 寫程式／敵人 AI／關卡碰撞資料的 10 分鐘城堡攻堅、四職業行動戰鬥；素材有人類 LPC 角色、ChatGPT 圖像生成城堡圖、程式生成特效聲音。人類導演／設計／實玩，沒有原始 prompt。 [Castle Courier](https://cfrog25.itch.io/castle-courier) 是 Opus 5.5/Three.js 的七城堡 3D 飛行送信、戰爭／龍襲／暴風／節慶狀態遊戲，頁面明言封面和截圖皆為遊戲畫面、作品仍屬 prototype；沒有 prompt／build log。 [Siege Labyrinth](https://miuni.itch.io/siege-labyrinth) 用傾斜／手機陀螺儀讓炸彈滾過 3D 城堡迷宮、火線倒數、陷阱、水、守衛／火炬／機關門與三星計時；Opus 5.5 寫 Godot 遊戲、測試 bots、build scripts 和 level editor，但 2D/3D 資產另用多種生成器再經 Blender 處理，人類負責玩法設計與 playtest。這些作品擴充題型資料，但皆未公開一次提示與對稱模型比較。

![Bastion 遊戲內直向畫面：資源採集、基地／機甲狀態與 HUD；來源為 itch 作者遊戲頁的短 GIF](https://img.itch.zone/aW1nLzMwNDAwOTQ4LmdpZg==/original/W3rKuS.gif)

#### 其他新發現與排除邊界

- [Chainmate](https://sneid1.itch.io/chainmate) 是 6×6 棋盤三幕 roguelite；公開作者說第一則提示是四張自製 ChatGPT art-direction 圖加文字「build this game」，但後來仍有短訊息調整光照，因此並非真正一 prompt 終稿。每局九戰、分支地圖、商人／休息／事件、永久死亡、每棋子升級、最多六種 relic、三個有專屬規則的 Boss、保存與棋類 AI。原作者稱 Opus 5.5 + Claude Code 產生遊戲程式、3D 模型、音樂、音效、測試和 builds；瀏覽器 playable、Windows 可下載。這是近期很強的 3D 棋類 roguelite 視覺／內容例，但作者承認後續提供了幾次光線回饋、遊戲仍待真實玩家平衡，且無 prompt transcript、repo／評分，不列 one-shot 成績。
- [Outrun 2026](https://mlouvet.itch.io/outrun-2026) 是 Opus 5.5/Claude Code 將 Master System 版《Out Run》移植到 Amstrad CPC 6128，含 15 賽段、分岔路、交通碰撞、三檔難度、手排／自排及重寫 Z80 引擎。人類明確比對舊遊戲曲線、音樂、車輛操控，並逐 build 在 emulator 與實機測試、回報錯誤；不是 one-shot，但可作「嚴格舊硬體限制＋行為相似度」能力展示。公開下載截至 10/03 是 v0.8.1，頁面仍在持續更新。
- [Outpace](https://github.com/ethanplusai/outpace) 是 10/01 的 Opus 5.5 單 session、約 45 分鐘、逐項公開 BUILD_LOG、47 tests 和 bots 平衡的 typing runner；但實際人類插手了四次中途方向修正、使用 2 個 Sonnet 5.5 subagents，機制也較簡單，分類為 QA／全產品流程方法範例，不當上限遊戲比較。逐字原始 brief 和可玩頁在 repo 中都公開。

#### 本輪搜尋與去重紀錄

| 查詢 | 查到／核實 | 後續避免重複 |
|---|---|---|
| `site:itch.io "Claude Opus 5.5" AI generated game 2026`、`site:itch.io "one prompt" "Opus 5.5" game Godot`、`site:itch.io "GPT-6 Astra" strategy game AI castle 2026`、`"Slapjam AI #1" "Claude Opus 5.5" one prompt game`、`site:reddit.com/r/ClaudeAI "Opus 5.5" "game" "prompt" game dev October 2026 demo` | 發現 Slapjam AI #1 的 145 件 AI 城堡遊戲、正式「好玩／視覺／主題」評審規則和 10/07 結果日期；核查 Tiny Necromancer、Bastion、Castle War、Castle Courier、Siege Labyrinth 等新 playable entries 的模型歸屬及人類參與。 | 已將該 jam 作為策略遊戲探索入口；不需重跑同一 itch/jam/標題搜尋。僅在 10/07 賽果公布後回查獎項／評分，或新作品公開原 prompt、session/build log、單一模型 run 時重開相應案例。 |
| `"I gave Opus 5.5 four reference images and build this game" chess roguelite`、`"Outrun 2026" "Claude Opus 5.5" Amstrad CPC`、`"typing game end to end" "Opus 5.5" open source free` | 核查 Chainmate 是四張方向圖＋一句任務後另有光照回饋；Outrun 是人類跨版本測試修訂的古機移植；Outpace 原始 prompt/repo/build log公開，但人類中途四次改方向、兩個子代理，遊戲本體為打字跑酷。 | 分別歸類為 roguelite reference、硬體移植 showcase、QA/全產品 pipeline 案例；不重搜標題，只在模型新增 run 或逐字歷史證據新公開時更新。 |
| `Slapjam AI #1 itch.io entries judging rules 2026`、`site:slapjam.ai 2026 AI game jam judging`、`site:itch.io/jam/slapjam-ai Tiny Necromancer` | 官方頁列 145 submissions、手機直向 HTML5、主題 castle、評 fun/visual/theme；評審到 10/07 才結束，當前尚無正式排名。 | 評分完成後回查一次；jam 不是控制模型／prompt／迭代數的 benchmark，未來不得引用其排名作模型排名。 |












### 2026-10-04 新增：AI Browser Game Jam 4 評分庫與近期徵件追蹤

這輪把搜尋範圍轉到近期公開 AI game jam 的可玩成果、作者工具揭露和人工評分，目的是補足「真實可玩的完整遊戲」及可借用的評測方法；不把自由創作競賽的名次誤當模型 head-to-head benchmark。

#### AI Browser Game Jam 4：有成品、有公開評分，但不能比較模型

[官方結果頁](https://itch.io/jam/ai-jam-4/results)列 125 件投稿、1,034 個評分、124 件被評（99.2%）；每款平均 8.3、中央値 7 個評分。評分維度為 Overall、Fun、Graphics、Audio、Theme、AI Usage。官方頁面與 #5 徵件頁存在 125 / 126 件投稿的數字落差：#4 結果頁寫 125 entries submitted，而 #5 主辦頁回顧 #4 有 126 entries；本文件保留兩種來源數字，不自行裁定是哪個口徑或更新造成差異。

| 公開成品 | 規模與作者披露 | jam 結果／本研究用途 |
|---|---|---|
| [Plug & Prosper](https://smallloopworks.itch.io/plug-prosper) | HTML5 物理線材解謎兼商店管理：拖曳插頭、插座和可重用轉接頭；五個手工關卡後另有持續經營 kiosk 模式、訂單倒數、升級、顧客耐心、重力變化與本機存檔。頁面顯示 10/03 更新至 1.4.1，仍在開發。作者揭露 Codex CLI harness、GPT-5.6 Sol（low–xhigh）主力 LLM，並使用 Lyria、GPT Image 2；由持續開發紀錄可知是反覆修訂，不是一次生成。 | jam Overall #1（10 人評）、Audio/Theme/Graphics/AI Usage 各 #1，Fun #11（3.6/5）；這個落差很適合提醒評測要分項。以可玩、近期更新、系統組合和明確工具揭露列為完整遊戲參照；模型比對因模型版本舊、人工疊代且缺原始 session 而排除。 |
| [AI2U – Guns & Girlfriends](https://helixngc7293.itch.io/gandg) | 3D 瀏覽器 RTS：三陣營、資源採集、基地建築、坦克與核武倒數；五張地圖、三種難度／AI 性格、兵種克制、單位 wiki 和即時數值。作者披露 Fable 5 + Opus 5 寫程式，Suno 音樂、Nano Banana 角色圖，程序幾何建模；是混合模型與工具的完整作品。 | jam Overall #2（15 人評），但 Fun #8、Theme #64；評論提到教學難懂、節奏偏快，作者回覆總投入約 72 小時並描述 gauntlet-loop prompting。作為高複雜度 RTS 成品參照很有用，不能當 one-shot，亦無法拆分 Fable/Opus 貢獻。 |
| [TECHNICAL DEBT](https://itch.io/jam/ai-jam-4/rate/4864314) | 家庭資源管理／敘事模擬：處理家人需求、雜貨配送與儲存、現金／信用、關係與多種結局。AI Code 披露稱 Codex 在人類指導下負責設計、程式、測試、平衡模擬和內容；美術、音樂音效亦使用其他工具。 | jam Overall #3（11 人評）但 Fun #52，顯示總體印象、趣味性和製作／AI 使用可能分歧。適合作為多系統與評分維度參照，非單模型或單次輸出。 |
| [Overcharged Demo](https://durian-arcade.itch.io/overcharged-demo) | 太空射擊／採礦／升級循環，投稿用 Fable 5，已有可玩 demo。 | jam Overall #10（10 人評）；比前三者系統較簡單，放次級候選，不升為上限主題。 |

社群評分樣本量多數只有 7–15 人，各項目允許不同模型、素材來源、團隊和人類投入。故可用來找成品、觀看可玩流程、找出趣味與完成度的差異；不可拿 jam 排名作模型排名。個別投稿的版本更新也可能晚於評分期。

#### 近期可追的三場 jam

| 活動 | 官方頁核對到的狀態 | 對 one-shot 研究的價值與限制 | 下次檢查時機 |
|---|---|---|---|
| [AI Browser Game Jam 5](https://itch.io/jam/ai-jam-5) | 10/17–10/31 投稿；無限制模型，必須免費且可在瀏覽器玩，作品大部分須由 AI 生成，但人類編輯／精修是允許且預期的；六個社群投票維度同 #4。頁面當時顯示 71 人加入。 | 最大價值是可以捕捉最新模型與真實可玩成品；規則明確容許人類精修，故只能當 showcase／人工評審語料。應優先檢查投稿文字有沒有模型精確版本、prompt、製作耗時、commit/build 證據。 | 投稿關閉 10/31 後先整理新作品；評分完成再記錄結果，之後不需反覆檢查徵件頁。 |
| [Jamference: AI Game Jam Hack 1](https://itch.io/jam/jamference-ai-game-jam-hack-1) | 10/02–10/09 投稿；共同主題 Cat and Robot，硬性限制是所有輸入只能控制角色移動；頁面當時 66 人加入。官方明講成品可以是一個 prompt，也可以是一週工作；三項同權重：Fun、AI use、Polish。 | 很好的「固定創意約束」來源，可以借 movement-only 做成相同長 prompt 的統一生成任務，要求模型設計出完整玩法、關卡、失敗／勝利、教學和可測流程；但 jam 本身容許一週迭代，不是 one-shot 實測。 | 10/09 投稿截止後查 build、模型揭露和 prompt；優先找有公開完整初始 prompt / 歷程的作品。 |
| [Ultimate AI-Powered Game Jam #5](https://itch.io/jam/ultimate-ai-powered-game-jam-5) | 10/09–10/12，72 小時；主題 Pumpkin，第二個隱藏題目在開賽時公布。規則允許事先準備 prompt pipeline、基礎素材和 boilerplate，最後整合／打磨要在 jam 期間完成。 | 適合找快速交付、模型指揮與適應新限制的案例。預先準備和 72 小時流程都不等於一次生成；活動分數只能當社群評審結果。 | 10/12 後先收 build 和 AI 揭露，10/15 評分結束後再收結果。 |

#### 本輪搜尋台帳與去重規則

| 本輪實際查詢 | 新核實結果 | 下次避免重複的規則 |
|---|---|---|
| `site:itch.io/jam/ "AI game jam" "October" 2026 entries GPT-6 playable`；`site:itch.io/jam/ "AI Browser Game Jam 4" results model game 2026`；`site:itch.io/jam/ "AI game jam" "Opus 5.5" "GPT-6 Astra" game September 2026`；`"GPT-6.1 Sol" "AI game jam" game October 2026 playable` | 找到 AI Browser Game Jam 4 結果頁、評分統計、近期投稿作品與 model disclosure；jam #4 主要是非控制式社群樣本。 | #4 的基本賽果、統計和上述四個案例已查；不重搜同樣的標題／jam query。只有作者補上原始 prompt/session、同題新模型 run，或有重要新版改變可玩性時回查。 |
| `site:itch.io/jam/ai-jam-5 "2026" AI Browser Game Jam 5 Focaccai October`；`AI Browser Game Jam 5 Oct 16 to 30 2026 official Focaccai itch.io`；`site:itch.io "AI Browser Game Jam 5" "October" "2026"` | 官方時程確認 10/17–10/31；瀏覽器可玩、AI 主導但人類精修允許；主辦對 #4 的投稿數記 126，與 #4 賽果頁 125 有一筆落差。 | #5 徵件規則與日期已核實。直接等 10/31 後抓投稿；除非日期／規則更改，不再搜 #5 宣傳頁。 |
| `site:itch.io/jam/ "AI Browser Game Jam 4" results model game 2026`；開啟 `https://itch.io/jam/ai-jam-4/results`、`/rate/4852654`、`/rate/4867618`、`/rate/4864314` 與作品頁 | 查 Plug & Prosper、AI2U – Guns & Girlfriends、TECHNICAL DEBT、Overcharged Demo 的規則、可玩頁、作者 AI 披露與分項名次。 | 不重開已記錄頁找同一欄位；新核查限作者發新 build、新披露或賽果頁更正。成績口徑以 jam 官方結果頁為準，作者頁用來核對玩法和製作資訊。 |
| `site:itch.io "AI Browser Game Jam 5" "October" "2026"`；開啟 `https://itch.io/jam/jamference-ai-game-jam-hack-1`、`https://itch.io/jam/ultimate-ai-powered-game-jam-5` | 發現 Jamference 一週／Cat+Robot／movement-only，明確接受單 prompt 到全週迭代；Ultimate #5 為 Pumpkin+hidden theme 的 72 小時活動且允許預備 prompt pipeline。 | 兩活動的規則、日期已記。僅於 10/09、10/12 等截止後查投稿與可玩成果，不重搜簡介。 |

**後續取樣建議：**先用 AI Browser Game Jam 4 補「成品實例與趣味性 rubric」，再把 Jamference 的 *Cat and Robot + movement input only* 轉為完全固定、一次生成的高要求題目——提示一次後禁止補充、修改或重試；要求一個可直接執行的遊戲成品。評分分開看：核心玩法能否在移動限制下成立、操作／碰撞可靠度、關卡與難度曲線、回饋和視覺可讀性、教學與勝敗閉環、是否能從初次啟動無人協助玩完。活動原生三分項可以參考，但模型評測要另外固定硬性自動驗收與匿名玩家評分。

### 2026-10-04 新增：GameASG-Bench 與《Armor Alley》長規格任務

#### GameASG-Bench：目前最有用的新「一次任務自主完成」正式基準

[論文（2026-09-18）](https://arxiv.org/abs/2609.21293)與[公開 GitHub 基準](https://github.com/areal-project/GameASG-Bench)共同定義 47 個 browser-native 遊戲生成任務，涵蓋 12 種主類型（32 個 2D、15 個 3D）。每題須生成自足的 `index.html`。題包包含 `target.md` 初始任務、`game-spec.md` 玩家可見規格、`tdd.md` 行為介面；公開測試程式和評估器與生成容器隔離。L1 檢查產物結構／來源要求，L2 由 headless Chromium 執行玩家輸入並比對遊戲狀態與 runtime 證據；任務題皆有獨立驗證的參考實作。每次用乾淨 session，預設一次生成嘗試、最長 3,600 秒，Claude Code 上限 120 turns；工具能讀寫檔案、跑程式、瀏覽器測試並自行修正。這是「一則初始委託後 agent 自主做完」而非 strict first-output（零修正）的規格。

論文以九種 agent stacks 在同一 47 題任務集比較；最大 reasoning effort 下 GPT-6 Astra / Codex CLI 26/47 題嚴格通過（55.3%）、Claude Opus 5 / Claude Code 24/47（51.1%）、GPT-5.6 Sol / Codex CLI 21/47（44.7%）。注意模型確切 roster 有 GPT-6 Astra 和 Opus 5，沒有 Opus 5.5、Sonnet 5.5 或 GPT-6.1 Sol；這是 9/18 論文 run 的結果，不可稱作目前所有最新模型排名。論文一處關鍵發現是 GPT-6 Astra 平均 L2 check pass 93.2%，但只有 55.3% 任務通過所有硬性必要項目；模型實作的平均互動表現和整題完整度必須分開報。其任務樣本每個模型／設定／題目只跑一次，未提供重複 run 方差。這些數據可當基準方法和舊版本比較基線；應使用其開源題包，另跑最新模型至少 3 次，分開公布第一次結果、平均／範圍、harness、effort、token、成本與失敗。

#### 值得抽出來做高難度題的官方任務：《Armor Alley》

基準中的 [Armor Alley `game-spec.md`](https://raw.githubusercontent.com/areal-project/GameASG-Bench/main/task/armor-alley/game-spec.md)已逐項指定一個橫向 2D RTS：玩家自己操控直升機偵察、開火、投彈、發射追蹤飛彈、空降士兵；同時花錢排隊生產坦克、導彈車、補給車，地面部隊自動前進交戰、擋路、護送或被消滅；士兵可佔領碉堡，工程師能修炮塔／地堡；玩家需要降落補給、管燃油／彈藥／人數、照看前線雷達和補給車。友軍補給車抵達敵基地獲勝，敵方補給車抵達我方基地則失敗，並要求選單、教程、暫停／重開、完整結局流程。這不只是視覺拼裝，也同時壓即時模擬、資源經濟、AI 對手、控制感、UI 狀態同步與勝負閉環。

**我的建議：**若希望題目難到明顯超過單一小遊戲、又能用瀏覽器和固定行為測試比較，優先從 Armor Alley 取樣做「海報式長 prompt + 10–15 個硬性可觀察測試」；取其中無後端、可在 3 分鐘內觸發的必要玩法，保持核心 RTS 不被 UI 或外觀稀釋。也可另比較 [Grand Theft Astro 的 3D 開放城區規格](https://raw.githubusercontent.com/areal-project/GameASG-Bench/main/task/grand-theft-astro/game-spec.md)，它要求徒步、射擊、NPC/警察/wanted、載具進出、商店、資源、任務鏈、死亡復活及 true-3D 城市，但官方將商店、較長任務鏈和手機支援列為可簡化深度，容易被模型做出表面豐富但核心閉環空洞的版本；需用硬性互動驗收避免只評截圖。

**2026-10-04 依使用者澄清重新分級：**多模型既有對照不是必要門檻。Armor Alley 應列為強重跑候選：GameASG-Bench repo 明確允許 agent 在單一初始任務後使用工具生成，預設一個 generation attempt、1 小時上限，再由隔離的 L1/L2 瀏覽器行為測試驗收；遊戲核心同時要求直升機控制與戰鬥、燃料／補給、生產佇列、地面部隊、雷達資訊、兩方補給車勝敗閉環。新找到的 [原作 DOSBox 實際畫面](https://www.schillmania.com/image/content/entries/2013/armor-alley-dosbox-2.png)只作玩法視覺參考，不是 AI 生成 build。此前短名單沒納入，是我把「近期 AI 成品圖廊／最新實測」當成過強篩選；正確限制應寫成視覺實證不足，而非任務上限不足。已回改檢閱 HTML，獨立標示原作畫面與 AI build 證據差異。

**對使用者目標的定位：**GameASG-Bench 是目前找到最有操作性的再跑框架：官方固定提示、目前仍新近的 GPT-6 Astra 基線、可見逐題規格、可執行隱藏檢查、錯誤細項、耗時／token／成本記錄。適合比「一次委託讓 agent 產出一個完整可玩 build」；若你指的是模型一次 completion 就交 HTML、連 agent 自己試跑／修正都不准，則必須另設 strict first-output 組別，不應跟此分數混表。它也不會直接提供每個模型生成結果的影片／截圖 gallery；paper/repo 提供的是題目、方法、reference implementation 與彙總分數，做自己的新跑次時要額外保留 screenshots/recorded input videos，補你想看的實物證據。

#### 新近錯誤標籤的一次提示線索：《MACH RUN》

[作者 Reddit 原帖與影片／圖片](https://www.reddit.com/r/aigamedev/comments/1wvysqb/mach_run_built_by_opus_55_in_essentially_one/)和[可玩 itch.io build](https://jebkj21.itch.io/mach-run)顯示一個很好的飛行物理題材：半擬真噴射機操縱、程序生成持續變化的山谷、低空穿橋／環、移動航空母艦著陸補給、爬高觸發敵機／飛彈、誘餌彈、火炮、分數倍數、每日相同地圖、全球排行，並支援鍵盤、搖桿、自訂軸、滑鼠、觸控／陀螺儀。作者明確更正標題可能誤導：Opus 5.5 一次提示只做出視覺、山谷和飛行動力學／基礎系統，現在可玩的遊戲經過數週打磨；目前 build 還在持續更新，不能當成整款遊戲一次生成。它仍值得借出「飛機物理＋世界生成＋飛行挑戰」的高難度副題，但不要算一次生成案例，也不要將現在的版本回推成原始輸出。

#### 本輪搜尋／去重台帳

| 搜尋字串或精確頁面 | 得到的證據 | 下次如何避免重複 |
|---|---|---|
| `"one prompt" game "GPT-6.1" playable game 2026`；`"one prompt" "Sonnet 5.5" game playable 2026`；`"one prompt" "Opus 5.5" complete game playable 2026 benchmark`；`AI game generation benchmark 2026 full game model evaluation interactive game benchmark` | 新找到 9/18 的 GameASG-Bench 論文與 9/26 的 DuelLab GameBench 2；多筆近期 Opus/Sonnet 案例仍須逐一確認「造遊戲」還是「用程式玩現有遊戲」。 | 下一輪用新模型精確版本＋日期過濾，已核實的兩個 benchmark 只追 model roster / 新 release，不重搜標題或摘要。 |
| 開啟 `https://arxiv.org/abs/2609.21293`、`https://arxiv.org/pdf/2609.21293`、`https://github.com/areal-project/GameASG-Bench`、`category/results.md`、`task/armor-alley/game-spec.md`、`task/grand-theft-astro/game-spec.md` | 核對 47 題、遊戲規格／TDD／測試和 reference 流程；單一工作委託可迭代；有 GPT-6 Astra 舊一輪可重現的結果。Armor Alley 與 Grand Theft Astro 可抽作更難的跨系統題。 | GameASG 基本規格、GPT-6 Astra/Opus 5 結果、Armor Alley 詳規均已列；日後只有出現 5.5 / 6.1 等更新同題 run、新版本題包或實際 sample artifact 才重查。不要把其舊結果冒充最新模型現況。 |
| `"GPT-6.1 Sol" "game" "one prompt" 2026 October`；`"Claude Sonnet 5.5" "one prompt" game 2026`；`"Claude Opus 5.5" game "one prompt" playable October 2026`；`site:reddit.com/r/ClaudeCode "Sonnet 5.5" game "one prompt" after:2026-09-30`；`site:reddit.com/r/ClaudeAI "Opus 5.5" game "one prompt" after:2026-09-30 playable`；`site:reddit.com/r/ChatGPT "GPT-6.1 Sol" game "one prompt" playable 2026 October`；`"GPT-6 Astra" "one prompt" game playable October 2026` | 本輪未找到高複雜、最新版本且能同時核對逐字 prompt、真實成品、單次條件的新增嚴格跑次；新找到的 Hill Climb 已在舊台帳、Roblox Kart 缺公開 build/run log、部分作品只出現在社群索引。 | 這組最新模型＋一次提示的查詢已查過；不得再泛搜相同字串。新候選要等原作者公布 playable/source、精確 prompt 或一次 run transcript 再核對。 |
| 開啟 [MACH RUN Reddit 原帖](https://www.reddit.com/r/aigamedev/comments/1wvysqb/mach_run_built_by_opus_55_in_essentially_one/) 和 [itch.io build](https://jebkj21.itch.io/mach-run) | 作者自述 Opus 5.5 僅一提示建了圖像、山谷與飛行動力學，完整遊戲後續打磨兩週；10/02 版 itch 持續更新。 | 已有作者對 one-shot 範圍的明確更正，不需因标题再重查。只在出現原始第一版、prompt、commit／screen recording 時比較基礎跑次和後版。 |
| 搜尋 `GameASG-Bench` 同時命中 [DuelLab GameBench 2](https://benchmarks.duellab.org/)；檢視其 leaderboard、methodology、GameASG paper references | DuelLab 的模型先寫「玩家程式」再與其他程式對弈，分數來自比賽勝負；不生成新遊戲。LMGame-Bench／GameQA 類也主要測模型玩遊戲或找 bug。 | 這些屬遊戲代理評測，不是遊戲生成；日後搜尋要加 `game generation` / `build a game`、排除 `game-playing agent`、`bug discovery`，避免把不同能力榜混入主 shortlist。 |


### 2026-10-04 收尾新增：可玩的單次展示與第二批正式研究

#### 新找到的 strict one-shot 候選：《Sky Reach》

[作者 2026-09-27 的 Reddit 原帖](https://www.reddit.com/r/aigamedev/comments/1wrstzo/i_remade_no_mans_sky_with_opus_55_threejs_on/)提供實際 gameplay 影片和作者自述：Claude Opus 5.5 + Three.js + Tesana，約 40 分鐘，作者稱影片是「first prompt output」。原始提示全文為：“Make a fully procedural No Man's Sky game, where I can seamlessly traverse between planets.” 作者主張作品有程序生成星系、星球地形／天氣／動植物、採礦、外星遺跡、小行星帶、太空站，以及無縫星球—大氣層—太空—另一星球飛行；可玩的[作者連結](https://tesana.com/game/sky-reach)列在原帖。

**這是本輪新增最貼近「單一 prompt 直接產生高複雜 3D 可玩成品」的公開候選。**但目前材料仍是作者自述與一段影片，沒有獨立 build / source / session log / 行為測試；本輪瀏覽器無法開啟 Tesana 連結，不能說我已確認 playable 正常。影片展示星球間移動與程序探索場景，尚不能驗證採礦／遺跡是否形成可玩的目標、經濟或勝敗閉環，也沒有確切 API model ID、effort 或評分。建議列「strict one-shot 候選 showcase（證據中等、待核 build）」，先看作者原片；若要把它做成重跑題，需補資源循環、落地探索、明確目標與 2–3 個行為驗收。不要直接把 showcase 自述當作基準分數。

#### 高複雜成品參照：《Tidewater》

[Opus 5.5 Tidewater repo](https://github.com/dgreenheck/tidewater)與[可玩版](https://dgreenheck.github.io/tidewater/)展示釣魚拉扯張力、魚貨出售／裝備升級、船隻與燃油、島嶼／珊瑚礁探索、日夜／魚群差異、海洋天氣與自製 WebGPU/WGSL renderer；repo 明確把它定位為高投入、多人代理、多階段開發（初版約 8 小時），之後又加入經濟玩法。故為高複雜玩法、渲染和產品閉環的題材參照，不能算 one-shot build。另查到《Twilight Crossing》其實是既有 Unity RTS 移植到網頁再加 Jev classifier，不是從零生成；此排除例也記入台帳。

#### 新的正式基準：如何使用、為何不能直接混入同一榜

| 資料／研究 | 新核實內容 | 對本研究的判斷 |
|---|---|---|
| [GameXpert-Bench](https://arxiv.org/abs/2608.21833) | 2026-08-22 論文；GameGen 軌從空白 workspace 依單一 request 生成完整遊戲，97 題、11 類；另有 100 個修復任務（50 關、每關 19–27 個植入錯誤）和 17 條、每條六輪的累積優化鏈。使用即時遊玩、deterministic behavior tests 或產品準則評估。 | 題型／生命周期切分比單一榜完整，GameGen 最貼近一次委託生成；但網站把程式碼／資料集標成待釋出，這輪未查到可立即完整重跑的 task/evaluator，也尚無 GPT-6 Astra／GPT-6.1 Sol 結果。列入追蹤，不當可立即跑的對照。 |
| [PlaytestArena](https://arxiv.org/abs/2605.28258)／[專案 demo 頁](https://continual-game-generation.vercel.app/) | 200 個 browser game generation 任務、八類，配逐項「遊戲中應出現什麼行為」rubric；GUI agent 真正開瀏覽器玩。論文稱 Direct LLM 單次生成是比較基線；比較的 GPT-5.4、Sonnet 4.6、Kimi K2.5 平均 rubric pass 約 31.6%、29.7%、27.8%，GUI 評分對人員逐項一致率 84.2%（32 款樣本）。專案頁目前列八款可玩 demo；Play2Code 是後續生成—遊玩—修改的多輪方法，不要與 one-shot 組混淆。 | 目前找到最清楚把 direct one-shot 和 agentic iteration 分開、又使用真實遊玩的研究。可借 rubric／盲評方式；但目前看不到完整 200 題、rubrics/evaluator 下載，且模型 roster 已舊，因此先列方法與少量作品預覽參考。 |
| [AutoUE / PlayGen-20](https://arxiv.org/abs/2603.07106) | Unreal Engine 5 的 20 個 3D 遊戲任務（5 簡單／7 中等／8 困難），包含物件拾取、互動、對話、戰鬥和目標依賴；有生成的遊戲／資產及 demo 影片。用 Scene、Gameplay、Visual 三項 LLM judge 評 1–10 分，加權 0.35、0.35、0.30。AutoUE 是檢索文件＋多代理＋自動 playtest 系統，結果不是統一條件多前沿模型的裸跑比較。 | 高難度 3D 空間／互動與引擎工作流題型很有參考性；適合從 hard tasks 借驗收點。由於專用多代理 pipeline 和 judge 分數，不作最新模型排行榜。 |
| [OpenGame-Bench](https://arxiv.org/abs/2604.18394)／[OpenGame repo](https://github.com/coconutpurpleJIN/OpenGame) | 150 個 browser game prompt、五類、三個 seed；Build Health、Visual Usability、Intent Alignment；repo 有 agent framework、playable demo/source。作者另稱錯誤會自動修復直到可玩。 | 評測方向可參考，但 benchmark pipeline／完整題集尚未釋出；多輪修補也不是 strict one-shot。模型年代較早，暫列背景研究。 |
| [WebGameBench](https://arxiv.org/abs/2605.17637) | 111 browser-game task，從規格、生成、部署到 browser interaction；分 EXCELLENT／USABLE／UNUSABLE，論文最佳設定 usable 76.9%、excellent 20.2%。 | 交付／部署評估啟發性高；本輪未找到官方題集、runtime evaluator 或 repo，暫不能重跑，亦非更大型原生遊戲。 |
| [GameDevBench](https://proceedings.mlr.press/v306/chi26a.html)／[官方 repo](https://github.com/waynchi/gamedevbench) | 333 個 Godot 專案級遊戲開發任務，重點是圖像／動畫、UI、既有遊戲邏輯的局部修改；repo 顯示 GPT-6.1 Sol xhigh 69.97%，GPT-6 Astra high 229/333（68.8%）。 | 模型版本新、可衡量多模態／遊戲開發能力，但不是空白起步的一次生成完整遊戲，必須另列，不放進主分數。 |
| [DuelLab GameBench 2](https://benchmarks.duellab.org/) | 2026-09-26 snapshot：73 個 model families、8 個公開遊戲、209,502 場比賽；GPT-6 Astra XHigh score 94.8、Claude Fable 5.1 XHigh 92.1、Opus 5.5 XHigh 81.9。模型先寫程式扮演玩家，再讓程式彼此競賽；不是生成新遊戲。 | 對弈結果不用人類／AI judge，適合「模型能否寫出會玩的 player」研究；與本研究的 game generation 是另一能力，排除主榜。 |

**方法建議更新：**研究應明確拆三條能力軸：A. strict first-output（初次模型輸出後立即凍結，不許工具測試／修改）；B. one-task agentic run（只給一則 user task，但可在同一 run 使用工具迭代、不能讓人類補充）；C. continual game dev（多輪人機協作）。GameXpert/PlaytestArena 的 one-shot track、GameASG 的單次 agent run、展示帖自稱 one-prompt，分別量到不同概念，分開榜單。三軸都應至少 3 個獨立 run、報每次成功／失敗，不把最好的一次代表模型。

#### 本輪新增搜尋與去重台帳（合併重複 query）

| 本輪實際用過的搜尋字串／來源頁 | 已核實／排除 | 未來去重規則 |
|---|---|---|
| `2026 benchmark generative game creation interactive games benchmark dataset paper playable agents`；`2026 game generation benchmark procedural game creation LLM evaluation benchmark playable demo dataset`；`site:arxiv.org 2026 benchmark "game generation" interactive game benchmark`；`site:github.com benchmark "game generation" LLM playable games evaluation 2026` | 找到 GameXpert-Bench、PlaytestArena、GameASG-Bench、OpenGame-Bench、WebGameBench、GameDevBench。後三者的評估用途不同：OpenGame 是 agentic generation、WebGameBench 是規格到交付、GameDevBench 是既有遊戲修改。 | 本輪所列正式基準已按 scope 歸位。之後以資料釋出、模型新增和 benchmark version 查，不用同一泛用論文 query 重掃。 |
| `PlayGen-20 Unreal benchmark 20 games models 2026 AutoUE`；`site:github.com/Pluto156/AutoUE Unreal game tasks evaluation` | 找到 AutoUE 的 UE5 multi-agent 3D 任務和 hard 題型，單一系統、LLM judge。 | 只在官方 repo 發新版、新模型 run 或 demo gallery 新增時回查。 |
| `GamED.AI game generation benchmark 200 questions demo 2026`；`GUI Agents for Continual Game Generation PlaytestArena 200 browser tasks rubric`；`PlaytestArena 200 browser game prompts GUI Agents continual game generation benchmark` | 查 PlaytestArena 的 200 題／1,548 rubrics／八款 demos，及 one-shot Direct LLM baseline 與多輪 Play2Code 分離。 | 只在完整 tasks/rubrics/evaluator 釋出或新模型追加時查；毋須重複查題目數與論文 baseline。 |
| `OpenGame-Bench github 150 prompts tasks model results playable games`；`OpenGame full benchmark task set eval pipeline 150 browser games` | 確認 150 prompts、3 seeds、interactive eval 與目前缺完整 benchmark pipeline。 | 等官方 evaluator 上線／新型號結果才重查。 |
| `WebGameBench 111 frozen specification-to-browser game tasks benchmark` | 確認 paper 的 delivery/deployment 評估指標；本輪未找到公開可重跑包。 | 只有官方題集／評估器公開時回查。 |
| `GameDevBench github 333 tasks game development benchmark repository`；[官方 repo](https://github.com/waynchi/gamedevbench) | 核對 GPT-6.1 Sol / GPT-6 Astra 成績與 task scope 是在既有 Godot 專案修改。 | 不再把它誤列完整遊戲生成；有新的 from-scratch track 才調整分類。 |
| `"first prompt output" Opus 5.5 game browser September 2026`；`"one prompt" "Claude Opus 5.5" game playable September 2026`；`"one-shot" Claude Opus 5.5 playable game September 2026`；`"Claude Opus 5.5" Tidewater fishing game repo playable prompt 8 hours September 2026`；`MattiTynka JEV-RTS Twilight Crossing Claude Opus 5.5` | 發現 Sky Reach、Tidewater，並排除其實是既有 Unity RTS port 的 Twilight Crossing。 | 不泛搜作者標題；Sky Reach 僅在出現 source、已驗證 playable build 或明確玩法閉環時回查；Tidewater 等原始 run log；Twilight Crossing 不再列從零生成候選。 |
| `"GPT-6.1 Sol" "game" "one prompt" 2026 October`；`"Claude Sonnet 5.5" "one prompt" game 2026`；`"Claude Opus 5.5" game "one prompt" playable October 2026`；`site:reddit.com/r/ClaudeCode "Sonnet 5.5" game "one prompt" after:2026-09-30`；`site:reddit.com/r/ClaudeAI "Opus 5.5" game "one prompt" after:2026-09-30 playable`；`site:reddit.com/r/ChatGPT "GPT-6.1 Sol" game "one prompt" playable 2026 October`；`"GPT-6 Astra" "one prompt" game playable October 2026`；`"GPT-6.1 Sol" "game" "Claude Opus 5.5" build game prompt`；`"Age of Empires-style multiplayer game" "Sonnet 5.5" ForwardEditor`；`"four-floor" "Resident Evil" "Sonnet 5.5" game`；`"CoD Zombies clone" "Sonnet 5.5" one prompt Three.js`；`"same prompt" "GTA Rio" "Sonnet 5.5" Opus 5.5 game` | 新的嚴格跑次中，高複雜證據仍稀缺。Roblox kart 沒公開 playable place / run log；Age of Empires、Resident Evil 等先在索引頁出現、原始社群帖無法核實。既有 Hill Climb、Kart、FPS 和 PUBG/MALL 等依台帳排除。 | 上述精確詞已查過；待作者公開完整 prompt/session、source 或實際 build 後再核對。索引命中不能作成品證據。 |
| `GPT-6.1 Sol vs Opus 5.5 Hill Climb`；`GPT-6 Astra Roblox kart racer case study`；`Claude Sonnet 5.5 Age of Empires Resident Evil game prompt`；`Moe Lueker GPT-6.1 Sol vs Astra vs Opus 5.5 games` | 排除重複／弱證據：Hill Climb 已在台帳、簡單關卡；Roblox case 只有轉述 prompt/影片；Sonnet 遊戲只有索引鏈接失效；Moe Lueker 跨模型內容主要不是完整遊戲。 | 不要因文章／索引再次發布而新建同名案例；只有多出作者原始 run 或具體可玩的新版本才復核。 |


## 2026-10-04 補漏複查：新增可重跑候選與證據分級

使用者提醒「足夠好就應列入」，因此本輪不是重做已查過的泛搜；而是回看高複雜度候選，並核對新發現的可玩輸出、任務規格與自主流程證據。是否已有多模型對照不作入選門檻。檢閱頁新增六題；其中三題有 AI build／流程材料，三題是正式任務規格強但尚無已確認的 AI 成品圖廊。未以原作／類型示意圖冒充 AI 輸出。

### 新增最優先重跑候選

| 候選 | 為何足夠強 | 證據與限制 |
|---|---|---|
| NEON BAY | 程序城市、交通與行人、通緝、警察追捕、七款車，以及剛體／懸吊／輪胎／ABS 等物理；明顯測 3D 物理、場景與 NPC 系統的耦合。 | Opus 5.5 單一 task 的作者自述，約 70 分鐘；repo 有 build log／自動駕車測試與修正紀錄；可玩版公開。無外部盲評。沒有徒步、任務、音訊、存檔，故定位為物理與程序城市副主測，不宣稱完整開放世界。來源：[repo](https://github.com/L1vsun/NEONBAY)、[playable](https://l1vsun.github.io/NEONBAY/)。 |
| Claude of Duty | Three.js FPS 長程整合，武器、敵人、動畫、程序資產、音訊與渲染；作者稱約 55k 行、11 個系統，自行用代理與視覺檢查迴圈。 | 原始 prompt、repo 與作者方法公開；作者說單一 task 後交付，但模型為 Opus 5，成果品質評語非盲測且未達 prompt 的 AAA 目標。適合固定原 prompt 重跑新模型，低於 NEON BAY／Ruinseed 優先序。來源：[prompt](https://github.com/mshumer/Claude-of-Duty/blob/main/prompt.md)、[repo](https://github.com/mshumer/Claude-of-Duty)、[建置說明](https://t.co/xixH3xaJGH)。 |
| LAST COURIER | 七個據點配送的程序 3D 冒險，載重與損壞、橋梯、雨蝕、潛行、電池／機體、存檔與結局；作者提及自動 bot 使用物理跑到結局。 | 有 repo 與可玩 build，但一次任務／無人工介入沒有被作者明確證實，repo 也跨多日更新。列為高深度任務素材，不能列作已核實的一次生成結果。來源：[repo](https://github.com/tanuu5/last-courier)、[playable](https://tanuu5.github.io/last-courier/)。 |

### 新增正式 benchmark 任務

GameASG-Bench 官方 README 確認總計 47 個 browser game 任務、12 個主要類型，其中 32 款 2D、15 款 3D。每題提供 target、game-spec、tdd；交付單一 `index.html`，驗收結合靜態檢查與 headless Chromium 實際操作／狀態檢查。預設一個乾淨工作區、單次生成嘗試、3600 秒上限；這符合「一次使用者任務、AI 可自我修正」，但額外要求單檔及公開測試介面，重跑時可依使用者測法裁剪。官方 README：[GameASG-Bench](https://github.com/areal-project/GameASG-Bench)。

| 題目 | 高難度所在 | 圖像／輸出證據 |
|---|---|---|
| Grand Theft Astro | 3D 城市；步行／駕駛切換；碰撞、導航、射擊、NPC、警察、任務、商店、小地圖、死亡重生等跨系統狀態。新題中範圍最大、失敗風險最高。 | 有完整官方任務與測試契約；未確認到 AI 成品圖廊，不放 genre image 假裝實測。來源：[target](https://github.com/areal-project/GameASG-Bench/blob/main/task/grand-theft-astro/target.md)、[spec](https://github.com/areal-project/GameASG-Bench/blob/main/task/grand-theft-astro/game-spec.md)。 |
| Ancient Beast | 六角格回合制戰術；佔格、距離、回合佇列、召喚成本、技能範圍、狀態效果及勝負判定。測狀態一致性與非法操作處理。 | 有官方原作可玩、原作畫面及完整測試契約；原作圖在 HTML 明確標示不是 AI build。來源：[spec](https://github.com/areal-project/GameASG-Bench/blob/main/task/ancient-beast/game-spec.md)、[tdd](https://github.com/areal-project/GameASG-Bench/blob/main/task/ancient-beast/tdd.md)、[official game](https://ancientbeast.com/)。 |
| Bikini Bottom Survivor | 3D 生存戰鬥：追擊敵人、自動攻擊、命中／死亡／經驗掉落、升級暫停與選擇、敗北及重開；延伸有 Boss、任務、旅行、成就、存檔。 | 有正式規格與 browser 測試；未找到 AI 成品圖廊，不以 SpongeBob 或 Vampire Survivors 類型畫面代替。來源：[target](https://github.com/areal-project/GameASG-Bench/blob/main/task/bikini-bottom-survivor/target.md)、[spec](https://github.com/areal-project/GameASG-Bench/blob/main/task/bikini-bottom-survivor/game-spec.md)。 |

### 原有高潛力題的再檢視與保留／不納入理由

- **Tumble**：明確物理與建造規格（無外部物理引擎、自製 180Hz、連續碰撞、100 marble 壓力、15 種元件、編輯器／undo-redo、demo 與 puzzle）。值得物理副題重跑；目前未核實到可玩的模型輸出與可復原 run，故候選文字先保留在此待清單，不列檢閱頁「AI 成品」主區。來源：[任務／比較文章](https://promptslove.com/blog/claude-opus-5-5-vs-gpt-6-astra/)、[影片](https://youtu.be/cwGSDctKCbk)。
- **3D Mini Golf**：Opus 與 Fable 各有可玩的九洞 3D build，並有物理求解、碰撞測試／headless 完賽材料；適合作為 3D 碰撞與關卡解法副題。不過原始共同任務 prompt 與各自迭代條件未公開到足以原樣公平重跑，故先列待補 prompt 的可玩參考，不列作核實的一次任務結果。來源：[Opus repo](https://github.com/leonvanzyl/3d-golf-opus)、[Fable repo](https://github.com/leonvanzyl/3d-golf-fable)、[影片](https://chooseto.ai/watch/NzyP4VjkrvM)。
- **Bastion / BASTIÓN MECHA**：有可玩的 Mech 戰鬥與城堡資源／建造循環，Opus 5.5 自動 bot／程序美術說明；但有人工遊戲設計和 HUD 美術介入、缺原始 prompt／完整 run log，故作遊戲系統參考，不列一次任務證據。來源：[itch page](https://lambdaforge.itch.io/bastion)。
- **Crazy Tanks — Wild Tides**：高度耦合的坦克物理、可破壞島嶼、風向、武器、崩塌／水火及 AI 對戰；任務規格是根據 source/reference 重建，並非已核實模型收到的原始 prompt，沒有 AI build。因此可作自行新寫 brief 的設計種子。來源：[spec source](https://www.tripo3d.ai/3d-prompts/crazy-tanks-3d-island-artillery)。
- **BioNeural**：開放式「自行設計並交付多人遊戲」很貼合自主性測試；原作者說 Opus 5.5 medium 約五小時完成多人、bot、voice、破壞物件與天候。但網站後續更新、無法只靠現在頁面還原首版狀態；server/network/tool 權限又大幅影響比較。可另立開放式創作測試，不與固定 brief 題混排。來源：[原始貼文](https://www.reddit.com/r/ChatGPT/comments/1wqd0gg/houston_we_have_a_problem_opus_55/)、[live site](https://bioneural.de/)。
- **Tiny Necromancer**：16 種房間、塔防／建造配置、骷髏工作分派、資源和三階段 boss，題目夠深；但由 GPT-6 Astra 與 Opus 5.5 協同開發，無獨立 prompt/session 證據。可借作 strategy/defense 任務素材，不當 one-task 成績。來源：[playable](https://dylanh.itch.io/tiny-necromancer)。
- **Opus 5.5 FPS／漂移賽車／單車 demo**：作者提供 playable source 與驗證，聲稱單 session 無人工程式編輯；各系統有趣，但較短 prompt 下完成的是中型專項，不及 Ruinseed、MALL ACTION、NEON BAY 的整體遊戲規格廣。來源：[repo/demo](https://github.com/riba2534/claude-opus-5-5-demo)。
- **Sky Reach**：單行 prompt、影片與無縫行星／太空概念吸引，但目前未核實完整可玩 build、source、目標任務或自主過程，僅列待查。來源：[作者貼文](https://www.reddit.com/r/aigamedev/comments/1wrstzo/i_remade_no_mans_sky_with_opus_55_threejs_on/)。
- **MACH RUN**：原作者澄清一提示只產生視覺、谷地與飛行物理，完整遊戲之後花數週完成；不符合「最後交付的一次產品」證據門檻，不加入。

### 本輪已做的新增搜尋與去重記錄

1. 回看研究底稿中「高複雜度但證據不足」候選，分別查官方／原作者 source、任務規格、build、prompt、autoplay 或迭代紀錄；新增 Tumble、Mini Golf、Bastion、Crazy Tanks、BioNeural、Tiny Necromancer、Opus demo、Sky Reach 狀態及不入主區理由。
2. 對 GameASG-Bench 官方 task catalog 再掃一遍，找出 Grand Theft Astro、Ancient Beast、Bikini Bottom Survivor；暫不追加 Fast Food Tycoon（3D 餐廳模擬值得保留但經濟循環與 Airship Trader 重疊，屬較低優先）、避免塞入過多同類項目。
3. 廣搜近期 Opus 5.5／GPT-6 Astra game repo 與 one-task/autonomous build，核對來源後新增 NEON BAY、Claude of Duty、LAST COURIER；排除 Wreckyard（多人伺服器與車體破壞規格雖強，但多階段規劃／112 commits，未見 one-task 無人工證據）、低產出 FPS 展示、兩 prompt 的 Crown and Claw。
4. 搜尋要點只做候選擴充，沒有聲稱本輪已對每個模型執行 benchmark。後續避免重跑廣泛搜索；只查：官方 prompt/任務版本有更新、當前模型新 build 出現、被標「流程待核」的項目補齊 prompt/session 證據，或使用者指定某一候選深入查。
5. 圖片政策：只有 AI 生成的實際遊戲畫面標作 AI build；原作圖及 genre reference 必須在圖說明確標示來源／用途。沒有可核實畫面時，讓完整規格和原始任務連結承擔說明，不生成替代圖、不使用不相干示意圖。


