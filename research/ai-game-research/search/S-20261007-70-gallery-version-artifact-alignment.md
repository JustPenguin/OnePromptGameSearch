# S70 · 公開遊戲作品集的版本歷史與 prompt／成品對照

- **日期：**2026-10-07
- **搜尋方向：**核對公開 AI 遊戲作品集新入庫的候選：版本歷史、模型歸因、原始 prompt／session、可玩頁與實際 build 是否能相互對上；特別檢視有高系統密度或 3D 美術流程的作品。
- **開始前核對：**本批前已重讀研究索引、精選候選摘要、搜尋索引，並用 `manage.py lookup` 查 AgentsLoop；C0003 已存在，故補充其版本差異而不另建目錄項。
- **實際查詢：**GitHub repository search `awesome AI built games`、`AI generated games prompt playable source GitHub Pages`、`one prompt model generated game artifacts`；另查 GitHub API `AgentsLoop/awesome-opus-5.5-games` commits 與 `games.json`、GitHub repository trees／README／設計文件／commit source、直接抓取 MUTE GitHub Pages app shell 與 Claude session/snapshot 路徑。
- **查閱來源：**[AgentsLoop repo](https://github.com/AgentsLoop/awesome-opus-5.5-games)、[新增批次 commit 7839811](https://github.com/AgentsLoop/awesome-opus-5.5-games/commit/7839811da5cc)、[gallery follow-up dd786c1](https://github.com/AgentsLoop/awesome-opus-5.5-games/commit/dd786c160f3a)、[MUTE repo](https://github.com/dippy34/Ai-vr-game)、[MUTE scaffold attribution commit](https://github.com/dippy34/Ai-vr-game/commit/cbd6dd0b0345775604a404ca3e880d35d13a9637)、[MUTE design](https://github.com/dippy34/Ai-vr-game/blob/claude/vigilant-gates-rfgepm/docs/DESIGN.md)、[MUTE art pipeline](https://github.com/dippy34/Ai-vr-game/blob/claude/vigilant-gates-rfgepm/art/README.md)、[MUTE art gallery](https://github.com/dippy34/Ai-vr-game/blob/claude/vigilant-gates-rfgepm/art/GALLERY.md)、[MUTE deployed page](https://dippy34.github.io/Ai-vr-game/)、[DEAD AIR repo](https://github.com/PieterMey/theboys)、[DEAD AIR attribution commit](https://github.com/PieterMey/theboys/commit/d4cb042d9493e086084858afff54c92b2de2d79c)、[DEAD AIR plan](https://github.com/PieterMey/theboys/blob/main/PLAN.md)。

## 版本及作品對照

- AgentsLoop 項目 2026-10-07 兩個新 commit：`7839811da5cc` 宣稱新增 37 game units／34 repos；`dd786c160f3a` 加入 Mindblown 生成器／gallery。API 讀到當前 `games.json` 727 筆；C0003 舊段落約 909 units／611 repositories 是先前 README 的另一種快照／計數邊界，不能視為相同分母。列表是策展發現入口，不等於有公開 prompt、原始 session、可玩 build 或視覺審查。
- **MUTE：**catalog 條目顯示 Claude Opus 5.5、source、無原始 prompt、無 screenshot URL。repo 可查 README／設計、完整 Blender 5.0.1 scripted asset pipeline 和 previews；初始 commit attribution 帶 Claude session URL，但頁面僅 app shell、snapshot API 無效 UUID／metadata 404，未取回 transcript。直接請求 GitHub Pages 得到標題 MUTE、Three.js JS/CSS bundle 和 canvas app mount point，代表部署 app 確實存在；本批未開瀏覽器、未完成進場或遊玩。新增 G0278，當作高系統／美術流程參照，藝術待使用者評價，one-shot 未確認。
- **DEAD AIR：**catalog 新增 Claude Opus 5.5 歸因與 co-op proximity voice horror；repo plan/design 與 58 playtest fix 記錄可查，但無 prompt、session、live demo 或 screenshot。新增 G0279 作為長程多人及 QA 題型，明確排除 one-shot 成績與視覺評價。
- **排除／去重：**Turbo Kart Rally 已在 G0164，不重複新增；Dawnmark、Catan 及其他新增條目未提供足以核對單次 task/build/人工介入的原始證據，本批不湊入個案；Mindblown 是 model-undisclosed gallery/generator，只有單一 lofi-bird 範例且無 source export／完整 provenance，留 catalog context，不當成單次遊戲 run。BoK16-9HD 是依賴原版 proprietary game files 的 partial engine remake，非完整交付。

## 結論與未查證事項

- 沒有新強 one-shot 完整遊戲候選，也沒有顯著提升既有案例的一次委託證據；此為 S54 後**第 16 個不同無增益方向**。不因公開作品集新增數量或目測開發活躍度而推定能力。
- MUTE 的實際遊戲畫面／品質、初始 prompt、session 和人類修改 timeline 尚待查；DEAD AIR 的 live build、真實畫面及 prompt/session 也未找到。若作者公開有效 session 或可比對凍結 build，再重查。
- **下一方向：**轉查近期第一手 AI coding agent 影片／run artifacts 中的高美術 playable build；優先追取得到原始 prompt、session 日期、輸出 build 與可直接檢視遊玩畫面的案例，避開單純 storefront tag／二手 gallery。
