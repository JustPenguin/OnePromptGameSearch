# S66 · VeltosGames 3D playable artifact 與來源查核

- **日期：**2026-10-07
- **搜尋方向：**新查 prompt-to-game 平台 VeltosGames 的近期 3D／高美術作品及公開 playable build，確認頁面能否證明原始任務、模型、一次委託與 frozen artifact。
- **開始前核對：**重讀 [研究索引](../../ai-game-one-shot-index.md)、[候選摘要](../../ai-game-one-shot-candidates.md)、[搜尋索引](index.md)，並查重 Veltos／Sky Isles 名稱及其官方 URL；目錄無既有記錄。避開已收錄的 PlaytestArena／Play2Code（B0032、S44）及 S62–65 方向。
- **實際查詢：**
  1. `AI generated game session trace source playable 3D 2026 author prompt coding agent game`
  2. `"game generation" prompt playable screenshot agent trajectory 3D coding agent 2026`
  3. `site:github.com "one-shot" game "Claude Code" prompt playable 3D 2026`
  4. `site:github.com game generation trace playable art coding model 2026 agent trajectory`
  5. `AI game creation benchmark prompt session trace 3D output no human intervention coding agent`
  6. `AI generated game 3D coding agent task prompt build screenshot autonomous session playable 2026`
  7. `Veltos AI games 3D prompt generated games VeltosGames`
- **檢視的一手來源：**[Veltos 官方首頁](https://www.veltos.ai/)（首頁將產品描述為 prompt-to-game，稱可從文字 prompt 產生 fully playable games／3D worlds）；[官方 VeltosGames 目錄](https://games.veltos.ai/)；[Sky Isles 作品頁](https://games.veltos.ai/game/sky-isles-YrAJJg0ggMUy)及其[HTML5 iframe build](https://dlys0ta9so5se.cloudfront.net/1171235bc6860a375df946cacfc2938d/games/chatid-d0e735bf29ed241e8ee95437426c4ff8/c242f9a81389ee243b3c4a4e24eb7659/index.html)；[Sky Isles 目錄縮圖](https://dlys0ta9so5se.cloudfront.net/1171235bc6860a375df946cacfc2938d/games/chatid-d0e735bf29ed241e8ee95437426c4ff8/c242f9a81389ee243b3c4a4e24eb7659/image.png)；[Flow Front](https://games.veltos.ai/game/flow-front-mAiiiruZW5tL)；[Evolve](https://games.veltos.ai/game/evolve-CZFPE0QPrrOF)。

## 查核結果

Veltos 首頁是產品能力自述；目錄提供可玩的具名作品與平台 metadata。抽查 Sky Isles、Flow Front、Evolve 的作品頁都回應 200。Sky Isles 頁 HTML 內有 iframe 直指 CloudFront 的遊戲 `index.html`；該 build HTML 回應 200，title 為 “Sky Isles — Tiny War Strategy”，import map 指向 Three.js 0.160。平台內嵌 metadata 將 Sky Isles 標示 `Pro_Game`、portrait/mobile、`bite` variant、`strategy`／`conquer` tags，時間欄為 2026-09-23／09-24。

公開資料沒有指明這些具名作品的原始 prompt、模型與版本、session trace、追加輸入、人工修改、來源 repo 或凍結版本。平台說明證明有 prompt-to-game 產品流程，不能替單件作品證明使用者只輸入一次。Sky Isles 的目錄縮圖看起來是明亮的低多邊形浮空島戰略畫面；它不是可核實的遊戲執行中截圖，不能據此給 gameplay art 判定。本次確認可載入 build endpoint，但沒有互動完整遊玩測試。

## 登錄、排除與未解問題

- 新增 [C0025](../records/C0025.md) 保存 VeltosGames 作品庫及來源限制。
- 新增 [G0275](../records/G0275.md) 保存 Sky Isles 公開 HTML5／Three.js build、可核 metadata、AI／one-shot provenance 缺口及待使用者評價的美術線索。此為平台作品參照，未列強候選。
- 其他平台與搜尋命中如 Veltos AI、Sorceress、EvoLink Kimi prompt collection、3DCodeBench 都沒有提供符合條件的單件完整遊戲 run。PlaytestArena／Play2Code 已由既有 B0032／S44 記錄，未重複建檔；EvoLink 頁面是 prompt 模板，不是 Kimi 實際輸出；3DCodeBench 測程序建模，非完整遊戲成品。
- 仍待查：Veltos 是否能公開特定遊戲的初始 prompt／模型與 build history；Sky Isles 實際遊玩時的畫面、完整玩法及 thumbnail 與 runtime 的關係；是否另有 model showcase 可供重跑。
- **計數：**S54 後第 12 個不同方向，未找到一次委託強候選，也未顯著提升既有案例的一次委託證據。這只更新暫時計數，不代表研究完成；Veltos 若出現可核 prompt/session，應沿 G0275 重查。
- **下一個方向：**改查近期大型模型官方 showcase／發布頁中可追溯到 coding session 或精確原始任務的 3D／stylized gameplay build，並逐一核對 build 的 AI 生成歸因與 gameplay 畫面，不再泛搜 prompt-to-game 作品庫。
