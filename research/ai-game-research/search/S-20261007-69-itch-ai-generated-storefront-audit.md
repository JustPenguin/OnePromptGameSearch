# S69 · itch.io AI Generated 標籤與近期 3D storefront 核查

- **日期：**2026-10-07
- **搜尋方向：**從 itch.io storefront 的 AI Generated／3D 標籤瀏覽近期 playable/downloadable 遊戲，確認是否有可追溯到單次 AI game-development task 的成品，並特別找高視覺 3D output。
- **開始前核對：**重讀研究索引、候選摘要、搜尋索引；查重本批發現的 AetherionCraft，無既有紀錄。
- **實際 storefront filter URL：**
  1. `https://itch.io/games/newest/tag-ai-generated`
  2. `https://itch.io/games/newest/tag-3d/tag-ai-generated`
  3. `https://itch.io/games/tag-ai-generated`
  4. `https://itch.io/games/tag-ai`
- **逐項查閱：**[itch AI Generated 最新頁](https://itch.io/games/newest/tag-ai-generated)、[熱門 AI Generated tag 頁](https://itch.io/games/tag-ai-generated)、[近期 3D／AI Generated 篩選頁](https://itch.io/games/newest/tag-3d/tag-ai-generated)、[AetherionCraft 開發者頁](https://yorudan210.itch.io/aetherioncraft)。

## 結果

itch 頁面把 AI Generated 定義為「generated or edited through generative AI」，可包含 AI 敘事與 NPC，不等於遊戲本身由 coding agent 從單一任務生成。熱門 tag 頁回報 87,334 個 results；最新頁展示的項目包括 AetherionCraft、Shinobi Saga、Rikochet、Doctrine、Cosecha Perdida 等，tag 沒有表示 AI 貢獻位於程式碼、素材、對話或 NPC 中，也沒有一次委託／session 欄位。

逐看 AetherionCraft 頁面：它是 Windows downloadable voxel survival/exploration game，介紹含無限隨機方塊世界、農業、建造、洞穴／礦物、boss 與 zombies；頁面沒有可核的 AI coding/model/prompt/session/build provenance，也沒有 one-shot disclosure。只因 storefront AI Generated tag 不足以當作 AI coding agent 成品，亦不能由精美商品圖推定 gameplay art 是 AI output。按證據規則不建遊戲紀錄。

3D＋AI Generated 最新篩選頁返回 Cloudflare「Just a moment」challenge（HTTP 200，約 6 KB challenge HTML），不能拿它判斷沒有 3D 候選；停止重試 challenge，改以可讀一般 tag 頁與具名頁核驗。搜尋引擎沒有提供可用站內資料源。這是可記錄的覆蓋限制，不是已完整盤點所有 3D tag entries。

## 判斷與下一步

- 本方向沒有新增 AI 一次委託遊戲候選，也沒有大幅補強現有紀錄；AI Generated tag 的範圍太寬，不能代替逐作品查作者 AI disclosure、原始任務與 playable build。
- **計數：**S54 後第 15 個不同無增益方向；研究仍持續。保留 Cloudflare 限制，未將暫時看不到的 3D entries 標成「無案例」。
- **下一方向：**改查 GitHub Pages／可下載一手模型 build 的版本歷史和單次輸出對照，優先選已有明確遊戲專案來源的 AI-created game archives，核對頁面上的 build 是否對應 repo 中保存的原始輸出／prompt。
