// IC8TEM'S SOFTWARE FARM – language picker and download finder
var LANGS = ['it','en','fr','de','es','pt','hi','ja','zh','id'];
function langPath(l){ return l === 'it' ? '/' : '/' + l + '/'; }
function pickLang(l){ try{ localStorage.setItem('lang', l); }catch(e){} location.href = langPath(l) + location.hash; }

(function(){
  // first visit on the Italian root page: go to the visitor's language if the site has it
  if (window.LANG === 'it' && location.pathname === '/') {
    var saved = null; try{ saved = localStorage.getItem('lang'); }catch(e){}
    var want = saved || (navigator.language || 'it').slice(0,2).toLowerCase();
    if (want !== 'it' && LANGS.indexOf(want) >= 0 && !/[?&]lang=it/.test(location.search)) { location.replace(langPath(want) + location.search + location.hash); return; }
  }
  var T = window.T, sel = document.getElementById('f-sys'); if (!sel || !window.DL) return;
  var res = document.getElementById('f-res'), tab = document.getElementById('f-tab'), q = document.getElementById('f-q'), cnt = document.getElementById('f-cnt');
  var progs = ['YA-NEC','YA-MS','YAEC','E-LAYER ANALYZER','IP-TRX-CTRL'];
  var pref = ['setup','dmg','appimage','portable','deb','rpm','arch','txz','app','zip'];
  function guess(){
    var u = navigator.userAgent, p = (navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || '';
    if (/Windows/i.test(u)) return /ARM64|aarch64/i.test(u) ? 'winarm' : (/Windows NT 6\./.test(u) ? 'win7_64' : 'win64');
    if (/Mac/i.test(p) || /Macintosh/.test(u)) return 'mac_arm';
    if (/aarch64|arm/i.test(u + p)) return 'rpi64';
    if (/Linux/i.test(u)) return 'lin64';
    return 'win64';
  }
  function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function auto(k){ var a = DL_AUTO[k]; return '<span class="' + (a ? 'yes' : 'no') + '">' + (a ? T.js.yes : T.js.no) + '</span>'; }
  Object.keys(T.sys).forEach(function(k){ if (k === 'other') return; var o = document.createElement('option'); o.value = k; o.textContent = T.sys[k]; sel.appendChild(o); });
  sel.value = guess();
  function show(){
    var s = sel.value, out = '';
    progs.forEach(function(p){
      var f = DL.filter(function(r){ return r.p === p && r.s.indexOf(s) >= 0; }).sort(function(a,b){ return pref.indexOf(a.k) - pref.indexOf(b.k); });
      out += '<div class="r"><b>' + p + ' <small>' + (f[0] ? f[0].v : '') + '</small></b>' +
        (f.length ? f.map(function(r){ return '<a href="' + r.u + '">⬇️ ' + esc(r.f) + '</a><small>' + T.kind[r.k] + ' · ' + T.js.auto + auto(r.k) + '</small>'; }).join('') : '<small>' + T.js.na + '</small>') + '</div>';
    });
    res.innerHTML = out;
  }
  function table(){
    var t = q.value.toLowerCase().split(/\s+/).filter(Boolean), n = 0, h = '';
    DL.forEach(function(r){
      var sys = r.s.map(function(k){ return T.sys[k]; }).join(' · ');
      var hay = (r.p + ' ' + r.v + ' ' + sys + ' ' + r.e + ' ' + r.s.join(' ') + ' ' + T.kind[r.k] + ' ' + r.k + ' ' + r.f).toLowerCase();
      if (t.every(function(w){ return hay.indexOf(w) >= 0; })) { n++; h += '<tr><td>' + r.p + ' ' + r.v + '</td><td>' + sys + '</td><td>' + T.kind[r.k] + '</td><td>' + auto(r.k) + '</td><td><a href="' + r.u + '">' + esc(r.f) + '</a></td></tr>'; }
    });
    tab.innerHTML = h; cnt.textContent = n + T.js.of + DL.length;
  }
  var pp = new URLSearchParams(location.search).get('p'); if (pp) q.value = pp.replace('E-LAYER-ANALYZER', 'E-LAYER ANALYZER');
  show(); table(); sel.onchange = show; q.oninput = table;
})();
