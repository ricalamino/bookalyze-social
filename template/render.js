const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(let i=1;i<=6;i++){await p.goto('file://'+__dirname+'/posts/post'+i+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);await p.screenshot({path:__dirname+'/posts/post'+i+'.png'});}
await b.close();})();
