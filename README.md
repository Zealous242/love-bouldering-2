# Love Bouldering

## Introduction

A Django-based Wikipedia-style website dedicated to bouldering. The purpose of this website is to provide an educational resource where visitors can learn about bouldering, while registered users can suggest improvements to articles. Bouldering is a climbing discipline (or hobby for some people) that is done on short walls - typically in a climbing gym - and/or on small rock formations outdoors without the use of ropes or harnesses. Suggested changes are reviewed and approved or rejected by an administrator before they can affect published content.

## Live Site Link

**Live site:** [**Boulder Wiki**](https://love-bouldering-2-69300253a310.herokuapp.com/)

## Project Overview

BoulderWiki is a Wikipedia-style knowledge base about **bouldering as a sport**.

The website is designed to allow visitors to learn about topics such as:

- Bouldering history
- Board climbing
- Climbing techniques
- Grading systems
- Climbing holds
- Safety
- Training
- Bouldering terminology
- Competitions
- Professional boulderers
- Bouldering locations and gyms

The website will use **Django's authentication and authorisation functionality** to control access to contribution and administration features.

### Core Contribution Model

The core rule of the website is:

> Anyone can read approved content, but only authenticated users can suggest changes. Suggested changes must be reviewed and approved by an administrator before they become part of the published article.

---

## User Roles

### Guest

A guest is a visitor who has not logged into an account.

Guests can:

- View the homepage
- Browse articles
- Search articles
- Browse categories
- Read approved bouldering information
- Register for an account
- Log in

Guests cannot:

- Suggest article changes
- Submit content suggestions
- View private contribution history
- Access administration features
- Approve or reject suggestions

---

### Registered User

A registered user has created an account and logged in.

Registered users can:

- Do everything a guest can do
- Suggest changes to articles
- Submit corrections
- Provide reasons for proposed changes
- View their submitted suggestions
- Track suggestion status
- View their account/profile

Registered users cannot:

- Directly modify published articles
- Approve suggestions
- Reject suggestions
- Access administrator functionality
- View other users' private suggestion history

---

### Administrator / Superuser

An administrator is a Django superuser with administrative permissions.

Administrators can:

- Access the Django admin interface
- Manage users
- Create articles
- Edit articles
- Delete articles
- Manage categories
- Review suggested edits
- Approve suggested edits
- Reject suggested edits
- Provide feedback on rejected suggestions
- Manage website content

---
## User Stories

### Epic 1 — Public Website and Navigation

#### US-01 — View the Homepage (Should Have)

**User Story**

As a visitor, I want to view the homepage so that I can understand what BoulderingWiki is and begin exploring bouldering content.

**Acceptance Criteria**

- The homepage loads successfully at `/`.
- The page clearly identifies the website as BoulderingWiki.
- A short introduction explains the purpose of the website.
- Users can access article search from the homepage.
- Users can navigate to Articles and Categories.
- The page displays a small selection of recent or featured articles.
- The page works on mobile, tablet, laptop, and desktop.

**Implementation Tasks**

- Create a homepage URL.
- Create a Django homepage view.
- Create `home.html`.
- Add an introductory hero section.
- Add the search form.
- Query a small number of recent articles.
- Display category links.
- Extend the shared `base.html` template.
- Add responsive styling.

---

#### US-02 — Navigate the Website (Should Have)

**User Story**

As a visitor, I want consistent navigation so that I can move between the main areas of the website easily.

**Acceptance Criteria**

- Navigation is available on all main public pages.
- Guests can access:
  - Home
  - Articles
  - Categories
  - Search
  - Login
  - Register
- Logged-in users can access Logout.
- The site logo or name links to the homepage.
- Navigation remains usable on smaller screens.
- Keyboard users can access all navigation links.

**Implementation Tasks**

- Build the navigation inside `base.html`.
- Use Django authentication checks to show different links for guests and authenticated users.
- Add a responsive mobile navigation pattern.
- Add accessible labels where required.
- Add visible keyboard focus states.
- Test navigation at all target breakpoints.

---

### Epic 2 — Articles and Categories

#### US-03 — View the Article Directory (Must Have)

**User Story**

As a visitor, I want to view a list of bouldering articles so that I can discover available content.

**Acceptance Criteria**

- The Article Directory is accessible without logging in.
- All published articles are displayed.
- Each entry shows:
  - Article title
  - Category
  - Short excerpt or summary
- Selecting an article opens its detail page.
- A useful message appears if no articles exist.
- Article entries are readable on different screen sizes.

**Implementation Tasks**

- Create the Article model if not already created.
- Add an article list URL.
- Create an article list view.
- Query articles using the Django ORM.
- Create `article_list.html`.
- Display title, category, and excerpt.
- Link each article to its slug-based detail page.
- Add empty-state handling.
- Add responsive card/list styling.

---

#### US-04 — Read an Article (Must Have)

**User Story**

As a visitor, I want to read a bouldering article so that I can learn about a particular topic.

**Acceptance Criteria**

- Article detail pages are publicly accessible.
- The page displays:
  - Title
  - Category
  - Article content
  - Last-updated date
- The article URL uses a readable slug.
- Invalid article URLs return a 404 response.
- Logged-in users can see a Suggest an Edit action.
- Guests can still read the article without registering.

**Implementation Tasks**

- Add a slug field to the Article model.
- Create an article detail URL.
- Create the article detail view.
- Use `get_object_or_404()`.
- Create `article_detail.html`.
- Display title, category, content, and metadata.
- Add a conditional Suggest an Edit action.
- Add readable article styling.

---

#### US-05 — Browse Categories (Should Have)

**User Story**

As a visitor, I want to browse bouldering categories so that I can explore articles by subject.

**Acceptance Criteria**

- The Categories page is publicly accessible.
- All categories are displayed.
- Each category shows its name and description.
- Selecting a category opens a page showing its articles.
- Empty categories are handled gracefully.
- Category URLs use readable slugs.

**Implementation Tasks**

- Create the Category model.
- Add the relationship between Category and Article.
- Create category list and category detail URLs.
- Create category list and category detail views.
- Create category templates.
- Query articles belonging to the selected category.
- Add `get_object_or_404()` handling.
- Add responsive category cards.

---

### Epic 3 — Search

#### US-06 — Search for Articles (Could Have)

**User Story**

As a visitor, I want to search for articles so that I can quickly find information about a particular bouldering topic.

**Acceptance Criteria**

- Search is available without logging in.
- Users can submit a search query.
- Results can match article titles.
- Results may also match article content.
- Matching articles are displayed with links.
- The original query remains visible on the results page.
- A helpful message appears if there are no matches.
- Empty searches are handled without an application error.

**Implementation Tasks**

- Create a search URL.
- Create the search view.
- Read the query from a GET parameter.
- Use Django ORM filtering with `Q`.
- Search article title and content.
- Create `search_results.html`.
- Display the query and matching articles.
- Add a no-results state.
- Add search forms to the homepage or navigation.

---

### Epic 4 — Authentication

#### US-07 — Register for an Account (Must Have)

**User Story**

As a visitor, I want to create an account so that I can suggest improvements to articles.

**Acceptance Criteria**

- A registration form is publicly accessible.
- The user can enter the required account information.
- Password validation uses Django's built-in authentication rules.
- Invalid submissions display useful validation errors.
- A duplicate username cannot be registered.
- Passwords are stored securely using Django's authentication system.
- A successful registration allows the user to continue into the application.

**Implementation Tasks**

- Use Django's built-in User model.
- Create a registration form using `UserCreationForm` or a subclass.
- Create the registration view.
- Add a registration URL.
- Create `register.html`.
- Display form validation errors.
- Redirect or log the user in after successful registration.
- Test valid and invalid registrations.

---

#### US-08 — Log In (Must Have)

**User Story**

As a registered user, I want to log in so that I can access contribution functionality.

**Acceptance Criteria**

- The login page is publicly accessible.
- Valid credentials authenticate the user.
- Invalid credentials produce a clear error message.
- Logged-in users can access protected contribution functionality.
- Users can be redirected back to the page they originally attempted to access where practical.

**Implementation Tasks**

- Configure Django's login view.
- Add the login URL.
- Create `login.html`.
- Configure `LOGIN_REDIRECT_URL`.
- Support Django's `next` parameter where appropriate.
- Add login navigation links.
- Test correct and incorrect credentials.

---

#### US-09 — Log Out (Must Have)

**User Story**

As a logged-in user, I want to log out so that I can securely end my session.

**Acceptance Criteria**

- Logged-in users can access a Logout control.
- Logging out ends the authenticated session.
- The user is redirected to an appropriate public page.
- Protected functionality is no longer accessible after logout.

**Implementation Tasks**

- Configure Django logout functionality.
- Add a logout URL or POST logout form.
- Add Logout to authenticated navigation.
- Configure the logout redirect.
- Test that the session ends correctly.
- Test that protected views redirect after logout.

---

### Epic 5 — Suggested Edits

#### US-10 — Suggest a Change to an Article (Must Have)

**User Story**

As a registered user, I want to suggest changes to an article so that I can help improve BoulderingWiki.

**Acceptance Criteria**

- Only authenticated users can access the Suggest an Edit form.
- The form clearly identifies the article being edited.
- Existing article content is available as the starting proposed content.
- The user can edit the proposed content.
- The user can provide a reason for the suggestion.
- Submitting the form creates a SuggestedEdit record.
- New suggestions default to `pending`.
- Submitting a suggestion does **not** directly modify the published article.
- The user receives confirmation that the suggestion was submitted.

**Implementation Tasks**

- Create the SuggestedEdit model.
- Add relationships to Article and User.
- Add fields for proposed content, reason, status, and creation date.
- Create a ModelForm exposing only user-editable fields.
- Create a login-protected suggestion view.
- Pre-populate proposed content using the current Article content.
- Assign the Article and authenticated User in the view.
- Set status to pending automatically.
- Create `suggest_edit.html`.
- Add Django success messaging.
- Redirect back to the article after submission.
- Test that Article content remains unchanged.

---

#### US-11 — Prevent Guests from Submitting Suggestions (Must Have)

**User Story**

As the site owner, I want guests prevented from suggesting edits so that contributions can be linked to authenticated accounts.

**Acceptance Criteria**

- Guests cannot directly access the Suggest an Edit page.
- Attempting to access the form redirects the guest to Login.
- Guests cannot successfully submit the suggestion endpoint manually.
- After authentication, the user may continue to the intended contribution flow.

**Implementation Tasks**

- Apply `login_required` to the suggestion view.
- Configure the login URL.
- Preserve the requested page through Django's `next` parameter.
- Ensure POST requests are also protected.
- Test anonymous GET requests.
- Test anonymous POST requests.
- Test authenticated access.

---

### Epic 6 — Administration and Moderation

#### US-12 — Access Django Admin (Must Have)

**User Story**

As an administrator, I want to access Django Admin so that I can manage BoulderingWiki content.

**Acceptance Criteria**

- Django Admin is available at `/admin/`.
- Non-staff users cannot access the Admin interface.
- Administrators can manage Articles.
- Administrators can manage Categories.
- Administrators can view SuggestedEdits.
- Administrative functionality uses Django permissions.

**Implementation Tasks**

- Register Category with Django Admin.
- Register Article with Django Admin.
- Register SuggestedEdit with Django Admin.
- Configure useful `list_display` fields.
- Configure search and filtering where useful.
- Create a superuser for development/testing.
- Test access as a superuser.
- Test that regular users cannot access Django Admin.

---

#### US-13 — View Pending Suggestions (Must Have)

**User Story**

As an administrator, I want to view pending edit suggestions so that I can review community contributions.

**Acceptance Criteria**

- Suggested edits are visible in Django Admin.
- The administrator can identify:
  - Article
  - Submitting user
  - Status
  - Submission date
- Suggestions can be filtered by status.
- The administrator can inspect the proposed content and reason.
- Pending suggestions are easy to distinguish from reviewed suggestions.

**Implementation Tasks**

- Configure `SuggestedEditAdmin`.
- Add article, user, status, and created date to `list_display`.
- Add status to `list_filter`.
- Add article/user search if useful.
- Make proposed content and reason available on the change page.
- Order suggestions with recent or pending items first.
- Test the admin moderation view.

---

#### US-14 — Approve or Reject a Suggestion (Must Have)

**User Story**

As an administrator, I want to approve or reject suggested edits so that only reviewed changes affect published articles.

**Acceptance Criteria**

- An administrator can approve a pending suggestion.
- Approving a suggestion updates the associated Article content.
- The suggestion status changes to `approved`.
- An administrator can reject a suggestion.
- Rejecting a suggestion does not change the Article.
- The suggestion status changes to `rejected`.
- Regular users cannot approve or reject suggestions.
- The moderation action cannot accidentally publish a rejected suggestion.

**Implementation Tasks**

- Add approve and reject admin actions.
- For approval:
  - Retrieve the associated Article.
  - Copy `proposed_content` into `Article.content`.
  - Save the Article.
  - Update suggestion status to approved.
- For rejection:
  - Leave Article unchanged.
  - Update suggestion status to rejected.
- Restrict moderation actions to authorised administrators.
- Add admin messages confirming actions.
- Test approved suggestions.
- Test rejected suggestions.
- Test that rejection leaves published content unchanged.

---

#### US-15 — Manage Articles and Categories (Should Have)

**User Story**

As an administrator, I want to create, update, and delete articles and categories so that I can maintain the website's content.

**Acceptance Criteria**

- Administrators can create Articles.
- Administrators can edit Articles.
- Administrators can delete Articles.
- Administrators can create Categories.
- Administrators can edit Categories.
- Administrators can delete Categories when appropriate.
- Articles can be assigned to Categories.
- Slugs are created or maintained correctly.
- Regular users cannot access these management controls.

**Implementation Tasks**

- Configure Article in Django Admin.
- Configure Category in Django Admin.
- Add slug handling.
- Add appropriate Admin list fields.
- Add search/filtering where useful.
- Validate category/article relationships.
- Test create, update, and delete operations.
- Test permissions.

---

### MVP Priority

| Priority | User Stories |
| --- | --- |
| Critical | US-03, US-04, US-07, US-08, US-09, US-10, US-11, US-12, US-13, US-14 |
| High | US-01, US-02, US-05, US-15 |
| Medium | US-06 |

If development time becomes limited, **Search is the safest feature to simplify or postpone**. The moderated edit workflow is more important because it differentiates BoulderingWiki from a basic Django blog.

---

### Definition of Done for the 2-Week MVP

At the end of the project, the application should support this complete journey:

```text
Visitor
   ↓
View Homepage
   ↓
Browse Articles / Categories
   ↓
Read Article
   ↓
Register / Login
   ↓
Suggest an Edit
   ↓
Suggestion saved as Pending
   ↓
Administrator reviews suggestion
   ↓
Approve ────────────── Reject
   ↓                      ↓
Article updated        Article unchanged
   ↓                      ↓
Suggestion Approved   Suggestion Rejected
```

The project should prioritise this complete moderated contribution workflow before adding any optional functionality.

The simplified project narrative is:

**Public knowledge base + authenticated contributions + controlled moderation**

## Design Alterations

The website was originally going to have a hero secrion on the homepage but this was scrapped due to time constraints.

The website was originally going to have custom user profiles where the user can change things like their profile pick and add details to their profile like a bio and links to their socials

A "Create a new post" page was added to the website to allow superusers to create a new post without needing to access the admin portal. 

## AI Usage

AI was used to:
- Generate user stories
- Make code suggestions for styling
- Enhance the UI of the admin portal in sections like comments
- Create the Category model in article/models.py and allow articles to be sorted by categories