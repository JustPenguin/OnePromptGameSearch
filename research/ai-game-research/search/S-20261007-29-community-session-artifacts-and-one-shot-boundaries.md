# S29｜最新模型社群 session 線索與一次交付邊界

**日期：**2026-10-07（台北時間）  
**研究問題：**S28 所指的非官方最新模型 session artifact 是否有新遊戲案例？對話／作者文章能否分清初始 prompt、自主 QA、使用者 follow-up 和最終 build？  
**先前查重：**已讀 README、S26–S28 批次及相關紀錄；Kart Blitz（G0080）有既有紀錄，本輪只用新來源交叉核對，避免另建同作項目。

## 實際查詢

- `"GPT-6.1 Sol" game "trajectory" playable repository one prompt`
- `"Claude Sonnet 5.5" game "session" GitHub prompt playable one-shot`
- `site:huggingface.co/datasets "GPT-6.1 Sol" game trajectory`
- `"GPT-6 Astra" game "trajectory" jsonl playable single prompt`
- 開啟 Sonnet 5.5 kart 原始貼文、獨立重跑文章與作者流程說明。
- 查閱 OpenAI Astra casebook 中 Rocket League 類、Sonic 類、Ghost of Tsushima 類、單檔 canyon racer、Emberwake 等線索，再點選原始作者 X 貼文。
- 查閱 Montanha: Zero Day 作者文章、初始 prompt、QA／後續回饋和公開 repo/build。

## 命中與處置

| 線索 | 查到的證據 | 判斷／更新 |
|---|---|---|
| GPT-6.1 Sol 近期完整 game session | 搜尋返回 G0211 Afterlight 等已有線索，沒有找到本輪可新增的完整公開 game-session export 或新 frozen build。Hugging Face query 沒命中可歸檔的新遊戲結果。 | 無新 Sol 遊戲項目；不把非遊戲、一般 benchmark trajectory 或社群模型意見當遊戲能力成績。日後以具名 run／新 trace 出現時再查。 |
| Kart Blitz Sonnet 5.5 High 原始 run | [作者原始 Reddit 記錄](https://www.reddit.com/r/ClaudeCode/comments/1wsx03y/sonnet_55_high_oneshot_a_full_mario_kart_from_1/)提供原 prompt、6 個 Sonnet 5.5 High agent、空資料夾、67 分鐘、424 model calls、遊戲 4 賽道／8 racers／10 道具；[可玩 build](https://ohmygames.app/play/turbo-karts)。 | 交叉補足既有 G0080 的 67 分鐘 High run，不能與 Nathan Onn 的 Max run 混作一次。作者／貼文自述而非完整逐訊息 transcript；G0080 已留有同一原始來源及不同 prompt 的獨立重跑證據，本批不重複建項。 |
| Kart Blitz Sonnet 5.5 Max 獨立重跑 | [Nathan Onn 2026-10-02 文章](https://www.nathanonn.com/sonnet-5-5-one-prompt-game/)第一人稱說明另一次 run 一則 prompt 後隔夜，作者全程零 follow-up；Max effort、網頁 cloud harness、Playwright／Firecrawl、五小時、五個 builders，先寫任務清單，lead 合併並用瀏覽器看畫面修四個 UI／road bugs，公開截圖、影片與 Claude Artifact。文章同時指出其 prompt 比原 High run 加了 browser、作業規劃、工具及 publish 要求，且表格列 308 tests。 | 這是高品質「一次交辦、AI 自修後交件」實物對照。文章自己承認模型沒能驗證真人遊戲手感、FPS、實體裝置或聲音品質；成品也已由使用者判定美術合格。G0080 已有相同來源／run，更新其搜尋批次，未另建。 |
| Montanha: Zero Day | [作者文章](https://dev.to/tiagovilasboas/i-built-a-full-pwa-game-in-one-day-with-claude-opus-55-and-claude-code-here-is-the-real-token-41p7)公開三句初始 prompt、Opus 5.5／Claude Code、可玩 PWA／GitHub、24 個 ES modules、測試 harness；但作者明確記錄對角色操控提出回饋，並後續要求第三關 boss 前場景由 7 段增至 12 段。修復前的測試還發現 boss 復活、擊退掉坑及可穿過雷射等 bug。 | 成品有三階段、boss 和結局，是高價值多系統重跑 brief，卻有明確使用者 follow-up。新建 G0244：最終 build 排除 strict one-shot 成績；保存原 kickoff prompt 供最新版模型乾淨重跑。 |
| Astra casebook 的 Car-football／Rocket League 類題 | [casebook 頁](https://github.com/zlxxlz1026/awesome-gpt-6-astra-casebook/blob/main/docs/gallery.md#)摘要指出 2026-09-05、單長 prompt、Three.js／Rapier、車體物理、球規則、完整 match loop、作者申報約 63 分鐘；X 原始 prompt／影片連結目前回應 403。 | 機制有賽車、球體碰撞、進球／完整比賽循環，作為副題有潛力；本輪不能直接核原 prompt、看原始 video／取得 playable build，也沒有 session trace，故暫不建獨立候選或推薦。僅留這個具名重查線索，待 X／原作者提供可存取資料。 |
| Astra casebook 的 Sonic-style、Ghost of Tsushima、Emberwake、canyon racer 等 | [公開策展 gallery](https://github.com/zlxxlz1026/awesome-gpt-6-astra-casebook/blob/main/docs/gallery.md)列長 prompt／短 prompt、Godot vertical slice、3D assets、critic subagent 等；Sonic 與 Emberwake 仍只有 X prompt／影片，Ghost 頁未提供可玩下載；canyon racer 摘要承認初版 packaging bug 後有 follow-up。原始 X links 回應 403。 | 僅是第三方線索，沒有足夠可訪問來源和獨立產品交驗證；不把圖廊作者的「polished」等判斷當作使用者美術驗收。已有明確 follow-up 的 canyon racer 排除 strict one-shot。避免為擴大名單而建立薄弱紀錄。 |

## 本輪結論與下一方向

現行模型的完整公開 game trace 仍很稀少。最完整的近期一手比較材料之一仍是 Kart Blitz 的 High 原始 run 加 Max 獨立 prompt 變體：兩者都符合「一次使用者請求後 AI 自己運用代理／瀏覽器／QA」的概念，但需分開 run 記錄與工具條件。新的 Montanha: Zero Day 證明多輪產物不能以三句 kickoff prompt 冒稱 one-shot 成績；原始 brief 仍可拿給最新模型重跑。Astra casebook 找到一些可能更高美術／物理要求的題材，但原始 X post 在查核時不可存取，未達列強候選的證據門檻。

- 更新／交叉核查：[G0080 Kart Blitz](../records/G0080.md)；既有 E0008 美術合格判定保持。
- 新增：[G0244 Montanha: Zero Day](../records/G0244.md)，定位為多輪迭代參照和最新版重跑 brief，排除原最終 build 的一次交付成績。
- 保留未建檔線索：Astra Rocket League 類遊戲、Sonic-style Godot slice、Emberwake；如原始 prompt／影片/build 可公開訪問，再按來源查重及建立紀錄。

**下一輪方向：**把研究範圍轉向模型社群以外的公開 agent build events／browser game jams 與帶官方錄影、人工追問 transcript 的挑戰活動；逐項讀 rules 判斷是否允許使用者中途指導，並只留原始 AI 最終 build。不要重跑 S28 官方 showcase 搜尋、S29 同一批 query、Kart Blitz 或已受限的 casebook X links。
