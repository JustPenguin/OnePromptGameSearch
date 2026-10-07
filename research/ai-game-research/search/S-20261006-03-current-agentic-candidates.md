# 搜尋批次 S-20261006-03｜單次委託、高系統範圍與自主 QA 交付

**日期／範圍：**2026-10-06；在使用者要求恢復持續研究後，補查近期公開的一次 prompt 成品、AI 自主迭代證據與遊戲系統規模。重點是找「可重跑的強題目」，不要求來源已做多模型比較。

## 研究問題與先前查重

先查根索引、候選名錄、全項目目錄及相關舊紀錄。先前 TETHER (G0152)、NEON WARDEN (G0100)、TOKYO DRIFT (G0186)、Fable/Claude 案例已有零散命中，本輪補的是：公開原始 prompt 和成品版本證據；作者是否明說一則委託後無追問；自主測試／修復的具體證據；任務系統深度是否足以成為上限題。新結果新增 G0191–G0193，並更新 G0152；曾命中的同作不重複建檔。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `2026 AI game benchmark one prompt single-pass playable 3D game screenshots zero shot agent` | 找到候選線索，但不少來源缺 prompt、真實 build 或對人類介入的描述；後續用原始 repo／作者文核對。 | G0137、G0191–G0193 | 新的官方/作者原始 transcript 或同 prompt 新 build。 |
| `AI coding agent one shot complete game no manual tuning first pass playable game 3D 2026` | 搜到以 agent 獨立完成、單次 prompt 及自動 QA 為標籤的作品；「single prompt」和「沒有人工改碼」需逐案核實，不能以平台分類替代證據。 | G0191–G0193 | 來源公開 commit/運行時間線或未修改首版。 |
| `site:github.com AI game "one-pass" playable "single prompt" game model benchmark 2026` | 導向 Fable Arcade；Fable Theft Auto README 有 one turn/no follow-up、生成時間、雜湊及精確任務。 | [G0191](../records/G0191.md) | 直接檢視 voxel 美術；查是否有自主 playtest 日誌。 |
| `single prompt game generation benchmark playable outputs 3D game zero-shot 2026 agent` | 找到多個 benchmark／作品庫結果；低複雜度 benchmark 未當成上限候選。 | G0137、G0191 | benchmark 明確新版／長流程題集時重查。 |
| `2026 one prompt AI game agent autonomous self play fix playable full game high quality 3D game Claude Sonnet 5.5` | 命中 Agent Games 的 TETHER、Tokyo Drift、Tank Rush、DEADBLOCK 等。Agent Games About 表示任何人與模型混合皆可提交，平台不認證有人是否改碼，故只把它當作 prompt／build 線索。 | [G0152](../records/G0152.md)、G0186，以及下列排除項 | 只有原作者補充無人工介入證據時，才能上調 provenance。 |
| `site:github.com game "one prompt" "playwright" "subagents" 2026 game playable Claude Fable` | 命中 Fable Cities、Raccoon Heist 等透明案例。前者有單次 instruction、多代理分工、截圖評論、效能檢測及明列失敗結果；後者明說不再詢問並有 Playwright 自動遊玩。 | [G0192](../records/G0192.md)、[G0193](../records/G0193.md) | 若作者發布新 version 或新 run，再更新同一紀錄。 |
| `site:reddit.com/r/ClaudeCode "one prompt" game "no follow-up" playable 3D game 2026` | 找到 Fable Cities 作者帖及其他作品說明。Fable Cities 系統規模極大，但需多代理、長時間迭代，作者承認畫面與效能未達其自設 AAA 門檻。 | [G0193](../records/G0193.md) | 當前模型重跑時統一多代理與預算；美術由使用者看原始成品。 |
| `site:github.com "one-shot" "game" "GPT-6 Astra" playable game prompt 2026` | 未找到比既有 THE NINTH BELL 更直接的嚴格 zero-shot 候選；GPT-6 Astra 社群收集多為 prompt／圖片，而非能驗證原始 run 的 build。 | G0137 | 有原始 commit／完整 demo 的新題目才值得續查。 |
| `2026 game built from one prompt no follow up AI game dev autonomous playable game Claude Fable 5.1 game`、`AI agent game development one prompt "playable" Fable 5.1 game built autonomous no follow-up 2026`、`site:github.com "single prompt" "game" "Fable 5.1" "playable" autonomous`、`site:github.com "one prompt" "game" GPT-6 Astra playable build game development autonomous` | 搜出 [One prompt. Four open worlds.](https://nitzan.games/OneShotGTA.html)：同一明確畫面目標／自主自測 prompt 有 Fable 5.1、GPT-6 Astra、Claude Opus 5.5 Max 四個實玩版本。最新一版 Golden Hour 開場畫面由研究者直接檢視，畫面風格較有完整設計感；玩法刻意排除槍戰／任務等，故保留作視覺和駕駛物理副題，不當系統上限主題。 | [G0188](../records/G0188.md) | 視覺門檻由使用者判斷；若將來重跑，固定代理和預算以避免數小時至數十小時的耗用差距。 |
| `site:agentgames.dev/play Sonnet 5.5 game "5 zones" game made with AI`、`site:agentgames.dev/play "1,000,000" tokens 3D roguelite game Sonnet 5.5`、`"Sonnet 5.5" "one prompt" game roguelite 3D visual game playable self-testing` | TETHER 公開 grapple-swing 物理、五區、18 升級、長程 progression、bot 模擬與 reviewer/regression QA。未明言無人介入，平台也不認證此事；保留作強系統 near-miss。 | [G0152](../records/G0152.md) | 取得原始 session／無人改碼佐證後再評估是否升為嚴格候選。 |
| `site:agentgames.dev/play "Fortnite OG"`、`site:agentgames.dev/play "DEADBLOCK: Outbreak"`、`site:agentgames.dev/play "Tank Rush"`、`site:agentgames.dev/play "TOKYO DRIFT"` | Fortnite OG 缺公開 prompt；DEADBLOCK 有多區多波次系統但像素畫面、prompt 含「build and refine」且 provenance 不明；Tank Rush prompt 鼓勵反覆 play-test 但畫面範圍較簡單；Tokyo Drift 有開放世界，但頁面為 v4.30、5,592 分鐘，不能證明單一 prompt後無人工參與。都未勝過嚴格/強系統候選。 | G0186（Tokyo Drift 已登錄）；其餘作批次排除線索 | 只在有可信首版時間線及人類介入證據時重查。 |
| `site:agentgames.dev/play "RIFTWAKE"`、`site:github.com "AOT Fable 5.1"` | RIFTWAKE 的原 prompt 是回應玩家對舊版介面的批評；AOT Fable 5.1 文件描述使用者逐步指導模型建角色。均不符合單次委託交付協定。 | G0187（Mortal Shadows，非同案）；本批保留排除理由 | 不重查，除非找到不受回饋／指導的獨立版本。 |
| Fable Arcade 作品庫及 [Fable Theft Auto README](https://raw.githubusercontent.com/sorrycc/fable-arcade/main/games/voxel-gta-city/README.md) | Claude Fable 5.1，2026-09-03，一次 prompt/no follow-up，54 turns 約72分鐘，repo 註明原樣保存及 SHA-256；固定 prompt 整合射擊、劫車、物理駕駛、交通、行人、通緝追捕、任務與 HUD。確認有可玩 build。該 README 未提供 QA 日誌；美術是否達使用者標準待看。 | [G0191](../records/G0191.md) | 使用者直接檢視實際畫面；若把 prompt 作固定題，以當前模型重跑並開放自主自測。 |
| [One prompt. Four open worlds.](https://nitzan.games/OneShotGTA.html) + `AI agent game GTA same prompt high quality low-poly autonomous screenshot critique 2026` | 同一 open-world driving sandbox prompt 產生 Fable 5.1 High、GPT-6 Astra、Fable 5.1 Extra High、Opus 5.5 Max 四個可玩 build，公開精確 prompt 與 source。任務排除任務／武器／警察／行人／故事，專測步行、偷車、車流駕駛、碰撞損毀與換車；visual target 清楚指定低多邊形、乾淨平塗與暖色長陰影，另要求自主截圖、挑錯、修正、重跑。作者回報 Opus 5.5 build 使用多代理、數十小時；研究者直接檢視 Opus 開場，畫面有成熟一致的海灣低多邊形風格，但尚未驗玩完整循環。這是適合視覺／物理副測的強候選，不是廣系統上限題。 | [G0188](../records/G0188.md)（更新既有 Palm Bay 記錄） | 同 brief 重跑時固定時間／token 與代理預算；取得更完整真實遊玩記錄或使用者檢視意見後更新。 |
| [Fable Cities GitHub README](https://github.com/rawprogress/fable-cities)、[完整 PROMPT](https://github.com/rawprogress/fable-cities/blob/main/PROMPT.md)、作者 [Reddit post](https://www.reddit.com/r/ClaudeCode/comments/1w4qziv/ok_this_is_wild_used_claude_fable_5_1_and_said/) | 作者稱一次 instruction、無修正 prompt；任務從空資料夾建 Cities: Skylines II 級 city builder，明列 architecture、multi-agent、headless screenshots、critique、最多四輪修正與盲測。README 自述三輪盲測落敗、首次體驗 5.5/10、部分 perf 未達標。這是高系統規模／自主驗收參照，不是美術通過例；大量代理和時間使它不適合與短程單檔作品混排。 | [G0193](../records/G0193.md) | 查看 repo 真實成品圖；當前模型重跑需設相同 agent/tool/time/token budget。 |
| [Raccoon Heist 原文](https://simonwillison.net/2026/Aug/5/raccoon-heist/)、[live build](https://simonw.github.io/raccoon-heist/) | Claude Fable 5 收到一則委託與兩張概念圖；作者明說不想再回答設計問題。Playwright 驗證桌機和兩種手機視口，具備守衛犬追蹤自動測試。材質／title art 使用 GPT Image 2，遊戲規模偏淺，不納上限候選；方法與美術校準可參照。 | [G0192](../records/G0192.md) | 若拆出共同評測 brief，明確規範是否提供圖片、是否可呼叫影像模型。 |
| [Agent Games TETHER](https://agentgames.dev/play/tether)、[平台 provenance 說明](https://agentgames.dev/about) | 補到 prompt 原文、五區／18升級系統與自動模擬、bug review／regression tests；平台指出創作者可申報任何人機混合作品，平台不認證是否有人改碼。 | [G0152](../records/G0152.md) | 需作者來源層級的人類介入／run timeline 證據。 |

## 其他查詢與排除

- `"Fable 5.1" one prompt game playable roguelite autonomous self test full game`：沒有找到比 Fable Cities 更適合測長時代理自主開發、且同時宣稱美術過關的成品；Fable Cities 作者的公開 QA 自身給出失敗分數。
- 新近公開的 [RSIGame 論文及原始碼](https://github.com/WenyiWU0111/RSIGame) 不是新遊戲題，而是可借用的自主改進流程：遊玩取證、定位問題、修補、獨立回放，保留最佳 checkpoint 並以飽和門檻停止；已更新方法紀錄 [M0019](../records/M0019.md)。它使用 30+ 輪的研究框架，不可以當作一般 one-shot 模型成績。
- `2026 game built from one prompt ...` 搜尋也返回用 GPT-6 Astra 玩 WoW 的 agent-run，但目標是 agent 玩既有遊戲，不是 AI 製作新遊戲；另有賣遊戲開發工作流／工具包的 repo，均非候選成品，未收錄為遊戲。
- `site:agentgames.dev/play "3D game" "visual QA"` 及其他近期展示查詢：新鮮成品多，但平台不核實有無人工改碼；若只因模型名、token 數或建置時數就宣稱 zero-shot，證據不成立。
- Meta 官方 one-shot game dev recipe（`https://dev.meta.ai/docs/cookbook/one-shot-game-dev?project_id=1661600634933790&team_id=2096920474558192`）是 20 分鐘的 3D Crossy Road recipe，採預置 Kenney 素材，範圍太小，只留方法參考。
- `https://aigamingdev.com/blog/3d-space-dodge-benchmark/`：3D space-dodge 題為短生存玩法，且有第二段 prompt，不作上限候選。
- GPT-6 Astra 社群 prompt repo `https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts` 有黑暗奇幻 ARPG、飛行模擬器和 Kaiju 城市戰題型；前兩個 prompt 寫了自我 play-test/fix，但未取得可核實的原始 playable build/session。Kaiju 可玩頁及螃蟹動作遊戲 prompt/build 偏窄。暫不建立遊戲推薦紀錄；若出現可追溯成品再收錄。
- Fortnite-style battle royale (Sonnet 5.5) 有多人 bot、建造／storm 等規格，出處為 prompt 聚合貼文但無原始 playable repo；只存作搜尋線索，未收作強候選。

## 結論與更新去向

- 新增 [G0191 Fable Theft Auto](../records/G0191.md)：較可控的高系統單次 prompt 重跑題，無追問證據清楚，視覺與自主 QA 未確認。
- 新增 [G0193 Fable Cities](../records/G0193.md)：長時間、多代理、自我評論與自我修正的系統上限參照；建置結果未通過作者自身視覺／效能門檻，不列為已驗收品。
- 新增 [G0192 Raccoon Heist](../records/G0192.md)：一次委託自主 QA、成品與視覺校準案例；機制範圍不足以作上限主測，且含影像模型與參考圖。
- 更新 [G0152 TETHER](../records/G0152.md)：記錄 prompt、玩法、bot QA 證據及 Agent Games 對人類參與未核驗的限制。
- 更新 [G0188 OneShotGTA](../records/G0188.md)：從單一 Astra/Palm Bay 擴成同題多個版本，加入較新 Opus 5.5 build；確認其視覺／物理強、系統範圍窄，定位為副測。
- 更新 [M0019 RSIGame](../records/M0019.md)：補記 2026-09-30 正式公開論文與框架，提取可用的自主 playtest／checkpoint 方法，不混算它的研究模型分數。
- 不更新成品美術通過名單；只有 Kart Blitz 是使用者目前明確肯定的候選。
- 有名無 build／protocol 不清楚的線索與排除理由均保存在本批次，避免重複搜尋。

## 重查條件

原作者公開新首版／session transcript、平台增加人類介入核驗欄位、當前 frontier model 可用型號明確更新、或使用者看完成品後指出新的美術標準時再查。相同 query 不因下一輪研究開始而重跑。
