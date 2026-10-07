# 搜尋批次：MoxRide／MIDWAY 1942 的 source、build history 與版本對照

**日期／範圍：**2026-10-07。依 S89 的下一步，直接檢查 MoxRide 官方／itch project page、作者 GitHub 帳號及 playable embed，並檢查 MIDWAY 1942 live static HTML／bootstrap asset、其作者公開 GitHub repo 清單與投稿連結，尋找 source、release history、凍結首版／終版對照。重點是補強 G0296／G0297 的視覺 artifact 可查程度與生成歷程界線。

## 實際 query 與來源

| query／來源 | 結果與證據 | 判斷 |
|---|---|---|
| GET `https://moxazza.itch.io/`、`https://moxazza.itch.io/moxride`、`https://www.moxride.com/` | MoxRide 官方頁連 itch.io；itch page 提供 900×900 HTML5 embed，實際 iframe 指向 `html-classic.itch.zone/html/19572615/moxridelootlockerglobaltop10-1.vercel.app/index.html?v=1791175362`，另有 YouTube embed `KzEMPJ7_84s`、三張 screenshot links。Moxazza GitHub API `GET /users/Moxazza/repos?per_page=100&sort=updated` 回空清單。 | 作品比 S89 已知的單張 creator capture 有更豐富可檢視材料，但 itch 頁未提供 source archive／agent session／frozen hash。三張 image files 是遊戲中下坡、rail trick、pause/help menu frames，可增強 art/UI inspection。 |
| 下載 itch 原圖：`https://img.itch.zone/aW1hZ2UvNTEwNDM5Ny8zMDU1ODI1Mi5wbmc=/original/2GjlDZ.png`；`https://img.itch.zone/aW1hZ2UvNTEwNDM5Ny8zMDU1ODI1MS5wbmc=/original/Pw6IRL.png`；`https://img.itch.zone/aW1hZ2UvNTEwNDM5Ny8zMDU1Nzc0MS5wbmc=/original/yP7Yev.png` | 三圖像素為 1002×862、715×412、712×415；可見角色、建築、滑板路線、遠景、連段 HUD 及 pause/help 面板。這些是 itch screenshot gallery，不是 3A certification，也沒有單張 capture 日期／版本說明。 | G0296 的 gameplay/art evidence 顯著增補；不能只看 landscape thumbnail。仍待使用者按偏好評價，三次畫面 follow-ups 的 one-shot 排除不變。 |
| `GET https://api.github.com/users/xilinnihao-afk/repos?per_page=100&sort=updated`；[MIDWAY page](https://ihca.cn/midway/)；`GET /midway/boot.js?v=c29d912b0c8c`、`/midway/styles.css?v=c29d912b0c8c` | 作者公開 repo 為 `tidewater`、`sandline-threejs-fps`，未見 MIDWAY source repo。current page 的 CSS／JS import map 使用 `?v=c29d912b0c8c`; boot.js 以 online import `./js/main.js`，offline 會載入 embedded bundles。沒有 `sourceMappingURL` 或連往 GitHub source 的 page link。 | 這個 query tag 可以在 2026-10-07 重訪目前 live modules，但無證據證明是 9/29 capture 使用的版本；沒有原始 prompt/session 或 source history。 |
| [MIDWAY author disclosure](https://github.com/MartinDelophy/awesome-gpt-6-astra/issues/110#issuecomment-5893086419)、Zhihu article `https://zhuanlan.zhihu.com/p/2087823478498116983`、WeChat article `https://mp.weixin.qq.com/s/-V5OZM4e0EPeYJ9uuZvlxg` | 公開 author disclosure 已摘要 2026-09-27 十條多輪 context。直接開發文章 fetch 分別回 HTTP 403 和 tunnel 403，本批未閱讀原文，故只引用 issue comment 的作者摘要。 | 將文章內容標明不可查閱，不從 URL 標題延伸未讀細節；待有可讀鏡像或原始公開 repo 再追。 |

## 結果與後續

- MoxRide 的 itch gallery 增加三張較大、不同遊戲狀態的實際 screenshot，顯著提升 G0296 的可評圖像證據；已將 screenshots、公開 embed 與限制更新至個案和 review HTML。它仍因作者明示三次 graphics follow-up 而非 one-shot。
- MIDWAY current static build 可用 `c29d912b0c8c` 追訪當下 web assets，但不能當 9/29 capture hash；source repo／session 未找到，作者文章在本執行環境不可讀。G0297 仍為多輪開發參照。
- 這是 S89 後**顯著補強現有案例視覺證據**，no-gain 連續計數重設為 **0／至少 3**；仍沒有新的 strong one-shot candidate，研究繼續。
- 下一方向：查公開的 3D game artist-quality／gameplay user-evaluation benchmark 或 human preference datasets 是否能提供可重用美術 rubric、真實 playthrough frame 與高 fidelity generated game samples；將 user-art rating 與 benchmark judge score 分離。
<!-- record-meta: {"id":"S-20261007-90","type":"search","updated":"2026-10-07"} -->
