# 搜尋批次 S-20261006-05：新模型展示與完整 RPG 任務 brief

**日期：**2026-10-06（台北時間）  
**問題：**在近期模型與 showcase 中，是否有系統夠深、適合一次使用者委託且允許 AI 自主 QA 的新遊戲或原始任務？重點是找出可真實重跑的好題目；單一模型結果也可入選，多模型比較不是門檻。

## 實際搜尋與查閱

### 查詢

- `2026 "one prompt" "full game" "Opus 5.5" AI game 2026 playable RPG`
- `GPT-6 Astra one prompt game full playable 3D game demo 2026 game`
- `"playable" "single prompt" AI game 3D full level 2026 Claude Fable`
- `AI game created in one prompt "boss" "self play" 2026 game build`
- `2026 game "no follow-up" "one prompt" AI game build`
- `2026 "one prompt" "game" "no human intervention" Claude game playable`
- `2026 AI game "autonomous" "self-play" playable game Opus`
- `site:github.com AI game Opus 5.5 one prompt game playable autonomous test`
- `"Browser Flight Simulator with a Complete Flight Loop"`
- `"Three.js dark-fantasy action RPG" GPT-6 Astra prompt`
- `site:x.com "Starfox" "Opus 5.5" NOVA LANCER`
- 重讀與交叉核對 Diablo 任務頁、完整實測文章、Descente 原始 Reddit 貼文、GPT-6 Astra prompt 收藏庫及 Opus 5.5 三款 one-sentence 遊戲 repo；對名稱／source 執行本地目錄查重。

## 有價值且更新的記錄

### [G0049 · Diablo-style ARPG](../records/G0049.md) — 優先作共同重跑題

重查後拿到完整精確 prompt，而舊紀錄的「四層地城、掉落、Boss」過於簡短，容易看不出題目真正難度。新證據顯示：城鎮到四層程序地城與 Boss 的完整流程、迷霧、五種敵人差異、精英、三類以上技能、角色升級／屬性點／技能點、稀有度與詞綴、背包、裝備比較、商店、死亡懲罰、存檔，以及 AI 自動通關、修 bug、15–30 分鐘人類難度校準。相較只重視「生出 3D 畫面」，這是一個完成度與系統互相牽連的上限題。

同一頁保存 Opus 5.5、Fable 5.1、GPT-6 Astra、Sonnet 5.5 的真實 build 截圖及作者 run 的耗時／token／成本資料。但該頁標示至少 Sonnet 是 native app、沒有 web playable；文章指出 ARPG 屬早期輪次，未像後續 Backrooms 測試那樣明確保證無追問及不 rerun。因此它**適合用原 prompt 重跑**，不應說成已證實全部既有 build 可供玩家直接驗收。模型截圖可作畫面查看材料，不能代替 playable build 或使用者美術驗收。

