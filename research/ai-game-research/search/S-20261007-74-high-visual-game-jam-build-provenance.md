# S74 · 高視覺遊戲 jam 的公開 build 與 AI／人類工作歸屬

- **日期：**2026-10-07
- **搜尋方向：**依 S73 後續，查有公開 browser build 和藝術／工具歸屬資料的遊戲 jam 作品，優先檢視風格化 3D/2.5D、城堡環境與較完整遊戲；確認 jam 是否要求一次委託、是否有原始 task/session/source，以及宣傳圖是否真為 gameplay。這與先前平台 gallery、官方模型展示及研究 benchmark 查核不同。
- **開始前核對：**重讀研究索引、候選摘要和搜尋索引；確認 Slapjam 已有活動 [E0005](../records/E0005.md)，《Aethel Fold》[G0274](../records/G0274.md) 已於 S65 登錄，避免重建活動／作品；先以名稱、作者、網址查重《Candle-Keeper's Parchment》。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| DuckDuckGo HTML `"AI game jam" 2026 game source playable submission AI generated` | 找到 itch AI GAME JAM、Vibe Jam、Slapjam 2026 等活動及 entry listing。多為 48 小時或非 one-shot 參賽，未見單一初始任務/session 規格；同一 Slapjam 活動已存在於 E0005。 | [E0005](../records/E0005.md) | 新活動若有 task freeze、session export 或 AI autonomy 規則再建事件／查項目。 |
| DuckDuckGo HTML `site:itch.io "AI game jam" "2026" game jam playable` | 找到 Jabali AI Game Jam、另一 itch AI Game Jam 等；目前頁面只證明 AI 工具參賽或作品分類，沒有 one-shot task/run 證據，未擴展登錄。 | — | 若作品頁公開一手 task、artifact freeze 和 runtime footage，再個案查核。 |
| DuckDuckGo HTML `Slapjam 2026 AI game jam entries best games source`；[Slapjam itch event](https://itch.io/jam/slapjam-ai-1)；[142-entry roster](https://itch.io/jam/slapjam-ai-1/entries)；[Slapjam official page](https://slapjam.ai/) | itch 活動列 142 entries，規則要求 48 小時內製作、手機直向、HTML5 browser build、AI 用於作品；官方允許 autonomous agent 完成作品，也允許人類代做最後上傳。無單次使用者委託、禁止 follow-up、session 或 freeze 規則。這補充既有 E0005，不形成一次交付證據。 | [E0005](../records/E0005.md) | 若主辦公開每件評審細分分數或 run provenance，更新評測方法。 |
| DuckDuckGo HTML `AI generated game showcase 3D game build prompt github 2026`；[Candle-Keeper's Parchment entry](https://itch.io/jam/slapjam-ai-1/entries)；[作者遊戲頁](https://theblazehen.itch.io/candle-keepers-parchment) | entry list 有《Candle-Keeper's Parchment》。作者頁列 HTML5/Godot，紙飛機穿越城堡六個年代、花園序章與故事書開／結尾；工具聲明稱 Claude/oh-my-pi 製作程式、關卡、shader、程序美術、特效和文字，Suno 作音樂，OpenAI image generation 作封面。作者明列人類 creative direction、資產選擇整合、testing、balancing、final assembly/submission。無原始 prompt、model snapshot、session/source/frozen build。 | 新增 [G0282](../records/G0282.md)，更新 [E0005](../records/E0005.md) | 若有 gameplay screenshot/video 或 source，另評遊戲內美術、可玩性與內容完成度。 |
| [封面圖原檔](https://img.itch.zone/aW1nLzMwNDA3NTE5LnBuZw==/original/p9GIxO.png) 與[縮圖](https://img.itch.zone/aW1nLzMwNDA3NTE5LnBuZw==/508x254%23mb/l%2FWjFZ.png)；實際查看縮圖 | 檢視到夕照雪城堡、河面反光、紙飛機；作者 credits 明確說封面由 OpenAI image generation 產生。因此這張精緻圖不能當 Claude 遊戲內 art。itch 頁沒有另見 gameplay screenshot/gallery，研究者未進行完整 runtime play。 | [G0282](../records/G0282.md) | 須取得遊戲內 capture 才能做美術評價；封面品質不代替 runtime。 |
| DuckDuckGo HTML `"Candle-Keeper’s Parchment" AI game jam source Claude`、`"Candle-Keeper's Parchment" GitHub` | 命中仍指向 jam entry／itch 頁，沒有找到 GitHub source 或 session transcript。 | [G0282](../records/G0282.md) | 有作者公開 trace/source 時重查。 |
| DuckDuckGo HTML `"LAST CASTLE: The Walking Keep" AI tools Codex`；[LAST CASTLE page](https://jjyo040102-cmyk.itch.io/last-castle-the-walking-keep)、[DREADFALL](https://sentryisgod.itch.io/dreadfall-demo)、[ASHEN RAMPART](https://haruka-apps-games.itch.io/ashen-rampart)、[Tiny Necromancer](https://dylanh.itch.io/tiny-necromancer) | 覆查幾款 roster 作品；LAST CASTLE 聲明 Codex 產 code/graphics、Gemini 產音效，但 solo human 負責創意方向、資產選擇整合、測試、平衡與提交；其餘頁面沒有公開完整 task/session。DREADFALL、ASHEN RAMPART 與 Tiny Necromancer 未出現能改變 one-shot 判斷的一手 trace，未湊成新個案。 | [E0005](../records/E0005.md) | 有 gameplay captures／source 的作品可按明確新證據再建；單憑 jam badge 不提升 one-shot 狀態。 |

## 結論與更新去向

- 更新既有活動 [E0005](../records/E0005.md)；新增 [G0282](../records/G0282.md) 作為公開 HTML5、AI-assisted procedural-art 風格參照。它有值得直接檢視的遊戲題材和完整短篇描述，但目前直接檢視到的精緻城堡圖是獨立 OpenAI 封面；沒有遊戲內畫面、可核 session 或一手原始 task。故美術待使用者評價，不能列強 one-shot 候選。
- 此方向沒有找到新強一次委託候選，亦沒有顯著提升既有案例的 one-shot 證據；S54 後第 **20** 個不同無增益方向。研究**仍持續**：目前方向數已超過最低門檻，但近期模型 run、正式 benchmark 完整 task/artifact 覆查等總條件尚未全部滿足，不作結案判定。
- **下一搜尋方向：**查有遊戲內、非宣傳封面之實機截圖／影片且公開原始 source 的高視覺 AI game-jam 成品；優先追本輪作者已列出可玩 HTML5 的《Candle-Keeper's Parchment》，嘗試從 itch build assets 找 runtime capture，並找其 task/session；若仍缺證據，轉查同 jam 中明列 AI 工具和 playable screenshots 的 3D／2.5D entries。每個新增案例仍分開判美術、可玩性、系統完整度、一次委託與證據強度。
