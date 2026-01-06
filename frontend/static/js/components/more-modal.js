document.addEventListener("DOMContentLoaded", () => {
  const actionBar = document.getElementById("actionBar");
  const viewBtn = document.getElementById("viewBtn");
  const editBtn = document.getElementById("editBtn");
  const addBtn = document.getElementById("addBtn");
  const deleteBtn = document.getElementById("deleteBtn");
  const savebutton = document.getElementById("savebtn");

  const checkboxes = document.querySelectorAll('input[type="checkbox"]');
  
  // Initialize modal once
  const infoModalEl = document.getElementById("infoModal");
  const infoModal = new bootstrap.Modal(infoModalEl);
  const modalBody = infoModalEl.querySelector(".modal-body");

  function updateActionBar() {
    const checked = Array.from(checkboxes).filter(cb => cb.checked);

    if (checked.length > 0) {
      actionBar.classList.remove('d-none');
      actionBar.classList.add('d-flex');
      
      if (checked.length === 1) {
        viewBtn.disabled = false;
        editBtn.disabled = false;
      } else {
        viewBtn.disabled = true;
        editBtn.disabled = true;
      }
    } else {
      actionBar.classList.remove('d-flex');
      actionBar.classList.add('d-none');
    }
  }

  function openEditModal(clientId) {
  infoModal.show();
  history.pushState(
    { modal: "edit", clientId },
    "",
    `/clients/${clientId}/edit/`
  );
}

function openViewModal(clientId) {
  infoModal.show();
  history.pushState(
    { modal: "view", clientId },
    "",
    `/clients/${clientId}/`
  );
}

  checkboxes.forEach(cb => cb.addEventListener("change", updateActionBar));

  viewBtn.addEventListener("click", async () => {
    const checked = Array.from(checkboxes).filter(cb => cb.checked);
    if (checked.length === 1) {
      const clientId = checked[0].dataset.id;

      try {
        const response = await fetch(`/client/${clientId}`);
        if (!response.ok) throw new Error("Client not found");

        const data = await response.json();

        // Clear and fill modal content
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

        // Show modal
        openViewModal(clientId);

      } catch (err) {
        console.error(err);
      }
    }
  });

   editBtn.addEventListener("click", async () => {
    const checked = Array.from(checkboxes).filter(cb => cb.checked);
    if (checked.length === 1) {
      const clientId = checked[0].dataset.id;

      try {
        const response = await fetch(`/client/${clientId}`);
        if (!response.ok) throw new Error("Client not found");

        const data = await response.json();

        // Clear and fill modal content
        modalBody.innerHTML = "";
        savebutton.classList.remove("d-none");
        savebutton.classList.add("d-inline-flex");
        for (let key in data) {
          const div = document.createElement("div");
          div.classList.add("mb-2");
          div.classList.add("gap-4")

          const label = document.createElement("h6");
          label.classList.add("mb-2")
          label.textContent = key.charAt(0).toUpperCase() + key.slice(1);

          const value = document.createElement("input");
          value.type = "text";
          value.classList.add("form-control");
          value.value = data[key]; 

          div.appendChild(label);
          div.appendChild(value);
          modalBody.appendChild(div);
        }
        // Show modal
        openEditModal(clientId);

      } catch (err) {
        console.error(err);
      }
    }
  });

  function openAddModal() {
  infoModal.show();
  history.pushState(
    { modal: "add"},
    "",
    `/clients/create`
  );
}


  addBtn.addEventListener("click", async () => {

      try {
        const response = await fetch(`/client/1`);
        if (!response.ok) throw new Error("Client not found");

        const data = await response.json();

        modalBody.innerHTML = "";
        savebutton.classList.remove("d-none");
        savebutton.classList.add("d-inline-flex");
        for (let key in data) {
          const div = document.createElement("div");
          div.classList.add("mb-2");
          div.classList.add("gap-4")

          const label = document.createElement("h6");
          label.classList.add("mb-2")
          label.textContent = key.charAt(0).toUpperCase() + key.slice(1);

          const value = document.createElement("input");
          value.type = "placeholder";
          value.classList.add("form-control");
          value.textContent = key.charAt(0).toUpperCase() + key.slice(1); 

          div.appendChild(label);
          div.appendChild(value);
          modalBody.appendChild(div);
        }
        // Show modal
        openAddModal();

      } catch (err) {
        console.error(err);
      }
    }
  });


  savebutton.addEventListener("click", async () => {
    const checked = Array.from(checkboxes).filter(cb => cb.checked);
    if (checked.length !== 1) return;

    const clientId = checked[0].dataset.id;
    
    // Collect all input values in the modal
    const inputs = modalBody.querySelectorAll("input");
    const updatedData = {};
    inputs.forEach(input => {
      const key = input.previousElementSibling.textContent.toLowerCase(); // assumes <h6> label
      updatedData[key] = input.value;
    });

    // CSRF token
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    try {
      const response = await fetch(`/clients/${clientId}/update/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken
        },
        body: JSON.stringify(updatedData)
      });

      if (!response.ok) throw new Error("Update failed");

      const data = await response.json();

      // Update the row in the table
      const row = checked[0].closest("tr");
      row.cells[1].textContent = data.nom;
      row.cells[2].textContent = data.prenom;
      row.cells[3].textContent = data.telephone;
      row.cells[4].textContent = data.email;
      row.cells[5].textContent = data.solde;

      // Hide modal
      infoModal.hide();
    } catch (err) {
      console.error(err);
      alert("Failed to update client");
    }
  });

  // Optional: reset modal content when hidden
  infoModalEl.addEventListener('hidden.bs.modal', () => {
    modalBody.innerHTML = "";
    history.pushState({}, "", "/clients/");
  });
});
