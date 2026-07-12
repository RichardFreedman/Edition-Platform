document.addEventListener("DOMContentLoaded", () => {
  const filterInput = document.getElementById("filter");
  const table = document.getElementById("catalog");
  const rows = Array.from(table.tBodies[0].rows);

  filterInput.addEventListener("input", () => {
    const term = filterInput.value.trim().toLowerCase();
    rows.forEach((row) => {
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(term) ? "" : "none";
    });
  });

  // Click a column header to sort by it
  table.tHead.querySelectorAll("th").forEach((th, colIndex) => {
    let ascending = true;
    th.addEventListener("click", () => {
      rows.sort((a, b) => {
        const aText = a.cells[colIndex].textContent.trim();
        const bText = b.cells[colIndex].textContent.trim();
        return ascending ? aText.localeCompare(bText) : bText.localeCompare(aText);
      });
      ascending = !ascending;
      rows.forEach((row) => table.tBodies[0].appendChild(row));
    });
  });
});
