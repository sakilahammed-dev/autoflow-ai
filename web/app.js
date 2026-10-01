// AutoFlow-AI Interactive Engine Simulation
// Author: Sakil Ahammed (https://github.com/sakilahammed-dev)

document.addEventListener('DOMContentLoaded', () => {
  const triggerBtn = document.getElementById('btn-trigger');
  const clearBtn = document.getElementById('btn-clear-logs');
  const terminal = document.getElementById('terminal-output');
  const actionsCounter = document.getElementById('val-actions');

  let executionCount = 2840;

  const nodes = [
    { el: document.getElementById('node-1'), conn: document.getElementById('conn-1'), name: 'Webhook Intake' },
    { el: document.getElementById('node-2'), conn: document.getElementById('conn-2'), name: 'AI Synthesis' },
    { el: document.getElementById('node-3'), conn: document.getElementById('conn-3'), name: 'Logic Execution' },
    { el: document.getElementById('node-4'), conn: null, name: 'Global Dispatch' }
  ];

  function getTimestamp() {
    const now = new Date();
    return now.toTimeString().split(' ')[0] + '.' + String(now.getMilliseconds()).padStart(3, '0');
  }

  function appendLog(message, type = 'info') {
    const line = document.createElement('div');
    line.className = 'log-line';
    
    let colorClass = 'text-info';
    if (type === 'success') colorClass = 'text-success';
    if (type === 'warning') colorClass = 'text-warning';
    if (type === 'muted') colorClass = 'text-muted';

    line.innerHTML = `<span class="text-muted">[${getTimestamp()}]</span> <span class="${colorClass}">${message}</span>`;
    terminal.appendChild(line);
    terminal.scrollTop = terminal.scrollHeight;
  }

  clearBtn.addEventListener('click', () => {
    terminal.innerHTML = '';
    appendLog('Telemetry buffer cleared. Standing by.', 'muted');
  });

  triggerBtn.addEventListener('click', async () => {
    triggerBtn.disabled = true;
    triggerBtn.innerHTML = '<span class="btn-icon">⚡</span> Running Autonomous Pipeline...';

    // Reset nodes
    nodes.forEach(n => {
      n.el.classList.remove('active', 'completed');
      n.el.querySelector('.node-status').innerText = 'Queued';
      if (n.conn) n.conn.classList.remove('active');
    });

    appendLog('Incoming event detected: CRM_LEAD_DISPATCH', 'warning');

    // Stage 1
    await executeStage(0, 'Ingesting raw webhook payload & verifying schema...', 'Intake Validated');
    
    // Stage 2
    await executeStage(1, 'Nova-Agent formulating context & LLM inference...', 'AI Reasoning Done');

    // Stage 3
    await executeStage(2, 'Transforming records & running business rules...', 'Tasks Executed');

    // Stage 4
    await executeStage(3, 'Dispatching secure webhooks & telemetry ack...', 'Dispatched (200 OK)');

    appendLog('✓ Workflow Pipeline concluded with 0ms human intervention.', 'success');

    // Increment metrics
    executionCount += 1;
    actionsCounter.innerText = executionCount.toLocaleString() + '+';

    triggerBtn.disabled = false;
    triggerBtn.innerHTML = '<span class="btn-icon">▶</span> Trigger Autonomous Run';
  });

  function executeStage(index, logMessage, statusText) {
    return new Promise(resolve => {
      const node = nodes[index];
      node.el.classList.add('active');
      node.el.querySelector('.node-status').innerText = 'Processing...';
      appendLog(`[STAGE ${index + 1}] ${logMessage}`, 'info');

      setTimeout(() => {
        node.el.classList.remove('active');
        node.el.classList.add('completed');
        node.el.querySelector('.node-status').innerText = statusText;
        if (node.conn) node.conn.classList.add('active');
        resolve();
      }, 700);
    });
  }
});
