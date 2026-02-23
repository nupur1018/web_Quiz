/* =====================================================
   WebDev Quiz — app.js
   Full quiz engine: topics, questions, timer, results
   ===================================================== */

// ── State ─────────────────────────────────────────────
const state = {
  topics:       [],       // topic metadata from API
  selectedTopics: [],     // user-selected topic IDs
  difficulty:   'easy',
  qCount:       5,
  playerName:   '',

  questions:    [],
  answers:      [],
  explanations: [],
  current:      0,
  score:        0,
  answered:     false,
  timer:        null,
  timeLeft:     0,
  timeTaken:    [],
  topicResults: {},       // { topicId: { correct, total } }
};

// ── DOM Helpers ───────────────────────────────────────
const $ = id => document.getElementById(id);

function showScreen(name) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  $(`screen-${name}`).classList.add('active');
}

let toastTimer;
function toast(msg, type = 'ok') {
  const el = $('toast');
  el.textContent = msg;
  el.className = `toast ${type} show`;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => el.classList.remove('show'), 3200);
}

function escHtml(s) {
  return String(s || '')
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

// ── Load Topics from API ──────────────────────────────
async function loadTopics() {
  try {
    const res  = await fetch('/api/topics');
    const data = await res.json();
    state.topics = data.topics || [];
    renderTopicCards();
  } catch (e) {
    toast('Could not load topics. Is Flask running?', 'err');
  }
}

// ── Render Topic Cards ────────────────────────────────
function renderTopicCards() {
  const grid = $('topicsGrid');
  grid.innerHTML = state.topics.map(t => `
    <div class="topic-card" id="tc-${t.id}" data-id="${t.id}"
         style="color:${t.color};" onclick="toggleTopic('${t.id}')">
      <div class="topic-emoji">${t.emoji}</div>
      <div class="topic-name">${t.name}</div>
      <div class="topic-count">${t.count} questions</div>
    </div>
  `).join('');
}

function toggleTopic(id) {
  const idx = state.selectedTopics.indexOf(id);
  if (idx === -1) state.selectedTopics.push(id);
  else            state.selectedTopics.splice(idx, 1);

  document.querySelectorAll('.topic-card').forEach(c => {
    c.classList.toggle('selected', state.selectedTopics.includes(c.dataset.id));
  });

  const btn = $('startBtn');
  btn.disabled = state.selectedTopics.length === 0;
  btn.textContent = state.selectedTopics.length === 0
    ? 'Select at least one topic to start →'
    : `Start Quiz (${state.selectedTopics.length} topic${state.selectedTopics.length > 1 ? 's' : ''}) →`;
}

// ── Settings (opt buttons) ────────────────────────────
document.querySelectorAll('.opt-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const group = btn.dataset.group;
    document.querySelectorAll(`.opt-btn[data-group="${group}"]`).forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    if (group === 'diff')   state.difficulty = btn.dataset.val;
    if (group === 'qcount') state.qCount = parseInt(btn.dataset.val);
  });
});

// ── Start Quiz ────────────────────────────────────────
$('startBtn').addEventListener('click', async () => {
  state.playerName = ($('playerName').value || '').trim() || 'Anonymous';

  if (!state.selectedTopics.length) {
    toast('Please select at least one topic!', 'err');
    return;
  }

  $('startBtn').disabled = true;
  $('startBtn').textContent = 'Loading questions...';

  try {
    const res  = await fetch('/api/questions', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({
        topics:     state.selectedTopics,
        difficulty: state.difficulty,
        count:      state.qCount,
      }),
    });
    const data = await res.json();

    if (!res.ok || data.error) {
      toast(data.error || 'Failed to load questions.', 'err');
      $('startBtn').disabled = false;
      $('startBtn').textContent = `Start Quiz (${state.selectedTopics.length} topic${state.selectedTopics.length > 1 ? 's' : ''}) →`;
      return;
    }

    state.questions    = data.questions;
    state.answers      = data.answers;
    state.explanations = data.explanations;
    state.current      = 0;
    state.score        = 0;
    state.timeTaken    = [];
    state.topicResults = {};
    state.selectedTopics.forEach(tid => {
      state.topicResults[tid] = { correct: 0, total: 0 };
    });

    $('liveScore').textContent = '0';
    showScreen('quiz');
    renderQuestion();

  } catch (e) {
    toast('Server unreachable. Is Flask running on port 5000?', 'err');
    $('startBtn').disabled = false;
  }
});

