# Love Bouldering

## Introduction

A Django-based Wikipedia-style website dedicated to bouldering. The purpose of this website is to provide an educational resource where visitors can learn about bouldering, while registered users can suggest improvements to articles and write comments on articles. Bouldering is a climbing discipline that is done on short walls - typically in a climbing gym - and/or on small rock formations outdoors without the use of ropes or harnesses. Suggested changes to an article are reviewed, and approved or rejected by an administrator before they can affect published content.

## Live Site Link

**Live site:** [**Boulder Wiki**](https://love-bouldering-2-69300253a310.herokuapp.com/)

## Project Board Link

**Link:** [**Project Board**](https://github.com/users/Zealous242/projects/11/views/1?visibleFields=%5B%22Title%22%2C%22Status%22%2C%22Labels%22%2C%22Linked+pull+requests%22%2C%22Sub-issues+progress%22%5D&layout=table)

## Device Views

![AmIResponsiveImage](/documentation/device-views.png)

## Project Overview

BoulderWiki is a Wikipedia-style knowledge base about **bouldering as a sport**.

The website is designed to allow visitors to learn about topics such as:

- Bouldering history
- Board climbing
- Climbing techniques
- Grading systems
- Climbing holds
- Training

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

---

## Database Design

Below is a picture of the ERD (entity relationship diagram) for the project

![Diagram of ERD](/documentation/boulder-wiki-erd-white-bg.png)

- The database is designed using PostreSQL
- Tables are created for created for Users, Profiles, Articles, Comments, Suggestions and Categories
- The ERD shows the relationships between these entities

## UX Design - Strategy Plane

### Project Purpose

BoulderWiki is an educational full-stack Django web application designed to provide clear and accessible information about bouldering.

The website allows visitors and guest users to:

- Browse bouldering articles
- Explore articles by category
- Search for information
- Read content without creating an account

Registered users can also:

- Log in securely
- Suggest improvements to existing articles
- Make comments on posts
- Update comments
- Delete comments

Administrators can:

- Manage articles and categories by accessing the Django admin portal
- Review suggested edits by accessing the Django admin portal
- Approve or reject proposed changes
- Create new posts
- Edit existing posts
- Delete posts

To protect the reliability and accuracy of published information, suggested changes enter a moderation workflow rather than immediately changing an article. An administrator reviews each suggestion before approving or rejecting it.

---

### Core Project Goal

The main goal is to create a simple, trustworthy knowledge-sharing platform that demonstrates a complete moderated contribution workflow. 

**Visitor → Discover Content → Read Article → Register / Login → Suggest → Improvement → Administrator Reviews → Approve or Reject**

---

### Site Owner Goals

The primary project goal is to create a useful educational resource while demonstrating the development of a secure, database-driven Django application.

The project objectives are to:

1. **Provide useful bouldering information**  
   Give users a central location for learning about different aspects of bouldering.

2. **Make information easy to discover**  
   Organise articles into meaningful categories and provide clear navigation and search functionality.

3. **Encourage community contributions**  
   Allow registered users to:
   - Suggest improvements when they identify missing, inaccurate, or outdated information
   - Make comments on posts
   - Update existing comments
   - Delete existing comments

4. **Maintain content quality**  
   Prevent unreviewed user contributions from immediately appearing on the public website.

5. **Provide effective content administration**  
   Allow administrators (superusers) to:
   - Create new articles
   - Edit existing articles
   - Create/delete categories
   - Create/delete users
   - Update/change user credentials such as their username and password
   - Approve/reject suggested edits

6. **Create an accessible and responsive experience**  
   Ensure the website works effectively across:
   - Mobiles 
   - Tablets
   - Laptops
   - Desktops

7. **Demonstrate full-stack development skills**  
   Showcase: 
   - Django models 
   - Authentication  
   - Authorisation 
   - CRUD functionality 
   - Forms 
   - Database relationships  
   - Testing 
   - Responsive design 
   - Accessibility 
   - UX desgin principles.

---

### User Goals

The project has three main user groups: **Guests**, **Registered Users**, and **Administrators/Superusers**.

**Guest Users**

Guest users are visitors who want to learn about bouldering without creating an account.

Their main goals are to:

- Quickly understand the purpose of BoulderWiki.
- Browse available bouldering articles.
- Explore information by category.
- Search for specific subjects.
- Read articles without registering.
- Navigate between articles and pages
- Learn more about bouldering.

The website should therefore place as few barriers as possible between a guest and the educational content. Registration is not required simply to browse or read the website.

**Registered Users**

Registered users have the same informational needs as guests but also want to participate in improving the website, and leaving comments on articles to share their thoughts.

Their goals are to:

- Register for an account
- Log in and log out securely
- Browse and read articles
- Identify information that could be improved
- Suggest changes to an article
- Explain why a change is being suggested

A key UX requirement is to make it clear that **suggesting an edit is not the same as directly editing an article**. Only administrators should have the ability to directly edit an article.

**Administrators (Superusers)**

Administrators are responsible for maintaining the website and protecting the quality of its published content.

Their goals are to:

- Create new articles
- Maintain/edit existing articles
- Delete inappropriate or obsolete articles
- Delete inappropriate comments
- Manage article categories by creating new cateogories or deleting existing ones
- Manage users
- Review suggested edits
- Compare proposed content with existing content
- Approve appropriate suggestions
- Reject unsuitable suggestions
- Implement suggested changes
- Provide feedback where appropriate
- Maintain the accuracy and organisation of the knowledge base

The administrator experience should therefore prioritise efficient moderation and content management.

---

### User Needs

The following table connects key user needs with the functionality that BoulderWiki will provide.

| User Need | BoulderingWiki Response |
| --- | --- |
| Learn about bouldering | Educational articles |
| Find specific information | Search functionality |
| Explore related subjects | Categories and related articles |
| Understand unfamiliar terminology | Dedicated educational content |
| Access information quickly | Clear navigation and article structure |
| Read from different devices | Responsive design |
| Participate in the website | User registration and authentication |
| Correct inaccurate information | Suggest-an-edit functionality |
| Know what happened to a contribution | Suggestion status tracking |
| Trust published information | Administrator moderation |
| Manage website content | Django Admin and administrator tools |

---

### Target Audience

The primary target audience is people interested in learning about or improving their knowledge of bouldering.

**Beginners**

Beginners may require information about:

- What bouldering is
- Basic terminology
- Safety
- Equipment
- Grading systems
- Basic techniques
- Gym etiquette

Their experience should prioritise discoverability, clarity, and understandable terminology.

**Intermediate Climbers**

Intermediate climbers may look for more detailed information about:

- Creating a training plan
- Climbing holds
- Strength and conditioning
- Antagonist training
- Hangboarding
- Introduction to board climbing
- Campus board training

Their experience benefits from search, categories, and links between related subjects.

**Experienced Climbers**

Experienced users may use BoulderingWiki as a reference resource or contribute improvements to existing material.

The **Suggest an Edit** workflow is particularly relevant to users who have knowledge or experience they want to contribute without giving them unrestricted access to published content.

---

### Core Value Proposition

> **BoulderWiki provides an accessible, organised, and community-supported knowledge base where people can learn about bouldering and help improve the information through moderated contributions.**

The project's core experience can be summarised as:

**Learn → Explore → Contribute**

---

### User Expectations

Users are likely to arrive with expectations influenced by other knowledge and reference websites.

The interface should therefore feel:

- Informational rather than commercial
- Easy to scan
- Content-focused
- Easy to navigate
- Searchable
- Clearly organised
- Trustworthy
- Accessible
- Consistent between pages

Articles should remain the dominant element of the interface rather than decorative or promotional content.

---

### Project Objectives and User Objectives

The Strategy Plane identifies where project objectives and user objectives overlap.

| Project Objective | User Objective | UX Solution |
| --- | --- | --- |
| Build a useful knowledge base | Learn about bouldering | Structured educational articles |
| Organise information | Find topics quickly | Categories |
| Improve discoverability | Find specific information | Search |
| Encourage participation | Contribute knowledge | Suggest an Edit |
| Encourage sharing opinions | Share opinions | Make comments on articles |
| Maintain accuracy | Trust published information | Moderation workflow |
| Build community participation | Participate in the project | User accounts |
| Maintain content | Access current information | Administrator tools |
| Demonstrate Django skills | Use reliable functionality | Database-driven architecture |
| Support multiple devices | Access information anywhere | Responsive design |
| Protect the application | Use accounts safely | Authentication and authorisation |

---

### Strategic UX Principles

**Content First**

The primary purpose of BoulderWiki is education. Article content should therefore receive greater visual importance than secondary interface elements.

**Browse Without Barriers**

Users should not need an account to consume educational content. Authentication should only become necessary when users attempt to contribute or access account-specific functionality.

**Easy to Explore**

Users should be able to move naturally through the website:

**Homepage → Category → Articles List → Article Page**

Navigation should help users understand where they are and discover additional relevant information.

**Contribution Without Compromising Quality**

Community participation should be encouraged without allowing unreviewed content to immediately alter published information.

The contribution workflow is therefore:

**User Suggestion → Pending Review → Administrator Review → Approved / Rejected**

rather than:

**User Edit → Immediately Published**

**Clear System Feedback**

When users perform actions, the website should clearly communicate the outcome.

For example:

> Your suggested edit has been submitted for review.

Users should also be able to identify whether their suggestions are **Pending**, **Approved**, or **Rejected**.

**Responsive by Design**

The core experience should remain usable across:

**Mobile → Tablet → Laptop → Desktop**

Content and functionality should be prioritised appropriately rather than simply shrinking the desktop interface.

**Accessibility**

Navigation, forms, buttons, headings, and content should be understandable and usable with assistive technologies and keyboard navigation.

---

**Success Criteria**

The project will be considered successful when the core user and project objectives can be achieved reliably.

Success criteria include:

- Visitors can locate and read articles without creating an account.
- Users can browse articles by category.
- Users can search for relevant articles.
- Users can register and authenticate successfully.
- Guests cannot access protected contribution functionality.
- Registered users can submit suggested edits.
- Suggested edits do not automatically alter published articles.
- Users can track the status of their own suggestions.
- Administrators can approve or reject suggestions.
- Approved suggestions correctly update the relevant article.
- Unauthorised users cannot access administrative functionality.
- The website remains usable across mobile, tablet, laptop, and desktop layouts.
- The application provides clear feedback when actions succeed or fail.
- Core functionality is supported by appropriate automated and manual testing.

---

### Strategy Plane Summary

The strategy for **BoulderingWiki** is to create an accessible and trustworthy educational resource that allows anyone to explore information about bouldering while enabling registered users to contribute improvements through a controlled moderation process.

The project balances two primary objectives:

1. Providing users with an easy way to discover and learn about bouldering.
2. Providing the site owner with a secure and manageable system for maintaining high-quality, community-supported content.

The UX will therefore prioritise **clear navigation, search and categorisation, readable article content, responsive design, accessibility, straightforward authentication, transparent contribution status, and administrator-controlled moderation**.

## UX Design — Scope plane

For BoulderingWiki, the scope is divided into two areas:

- **Functional requirements** - the features and interactions the application must provide
- **Content requirements** - the information and content that users need to access

The initial scope focuses on creating a practical **Minimum Viable Product (MVP)** while avoiding unnecessary features that could cause scope creep.

### Functional Requirements

#### Public Content Browsing

Visitors must be able to access the educational content without creating an account.

Users will be able to:

- Visit the homepage.
- Browse the article directory.
- Open and read individual articles.
- Browse articles by category.
- Search for articles.
- Navigate between related areas of the website.

Requiring registration simply to read educational content would create an unnecessary barrier, so public content remains accessible to guests.

---

#### Article Management

BoulderWiki will use a structured article system to store and present educational content.

Each article will contain information such as:

- Title
- Slug
- Content
- Category
- Date created
- Last updated date

Each article belongs to a category, while a category can contain multiple articles.

Administrators will be able to:

- Create articles.
- Edit existing articles.
- Delete articles.
- Assign articles to categories.
- Maintain and update published content.

Normal registered users will not be able to directly modify published articles.

---

#### Categories

Categories will organise articles into logical areas and make the knowledge base easier to explore.

Example categories may include:

- Bouldering Fundamentals
- Techniques
- Equipment
- Safety
- Training
- Grading
- Terminology
- History

Users will be able to select a category and view the articles associated with it.

Administrators will be responsible for creating, editing, and managing categories.

---

#### Search

The website will provide search functionality to help users locate specific information.

Users should be able to search using keywords associated with:

- Article titles
- Article content

Search results should provide enough information for the user to identify relevant articles and navigate to them.

If no matching content is found, the website should provide a clear message rather than displaying an empty or confusing page.

Search will be available to both guests and authenticated users.

---

#### User Registration

Visitors who want to contribute to BoulderingWiki will be able to create an account.

Registration will collect the information required by the authentication system, such as:

- Username
- Email address where required
- Password
- Password confirmation

The system should validate submitted information and provide clear feedback when registration cannot be completed.

Django's built-in authentication and password security functionality will be used wherever appropriate.

---

#### Login and Logout

Registered users will be able to authenticate securely.

The application must provide:

- Login functionality
- Logout functionality
- Authentication-aware navigation
- Appropriate redirects for protected functionality

After authentication, users will gain access to contribution features that are unavailable to guests.

---

#### Suggest an Edit

Registered users will be able to suggest improvements to existing articles.

A suggestion will contain:

- The article being changed
- Proposed article content
- A reason for the suggested change
- The submitting user
- Submission date
- Review status

All new suggestions will initially have a **Pending** status.

Submitting a suggestion must **not immediately modify the published article**.

The contribution workflow will be:

**Registered User → Suggest Edit → Pending Review → Administrator Review → Approved / Rejected**

This moderation process allows community participation while protecting the reliability of published content.

---

#### My Suggestions

Authenticated users will be able to view the suggestions they have previously submitted.

The page should show information such as:

- Article
- Submission date
- Suggestion status
- Administrator feedback where applicable

Possible statuses are:

- **Pending** — awaiting administrator review
- **Approved** — accepted and applied to the article
- **Rejected** — declined and not applied to the article

Users must only be able to access suggestions associated with their own account.

---

#### Administrator Moderation

Administrators will be responsible for reviewing user-submitted changes.

They must be able to:

- View pending suggestions.
- Identify the article associated with a suggestion.
- Identify the submitting user.
- Review proposed content.
- Review the user's reason for the change.
- Approve a suggestion.
- Reject a suggestion.
- Add review feedback where appropriate.
- Record when the suggestion was reviewed.

When a suggestion is approved:

1. The relevant article is updated.
2. The suggestion becomes **Approved**.
3. The review date is recorded.

When a suggestion is rejected:

1. The published article remains unchanged.
2. The suggestion becomes **Rejected**.
3. The review date is recorded.
4. Administrator feedback can be stored for the user.

Administrative functionality will initially be provided primarily through **Django Admin**, reducing the need to create a separate custom content-management system for the MVP.

---

#### User and Permission Management

Different functionality will be available depending on the user's role.

| Functionality | Guest | Registered User | Administrator |
| --- | :---: | :---: | :---: |
| View homepage | ✓ | ✓ | ✓ |
| Browse articles | ✓ | ✓ | ✓ |
| Read articles | ✓ | ✓ | ✓ |
| Browse categories | ✓ | ✓ | ✓ |
| Search | ✓ | ✓ | ✓ |
| Register | ✓ | — | — |
| Log in | ✓ | — | — |
| Suggest an edit | ✗ | ✓ | ✓ |
| View own suggestions | ✗ | ✓ | ✓ |
| Directly edit published articles | ✗ | ✗ | ✓ |
| Create/delete articles | ✗ | ✗ | ✓ |
| Manage categories | ✗ | ✗ | ✓ |
| Review suggestions | ✗ | ✗ | ✓ |
| Manage users | ✗ | ✗ | ✓ |

Permissions must be enforced by the backend rather than relying only on hiding interface controls.

---

### Content Requirements

BoulderingWiki will require enough educational content to demonstrate how users can browse, search, and navigate the knowledge base.

The initial project does not need to contain hundreds of articles. A smaller collection of representative content is sufficient for the MVP.

#### Homepage Content

The homepage should introduce the website and provide clear routes into the knowledge base.

Content may include:

- Website introduction
- Search bar
- Featured article
- Category links
- Popular or recommended topics
- Explanation of how users can contribute

The primary purpose of the homepage is to help users quickly understand the website and begin exploring.

---

#### Article Content

Individual articles should provide clear educational information about a specific bouldering subject.

Article pages may include:

- Article title
- Category
- Last updated date
- Main article content
- Relevant imagery
- Suggest an Edit action for authenticated users
- Edit post action for administrators (superusers)

Example article topics include:

- What Is Bouldering?
- Dynos
- Climbing Holds
- Bouldering Grades
- Climbing Shoes
- Crash Pads
- Bouldering Safety
- Training for Bouldering

---

#### Category Content

Each category page should:

- Identify the category
- Display articles belonging to the category
- Provide links to individual articles

Categories should help users discover information even when they do not know exactly what to search for.

---

#### Search Results Content

Search results should clearly identify relevant articles.

Each search result should display a list of articles with:

- Article title
- Category
- Short excerpt or description
- Link to the full article 

A useful alert message should be displayed when no results match the search query.

---

#### Contribution Content

The website must provide explanatory content around the suggestion process so users understand that submissions are moderated.

Users should be informed that:

- Suggestions do not immediately change articles
- Suggestions are reviewed by administrators
- Suggestions may be approved or rejected
- Their suggestion status can be viewed from their account

Clear messaging will reduce confusion about how the contribution system works.

---

### Navigation Requirements

The primary navigation should provide access to the most important areas of the website.

For guests, this may include:

- Home
- Articles
- Categories
- Search
- Login
- Register

For authenticated users, account-specific options may include:

- My Suggestions
- Profile or account area
- Logout

Article pages may also use breadcrumb navigation to communicate hierarchy, for example:

**Home → Techniques → Dyno**

Navigation should remain consistent across the website and adapt appropriately for smaller screen sizes.

---

### Responsiveness  Requirements

The website must provide a usable experience across the responsive layouts established in the wireframes.

| Device | Approximate Screen Width |
| --- | --- |
| Mobile | ≤ 767px |
| Tablet | 768px–1023px |
| Laptop | 1024px–1439px |
| Desktop | ≥ 1440px |

The functionality should remain consistent across devices, while the layout adapts to the available space.

For example:

- The articles page may adopt a 3-column layout on laptops and larger devices
- The articles page may adopt a 3-column layout on tablets when in landscape mode
- Articles may stack vertically in a single column on mobiles  
- Articles may stack vertically in a single column on tablets when in portrait mode
- Navigation may collapse into a burger menu on mobiles
- Forms should expand appropriately to available width.
- Article content should maintain a comfortable reading width.
- Touch targets should remain usable on smaller devices

---

### Non-Functional Requirements

In addition to the visible functionality, BoulderWiki must meet several quality requirements.

#### Accessibility

The application should use:

- Semantic HTML5.
- Logical heading structures.
- Accessible form labels.
- Keyboard-accessible navigation.
- Visible focus states.
- Alternative text for meaningful images.
- Appropriate colour contrast.
- Clear validation and error messages.
- Text labels rather than colour alone to communicate status.

---

#### Security

The application should:

- Use Django's authentication system.
- Store passwords securely using Django's password handling.
- Use CSRF protection for forms.
- Restrict protected views to authenticated users.
- Restrict moderation functionality to authorised administrators.
- Prevent users from accessing another user's private suggestions.
- Validate submitted data.
- Protect sensitive configuration values.

---

#### Performance

The application should:

- Load pages efficiently.
- Avoid unnecessary database queries.
- Use appropriate Django ORM queries.
- Paginate large article lists where necessary.
- Optimise images and static assets where practical.

---

#### Reliability and Error Handling

The application should provide:

- Form validation.
- Clear success and error messages.
- Appropriate handling of invalid URLs.
- A custom 404 page where practical.
- Protection against invalid or unauthorised requests.
- Automated tests for important functionality.

---

### MVP Feature Prioritisation

The project scope will be prioritised using **Must Have**, **Should Have**, and **Could Have** categories.

#### Must Have

The MVP requires:

- Homepage
- Article directory
- Article detail pages
- Categories
- Search
- Registration
- Login
- Logout
- Suggest an Edit
- Administrator moderation
- Article management
- Category management
- Authentication and authorisation
- Form validation
- Responsive layouts
- Core security measures

These features are required for the primary BoulderingWiki workflow to function.

---

### Excluded Features

Defining what the application will **not** provide is important for preventing scope creep.

The initial version will not attempt to provide:

- Article revision history
- Notifications
- Bookmarks
- Signing up with emails such as Google, Outlook, Yahoo, etc
- Nested comments
- Likes/Dislikes
- Article ratings
- Recommendation algorithms
- Custom admin dashboard
- AI-generated articles
- Private messaging
- Discussion forums

The features listed above are outside the initial scope of the project. These features could be considered in future development but are not required to satisfy the current project objectives.

---

### Project Constraints

- Only authenticated users can comment or submit article suggestions.
- Users can edit and delete only their own comments and suggestions.
- Only superusers can create or edit posts outside Django Admin.
- Draft posts are not visible on the public website.
- Published posts are visible to visitors.
- Suggestions require moderation and use pending, approved, or rejected statuses.
- Editing a reviewed suggestion returns it to pending status.
- Posts may have multiple categories managed through the Category model.
- Post images must use supported Cloudinary image formats.
- Cloudinary credentials must be configured through environment variables.
- User-submitted forms require CSRF protection.
- Comment submissions use POST/Redirect/GET to prevent duplicate comments on refresh.
- Search results are limited to published articles.
- Users cannot access another user’s suggestions by changing the URL.
- Article titles and slugs must be unique.
- The project depends on Django, PostgreSQL-compatible database configuration, Cloudinary, Bootstrap, Summernote, and django-allauth.
- The website must remain usable on desktop and mobile screen sizes.
- Rich-text editors depend on Summernote assets and JavaScript.
- Public article content is rendered as trusted HTML and therefore requires controlled content entry.
- Existing user and database records must be preserved when migrations are applied.
- New functionality must remain consistent with the existing design palette, Bootstrap layout, and shared templates.

---

### Project Deliverables

#### Functional Deliverables

- Public homepage displaying published bouldering articles
- Article detail pages with:
   - Title
   - Author
   -  Categories
   - Featured image
   - Article content
   - Creation and update dates
   - Comments
   
- Multiple article categories.
- Category filtering.
- Article search by title, content, excerpts, and categories.
- Helpful no-results search messages.
- User registration, login, logout, and password management.
- Comment creation, editing, deletion, and timestamps.
- Article change suggestion submission.
- Current article content import into suggestion forms.
- Rich-text suggestion editing.
- User suggestion history page.
- Suggestion status display: pending, approved, or rejected.
- Suggestion editing and deletion by the submitting user.
- Duplicate-comment prevention after page refresh.

---

#### Adiministrative Deliverables

- Django Admin configuration for:
   - Posts
   - Categories
   - Comments
   - Suggestions
   - Users

- Superuser-only post creation page outside Django Admin
- Superuser-only post editing page outside Django Admin
- Post image uploads through Cloudinary
- Rich-text post editing through Summernote
- Multiple category assignment
- Draft and published post statuses
- Suggestion moderation workflow
- Adjustable Posts and Comments admin columns
- Superuser-only create and edit controls

---

#### Technical Deliverables

- Django models and relationships for:
   - Posts
   - Categories
   - Comments
   - Suggestions
   - About content
   - Collaboration requests

- Database migrations for all schema changes.
- Django forms with validation.
- Authentication and authorisation controls.
- CSRF protection on submitted forms.
- Cloudinary configuration for image storage.
- Responsive Bootstrap templates.
- Shared navigation and footer templates.
- Static CSS and JavaScript assets.
- Summernote rich-text integration.
- Search and category filtering using Django ORM queries.

---

#### Quality Deliverables

- Responsive layouts for mobile, tablet, laptop, and desktop.
- Accessible labels, focus states, and controls.
- Helpful success, error, and empty-state messages.
- Permission checks for protected views.
- Ownership checks for user suggestions and comments.
- Django system checks passing.
- Tested authentication and contribution workflows.
- Secure handling of environment variables and Cloudinary credentials.

---

### Scope Plane Summary

The Scope Plane translates the objectives established during the Strategy Plane into a defined set of functional and content requirements.

BoulderWiki will provide a public educational knowledge base where visitors can browse,  search for, and read bouldering information without creating an account. Registered users will be able to contribute improvements through suggested edits, while administrators will retain control over published content through a moderation process.

The MVP prioritises the complete journey from:

**Discover Content → Read Article → Register/Login → Suggest Improvement → Administrator Review → Approved/Rejected**

More advanced social, collaborative, and personal climbing features remain outside the initial scope so that the project stays focused, maintainable, and achievable.

---

## UX Design — Structural Plane

The **Structure Plane** defines how the features and content established in the Scope Plane are organised into an understandable system. It focuses on **interaction design** and **information architecture**.

For BoulderingWiki, the Structure Plane answers questions such as:

- How do users move through the website?
- How is information grouped?
- What happens after a user performs an action?
- How are public, authenticated, and administrative areas separated?
- How does the contribution workflow behave?

The structure is designed around three core user activities:

**Learn → Explore → Contribute**

---

### Information Architecture

The main content hierarchy is:

```text
Homepage
│
├── Articles
│   ├── Article Directory
│   └── Article Details
│
├── Search
│   └── Search Results
│       └── Relevant articles
│
├── Authentication
│   ├── Register
│   ├── Login
│   └── Logout
│
└── Administration
    ├── Articles
    ├── Categories
    ├── Users
    ├── Suggested Edits
    ├── Users
    └── Comments
```

This hierarchy keeps the public knowledge base at the centre of the application while placing contribution and moderation functionality in clearly defined areas.

---

### Primary Navigation Structure

For guest users:

```text
Home | Articles | Categories | Search | Login | Register
```

For authenticated users:

```text
Home | Articles | Categories | Search | My Suggestions | Logout
```

Administrative functionality can remain accessible through Django Admin or an administrator-specific link where appropriate, keeping the public interface focused on educational content.

---

### Homepage Structure

The homepage acts as the main entry point into the knowledge base:

```text
Homepage
│
├── Introduction / Hero Section
├── Search
├── Explore Categories
├── Article List
```

The most important user actions should appear early on the page:

1. Search for information.
2. Browse articles.
3. Explore categories.

Contribution information should remain secondary to the educational purpose of the website.

---

### Article Directory Structure

```text
Article Directory
│
├── Search / Filtering
├── Article List
│   ├── Article Title
│   ├── Category
│   └── Short Summary
└── Pagination
```

Selecting an article takes the user to its Article Detail page. The directory should prioritise scanability so users can quickly identify useful topics.

---

### Article Detail Structure

The Article Detail page is the application's primary content page:

```text
Article Detail
│
├── Article Title
├── Category
├── Last Updated
├── Main Article Content
├── Comments
└── Suggest an Edit
```

Longer articles may also contain a table of contents.

The **Suggest an Edit** action should be visible to authenticated users without distracting from the article. Guests attempting to contribute should be directed towards authentication.

---

### Category Structure

Categories provide an alternative way to explore content:

```text
Categories
    ↓
Articles in Category
    ↓
Article List
```

For example:

```text
Categories
    ↓
Board Climbing
    ↓
Moonboard 
Tension baord
Kilter board
Introduction to board climbing
```

This supports users who want to browse conceptually rather than relying only on search.

---

### Search Structure

```text
Enter Search Query
        ↓
Submit Search
        ↓
Search Results
        ↓
Select Result
        ↓
Article Detail
```

If no results are found:

```text
Search Query
      ↓
No Results
      ↓
Helpful Message
      ↓
Try Another Search / Browse Categories
```

The structure should avoid dead ends by providing alternative routes when a search is unsuccessful.

---

### Authentication Structure

Authentication is required only for contribution and account-specific functionality.

Registration:

```text
Register
   ↓
Submit Details
   ↓
Validation
   ↓
Account Created
   ↓
Login / Authenticated State
```

Login:

```text
Login
  ↓
Credentials Submitted
  ↓
Authentication
  ↓
Return to Intended Page
```

Where possible, users should return to the action they originally intended to complete:

```text
Article
   ↓
Suggest an Edit
   ↓
Login Required
   ↓
Login
   ↓
Return to Suggest Edit
```

This reduces unnecessary friction in the contribution journey.

---

### Suggest an Edit Interaction Structure

The suggested-edit workflow is one of the application's central interactions:

```text
Article Detail
      ↓
Suggest an Edit
      ↓
Edit Form
      ↓
Submit Suggestion
      ↓
Pending Status
      ↓
Admin Review
     ↙     ↘
Approved   Rejected
```

The published article remains unchanged while the suggestion is pending, maintaining a clear distinction between **published content** and **proposed content**.

---

### Suggestion Form Structure

```text
Suggest an Edit
│
├── Article being edited
├── Proposed Content
├── Reason for Change
└── Submit Suggestion
```

The article should be identified automatically rather than asking the user to select it again. The submitting user should also be identified through the authenticated session.

This reduces unnecessary input and helps prevent mistakes.

---

### My Suggestions Structure

```text
My Suggestions
│
├── Pending
├── Approved
└── Rejected
```

Each suggestion should include:

- Article title
- Date submitted
- Status
- Review feedback where available

Only suggestions belonging to the authenticated user should be accessible.

---

### Administrator Moderation Structure

```text
Admin
  ↓
Suggested Edits
  ↓
Pending Suggestions
  ↓
Review Suggestion
  ↓
Compare Existing / Proposed Content
       ↓
Approve or Reject
```

If approved:

```text
Approve
   ↓
Manually Update Article Content
   ↓
Mark Suggestion Approved
   ↓
Record Review Date
```

If rejected:

```text
Reject
   ↓
Article Unchanged
   ↓
Store Feedback
   ↓
Mark Suggestion Rejected
```

The administrator workflow should make pending work and previously reviewed contributions easy to distinguish.

---

### Role-Based Interaction Structure

| Feature | Guest | Registered User | Administrator |
| --- | :---: | :---: | :---: |
| Browse content | ✓ | ✓ | ✓ |
| Search | ✓ | ✓ | ✓ |
| Read articles | ✓ | ✓ | ✓ |
| Register | ✓ | — | — |
| Login | ✓ | — | — |
| Suggest edits | ✗ | ✓ | ✓ |
| View own suggestions | ✗ | ✓ | ✓ |
| Create new articles | ✗ | ✗ | ✓ |
| Directly edit articles | ✗ | ✗ | ✓ |
| Delete articles | ✗ | ✗ | ✓ |
| Review suggestions | ✗ | ✗ | ✓ |
| Manage categories | ✗ | ✗ | ✓ |
| Manage users | ✗ | ✗ | ✓ |

These boundaries must be enforced by the backend even if a user manually attempts to access a protected URL.

---

### Error and Recovery Structure

#### Invalid URL

```text
Invalid URL
   ↓
404 Page
   ↓
Return Home / Browse Articles
```

#### Invalid Form

```text
Invalid Form
   ↓
Input Validation Message
   ↓
Correct Input
   ↓
Resubmit
```

#### Unauthorised Action

```text
Unauthorised Action
   ↓
Login or Permission Message
   ↓
Return to Appropriate Page
```

Users should rarely encounter a dead end. Error states should provide an appropriate next action wherever possible.

---

### Responsive Structural Behaviour

The information architecture remains consistent across devices while its presentation adapts to available space.

Larger screens:

```text
Header
------------------------------------------------
Main Page or Article Content     
------------------------------------------------
Footer
```

Mobile:

```text
Header
Search
Main Page or Article Content
Footer
```

This preserves a consistent mental model across desktop, laptop, tablet, and mobile layouts.

---

### Interaction Design Principles

#### Predictability

Interface labels should clearly communicate their action, for example:

- Read Article
- Suggest an Edit
- Submit Suggestion
- Approve
- Reject
- View My Suggestions

#### Feedback

Important actions should produce clear feedback, for example:

> Your suggested edit has been submitted and is awaiting review.

#### Prevention

The design should prevent avoidable mistakes. For example:

- The authenticated user is automatically associated with their suggestion.
- The current article is automatically associated with the Suggest an Edit form.
- Normal users are not presented with administrator controls.
- Invalid form data is identified before processing.

#### Recovery

When an error occurs, users should receive clear information about what went wrong and how to correct it.

---

### Core User Flows

#### Learning Journey

```text
Homepage
   ↓
Search / Category / Articles
   ↓
Article Detail
```

#### Contribution Journey

```text
Article Detail
   ↓
Suggest an Edit
   ↓
Login if Required
   ↓
Suggestion Form
   ↓
Submit
   ↓
Pending
   ↓
My Suggestions
```

#### Moderation Journey

```text
Admin
   ↓
Pending Suggestions
   ↓
Review Suggestion
   ↓
Approve / Reject
   ↓
Article and Status Updated
```

These three flows represent the central structure of BoulderingWiki.

---

### Relationship to the Database Structure

The interaction structure is supported by the application's core data relationships:

```text
Category
   │
   └────< Article
              │
              └────< Suggestion >──── User
```

These relationships support the main journeys:

- Categories organise Articles.
- Articles provide educational content.
- Users submit SuggestedEdits against Articles.
- Administrators review SuggestedEdits.
- Approved changes can update the relevant Article.

The database therefore supports the information architecture rather than determining the user experience independently.

---

### Structure Plane Summary

The Structure Plane organises BoulderWiki into a clear information architecture and a predictable set of user interactions.

The website is structured around three primary activities:

**Learn → Explore → Contribute**

Public users can browse, search, and read educational content without authentication. Registered users can move from reading an article into a controlled contribution workflow, while administrators manage content quality through moderation.

The structure deliberately keeps the article system at the centre of the application, with authentication, contribution, and administrative functionality supporting the educational experience rather than interrupting it.

The three central journeys can be summarised as:

**Learning Journey:**  
**Discover → Explore → Read → Continue Learning**

**Contribution Journey:**  
**Read → Suggest → Submit → Track**

**Moderation Journey:**  
**Review → Approve/Reject → Update**

---

## UX Design — Skeleton Plane

The **Skeleton Plane** defines how the application’s interface elements are arranged on each page. It focuses on three areas: **interface design**, **navigation design**, and **information design**.

For BoulderWiki, the Skeleton Plane determines where key elements such as navigation, search, article content, forms, buttons, status messages, and administrative controls should appear so users can complete tasks efficiently and consistently.

---

### Interface Design

The interface should prioritise clarity, consistency, and readability. BoulderingWiki is primarily an educational website, so content should remain the central focus.

The interface should use a consistent page framework containing:

```text
Header
│
├── Logo / Site Name
├── Primary Navigation
└── Account Controls

Main Content
│
├── Page Heading
├── Page-Specific Content
└── Primary Actions

Footer
│
├── Secondary Navigation
├── Project Information
└── Supporting Links
```

This consistent layout helps users understand where to find common actions regardless of the page they are viewing.

---

### Global Header

The global header should appear across the main public-facing pages.

It should contain:

- Logo or site name
- Home
- Articles
- Categories
- Login and Register for guests
- Logout for authenticated users
- Mobile menu control on smaller screens

---

### Mobile Navigation

On smaller screens, the full navigation should collapse into a burger menu to conserve horizontal space.

```text
--------------------------------
BoulderingWiki          Menu ☰
--------------------------------
```

When opened:

```text
Home
Categories
Logout
```

The navigation should remain keyboard accessible and clearly indicate whether the menu is expanded or collapsed.

---

### Search Placement

Search is a major discovery tool and should be easy to find.

Search may appear:

- In the global header on larger screens
- As a dedicated search input on the homepage
- On the Article Directory

The homepage search should be more prominent than secondary search controls.

```text
-----------------------------------------
What would you like to learn about?

[ Search bouldering topics... ] [Search]
-----------------------------------------
```

The search control should include a clear label or accessible name.

---

### Wireframes

A set of wireframes for desktops was not required since the website would look the same on desktops and laptops. You can therefore treat the laptop wireframes the same as desktop wireframes.

#### Laptops and Larger Devices:

![Diagram of  wireframes for laptops and larger devices](/documentation/wireframes/laptops-and-larger-devices/laptops-and-larger-devices.png)

#### Tablets (Portrait):

![Diagram of tablet portrait wireframes](/documentation/wireframes/tablet/portrait/tablet-portrait.png)

#### Tablets (Landscape):

![Diagram of tablet landscape wireframes](/documentation/wireframes/tablet/landscape/tablet-landscape.png)

#### Mobiles:

![Diagram of mobile wireframes](/documentation/wireframes/mobile/mobile-wireframes.png)

---

### Article Readability

Article content should use:

- Clear H2 and H3 headings
- Short paragraphs
- Lists where appropriate
- Comfortable line length
- Adequate spacing
- Images only where they support understanding
- Descriptive captions where necessary

The interface should avoid placing too many controls inside the reading area.

---

### Form Design

Forms throughout the application should use a consistent structure:

```text
Label
[ Input ]

Supporting text or error message

Label
[ Input ]

Supporting text or error message

[ Primary Action ]
```

Form labels should remain visible rather than relying entirely on placeholder text.

Validation errors should appear close to the relevant field.

```text
Username
[ name ]

This username is already in use.
```

This reduces the distance between the problem and its explanation.

---

### Information Design

Information design determines how content is presented so users can understand it quickly.

For BoulderWiki, the visual hierarchy should generally follow:

```text
Page Title
↓
Context / Metadata
↓
Primary Content
↓
Primary Action
↓
Related / Secondary Content
```

For example, on an article page:

```text
Dyno                        ← Page title
Techniques · Updated ...    ← Metadata
Article text                ← Primary content
Suggest an Edit             ← Primary action
```

This keeps the user's attention on the reason they visited the page.

---

### Feedback Messages

The application should provide immediate confirmation after important actions.

Success examples:

> Your suggested edit has been submitted and is awaiting review.

> Your account has been created successfully.

> The suggestion has been approved.

Error examples:

> Please correct the highlighted fields.

> You must be logged in to suggest an edit.

> You do not have permission to access this page.

Feedback should appear near the relevant content and should not rely on colour alone.

---

### Empty States

Pages should remain useful even when there is no content to display.

For My Suggestions:

```text
You haven't submitted any suggestions yet.

Browse an article and select "Suggest an Edit"
if you would like to contribute.

[ Browse Articles ]
```

For Search:

```text
No articles matched "campus board".

Try another search or browse the categories.

[ Browse Categories ]
```

Good empty states explain what happened and provide a useful next step.

---

### Responsive Skeleton

The layout should adapt according to screen size without changing the core information architecture.

| Device | Skeleton Behaviour |
| --- | --- |
| Mobile | Single column, collapsed navigation, stacked cards and forms |
| Tablet | Wider single column or limited two-column layouts |
| Laptop and larger devices | Full navigation, multi-column layouts where useful |

The order of content should remain logical when columns collapse.

---

### Touch and Interaction Targets

Interactive controls should be large enough to use comfortably on touch devices.

This includes:

- Navigation links
- Buttons
- Form controls
- Search controls
- Menu toggles
- Pagination
- Category cards

Controls should also have enough spacing to reduce accidental selections.

---

### Consistency Across Pages

Common elements should behave consistently throughout the website.

For example:

- The logo always returns to Home.
- Search behaves consistently.
- Primary buttons share the same styling.
- Form validation follows the same pattern.
- Statuses use consistent wording.
- Article cards follow the same layout.
- Navigation changes predictably after login.

Consistency reduces the amount users need to learn.

---

### Accessibility Considerations

The Skeleton Plane should support accessibility before visual styling is applied.

The layout should include:

- Logical heading order
- Semantic landmarks
- Visible form labels
- Keyboard-accessible controls
- Logical tab order
- Skip-to-content support where appropriate
- Clear focus states
- Descriptive links
- Accessible status messages
- Responsive layouts that work with zoom
- No essential information communicated through position or colour alone

Accessibility should therefore be part of the interface structure rather than added only during the Surface Plane.

---

### Skeleton Plane Summary

The Skeleton Plane defines how BoulderingWiki's information architecture and interaction flows are translated into usable page layouts.

The interface prioritises:

**Content → Navigation → Action → Feedback**

Article content remains the dominant element of the application, while search, categories, authentication, contribution tools, and moderation controls are positioned according to their importance to each user journey.

The skeleton establishes consistent patterns for:

- Global navigation
- Search
- Article layouts
- Categories
- Authentication forms
- Suggested edits
- User suggestion tracking
- Administrative review
- Feedback and error states
- Responsive layouts
- Accessibility

## UX Design — Surface Plane

The **Surface Plane** defines the final visual appearance of BoulderingWiki. It brings together the decisions made throughout the previous UX planes and determines how the interface should **look and feel** to the user.

It focuses on areas such as:

- Colour
- Typography
- Imagery
- Icons
- Spacing
- Buttons
- Cards
- Forms
- Navigation styling
- Visual hierarchy
- Responsive presentation
- Accessibility
- Consistency
---

### Visual Design Goals

The interface should support the educational purpose of the website rather than compete with it.

The main visual goals are:

1. **Readability** - articles should be comfortable to read for extended periods.
2. **Clarity** - important actions and information should be immediately identifiable.
3. **Consistency** - components should look and behave consistently.
4. **Accessibility** - visual choices should support users with different accessibility needs.
5. **Identity** - the interface should have a recognisable bouldering-inspired visual style.
6. **Trust** - the design should reinforce the moderated, educational nature of the platform.
7. **Responsiveness**- the visual system should work consistently across mobile, tablet, laptop, and desktop.

---

### Visual Identity

BoulderingWiki should combine the clarity of an educational reference website with the visual character of modern climbing environments.

Visual inspiration can come from:

- Climbing walls
- Rock surfaces
- Climbing holds
- Chalk
- Outdoor environments
- Topographic shapes
- Route markers

These influences should remain subtle. The interface should not become overly decorative because the primary purpose is reading and discovering information.

### Color Palette

![Diagram of ERD](/documentation/color-palette.png)

### Typography

Typography is especially important because BoulderingWiki is a content-heavy application.

The type system should prioritise readability over decorative styling.

A simple hierarchy could use:

| Element | Relative Importance |
| --- | --- |
| H1 | Article/page title |
| H2 | Major content section |
| H3 | Subsection |
| Body | Main article content |
| Small | Metadata/supporting information |

A clean sans-serif font would work well for interface elements.

Possible font families include:

- Inter
- Roboto
- Open Sans
- Source Sans
- System UI fonts

A system font stack would also reduce external dependencies and improve loading performance.

---

### Typography Hierarchy

A typical article could visually follow:

```text
DYNAMIC MOVEMENT
Page / Article Title

Introduction
Major section heading

Generating Momentum
Subsection heading

Bouldering involves solving movement problems...
Normal body content

Updated 8 September 2026
Secondary metadata
```

Typography should make it possible to understand the structure of an article even when scanning rather than reading every sentence.

### Article Readability

Article pages should provide comfortable reading conditions.

The design should avoid stretching text across the entire width of large monitors. Instead, article content should use a controlled maximum width.

Important considerations include:

- Comfortable line length
- Sufficient line height
- Clear paragraph spacing
- Strong heading hierarchy
- Adequate contrast
- Limited use of bold text
- Consistent lists
- Appropriate image spacing

On desktop, unused space can support a table of contents or related information.

---

### Navigation Styling

The navigation should visually separate itself from the main article content while remaining simple.

```text
┌───────────────────────────────────────────────────────┐
│ BoulderWiki   Home  Articles  Categories  Search   │
│                                    Login   Register   │
└───────────────────────────────────────────────────────┘
```

The current section should have a visible active state. Hover and keyboard focus states should also be visually identifiable.

---

### Button Design

Buttons should follow a consistent visual hierarchy.

#### Primary Buttons

Used for important actions such as:

- Search
- Login
- Create Account
- Submit Suggestion
- Approve

These should use the strongest brand styling.

#### Secondary Buttons

Used for actions such as:

- Cancel
- Back
- View Details
- Browse Articles

These should be visually quieter.

#### Destructive Actions

Actions such as:

- Delete
- Reject

should have a distinct treatment that communicates additional risk.

Destructive styling should not be used for ordinary navigation.

---

### Button States

Interactive elements should visually communicate their current state.

Buttons should account for:

- Default
- Hover
- Focus
- Active
- Disabled

A strong keyboard focus indicator is particularly important for accessibility.

---

### Link Styling

Links within article content should be clearly distinguishable from normal text.

Links should not depend entirely on colour. Options include underlining links, providing clear hover treatment, and using visible keyboard focus styling.

Users should immediately understand which text is interactive.

---

### Form Styling

Forms should have a simple and predictable appearance.

```text
Username

┌──────────────────────────────┐
│                              │
└──────────────────────────────┘

Password

┌──────────────────────────────┐
│                              │
└──────────────────────────────┘

[ Login ]
```

Inputs should provide clear labels, borders, focus states, error states, help text, and required-field indicators where appropriate.

Placeholder text should not replace permanent field labels.

---

### Form Validation Styling

Errors should appear close to the field that caused them.

```text
Username

┌──────────────────────────────┐
│ name                        │
└──────────────────────────────┘

⚠ This username is already in use.
```

Error messages should explain what went wrong and how the user can correct it.

The interface should not rely solely on a red border to indicate an error.

---

### Feedback and Alert Styling

System feedback should be visually distinguishable from normal page content.

Examples include:

```text
✓ Your suggestion has been submitted successfully.
○ Your suggestion is awaiting administrator review.
⚠ Please correct the errors below.
```

Messages should use consistent visual treatments for success, information, warning, and error states.

The wording should remain concise and actionable.

---

### Imagery

Images should support learning rather than being included purely for decoration.

Useful imagery may include:

- Bouldering techniques
- Climbing holds
- Equipment
- Climbing walls
- Outdoor boulders
- Body positioning examples

Images should:

- Be relevant to the article
- Be appropriately compressed
- Include alternative text when informative
- Scale responsively
- Maintain suitable aspect ratios
- Include attribution where licensing requires it

Decorative images should use appropriate accessibility treatment so they do not add unnecessary screen-reader content.

---

### Iconography

Icons can improve scanning when used alongside labels.

Possible uses include:

- Search
- User account
- Menu
- Edit
- Category
- Approved
- Pending
- Rejected

Icons should generally accompany text when their meaning may not be immediately obvious.

For example:

```text
✎ Suggest an Edit
```

is clearer than presenting an unexplained pencil icon alone.

---

### Responsive Visual Design

The visual identity should remain consistent across the project's four responsive ranges:

| Device | Width |
| --- | ---: |
| Mobile | ≤ 767px |
| Tablet | 768–1023px |
| Laptop | 1024–1439px |
| Desktop | ≥ 1440px |

A desktop layout may present:

```text
┌──────────────────────────────────────────────┐
│ Header                                       │
├──────────────────────────────┬───────────────┤
│                              │               │
│ Article                      │ Table of      │
│ Content                      │ Contents      │
│                              │               │
├──────────────────────────────┴───────────────┤
│ Related Articles                             │
└──────────────────────────────────────────────┘
```

On mobile, the content should stack into a logical single-column layout.

The branding remains consistent while the layout adapts.

---

### Mobile Visual Priorities

On smaller screens, the design should prioritise:

1. Article title
2. Essential metadata
3. Main content
4. Primary actions
5. Related content

Decorative elements should be reduced where necessary.

Buttons and navigation controls should remain large enough for comfortable touch interaction.

---

### Accessibility and Visual Design

Accessibility should influence every Surface Plane decision.

The final interface should provide:

- Strong text/background contrast
- Visible keyboard focus indicators
- Readable font sizes
- Sufficient line spacing
- Clearly identifiable links
- Large enough interaction targets
- Text labels for status information
- Alternatives to colour-only communication
- Responsive typography
- Accessible form states
- Alternative text for informative images

Visual design should never reduce usability simply to create a more distinctive aesthetic.

---

### Visual Consistency

Reusable components should follow the same visual rules throughout the application.

| Component | Consistency Requirement |
| --- | --- |
| Header | Same branding and navigation pattern |
| Buttons | Consistent hierarchy and states |
| Forms | Same labels, inputs and validation |
| Cards | Consistent spacing and typography |
| Articles | Consistent reading layout |
| Categories | Consistent card structure |
| Statuses | Same terminology and visual treatment |
| Alerts | Consistent success/error patterns |
| Breadcrumbs | Same placement and styling |

This also makes the frontend easier to maintain because shared CSS classes and Django template components can be reused.

---

### Design System

Rather than styling every page independently, BoulderWiki should use a small reusable design system.

```text
Colours
│
├── Primary
├── Secondary
├── Background
├── Text
├── Success
├── Warning
└── Error

Typography
│
├── H1
├── H2
├── H3
├── Body
└── Small / Metadata

Components
│
├── Buttons
├── Inputs
├── Cards
├── Alerts
├── Navigation
├── Breadcrumbs
└── Status Badges

Layout
│
├── Container widths
├── Grid
├── Spacing
└── Breakpoints
```

This provides a single visual language across the project and makes later design changes easier because components can be updated centrally rather than individually.

---

### Surface Plane Success Criteria

The Surface Plane can be considered successful when:

- The visual identity is consistent across the application.
- Articles are comfortable to read.
- Navigation is immediately recognisable.
- Primary and secondary actions are visually distinct.
- Interactive elements provide hover and focus feedback.
- Form states are easy to understand.
- Suggestion statuses are identifiable without relying only on colour.
- The interface works visually across all devices
- Images support rather than distract from educational content.
- Colour contrast meets accessibility requirements.
- Components can be reused throughout the project.
- The interface feels appropriate for a trustworthy educational bouldering resource.

---

### Surface Plane Summary

The Surface Plane completes the UX design process by applying a coherent visual language to the structure established in the previous planes.

BoulderWiki should have an interface that feels:

**Informative → Approachable → Trustworthy**

The design should combine a clean educational layout with subtle visual references to bouldering through colour, imagery, icons, and branding.

The most important visual priority remains the content itself. Typography, spacing, colour, cards, buttons, imagery, and navigation should all make that content easier to discover, understand, and contribute to.

A reusable visual system should establish consistent rules for:

- Colour
- Typography
- Spacing
- Navigation
- Buttons
- Forms
- Cards
- Status indicators
- Alerts
- Imagery
- Responsive behaviour
- Accessibility

---

## Design Alterations/Additions

The website was originally going to have a hero secrion on the homepage but this was scrapped due to time constraints.

The website was originally going to have custom user profiles where the user can change things like their profile pick and add details to their profile like a bio and links to their socials.

A "Create a new post" page was added to the website to allow superusers to create a new post without needing to access the admin portal. 

A "My suggestions" page was added to the website to allow registered users to keep track of the article changes they suggest. On this page they can see:
- A list of suggestions 
- What post they are for  
- When they were created
- If they have been approved or rejected

The user can also update, edit or delete suggestions on this page. 

The website was originally going to have breadcrumb navigation to communicate hierarchy across pages. This idea was scrapped though since there was not much depth to the hierarchy in the end.

---

## Website Features

### Visitor Features

- View published bouldering articles
- Browse article cards with titles, excerpts, images, authors, dates, and categories
- Open detailed article pages
- Search articles by title, content, excerpt, or category
- Filter articles by category
- Receive a helpful message when no search results are found
- View article comments
- Register for an account
- Log in and log out
- Reset or manage account passwords

### Registered User Features

- Submit comments on articles
- Edit personal comments
- Delete personal comments
- View comment creation and edit dates
- Submit article change suggestions
- Import existing article content into a suggestion editor
- Edit submitted suggestions
- Delete submitted suggestions
- View suggestion history
- View whether suggestions are pending, approved, or rejected
- See the total number of submitted suggestions in the navbar

### Administrator (Superuser) Features

- Create new posts without accessing Django Admin
- Edit existing posts without accessing Django Admin
- Upload post images through Cloudinary
- Add rich-text article content
- Assign multiple categories to posts
- Publish posts or save them as drafts
- Access Django Admin for full content management
- Manage categories
- Review and manage comments
- Review user suggestions
- Approve or reject suggestions
- Resize columns in the Posts and Comments admin tables

### Content Features

- Rich-text article editing through Summernote
- Rich-text suggestion editing.
- Featured images stored with Cloudinary.
- Multiple categories per article.
- Draft and published post statuses.
- Article excerpts and full content.
- Automatic post creation and update timestamps.
- Automatic comment edit timestamps.
- User-specific suggestion records.

### Interface Features

- Responsive Bootstrap layout.
- Fixed navbar.
- Home-page search bar.
- Fixed, centered search bar beneath the navbar.
- Dismissible notification alerts.
- Password visibility toggle with Font Awesome icons.
- Responsive article cards with consistent heights.
- Superuser-only Create post and Edit post controls.
- Accessible labels and button descriptions.

### Future Features

- Article revision history
- Notifications
- Bookmarks
- Signing up with emails such as Google, Outlook, Yahoo, etc
- Nested comments
- Likes/Dislikes
- Article ratings
- Recommendation algorithms
- Custom admin dashboard
- AI-generated articles
- Private messaging
- Discussion forums

---

## Bug Fxing


---

## Testing

A detailed documentation of the testing done can be found at [Testing](/TESTING.md)

---

## Deployment

The live deployed application can be found deployed on [Heroku](https://love-bouldering-2-69300253a310.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

!!! IMPORTANT !!! 

- ⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! 
- ⚠️ Replace the keys below with your own actual keys used; example: if not using Cloudinary, then remove those keys, or replace with whatever ones you're using. 

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

---

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

---

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

---

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```
---

### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

🛑 !!! ATTENTION Zealous242 !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️
⚠️ Replace the keys below with your own actual keys used; example: if not using Cloudinary | AWS, then replace those keys with whatever keys you're using. ⚠️

🛑 --- END --- 🛑

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

---

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/Zealous242/love-bouldering-2).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/Zealous242/love-bouldering-2.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/Zealous242/love-bouldering-2)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

---

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/Zealous242/love-bouldering-2).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

---

### Local VS Deployment

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss any differences between the local version you've developed, and the live deployment site. Generally, there shouldn't be [m]any major differences, so if you honestly cannot find any differences, feel free to use the following example:

⚠️ --- END --- ⚠️

There are no remaining major differences between the local version when compared to the deployed version online.

---

## AI Usage

AI was used to:
- Generate user stories
- Make code suggestions for styling
- Enhance the UI of the admin portal in sections like comments
- Create the Category model in article/models.py and allow articles to be sorted by categories
- Create the Suggestions model article/models.py to allow users to make article change suggestions 
- Test and debug the application

---

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |
| [![badge](https://img.shields.io/badge/Copilot-grey?logo=githubcopilot&logoColor=##000000)](https://github.com/copilot) | Help debug, troubleshoot, and explain things. |

## Credits