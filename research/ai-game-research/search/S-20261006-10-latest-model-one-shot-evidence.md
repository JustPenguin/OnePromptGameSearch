# 搜尋批次 S-20261006-10：最新模型 one-shot 實測與成品更新

**日期：**2026-10-06（台北時間）  
**研究問題：**既有高複雜度 one-shot 題是否已有更新模型的可玩輸出？近期比較是否能補足一則任務、自治 QA、最終成品評分的實測證據？

## 開始前查重

先讀根索引、精選候選、全目錄及 S06–S09。Single HTML Game Bench 已是 G0137／B0036；Hill Climb Racing 已是 G0077；Game Bench 固定題已是 B0009。此批不另建重複項目，只為同題新增 GPT-6.1 Sol 版本、更新公開 roster，並補記近期 Hill Climb 對照的任務與品質證據。

## 實際搜尋與查閱

| 查詢／來源 | 結果與證據 | 更新與限制 |
|---|---|---|
| `site:github.com/chojondocho/single-html-game-bench GPT-6.1 Sol`；[Single HTML Game Bench README](https://github.com/chojondocho/single-html-game-bench/blob/main/README.md)；[GPT-6.1 Sol playable build](https://chojondocho.github.io/single-html-game-bench/codex-gpt-6-1-sol-max.html) | 原 repo 現列 20 個 build；共同 exact prompt 為單 HTML 3D horror + RPG/roguelike，規則為 zero-shot、one-pass、禁止人工 gameplay/system tuning。9/30 個人手玩排序列 GPT-6.1 Sol Max 第 6、Opus 5.5 Max 第 1、GPT-6 Astra Max 第 5。6.1 build 是 THE NINTH BELL，同名題材但不同模型輸出，可實際載入遊玩。 | 更新 G0137／B0036 和候選頁，將 6.1 Sol 作為較新模型成品連結。作者排名仍屬主觀、非盲測；頁面沒有公開該跑次 transcript、時間或成本。one-pass 首版測試不等同允許自主迭代的長程測法。 |
| `GPT-6.1 Sol Opus 5.5 one attempt game brief test fix 2026`；[BitsMinds 原始實測](https://www.bitsminds.com/news/claude-opus-5-5-vs-gpt-6-1-sol-hill-climb-2026) | 9/30 公布 GPT-6.1 Sol max/Codex 與 Opus 5.5 max/Claude Code Hill Climb 單次實測；Sol 57:38、Opus 98:06；四軸 graphics/physics/sound/gameplay，13/20 對 19/20，兩邊都被要求實跑、修正、凍結 build。頁內有兩個真實 playable build 和遊戲過程截圖。文章逐項描述 brief，但未公開 exact prompt file。 | 更新 G0077。屬單關物理／操作子題，不能代替完整遊戲上限；Sol 與 Astra build 相似是文章觀察，對訓練資料來源的解釋仍只是作者推論。最重要的冷啟動限制：GPT-6.1 Sol 讀過 Codex memory，Opus 子代理讀過專案 memory index，因此不能當無記憶 clean-start 比較。 |
| `Game Bench latest models September 2026 GPT-6 Astra one shot game prompt`；[Game Bench leaderboard/protocol](https://game-bench.piccini.app/) | 現頁 25 跑次，9 月資料中有 GPT-6 Astra 9/24（95.5、$4.95、16:06）、GPT-6 Sol、Opus 5.5、Fable 5.1 等。凍結 prompt、clean workspace、one-shot 自主測試交付和 45/15/25/15 四軸 rubric 清楚。 | 已有 B0009 記錄此來源及題目深度限制；確認目前公開資料 roster，沒有新增一款新模型 run。它的 Spider V3 仍是單一短循環，不升主測候選。 |

## 本批結論

- G0137 增加 GPT-6.1 Sol Max 的同題 playable run；可直接並看同一高難度 prompt 在 GPT-6 Astra Max、GPT-6.1 Sol Max 和 Opus 5.5 Max 的差異。成品可見性提升，但作者名次只當個人 hands-on 記錄，且仍沒有完整 session 證據。
- G0077 補入一組透明度較高的近期單次對照，適合評量車輛物理、失敗條件、自測與簡短操作迴圈。因題目窄、prompt 原檔未公開且雙方有記憶上下文，不推薦作整體上限主題。
- B0009 現行 roster 有最新可核實的 9 月 runs；其任務和四軸方法可借用，但遊戲循環仍過窄，符合使用者排除簡單遊戲的要求，保留為流程方法而非題型推薦。

## 重查條件

若 Single HTML Game Bench 加入新模型、原始 session log 或更新評測方式，再更新 G0137／B0036；若 BitsMinds 公開 exact brief 或 cold-start 重跑，再更新 G0077 的比較效力；若 Game Bench 新增更深的長流程題或 10 月 run，再回查 B0009。避免重搜以上相同 URL 和 roster。
