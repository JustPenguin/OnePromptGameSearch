# S68 · 公開 agent session transcript 與一次生成 run

- **日期：**2026-10-07
- **搜尋方向：**查公開 GitHub repository 是否有可對照初始遊戲 task、coding agent transcript、最終 playable build 的完整證據；並查專用 one-shot benchmark 是否有實際具名輸出。
- **開始前核對：**重新閱讀研究索引、候選摘要、搜尋索引；用目錄查重 Torchboy、Code Bench Fun、one-prompt-games，均無既有紀錄。已知 Bash Fighter、newmodel-games、PlaytestArena 等不重做。
- **GitHub Repository search 的實際 query：**
  1. `game generation agent`
  2. `game prototype codex`
  3. `AI game coding agent`
  4. `one-shot game prompt AI`
  5. `LLM game generation playable`
  6. `game agent transcript prompt`
- **查閱來源：**[Torchboy repo](https://github.com/apshoemaker/torchboy)、[README](https://github.com/apshoemaker/torchboy/blob/main/README.md)、[建置說明](https://github.com/apshoemaker/torchboy/blob/main/docs/HOW-THIS-WAS-BUILT.md)、[27-prompt transcript index](https://github.com/apshoemaker/torchboy/blob/main/docs/transcript/README.md)、[第 1 個 prompt](https://github.com/apshoemaker/torchboy/blob/main/docs/transcript/01-i-want-you-to-help-me.md)、[gameplay GIF 1](https://github.com/apshoemaker/torchboy/blob/main/docs/media/discovery.gif)、[gameplay GIF 2](https://github.com/apshoemaker/torchboy/blob/main/docs/media/gate.gif)、[ending GIF](https://github.com/apshoemaker/torchboy/blob/main/docs/media/ending.gif)；[Code Bench Fun repo](https://github.com/GGCryptoh/code_bench_fun)、[README](https://github.com/GGCryptoh/code_bench_fun/blob/main/README.md)、[data schema](https://github.com/GGCryptoh/code_bench_fun/blob/main/docs/SCHEMA.md)、[Cars vs Canyon run JSON](https://github.com/GGCryptoh/code_bench_fun/blob/main/data/runs/cars-vs-canyon.json)、[模型並排 viewer](https://ggcryptoh.github.io/code_bench_fun/run.html?id=cars-vs-canyon)、[Opus 4.8 實際 HTML build](https://ggcryptoh.github.io/code_bench_fun/games/cars-vs-canyon/opus-4.8.html)；[Combyyy/one-prompt-games README](https://github.com/Combyyy/one-prompt-games/blob/main/README.md)。

## 公開證據

### Torchboy

作者公開首個完整 prompt、全部 27 個 human prompt 的 transcript、source、建置與測試說明，以及以實際瀏覽器操作錄製的三段 game GIF。首個任務是等角暗洞穴、火把資源、接近時才揭示的通道、Blender 角色／場景資產與 Three.js browser game。後續經使用者多輪改遊戲機制、美術／音效、debug，最後形成程序生成多層洞穴、收集所有 passage 才解鎖出口、音樂與依玩家路徑寫的故事。

README／HOW-THIS-WAS-BUILT 自述 Claude Code 約 25 小時／兩日、27 個 prompts、793 個 tool calls、無人手打 code；工具統計含 Playwright MCP 286 次、Blender MCP 23 次。作者以真實瀏覽器走關卡、檢查狀態及錄製畫面，並稱測 900 個 cave seeds。此材料是高價值系統任務、3D procedural art 與自主測試參照；27 次 human prompting 不符合 one-shot。coding-agent 的確切 base model/version 未公開；第 8 prompt 提及的 Sonnet 5 是內嵌故事生成 API 選擇，不能當成 Claude Code agent 的版本。三張 GIF 可直接供使用者評價 stylized 3D 美術，尚無 live hosted game；`apshoemaker.github.io/torchboy/` 回 404。新增 [G0277](../records/G0277.md)。

### Code Bench Fun

repo 保存一回合單 completion 的多模型競賽結果、完整 task/system prompt、每個模型輸出 HTML、時間／token／成本／timeline 與 Opus 4.8 source-code judge。Cars vs Canyon (2026-07-05) 是自動播放 2D car physics sim：六列結果、五個 HTML outputs，一列 no HTML；每列記一 turn。評 Works／Fidelity／Polish／Creativity，source prompt 強調視覺 polish。這是一次生成 protocol 和比較 UI 方法參考，任務沒有玩家操作／目標／關卡，判分只讀 source code，不能把 `polish` 當使用者 gameplay-art 評價；模型也非當前最新。

README 一處稱無 retries；runner 同時聲明對截斷 HTML 自動 retry 一次，因此執行規則需區分「模型回合」和底層重試呼叫。Cars vs Canyon 公開 JSON 每 row `turns:1`，仍沒有可核的人類視覺盲評。新增 [B0057](../records/B0057.md) 作 method reference，不列完整遊戲候選。

### 尚未提供作品的 one-shot 倉庫

Combyyy/one-prompt-games README 自述一 prompt／一 reply／無 tools，卻也明說目前沒有任何 game，首場 race 要等 episode 發布。無遊戲、模型結果或 artifact，因此不建候選紀錄；日後有 release 才重查。

其他 repository 搜尋結果多為 AI game-dev 工具、multi-agent 平台、 curated showcase、gameplay agent 或短 prototype，未提供符合規格的新一手 task/session/final artifact，按範圍排除或沿既有紀錄去重。

## 結論與下一步

- 新增 G0277 Torchboy 作高系統題目、公開 trace／測試方法與 stylized 3D 美術參照；其多輪介入已明確保存，不列 one-shot。
- 新增 B0057 Code Bench Fun 作 one-completion 多模型 benchmarking／成本記錄方法；現有 output 是低難度 2D simulation，source-only judge 不能判定實際 gameplay art。
- **計數：**S54 後第 14 個方向，沒有新強 one-shot 完整遊戲候選或既有 one-shot 證據重大提升。Torchboy 在任務與測試 trace 上很有價值，但明確多輪；Code Bench Fun 一回合樣本太簡單且缺視覺盲評。研究仍持續。
- **下一方向：**對照公開 one-shot build 的生成內容與它們聲稱的「final artifact」／實際回合記錄，重查是否有提供 freeze 時點、error-only 修正界線和獨立 gameplay test；優先找有較大系統範圍與原始交付檔的 release。
