# S23 · Agent 平台、OpenGame 任務圖廊與 3D 世界基準

**日期：**2026-10-06　**研究方向：**承接 S21 中的 Tesana LOOP 線索，查清遊戲專用自治平台如何運作；檢視 OpenGame 新公開的一次 prompt 成品／source 圖廊能否用來比較可替換模型；另外覆查剛公開的 3D gaming-world benchmark 是否提供高難度可重跑題。

## 實際搜尋詞

- `Tesana Atomos LOOP Rubberhose Ruckus AI built game initial prompt 9 hours official`
- `site:tesana.ai/blog Atomos LOOP game platformer Rubberhose Ruckus`
- `"Rubberhose Ruckus" prompt LOOP game generation`
- `site:reddit.com/r/aigamedev Tesana Atomos LOOP game platformer`
- `site:tesana.ai/blog Atomos model Tesana AI game model`
- `site:docs.tesana.ai Atomos model game AI Tesana selected model`
- `Tesana Atomos model release game AI model official 2026`
- `AI game creation platform autonomous build loop self play game one prompt public playable games 2026 alternative to Tesana`
- `agentic AI game development platform unattended self playtest game generation long horizon public game demo 2026`
- `"one prompt" "builds" "game" AI "plays" "rebuilds" game platform 2026`
- `site:github.com autonomous game coding agent self-play browser game build one prompt 2026`
- `OpenGame autonomous framework complete playable game from scratch GameCoder-27B OpenGame-Bench official github 2026`
- `site:arxiv.org OpenGame GameCoder-27B Game Skill game generation`
- `site:github.com OpenGame GameCoder-27B game agent`

## 查閱來源與結果

### Rubberhose Ruckus／Tesana LOOP：保留為高價值開放式重跑題與平台專屬實物

