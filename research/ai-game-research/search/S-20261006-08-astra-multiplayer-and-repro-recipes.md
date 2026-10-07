# 搜尋批次 S-20261006-08：GPT-6 Astra 多人遊戲與可重現任務

**日期：**2026-10-06（台北時間）  
**研究問題：**新近模型是否已有「一則任務、可檢查執行紀錄、真實多人系統／多種武器、實際成品錄影」的成品？同時查是否有可重跑的高難度遊戲規格和正式驗收清單。

## 開始前查重

查閱研究索引、candidate shortlist、整合目錄與搜尋索引，新增檢查了「Smash Karts Arena」「GPT-6 Astra Smash Karts」及其 Hugging Face dataset URL，沒有同名紀錄。既有 G0080 Kart Blitz 是 Sonnet 5.5 的 8 賽道競速；新案是 GPT-6 Astra 的 3D 武器競技＋服務端多人遊戲，題目系統不同，不合併。S07 已查最新 Opus 5.5 source repo，本輪改查 GPT-6 Astra，並從原始 game task repos 找可重跑的標準化 brief。

## 實際搜尋與查閱

| 搜尋式／來源 | 結果與驗證 | 去向／重查條件 |
|---|---|---|
| `"GPT-6 Astra" "one prompt" game playable 3D GitHub September 2026`、`"source-verified" "one-shot" Opus 5.5 games game repo prompt`、`site:github.com/amsminn/gpt-6-astra-smash-karts trailer screenshot gameplay`、`"GPT-6 Astra × Smash Karts" playable build screenshots 8 players`、`amsminn smash-karts multiplayer trajectory Codex exact prompt` | 找到 GPT-6 Astra Smash Karts Arena。官方 repo 寫明 model ID、Codex CLI 版本、2026-09-05 核心單 session 約 42 分鐘，公開逐字任務、完整 source、本機 run 指南、YouTube 實玩影片及 Hugging Face trajectory JSONL。直接 stream 並解析 6.4 MB trajectory：385 records，訊息角色中只有 1 則實際遊戲任務 user message；另 1 則 user event 只是環境 context。主 session 含一個 subagent spawn，但 child transcript 不在公開包中。影片是實際玩 bot 模式，並非可直接點開的多人 hosted build。 | 新增 [G0206](../records/G0206.md)；列強備選。若作者補 child transcript／hosted build、遊戲被獨立 playtest，或更新模型重跑時補記。 |
| [Smash Karts source](https://github.com/amsminn/gpt-6-astra-smash-karts)；[trajectory](https://huggingface.co/datasets/amsminn/smash-karts-multiplayer-trajectory/blob/main/traces/rollout-2026-09-05T17-40-19-01a070b9-c9b8-7d00-8cbf-8fd0416df521.jsonl)；[gameplay video](https://youtu.be/3laRe_z_gbI) | README 列 8 人房間／invite link、11 款武器、三分鐘對戰、bot 練習、server-authoritative simulation、断線恢復、鍵盤觸控和 Discord Activity。23 個 tests 涵蓋 WebSocket rooms、同步、重連、武器／道具、碰撞與回合計時；這是作者提供的測試結果，不替代獨立遊玩與畫面評估。title art 是作者稱分開生成，遊戲場景／車／武器效果程式生成。沒有公開 hosted playable URL，需本機 `npm run setup`／`npm run dev`，多人要部署自己的 server。 | G0206 將評測用途定為線上狀態一致性、房間／重連、武器系統和端到端閉環；評分時分開計算本機 bot 與真正多人客戶端。 |
| `site:github.com "GPT-6 Astra" "one prompt" "full game" model 2026 recipes benchmark`、[Awesome GPT-6 Astra game prompts](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts) | 找到社群 case + recipe 集：363 公開社群案例（collection 自述）和 26 份可重跑 recipe；recipe 固定 model release date/settings/input/acceptance。明確標成 draft 且未獨立重現；不是 26 份已驗證的 generated game。完整題有 advanced voxel sandbox、marble physics platformer、FPS explorer 等。 | 新增 [B0045](../records/B0045.md) 當標準化題目設計參考。當有 recipe 被現行 frontier model 跑出公開 build 與可追溯結果時再獨立新增／更新遊戲紀錄。 |
| [Voxel Sandbox full-game prompt](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts/blob/main/prompts/full-games/astra-3d-005-voxel-sandbox.md)；`GPT-6 Astra voxel sandbox prompt greedy meshing recipe` | 詳查一份 advanced recipe：128×128 seeded world、改動只 remesh affected chunks、greedy meshing、raycast／block placement、FPS、memory leak checks；附固定 seed／依賴／run checklist／failure modes。recipe 目標模型寫為 2026-09-03 Astra，狀態 draft，尚未被獨立重跑。任務有工程深度，但其單檔＋短 output budget 限制不能冒充完整長流程遊戲測試。 | 收入 B0045 作固定規格方法參考；未當成成品候選，等待實際跑出可玩 build 再評。 |
| [GPT-6 Astra game casebook](https://github.com/zlxxlz1026/awesome-gpt-6-astra-casebook/blob/main/docs/categories/games.md) | 集合 20 個遊戲／模擬條目，逐項標示 prompt 完整度及限制；重查 Voidrunner（完整反重力武器賽車 prompt、作者稱 25 分鐘，source/build 需繼續查）、Sonic-style Godot slice 和 car-football。前者有已記錄的 Ka/weapon/physics 多系統 brief；Sonic 可能有外部專用工具與版權角色輸入；尚未找到獨立且可立即 play 的優勢足以高過 Smash Karts／既有 Kart Blitz；不作本批新增候選。
- **複核規則：**collection 的「作者報時」等於 case evidence，不是可重現結論；有完整 prompt 不等於 playable，source 有玩法程式不等於 runtime 已實測。後續只查本庫收錄候選的 canonical post、build 及品質限制，不重搜整份 gallery。

## 本批結論

- GPT-6 Astra Smash Karts Arena 是本輪最強新成品線索：高密度多人系統、明確模型與 run 日期、單一 user task 由公開 trajectory 確認、可玩影片、source、作者自動／工程測試都有。它不是 one-click hosted build，且 subagent trace 未公開；成品需安裝部署／啟動，視覺也尚待使用者看過後判斷。適合作為**多人競技與伺服端系統上限題**，不和純前端單檔題混成同一種分數。
- B0045 是可重跑任務工程方法庫，不是新 game result。Draft／未獨立重現的標籤要保留，尤其不把 recipe 的 acceptance checklist 誤報成已經有人完成並 pass。
- 更新根索引與檢閱 HTML：加入 G0206 和新增 Opus 5.5 games，分出開放式創作、固定規格重跑、多人網路、長時代理及物理專項題。沒有任何項目被標成美術通過。

## 下一輪方向

沿 GPT-6 Astra source-repo 關聯做系統型搜尋，優先查 Voidrunner、voxel sandbox、3D delivery／action RPG 類型是否有近期 model-generated playable outputs、原始 trajectory 及完整 prompt。另查 2026-09 至 10 月更新的 model variants 是否對已收錄 high-density prompt 做新 run；不重跑廣泛的 `one prompt game` 通用搜尋。
