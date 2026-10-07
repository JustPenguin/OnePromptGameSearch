# S34 · GPT-6 Astra 社群遊戲 prompt 與飛行實際 build

**日期：**2026-10-07　**研究方向：**社群案例 prompt／成果出處核驗與可重跑任務價值

## 研究問題

檢查 GPT-6 Astra 社群 prompt 集中的黑暗奇幻 ARPG、完整飛行循環與 playable battle 案例，確認原始任務、遊戲範圍、實際 build／來源欄位及是否有生成過程證據；另查已有 28 個模型 build 的 Flightsim 是否足以作為使用者所要求的「一次委託後 AI 可自我修正」上限題。

## 實際查詢

- `"2096637091627364531" Three.js dark fantasy RPG live demo`
- `"2096236137266512181" browser flight simulator demo`
- `site:goldiebench.com/tasks/flightsim FlightSim 28 models`
- `GPT-6 Astra game prompts dark fantasy flight simulator one shot playable demo`
- `GPT-6 Astra community game prompts playable flight simulator dark fantasy RPG`

## 查閱來源與發現

| 項目 | 核對結果 | 判斷／台帳 |
|---|---|---|
| GPT-6 Astra 遊戲案例與 prompt 策展 repo | README 自述整理 418 個 community cases、26 個可重現 recipe 和 6 個 playbook，個案連回 X 原帖；其 snapshot 日期為 2026-09-17。Featured 區把 Flight Simulator、Dark-Fantasy ARPG 和 Kaiju City Battle 當學習案例。策展收錄不等於每個作品都有成品或可重現 run。 | [repo README](https://github.com/yangzhou-chaofan/awesome-gpt6-astra-game-prompts)。B0045 為方法／線索來源，非生成結果排名。 |
| Browser Flight Simulator with a Complete Flight Loop（G0198） | 原 prompt 有機場、可控飛機、節流／俯仰／滾轉／偏航／煞車、基本慣性與飛行物理、起飛／繞場／落地、失敗重開、HUD、開始與成績頁；明確要求模型自行測完整循環並修正。策展 repo 的原始 case metadata `live_demo` 空白，僅列 image preview。 | 高品質 flight-loop brief，可按原規格交現行模型重跑；不是已證實成品，也未證明 prompt 中的自測要求確實執行。更新 [G0198](../records/G0198.md)。 |
| Three.js dark-fantasy action RPG（G0197） | 原 prompt 指定俯視斜角相機、森林侵蝕的哥德聖所、盔甲騎士披風與符文武器、移動／斬擊／翻滾／格擋／治療／魔法、守衛與鹿角騎士 Boss、繁中 HUD、裝備、勝敗重開，並要求自行製作資產、反覆 playtest 與修正。case metadata 的 `live_demo` 空白、`media_type=image`。 | 藝術方向強，但任務沒有完整角色成長／長流程規格，原 run build 與 session 均未確認；不升成實測成績。其高層視覺與動作 brief 可作副題重跑，但 G0049 等現有任務系統更明確。更新 [G0197](../records/G0197.md)。 |
| Kaiju City Battle | Featured 列有 Netlify 可玩連結，repo 也保存 X 原帖 prompt；現有 prompt 僅短句要求用 Three.js 做 Kaiju 戰鬥、生成怪獸模型／音效及可讀的巨物尺度戰鬥場景。沒有足以證明長流程、複數互依系統或自主修正的公開資料。 | 有畫面的短戰鬥案例；不因「可玩」或 featured 標籤升成上限主測。只列本批排除／題型參照，避免以弱內容增加名單。 |
| Goldie Bench Flightsim（G0249） | 任務是一句固定 prompt：`Flight Simulator — take off, fly over terrain, full flight HUD, land on the runway.` 頁面宣稱 28 次嘗試、23 個有分、平均 7.61/10，連到各首輪單 HTML；明示 no iteration、無 system prompt 範例。方法為能否執行、是否符合 brief、外觀 polish 三軸平均，分數由作者參考其他比較指南並以 eyeball 評估。Fusion 8.7 標 `showcase · game-director`，內部模型組成／harness 不透明。公開 roster 沒有 GPT-6 Astra 或 GPT-6.1 Sol。 | 保存為視覺與飛行物理校準副題，不是自主 QA／完整遊戲上限題。作者的模型分數不是盲評，亦不代表自主迭代能力。見 [G0249](../records/G0249.md)。 |

## 排除與邊界

- Astra 社群案例頁用「one prompt」描述或在 prompt 內寫「自己測試修正」，都不能證明實際 run 沒有人類 follow-up 或真的執行了 QA。
- Dark-Fantasy ARPG 只有靜態預覽，不能拿來當成品畫面驗收；flight prompt 同樣沒有原作者 playable build 對應證明。
- Kaiju City Battle 有 playable URL，但公開 task 範圍短，並缺生成流程與自主修正 evidence，故只作短題參照。
- Goldie Flightsim 的 28 個 build 對比較首輪視覺輸出有用，但 no-iteration 協定與狹窄飛行循環不符合主要測試目標；它未含最新 frontier roster。
- 本輪未找到可升格為「已有證據證明一次委託、AI 無人類介入自主修正、交付完整高系統遊戲」的新成品候選。保留有足夠詳細原始 prompt 的 G0197／G0198，因為它們可用最新模型重跑。

## 待查

1. 若 X 原作者後續公開 dark-fantasy 或 flight-sim live build／完整 Codex trace，重新核驗是否為原任務停止時的交件。
2. Goldie Bench 若增加 GPT-6 Astra／GPT-6.1 Sol 且公開固定模型、harness 與可核查操作結果，再更新 roster 狀態；其短循環限制仍在。
3. 下一搜尋方向轉向近期公開的 autonomous gameplay agent runs，判斷其中是否有可轉用的客觀流程／任務測法；遊玩既有作品不算遊戲生成成績。