- [作者原始 Reddit 貼文與評論](https://www.reddit.com/r/aigamedev/comments/1v9bqzx/ai_made_platformer_trying_long_horizon_prompting/)：貼文日期 2026-07-28。作者在留言公開原始起始 prompt，稱用 Tesana 新 LOOP mode 啟動，讓 agent 約 9 小時無人監督運行後得到第一個輸出；無外加視覺參考。原文另稱可雙人合作、三 Boss、熟手通關約兩小時，並分享可玩的遊戲連結。九小時、玩法範圍、零後續指令都是作者自述，無 run log。
- [Rubberhose Ruckus 官方可玩頁](https://tesana.com/game/rubberhose-ruckus)：官方介紹包含逐線程序繪製角色、rubber-hose 動畫、三階段 Boss、跳躍／dash／八向射擊、粉紅彈反、超級攻擊及三種武器；此 live 版是否與 run 首次 final build 相同未知。
- [留言公開的原始短 prompt](https://www.reddit.com/r/aigamedev/comments/1v9bqzx/ai_made_platformer_trying_long_horizon_prompting/)，要求 2D platformer-inspired boss-rush shooter、procedural 1930s rubber-hose 動畫、多階段 boss、hitboxes、parry、ink textures 和 jazz。三 Boss／合作等資訊超出這段 prompt，不能假裝是 prompt 明訂的需求。
- [Tesana LOOP 官方介紹](https://tesana.com/blog/introducing-loop)及[官方操作說明](https://docs.tesana.ai/building/loop-mode)：確認單次起始 prompt 後可依預設 credit budget unattended 運作，分區建置、critic 判斷、playtest 與返工；文件也明示使用者可以中途 leave a note，因此此 run 的「零介入」無 trace 獨立確認。
- [Tesana agent／模型文件](https://docs.tesana.ai/how-tesana-works)、[Atomos changelog](https://tesana.com/changelog)：官方稱每次 run 可由平台選模型，Atomos 在 2026-07-01 成為新遊戲預設。Reddit 作者稱用專用 game model／engine；留言提及 Atomos，但沒有該 run 的 usage ledger，所以精確 model/version 仍列未核。
- 判斷：高視覺／Boss 戰／高自由 prompt 的重跑素材值得保留；但封閉 LOOP 和自選底模使原作品只能作平台特定例，不是通用 frontier 模型成績。跨模型重跑須在同一套可鎖模的 harness 內重新交付這段 brief。使用者尚未檢視此 build，美術不標通過。

### OpenGame / OpenGame-Bench：由未公開變成已有開源執行架構及具名單 prompt gallery

- [官方 GitHub repo](https://github.com/leigest519/OpenGame)在本次可見內容說明：2026-04-21 release；展示一組從 single prompt 端到端產生的 playable demos，可查看 live build 和生成 source archive。明示空白 folder、headless `opengame -p ... --yolo` 起跑；Game Skill 包含選 skeleton/template 與 Debug Skill，會跑遊戲、檢查 console／互動失敗並修復至 end-to-end playable。主模型支援 OpenAI-compatible `OPENAI_MODEL` 設定，資產／reasoning provider 可獨立配置。本輪也讀了該 repo 的 fork [0xinnovator/opengame](https://github.com/0xinnovator/opengame)；以論文作者的上游 repo 作主要引用。
- 可直接抽取的公開 prompt/build 包含多角色三關動作平台遊戲 [Marvel Avengers: Infinity Strike](https://github.com/0xinnovator/opengame)（3 playable heroes、每角 basic/special/ultimate、3 關與 Thanos 終局）、quiz/card/fighter hybrid、hand-drawn tower defense 等。各 prompt、live demo、source zip 由 repo 圖廊連出。這給不同模型一套固定的 agent 工具、game skills 與驗收 harness，重跑比單純展示玩具更有研究價值；但不是裸模型測試。
- README 中 OpenGame-Bench evaluator 尚標示 evaluation pipeline「will be released soon」，故不能把 paper 報的 150 prompts 整組 benchmark 說成資料已完整釋出；公開圖廊可重跑的 sample prompts/builds 已足夠更新 B0029 的狀態。每個 gallery build 的底模、模型版本及生成日期未逐項標記，不能作模型版本對照。
- 納入為基準／固定 agent harness 與高密度題目來源；不是獨立最新模型 build。使用者美術評價尚未涵蓋圖廊新增遊戲，不推定通過。未將每個 demo 各建 G 記錄，避免把圖廊的所有樣例當成獨立經驗證的成績。

### Code2Games / GameCode4D：新鮮 3D 世界任務及輸出，但初始環境不符核心空白起跑

- [arXiv 論文](https://arxiv.org/abs/2610.05033) (2026-10-04)、[官方專案頁](https://aigeeksgroup.github.io/Code2Games/)、[GitHub](https://github.com/AIGeeksGroup/Code2Games)、[Hugging Face GameCode4D 任務資料](https://huggingface.co/datasets/AIGeeksGroup/GameCode4D)。Dataset 列出 20 個 prompt、10 類場景的兩種版本及配對 Blender `.blend` world；網站提供每題兩份輸出 gameplay video，涵蓋 FPS、Monster Hunt、racing、skiing、Temple、tactical、underwater、flight、block-world、archer 類題型。論文說三種 foundation-model 設定並以視覺／互動忠實度／多模態素材／可玩品質評估。
- 官方執行程序需既有 Code2Worlds Blender 場景、animated FBX NPC、Blender、Hunyuan3D 及 DashScope，輸出 `.blend` gaming world 和 MP4 gameplay video；Unreal Engine 5 是論文的執行驗證端。未確認一般使用者可直接玩的 packaged complete game。
- 判斷：新增 M0025 作重要 3D world-building 方法與任務素材，非一次文字 brief、空白工作區的主 benchmark；是明確有理由的範圍排除／方法補充，不升主候選。

### 同方向查詢排除／線索

- 搜尋 Summer Engine、IdeaToGame、Arcadian、Tanvil 等泛文字遊戲產生平台。命中多是廠商自述「單 prompt」或快生成平台，未找到同時含高系統任務、可驗證自治 QA、可核對模型／run 版本及深度 build 的個案；不新建候選。
- 搜尋命中 Roblox Studio agentic AI、Project Genie 等，但前者是 Studio 多步協作／playtest 工具而非已核的單輸入公開成品；後者偏互動 world model，非可交付一般完整遊戲。本批不作核心題。
- OpenGame 的授權 IP 示例不直接作推薦美術基準；其價值在已發布框架、短 prompt 和可看生成 build，重跑時可將任務另換成原創 IP 而保留機制規格。

## 結論與更新去向

- 新增 [G0237](../records/G0237.md) Rubberhose Ruckus，定位為高價值開放式重跑題／平台專屬原生成績，記錄 exact prompt、Tesana LOOP、作者自述、可玩輸出及模型鎖定限制。
- 更新 [B0029](../records/B0029.md) OpenGame-Bench：固定 headless agent/framework 已可從 repo 重跑，具名 single-prompt gallery 有 live demos/source archives；整個 150 prompt evaluator/data 仍未確認完整公開。
- 新增 [M0025](../records/M0025.md) Code2Games/GameCode4D，記錄公開 20 prompt 任務資料及預生成世界依賴；只作 3D 鄰接方法。
- 更新精選候選說明和 review HTML，將平台限定題與可替換模型的框架分開呈現，不改動 2026-10-06 前使用者已作出的美術驗收結論。
- 下一輪：查 source 公開的完整遊戲 agent task galleries / game jams run artifacts，特別是可直接替換模型、明載自主 playtest 且含完整模型日期的 3D／strategy outputs；先查重 B0029、GameCraft-Bench 與既有 recent showcasess，勿重跑本批 Tesana／OpenGame／Code2Games 查詢。
