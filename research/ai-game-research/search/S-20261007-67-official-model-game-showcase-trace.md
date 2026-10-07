# S67 · 官方模型開發方的近期遊戲 showcase 與任務證據

- **日期：**2026-10-07
- **搜尋方向：**查模型開發方官方 release/showcase sitemap，尋找近期高階模型的實際遊戲 build、原始任務、agent 流程與可檢視 gameplay 畫面；聚焦一手發布頁，不重做 S66 作品庫方向。
- **開始前核對：**重讀研究索引、候選摘要、搜尋索引；用管理工具查重 Playco、GPT-6 Astra、Playbot，均無舊紀錄。
- **實際搜尋查詢：**
  1. `site:openai.com/index game "GPT-6.1" playable game coding agent`
  2. `site:developers.openai.com/codex/showcase game playable GPT-6`
  3. `site:anthropic.com/news game Claude Code playable 3D`
  4. `site:deepmind.google/discover game playable AI-generated world`
  5. `site:blog.google AI-generated games playable coding agent 2026`
  6. `site:github.com AI game repo prompt session 3D 2026 October Claude Code`
- **搜尋引擎限制：**DuckDuckGo 對 HTML 查詢回傳人機驗證 challenge；Google 搜尋回 relay challenge，無可用 result list；Bing 在這些查詢下主要回傳通用遊戲網站，與限定官方來源不符。未把無關結果當成查找成功或證據。改直接查看廠商官方 sitemap／已找到官方頁面。
- **檢視來源：**[Anthropic sitemap](https://www.anthropic.com/sitemap.xml)；[OpenAI sitemap index](https://openai.com/sitemap.xml)、其中 [startup 類別](https://openai.com/sitemap.xml/startup/)、[OpenAI Playco 案例](https://openai.com/index/playco-game-prototyping-with-astra/)、[官方 Vimeo 影片](https://player.vimeo.com/video/1223381989?h=db54ade737)；[OpenAI publication 類別 sitemap](https://openai.com/sitemap.xml/publication/)；DeepMind sitemap endpoint 回應不是可解析 XML，本批未據此建項。

## 結果

OpenAI 於 2026-09-03 發布 Playco 使用 GPT-6 Astra／Playbot 製作三個 playable themed prototypes 的客戶案例。文章稱團隊先從 primitives 建立 unthemed grey box，再做「a few iterations」調整玩法與創意細節，之後從共用底稿產生三款；Playco 說 GPT-6 Astra 一次做出三款，多數 prototype 首次結果可用，一款 cyberpunk build 需要 performance fix，另兩款無額外 iteration。Playbot 連 Unity／Godot，模型可改場景、playtest、驗證與平行工作。OpenAI 另稱 Playco 報告人工修正比前代少 50%。

此案例高度相關於使用者重視的遊戲美術方向：文章提到模型對空間與物件定位、reference-image recreation、Unity 內 responsive UI 及 game feel 的改善；但頁面沒有三個 game build 的 playable links、repo、任務原文、清晰 gameplay screenshots 或版本 hash。50% 指標沒有樣本數、人工修正定義、對照版本或方法，保留為發布方／客戶自述。Vimeo 影片嵌入為 OpenAI 具名的 67 秒片段，但本批沒有取得逐款可玩材料或可評畫面。

「三款一次做出」不能改寫成使用者只發出一次 task：原文明說前面有數次 gameplay／creative iteration；同時沒有原始 prompt、human follow-up trace 或 build freeze。故新建 [G0276](../records/G0276.md) 作近期模型／高難度重跑與藝術軸設計參照，不升主要 one-shot 候選。美術不可評，不據其官方形容判為 3A。

## 排除與待查

- sitemap 內其他命中為 Codex 通用展示、Sora world simulator、理論 GamePad、非遊戲工具等；不能回答完整遊戲一次委託能力。
- Anthropic sitemap 沒發現符合目標的 model game artifact；Google/DeepMind 搜尋索引受到 challenge／不完整 XML 限制，不能宣稱已完整覆蓋這些發布頁。
- 待查 Playco／Playbot 能否釋出一款 build、reference images、初始灰盒與三個主題的 frozen outputs；「一款需要 performance fix、其餘兩款無額外迭代」的分項紀錄、manual fix 統計方法與前代型號；官方是否公開其他有 task 或 session 的高美術 case。
- **計數：**S54 後第 13 個不同方向，沒有新增已核一次委託候選，也未補足既有 one-shot 證據。Playco 有重要方法價值，但不符合研究核心的無追問流程，也無 artifact 可核，計數不重設。研究仍持續。
- **下一方向：**另查公開可檢閱的模型 agent session／提交 trace 倉庫中，作者提供完整初始遊戲 task 且有可玩的最終 build 的案例；只保留能交叉驗證 no-follow-up 與實際畫面的項目。