// ── Render Question ───────────────────────────────────
function renderQuestion() {
  const q     = state.questions[state.current];
  const topic = state.topics.find(t => t.id === q.topic_id) || { name: q.topic_id, emoji: '❓', color: '#888', bg: '#f5f5f5' };

  state.answered = false;

  // Progress bar
  const pct = (state.current / state.questions.length) * 100;
  $('progressFill').style.width = pct + '%';
  $('qNum').textContent   = state.current + 1;
  $('qTotal').textContent = state.questions.length;

  // Badge
  const badge = $('qBadge');
  badge.textContent      = topic.emoji + ' ' + topic.name;
  badge.style.background = topic.bg;
  badge.style.color      = topic.color;

  // Diff badge
  const diffBadge = $('qDiffBadge');
  diffBadge.textContent = q.diff === 'hard' ? '🔥 Hard' : '⭐ Easy';

  // Question text
  $('qText').textContent = q.q;

  // Code block
  const codeEl = $('qCode');
  if (q.code) {
    codeEl.textContent   = q.code;
    codeEl.style.display = 'block';
  } else {
    codeEl.style.display = 'none';
  }

  // Options
  const letters = ['A', 'B', 'C', 'D'];
  $('optionsGrid').innerHTML = q.opts.map((opt, i) => `
    <button class="option-btn" onclick="selectAnswer(${i})">
      <span class="opt-letter">${letters[i]}</span>${escHtml(opt)}
    </button>
  `).join('');

  // Reset feedback + next
  const fb = $('feedbackBar');
  fb.className = 'feedback-bar';
  $('nextBtn').classList.remove('show');

  startTimer();
}

// ── Timer ─────────────────────────────────────────────
function startTimer() {
  const MAX = 20;
  state.timeLeft   = MAX;
  state.timerStart = Date.now();
  clearInterval(state.timer);
  $('timerVal').textContent = MAX;
  $('timerVal').classList.remove('hurry');

  state.timer = setInterval(() => {
    state.timeLeft--;
    $('timerVal').textContent = state.timeLeft;
    if (state.timeLeft <= 5) $('timerVal').classList.add('hurry');
    if (state.timeLeft <= 0) {
      clearInterval(state.timer);
      handleTimeout();
    }
  }, 1000);
}

function handleTimeout() {
  if (state.answered) return;
  state.answered = true;

  const q = state.questions[state.current];
  state.timeTaken.push(20);
  if (state.topicResults[q.topic_id]) state.topicResults[q.topic_id].total++;

  const btns = $('optionsGrid').querySelectorAll('.option-btn');
  btns.forEach(b => b.disabled = true);
  btns[state.answers[state.current]].classList.add('reveal-correct');

  showFeedback('timeout', "⏰ Time's Up!",
    `Correct answer: ${q.opts[state.answers[state.current]]}. ${state.explanations[state.current]}`);
  $('nextBtn').classList.add('show');
}

// ── Select Answer ─────────────────────────────────────
function selectAnswer(idx) {
  if (state.answered) return;
  state.answered = true;
  clearInterval(state.timer);

  const q      = state.questions[state.current];
  const correct = state.answers[state.current];
  const taken   = 20 - state.timeLeft;
  state.timeTaken.push(taken);

  const btns = $('optionsGrid').querySelectorAll('.option-btn');
  btns.forEach(b => b.disabled = true);

  if (state.topicResults[q.topic_id]) state.topicResults[q.topic_id].total++;

  if (idx === correct) {
    btns[idx].classList.add('correct');
    state.score++;
    $('liveScore').textContent = state.score;
    if (state.topicResults[q.topic_id]) state.topicResults[q.topic_id].correct++;
    showFeedback('correct', '✅ Correct!', state.explanations[state.current]);
  } else {
    btns[idx].classList.add('wrong');
    btns[correct].classList.add('reveal-correct');
    showFeedback('wrong',
      `❌ Wrong — Correct: ${q.opts[correct]}`,
      state.explanations[state.current]);
  }

  $('nextBtn').classList.add('show');
}

function showFeedback(type, title, exp) {
  const fb = $('feedbackBar');
  $('fbTitle').textContent = title;
  $('fbExp').textContent   = exp;
  fb.className = `feedback-bar show ${type === 'correct' ? 'correct-fb' : type === 'timeout' ? 'timeout-fb' : 'wrong-fb'}`;
}

// ── Next Question ─────────────────────────────────────
$('nextBtn').addEventListener('click', () => {
  state.current++;
  if (state.current >= state.questions.length) showResults();
  else renderQuestion();
});