來源：[精確 prompt 與 build 截圖](https://www.aiformortals.co/built-by-pat/build-a-diablo-style-action-rpg-5koom8) · [run 條件、goal mode 說明與 token／耗時資料](https://www.aiformortals.co/blog/sonnet-5-5)

### [G0196 · Descente](../records/G0196.md) — 高能力參照，嚴格條件排除

Opus 5.5 + Godot 4.7 的動作 roguelite；作者描述約 5 小時 48 分、15k GDScript + 3k Python、最多 800 名敵人、8 種敵人、兩隻小 Boss、三階段終 Boss、meta progression。AI 自建 Godot MCP 取錯誤／截圖／模擬按鍵，也寫 bot 跑超過 200 局；美術使用 3D 渲染逐格轉程序像素圖。**決定性不符點：**作者明說開發中途留言三、四次，其中要求把 bot 改得更像真人後模型又重調平衡，並先提供六張美術參考圖和詳細規格。系統 QA 與 asset pipeline 很有參考價值，但不是使用者所要「一次輸入後不再干預」的案例。

來源：[作者原始貼文與規格流程](https://www.reddit.com/r/ClaudeAI/comments/1wqo6o5/i_gave_claude_a_detailed_game_spec_and_let_it/)

### [G0197 · Three.js Dark-Fantasy Action RPG Prompt](../records/G0197.md) — 題目線索，不算已交付遊戲

GPT-6 Astra prompt 有清楚的 gothic ruin / forest 場景、騎士動作戰鬥、魔法、Boss、繁中 HUD 與完整遊戲流程，並要求持續測試和修正；但查到的主要材料是收藏庫中的 prompt 與靜態截圖，沒有 live playable、repo 或 run log。QA 是 prompt 中的要求，尚無證據證明該次實際完成。值得留題目，不升成品候選。

來源：[原始貼文](https://x.com/HiltonMisia/status/2096637091627364531) · [帶原帖及 prompt 的收藏庫](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts)

### [G0198 · Browser Flight Simulator with a Complete Flight Loop](../records/G0198.md) — 強副題 brief，證據待補

原帖 prompt 設計完整的起飛至降落閉環，並要求控制面、基本物理、成功／失敗 feedback、自動完整試飛和修錯。題目容易用一致性行為驗收，但範圍仍是單一短飛行挑戰，不能單獨測長流程遊戲上限。原作者資料只有靜態圖，沒有 live build 或 run log；後續頁面出現的 playable 標示未能連回這個 Astra run。

來源：[原始貼文](https://x.com/adxtyahq/status/2096236137266512181) · [prompt 保存副本](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts)

### [G0033 · Chainmate](../records/G0033.md) — 實際可玩、但明確有中途人工回饋

Opus 5.5 生成三幕／九場 3D chess roguelite；6×6 棋盤、敵方 AI、棋子永久死亡與升級、三個規則型 Boss、分支行程、商人／休息／事件、18 種 relic、保存進度；作者提供可玩的 itch.io 版。它的生成內容、畫面與 run 規模有參考價值，然而原始輸入是「build this game」加四張參考圖，作者再回饋燈光。這是一次啟動後 AI 大量自主工作，卻不符合「不再給 AI 任何中途指示」。既有目錄已登錄 G0033，故更新而不重複新增。

來源：[作者描述原始輸入、玩法及 short feedback](https://www.reddit.com/r/ClaudeAI/comments/1wp8uxb/i_gave_opus_55_four_reference_images_and_build/) · [playable build](https://sneid1.itch.io/chainmate)

### [G0199 · GPT-6 Astra Roblox Kart Racer](../records/G0199.md) — 高價值 brief，成品待補

單一 GPT-6 Astra prompt 聲稱約 30 分鐘生成 Roblox kart racer；brief 同時指定 Roblox Studio MCP、Blender／Three.js 資產、Luau runtime，要求完整賽道、AI 車手、倒數／圈數／結果／重開與實際 playtest、截圖和修 bug。文章核實作者貼出 prompt 和影片，也指出沒有公開 Roblox place 或 run log，不能驗證最後 playable 狀態與 30 分鐘說法。可當現行模型重跑的競速工具鏈 brief；不列既有成品。

來源：[brief 與 provenance 分析](https://bloxbot.ai/guide/gpt-6-astra-roblox-kart-racer-case-study) · [原作者影片貼文](https://x.com/givros/status/2096219700879331665) · [原作者 prompt 貼文](https://x.com/givros/status/2096219703282733430)

### [G0200 · PATCH Territory Capture](../records/G0200.md) — playable 已有，任務上限不足

Agent Games 的 GPT-6 Astra 遊戲有可玩版與公開 prompt，100,000 tokens、195 分鐘（平台列值）；其 bot、圈地、碰撞、排行榜和觸控輸入是可驗的中型街機任務，但主要玩法只有單一領地圈線循環，系統量不足以代表完整遊戲生成上限，因此僅保存為中型規則校準。

來源：[playable 頁與 prompt](https://agentgames.dev/play/patch)

### [G0201 · Call of Duty-Style Browser FPS Brief](../records/G0201.md) — 美術與系統重跑候選

這是本批重要的新發現。原 prompt 把高標 3D 角色與動畫、各自手感不同的武器、掩體 AI、killstreak、killcam、可進入的樓層地圖、完整比賽閉環、60fps 與最終多角度截圖檢查都列成驗收內容；可同時測畫面品質及功能系統是否真連動。原測試公開 GPT-6 Astra、Fable 5.1 真實 build 截圖，但原文明說此 FPS 題是三項測試中唯一有 follow-up passes 的任務。結論是「spec 特別值得用現行模型嚴格 one-shot 重跑」，不是「已有兩個符合條件的 one-shot 成品」。圖片連結指向作者頁上的實際模型 build output，尚未由使用者判定美術合格，也未確定可遊玩 demo 可直接公開取得。

來源：[原始任務、prompt、build 圖及執行描述](https://www.aiformortals.co/blog/gpt-6-astra-vs-fable-5-1) · [GPT-6 Astra 實際輸出截圖](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/fps-nuketown-gpt-astra.jpg) · [Fable 5.1 實際輸出截圖](https://uzgqbjufkfadoprvamcs.supabase.co/storage/v1/object/public/simmonsbench/shots/fps-nuketown-fable-5-1.jpg)

## 本輪發現但未升級的新展示集合

- **GPT-6 Astra game prompts：**查到由社群整理、標稱數百個 preview-backed 案例和約 20 多個 game showcase 的索引。可快速發現題目與原帖，但其 prompt / screenshot 收錄不代表每項有可玩 build；目錄裡的「recipes」自己標為 draft，也沒有獨立重現。採逐項回到作者原帖與 runnable result 的方式，不把收藏庫總數當作品質證據。
- **Opus 5.5 三款 one-sentence 3D game repo：**repo 聲稱三個遊戲各自從一句話、一個自主 session、無人工改碼完成，並公開 source 與 live demos；遊戲是單車、運輸船 FPS 和甩尾賽車。這延續既有 [G0035/G0164/相關 Opus demo](../catalog.html) 的證據線索，但就可見玩法範圍而言多屬單場景／短循環，不比現有 Ruinseed、MALL ACTION、Fall Line、Diablo brief 等更適合作為完整上限主題。保留作單句開放式 prompt benchmark，不搶主候選位置。
- **GPT-6 Astra browser GTA 測試：**查到單 prompt 產生的小範圍可玩原型，但現有公開描述只到數個街區的 prototype；與已登錄 Fable Theft Auto、Grand Theft Astro 比較，沒有帶來更清楚的任務深度／自我驗收證據。
- **GPT-6 Astra WoW / Portal agent run：**近期報導涉及 agent 玩既有商業遊戲的自動操控與長時推理，不是 AI 從一次委託生成新遊戲，因此不納入本研究主問題。

## 無結果與排除條件

- 對 `GPT-6 Astra one prompt game full playable 3D game demo` 的搜尋常見 coin collection、scene builder、短 prototype、遊戲素材或長期迭代專案；單有 3D 或「一次 prompt」標題不足以升級。
- `Descente` 是本次最明確「系統與自動測試很強，但中途有人介入」案例；不以「未改程式碼」偷換成無使用者指示。
- 新見《Chainmate》是很值得看的 playable 3D roguelite，但作者公開承認有四張 reference images 和燈光回饋；新見 Roblox kart brief 技術範圍扎實，尚無可驗證 playable；PATCH 可玩但玩法太窄。
- CoD-style browser FPS 的模型 build 有後續 passes，因此不符合一次交件實驗；但原任務對 rigged characters、animations、gunplay、AI、killcam、完整 match 和自我截圖檢查的要求，是目前找到最對應「美術不能太低階」且保有功能難度的重跑題之一。
- Flight Simulator 的 prompt 要求模型自測不是 run 已自測的獨立證據；dark-fantasy RPG 的精美預覽不是 playable build。
- 最新型號與已發布 build 分開處理：好舊題可由最新模型重跑；新型號 demo 若任務太小，仍不必塞進主測。

## 下一次重查條件

1. Diablo prompt 若出現 playable build／原始 session 或一個更接近當前模型的新跑次，確認是否完全無追問、保存凍結版本和實際畫面。
2. G0197 / G0198 作者若提供自己執行的 build、run log 或可驗證的工作階段，補核實；若沒有，不反覆搜尋同一份策展清單。
3. 遇到更近期模型案例時只追加能明確回答「原始委託是什麼、途中有無人類訊息、AI 停止時交了什麼、是否可直接玩、實際 QA 了什麼」的新證據。
