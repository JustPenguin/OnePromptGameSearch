# S31｜AI Browser Game Jam 高排名作品查核

**日期：**2026-10-07（台北時間）  
**研究問題：**S30 找到的高品質 game-jam 線索是否同時符合「一次委託、之後無使用者干預，AI 自主修正、以凍結最終成品驗收」？核對 top-ranked 可玩作品的實際玩法、模型／工具、玩家評分、公開任務和開發／回饋時間線。  
**先前查重：**重讀研究索引、精選候選、search/index 與 S30；`Plug & Prosper` G0119、`AI2U – Guns & Girlfriends` G0013 已存在，故更新原紀錄；其餘三作查重後分配 G0245–G0247。S30 預告的下一方向是深查 AI Browser Game Jam 高完成度作品。

## 實際搜尋與查閱

- `site:itch.io/jam/ "AI Browser Game Jam 4" entries Focaccai 82`
- `"AI Browser Game Jam 4" winner 2026 itch.io Focaccai`
- `site:itch.io/jam/ "AI Browser Game Jam 3" entries June 2026 Focaccai`
- `"Plug & Prosper" "prompt" Codex 5.6 Sol Small Loop Works`
- `"A Low Poly Dungeon Game" itch AI Browser Game Jam 3 source AI model`
- `"Plug & Prosper" game jam AI generated game prompt developer log`
- 點進 Jam 4／Jam 3 官方 Results 的 top entries，再開原提交頁與 itch playable/game page；另看 Plug & Prosper 開發者文章、玩家留言及版本資訊。

## 結果核對

