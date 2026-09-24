/* jshint esversion: 11 */
/* global bootstrap */

document.addEventListener("DOMContentLoaded", function () {
    const filterMenu = document.querySelector("#changelist-filter");

    if (filterMenu) {
        const filterContent = document.createElement("div");
        const filterToggle = document.createElement("button");

        filterContent.className = "admin-filter-content";
        filterToggle.type = "button";
        filterToggle.className = "admin-filter-toggle";
        filterToggle.textContent = "Hide filters";
        filterToggle.setAttribute("aria-expanded", "true");
        filterContent.setAttribute("aria-hidden", "false");

        while (filterMenu.firstChild) {
            filterContent.appendChild(filterMenu.firstChild);
        }

        filterMenu.append(filterToggle, filterContent);

        filterToggle.addEventListener("click", function () {
            const isExpanded = filterToggle.getAttribute("aria-expanded") === "true";
            filterMenu.classList.toggle("is-collapsed", isExpanded);
            filterToggle.setAttribute("aria-expanded", String(!isExpanded));
            filterContent.setAttribute("aria-hidden", String(isExpanded));
            filterToggle.textContent = isExpanded ? "Show filters" : "Hide filters";
        });
    }

    const table = document.querySelector("#result_list");

    if (!table) return;

    const headers = table.querySelectorAll("thead th");
    const colgroup = document.createElement("colgroup");
    let firstFieldFound = false;

    headers.forEach(function (header) {
        const column = document.createElement("col");
        const isActionField = header.classList.contains("action-checkbox-column");
        const isTitleField = header.classList.contains("column-title");
        const isStatusField = header.classList.contains("column-status");
        const isCreatedOnField = header.classList.contains("column-created_on");
        const isUpdatedOnField = header.classList.contains("column-updated_on");
        const isFirstField = !firstFieldFound && !isActionField;
        const initialWidth = isActionField ?
            70 :
            isStatusField || isCreatedOnField || isUpdatedOnField ?
            80 :
            isTitleField ?
            150 :
            isFirstField ?
            50 :
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