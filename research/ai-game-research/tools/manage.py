"""Local Markdown record management; Python standard library only."""
import argparse
import hashlib
import html
import json
import re
import unicodedata
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'archive/ai-game-one-shot-research-history-2026-10-04.md'
PREFIX = {'game':'G','benchmark':'B','catalog':'C','event':'E','method':'M'}
LABELS = {'game':'遊戲／具體題目','benchmark':'基準／評測','catalog':'作品庫／平台','event':'活動','method':'方法／鄰接研究'}
META = re.compile(r'^<!-- record-meta: (.+) -->$', re.M)
if hasattr(sys.stdout,'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def norm(s):
    return re.sub(r'[^\w]', '', unicodedata.normalize('NFKC',s).casefold())

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')

def records():
    result=[]
    for p in sorted((ROOT/'records').glob('*.md')):
        match=META.search(p.read_text(encoding='utf-8'))
        if not match:
            raise ValueError(f'Missing metadata: {p}')
        obj=json.loads(match.group(1)); obj['path']=f'records/{p.name}'
        result.append(obj)
    if len({r['id'] for r in result})!=len(result):
        raise ValueError('Duplicate IDs')
    return result

def render_record(obj, body):
    meta=json.dumps(obj,ensure_ascii=False,separators=(',',':'))
    return f'<!-- record-meta: {meta} -->\n# {obj["id"]} · {obj["name"]}\n\n**類型：**{LABELS[obj["type"]]}　**狀態：**{obj["status"]}　**最後整理：**{obj["updated"]}\n\n**別名：**'+('、'.join(obj.get('aliases',[])) or '尚無')+'\n\n'+body

def rebuild():
    data=records()
    write(ROOT/'catalog.json',json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    rows=['# 全項目目錄\n\n此目錄由獨立紀錄產生；可查推薦、待核實、排除項目及平台／研究。完整查找入口是 [可搜尋目錄](catalog.html)。\n\n| 編號 | 名稱 | 類型 | 狀態 |\n|---|---|---|---|']
    for r in data:
        name=r['name'].replace('|','／')
        rows.append(f'| [{r["id"]}]({r["path"]}) | {name} | {LABELS[r["type"]]} | {r["status"]} |')
    write(ROOT/'catalog.md','\n'.join(rows)+'\n')
    payload=json.dumps(data,ensure_ascii=False).replace('<','\\u003c')
    page='''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 遊戲研究 · 全項目目錄</title><style>body{margin:0;background:#f4f6f8;color:#18212f;font:16px/1.6 "Segoe UI","Microsoft JhengHei",sans-serif}main{max-width:1150px;margin:auto;padding:32px 24px}h1{margin-bottom:8px}p{color:#596779}input,select{font:inherit;padding:10px;border:1px solid #d8e0ea;border-radius:8px;background:white}input{min-width:300px}.controls{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0}table{width:100%;border-collapse:collapse;background:white}th,td{text-align:left;padding:12px;border-bottom:1px solid #e5eaf0}th{background:#e7edf5}a{color:#245bc2}small{display:block;color:#6c7989}.count{margin:12px 0}.wrap{overflow-x:auto}</style><main><h1>AI 遊戲研究 · 全項目目錄</h1><p>收錄舊研究中已命名的遊戲、具體題目、正式基準、作品庫及活动。每項標示目前判斷；列入目錄不代表推薦。日期是整理日，歷史證據不視為今日重新驗證。</p><a href="../ai-game-one-shot-index.md">研究索引</a> · <a href="history/index.md">完整歷史段落</a> · <a href="../ai-game-one-shot-review.html">候選檢閱</a><div class="controls"><input id="q" placeholder="搜尋名稱、別名、來源網址"><select id="type"><option value="">全部類型</option><option value="game">遊戲／具體題目</option><option value="benchmark">正式基準</option><option value="catalog">作品庫／平台</option><option value="event">活動</option><option value="method">方法／鄰接研究</option></select><select id="status"><option value="">全部狀態</option></select></div><div id="count" class="count"></div><div class="wrap"><table><thead><tr><th>編號</th><th>名稱與別名</th><th>類型</th><th>狀態</th></tr></thead><tbody id="rows"></tbody></table></div></main><script>const data=PAYLOAD;const labels=LABELS;const q=document.querySelector('#q'),type=document.querySelector('#type'),status=document.querySelector('#status');for(const v of [...new Set(data.map(x=>x.status))].sort()){const o=document.createElement('option');o.value=o.textContent=v;status.append(o)}function draw(){const term=q.value.toLocaleLowerCase().trim();const found=data.filter(x=>(!type.value||x.type===type.value)&&(!status.value||x.status===status.value)&&(!term||[x.id,x.name,...x.aliases,...(x.sources||[])].join(' ').toLocaleLowerCase().includes(term)));document.querySelector('#count').textContent=`顯示 ${found.length} / ${data.length} 項`;const rows=document.querySelector('#rows');rows.replaceChildren();for(const x of found){const tr=document.createElement('tr');for(const value of [x.id,x.name,labels[x.type],x.status]){const td=document.createElement('td');td.textContent=value;tr.append(td)}const a=document.createElement('a');a.href=x.path;a.textContent=x.id;tr.children[0].replaceChildren(a);const s=document.createElement('small');s.textContent=x.aliases.join('、');tr.children[1].append(s);rows.append(tr)}}for(const e of [q,type,status])e.addEventListener('input',draw);draw();</script></html>'''
    page=page.replace('PAYLOAD',payload).replace('LABELS;',json.dumps(LABELS,ensure_ascii=False)+';').replace('活动','活動').replace('正式基準','基準／評測').replace('...(x.sources||[])','...(x.sources||[]),...(x.context_sources||[]),...(x.keywords||[])')
    write(ROOT/'catalog.html',page)
    return data

def migrate():
    if (ROOT/'coverage-report.json').exists():
        raise ValueError('Migration already completed. Use rebuild or validate; original migration is preserved.')
    raw=SOURCE.read_bytes(); lines=raw.splitlines(keepends=True)
    starts=[0]+[i for i,line in enumerate(lines) if i and re.match(rb'^#{1,4} ',line)]
    chunks=[]
    for j,start in enumerate(starts):
        end=starts[j+1] if j+1<len(starts) else len(lines)
        current=start; size=0
        for k in range(start,end):
            if size and size+len(lines[k])>16000:
                chunks.append((current,k));current=k;size=0
            size+=len(lines[k])
        if current<end: chunks.append((current,end))
    sections=[]
    for n,(start,end) in enumerate(chunks,1):
        content=b''.join(lines[start:end]); title=lines[start].decode('utf-8-sig').strip().lstrip('# ').strip()
        if not title or not re.match(rb'^#{1,4} ',lines[start].lstrip(b'\xef\xbb\xbf')):
            title=f'接續研究段落（原始第 {start+1} 行）'
        ident=f'N{n:04d}'; path=f'history/sections/{ident}.md'
        target=ROOT/path; target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(content)
        sections.append(dict(id=ident,title=title,start_line=start+1,end_line=end,path=path,sha256=hashlib.sha256(content).hexdigest()))
    manifest=dict(source=str(SOURCE),source_sha256=hashlib.sha256(raw).hexdigest(),source_bytes=len(raw),source_lines=len(lines),sections=sections)
    write(ROOT/'migration-manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    entries=[]
    for name in ['inventory-early.json','inventory-late.json']:
        entries.extend(json.loads((ROOT/name).read_text(encoding='utf-8-sig')))
    overrides={'8-Bit AI Arena / Ruinseed':'Ruinseed','Ruinseed: The Shattered World':'Ruinseed','Open-World Airship Trader':'Airship Trader','GameCraft-Bench Airship Trader':'Airship Trader','Bastion / BASTIÓN MECHA':'Bastion','Bastion / Bastión Mecha':'Bastion','PacBench / Pac-Man bake-off':'PacBench','AutoUE / PlayGen-20':'AutoUE / PlayGen-20','GameDaily how-it’s-made':'GameDaily'}
    overrides.update({'GameCraft-Bench：Airship Trader':'Airship Trader',
        'KJLKurt Opus waterslide':'Slide Rush','KJLKurt Astra waterslide':'Splashline',
        'Sonnet Fortnite-style Battle Royale':'Fortnite-style battle royale',
        'Hill Climb':'Hill Climb Racing','UE5.8熱帶島嶼休閒開放世界':'UE5.8 tropical open-world island',
        'GPT-6.1 safari範例':'GPT-6.1 Sol jungle safari',
        'Fez風格旋轉平台遊戲':'Fez-style 2.5D game',
        'Opus FPS demo':'FPS團隊槍戰','Opus漂移賽車demo':'QQ飛車風格漂移競速','Opus單車demo':'鵜鶘騎自行車',
        'PUBG案例':'Yuzzy Itaba PUBG-style browser game',
        'GameHorizon Suite':'GameHorizon','A2Z GameSpec-Bench':'A2Z',
        'OpenGame':'OpenGame-Bench','Procedural Pixel Creatures':'Procedural Pixel Creature Workshop',
        'AgentsLoop latest-games':'AgentsLoop awesome-opus-5.5-games',
        'Slapjam AI 48-hour game jam':'Slapjam AI #1','Kart案例':'Kart Blitz'})
    merged={}; input_mapping=[]
    for e in entries:
        original=e['name'];e['name']=overrides.get(original,original)
        e['aliases']=[a for a in e.get('aliases',[]) if a not in ['原作reference','Sonnet 5.5']]
        e['aliases']=list(dict.fromkeys(e.get('aliases',[])+([original] if original!=e['name'] else [])))
        key=norm(e['name'])
        input_mapping.append(dict(original_name=original,canonical_key=key,lines=e.get('lines',[])))
        if key in merged:
            old=merged[key];old['aliases']=list(dict.fromkeys(old['aliases']+e['aliases']));old['lines']=sorted(set(old.get('lines',[])+e.get('lines',[])))
            if e.get('summary') and e['summary'] not in old['summary']:old['summary']+='\n\n'+e['summary']
            if old.get('status')!='推薦' and e.get('status')=='推薦':old['status']='推薦'
        else:merged[key]=e
    curated=(ROOT.parent/'ai-game-one-shot-candidates.md').read_text(encoding='utf-8-sig')
    curated_blocks={}
    for m in re.finditer(r'^### (.+)\n([\s\S]*?)(?=^## |^### |\Z)',curated,re.M):
        title=m.group(1).split(' — ')[0];curated_blocks[norm(overrides.get(title,title))]=m.group(2).strip()
    current={'Ruinseed','MALL ACTION','Kart Blitz','Backrooms','NEON BAY','Armor Alley','Grand Theft Astro','Ancient Beast','Bikini Bottom Survivor','Airship Trader'}
    textlines=[l.decode('utf-8-sig') for l in lines]
    existing_by_name={norm(r['name']):r for r in records()}
    key_ids={}
    for key,e in sorted(merged.items(),key=lambda item:(item[1]['type'],item[1]['name'].casefold())):
        aliases=list(dict.fromkeys([e['name']]+e['aliases']))
        hits=set(e.get('lines',[]))
        for i,line in enumerate(textlines,1):
            if any(a.casefold() in line.casefold() for a in aliases if len(a)>=4):hits.add(i)
        related=[s for s in sections if any(s['start_line']<=line<=s['end_line'] for line in hits)]
        urls=[]
        for line in hits:
            if 1<=line<=len(textlines):urls.extend(re.findall(r'\]\((https?://[^)\s]+)\)',textlines[line-1]))
        source_urls=list(dict.fromkeys(urls))
        typ=e['type'];existing=list((ROOT/'records').glob(PREFIX[typ]+'*.md')) if (ROOT/'records').exists() else []
        ident=existing_by_name[key]['id'] if key in existing_by_name else PREFIX[typ]+f'{max([int(p.stem[1:]) for p in existing]+[0])+1:04d}'
        key_ids[key]=ident
        status='推薦' if e['name'] in current else e.get('status','歷史待整理')
        obj=dict(id=ident,name=e['name'],aliases=e['aliases'],type=typ,status=status,updated='2026-10-06',origin='legacy-migration',sources=source_urls,sections=[s['id'] for s in related])
        body='## 整理判斷\n\n'+e.get('summary','原文有紀錄；目前待整理。')+'\n\n'
        if key in curated_blocks: body+='## 目前候選資料\n\n'+curated_blocks[key]+'\n\n'
        if e['name'] in ['NEON WARDEN','VESPERA']:
            body+='原始作者專案：[Fable / NEON WARDEN](https://nipale-ai.github.io/fable-5-1-one-prompt-game/) · [GLM / VESPERA](https://nipale-ai.github.io/glm-5-3-one-prompt-game/)。先前候選摘要誤連至其他作者文章，此處依舊台帳原始專案段落校正。\n\n'
        body+='## 歷史證據與搜尋紀錄\n\n以下段落保留當時完整內容，可能含舊版推薦；目前狀態以上方紀錄為準。日期為整理日，未在本次重新執行遊戲。\n\n'
        body+='\n'.join(f'- [{s["id"]} · {s["title"]}](../{s["path"]})（舊台帳 {s["start_line"]}–{s["end_line"]} 行）' for s in related)+'\n\n'
        body+='## 後續更新\n\n取得新版本、原始 prompt、首版交付或人工介入證據時，更新本紀錄並在搜尋批次檔留下來源與日期；保留原判斷的變更理由。\n'
        write(ROOT/f'records/{ident}.md',render_record(obj,body))
    for row in input_mapping:
        row['record_id']=key_ids[row.pop('canonical_key')]
    write(ROOT/'migration-name-mapping.json',json.dumps(input_mapping,ensure_ascii=False,indent=2)+'\n')
    data=rebuild()
    rows=['# 歷史研究段落索引\n\n舊台帳逐段遷移在此；每段保留原始文字。段落中的早期排序屬歷史判斷，現行結論請看[研究索引](../../ai-game-one-shot-index.md)。少數原文的本機相對連結以封存檔位置為基準，現行文件入口請使用本索引連結。\n\n| 段落 | 原始行號 | 主題 | 關聯項目 |\n|---|---|---|---|']
    for s in sections:
        refs=[f'[{r["id"]}](../{r["path"]})' for r in data if s['id'] in r.get('sections',[])]
        rows.append(f'| [{s["id"]}]({s["path"].replace("history/", "")}) | {s["start_line"]}–{s["end_line"]} | {s["title"].replace("|","／")} | '+('、'.join(refs) or '共通研究／搜尋內容')+' |')
    write(ROOT/'history/index.md','\n'.join(rows)+'\n')
    validate()

def validate():
    manifest=json.loads((ROOT/'migration-manifest.json').read_text(encoding='utf-8'))
    expected_line=1
    for s in manifest['sections']:
        content=(ROOT/s['path']).read_bytes()
        if s['start_line']!=expected_line or hashlib.sha256(content).hexdigest()!=s['sha256']:
            raise ValueError('Section span/hash mismatch: '+s['id'])
        expected_line=s['end_line']+1
    if expected_line!=manifest['source_lines']+1:raise ValueError('Incomplete line coverage')
    assembled=b''.join((ROOT/s['path']).read_bytes() for s in manifest['sections'])
    if hashlib.sha256(assembled).hexdigest()!=manifest['source_sha256']:raise ValueError('Historical content mismatch')
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest()!=manifest['source_sha256']:
        raise ValueError('Archived source changed after migration')
    data=records(); missing=[]
    for r in data:
        if r.get('origin')=='legacy-migration' and not r.get('sections'):missing.append(r['id'])
        if set(r.get('sections',[]))-{s['id'] for s in manifest['sections']}:
            raise ValueError('Unknown source section: '+r['id'])
    if missing:raise ValueError(f'Records without source sections: {missing}')
    mapping=json.loads((ROOT/'migration-name-mapping.json').read_text(encoding='utf-8'))
    ids={r['id'] for r in data}
    if any(row['record_id'] not in ids for row in mapping):raise ValueError('Unmapped inventory entry')
    report={'historical_bytes':len(assembled),'historical_lines':manifest['source_lines'],'sections':len(manifest['sections']),'inventory_entries':len(mapping),'mapped_inventory_entries':len(mapping),'records':len(data),'types':{t:sum(r['type']==t for r in data) for t in PREFIX},'lossless_history':True,'every_migrated_record_has_source_section':True,'name_inventory_scope':'人工盤點具名案例、題目、基準、平台和活動；泛稱未命名項目仍保留於完整歷史段落。'}
    write(ROOT/'coverage-report.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))

def lookup(term):
    hits=[r for r in records() if term.casefold() in ' '.join([r['id'],r['name']]+r['aliases']+r.get('sources',[])+r.get('context_sources',[])+r.get('keywords',[])).casefold()]
    print(json.dumps(hits,ensure_ascii=False,indent=2))

def new_record(args):
    data=records();names=[args.name]+args.aliases
    duplicates=[r for r in data if set(map(norm,[r['name']]+r['aliases']))&set(map(norm,names))]
    if duplicates:raise ValueError('Already registered: '+', '.join(r['id']+' '+r['name'] for r in duplicates))
    prefix=PREFIX[args.type];n=max([int(r['id'][1:]) for r in data if r['id'].startswith(prefix)]+[0])+1
    obj=dict(id=f'{prefix}{n:04d}',name=args.name,aliases=args.aliases,type=args.type,status='待核實',updated=args.date,origin='new-research',sources=[],sections=[],batches=[])
    body='## 發現與來源\n\n填入原始來源、發現日期與搜尋批次。\n\n## 證據與限制\n\n記錄 prompt、模型／工具、人工介入、首版 build、圖片／影片與測試結果；缺證據者明確寫未核實。\n\n## 判斷與重查條件\n\n寫明推薦／待查／排除理由及下一次重查觸發條件。\n'
    write(ROOT/f'records/{obj["id"]}.md',render_record(obj,body));rebuild();print(obj['id'])

if __name__=='__main__':
    parser=argparse.ArgumentParser();sub=parser.add_subparsers(dest='cmd',required=True)
    for name in ['migrate','rebuild','validate']:sub.add_parser(name)
    find=sub.add_parser('lookup');find.add_argument('term')
    new=sub.add_parser('new');new.add_argument('--name',required=True);new.add_argument('--type',choices=PREFIX,default='game');new.add_argument('--aliases',nargs='*',default=[]);new.add_argument('--date',required=True)
    args=parser.parse_args()
    {'migrate':migrate,'rebuild':rebuild,'validate':validate,'lookup':lambda:lookup(args.term),'new':lambda:new_record(args)}[args.cmd]()
