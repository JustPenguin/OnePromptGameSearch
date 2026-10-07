# 搜尋批次 S-20261007-37：近期模型遊戲來源與 QA 稽核

**日期／範圍：**2026-10-07（Asia/Taipei）。查近期 GPT-6.1 Sol／GPT-6 Astra 與 Claude Opus 5.5 實際可玩輸出，優先追 source、任務、作者 QA、模型歸因和使用者介入證據；用逐項來源核對篩選策展清單與社群高評作品。

## 研究問題與先前查重

延續 S36 對「近期模型遊戲 build／session artifact」的方向，本批把關注點收窄到有公開原始碼和可運行測試的高完成度實物。讀過索引、候選摘要、搜尋批次索引；`manage.py lookup Slipstream` 已命中既有 **G0143**，因此更新原紀錄而不建新遊戲編號。策展入口為既有 **C0003**；Space Attack、ORBITAL、Mall Action、Slipstream 也都已在本地台帳，避免重複建檔。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `GPT-6 Astra full game source code self playtest playable game September 2026 single prompt RPG`；`Claude Opus 5.5 game build source code autonomous playtest complete RPG 2026 one prompt`；`site:github.com GPT-6 Astra game "playtest" "boss" game generated`；`site:github.com "GPT-6.1 Sol" game "playable" prompt game generation` | 找到／交叉遇到 Slipstream、DEAD AIR、MUTE、Dawnmark 等 repo；Slipstream 有短任務摘要、空白 workspace 與完整 Playwright QA 說明，成為本批最完整的新近源碼實物。其餘數項的公開歷史顯示迭代或缺乏獨立遊戲成品／流程證據，見下列排除。 | [G0143](../records/G0143.md)、[G0232](../records/G0232.md)、[C0003](../records/C0003.md) | 若 Slipstream 公開原始 session／首版 hash 或使用者評過美術，再更新證據；若資料庫出現明確更深的 GPT-6.1 Sol 作品，優先查是否包含多賽事／生涯閉環。 |
| `site:youtube.com/watch "Rampart" "Apex Circuit" "Void Wing" "Colossus" Astra Brendan`；`"Rampart" "Apex Circuit" "Void Wing" "Dead Signal" "Colossus" "Brendan Jowett" prompts`；`"NEW Opus 5.5 vs GPT-6 Astra Building Video Games" prompt exact task download playable build`；`Brendan Jowett Rampart Apex Circuit Void Wing Colossus GPT-6 Astra GitHub` | 對照 S36 的五題 UE5 影片資料；只有成品片段及時間／成本面板，未找到可核實的逐字 prompt、source／build 或 session，因此維持題型／畫面參照，不升為一次交付成績。這些字詞部分與 S36 查詢重疊，列出以保留本批線索核查路徑。 | [B0049](../records/B0049.md) | 若創作者釋出逐字任務、repo 或完整 build，重新稽核。 |
| `site:youtube.com "NEW Opus 5.5 vs GPT-6 Astra Building Video Games" prompt exact task download playable build`（連到同作者 2026-09-24 影片） | 與 S36 重查同一來源。重確認該影片不提供足以逐字重跑的任務與源碼；不另建重複記錄。 | [B0049](../records/B0049.md)、[S36](S-20261007-36-current-model-game-generation-runs.md) | 只在原作者追加可重現材料時再查。 |
| [Slipstream repo](https://github.com/KJLKurt/waterslide-game-gpt-6.1-sol)；[progress.md](https://github.com/KJLKurt/waterslide-game-gpt-6.1-sol/blob/main/progress.md)；[README](https://github.com/KJLKurt/waterslide-game-gpt-6.1-sol/blob/main/README.md)；[playable build](https://kjlkurt.github.io/waterslide-game-gpt-6.1-sol/) | Repo 自稱 GPT-6.1 Sol Extra-high、0-shot；`progress.md` 存作者標示的原始 prompt 摘要、空白起始 workspace 及多輪 AI 自測／修正項；README 列 51:58、49 API calls、4.82M tokens、main＋auto-review child，並列建置、Playwright 和 gameplay QA 覆蓋。沒有原始 session transcript，所以模型歸因與無使用者 follow-up 不是獨立稽核；「日期」只以 repo 2026-09-30 建立日作 proxy。完整原文與限制已寫入 G0143。 | [G0143](../records/G0143.md) | 若出現原始 transcript、精確 session 日期或外部玩家獨立通關測試，補證；待使用者親自判美術。 |
| [Slipstream curator note](https://github.com/AgentsLoop/awesome-opus-5.5-games/blob/main/games/slipstream/readme.md)；[GPT-6.1 Sol model page](https://github.com/AgentsLoop/awesome-opus-5.5-games/blob/main/models/gpt-6-1-sol.md)；[collection README](https://github.com/AgentsLoop/awesome-opus-5.5-games/blob/main/README.md) | 個別 curator note 把 Slipstream 評 8.5/10，但明確表示評 source completeness、mechanics、documented run path、tests、attribution，非視覺／runtime benchmark；目前沒有登錄該作 gameplay screenshot。README 當下報 909 game units／611 source repos，入口適合找線索，不構成控制過的模型評測。Model page snapshot 與 collection README 對 GPT-6.1 Sol 條目數有快取／版本差異；只把穩定可核的 Slipstream 個案收下，不推斷絕對完整 roster。 | [C0003](../records/C0003.md)、[G0143](../records/G0143.md) | 清單持續變動；僅在新條目具備原始任務、source／build 或強 session artifact 時值得重新掃描。 |
| [DEAD AIR source](https://github.com/PieterMey/theboys)；[MUTE source](https://github.com/dippy34/Ai-vr-game)；[Dawnmark source](https://github.com/Funashigiri/dawnmark) | **不升 strict one-shot 候選。**DEAD AIR 專案有規劃／回饋／多次 playtest 修正；MUTE 的直接模型證據指向 scaffold／design 檔，尚無與承諾相符的獨立 playable build 與乾淨交付流程；Dawnmark 有多個迭代版但沒有一次委託／初版 QA 依據。它們可留在已存在的查核索引或本批排除脈絡，不能以高策展分補足介入證據。 | [G0232](../records/G0232.md)、[S37 排除紀錄](#排除與邊界) | DEAD AIR 若找到一個清楚凍結的單 prompt 首版 run，可重新分開評；MUTE 若公開可玩版與完整 task trace，可復核；Dawnmark 若作者公開零追問 run artifact 再查。 |
| [Playco/Astra 官方案例](https://openai.com/index/playco-game-prototyping-with-astra/) | Playco 先有人工灰盒基底、經過原型／創意迭代，再由 Astra 一次生成三個主題版本；最接近單次生成的其中一版仍有性能修正。其內部 Playbot 可反覆操作 Unity/Godot，但基礎專案與迭代流程不符合「空白起始、一次交辦後無人介入」成品證明。保留作方法參考，不新增遊戲候選。 | [B0045](../records/B0045.md) | 若有獨立 blank-start run 和可下載固定成果再評估。 |
| [PaperRoute creator report](https://agientry.com/en/articles/astra-paperroute-full-game)；[Embervale 社群原文](https://www.reddit.com/r/ClaudeCode/comments/1w4qziv/ok_this_is_wild_used_claude_fable_5_1_and_said/) | PaperRoute 的「one-shot」指第一輪有可展示原型；完整遊戲跨數日、39 tracked hours、多人工作流和反覆 polish，不能算最終產品一次交付。Embervale 約 60–70 prompts、兩天並頻繁人工遊玩／引導；重申為長程自治參照，不是無人介入 run。 | [G0193](../records/G0193.md)、[S37 排除紀錄](#排除與邊界) | 若研究不同改版成本或長程自治，可另作方法比較；不加入 strict one-shot 名單。 |
| [Ink Field 社群貼文](https://www.reddit.com/r/ClaudeAI/comments/1wnzcbg/i_gave_opus_55_one_prompt_and_one_hour_to_make_a_game_then_actually_played_the_thing/)（S06 舊來源重查） | 標題／貼文說 one prompt／hands off，但已存 S06 作者留言寫明先問 concept、再被要求開始實作，實際至少兩次人類指示。視為舊項目去重與矛盾證據核對，不當新 run。 | [G0079](../records/G0079.md) | 若作者澄清不同 session 或公開 trace，再更新；目前不升格。 |

## 排除與邊界

- 不因策展 8.5 分、漂亮標題或「one-shot」行銷用語直接認定成功。Slipstream 的證據優勢是任務內容、source、可運行 build 與自主回歸測試可交叉檢查；主要不足是全程 trace 與美術檢視缺席。
- 近期高系統作品若有明確人工多輪 playtest／改版，保留題材參照但不納入使用者協定下的 run 成績。
- 類似的過往檢索查詢有重複使用，這是為了核實已知線索，不把重查次數冒充新增發現。

## 結論與更新去向

- 更新既有 [G0143](../records/G0143.md)：加入任務摘要、模型／時間／effort、source 與 QA 細節、one-shot 不確定性，以及美術待判定。
- 更新既有 [C0003](../records/C0003.md)：記錄作品庫評分定義、當下快照與可能更新／快取差異。
- 把 Slipstream 加入[研究索引](../../ai-game-one-shot-index.md)、[精選候選](../../ai-game-one-shot-candidates.md)及[供使用者檢視的 HTML](../../ai-game-one-shot-review.html)。定位為物理／自主 QA 副題，不取代完整長流程主測。
- 本批沒有新增 G 編號；主要提升既有 G0143 的可核細節，不足以說它是獨立驗證過的 zero-follow-up 成績。
- **待查：**目前 HTML 中 Slipstream 美術待使用者判定；如果可行，在公平條件下重新跑公開 prompt 時保存從任務提交到最後停止的完整 session 和終端 build hash。下一個方向可轉查現行模型近期的高系統 RPG／simulation，優先官方或作者一手 session artifact，避開本批源碼／競速方向。
