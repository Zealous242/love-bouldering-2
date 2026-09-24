/* jshint esversion: 11 */

const editButtons = document.getElementsByClassName("btn-edit");
const editCommentModalElement = document.getElementById("editCommentModal");
const editCommentModal = editCommentModalElement ?
    new bootstrap.Modal(editCommentModalElement) :
    null;
const editCommentForm = document.getElementById("editCommentForm");
const editCommentBody = document.getElementById("editCommentBody");

const deleteModalElement = document.getElementById("deleteModal");
const deleteModal = deleteModalElement ?
    new bootstrap.Modal(deleteModalElement) :
    null;
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");



/*
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        editCommentBody.value = commentContent;
        editCommentForm.setAttribute("action", e.target.dataset.editUrl);
        editCommentModal.show();
    });
}

/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        if (!deleteModal) return;
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}