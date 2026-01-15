export function btnLogic() {
  const actionBar = document.getElementById("actionBar");
  const viewBtn = document.getElementById("viewBtn");
  const editBtn = document.getElementById("editBtn"); 
  const addBtn = document.getElementById("addBtn");
  const deleteBtn = document.getElementById("deleteBtn");
  const saveBtn = document.getElementById("savebtn");
  const table = document.querySelector("table[data-name]");
  const name = table.dataset.name;

  const infoModalEl = document.getElementById("infoModal");
  const infoModal = new bootstrap.Modal(infoModalEl);
  const modalBody = infoModalEl.querySelector(".modal-body");


  function updateActionBar() {
    const currentCheckboxes = document.querySelectorAll('.row-checkbox');
    const checked = Array.from(currentCheckboxes).filter(cb => cb.checked);
    
    if (checked.length > 0) {
      actionBar.classList.remove('d-none');
      actionBar.classList.add('d-flex');
      viewBtn.disabled = checked.length !== 1;
      editBtn.disabled = checked.length !== 1;
    } else {
      actionBar.classList.remove('d-flex');
      actionBar.classList.add('d-none');
    }
  }

  document.addEventListener("change", function (e) {
        if (e.target.classList.contains("row-checkbox")) {
            updateActionBar();
        }
  });


  function openEditModal(id) {
    infoModalEl.dataset.mode = "edit";
    infoModal.show();
    history.pushState({ modal: "edit", id }, "", `/${name}/${id}/edit/`);
  }

  function openViewModal(id) {
    infoModal.show();
    history.pushState({ modal: "view", id }, "", `/${name}/${id}/`);
  }

  function openAddModal() {
    infoModalEl.dataset.mode = "create";
    infoModal.show();
    history.pushState({ modal: "add" }, "", `/${name}/create/`);
  }


  viewBtn.addEventListener("click", async () => {
    const checked = document.querySelectorAll('.row-checkbox:checked');
    if (checked.length !== 1) return;
    const id = checked[0].dataset.id;

    try {
      const response = await fetch(`/${name}/${id}`);
      if (!response.ok) throw new Error("Data not found");
      const data = await response.json();

      modalBody.innerHTML = "";
      for (let key in data) {
        const div = document.createElement("div");
        div.classList.add("mb-4");

        const label = document.createElement("h6");
        label.textContent = key.charAt(0).toUpperCase() + key.slice(1);

        const value = document.createElement("p");
        value.textContent = data[key];

        div.appendChild(label);
        div.appendChild(value);
        modalBody.appendChild(div);
      }

      openViewModal(id);
    } catch (err) {
      console.error(err);
    }
  });


  editBtn.addEventListener("click", async () => {
    const checked = document.querySelectorAll('.row-checkbox:checked');
    if (checked.length !== 1) return;
    const id = checked[0].dataset.id;

    try {
      const response = await fetch(`/${name}/${id}`);
      if (!response.ok) throw new Error("Data not found");
      const data = await response.json();

      infoModalEl.dataset.id = id;

      modalBody.innerHTML = "";
      saveBtn.classList.remove("d-none");
      saveBtn.classList.add("d-inline-flex");

      for (let key in data) {
        if (key === "id" || key === "date_creation") continue;
        
        const div = document.createElement("div");
        div.classList.add("mb-2", "gap-4");

        const label = document.createElement("h6");
        label.classList.add("mb-2");
        label.textContent = key.charAt(0).toUpperCase() + key.slice(1);

        const input = document.createElement("input");
        input.type = "text";
        input.classList.add("form-control");
        input.value = data[key];
        input.name = key;

        div.appendChild(label);
        div.appendChild(input);
        modalBody.appendChild(div);
      }

      openEditModal(id);
    } catch (err) {
      console.error(err);
    }
  });

  
  addBtn.addEventListener("click", async () => {
    try {
      saveBtn.classList.remove("d-none");
      saveBtn.classList.add("d-inline-flex");

      const response = await fetch(`/${name}/info/`);
      if (!response.ok) throw new Error("Data not found");

      const fields = await response.json();

      const typeMap = {
        string: "text",
        number: "number",
        email: "email",
        tel: "tel"
      };

      modalBody.innerHTML = "";

      for (let key in fields) {
        const div = document.createElement("div");
        div.classList.add("mb-2");

        const label = document.createElement("h6");
        label.textContent = key.charAt(0).toUpperCase() + key.slice(1);

        const input = document.createElement("input");
        input.type = typeMap[fields[key]] || "text";
        input.classList.add("form-control");
        input.name = key;

        div.append(label, input);
        modalBody.appendChild(div);
      }

      openAddModal();

    } catch (err) {
      console.error(err);
    }
  });


  // --- Save Button ---
saveBtn.addEventListener("click", async () => {
  const mode = infoModalEl.dataset.mode;
  const id = infoModalEl.dataset.id;

  const inputs = modalBody.querySelectorAll("input");
  const dataToSend = {};
  inputs.forEach(input => {
    dataToSend[input.name] = input.value;
  });

  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  try {
    let url = "";
    if (mode === "edit") {
      url = `/${name}/${id}/edit/`;
    } else if (mode === "create") {
      url = `/${name}/create/`;
    }

    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken
      },
      body: JSON.stringify(dataToSend)
    });

    if (!response.ok) throw new Error(`${mode === "edit" ? "Update" : "Create"} failed`);

    const data = await response.json();

    if (mode === "edit") {
      const row = document.querySelector(`.row-checkbox[data-id="${id}"]`).closest("tr");
      let cellIndex = 0;
      for (let key in data) {
        if (key === "id") {
      row.cells[cellIndex].innerHTML = `
        <input class="form-check-input row-checkbox" type="checkbox" data-id="${data.id}">
        <label class="form-check-label">${data.id}</label>
      `;
    } else if (key === "disponibilite") {
      const badgeClass = data[key] ? "badge-success" : "badge-failure";
      const badgeText = data[key] ? "Disponible" : "Non Disponible";
      row.cells[cellIndex].innerHTML = `<span class="badge ${badgeClass}">${badgeText}</span>`;
    } else {
      row.cells[cellIndex].textContent = data[key];
    }
    cellIndex++;
      }
    } else if (mode === "create") {
      console.log("Created client:", data);
    }

    infoModal.hide();
  } catch (err) {
    console.error(err);
    alert(`${mode === "edit" ? "Update" : "Create"} failed`);
  }
});


 infoModalEl.addEventListener("hidden.bs.modal", () => {
    history.replaceState(null, "", `/${name}/`);
     window.location.reload();
  });

  

  deleteBtn.addEventListener("click", async () => {
    const checked = Array.from(document.querySelectorAll('.row-checkbox:checked'));
    if (checked.length === 0) return;

    const ids = checked.map(cb => cb.dataset.id);

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    try {
      const response = await fetch(`/${name}/delete/`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ ids })
      });

      if (!response.ok) throw new Error("Delete failed");

      checked.forEach(cb => cb.closest('tr').remove());
      
      actionBar.classList.add('d-none');
      actionBar.classList.remove('d-flex');

    } catch (err) {
      console.error(err);
      alert("Delete failed");
    }
  });
 
};


