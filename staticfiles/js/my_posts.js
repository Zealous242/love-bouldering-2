/* jshint esversion: 11 */

document.addEventListener("DOMContentLoaded", function () {
    const tables = document.querySelectorAll(".resizable-table");

    if (!tables.length) return;

    tables.forEach(function (table) {
        table.style.tableLayout = "fixed";
        const headers = table.querySelectorAll("thead th");
        const colgroup = document.createElement("colgroup");

        headers.forEach(function (header) {
            const column = document.createElement("col");
            column.style.width = `${Math.max(100, header.getBoundingClientRect().width)}px`;
            colgroup.appendChild(column);

            const handle = document.createElement("span");
            handle.className = "column-resize-handle";
            handle.setAttribute("aria-hidden", "true");
            header.appendChild(handle);

            handle.addEventListener("pointerdown", function (event) {
                event.preventDefault();
                handle.setPointerCapture(event.pointerId);

                const startX = event.clientX;
                const startWidth = column.getBoundingClientRect().width;

                function resize(moveEvent) {
                    const newWidth = Math.max(100, startWidth + moveEvent.clientX - startX);
                    column.style.width = `${newWidth}px`;
                }

                function stopResize() {
                    document.removeEventListener("pointermove", resize);
                    document.removeEventListener("pointerup", stopResize);
                    document.body.classList.remove("is-resizing-column");
                }

                document.body.classList.add("is-resizing-column");
                document.addEventListener("pointermove", resize);
                document.addEventListener("pointerup", stopResize);
            });
        });

        table.prepend(colgroup);
    });
});