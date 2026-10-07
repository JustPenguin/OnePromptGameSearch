# S28｜官方展示頁中的單次委託與自主 Goal run

**日期：**2026-10-07（台北時間）  
**研究問題：**官方模型／agent 團隊是否提供新近、可玩的完整遊戲，並公開初始任務與模型自主迭代方式？其中是否有值得用當前模型重跑的高系統題？  
**先前查重：**先讀研究 README、候選摘要、S26／S27 批次及全目錄；以 G0225（Hollowflux）、G0226（Void Explorer）等已有官方展示作品為背景，本批只新增未登錄作品，不重開舊項目。

## 實際查詢

- `site:developers.openai.com/showcase game GPT-6 Astra game playable`
- `site:developers.openai.com/showcase "GPT-6 Astra" "game" playable`
- `site:developers.openai.com/showcase "Sunwake" game GPT-6 Astra`
- `site:developers.openai.com/showcase "Little Ritual" GPT-6 Astra game`
- `site:developers.openai.com/showcase "physics" game GPT-6 Astra`
- `site:anthropic.com/news game Claude Opus 5.5 game 2026`
- `AI generated game GPT-6.1 Sol playable 2026 demo prompt session`

## 查閱來源與判斷

| 作品／來源 | 已核實材料 | 判斷與處置 |
|---|---|---|
| Phantasy Codex Adventure | [官方任務與 build process](https://developers.openai.com/showcase/phantasy-codex-adventure)、[官方可玩 build](https://phantasy-codex-adventure.openai.chatgpt.site/)、[官方 final result 圖](https://developers.openai.com/showcase/gpt-5-6-phantasy-codex-adventure.webp) | 初始 prompt 直接要求 set an ongoing goal、模型自行創意決策並迭代到 polished／validated／published；階段摘要記錄試玩後擴大 goal、八生態區域 Journey、職業／武器／首領／合約／生存模式和 desktop／phone playtest。高系統、來源具體，值得以最新模型重跑；原成果為 GPT-5.6 Codex，不是最新成績，且逐訊息 trace 未公開。新增 G0242，列為強重跑任務種子；美術等使用者判定。 |
| Tiny Rails Rollercoaster | [官方任務與階段](https://developers.openai.com/showcase/tiny-rails-rollercoaster)、[可玩 build](https://sol-on-rails.openai.chatgpt.site/)、[官方 final result 圖](https://developers.openai.com/showcase/gpt-5-6-tiny-rails-rollercoaster.webp) | 初始 prompt 授權 ongoing goal／多代理／ImageGen；後續反覆調物理和賽道，擴成四種駕駛模式與三個雙向岔道（八種路線），做全流程與物理 QA。更適合高視覺／物理副題，不是長流程完整遊戲主測；無公開逐訊息 trace，原 model showcase 為 GPT-5.6 Codex。新增 G0243，候選摘要待簡述其定位。 |
| Velocity Loop | [官方 build process／可玩頁](https://developers.openai.com/showcase/velocity-loop) | 3D 五賽道玩具車計時賽，包含 Nitro、ghost、四車 garage、賽事與 rewards；頁面記錄反覆 playtest／replay 和 13 個建置階段。系統比 Tiny Rails 窄且沒有公開初始自主 Goal／trace。本輪不另立主候選，作後續查重線索。 |
| Codex Pet Arena | [官方初始 prompt 與 build process](https://developers.openai.com/showcase/codex-pet-arena) | 清楚的單人平台 arena：八隻原創寵物、CPU rivals、蒐集／成長／推擠、動態換圖、power-ups、鍵盤／觸控；多階段測試摘要。單 arena loop 範圍窄於完整 RPG，未見一次自主 goal 的逐訊息稽核，暫不另加強候選。 |
| Time to Fly、Theme Park Builder | [Time to Fly](https://developers.openai.com/showcase/time-to-fly)、[Theme Park Builder](https://developers.openai.com/showcase/theme-park-builder) | 官方頁公開五關軌道重力 puzzle 及等距主題樂園管理 minigame 的 prompt／多輪 build；任務深度與系統量不足以代表使用者要測的遊戲上限，保留為已檢索項目，不作強候選。 |
| Anthropic 近期 model release | [Opus 5.5 release](https://www.anthropic.com/claude-opus-5-5)、[Newsroom](https://www.anthropic.com/news) | 官方 9/22 發布文只概述「多個 Claude 模型以單 prompt 建遊戲，Opus 5.5 在 graphics/polish 得分最高」，沒有公布名稱、prompt、分數表、build 或 evaluator；Sonnet 5.5 於 9/28 發布。可作模型新鮮度來源，但這段遊戲比較無法重現，也沒有比已記錄 Kart Blitz 證據更完整的新增案例。 |
| OpenAI Games showcase | [官方遊戲目錄](https://developers.openai.com/showcase/games?app_type=game&use_case=games) | 找到上述新遊戲與先前已有的 Hollowflux、Little Ritual、Sunwake、Void Explorer。展示頁有豐富 game build 及階段摘要，但多數是多輪 goal 工作，不可僅從頁面默認是一次無人介入的最終 run。 |

## 研究結論與更新

本輪找到一個高價值的全流程重跑種子和一個視覺／物理副題，兩者官方初始任務都直接允許模型持續自主迭代；這種證據比只有作者貼「one prompt」標籤的 repo 具體。不過官方 build-process 摘要不能證明每輪都由 agent 自發、也沒有逐訊息 trace，因此現存成果只標為作者／官方公開過程，不記作已獨立驗證的 no-user-intervention 分數。原始模型為 GPT-5.6 Codex，依使用者偏好應拿初始任務重跑最新型號，而非因原成品官方呈列就照搬成績。

- 新增 [G0242 Phantasy Codex Adventure](../records/G0242.md)：最值得優先用最新模型重跑的長程俯視動作 RPG 任務種子；現有畫面供使用者審美，不代判合格。
- 新增 [G0243 Tiny Rails Rollercoaster](../records/G0243.md)：物理、賽道、多路線和風格化場景副題；不與 Kart Blitz 的主題評估混同。
- 不新增 Velocity Loop、Codex Pet Arena、Time to Fly、Theme Park Builder 為強候選；各自查過的材料與排除理由已記此批，後續只有新首版／trace／模型版本證據才值得重查。
- Anthropic 官方 release 的遊戲比較無 prompt、成品、分數或方法細節；不另建遊戲紀錄，不當可重現評測。

**下一輪方向：**從非官方一手公開 session data／完整對話匯出找 2026 最新模型的一次任務遊戲，而非再掃官方 showcase 或 S27 的 repo／策展清單；先追 G0242、G0243 相似公開 run 是否有作者 session export，再找含凍結 build 和實際玩家畫面的新案例。若沒有 trace，清楚標為作者申報，不因模型新就降低證據門檻。
