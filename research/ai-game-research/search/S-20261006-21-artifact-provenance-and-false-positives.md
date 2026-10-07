# S21 · 成品出處核對與 one-shot 假陽性

**日期：**2026-10-06　**研究方向：**從社群 build 展示回查 repo、固定 prompt、可玩成品與人類介入史，辨別最終 repo 是否真是一次交付。

## 實際搜尋詞

- `site:reddit.com/r/aigamedev "one prompt" game playable "2026" AI built game`
- `site:reddit.com/r/ClaudeCode "one prompt" game "playable" "subagents" 2026 game`
- `site:github.com "one prompt" "game" "Opus 5.5" playable game 2026`
- `AI model one-shot game demo strategy RPG platformer full game September 2026 playable`

## 查閱來源與結果

### 排除為嚴格 one-shot 成績、保留有價值的成品／題材參照

- **Low Thunder（G0234）：**[Scenario 的完整製作說明與遊戲截圖](https://www.scenario.com/blog/ai-game-development-low-thunder-scenario-four-days)、[playable](https://low-thunder.com/)。有十輛坦克、十名指揮官、十個戰場和十場 campaign，可看真實作品；公司共同創辦人／CEO 提供創意方向，逐次審稿並要求修改，跨四天用 Scenario MCP 生圖、音效及 3D 資產。因此不是一次委託後零追問。新增 G0234。
- **PixelArtGameOpus（G0235）：**[repo／原始 prompt／測試／畫面](https://github.com/Odiriuss/PixelArtGameOpus)、[playable builds](https://odiriuss.github.io/PixelArtGameOpus/)。其中 `The Hourglass City` 偵探冒險與 `The Black Sedan` 駕駛／射擊關卡是後續 follow-up prompt 的作品；唯一始於一則 prompt 的 `Ravenshore Garden` 是夕陽花園循環 vignette，沒有完整玩法目標／勝敗閉環。不能把整個 repo 的後續內容歸入一次輸入。新增 G0235。

### 看見線索、保留下一輪查核

- **Rubberhose Ruckus／Tesana Atomos：**[社群貼文](https://www.reddit.com/r/aigamedev/comments/1v9bqzx/ai_made_platformer_trying_long_horizon_prompting/)展示可玩 Cuphead 風格 boss-rush platformer，評論列出一段原始起始 prompt；發帖者稱把一則要求交給平台的 LOOP mode 後讓它約九小時自行迭代。作者也承認平台提供數百種動畫／遊戲素材，且此 LOOP／engine 為廠商私有模型系統；精確基礎模型、prompt 是否從空 workspace 起步、過程中是否需點選／補指令仍待核。先不列通用模型強候選；下輪查官方 Atomos／LOOP 介面、輸出可重現方式、真實遊戲與是否能同任務公平比較。

### 重複項／無新內容

- 搜到 **Fable Cities** 的貼文，與已有 G0193 是同一作品，不另建紀錄。
- 結果頁中的 generic Steam 遊戲、只有宣傳圖但找不到 prompt 或 source 的遊戲，以及自行寫有「AI-made」但作者／模型／run 不明的項目，不納入強候選；沒有足夠可追查資訊建立獨立具名紀錄。

## 本輪結論與後續

最終 repo／成品不能反向證明 one-shot；需要查原始 prompt、是否 follow-up、初版 frozen build 及作者編輯／QA 痕跡。S21 新增兩個明確排除紀錄 G0234、G0235；Tesana 是未決工具專屬線索，指定在之後一輪查官方說明，不要重跑本輪 Reddit 泛查。