// ── Results ───────────────────────────────────────────
function showResults() {
  showScreen('results');
  $('progressFill').style.width = '100%';

  const total   = state.questions.length;
  const correct = state.score;
  const pct     = Math.round((correct / total) * 100);
  const avgTime = state.timeTaken.length
    ? Math.round(state.timeTaken.reduce((a, b) => a + b, 0) / state.timeTaken.length)
    : 0;

  // Grade
  let emoji, title, sub;
  if (pct === 100) { emoji='🏆'; title='Perfect Score!';  sub='Absolutely flawless. You\'re a web dev legend!'; }
  else if (pct>=80){ emoji='🎉'; title='Excellent!';       sub='You really know your web technologies!'; }
  else if (pct>=60){ emoji='👍'; title='Good Job!';        sub='Solid knowledge. Keep practicing!'; }
  else if (pct>=40){ emoji='📚'; title='Keep Learning!';   sub='You\'re getting there. Review the explanations!'; }
  else             { emoji='💪'; title="Don't Give Up!";   sub='Every expert was once a beginner. Try again!'; }

  $('resultEmoji').textContent = emoji;
  $('resultTitle').textContent = title;
  $('resultSub').textContent   = sub;
  $('statCorrect').textContent = correct;
  $('statWrong').textContent   = total - correct;
  $('statTime').textContent    = avgTime + 's';

  // Score circle
  const arc = $('circleArc');
  const offset = 314 - (pct / 100) * 314;
  const color = pct >= 70 ? '#22c55e' : pct >= 40 ? '#f59e0b' : '#ef4444';
  arc.style.stroke = color;
  setTimeout(() => {
    arc.style.strokeDashoffset = offset;
    $('circlePct').textContent = pct + '%';
    $('circlePct').style.color = color;
  }, 200);

  // Topic performance bars
  const topic_entries = Object.entries(state.topicResults).filter(([, v]) => v.total > 0);
  const perfSection   = $('topicPerf');
  if (topic_entries.length > 0) {
    const rows = topic_entries.map(([tid, v]) => {
      const t = state.topics.find(x => x.id === tid) || { emoji: '❓', name: tid, color: '#888' };
      const p = Math.round((v.correct / v.total) * 100);
      return `
        <div class="perf-row">
          <div class="perf-name">${t.emoji} ${t.name}</div>
          <div class="perf-track">
            <div class="perf-fill" style="background:${t.color}" data-w="${p}"></div>
          </div>
          <div class="perf-val">${p}%</div>
        </div>`;
    }).join('');
    perfSection.innerHTML = `<div class="topic-perf-title">Performance by Topic</div>${rows}`;
    setTimeout(() => {
      perfSection.querySelectorAll('.perf-fill').forEach(el => {
        el.style.width = el.dataset.w + '%';
      });
    }, 400);
  } else {
    perfSection.innerHTML = '';
  }

  // Pre-fill name
  $('saveNameInput').value = state.playerName !== 'Anonymous' ? state.playerName : '';
}

// ── Save Score to MongoDB ─────────────────────────────
$('saveScoreBtn').addEventListener('click', async () => {
  const name = $('saveNameInput').value.trim() || 'Anonymous';
  const pct  = Math.round((state.score / state.questions.length) * 100);
  const avgT = state.timeTaken.length
    ? state.timeTaken.reduce((a, b) => a + b, 0) / state.timeTaken.length
    : 0;

  $('saveScoreBtn').disabled    = true;
  $('saveScoreBtn').textContent = 'Saving...';

  try {
    const res = await fetch('/api/scores', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        player_name: name,
        score:       state.score,
        total:       state.questions.length,
        pct:         pct,
        topics:      state.selectedTopics,
        difficulty:  state.difficulty,
        avg_time:    Math.round(avgT * 10) / 10,
      }),
    });

    $('saveSuccess').style.display = 'block';
    $('saveSuccess').textContent   = `✅ Score saved for "${name}"! Check the leaderboard.`;
    toast('Score saved to leaderboard! 🏆', 'ok');

  } catch (e) {
    toast('Could not save score. DB may be offline.', 'err');
    $('saveScoreBtn').disabled    = false;
    $('saveScoreBtn').textContent = 'Save to Leaderboard';
  }
});

// ── Result Buttons ────────────────────────────────────
$('playAgainBtn').addEventListener('click', async () => {
  $('liveScore').textContent = '0';
  $('startBtn').disabled = false;
  $('startBtn').textContent = `Start Quiz (${state.selectedTopics.length} topic${state.selectedTopics.length > 1 ? 's' : ''}) →`;

  // re-fetch questions
  $('startBtn').click();
});

$('changeTopicsBtn').addEventListener('click', () => {
  $('liveScore').textContent = '0';
  // Reset save state
  $('saveScoreBtn').disabled    = false;
  $('saveScoreBtn').textContent = 'Save to Leaderboard';
  $('saveSuccess').style.display = 'none';
  showScreen('home');
});

// ── Init ──────────────────────────────────────────────
loadTopics();
