# 搜尋批次 S54：玩家實際遊玩評量、盲測流程與近期 one-shot build

**日期／範圍：**2026-10-07；承接 S53 的 TODO，對照 B0055 公開 acceptance coverage 與人工試玩問題，另搜近期固定題、無中途回饋且保留成品／玩家評量方法的 browser-game run。

## 研究問題與先前查重

本批先重讀研究索引、候選摘要、搜尋索引、B0055、B0009、B0032、B0043、S53。S53 中 B0055 是三題各 10 項 public machine checks；作者手動發現 checks 仍漏掉 Sol FPS 敵人不射擊、卡丁車反向操控／賽道單一與對手偏弱、RPG 地城可讀性等。既有 WebGameBench (B0043) 由獨立 browser agent 操作交件並區分 Usable／Excellent，PlaytestArena (B0032) 用 GUI agent 在遊戲內操作驗收行為；本輪查新的盲玩／全流程評量證據，不重作 S48–S53 已做的候選 repo 搜索。

## 實際搜尋與查閱

| 實際 query／來源 | 結果、核查及判斷 | 關聯紀錄 | 重查條件 |
|---|---|---|---|
| DuckDuckGo HTML query: `AI generated browser games human playtest evaluation benchmark full playthrough game quality rubric` | 結果包含 Game Bench、WebGameBench、PlaytestArena、GameEval、Carrick AI GameBench 和 AITHEthing「From Prompt to Playable」。逐一點開直接來源，Game Bench 出現目前未列入精選的實際 GPT-6 Astra build 與 V3 frozen task，故納入 G0266、更新 B0009。其餘依下面逐條排除／方法定位。 | [B0009](../records/B0009.md)、[G0266](../records/G0266.md) | Game Bench 公開 run review、source snapshot、score sheet 或實際盲測結果時。|
| DuckDuckGo HTML query: `game generation benchmark human evaluators playability graphics user study full game AI 2026` | 查見 PlaytestArena 論文 v2、AI game generation 方法論及非正式比較頁。PlaytestArena 是已登錄 B0032 的 200 題評估方法；論文 v2 沒改變 full corpus 未公開／Play2Code 多輪的現行判斷。 | [B0032](../records/B0032.md) | 公開 200 題 corpus/evaluator，或發表單一完整委託且保存 playable output 的現行模型 run。|
| DuckDuckGo HTML query: `"WebGameBench" playable game human evaluation rubric excellent usable unusable` | 對照既有 B0043，可用於成品的獨立 browser walkthrough 與品質分級；本批未發現其完整題庫／evaluator 已成可下載套件，也沒有新增最新模型 build run。 | [B0043](../records/B0043.md) | 完整題庫、runtime evaluator 或最新模型實際成品 release。|
| DuckDuckGo HTML query: `"AI game generation" "human evaluation" benchmark playable` | 命中 PlayGen（生成模型／playability evaluation）、Game Bench、PlaytestArena 等。PlayGen 是 game-content generation pipeline，不是近期 coding agent 收到一次完整遊戲委託並交 playable full game 的 run；相關 AutoUE／PlayGen-20 已登錄 B0004/B0031。 | [B0004](../records/B0004.md)、[B0031](../records/B0031.md) | 若來源新增 coding-agent whole-game task 與 playable artifact，再重評。|
| [Game Bench 個人專案說明](https://piccini.app/projects/game-bench/)；[現行榜／評測 protocol](https://game-bench.piccini.app/)；[盲測頁](https://game-bench.piccini.app/blind-tests/) | 頁面說同一 frozen prompt、空 workspace、no human corrections/examples/follow-ups；AI 可以自行計畫、建置、測試、交付。主榜 25 款 build、4 軸、加權 Gameplay/Adherence/Engineering/Art = 45/15/25/15。Blind page 現已提供 25 款匿名可玩 build 與評價表，鼓勵至少玩到懂循環、死亡一次並重開；但沒有公開盲測回覆／彙總。專案介紹頁仍稱 9 routes，與 app 當前 25 build 不一致，依直接 app 頁記數並記下不同步。 | [B0009](../records/B0009.md) | blind-test 有真實 response sample、盲評彙整及 evaluator 重現時。|
| [凍結 V3 prompt](https://game-bench.piccini.app/frozen-prompt.md)；[GPT-6 Astra playable build](https://game-bench.piccini.app/games/gpt-6-astra-20260924/) | GPT-6 Astra high，2026-09-24，網站 row 報 16m06s／1.84M tokens／$4.95；score 95.5，分軸 Gameplay 92.6、Adherence 99.8、Engineering 96.2、Art 98.5。任務明寫 small game，但要求耐力、flies、雨／避難洞、difficulty、音效、mobile、教學／重開及作者要求的 end-to-end self-playtest。現行 row 的 `processStatus: review` 說「Third attempt passed process and play; VM-host containment canary remains unresolved」；作者網站通用 one-shot protocol 與此個別 run 註記並列，attempt/isolation 邊界仍有待解。可玩 artifact 與任務可核，但沒有 public frozen source hash 或完整 trajectory；Astra 四軸分是 Luiz 本人提供，所稱 sheet 沒有可見直達連結。依使用者不以小遊戲湊上限候選的規則，收錄成近期輸出／短循環自主 QA 副測，而非核心推薦。**美術待使用者評價**；作者 Art 分不是使用者評語。 | 新建 [G0266](../records/G0266.md)，補強 [B0009](../records/B0009.md) | 公開 process-review 細節、score sheet、hash/trace 或可核盲測結果；不得單憑排行榜自述解除 review。|
| [Game Bench Astra run assets](https://game-bench.piccini.app/games/gpt-6-astra-20260924/) | run HTML 引用 `game.js`、`style.css`、`audio.js`，三個現行資源均 HTTP 200。這驗證 hosted files 可取用，不等同本研究完成全程玩法、功能、畫面或手機實測；沒有 frozen package/hash 可對版。 | [G0266](../records/G0266.md) | 有跨裝置獨立測試或凍結 zip/hash 後加做 runtime 測試。|
| [AITHEthing article](https://aithething.com/articles/research/from-prompt-to-playable-ai-browser-games.html)（query 1 命中） | 作者比較三種 coding platforms 以單 prompt 做《Jumping Jim》，有小型跳台街機可玩性／流程分數；全文描述的題目是 HTML/CSS/JS、跳躍、危險、collectibles、分數，耗時與迭代 workflow 也在比較內。缺少與 B0055/G0266 同級的高系統任務與可稽核 full run artifacts；因範圍小，不作本使用者的完整遊戲上限候選。 | 不新建（規格範圍不足） | 如提供高系統原 task、永久 build、run trace，可另案。|
| [GameEval QA Pipeline README](https://raw.githubusercontent.com/adam0white/GameEval/main/README.md)（query 1 命中） | README 稱是以 Cloudflare/Playwright/vision agent 對使用者提交 game URL 做四階段自動測試；沒有它自行生成的模型遊戲、固定 prompt 或已測模型 run。屬 QA service，不是生成案例。 | 不新建（工具／評測方法，不是模型 output） | 發現附公開生成 run／任務且可玩交付再重評。|
| [Carrick AI GameBench 0.7.0 README](https://raw.githubusercontent.com/Carrick-K7/carrick-ai-gamebench/main/README.md)（query 1 命中） | repo 說 build suite 用 frozen task、每題一次 Agent invocation、freeze source、canonical seed 測 2048、Minesweeper、2D Parking、Texas Hold'em；0.7.0 新增 Play suite，但 README 明言沒有新 measured Build result。固定題有 contract 重現價值，題目是緊湊 minigame／task 而非完整高上限遊戲。列搜尋排除，不因新版本號立項。 | 不新建（任務範圍不足、沒有新 build run） | 有新的高系統任務與最新模型 output 時再核。|
| [PlaytestArena v2 paper](https://arxiv.org/html/2605.28258v2)；[WebGameBench paper](https://arxiv.org/html/2605.17637) | 更新可直接讀 v2 論文與 WebGameBench method 細節；兩者都強調 behavior rubric、真實 browser input、獨立 reviewer／玩家，而 B0055 公開 `window.__game`／state-driven grader 主要驗 contract，未單獨測敵人是否主動攻擊、AI 對手競爭性／賽道路線變化、一般玩家能否自然理解控制、game fun/art。這個 coverage gap 已由 S53 收錄的 B0055 作者 hands-on 發現直接支持；本批沒有找到可新增給 B0055 的獨立 run 或完整 evaluator。 | [B0032](../records/B0032.md)、[B0043](../records/B0043.md)、[B0055](../records/B0055.md) | 若取得 B0055 blind full-play reports 或 3D grader 在相容環境成功運行，更新原 record。|

## 結論與更新去向

- 新增 [G0266](../records/G0266.md) 並更新 [B0009](../records/B0009.md)。此 run 的完整任務、GPT-6 Astra 可玩 build、四軸 score 和 player-facing protocol，實質提高近期實際生成結果及評量方法覆蓋；故**無增益計數重設為 0／至少 3**。因題目自稱 small game 且為一條循環，不升為完整遊戲上限候選；個別 run 仍有 `processStatus: review`。
- 已將美術、可玩性、系統／內容、一次委託證據與整體證據強度分開記錄；使用者 art 待評，作者 Art 98.5 未取代使用者判定。
- S54 對照 B0055 machine grader / user-facing tests：作者手動 QA 已捕捉機器契約未測到的玩家缺陷；目前沒有因此找到新的獨立 B0055 測試結果。
- 本輪抓取的臨時網站 HTML／assets 在 `/tmp/s54-*`，下一輪引用時須核對線上新版本，因為個人站頁面和 roster 會變動。
- 下一方向不要回到 Game Bench／B0055 player-coverage 重查；先讀索引，再搜尋**現行前沿模型在公開遊戲 jam／玩家交件活動中的可玩 build 與原始 task／開發記錄**。若沒有強候選，清楚記為 S54 後第一個無增益方向。
