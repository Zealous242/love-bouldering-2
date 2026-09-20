document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector("#result_list");

    if (!table) return;

    const headers = table.querySelectorAll("thead th");
    const colgroup = document.createElement("colgroup");
    let firstFieldFound = false;

    headers.forEach(function (header) {
        const column = document.createElement("col");
        const isFirstField = !firstFieldFound &&
            !header.classList.contains("action-checkbox-column");
        const isActionField = header.classList.contains("action-checkbox-column");
        const isAuthorField = header.classList.contains("column-author");
        const isApprovedField = header.classList.contains("column-approved");
        const initialWidth = isActionField ?
            70 :
            isAuthorField || isApprovedField ?
            150 :
            isFirstField ?
            500 :
            header.getBoundingClientRect().width;

        column.style.width = `${initialWidth}px`;
        if (isFirstField) firstFieldFound = true;
        colgroup.appendChild(column);

        const handle = document.createElement("span");
        handle.className = "column-resize-handle";
        handle.setAttribute("aria-hidden", "true");
        header.appendChild(handle);

        handle.addEventListener("mousedown", function (event) {
            event.preventDefault();

            const startX = event.clientX;
            const startWidth = column.getBoundingClientRect().width;

            function resize(moveEvent) {
                const newWidth = Math.max(80, startWidth + moveEvent.clientX - startX);
                column.style.width = `${newWidth}px`;
            }

            function stopResize() {
                document.removeEventListener("mousemove", resize);
                document.removeEventListener("mouseup", stopResize);
                document.body.classList.remove("is-resizing-column");
            }

            document.body.classList.add("is-resizing-column");
            document.addEventListener("mousemove", resize);
            document.addEventListener("mouseup", stopResize);
        });
    });

    table.prepend(colgroup);
});