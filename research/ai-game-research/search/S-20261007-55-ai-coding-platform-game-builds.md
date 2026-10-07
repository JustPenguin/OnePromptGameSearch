# 搜尋批次 S55：AI coding platform 公開遊戲案例與 agent provenance

**日期／範圍：**2026-10-07；避開 S53 GitHub matched-task 搜索、S51 競賽與 S52 官方發布，查 AI coding platforms（Replit、Bolt、Lovable、Cursor）公開遊戲 showcase／作者案例是否提供可玩的高系統成品及原始 one-task/session。

## 研究問題與先前查重

本批先讀研究索引、候選摘要、搜尋索引及 S50–S54，並用 `manage.py lookup` 查 Bash Fighter／`bashfighter.com`；沒有既有項目。研究假設是平台行銷頁、社群 gallery 或作者案例可能提供近期 playable game 與工具來源，但只有可對應具體任務、模型／agent 條件、交付版本和無中途使用者指示的材料才能升格。S54 已查過 AITHEthing 的 Jumping Jim 小型三平台比較，避免重列同類小遊戲。

## 實際搜尋與查閱

| 實際 query／來源 | 結果、核查及判斷 | 關聯紀錄 | 後續／排除條件 |
|---|---|---|---|
| DuckDuckGo HTML query: `"Replit Agent" game "one prompt" generated game playable 2026`；[Replit Agent docs](https://docs.replit.com/features/agent/overview) | exact one-prompt query 無結果。官方 docs 說明 Replit Agent 可根據 prompt 建置／部署 app，但沒有具名 game run、模型／版本、凍結任務或可檢視 game artifact。| — | exact one-prompt game run/build 和 no-follow-up trace 出現時重查。|
| DuckDuckGo HTML query: `"Lovable" "AI game" prompt playable game coding agent` | 無結果。| — | — |
| DuckDuckGo HTML query: `"Bolt.new" generated browser game prompt playable build AI 2026` | 無結果。| — | — |
| DuckDuckGo HTML query: `"Cursor" "one prompt" game playable generated no follow up coding agent` | 命中 S54 已查過的 AITHEthing「Jumping Jim」小遊戲文章，以及二手 prompt-to-playable 文章、YouTube 標題和 AI-games curated repository；沒有 query result 本身能證明完整任務／no-intervention。| 既有 [S54](S-20261007-54-player-facing-evaluation-coverage.md) | 碰到新的高系統作品後仍需追其第一手 task／run，而非用 curated title 當證據。|
| DuckDuckGo HTML query: `Replit Agent game created from prompt playable browser game 2026`；[Replit AI Game Builder use case](https://replit.com/usecases/ai-game-builder)；[Replit Agent docs](https://docs.replit.com/features/agent/overview) | 直接讀到的 Replit 頁是平台能力／功能宣傳及開始註冊 CTA，沒有具名模型 run、原始單一任務、session 或可獨立辨識 build provenance 的 showcase；官方頁 metadata dateModified 為 2026-09-17，不改變此結論。| — | 官方公開具名 task/build/agent transcript 時再查。|
| [Vibe Mart「Games Built with Replit Agent」](https://www.vibemart.app/learn/games/built-with-replit-agent) | 文章自述教學目標是 prompt、generate、run、test、iterate，再把成熟作品商品化；它沒有列具名 game run 或原始 prompt/session，不能當一次委託證據。| — | 個別 case 有 source／task／first build 時再評。|
| DuckDuckGo HTML query: `Bolt.new AI generated game demo playable`；[Bolt Tower Devpost result](https://devpost.com/software/bolt-tower)；[Bolt.new official site](https://bolt.new/) | DDG 顯示 Bolt Tower Devpost 命中，但直接 page 回 HTTP 403，本研究無法核實其 task、build 或 AI 使用情況；不以標題／snippet下結論。Bolt 官方首頁只稱 AI app builder，沒有具名 game run。| 未確認線索，不新建 | 需要可讀 mirror、原作者 repo 或可玩頁，再核查 task and workflow。|
| DuckDuckGo HTML query: `Lovable AI generated game playable browser AI coding platform`；[Lovable interactive games page](https://lovable.dev/solutions/use-case/front-end-app-interactive-games) | 官方案例頁流程明寫「describe → generate → refine visuals/rules/user flow → publish」，沒有具名 game、model session 或一 prompt 完成證據；流程本身允許迭代，不等同使用者退出。| — | 只有有 frozen build/session 的個別 one-task artifact 再納入。|
| DuckDuckGo HTML query: `Lovable AI generated game playable browser AI coding platform`；curated [Awesome AI-Built Games](https://github.com/lappemic/awesome-ai-built-games) README | 收錄許多 playable AI-built games，包含 Vibe Jam 2026 得獎項與 Bash Fighter；README 只提供 curator 的 AI-built 描述，單項 prompt／model/run 不齊。本批只沿此目錄查 Bash Fighter，沒有把其他未核條目列為 candidate。| [G0267](../records/G0267.md) | 若 curator 對單一作品補原始 task/session，可逐項重查。|
| GitHub Repository API query `Bash Fighter`；[Bash Fighter README](https://github.com/Bash-Entertainment/bash-fighter/blob/main/README.md)、[architecture](https://github.com/Bash-Entertainment/bash-fighter/blob/main/docs/ARCHITECTURE.md)、[roadmap](https://github.com/Bash-Entertainment/bash-fighter/blob/main/docs/ROADMAP.md)、[repo history](https://github.com/Bash-Entertainment/bash-fighter/commits/main)、[live web game](https://bashfighter.com/)、[itch.io](https://bashfighter.itch.io/bash-fighter) | 一手 README 明言日常開發（大部分 repo code 和帳號發文）由代表 owner 工作的 AI agent 持續完成，PR/issues 亦由 agent 審閱。source／architecture／tests 描述 20 玩家 online platform fighter、deterministic fixed-point sim、server-authoritative netcode、lobbies、bot fill、items/hazards、characters、spectator、reconnect；有 live browser、itch、CI/tests。repo created 2026-09-07、於 2026-10-03 有更新。其 AI involvement 是長期/迭代 project attribution，沒有一份起始委託、模型/版本、AI tool harness/session 或 human instruction trace，且 roadmap 說部分 modes 尚未 end-to-end 完成。記為值得追蹤的高系統線索，不是已核 one-shot result。| 新增 [G0267](../records/G0267.md) | 作者若公開原始 brief、模型/agent logs、commit attribution、起迄 frozen artifact，才有機會升格為 run case；否則維持 lead。|

## 結論與更新去向

- Replit/Bolt/Lovable/Cursor 平台 showcase 搜索未找到符合本研究範圍的新模型一次委託成品，也沒有補強現行高候選。**S54 之後第一個無增益方向：1／至少 3。**
- Bash Fighter 是有來源的 research lead 而非弱 candidate：作者公開承認 AI agent 長期寫大部分 code，且具真正的 browser online game/source/test；因它是 ongoing AI-assisted product development，沒有 one-shot 初始委託 provenance，不納入短名單或宣稱 model success。新增 [G0267](../records/G0267.md) 僅供後續有一手 run artifact 時查重。
- Bolt Tower Devpost 403 是存取阻礙，已精確保留；未把它誤判為不符合。 Replit/Lovable 頁為產品功能／迭代指引，不能視為已證明單次交付案例。
- 下一方向：先重讀三份索引，再查**最近兩週公開的 coding-agent 完整軟體／遊戲交付排行榜或作者 run logs 中，有沒有專門的 game tasks、未剪輯 playable artifact 或可核驗 initial/final commits**；避開 AI SaaS builder 產品展示、game jam、GitHub curated lists與 S53 的 generic repo query。
