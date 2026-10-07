# 搜尋批次 S43：公開單 prompt 遊戲挑戰規則、重跑與任務上限

**日期／範圍：**2026-10-07；另查一次委託競賽中「只交一次 prompt、AI 自主測試修正、以最後 build 驗收」的正式規則，並確認已舉辦活動是否公開了可重跑規格、模型版本、盲測或重跑結果。此方向與 S42 的最新模型單次生成案例蒐集不同。

## 研究問題與先前查重

索引已收錄 [E0007 profiq Summer Coding Challenge](../records/E0007.md)，S18 當時只查到簡短首頁並因 mini-game／60 分鐘上限列方法副參考。此次沿用固定編號，轉查主辦方完整官方規則、活動截止後的作品畫廊和 prompt／model 提交要求；另外檢查 Opus 5.5 的新 gallery 是否出現未入帳的高難單句遊戲，以及 Meta 即時遊戲編輯工具是否符合「使用者不介入，AI 自己交成品」。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `site:profiq.github.io/ "DEAD ZONE" "Summer Coding Challenge" prompt model`；[官方作品畫廊](https://profiq.github.io/) | 目前畫廊公開多款可玩參賽 build，包含 DEAD ZONE 小城區 FPS 搜刮戰鬥、VESPER 城市 RPG、APEX // QUALIFY 物理賽車及 BRICKSMITH 建造 puzzle。畫廊只顯示玩法簡述／實際 build，不替每款附完整 prompt、model/version/tooling、run trace 或正式分項分數。它可以作真實輸出和互動參照，但尚無足夠資料把作品和模型對應起來。 | [E0007](../records/E0007.md) | 若參賽者個別 release prompt.md、版本設定與凍結 HTML，逐項評估是否另建遊戲紀錄；只在規格和完整度足夠時升候選。 |
| `site:pracujprosiliconvalley.cz "Summer Coding Challenge 2026" results APEX DEAD ZONE`；[主辦方規則頁](https://www.pracujprosiliconvalley.cz/summer-coding-challenge-2026/) | 官方頁明示競賽已結束，最遲 2026-09-23 公布結果，但頁面未提供排名／評審分數總表。規則要求一份不超過 10,000 字元的 prompt、生成開始後零人類追問／手改，agent 可自主計畫、測試、修錯；生成上限 60 分鐘，最後提交 prompt、model／agent／tool 設定與原始單檔 HTML。評審在乾淨瀏覽器檢查作品並以同 prompt 再跑一次。 | [E0007](../records/E0007.md) | 若結果榜或完整提交 archive 釋出，補記分數、prompt/model 對應與再跑表現。 |
| `[ProfIQ challenge] "60 min hard cap" "prompt quality" reproducibility game` | 覆核官方畫廊以一 prompt、單檔、零 do-overs 自我描述；完整規則補齊首頁簡述缺的自主測試、交件欄位及主辦方重跑程序。評分權重是主題／可執行 25%、原創 25%、UX／設計 20%、prompt 品質 20%、重現性 10%，故用總名次比較模型會把 prompt 工藝混入 model result。 | [E0007](../records/E0007.md) | 重用方法時固定共同 prompt，分列功能／作品品質、prompt 品質和第二次重跑穩定度。 |
| `Claude Opus 5.5 game one-sentence prompt browser soak testing autonomous repo games`；[by_opus repo](https://github.com/chandan0000001/by_opus) | Repo 有 Pelican Bicycle、CrossFire: Transport Ship、QQ Speed 三款單句 prompt、source、live demo，宣稱 Opus 5.5 xhigh 單 session／程序美術；流程含 headless browser soak test、subagent code review 與 auto-fix。這三項已分別在 G0117／G0203／G0204 記錄，且使用者已判定 Pelican 美術合格、CrossFire 與 QQ Speed 不合格；本批不另建重複項目。 | [G0117](../records/G0117.md)、[G0203](../records/G0203.md)、[G0204](../records/G0204.md) | 只有在實際新增遊戲／task 或更高證據等級的 session archive 出現時才更新候選；不要重複登錄同 repo 三款作品。 |
| `Sonnet 5.5 Built a Full Game From One Prompt Nathan Onn`；[Kart Blitz 長文與影片](https://www.nathanonn.com/sonnet-5-5-one-prompt-game/) | 確認作者自述 Sonnet 5.5 Max 約五小時、五個 agents、開發中無人類 follow-up，曾自主截圖找出並修正四個畫面 bug，最後有 8 賽道／三種模式／AI 對手／觸控／可玩 Artifact；作者也說 prompt 與 67 分鐘 High run 不同，並坦承真實操控／實機幀率等未核實。該 run 和證據已完整記錄於 G0080／S29，沒有新 run 或新跨模型結果，本批不重建。 | [G0080](../records/G0080.md)、[S29](S-20261007-29-community-session-artifacts-and-one-shot-boundaries.md) | 若作者發布原始完整 session 或獨立第三方凍結 build playtest，再提升證據；維持其使用者美術合格判定。 |
| `Meta Horizon Create Horizon Studio hands on prompt game engine September 2026`；[Android Central 試用報導](https://www.androidcentral.com/gaming/meta-horizon-create-horizon-studio-hands-on) | 報導描述 Horizon Create 即時提示與修改、多人同世界分工、對場景物件反覆編輯／重混及發佈；不符合「使用者一次委託後退出、AI 自主完工」的固定流程。沒有某單一 prompt、完整 run 記錄或能鎖定 model 的交付 build，也不能當成高上限 one-shot 證據。 | — | 除非 Meta 提供無人後續介入的固定 task/export 和模型標記，維持排除於本研究核心條件。 |
| `site:pracujprosiliconvalley.cz "Summer Coding Challenge 2026" results winners APEX DEAD ZONE`；`"profiq" "SUMMER CODING CHALLENGE 2026" results 2026 AI game prompts` | 搜尋未找到官方 winners／分項分數頁或逐題 prompt archive。官方結果應已公布的時限已過，不能把「畫廊仍可玩」推論為「成績／模型資料已公開」。 | [E0007](../records/E0007.md) | 如後續主辦方發布排名、評分細節或 anonymized submissions，更新 E0007。 |

## 結論與更新去向

- 更新既有 [E0007](../records/E0007.md)：它比先前已知更符合本研究的流程定義，因為允許 agent 在單次委託內自主測試／修正，並要求主辦方按同一 prompt 重跑；交件欄位和加權 rubric 也已核實。
- 仍不升成完整遊戲上限主候選：活動明定 mini-game、60 分鐘與單檔限制，畫廊沒有逐件公開 prompt/model/session 或結果榜；最接近完整題的 DEAD ZONE 仍只是小城區生存搜刮射擊，公開描述不證明完整長程閉環。
- 本批沒發現需要另建 G 編號的新強候選。Opus gallery 三款與 Kart Blitz 均已入帳；Meta Horizon Create 的即時迭代／多人編輯流程不符合使用者不介入的核心規則。
- 下一個明確方向：核實 A2Z GameSpec-Bench、GameXpert、PlaytestArena、GameASG／GameCraft 是否有新釋出的完整 task corpus、evaluator 與當前 frontier model run；與 S43 的活動賽制不同，聚焦正式 benchmark artifact 可下載性與一次任務結束產品評測是否相符。
