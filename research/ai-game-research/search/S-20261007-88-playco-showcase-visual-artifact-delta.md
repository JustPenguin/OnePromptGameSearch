# 搜尋批次：Playco／GPT-6 Astra 官方 showcase 可見畫面與發布附件覆查

**日期／範圍：**2026-10-07。沿 S87 預定方向，直接下載 OpenAI Playco／GPT-6 Astra 案例頁、startup sitemap 與 Vimeo embed metadata，確認是否有未記錄的 playable links、repo、task artifact、逐款 gameplay frames 或頁面更新。與 S67 內容查讀不同，本批檢查官方頁面實際 HTML／分享圖與影音附件。

## 實際 query 與查看來源

| query／來源 | 結果及檢視 | 納入／排除理由 |
|---|---|---|
| HTTP GET `https://openai.com/index/playco-game-prototyping-with-astra/`（2026-10-07 取回 419,384-byte HTML），抽取 canonical、og/twitter tags、頁面章節、外連 URL 與敘述 | canonical 仍是 S67 記錄的案例頁；正文仍說先建立 grey-box，再做 “a few iterations” 後產生三款 themed prototypes。可機器擷取的 media embed 是 Vimeo `1223381989`，未見新增 source repository、公開 build、prompt、session、模型 run ID 或 downloadable task。 | 沒有新的一對一任務／輸出／run artifact；確認頁面仍需區分 grey-box 與後續迭代。 |
| 取下頁面 `og:image`／`twitter:image`：`https://images.ctfassets.net/kftzwdyauwt9/28ZM0n7QF2RlXDOMBkLgXY/d47e2a4059f529c346950b385b9430a5/playco-astra-seo-image-option-b.png?w=1600&h=900&fit=fill`，檢視 1600×900 PNG | 圖片為 OpenAI 與 Playco 標誌及抽象光色圖形；不是遊戲 screenshot、prototype capture 或 3D artwork。 | 不納入遊戲美術評級；避免把官方 campaign graphic 誤標為 gameplay evidence。 |
| GET `https://openai.com/sitemap.xml/startup/`，篩選 Playco／Astra／game URL | sitemap 含 Playco 案例頁與數篇 Astra 商業案例，未見新增 Playco game build 或 artifact URL。 | 只能表示該 sitemap 抽查結果，不宣稱其他域名沒有相關發布。 |
| GET `https://player.vimeo.com/video/1223381989?h=db54ade737` | Vimeo embed 頁仍是官方 hero video；沒有從 embed 頁取得可下載逐款 build、任務或 source link。 | 影片是已知發布附件，未帶來可核 task/session/frozen output。 |

## 結果與計數

- 沒有新強 one-shot 候選，也沒有顯著提升 G0276 的模型版本、原始任務、可玩性或美術證據。官方分享圖只是品牌主視覺；已知流程仍包含 gameplay／creative iterations，三款 prototype 沒有公開逐款 build。
- S83 後第 5 個不同無增益方向（S86 為第 3、S87 第 4）：**5／至少 3**。研究仍未結束；此數字只代表已完成最低的無新增方向覆蓋要求，不代表其他值得追查線索已結清。
- 下一方向：檢查 GamesByAI/C0027 目錄新提交或上游 creator posts，尋找新增的 Unity／Unreal 可玩項目中具名模型版本、原任務和可對照 gameplay screen recording 的作品；若只有 curated thumbnail 或作者聲明，仍作線索而非成績。
<!-- record-meta: {"id":"S-20261007-88","type":"search","updated":"2026-10-07"} -->
