# 搜尋批次 S47：最新模型的一次委託可玩遊戲輸出

**查核日期：**2026-10-07（台北時間）  
**研究方向：**從近期公開模型作品、原創 hands-on 測試與基準頁面尋找 GPT-6.1 Sol／Claude Sonnet 5.5 等新模型實際生成的可玩遊戲，優先驗證一則 brief、AI 自測修正、最終輸出能直接檢視的 run。此輪不重複 S46 的多日自主案例或 GameASG/GameCraft 任務逐題篩選。

## 先讀索引與查重

按流程先讀 [研究索引](../../ai-game-one-shot-index.md)、[候選摘要](../../ai-game-one-shot-candidates.md)、[搜尋索引](index.md) 和 [S46](S-20261007-46-long-horizon-autonomous-game-runs.md)；比對目錄與既有 G0263、G0211、G0219、G0228、G0258、B0012、B0045，排除重複的 Crowd Rush、Afterlight、GPT-6.1 benchmark 既有記錄。這批聚焦近期一次 brief 生成的 playable file，而不是把局部 Godot 改檔 benchmark 當作完整遊戲。

## 實際查詢與來源

| query／來源 | 結果、核對與入選／排除原因 | 去向／待查 |
|---|---|---|
| Web queries：`"GPT-6.1 Sol" game built autonomous long-running coding agent game showcase`；`"Claude Sonnet 5.5" autonomous game development build multi-day one task playable`；`"GPT-6.1" "game" "autonomous" coding agent build showcase`；`site:developers.openai.com/showcase game coding agent GPT-6.1 autonomous game build`；官方 [OpenAI Showcase](https://developers.openai.com/showcase/all) | 近期 GPT-6.1 Sol 的遊戲成品線索包括已有紀錄 Crowd Rush、GameDevBench 最新榜，以及未重複的 BitsMinds Hill Climb 實測。OpenAI Showcase 當前篩選可見 GPT-6 Astra／GPT-5.6／5.5 作品，沒有新列 GPT-6.1 Sol build；官方展示不能當它已有長程遊戲案例的證據。 | 補強既有 [G0077 Hill Climb Racing](../records/G0077.md)，不另計同一 brief 的 Ridge Run 輸出；曾建立的 G0264 保留為轉向頁。已有 Crowd Rush 不複製成新紀錄。 |
| [BitsMinds Lab 原創 hands-on 測試](https://www.bitsminds.com/news/claude-opus-5-5-vs-gpt-6-1-sol-hill-climb-2026)；實際輸出 [Ridge Run](https://www.bitsminds.com/buildoff-2026-09/hillclimb_sol61.html)、[Hill Hopper](https://www.bitsminds.com/buildoff-2026-09/hillclimb_opus55.html)；作者實際 screenshot：[Sol](https://www.bitsminds.com/buildoff-2026-09/hillclimb_sol61_play.jpg)、[Opus](https://www.bitsminds.com/buildoff-2026-09/hillclimb_opus55_play.jpg) | GPT-6.1 Sol 一次 brief、Codex max、自行測試修正、57m38s，build 內嵌可直接玩；同題 Opus 5.5 98m06s，有不同工具 harness。任務要求單檔 HTML 無外部網路／圖片，3-screen 遊戲循環、車輪懸吊、鍵盤／觸控、物理、失敗／重開。Hands-on author score Sol 13/20（圖形3／物理4／音效3／玩法3），Opus 19/20。作者指出 Sol 版本的 900m／五區、較順的貨幣收集與偏寬鬆油耗，故低分主要在畫面差異及玩法深度，而不代表物理系統不存在。 | 收錄為**高品質單關物理／自主 QA 副測**，不列完整遊戲上限主測。使用者美術尚待直接評價，作者 3/5 不是使用者判定。 |
| 同一 BitsMinds 報告中的 task/session/evidence 描述與兩份 playable page | 作者明稱原始 prompt 文件未公開，文章內只有詳細任務描述；沒有完整 raw session。作者稱兩題除了輸出路徑只差兩行，並說 Sol build 的提交前測試含 headless Chrome、多種賽道行為、restart、touch、frame-rate physics、screenshots。GPT-6.1 Sol 讀過 Codex 對先前 one-shot build 的一般 memory；作者未找到 memory 包含此題答案的跡象。 | 自主 no-follow-up 和相同 brief 是第一手作者報告，非第三方 session 稽核；不同 harness、有先前一般 memory、無盲評，控制條件有混雜。保留為有效 re-run seed，不把作者名次當純模型因果比較。 |
| Official leaderboard： [GameDevBench](https://waynechi.com/gamedevbench/)；已有 [B0012](../records/B0012.md) 與 S26 | GPT-6.1 Sol xhigh/Codex 為 333 題中目前榜首 69.97% ±4.9，略高 GPT-6 Astra 68.8% ±5.0；榜單明示 pass@1 與各模型最佳多模態設定。查閱後確認這是既有 Godot 專案開發任務，不是空白工作區完整遊戲生成；資料已在 B0012 記錄，非本輪新候選或排名。 | 保持 B0012 的範圍限制；連結本批次作近期覆查，不把榜首轉成 one-shot full-game score。 |
| Queries：`"3D zombie FPS" "49 minutes" Sonnet 5.5 prompt playable github`；`site:bitsminds.com/news/claude-opus-5-5-vs-gpt-6.1-sol-hill-climb-2026 prompt screenshots playable`；Reddit 原始貼文及二手逐步教學 | Sonnet 5.5 49 分鐘／$177 3D zombie FPS 目前可找到的主來源是 Reddit 發文和依其改寫的教學；未取得原始 prompt、可核實生成 build/source、完整 trace 或作者遊玩記錄。宣傳語本身不足以核實一次委託或成品系統。 | 不新增強候選；保留為未核實線索。若原作者補上 prompt、實玩 build、版本及自主迭代證據再查。 |

## 本輪結論

S47 原將 Ridge Run 另建為 G0264；查重時發現既有 G0077 已收錄同一 Hill Climb brief 和此次對照，因此將新 build、量測與限制併入 G0077，G0264 保留轉向頁，不重複計為候選。Ridge Run 完整呈現了模型在物理、副系統、單關閉環與畫面上的實際取捨；但它的任務規模有限，應當用作物理副測或 calibration brief，不應取代長流程／多系統主測。直接 playable build + 真實輸出 screenshot 已加入 review HTML，並明示美術由使用者尚待評價。

本輪未發現 Sonnet 5.5 49 分鐘 FPS 說法足以核實的一次 run；GameDevBench 新榜首也仍是專案修改能力，不能補成完整遊戲成績。

## 交接後連結核對與證據補充（2026-10-07）

- 原先記錄的作者文章 URL 把 slug 寫成 `gpt-6.1-sol`，回傳 404；由 BitsMinds 新聞索引確認正確網址為 [Claude Opus 5.5 vs GPT-6.1 Sol: A Familiar Hill Climb](https://www.bitsminds.com/news/claude-opus-5-5-vs-gpt-6-1-sol-hill-climb-2026)，直接讀取回傳 200。兩份 playable HTML 與兩張 JPEG screenshot 也回傳 200。已在 G0077、候選、總索引及檢閱頁修正連結。
- 正文補足可核查任務條件：單一 self-contained HTML、無 CDN／網路／圖片／web fonts、iframe sandbox、三畫面閉環、懸吊車輛、鍵盤／觸控、失敗重開及固定幀率物理。作者明確描述每模型一次嘗試、無 follow-up／清理，Sol brief 除輸出路徑外與 Opus 相同；原始 prompt 與完整 session 仍未公開，以上流程屬作者報告。
- 文章新增的量測包括 Sol 在 378m／594m 的特定速度翻車、30–50 km/h 完賽、80 枚金幣在每個完賽 run 全數取得、完賽後燃量至少 76%、低速停坡後耗油，以及 fixed 120 Hz 和多種自主 QA 描述。這些是作者直接操作 build 並讀取其程式狀態所得，沒有獨立重現。
- 一般 HTTP 檢查：OpenAI Showcase、GameDevBench、Sonnet FPS 線索頁、Sol／Opus builds、Sol／Opus screenshots 皆可載入。連結可達不會補足 Sonnet FPS 的原始 prompt、build 或 session 證據。

## 下一個搜尋方向

下一輪改查**公開模型盲測／同一完整任務的可玩交付集**：確認不同前沿模型是否已在固定同一規格、共同 agent/tool 條件下各自交付完整長流程遊戲；要求原任務、凍結首交 build／影片、明確人類介入記錄和逐維評分。避免再查已覆蓋的 Hill Climb family 與 GameDevBench；如果只找到短單關成果，列校準／副測或排除，不升格主測。
