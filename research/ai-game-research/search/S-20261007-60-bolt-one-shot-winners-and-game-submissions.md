# 搜尋批次 S60：Bolt One-Shot 名錄及遊戲作品篩查

**日期／範圍：**2026-10-07；依 S59 handoff 查官方 Bolt.new／Devpost One-Shot track 名錄與得獎展示，逐一檢視能辨識為遊戲或互動內容的作品；不再搜通用 AI builder gallery。

## 研究問題與查重

開始前重讀 `ai-game-one-shot-index.md`、`ai-game-one-shot-candidates.md`、`search/index.md`，查 `manage.py lookup 'Bolt Chef'`、`manage.py lookup 'One Shot Prompt Challenge'` 無命中；並回查 G0269 Bolt Tower。研究問題是正式 One-Shot roster 中有沒有比 Bolt Tower 系統更完整、且能看到原始 prompt／AI build trail 的 playable game。

## 實際搜尋與查閱

| 實際 query／來源 | 查核結果與判斷 | 關聯紀錄 | 後續／排除理由 |
|---|---|---|---|
| DuckDuckGo HTML：`site:devpost.com/software "1-Shot Prompt Challenge" game`；`site:devpost.com/software "1-Shot Prompt Challenge" "game" Bolt.new`；`"One-Shot Competition" Bolt.new game tower game`；`site:worldslargesthackathon.devpost.com/software game "1-Shot"` | query 命中 Bolt Tower、RulebookGPT & CosmicTacToe、MathBombs 等可識別遊戲項目；完整篩查名錄見下方。未找到另一款能提供長流程高系統 playable game 加可讀 exact prompt/session 的作品。| [G0269](../records/G0269.md)、新增 [G0270](../records/G0270.md)、新增 [G0271](../records/G0271.md) | 新提交出現更廣系統、可讀模型／prompt／session 時重查。|
| [Bolt.new 官方 awards/winners](https://bolt.new/winners)；[World's Largest Hackathon 官方 rules](https://worldslargesthackathon.devpost.com/rules)；[官方 Hackathon 首頁](https://worldslargesthackathon.devpost.com/)；可讀 [Devpost One-Shot 名錄](https://r.jina.ai/http://bolt.new/winners) | 官方 awards page 有 One-Shot Winners 列表；rules 明確規定單一 prompt，修錯可、加／改功能不可。頁面列有 MathBombs、CosmicTacToe、GameSounder 等；名錄和規則能定義任務限制，但不自動驗證個別 session。Awards page 列的主賽總榜不以 Bolt Tower 為已知得獎項目；不將參賽 track 身分說成主賽得獎。| [G0270](../records/G0270.md)、[G0271](../records/G0271.md) | 找個別 challenge winner/award 裁決而不是套用主賽總排名。|
| [MathBombs submission](https://devpost.com/software/mathbombs)、[MathBombs live game](https://mathbombs.netlify.app/) | HTTP 可讀 Devpost mirror 顯示它是 One-Shot bonus-prize entry；一個反應式算術防守循環，三次生命、Easy/Medium/Hard、炸彈速度設定，離線單頁 build。作者提及難度／流暢動畫打磨，但沒有 prompt/session/model/version；評論者和作者談 Hard 不可玩。遊戲具有真實防守循環但範圍窄、內容少，不適合上限主測，新增 G0270 排除短名單。| 新增 [G0270](../records/G0270.md) | 可留作心算／快速輸入副題，不因競賽 badge 升上限候選。|
| [RulebookGPT & CosmicTacToe submission](https://worldslargesthackathon.devpost.com/submissions/726974-rulebookgpt-cosmictictactoe)、[CosmicTacToe](https://cosmictactoe.xyz/)、[Bolt project link](https://bolt.new/~/sb1-ntt6cudf) | 作者把 CosmicTacToe 明稱 classic tic-tac-toe 的 stylized one-shot；同頁另一個 PDF rulebook assistant 另含 Netlify/Mistral OCR/ElevenLabs，不可算在遊戲系統中。原 Bolt session 須登入。只一種井字棋 loop，低於目標；新增 G0271 排除。| 新增 [G0271](../records/G0271.md) | 若後續有高難度 variant／另一次可讀 run，不與原 classic tic-tac-toe 混作同項。|
| [GameSounder One Prompt](https://worldslargesthackathon.devpost.com/submissions/716483-gamesounder-one-prompt)、[GameSounder build](https://frolicking-heliotrope-7e61c9.netlify.app/) | 具名 one-shot track submission，但實際上是產生／編輯 chiptune loop 的 visual sound sequencer，Devpost 自述「Getting in just One Prompt」並給一條 `make retro game sounds in the browser` brief；它不是待測完整遊戲，按範圍排除。| — | 可另供生成式 game audio 工具研究，不列遊戲成品。|
| [One Shot Prompt Challenge app](https://devpost.com/software/one-shot-prompt-challenge-amyc9v)、[Vimeo demo](https://vimeo.com/1097348245) | 提交者說先讓 ChatGPT 寫一份 one-shot prompt，再 copy 到 Bolt.new；交付是氣候儀表板、互動 story、mini-games／simulation、AI narratives 的多頁 app。它不是一款閉環遊戲，而且包含 pre-generation 用 ChatGPT 的人機／模型流程，與目標遊戲成果範圍不同；不建項。| — | 若其 mini-game 有獨立原始 task/build 再另核。|
| [Bolt Tower Devpost](https://devpost.com/software/bolt-tower)、[session](https://bolt.new/~/sb1-czijj5rv) | 重核既有 G0269；在 official one-shot winner roster 之外，仍自述參加 1-Shot Prompt Challenge 並有 public tower-defense demo。Session 現在導向 Bolt login，無新 evidence，維持待核副候選而非獲獎／驗證 run。| [G0269](../records/G0269.md) | 解鎖可讀 session 和 exact prompt/model/build 再升級。|

## 結論與更新去向

- 官方 one-shot 名錄帶來兩個具名 game entries，但兩者皆是短單循環：MathBombs 是算術炸彈防守，CosmicTacToe 是標準井字棋換皮。分別新增 G0270、G0271 留存 one-shot track 標籤、playable link、不同面向判斷與排除理由，**不列主 shortlist**。
- GameSounder 是 sound sequencer；One Shot Prompt Challenge 是 ChatGPT 寫 prompt 後生成的 climate app；按遊戲範圍排除。
- 未找到新強候選或對現有上限案例的重大補強，S54 以來 no-gain count 繼續。研究仍有 S59 的 CSDN canonical article 線索及 G0269 Bolt session 限制待查；若追不到原文，精確記錄阻礙後再評停搜條件。
