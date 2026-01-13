document.addEventListener("DOMContentLoaded", () => {
  const addBtn = document.getElementById("addBtn");
  const savebutton = document.getElementById("savebtn");
  
  const infoModalEl = document.getElementById("infoModal");
  const modalBody = infoModalEl.querySelector(".modal-body");
  const tableBody = document.getElementById('body');


  function openAddModal() {
  infoModal.show();
  history.pushState(
    { modal: "add"},
    "",
    `/clients/create`
  );
  }


addBtn.addEventListener("click", () => {
  modalBody.innerHTML = ""; 

  savebutton.classList.remove("d-none");
  savebutton.classList.add("d-inline-flex");

  const fields = [
    { key: "nom", label: "Nom", type: "text" },
    { key: "prenom", label: "Prénom", type: "text" },
    { key: "telephone", label: "Téléphone", type: "text" },
    { key: "email", label: "Email", type: "email" },
    { key: "solde", label: "Solde", type: "number" }
  ];

  fields.forEach(field => {
    const div = document.createElement("div");
    div.classList.add("mb-2");

    const label = document.createElement("h6");
    label.textContent = field.label;

    const input = document.createElement("input");
    input.type = field.type;
    input.classList.add("form-control");
    input.placeholder = `Entrer ${field.label.toLowerCase()}`;

    input.dataset.key = field.key; 

    div.appendChild(label);
    div.appendChild(input);
    modalBody.appendChild(div);
  });

  infoModal.show();
});



savebutton.addEventListener("click", async () => {
  const inputs = modalBody.querySelectorAll("input");
  const payload = {};

  inputs.forEach(input => {
    payload[input.dataset.key] = input.value;
  });

  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    try {
        const response = await fetch("/clients/create/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error("Create failed");

        const data = await response.json();

        const tr = document.createElement("tr");
        tr.innerHTML = `
        <td>
            <input class="form-check-input row-checkbox" type="checkbox" data-id="${data.id}">
            <label class="form-check-label">${data.id}</label>
        </td>
        <td>${data.nom}</td>
        <td>${data.prenom}</td>
        <td>${data.telephone}</td>
        <td>${data.email}</td>
        <td>${data.solde}</td>
        `;

        tableBody.prepend(tr);

        infoModal.hide();
        modalBody.innerHTML = "";

    } catch (err) {
    console.error(err);
    alert("Failed to create client");
    }
})

});
