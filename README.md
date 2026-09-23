# Love Bouldering

## Introduction

A Django-based Wikipedia-style website dedicated to bouldering. The purpose of this website is to provide an educational resource where visitors can learn about bouldering, while registered users can suggest improvements to articles and write comments on articles. Bouldering is a climbing discipline that is done on short walls - typically in a climbing gym - and/or on small rock formations outdoors without the use of ropes or harnesses. Suggested changes to an article are reviewed, and approved or rejected by an administrator before they can affect published content.

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

## Database Design

Below is a picture of the ERD (entity relationship diagram) for the project

![Diagram of ERD](/documentation/boulder-wiki-erd-white-bg.png)

## Strategy Plane

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

### Excluded Features

Defining what the application will **not** provide is important for preventing scope creep.

The initial version will not attempt to provide:

- Article revision history
- Notifications
- Revision comparison
- Bookmarks
- Social networking
- Private messaging
- Discussion forums
- User comments
- E-commerce
- Personal climbing statistics
- Training logs
- Route tick lists
- Real-time collaborative article editing
- AI-generated articles
- Advanced Wikipedia-style citation management
- Recommendation algorithms

The features listed above are outside the initial scope of the project. These features could be considered in future development but are not required to satisfy the current project objectives.

---

### Scope Plane Summary

The Scope Plane translates the objectives established during the Strategy Plane into a defined set of functional and content requirements.

BoulderWiki will provide a public educational knowledge base where visitors can browse,  search for, and read bouldering information without creating an account. Registered users will be able to contribute improvements through suggested edits, while administrators will retain control over published content through a moderation process.

The MVP prioritises the complete journey from:

**Discover Content → Read Article → Register/Login → Suggest Improvement → Administrator Review → Approved/Rejected**

More advanced social, collaborative, and personal climbing features remain outside the initial scope so that the project stays focused, maintainable, and achievable.

---

## Design Alterations/Additions

The website was originally going to have a hero secrion on the homepage but this was scrapped due to time constraints.

The website was originally going to have custom user profiles where the user can change things like their profile pick and add details to their profile like a bio and links to their socials.

A "Create a new post" page was added to the website to allow superusers to create a new post without needing to access the admin portal. 

The website was originally going to have breadcrumb navigation to communicate hierarchy across pages. This idea was scrapped though since there was not much depth to the hierarchy in the end.

## AI Usage

AI was used to:
- Generate user stories
- Make code suggestions for styling
- Enhance the UI of the admin portal in sections like comments
- Create the Category model in article/models.py and allow articles to be sorted by categories