// Headless local HTML verification. No network or user browser interaction.
const fs=require('fs');
const path=require('path');
const {chromium}=require('C:/Users/Jeff/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
  const root=path.resolve(__dirname,'..');
  const html=fs.readFileSync(path.join(root,'catalog.html'),'utf8');
  const executables=[chromium.executablePath(),'C:/Program Files/Google/Chrome/Application/chrome.exe','C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'];
  const executablePath=executables.find(p=>fs.existsSync(p));
  if(!executablePath)throw Error('No installed browser executable available');
  const browser=await chromium.launch({headless:true,executablePath});
  try {
    const page=await browser.newPage({viewport:{width:1280,height:900}});
    const errors=[];page.on('pageerror',e=>errors.push(String(e)));
    await page.setContent(html);
    const count=await page.locator('#rows tr').count();
    await page.screenshot({path:path.join(root,'validation/catalog-preview.png')});
    await page.locator('#q').fill('Armor Alley');
    const armor=await page.locator('#rows').innerText();
    await page.locator('#q').fill('MACH RUN');
    const excluded=await page.locator('#rows').innerText();
    await page.locator('#q').fill('');
    await page.locator('#type').selectOption('game');
    const games=await page.locator('#rows tr').count();
    await page.locator('#status').selectOption('排除');
    const onlyExcluded=await page.locator('#rows tr').count();
    await page.setViewportSize({width:390,height:844});
    await page.locator('#status').selectOption('');
    const fits=await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth);
    if(count!==281||games!==184||!armor.includes('G0018')||!excluded.includes('排除')||!onlyExcluded||!fits||errors.length)throw Error(JSON.stringify({count,games,armor,excluded,onlyExcluded,fits,errors}));
    const fixture=Array.from({length:1000},(_,i)=>({id:'TEST'+i,name:'Temporary fixture '+i,aliases:[],sources:[],type:'game',status:'待核實',path:'#'}));
    const fixturePage=await browser.newPage();fixturePage.on('pageerror',e=>errors.push(String(e)));
    await fixturePage.setContent(html.replace(/const data=[\s\S]*?;const labels=/,'const data='+JSON.stringify(fixture)+';const labels='));
    const fixtureCount=await fixturePage.locator('#rows tr').count();
    await fixturePage.locator('#q').fill('Temporary fixture 999');
    const fixtureSearch=await fixturePage.locator('#rows tr').count();
    if(fixtureCount!==1000||fixtureSearch!==1||errors.length)throw Error('1000-entry catalog verification failed');
    const report={records:count,game_filter:games,name_search:true,status_filter:true,mobile_page_fits:fits,fixture_catalog_records:fixtureCount,fixture_search_matches:fixtureSearch,synthetic_data_not_in_research:true,script_errors:errors};
    fs.writeFileSync(path.join(root,'validation/catalog-check.json'),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify(report));
  } finally {await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