| 作品 | 玩家評分／作品內容 | 流程證據及結論 |
|---|---|---|
| [Plug & Prosper](https://smallloopworks.itch.io/plug-prosper)（[Jam 4 投稿評分](https://itch.io/jam/ai-jam-4/rate/4852654)） | Jam 4 總榜第 1，10 票／4.100；Graphics 第 1（4.500）、AI Usage 第 1（4.400），Fun 第 11（3.600）。投稿披露 Codex CLI harness、GPT-5.6 Sol low–xhigh、Lyria、GPT Image 2。當前作品有線材物理、配件／能源管理、五個手工關卡、星等、無盡 kiosk／跨日升級；舊版文章記錄三分鐘 12 單的原型 brief。 | Jam 4 規則明確歡迎且預期人工編輯精修、完整流程披露是 optional。原 prompt／session 未公開；遊戲頁有玩家自動化試玩回饋與作者修補，現版已多次更新至 1.4.1。可作高品質管理益智／線材物理題型參照，不是 one-shot 成績，也不因 Graphics 第一就預判符合使用者美術門檻。更新 G0119。 |
| [AI2U - Guns & Girlfriends](https://helixngc7293.itch.io/gandg)（[Jam 4 評分](https://itch.io/jam/ai-jam-4/rate/4867618)） | 總榜第 2，15 票／4.000；Graphics 第 6（4.200）、Fun 第 8（3.667）。作者列 Fable 5 + Opus 5、Gemini／Nano Banana、Suno。三陣營 RTS、有五張地圖、三種 AI 難度人格、兵種克制、資源採集、基地和核武勝利條件。 | 作者留言明說使用 gauntlet-loop prompting、總投入約 72 小時；有玩家通報地圖操作 bug，作者回覆修好。這是高系統範圍 RTS 的好設計／品質參照，流程明確有迭代，且無原始 prompt／逐輪 trace；排除 one-shot 成績。更新 G0013。 |
| [Monster Mash](https://cameronsevern.itch.io/monster-mash)（[Jam 4 評分](https://itch.io/jam/ai-jam-4/rate/4856172)） | 總榜第 8，7 票／3.714；Graphics 第 2（4.286）。簡介是 1–2 人 turn-based monster fighting，能以戰損部位組合怪物。 | 投稿列兩位作者、Codex、Suno，標示 AI 輔助 code／graphics／sound／text；無模型版本、原始 prompt 或完整流程。只保存作品線索，不升格。新增 G0245。 |
| [Pyramid Wars Demo](https://durian-arcade.itch.io/pyramid-wars)（[Jam 3 評分](https://itch.io/jam/ai-game-jam-3/rate/4673138)） | Jam 3 總榜第 1，14 票／4.286，Fun 4.357 第一。10 關 RTS，基地、資源、部隊、技能和 booster cards。 | 作者稱 solo vibe-coded 三週，使用 Claude Opus 4.8；玩家建議後作者調整炮塔耐久／建造時間與卡包，另有關卡／編輯器更新。無精確 prompt／session，明確是持續人類迭代；僅保留 RTS 品質與題型參照。新增 G0246。 |
| [A Low Poly Dungeon Game](https://fynbosexplorer.itch.io/a-low-poly-dungeon-game)（[Jam 3 評分](https://itch.io/jam/ai-game-jam-3/rate/4664865)） | 總榜第 2，14 票／4.071；Graphics 第 3（4.214）、Fun 第 4（3.714）。固定 seed 的 PSX 第一人稱三區地城，鑰匙／鎖門／寶箱、具攻擊模式的骷髏、輕重擊／格擋／耐力／藥水與不可逃離的 Boss。 | 列 Claude Code、ElevenLabs、Suno；畫面來自資產包，沒有模型版本或 prompt。玩家提出難度、狀態提示、靈敏度問題後作者調低難度、加血條並修操控。遊戲完整度高，但 live build 含人類 feedback loop，不能算一次交付。新增 G0247。 |

### 賽制及分數的界線

官方 [AI Browser Game Jam 4 規則](https://itch.io/jam/ai-jam-4)說明活動目標是探索 AI 輔助創作、使用任何 AI 工具，鼓勵分享流程但不強制；規則明文歡迎並預期人類創意、編輯與精修，個人或團隊均可。官方 Results 頁記錄 125 entries、1,034 ratings，平均每作 8.3 票；Jam 3 results 為 77 entries、596 ratings。這些評分只描述當期參賽者對遊戲及 AI 使用的感受，不能當成模型排名或零介入實驗。Jam 4 投稿數字與後來提交頁另顯示 126 entries，保留來源時點的差異，不推定哪頁出錯。

## 結論與更新去向

這一輪核對了 5 款獲高玩家評價的真實可玩作品，確實找到強 system／game-quality 參照：AI2U 和 Pyramid Wars 的 RTS 系統，A Low Poly Dungeon 的戰鬥／關卡閉環，以及 Plug & Prosper 的創意物理與經營玩法。然而它們不是可直接採用的一次生成成績：有的流程明示三週／72 小時迭代，有的經受玩家回饋修訂，其他則欠缺原始任務與模型／版本 trace。Jam 規則本身也允許、甚至期待人類精修。故本輪**不新增精選 one-shot 候選**，不把 jam 排名當成人工美術驗收；若將來為現行模型重跑，需先重寫固定任務規格，另行記錄新 run。

- 更新既有 [G0119 Plug & Prosper](../records/G0119.md) 和 [G0013 AI2U – Guns & Girlfriends](../records/G0013.md)。
- 新增 [G0245 Monster Mash](../records/G0245.md)、[G0246 Pyramid Wars Demo](../records/G0246.md)、[G0247 A Low Poly Dungeon Game](../records/G0247.md) 作已核線索與排除理由。
- 不變更精選候選頁或 HTML，因沒有作品同時補足一次任務、版本／模型及自治流程證據。
- **下一方向：**S30 的 Jamference 作品在 2026-10-09 截止後一週互評；屆時用官方提交頁和作者自述檢查鎖版作品，優先查能提供初始 prompt、commit/session 時間線、可玩 build、遊戲本身評測並排除人類回饋修訂的高品質 entries。若仍缺少，轉查目前 GPT-6.1 Sol／GPT-6 Astra／當前 frontier 模型有 prompt、未修改 frozen build 和 run log 的社群可玩發布，而不是再根據 leaderboard 排名加案例。
