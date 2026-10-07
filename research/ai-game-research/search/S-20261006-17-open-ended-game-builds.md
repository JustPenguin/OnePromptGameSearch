# 搜尋批次 S-20261006-17：低約束開放委託與近期可玩建置

**日期：**2026-10-06（台北時間）  
**研究問題：**從近期 AI 遊戲作品庫與作者公開任務中，找低約束創作、完整長流程或高跨系統密度的可玩 build；優先保留有原始 prompt、模型資訊及自行測試說明的候選，同時核實目前版本是否被後續指示／更新污染。

## 查重與方向

先讀 [S16](S-20261006-16-autonomous-artifact-gallery-audit.md)、全目錄及歷史索引。查詢 Agent Games 作品庫後，逐項讀 FROM ZERO、DEAD AHEAD、Tank Rush、Neon Serpent 3D 等作者頁；重查既有的 BioNeural、Crowd Rush、Ink Field、TOKYO DRIFT，確認新證據是否改變分類。未重建已存在的 G0026、G0042、G0079、G0186。

## 實際搜尋與查閱

| 實際 query／網址 | 發現、證據與判斷 | 關聯項目 | 待查／重查條件 |
|---|---|---|---|
| `site:agentgames.dev/play "Fable 5.1" "prompt" game`；[FROM ZERO](https://agentgames.dev/play/from-zero) | 新建 **G0221**。頁面公開極短開放 prompt、Fable 5.1／High、作者申報 3.08M tokens／337 分鐘、目前 1.6 browser build；玩法有八分鐘固定 seed 日循環、死亡狀態保留／遺失、三個首領及 roguelite 成長；作者說以 headless Chrome 自動模擬並截圖。prompt 說「another game」及「fifth or sixth」，所以原始上下文可能非空；無 transcript、初版快照、hash；Agent Games 說上傳者自行填流程資料。定為高價值創作自主性重跑題，不把現版當已核實原始 one-shot；美術須用實際 build 由使用者判斷。 | [G0221](../records/G0221.md) | 取得模型工作區／完整 run trace 和 v1.0 快照；或把公開 prompt 在乾淨工作區重跑。 |
| `site:agentgames.dev/play "Opus 5.5" multiplayer destructible`；[Reddit 原始委託](https://www.reddit.com/r/ChatGPT/comments/1wqd0gg/houston_we_have_a_problem_opus_55/)；[BIONEURAL 現行站](https://bioneural.de/) | 更新 **G0026**。作者原文列單次極寬鬆委託，玩法、圖像資產與完整遊戲由模型決定；自述 Opus 5.5 Medium、單一 5 小時 session、AI 自行用本機工具測試並部署，後補列 Blender 5.2、Unreal 5、PHP、Node、FileZilla、Suno、Cloudflare、WebRTC 等。站點 patch notes 顯示 1.0 launch 9/26；目前 1.8（10/04）經過八次版本變更；作者曾額外要求手機支援，並加入 5v5、clans、shop 等後續功能。可重跑作「開放選題＋多人整合＋部署」壓力任務，但模型、主機、訂閱和登入工具環境不等價，現版不能當第一輪 build。 | [G0026](../records/G0026.md) | 若取得 v1.0 frozen build 或 transcript，核實第一輪範圍和介入次序；比較時統一服務／帳號／工具環境。 |
| `"DEAD AHEAD" "Fable 5.1" game prompt`；[DEAD AHEAD](https://agentgames.dev/play/dead-ahead) | 新建 **G0223**。Fable 5.1／Max，作者申報 10.07M tokens、415 分鐘，公開 prompt、v1.7 可玩版與完整說明。跨系統閉環為剛體車輛物理、燃料／碰撞、固定 seed 3127 英尺路線、三車及六升級線、日循環收入／逃脫條件；頁面描述 Node bot 自行玩完整經濟流程，發現並修正火箭穿牆與坦克卡住等問題。沒有 transcript 或 frozen first build，確認為強重跑 brief，流程只列作者申報。 | [G0223](../records/G0223.md) | 取得首次 build／trace；重跑要驗完整通關、升級及失敗後經濟循環。美術尚待使用者評閱。 |
| `site:agentgames.dev/play "long play-test loop" tank shooter`；[Tank Rush](https://agentgames.dev/play/tank-rush) | 新建 **G0224**。Fable 5.1／Max，作者申報 101K tokens、169 分鐘，現版 1.27 並公開 prompt。29 個生成關卡、六武器、四升級線、戰利品階段、持續升級後控難度；作者描述 pathfinding、crowd separation、瞄準及經濟的長 play-test loop。系統題比普通 arcade 有分量，但規模低於主要長流程候選，作者敘述也未證明沒有人工跟進，列重跑備選。 | [G0224](../records/G0224.md) | 取得 trace 或一次任務的明確證言；若擴充多種關卡／角色或團隊戰等系統，再升級範圍評估。 |
| `site:agentgames.dev/play "Neon Serpent 3D" Opus 5.5`；[Neon Serpent 3D](https://agentgames.dev/play/neon-serpent-3d) | 新建 **G0222** 排除紀錄。頁面稱 Opus 5.5／Low 並可玩，但作者未公開 prompt；核心仍為蛇遊戲單一街機迴圈，不足以測完整遊戲上限。 | [G0222](../records/G0222.md) | 只有公開更大任務／多階段系統時重查。 |
| `site:agentgames.dev/play "Crowd Rush" GPT-6.1 Sol`；[Crowd Rush](https://agentgames.dev/play/crowd-rush) | 更新搜尋脈絡而非另建紀錄。既有 **G0042** 已確認公開 prompt 是修訂指令，要求保留已完成的 30 關戰役、裝備、商店等，並非首輪任務；不列一次輸出。 | [G0042](../records/G0042.md) | 取得 blank-workspace 原始 prompt、trace 或未修訂 build 後重核。 |
| `site:agentgames.dev/play "one prompt" "one hour" Ink Field`；[Ink Field 作者貼文與影片](https://www.reddit.com/r/ClaudeAI/comments/1wnzcbg/i_gave_opus_55_one_prompt_and_one_hour_to_make_a_game_then_actually_played_the_thing/) | 既有 **G0079** 有過程更正：作者先收到模型方案，再另發指示讓它開始建置；缺 exact prompt、source／可玩首版。雖有作者通關評論和視覺影片，不符合零後續指示；不重複造紀錄。 | [G0079](../records/G0079.md) | 若公開原始兩則對話、source／frozen build，可更新證據，但流程仍不符嚴格一次委託。 |
| `site:agentgames.dev/play "TOKYO DRIFT" Fable 5.1 prompt`；[TOKYO DRIFT](https://agentgames.dev/play/touge) | 既有 **G0186** 已有 prompt 和現版。新頁面說明現版 4.30（10/02 更新），44.46M tokens、5592 分鐘、約 $453 自報；任務與成品確實有高系統／視覺企圖，但如此長的持續建置及版本更新不能當一次交付。現有記錄已列流程待核，不升級。 | [G0186](../records/G0186.md) | 有 frozen initial build／session trace 才能驗證 one-shot；當前 build可供使用者美術檢閱。 |
| `site:agentgames.dev/play "GPT-6.1 Sol" newest games game`；[Agent Games 最新作品索引](https://agentgames.dev/?sort=new) | 發現 GPT-6.1 Sol 的 Sector Zero、Afterlight、Crowd Rush 等新列項。Afterlight 已是 G0211；Crowd Rush 是 G0042；Sector Zero 無足夠可讀原始 prompt／作者成品細節，需另一輪直接查清。本輪未把「new」標籤當作品質或一次委託證明。 | [G0211](../records/G0211.md)、[G0042](../records/G0042.md) | 下輪查 Sector Zero 與 Oct 1 之後的新 AI game runs，優先原始 prompt、可玩 build 和 session 記錄。 |

## 本輪結論與文件更新

- 本批新增 G0221（FROM ZERO）、G0222（Neon Serpent 3D，排除）、G0223（DEAD AHEAD）、G0224（Tank Rush）；更新既有 G0026（BioNeural）的原始 prompt、1.0 功能與後續 1.8 patch 區隔。
- 最值得拿新模型重跑的兩種新題：**BioNeural** 測開放選題／多人跨系統／工具與發布部署，需嚴格統一工具帳號環境；**DEAD AHEAD** 測物理／成長／經濟／長期 bot QA，較容易固定測試環境。**FROM ZERO** 測純創作自主性，但原 task context 可能有前史；**Tank Rush** 是較窄的戰鬥平衡副題。
- 除 Agent Games 自動安全檢查／人工上架外，來源頁不等於 AI 來源及無人工介入的獨立稽核；現版網站遊戲也不是凍結初版。所有建置時間／token 成本都標為作者申報。
- **尚未由研究方檢查各 playable 的美術品質，均不預判通過。**直接開遊戲由使用者檢視；封面或文字介紹不當成 gameplay 畫面。

## 下一輪方向

1. 直接追 Agent Games 中 GPT-6.1 Sol 的新遊戲 Sector Zero、Afterlight 同期作品，找有更強任務原文與可驗證原始 run 的案例；對已有目錄的遊戲更新證據，不重建紀錄。
2. 轉到實際公開 session／社群 run trace 的新近一鍵生成場景，找 physics、strategy、simulator 類高系統題，不限一個平台。
3. 找 FIRST BUILD 或 gameplay 錄影／repo 可以分辨交付時間點的多版本作品，避免把長期演進版本算成首次輸出。
