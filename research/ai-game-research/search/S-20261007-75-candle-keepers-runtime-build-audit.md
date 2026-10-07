# S75 · Candle-Keeper's Parchment runtime build 與畫面證據追查

- **日期：**2026-10-07
- **搜尋方向：**依 S74 手交線索，直接查這款遊戲的 itch HTML5 embed、公開 runtime files、version/hash 和可取得的 gameplay imagery，區分存在可玩 build、source、凍結版本與可評遊戲內美術。此批只追單一具名 artifact 的 build provenance，不重做 jam entry roster 搜尋。
- **開始前核對：**重讀研究索引、候選摘要及搜尋索引；用 `manage.py lookup "Candle-Keeper's Parchment"` 查名，確認既有 [G0282](../records/G0282.md) 與 S74，不另建同名個案。查 S74 所列原始頁與下一步，確認還沒有遊戲內 screenshot、session 或 source。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| DuckDuckGo HTML `"Candle-Keeper's Parchment" gameplay screenshot Godot` | 無結果，沒有找到遊戲內 screenshot 或錄影索引。 | [G0282](../records/G0282.md) | 作者或 jam 結果發布 gameplay capture 時更新。 |
| DuckDuckGo HTML `theblazehen Candle Keepers Parchment source build capture` | 搜尋結果回到 itch 作者頁、個人 profile、jam rate 頁和不相關 GitHub packaging 專案；未找到本作 source repo。rate 頁摘錄顯示提交時間為 deadline 前 14 分 10 秒，但不能推斷之後未更新 build。 | [G0282](../records/G0282.md) | 有同作者明確連結到此遊戲的 repo／release 時重新關聯。 |
| DuckDuckGo HTML `"html-classic.itch.zone/html/19486036"` | 無搜尋結果；以 itch 作者頁內嵌 iframe URL 為可核來源。 | [G0282](../records/G0282.md) | 若該 URL 改版或出現可追溯 build manifest，再記錄新版本。 |
| [itch 作者頁](https://theblazehen.itch.io/candle-keepers-parchment) → [實際 embed bootstrap](https://html-classic.itch.zone/html/19486036/index.html?v=1790779853) | HTTP 200；bootstrap 是 Godot HTML5 export，config 指定 PCK `39,317,660` bytes、WASM `39,513,091` bytes。取得目前公開 bootstrap、JS、PCK、WASM、icon 和 worklet assets。本次取得 PCK SHA-256 `e48f76384c6b0913170c3b784da318e0e6f6466df53e9015e0ad515057b5f094`；WASM SHA-256 `35116f68540ac41acf7d71ea457added91b5e960a9cca3e2acc72918eaf01277`。這些 hash 定義本次 retrieve 的現行 build snapshot；沒有作者提交時 hash 可用來證明 jam 截止版相同。 | 更新 [G0282](../records/G0282.md) | 若作者公開 source／project repo、原始任務、session 或歷史凍結 artifact，評估一次委託與提交版差異。 |
| 本機暫存下載後，以 Chromium headless 對 local HTTP runtime 執行 screenshot capture | 本機 server 收到 bootstrap、PCK、WASM、JS 的 200 requests；Chromium 30 秒後 timeout，沒有產生圖片，log 出現 TLS handshake errors。另以本機 Godot 4.6.3 `--main-pack` 嘗試開 PCK 時回報 pack version unsupported；這只表明本機 engine 版本不相容於該 pack，不能推論線上 HTML5 build 有故障。兩條路都沒得到 gameplay capture／通關 evidence。 | 更新 [G0282](../records/G0282.md) | 需要有可直接互動的 browser environment 或作者發布 gameplay capture；避免把技術擷取失敗轉成遊戲品質判斷。 |
| [itch 作者頁](https://theblazehen.itch.io/candle-keepers-parchment) credits／description 重讀 | credits 再確認唯一直接檢視的城堡夕照圖是 OpenAI image generation cover；作者宣稱的程序 art、shader、effects 屬 gameplay 內容歸因，但沒有目前可見遊戲畫面。無 user task/session 或人工獨立評分。 | [G0282](../records/G0282.md) | 不以 cover image 代替 runtime art；需等遊戲內畫面可檢視。 |

## 結論與更新去向

- 更新 [G0282](../records/G0282.md)：加上 itch 動態 embed、Godot PCK/WASM 大小及本次 runtime file hashes；將截圖擷取失敗和 browser/native runtime 限制明確記錄。這提升了「當下公開 build 存在且可凍結識別」的證據，但不證明 jam submission 當時版、source provenance、遊戲內美術品質或 one-shot 條件。
- 沒有找到遊戲內 screenshot/source/session，沒有新增強 one-shot 候選或重大提升 one-shot 證據；S54 後第 **21** 個不同無增益方向。研究仍未完成，因最新模型實際生成案例及正式 benchmark artifact 覆查仍未完整。
- **下一方向：**重新查 A2Z GameSpec-Bench 官方 repo／論文 artifact link／release 和資料集平台，確認 2026-10-07 當前是否已釋出可重跑的大型 GDD、生成輸出與 evaluator；先查現有 [B0052](../records/B0052.md)、S40、S49 去重，若無 release 才記作未變。這是正式高難遊戲生成 benchmark 狀態覆查，與本批單一 itch runtime artifact 不同。
