/* S12 demo: left-to-right soft green-list watermark (Kirchenbauer et al., ICML 2023),
   drawn in the visual style of the dgMARK site animation but NOT its diffusion order.
   Data: watermark-demo-data.js (generated + checked by generate-figures.py).
   Loops only while its slide is .active; restarts from the first step on re-entry.
   Controls: on-slide buttons, or P (pause/resume) and R (restart) while the slide is shown.
   Static frame (print, prefers-reduced-motion, no JS timers): finished sentence +
   the second position's candidates after the boost, with the red word selected. */
(function () {
  var D = window.YM_DEMO;
  var root = document.querySelector('.ym-demo');
  if (!D || !root) return;
  var slide = root.closest('.slide');
  var sentence = root.querySelector('.ym-demo-sent');
  var rowsBox = root.querySelector('.ym-demo-rows');
  var head = root.querySelector('.ym-demo-head');
  var pauseBtn = root.querySelector('.ym-demo-pause');
  var restartBtn = root.querySelector('.ym-demo-restart');

  // Phase durations (ms): neutral, split, boost, select, append; then final hold.
  var PH = [2000, 2000, 2200, 1600, 1400];
  var HOLD = 3600;

  var step = 0, phase = 0, timer = null, paused = false;

  function chip(text, cls) {
    var s = document.createElement('span');
    s.className = 'ym-w ' + (cls || '');
    s.textContent = text;
    return s;
  }

  function drawSentence(nDone, withSlot) {
    sentence.innerHTML = '';
    sentence.appendChild(chip(D.prefix, 'ym-w-pre'));
    for (var i = 0; i < nDone; i++) {
      var st = D.steps[i];
      var g = st.cands.filter(function (c) { return c.w === st.pick; })[0].g;
      sentence.appendChild(chip(st.pick, g ? 'ym-w-g' : 'ym-w-r'));
    }
    if (withSlot) sentence.appendChild(chip('?', 'ym-w-slot'));
  }

  function drawRows(st, ph) {
    rowsBox.innerHTML = '';
    st.cands.forEach(function (c) {
      var row = document.createElement('div');
      row.className = 'ym-demo-row';
      if (ph >= 1) row.classList.add(c.g ? 'is-g' : 'is-r');
      if (ph >= 3 && c.w === st.pick) row.classList.add('is-pick');
      var p = ph >= 2 ? c.p1 : c.p0;
      row.innerHTML =
        '<span class="ym-demo-mark">' + (ph >= 3 && c.w === st.pick ? '▶' : '') + '</span>' +
        '<span class="ym-demo-word"></span>' +
        '<span class="ym-demo-grp">' + (ph >= 1 ? (c.g ? '초록' : '빨강') : '') + '</span>' +
        '<span class="ym-demo-track"><span class="ym-demo-ghost" style="width:' + (c.p0 * 1.6) + '%"></span>' +
        '<span class="ym-demo-bar" style="width:' + (c.p0 * 1.6) + '%"></span></span>' +
        '<span class="ym-demo-val">' + p + '%</span>';
      row.querySelector('.ym-demo-word').textContent = c.w;
      rowsBox.appendChild(row);
      if (ph >= 2) {
        var bar = row.querySelector('.ym-demo-bar');
        if (ph === 2) {             // animate p0 -> p1 on entering the boost phase
          void bar.offsetWidth;
        } else {
          bar.style.transition = 'none';
        }
        bar.style.width = (c.p1 * 1.6) + '%';
      }
    });
  }

  function render() {
    root.classList.remove('is-final');
    if (step >= D.steps.length) {     // finished sentence hold
      root.classList.add('is-final');
      drawSentence(D.steps.length, false);
      head.textContent = '완성된 문장';
      rowsBox.innerHTML = '';
      return;
    }
    drawSentence(phase >= 4 ? step + 1 : step, phase < 4);
    head.textContent = (step + 1) + '번째 단어 후보';
    drawRows(D.steps[step], phase);
  }

  function tick() {
    timer = null;
    if (paused || !slide.classList.contains('active')) return;
    if (step >= D.steps.length) { step = 0; phase = 0; }
    else if (++phase >= PH.length) { phase = 0; step++; }
    render();
    schedule();
  }

  function schedule() {
    clearTimeout(timer);
    timer = setTimeout(tick, step >= D.steps.length ? HOLD : PH[phase]);
  }

  function restart() {
    step = 0; phase = 0;
    render();
    if (!paused) schedule();
  }

  function setPaused(v) {
    paused = v;
    pauseBtn.textContent = paused ? '▶ 재생' : '❚❚ 일시정지';
    root.classList.toggle('is-paused', paused);
    if (paused) { clearTimeout(timer); timer = null; } else schedule();
  }

  function staticFrame() {             // representative still: red pick at position 2
    drawSentence(D.steps.length, false);
    head.textContent = '2번째 단어 후보 (예시)';
    drawRows(D.steps[1], 3);
  }

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  staticFrame();
  if (reduce) { root.classList.add('is-static'); return; }

  function onActive() {
    if (slide.classList.contains('active')) { setPaused(false); restart(); }
    else { clearTimeout(timer); timer = null; staticFrame(); }
  }
  new MutationObserver(onActive).observe(slide, { attributes: true, attributeFilter: ['class'] });
  window.addEventListener('beforeprint', function () { clearTimeout(timer); timer = null; staticFrame(); });
  window.addEventListener('afterprint', onActive);

  pauseBtn.addEventListener('click', function (e) { e.stopPropagation(); setPaused(!paused); });
  restartBtn.addEventListener('click', function (e) { e.stopPropagation(); restart(); });
  document.addEventListener('keydown', function (e) {
    if (!slide.classList.contains('active')) return;
    if (e.key === 'p' || e.key === 'P') setPaused(!paused);
    else if (e.key === 'r' || e.key === 'R') restart();
  });
  onActive();
})();
