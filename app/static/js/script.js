document.addEventListener('DOMContentLoaded', () => {
    fetch("/api/tasks")
      .then(res => res.json())
      .then(data => {
        const list = document.getElementById('task-list');
        data.forEach(task => {
            const card = `
              <div class="col-md-4 mb-3">
                <div class="card p-3">
                  <h5>${task.title}</h5>
                  <p>${task.description}</p>
                  <span class="badge ${task.completed ? 'bg-success' : 'bg-warning'}">
                    ${task.completed ? 'Completed' : 'Pending'}
                  </span>
                </div>
              </div>`;
            list.innerHTML += card;
        });
      })
      .catch(err => console.error("Error loading tasks:", err));
});

