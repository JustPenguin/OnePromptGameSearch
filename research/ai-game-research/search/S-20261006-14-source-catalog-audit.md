# 搜尋批次 S-20261006-14：來源型遊戲目錄與高視覺 3D 成品覆核

**日期：**2026-10-06（台北時間）  
**研究問題：**在近期 source-backed 遊戲目錄、作者原始 repo 與新模型公開作品中，是否有具真實 gameplay 證據、足夠跨系統深度且美術有檢視價值的新候選；並追查 Sunward 等未入台帳線索。

## 開始前查重

開始前查閱研究索引、候選名錄、S13 搜尋批次、全目錄及搜尋歷史。已知賽車題包括 Kart Blitz、Turbo Kart Rally、QQ Speed、NEON BAY；不重複建項。以名稱、作者／repo URL 查詢 Sunward、SUNBREAK、HEADQUARTERS、Street Heat、The Simpsons: Hit & Run、Opus town-defense RPG 均無現行紀錄。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `site:github.com/yjrocks712/Sunward-by-GPT-6-Astra Sunward GPT-6 Astra Unity one prompt`; `"Sunward" "GPT-6 Astra" game one hour Unity`; [canonical repo](https://github.com/yjrocks712/Sunward-by-GPT-6-Astra); [v0.1.0 release](https://github.com/yjrocks712/Sunward-by-GPT-6-Astra/releases/tag/v0.1.0); [社群 gameplay 記錄](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/games/sunward/readme.md) | 核實 10.34 km 島嶼、三條賽道、AI rivals／60 traffic、四車、garage、存檔、後加 radio／photo mode／testing；提供 Unity source 與 Apple Silicon Mac build。作者稱互動式 Codex 開發、首版約一小時，沒 prompt/transcript/no-follow-up 證據。實際圖可看 README 的 driving/photo-mode；策展者手動畫面評分 7.8，非使用者判定。 | [G0213](../records/G0213.md) | 作者釋出原始對話、prompt、凍結首版或 no-follow-up 證據時重查。作開放世界賽車 brief 種子，不列嚴格成績。 |
| `"SUNBREAK — Downhill Club" github`; `Imirushik SUNBREAK Downhill Club GPT-6 Astra model evidence prompt`; [canonical repo](https://github.com/Imirushik/sunbreak-downhill-3D-game); [作者模型證據貼文 1](https://x.com/Im_IrushiK/status/2096280064019353891); [作者貼文 2](https://x.com/Im_IrushiK/status/2096291038172455124); [策展者實際畫面與證據記錄](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/games/sunbreak-downhill-club/readme.md); [非官方可玩複本說明](https://tikgame.org/game/sunbreak/) | 找到完整 2.3 km BMX 競賽、4 車手／3 AI、技巧物理、程序侵蝕山地、cel-shading、雨霧特效、ghost/replay、10 項 gameplay/effects checks；repo source 可查且模型歸因有作者原始貼文。官方沒有 hosted build，第三方 tikgame 自行從 source 建置副本。策展者人工截圖評 8.9，但不是使用者評分。原 prompt/no-follow-up 缺失。 | [G0214](../records/G0214.md)、[G0164](../records/G0164.md)、[G0014](../records/G0014.md) | 若取得原 prompt/session 或作者正式 playable 部署，重查一次委託資格；先供使用者看作視覺／物理副測，避免與現有 kart 題重複定位。 |
| `site:github.com "GPT-6.1 Sol" game created "October" 2026 playable`; `site:github.com/AgentsLoop/awesome-gpt-astra-games/games/ "GPT-6.1 Sol" "2026-10-03"`; [近期 source-backed catalog](https://github.com/AgentsLoop/awesome-gpt-astra-games) | 目錄截至 10/04 收入 Space Attack、ORBITAL 等 10/03 建立的 Sol repo，但 repository creation date 不證明發布日期，第一輪摘要未見具足夠任務深度、prompt 與實際結果的新強候選。目錄可作發現索引，需逐作回到原 repo 核實。 | [G0211](../records/G0211.md)、[G0207](../records/G0207.md) | 後續針對 Space Attack／ORBITAL 讀原始 repo、model source 與真實畫面；有完整 brief／QA 證據再決定是否登錄。目前僅搜尋層級篩選，不宣稱已審完該目錄全部作品。 |
| `"GPT-6.1 Sol" "game" "playable" one prompt October 2026`; [GamesByAI 比較文章](https://gamesbyai.win/compare/claude-code-vs-codex-for-game-development/) | 找到 VOID PULSE（GPT-6.1 Sol）與 PRISMFALL（Opus 5.5）的同題比較。2026-10-01 固定 neon arena survival 題，三輪 build→收到同一 seeded bot 的 playtest screenshot→polish；Codex 約一小時、Claude 約 20 分鐘（另有兩次輸出 token limit 空跑）。作者也指出 tool access 不同。 | — | 不列一次交付候選：有明確人類／外部 screenshot 回饋與三輪迭代，且單 arena 生存 loop 範圍偏窄。可供日後借用三輪迭代評測方法，不與使用者 zero-follow-up 協定混算。 |
| `"GPT-6 Astra" "game" "prompt" Codex 2026`; [HEADQUARTERS case study](https://futureproofagents.com/blog/game-design-case-study-gpt-6-astra/) | 六章 run-and-gun、四角色、56 敵人、12 Boss、110 自動測試；但作者先寫 141 KB design bible，後加故事 PDF，並有六輪 feedback，約 12 小時才有 first playable。文章有實際截圖，無公開 playable build。 | [G0215](../records/G0215.md) | 清楚排除一次任務；可參考長流程題的分層設計與 feedback-as-tests，不再追為嚴格候選。 |
| `"Claude Opus 5.5" game "one prompt" playable`; Reddit 相關線索 [作者貼文](https://www.reddit.com/r/ChatGPT/comments/1wro1ka/another_game_one_shot_by_opus_55/) | 作者稱約一小時，以數張參考圖與逐字 brief 做未命名 town-defense RPG；有職業選擇／自訂／成長及「讓城鎮亮到黎明」目標，提供預覽。沒專名、repo、build、playable 或完整 transcript。 | [G0218](../records/G0218.md) | 只保留重跑題型；有 playable/source 或作者公開 session 再升級。 |
| `"Street Heat" "GPT-6 Astra" game`; `"Street Heat" "single prompt" Astra arcade racer`; `site:x.com "Street Heat" "GPT-6 Astra" game` | 看到街機漂移、combo、near-miss、nitro、traffic 的轉述頁，但原始 X 貼文無法直接開啟；沒有找到 prompt/source/playable build。轉述頁非逐字原文。 | [G0216](../records/G0216.md) | 等作者原始貼文或可驗成品出現才重查；目前排除，不再重試泛用 Street Heat 搜尋詞。 |
| `"The Simpsons: Hit & Run" "GPT-6 Astra" browser reconstruction repo`; [作者 repo](https://github.com/Vheissu/hit-and-run-web); [轉述文章](https://arkade.com.br/the-simpsons-hit-run-agora-roda-direto-do-navegador-e-voce-pode-visitar-springfield-agora-mesmo/) | repo 和文章可查 browser rebuild、原 PS2 盤資產轉換／復用、七種關卡、駕車／步行／任務／追捕與模型 attribution；作者表示修過路牌、選單和 cutscenes，且 full-playthrough 尚持續。 | [G0217](../records/G0217.md) | 排除空白專案的一次委託；仍可作移植／資產處理題。無需再搜同標題，除非有明確獨立新創建版本。 |
| AgentsLoop source-backed catalog 內之 [SUNBREAK screenshot note](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/games/sunbreak-downhill-club/readme.md)、[Sunward screenshot note](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/games/sunward/readme.md) | 逐項查了圖片來源、手動評分與 model evidence；把 curator visual score 明確降為第三方印象，不視作玩法測試或 Jeff 的美術認可。 | [G0213](../records/G0213.md)、[G0214](../records/G0214.md) | 未新增模型排名。美術最終仍由使用者看 gameplay 判斷。 |

## 結論與更新去向

- 新增 G0214 SUNBREAK 為實際畫面與系統深度值得一看的視覺／物理副測；任務確切一次輸入流程尚無證據。它不取代 Ruinseed、FALL LINE 等長流程候選。
- 新增 G0213 Sunward 作為賽車題型參照但排除 strict one-shot；公開現版含明確後續加工，作者自述畫面仍有改進空間。
- G0215 HEADQUARTERS、G0217 Simpsons reconstruction 因大量人類設計／回饋或既有資產依賴而排除。G0216 Street Heat 因二手描述且缺成品／原始 prompt 排除。G0218 town-defense RPG 僅作待核 brief 線索。
- 新查 GamesByAI VOID PULSE／PRISMFALL 比較；它有外部 screenshot feedback 和三輪迭代，與目標協定不符，且題型小，不列強候選。
- 已新增 G0213–G0218，將 G0214 放入精選候選的視覺／物理副測段，並於 HTML 顯示作者 repo 的真實遊戲畫面、第三方遊玩鏡像和證據限制。最新 Sol repo 清單尚未逐一完成審核，保留為下輪方向。

## 下一輪方向

1. 直接逐項核查 GPT-6.1 Sol 新 repo Space Attack、ORBITAL：先看原始 game loop、可玩截圖／build、模型與任務證據；若只是短 arcade loop 則在下一 batch 留下排除原因。
2. 在 source-backed 目錄以更高美術截圖分層（如 Turbo Kart Rally、Neural Sight、SUNBREAK）找真實 gameplay；避免將策展分數直接套作使用者審美。
3. 找能公開 original prompt／session trace 的現行模型較大體量作品；不重做泛用 "one prompt game" 查詢，除非日期／model roster 已更新。
