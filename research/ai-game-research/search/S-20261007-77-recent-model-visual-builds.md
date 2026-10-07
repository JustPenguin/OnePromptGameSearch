# 搜尋批次：近期模型的高視覺 build、source 與 prompt provenance

**日期／範圍：**2026-10-07。沿 S76 指向，找近期 GPT-6.1 Sol、Claude Sonnet 5.5／Opus 5.5 的可玩遊戲原始碼、實際 gameplay 畫面與可核單任務證據；特別補足獨立高權重的美術軸。先讀研究索引、候選摘要、搜尋索引及 S76，查重 C0024、B0055、G0077、G0164、C0003。

## 實際搜尋與查閱

| query／網址 | 結果與證據 | 關聯固定編號 | 後續／重查條件 |
|---|---|---|---|
| DuckDuckGo：`"GPT-6.1 Sol" game "playable" source build 2026` | 回應 HTTP 202 challenge，無法取得可用結果頁；沒有把挑戰頁視為零命中。 | C0024、G0077 | 使用 GitHub API 替代；若搜尋端恢復可用，再查新的 10 月發佈。 |
| DuckDuckGo：`"Claude Sonnet 5.5" game generated playable build source 2026`；`"Claude Opus 5.5" one prompt game playable source build September 2026`；`"GPT-6.1" game jam playable source prompt coding agent` | 三個頁面搜尋方向受同一 HTTP 202 challenge，無可靠 SERP。 | B0055、C0003 | 不把失敗查詢當作來源覆蓋；以下用 source repository API 與原始檔案補查。 |
| GitHub repository search API：`GPT-6.1 Sol game playable`；`Claude Sonnet 5.5 game playable source`；`Claude Opus 5.5 one prompt game source` | Sol query 命中 `PromptEngineer48/gpt-6.1-sol-light-games`，已是 C0024／S50；Sonnet／Opus 的 exact repository searches 無新增遊戲命中。 | C0024、B0055、G0077 | 若出現新 repo 且提供任務／session/build，逐項查版本與是否重複。 |
| GitHub repository search 擴大查找並比對 AgentsLoop repo canonical URL | 找到 `AgentsLoop/awesome-gpt-astra-games`：README 宣稱 945 game units、644 qualifying source repositories、308 WebGL family；GitHub tree 有逐案 notes／screenshots。`awesome-opus-5.5-games` 的連結會指向相同 canonical 作品庫，不另建重複 catalog。 | C0003 | 策展清單作 discovery source，不以其收錄數或評分證明 one-shot。 |
| [AgentsLoop 作品庫 README](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/README.md)、[Turbo Kart Rally note](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/games/turbo-kart-rally/readme.md)、[原始遊戲 repo／prompt](https://github.com/bridge-mind/turbo-kart-rally)、[實際比賽截圖](https://github.com/bridge-mind/turbo-kart-rally/blob/main/docs/screenshots/race.jpg) | README 明示 30 張最佳圖由人工檢閱 composition、scene detail、visual coherence、gameplay readability；僅是 visual impression，不是 runtime playtest 或 AAA 證明。Turbo Kart Rally 策展者給截圖 9.8/10、遊戲 source score 9.3/10；後者依 source／功能／HTTP reachable demo，無 runtime playtest。原始 README 有請五名 Opus 5.5 子代理製作 Mario Kart 類遊戲、不向使用者提問的 prompt；無完整 session trace。畫面是完整可辨識的低多邊形賽車 gameplay，不等於寫實 3A。 | G0164、C0003 | 更新 G0164 截圖與外部 curator score；仍待使用者看實圖評美術，one-shot 仍依作者自述。 |
| [Neural Sight source／README](https://github.com/monstercameron/Neural-Sight)、[公開 demo](https://monstercameron.github.io/Neural-Sight/)、[experiment](https://monstercameron.github.io/Neural-Sight/experiment.html)、[repo capture](https://github.com/monstercameron/Neural-Sight/blob/main/docs/images/nelson-ghost-town.jpg)、[策展 note](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/games/neural-sight/readme.md) | 作者說約 24 小時以 GPT-6 Astra 建立 photographic FPS playground；source 有四個 captured environments、FPS controls、weapon/reload/ball/zombie systems 和 WebGPU demo。README 明說靜態世界使用外部作者 Gaussian-splat captures，手與槍是事前生成的 AI footage。遊戲內 screenshot 可見近距離老車、水塔及日照場景。策展人工最佳圖 9.7/10，遊戲分 9.2/10；不代表使用者或本研究評分。沒找到原始 prompt/session、無 follow-up trace 或凍結首版。 | 新增 G0286、C0003 | 若公開原始 task/session、清楚標示的模型生成資產分界與 frozen build，可重估流程條件；畫面美術待使用者評價。 |
| 排除對照：[Kart Royale note](https://github.com/AgentsLoop/awesome-gpt-astra-games/blob/main/games/kart-royale/readme.md)、其他 top screenshot entries | Kart Royale screenshot 9.5/10 但 game score 7.0/10，較少補足系統／視覺完整度；Silent Meridian、其他 2D／短循環項目不勝過現有候選。作品庫的 curator rating 均不當使用者評價，未為擴大名單而逐項新建。 | C0003、G0164 | 有新的一手 prompt／session 或更高品質 gameplay capture 時再查。 |

## 結論與更新去向

- 新增 [G0286 Neural Sight](../records/G0286.md)，定位為近期高寫實視覺與 FPS 系統參照；不列已核 one-shot 候選。清楚分開外部捕捉世界、預生成 AI 武器影格與遊戲系統來源。
- 更新 [G0164 Turbo Kart Rally](../records/G0164.md)：納入同 repo gameplay screenshot 和策展者人工 9.8/10，明示不是使用者美術判定，也不是 3A 品質證明；未改其零介入只依作者自述的流程判斷。
- 更新 [C0003 AgentsLoop catalog](../records/C0003.md)：記錄新 canonical repo 及人工 screenshot scoring 方法；945／644／308 為作品庫自述的浮動計數，不代表有效 one-shot 案例數。
- 更新 candidate summary、研究索引及 HTML 檢閱頁，供使用者直接看兩張實際遊戲畫面。Neo Sight 的策展 9.7/10 與 Turbo 的 9.8/10 均以 curator score 明確標示。
- 這輪對美術證據有顯著補強（G0164）並增加可直接看圖的 high-visual reference；S77 起「無新強候選且無顯著證據提升」方向計數重設為 0。下一方向不要重查本批 gallery：轉查近期官方模型／agent 公布的 playable build、session export 或真實任務 provenance，優先找 3D／高美術成品以及原始 screenshot/video，並查相對應 repo／日期／artifact。
