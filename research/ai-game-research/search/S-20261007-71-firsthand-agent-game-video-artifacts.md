# S71 · 第一手 coding-agent run 的遊戲展示影片與高美術成品

- **日期：**2026-10-07
- **搜尋方向：**查近期 AI coding agent 第一手文章／影片提到的遊戲展示，再追到可玩 build、公開畫面、source 和原始任務；重點檢視 stylized/high-fidelity 美術與大規模遊戲內容。
- **開始前核對：**重讀研究索引、候選摘要及搜尋索引；以 Montanha: Zero Day、Hearthlight、DEV 文章標題查 catalog 和別名。Montanha 已在 G0244，避免重複新增。
- **實際查詢：**DuckDuckGo HTML queries `Anthropic Claude Code game built showcase gameplay`、`site:anthropic.com Claude Code game game development`、`AI coding agent game showcase gameplay 3D 2026`、`"Claude Code Built These Games From One Prompt"`、`"I Built My Dream Game in 72 Hours" Assets by AI Gameplay by Claude Code`、`site:dev.to/tiagovilasboas "Claude Opus 5.5" PWA game token`；follow DEV article links to Hearthlight, GitHub and Reddit; fetch article, GitHub API repo/commit/tree/README, and GitHub Pages landing HTML.
- **查閱來源：**[DEV 作者文章](https://dev.to/tiagovilasboas/i-built-a-full-pwa-game-in-one-day-with-claude-opus-55-and-claude-code-here-is-the-real-token-41p7)、[Hearthlight GitHub Pages](https://hearthlight.github.io/)、[Hearthlight repo](https://github.com/Hearthlight/hearthlight.github.io)、[README](https://github.com/Hearthlight/hearthlight.github.io/blob/main/README.md)、[screenshots](https://github.com/Hearthlight/hearthlight.github.io/tree/main/docs/screenshots)、[文章所引 Reddit post](https://www.reddit.com/r/ClaudeAI/comments/1wtcs7k/i_opensourced_the_cozy_pixelart_game_opus_55_made/)。Google blocked direct search-page content with a JavaScript challenge; YouTube video/oEmbed domains failed at the network tunnel, so surfaced video titles could not be inspected and are not treated as evidence.

## 結果

- **Hearthlight 新增 G0280：**作者文章引用一篇 Opus 5.5 game post，稱 Hearthlight 由 Claude Code + Opus 5.5 + Three.js 建置並經 natural-language playtesting iterations。Repo README、screenshots 和 live Pages 可核：十章、兩大洲、八名角色／最多八人合作，遊戲畫面是完整程序像素風。README 說是 demo、遊戲功能由 test bots 試跑，未經真實玩家完整測試。Reddit post/API 回 403，直接模型歸因、初始任務及 session 沒有核實。故保留 art review／題材參照，非 strict one-shot 案例；美術待使用者評價。
- **Montanha: Zero Day 去重複核：**DEV 文直接給短 initial prompt、Opus 5.5、Claude Code、公開 PWA/source，還說 agent 自行用 Playwright bot 測試並處理 Artlist 資產網路限制；同文也公開作者對角色手感及 Stage 3 的後續指示，以及多輪修正後 bug。它已在 G0244 登錄，本批未有新證據足以改變「多輪／不算 strict one-shot」判斷，沒有新增紀錄。
- DuckDuckGo 搜尋見到 YouTube 標題「Claude Code Built These Games From One Prompt」及 72 小時夢想遊戲標題，但 YouTube 頁與 oEmbed 都因 tunnel 403 無法讀取；因此沒有推論成片內容或新增案例。Anthropic 官網精確查詢只回 creative-work general article，無新的公開 game run。

## 結論與未查事項

- Hearthlight 加入了新的高內容 stylized art review reference，但沒有足夠來源支持一次輸入和未介入；本方向未找到新強 one-shot 完整遊戲候選，也未顯著提升既有案例的嚴格一次輸入證據。是 S54 後第 **17** 個不同無增益方向，研究仍持續。
- 待查：作者 Reddit 原貼因 403 無法直接讀；Hearthlight 原始 prompt、session、model attribution 一手來源；YouTube surfaced video 無法直接讀。若有可用 article mirror／transcript、作者 session 或 snapshot build 再回查。
- **下一方向：**查近期 3D／high-fidelity game-agent 類研究的公開 benchmark artifact gallery 和原始 scoring traces；要求有實際 gameplay screenshot/build，確認任務究竟是生成新遊戲還是修改既有 project，並把 visual quality 與 game/system evaluation 分開。
