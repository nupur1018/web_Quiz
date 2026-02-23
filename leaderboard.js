/* =====================================================
   WebDev Quiz — leaderboard.js
   Loads and renders the leaderboard from the API
   ===================================================== */

async function loadLeaderboard() {
  const tbody = document.getElementById('lbBody');
  tbody.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:32px;color:#8b90b8;">Loading...</td></tr>`;

  try {
    const [lbRes, statsRes] = await Promise.all([
      fetch('/api/leaderboard?limit=15'),
      fetch('/api/stats'),
    ]);

    const lbData    = await lbRes.json();
    const statsData = await statsRes.json();

    // Stats cards
    document.getElementById('statTotalGames').textContent = statsData.total_games || 0;
    document.getElementById('statAvgScore').textContent   = (statsData.avg_pct  || 0) + '%';
    document.getElementById('statTopScore').textContent   = (statsData.max_pct  || 0) + '%';

    const entries = lbData.leaderboard || [];
    if (!entries.length) {
      tbody.innerHTML = `
        <tr><td colspan="6">
          <div class="lb-empty">
            <span class="lb-empty-icon">🏆</span>
            No scores yet! Be the first to take the quiz.
          </div>
        </td></tr>`;
      return;
    }

    tbody.innerHTML = entries.map(entry => {
      const rankClass = entry.rank === 1 ? 'rank-1' : entry.rank === 2 ? 'rank-2' : entry.rank === 3 ? 'rank-3' : 'rank-other';
      const rankIcon  = entry.rank === 1 ? '🥇' : entry.rank === 2 ? '🥈' : entry.rank === 3 ? '🥉' : entry.rank;
      const topics    = (entry.topics || []).map(t => `<span class="topic-chip">${t}</span>`).join('');
      const barWidth  = Math.round(entry.pct || 0);
      const diff      = entry.difficulty || 'mixed';
      const diffColor = diff === 'hard' ? '#ef4444' : diff === 'easy' ? '#22c55e' : '#f59e0b';

      return `
        <tr>
          <td><span class="rank-badge ${rankClass}">${rankIcon}</span></td>
          <td style="font-weight:800;color:#1a1d2e;">${escHtml(entry.player_name || 'Anonymous')}</td>
          <td>
            <div class="score-pct-bar">
              <div class="mini-bar-track">
                <div class="mini-bar-fill" style="width:${barWidth}%"></div>
              </div>
              <strong>${barWidth}%</strong>
            </div>
          </td>
          <td style="font-weight:700;">${entry.score}/${entry.total}</td>
          <td>${topics || '<span class="topic-chip">—</span>'}</td>
          <td style="font-size:11px;color:#8b90b8;">${entry.created_at || '—'}</td>
        </tr>`;
    }).join('');

  } catch (e) {
    tbody.innerHTML = `
      <tr><td colspan="6">
        <div class="lb-empty">
          <span class="lb-empty-icon">⚠️</span>
          Could not load leaderboard. Is Flask running?
        </div>
      </td></tr>`;
  }
}

function escHtml(s) {
  return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

document.getElementById('refreshBtn').addEventListener('click', loadLeaderboard);

loadLeaderboard();
