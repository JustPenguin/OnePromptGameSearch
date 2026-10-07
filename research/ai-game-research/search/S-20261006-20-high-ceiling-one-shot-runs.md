# 搜尋批次 S-20261006-20：高難度一次委託成果與評測補充

**日期：**2026-10-06（台北時間）

## 研究問題與先前查重

尋找近期可由第三方直接檢閱的高難度 one-shot 遊戲產物：一次使用者委託、途中無人補指示、AI 可在原任務內自主測試修正、最後有可玩凍結成果。優先查新模型、多系統／高技術挑戰、實際畫面或 build 和清楚評分。開始搜尋前核對研究索引、候選清單及目錄；查重既有 [G0080 Kart Blitz](../records/G0080.md)、[G0140 Sky Reach](../records/G0140.md)、[G0226 Void Explorer](../records/G0226.md)、[B0020 Goldie Bench](../records/B0020.md) 及既有 one-shot 基準，避免把相似「太空到地表」作品或方法項重複推薦。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| `"one prompt" "playable" "game" Claude October 2026 site:reddit.com/r/ClaudeCode` | 命中作者 Nathan Onn 2026-10-02《Kart Blitz》Sonnet 5.5 Max 獨立 run 及原始 Reddit 社群 run。作者公開 prompt、瀏覽器自測修正說明、截圖、影片、可玩版；新文章是加工具和 QA 指令的獨立變體，不和早先 67 分鐘 High run 混算。更新既有紀錄，未重複建遊戲項目。 | [G0080](../records/G0080.md) | 若新增更近期模型的獨立 run，補記 build 與條件；比較前固定 prompt 和 harness。 |
| `"one prompt" "game" GPT-6.1 October 2026 generated playable`；`"single prompt" "game" "playable" Sonnet 5.5 September 2026`；`site:bitsminds.com/news "No Man’s Sky" game brief Oct 5 2026` | 找到 BitsMinds 10 月 5 日 Planet Landing brief 的 Opus 5.5、GPT-6 Astra、Grok 4.7 三份凍結、可在文章內玩的單檔成果。每模型一回、自主運行／測試／修正。由太空無縫飛到真球形星球、著陸、下船步行，還可回船升空；不許第三方庫或引擎。共用任務文字、實際截圖、完成品及單一評者按圖形／物理／聲音／玩法給分。任務很難，但範圍是一段高技術體驗，不含長期任務／經濟／敵人，因此列高難度技術副主測，不取代長流程題。 | 新增 [G0233](../records/G0233.md)；鄰接 [G0140](../records/G0140.md)、[G0226](../records/G0226.md) | 查作者是否釋出逐模型原始 prompt／session、原始 prompt 檔及更近期模型 run；重跑時統一模型工具環境。 |
| `"Opus 5.5 vs GPT-6 Astra vs Grok 4.7" "No Man" playable`；BitsMinds [Lab](https://www.bitsminds.com/lab) | 核對測評協定：同 brief、單次、同產品最高手動 effort；遊戲成題要求模型自行執行、玩測、修正並凍結。文章稱不清理各模型輸出；各自 harness 不同（Claude Code、Codex、Grok Build），評分是作者 hands-on，不是盲測。這個透明人工評分、遊戲可玩成果比只看宣傳剪輯更有查驗價值，但分數不是純模型控制實驗。 | [G0233](../records/G0233.md) | 若後續用同一 harness 重跑並公開 trace，升級公平比較證據；不要直接沿用原 18/11/7 排名。 |
| `AI game benchmark latest models one shot October 2026`；`"one-shot" "full game" AI model "Oct" 2026 game demo` | 找到 [Goldie Bench game task](https://goldiebench.com/tasks/game)：27 模型，全部同一寬泛「make a game」提示、單一 HTML、首輪即展示，21/27 已給分，均分 8.14/10。能看大量模型做簡短網頁街機遊戲，但任務欠缺足夠系統規格和長時自主修正，不符上限主測；作 model breadth／簡短 baseline 參考並更新舊紀錄。 | [B0020](../records/B0020.md) | 若新增明確難題、AI 自主 QA，且公開輸出／rubric，重新判斷能否升級。 |
| `Spec2Game Can LLMs Generate Complete Playable Games Detailed Specifications arxiv 2026` | 2026-10-03 預印本提出 15 個 Pygame 家族、150 個任務變體、14 模型與 3,330 個生成專案，以執行、規格實現、程式品質、使用者品質四面向評估。指出「能跑」不等於遵循規則，也常漏勝負／終止條件。適合借評分方法；不是長流程高美術展示，也未核實有現成公開 build gallery／重跑包。 | 新增 [B0046](../records/B0046.md) | 待代碼、資料及 prompt 公開，或論文正式發表時再評估可重跑性。 |
| 官方模型頁：Anthropic [newsroom](https://www.anthropic.com/news)、OpenAI [GPT-6 Astra](https://openai.com/index/gpt-6-astra/)、Google [model cards](https://deepmind.google/models/model-cards/)、SpaceXAI [Grok 4.7](https://x.ai/news/grok-4-7) | 核對截至 10 月 6 日日期：Anthropic newsroom 列 Sonnet 5.5（9/28）及 Opus 5.5（9/22）；GPT-6 Astra 和 Grok 4.7 於 9 月推出，Google model cards 已列 Gemini 3.8 Flash（9/2）及 3.8 Audio（9/24）。因此 BitsMinds 10/5 題確實很新，但其三個模型 roster 不是所有當前模型；重跑應按可取得的最新 coding-capable 型號擴充，例如加入 Sonnet 5.5／GPT-6.1 Sol／Gemini 3.8 的合適 coding 變體，並記明測試日期。 | [G0233](../records/G0233.md) | 每次正式開測前再查供應商官方型號、effort 設定與可用工具；不可把 10/5 roster 說成全市場完整比較。 |
| `"one prompt" "game" "2026" AI built playable Opus game`；[GamePrompt.ai](https://gameprompt.ai/ai-game-generator)；`Claude Fable 5.5` 預測線索 | 泛搜出多種宣傳「一句生成完整遊戲」的工具／文章，沒有同等可查的單一實際 session、凍結 build 及明確自主 QA；Fable 5.5 搜尋結果是未證實傳聞，不能當已公開模型或案例。僅記為搜尋結果類型，不新增候選。 | 無新增 | 只有找到實際產品頁、可玩的原始 build 和流程證據再查。 |

## 結論與更新去向

- 新增 [G0233 Planet Landing one-shot brief](../records/G0233.md)：推薦使用者檢閱其真實圖像與 playable builds，定位為單段技術上限副測；明確保留其任務範圍窄於長流程遊戲的限制。
- 新增 [B0046 Spec2Game](../records/B0046.md)：方法參考，不當成可以直接驗收的商用風格遊戲候選。
- 更新 [G0080 Kart Blitz](../records/G0080.md) 的 10 月 2 日獨立 run 證據及批次連結；更新 [B0020 Goldie Bench](../records/B0020.md) 的 27 模型最新頁面與低上限題定位。
- 同步研究索引、精選候選及 HTML 檢閱頁，讓候選可一鍵開啟原文和實際作品。
- 未解決：Planet Landing 原始 session 和逐模型 prompt 檔尚無公開連結；不同 agent harness 影響分數；尚未由使用者看圖判定視覺門檻。比較任何模型時應重新確認當前可用的最新模型。
