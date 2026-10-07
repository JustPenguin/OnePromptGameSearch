# S32｜最新 Agent Games 可玩生成作品查核

**日期：**2026-10-07（台北時間）  
**研究問題：**從最新作品索引抽查 GPT-6.1 Sol 及近期模型的可玩遊戲，確認是否有較目前候選更適合測試「使用者一次交辦、AI 自行修正、只驗收最終交件」上限的新增作品；同時核對公開 prompt、模型／工具、日期、版本和一次輸入證據。  
**先前查重：**先讀研究索引、精選候選、search/index 與 S31。Agent Games 新作索引的 Metro Rush 已是 G0228；Crowd Rush 是 G0079；Afterlight 是 G0211。其餘具名項目以全目錄查重後才決定新增。

## 實際搜尋與查閱

搜尋文字：

- `2026 GPT-6.1 Sol AI generated game playable game one prompt Codex game October`
- `2026 GPT-6 Astra game generation playable browser game one prompt artifact October 2026`
- `site:agentgames.dev/play GPT-6.1 Sol 2026 October playable games game`
- `AI game generation benchmark 2026 latest model game playable artifact prompt autonomous`

| 查閱來源／項目 | 取得的證據及判斷 | 關聯紀錄 | 後續條件 |
|---|---|---|---|
| [Agent Games 最新作品索引](https://agentgames.dev/search?sort=new)；[平台首頁](https://agentgames.dev/) | 搜尋當日索引列出 48 款作品。這是一個不斷變動的策展作品庫，作品頁提供可玩入口和部分作者提交的模型／prompt 資訊，不能單憑「新」或列表排名認定是獨立的一次生成 run。從近期 GPT-6.1 Sol/MiMo 作品抽樣逐頁核對。 | 本批其他列項 | 新作索引出現有較完整長程系統、公開原始任務及凍結 run 的作品時重查。 |
| [Metro Rush](https://agentgames.dev/play/metro-rush) | G0228 已有基本紀錄。本次頁面核對到公開的逐字 prompt，GPT-6.1 Sol／Codex desktop／High、58 分鐘、10,845,228 tokens、v1.1.1；三線跑酷、四道具、hoverboard、追逐開場、手機 controls 和排行榜。prompt 要求 build、宣傳圖和發布，但頁面無 session transcript、首版 hash 或 no-follow-up 證明。它仍是單一跑酷循環，深度不足以當上限主測；更新既有紀錄保存 prompt 與證據缺口。 | [G0228](../records/G0228.md) | 公開首版/session trace，或出現多區域長程 campaign／更複雜系統時重核。 |
| [Afterlight](https://agentgames.dev/play/afterlight)；[目前可玩 build](https://play.agentgames.dev/g/g_5bDBTNoVMJLfPNeZ/index.html) | G0211 已記錄。重核到 exact prompt：讓 GPT-6.1 Sol 自選並製作 progression game，具三名角色、三座聖所、九場遭遇、三個 guardian、可疊加升級、永久成長；要求程序視覺、音效、鍵鼠／觸控、存檔，並自驗戰鬥、升級、獎勵、持久性及離線遊玩。頁面列 2026-10-01、High、約 41 分鐘及現版 1.0.0。缺 session transcript、首版凍結版和獨立驗收；依既有結論保留為重跑備選，不宣稱 one-shot 已核實。將逐字任務補進原紀錄。 | [G0211](../records/G0211.md) | 新增 session／trace 或凍結原 build 後更新自治證據；使用者已判定美術不合格（見 E0008）。 |
| [Crowd Rush](https://agentgames.dev/play/crowd-rush) | G0079 已登錄。作者頁目前明示 prompt 是恢復既有作品自動 Boss 遭遇並移除互動 Boss 控制，再保留既有 30 關、商店與成長；版本 4.1.0 更新 10/02。這是針對已存在遊戲的維護／改版任務，不是空白起始的新生成成績；重查確認舊結論。 | [G0079](../records/G0079.md) | 只有出現其空白起始原始 run／首版 trace 才作新生成評估。 |
| [Crowd Gate Runner](https://agentgames.dev/play/crowd-gate-runner) | 新增 G0248。MiMo V2.6 Pro／High，頁面列 138 分鐘、269,000 tokens、1.7 版，prompt 和 playable build 公開；核心是 3D 數學閘門人群跑酷、障礙、敵群、10 關和簡單升級商店。沒有原始 session／首版／介入證據，且玩法系統仍屬 hyper-casual 跑酷，不比現有長流程候選更能測上限。保留明確排除理由，避免下次因「十關／有 3D」誤升。 | [G0248](../records/G0248.md) | 除非新增多系統長程任務或相反的原始 run 證據，無須重查。 |
| [Dead Sector](https://agentgames.dev/play/dead-sector) | 頁面標 MiMo V2.6 Pro／Max、可玩 3D 生存射擊，但沒有 prompt、工具、耗時或生成流程；介紹只泛稱敵潮、武器升級和求生，無法評估內容量／玩法系統，也無法核實美術與一次交付。記在本批排除線索，不新增候選紀錄，以免把模糊自述當證據。 | — | 僅在作者補公開 prompt、首版、session 或足以查核的遊戲流程後建立個案。 |
| [GPT-6.1 Sol reasoning-effort 對照](https://spectrumailab.com/blog/gpt-6-1-sol-reasoning-effort-test-2026) | 2026-10-04 更新，12 個全新 session 對照兩個 prompt、六種 effort，提供完整網站 build 和 3D Colosseum 場景 build、Codex event logs、耗時／token 及盲評。兩個題目都不是遊戲（Colosseum 是建築場景，另一個是模型介紹網站），故不能作遊戲生成成績；可參考控制模型 effort、隔離資料夾和保存 event log 的實驗方法。 | 方法旁證，本輪不另建遊戲項目 | 若作者後續用相同 protocol 加入完整遊戲 brief，核對完整 artifacts。 |
| [WorldBuild Bench 2026-07-13 pilot](https://sandscape.app/worldbuild/rounds/ai-game-benchmark-2026-07-13) | 有 10 模型／29 個 build／3 個共同 brief（競技場戰鬥、物理謎題、競速），公開 playable artifacts、時間／成本／程式規模及盲評入口；頁面當時的模型 roster 到 GPT-5.6 Sol、沒有 GPT-6.1 Sol/Astra，Arena ratings 顯示 pending。它能提供可重跑對照題和開放 build 檢視，不是目前最新 frontier 結果，也不是長程／多系統的上限任務。 | 方法／題型參考，本輪不新增紀錄 | 若發新版加入當前模型、完整評分及難度更高任務，追查其 run protocol 和題庫。 |
| [Playable Worlds：GPT-6 Astra 10 builds](https://neta.art/app/gpt6-astra-prompt/gpt6-astra-worlds)；[Astra prompt collection](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts) | 頁面稱十款單 prompt browser worlds 並連到個案；其中的策展 recipes 已在 [B0045](../records/B0045.md) 說明。現頁多是互動世界／小型題，缺足以證明長程遊戲上限的系統與公開生成 trace；本批不重複建項。 | [B0045](../records/B0045.md) | 只有出現原始完整 prompt、可凍結 build／trace 且玩法規模明顯超出小型 world demo 時再個別新增。 |
| Agent Games 的 [Sector Zero](https://agentgames.dev/play/sector-zero) | 新作索引列 GPT-6.1 Sol，但來源工具回傳 cache miss，無法確認任務或遊戲內容；不將標題／模型標籤推論為合格案例。 | — | 來源可讀時再檢查。 |

## 判斷與更新去向

本批實際查核到最新 Sol 可玩作品的更多原文證據，但**沒有發現新增的高上限候選**。Afterlight 是這批最完整的新模型遊戲 prompt 和長流程遊戲結構，已在 G0211 收錄，故只補任務原文，不重複推薦。Metro Rush 雖已找到完整公開 prompt，仍然是單循環跑酷；Crowd Gate Runner 的 3D／十關／商店也沒有改變其 hyper-casual 題型深度。Crowd Rush 明確是修補既有 build；Dead Sector 資料不足。故不更新精選候選頁或檢閱 HTML，不把 Agent Games 的人氣／版本數當作成績。

- 更新 [G0228 Metro Rush](../records/G0228.md) 的逐字任務及目前模型／版本資訊。
- 更新 [G0211 Afterlight](../records/G0211.md) 的逐字任務並交叉註明本批重核。
- 新增 [G0248 Crowd Gate Runner](../records/G0248.md) 並記明排除理由。
- Crowd Rush、Dead Sector、WorldBuild Bench、Spectrum 對照結果與 Sector Zero 阻礙均已記在本批；沒有不必要地將泛稱項目建成強候選。
- **下一方向：**轉查近期公開的高難度原始遊戲 brief 與實際 agent session／frozen artifact，而非繼續按 Agent Games 列表抽樣；優先搜完整 RPG/FPS/模擬／多人任務與有 session 可交叉驗證的一次使用者委託。對今年已登錄的 benchmark 另查是否公布 GPT-6.1 Sol／GPT-6 Astra 等最新模型重跑資料。
