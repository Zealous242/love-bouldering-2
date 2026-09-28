# Testing

## Lighthouse Testing

Lighthouse testing was done in Chrome to assess the application for Performance, Accessibility, Best Practices, and SEO.

Testing was performed on nine core pages that a user will visit. The pages were tested for mobiles and desktops.

The more images that a page had, the lower the score would be. This meant that pages like the "Homepage" which had a lot of images on were the ones that achieved the lowest scores. In fact, the homepage was the page that achieved the lowesst scores because of this. 

Each article has it's own page, but for the sake of this document, the page that shows an articles content will be referred to as the "Article Details" page. 

While the scores of some of the pages like the "About" page tend to be similar each time they're tested, the scores of other pages like the "Homepage" and "Article Details" page can be inconsistent because the content on them varies. For example, the "Homepage" had a higher score when it had much less articles on it because this meant it has much fewer images. The "Article Details" page varies depending on how much content has been written in the corresponding article. 

### Homepage

![Lighthouse test for Homepage](/documentation/testing/lighthouse-testing/homepage.png)

### About Page

![Lighthouse Test For About Page](/documentation/testing/lighthouse-testing/about.png)

### Create Article Page

![Lighthouse Fest For Create Article Page](/documentation/testing/lighthouse-testing/create-article.png)

### Manage Articles Page

![Lighthouse Test For Manage Articles Page](/documentation/testing/lighthouse-testing/manage-articles.png)

### Categories Page

![Lighthouse Test For Categories Page](/documentation/testing/lighthouse-testing/categories.png)

### Suggestions Page

![Lighthouse Test For Suggestions Page](/documentation/testing/lighthouse-testing/suggestions.png)

### Registration Page

![Lighthouse Test For Registration Page](/documentation/testing/lighthouse-testing/registration.png)

### Login Page

![Lighthouse Test For Login Page](/documentation/testing/lighthouse-testing/login.png)

### Article Details Page

![Lighthouse Test For Article Details Page](/documentation/testing/lighthouse-testing/article-details.png)

### Discussion

From the lighthouse tests that were done, the main area that could be imrpoved on is performance. This could be done by using more modern image formats for articles - most articles use PNG and JPG formats. This would reduce image file sizes while also maintaining image quality.

 Best practices could also be improved by using the HTTPS protocol instead of HTTP. In addtion to this, there is also room for improvement with Accessibility and SEO, but this isn't that necessary given that the scores for these areas were above 90 across the board. 

SEO could be improved by includiing more relevant meta tags with descriptions. 

Accessibility could be improved by changing background, foreground and text colors to increase color contrast ratios. 

## HTML5 Validation

The deployed BoulderWiki website was tested using the [W3C HTML Validator](https://validator.w3.org/).

For the validation testing, HTML5 code was copied from the page sources of the pages on the deployed site and pasted into the validators direct-input field. The URI link was also pasted into the validator for comparison. 

### Homepage

![Homepage validations](/documentation/testing/html-css-js-validation/html-validation/homepage.png)

The error message in the top-left image were fixed by appending px to ```style="top: 70```. 

A h1 tag was added to the top of the Homepage.

The info messages didn't matter that much but were resolved by removing trailing slashes from hr and meta tags. 

### About Page

![About Page Validation](/documentation/testing/html-css-js-validation/html-validation/about.png)

No errors returned

### Create Article Page

![Create Article Page Validation](/documentation/testing/html-css-js-validation/html-validation/create-article.png)

The errors and warnings shown in the image above were being caused by the Summernote rich text field. 

These errors were fixed by adding the HTML5SummernoteWidget class in article/forms.py and adding some properties and methods to the class. The code below was implemented in the article/forms.py file to achieve this:

```python
class HTML5SummernoteWidget(SummernoteWidget):
    def render(self, name, value, attrs=None, **kwargs):
        rendered = super().render(name, value, attrs, **kwargs)
        rendered = rendered.replace(
            '<style>\niframe.note-fullscreen {\n'
            '  position: fixed;\n'
            '  top: 0;\n'
            '  left: 0;\n'
            '  width: 100vw!important;\n'
            '  height: 100vh!important;\n'
            '  z-index: 4000;\n'
            '}\n</style>\n',
            '',
        )
        rendered = re.sub(
            r'<div class="summernote-div"\s+class="([^"]*)"',
            r'<div class="summernote-div \1"',
            rendered,
        )
        rendered = re.sub(
            r'<div\b[^>]*class="([^"]*summernote-div[^"]*)"[^>]*>',
            r'<div class="\1">',
            rendered,
        )
        rendered = rendered.replace(' frameborder="0"', '')
        rendered = rendered.replace('hidden="true"', 'hidden')
        return re.sub(
            r'(<(?:input|img|hr|meta|link|br|area|base|col|embed|param|source|track|wbr)\b[^>]*?)\s*/>',
            r'\1>',
            rendered,
        )
```

After implementing the code above, the errors in the validator disappeared with the exception of the info message for the URI input. The remaining info message was not addressed because trying to fix it wasn't that necessary. 

###  Manage Articles Page

![Manage Articles Page Validation](/documentation/testing/html-css-js-validation/html-validation/manage-articles.png)

The warning message that occured from URI input was fixed by adding h1 tags to the login.html, logout.html and signup.html files as top-level headings. 

h2 tags were replaced by h1 tags.  

###  Categories Page

![Categories Page Validation](/documentation/testing/html-css-js-validation/html-validation/categories.png)

No errors returned

### Suggestions Page

![Suggestions Page Validation](/documentation/testing/html-css-js-validation/html-validation/suggestions.png)

No errors returned

###  Logout Page

![Logout Page Validation](/documentation/testing/html-css-js-validation/html-validation/logout.png)

No errors returned

### Login Page

![Login Page Validation](/documentation/testing/html-css-js-validation/html-validation/login.png)

No errors returned

### Registration Page

![Registration Page Validation](/documentation/testing/html-css-js-validation/html-validation/registration.png)

The first error was being caused by the ```{{ form.as_p }}``` django template code in signup.html with more explicit valid field wrappers. Password input groups were also moved into valid div elements. 

The following code was implemented in ```templates\account\signup.html``` to acheive the fixes: 

```html
    <div id="username-field" class="mb-3">
          {{ form.username.label_tag }}
          {{ form.username }}
          {{ form.username.errors }}
        </div>
        <div class="mb-3">
          {{ form.email.label_tag }}
          {{ form.email }}
          {{ form.email.errors }}
        </div>
        <div class="mb-3">
          {{ form.password1.label_tag }}
          <div class="input-group">
            {{ form.password1 }}
            <button type="button" class="btn btn-outline-secondary password-toggle"
              data-password-target="id_password1" aria-label="Show password"
              title="Show password" aria-pressed="false">
              <i class="fas fa-eye" aria-hidden="true"></i>
            </button>
          </div>
          {{ form.password1.errors }}
        </div>
        <div class="mb-3">
          {{ form.password2.label_tag }}
          <div class="input-group">
            {{ form.password2 }}
            <button type="button" class="btn btn-outline-secondary password-toggle"
              data-password-target="id_password2" aria-label="Show password"
              title="Show password" aria-pressed="false">
              <i class="fas fa-eye" aria-hidden="true"></i>
            </button>
          </div>
          {{ form.password2.errors }}
        </div>

```

Some JavaScript and other code was also added. The exact implementation details can be found by looking at the commit history of this project. 

### Article Details Page

![Article Details Page Validation](/documentation/testing/html-css-js-validation/html-validation/article-details.png)

The errors in the image above were fixed by replacing the SummernoteWidget() with HTML5SummernoteWidget() in the SuggestionForm class in article/forms.py. The exact implementation details of these changes can be found by looking at the commit history of this project. 

## CSS3 Validation

The CSS3 files for the deployed website were tested using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

### ```style.css```

![style.css validation](/documentation/testing/html-css-js-validation/css-validation/style.png)

The validator returned two warnings before implementing the fixes. These warnings were resolved by removing the two vendor extension styles. 

### ```adming_comments.css```

![adming_comments.css validation](/documentation/testing/html-css-js-validation/css-validation/admin-comments.png)

The validator returned two warnings before implementing the fixes. These warnings were resolved by removing the two deprecated styles. 

## JavaScript Validation

The JavaScript files for the deployed website were tested using [JSHint](https://jshint.com/)

For validation purposes:

 - ```/* jshint esversion: 11 */``` was added to line in all JavaScript files

 - ```/* global bootstrap */``` was added to line 2 of JavaScript files containing Bootstrap components

 No errors were found during validation testing.

### admin_comments.js

![admin_comments.js validation](/documentation/testing/html-css-js-validation/js-validation/admin_comments.png)

### admin_posts.js

![admin_posts.js validation](/documentation/testing/html-css-js-validation/js-validation/admin_posts.png)

### comments.js

![comments.js validation](/documentation/testing/html-css-js-validation/js-validation/comments.png)

### my_posts.js

![my_posts.js validation](/documentation/testing/html-css-js-validation/js-validation/my_posts.png)

## Python Validation Testing (PEP8)

**Note:** the filename at the end of the urls in the screenshot didn't match with the names of the files being tested because the code for different files were being copied and pasted into the same validator in the same tab

### File: about/admin.py

![](/documentation/testing/python-validation/about/admin.png)

### File: about/apps.py

![](/documentation/testing/python-validation/about/apps.png)

### File: about/forms.py

![](/documentation/testing/python-validation/about/forms.png)

### File: about/models.py

![](/documentation/testing/python-validation/about/models.png)

### File: about/urls.py

![](/documentation/testing/python-validation/about/urls.png)

### File: about/views.py

![](/documentation/testing/python-validation/about/views.png)

### File: article/admin.py

![](/documentation/testing/python-validation/article/admin.png)

### File: article/apps.py

![](/documentation/testing/python-validation/article/apps.png)

### File: article/context_processors.py

![](/documentation/testing/python-validation/article/context-processors.png)

### File: article/forms.py

![](/documentation/testing/python-validation/article/forms.png)

### File: article/models.py

![](/documentation/testing/python-validation/article/models.png)

### File: article/urls.py

![](/documentation/testing/python-validation/article/urls.png)

### File: article/views.py

![](/documentation/testing/python-validation/article/views.png)

### File: boulderWiki/settings.py

![](/documentation/testing/python-validation/boulderWiki/settings.png)

### File: boulderWiki/urls.py

![](/documentation/testing/python-validation/boulderWiki/urls.png)

### File: manage.py

![](/documentation/testing/python-validation/manage.png)

## Responsiveness Testing

BoulderWiki was manually tested for responsiveness on all relevant device viewports using the Chrome dev tools. The viewports that were tested were: laptops and larger devices, tablets and mobiles. 

I've tested my deployed project to check for responsiveness issues and tested all pages that a user would visit.

On laptops and larger devices, the homepage adopts a three-column layout, while on tablets (in portrait mode) and mobiles the homepage adopts a single column layout. The single column layout makes the homepage easier to read on narrower screens. 

The screenshots for mobile were taken on my phone - a Samsung Galaxy S22 - this would be approximately 350 x 750 in the Chrome dev tools

The following viewport dimensions have been chosen for each device:

- Laptop - 1440 x 830
- Tablet - 750 x 830 
- Mobile - Samsung Galaxy S22

| Page | Mobile | Tablet | Laptops | Result |
| --- | --- | --- | --- | --- |
| Homepage | ![screenshot](/documentation/testing/responsiveness/mobile/homepage.jpg) | ![screenshot](/documentation/testing/responsiveness/tablets//homepage.png) | ![screenshot](/documentation/testing/responsiveness/laptops/homepage.png) | Works as expected |
| About  | ![screenshot](/documentation/testing/responsiveness/mobile/about.jpg) | ![screenshot](/documentation/testing/responsiveness/tablets/about.png) | ![screenshot](/documentation/testing/responsiveness/laptops/about.png) | Works as expected |
| Create Article | ![screenshot](/documentation/testing/responsiveness/mobile/create-article.jpg) | ![screenshot](/documentation/testing/responsiveness/tablets/create-article.png) | ![screenshot](/documentation/testing/responsiveness/laptops/create-article.png) | Works as expected |
| Manage Articles  | ![screenshot](/documentation/testing/responsiveness/mobile/manage-articles.jpg) | ![screenshot](/documentation/testing/responsiveness/tablets/manage-articles.png) | ![screenshot](/documentation/testing/responsiveness/laptops/manage-articles.png) | Works as expected |
| Categories | ![screenshot](/documentation/testing/responsiveness/mobile/categories.jpg) | ![screenshot](/documentation/testing/responsiveness/tablets/categories.png) | ![screenshot](/documentation/testing/responsiveness/laptops/categories.png) | Works as expected |
| Suggestions | ![screenshot](/documentation/testing/responsiveness/mobile/suggestions.jpg) | ![screenshot](/documentation/testing/responsiveness/tablets/suggestions.png) | ![screenshot](/documentation/testing/responsiveness/laptops/suggestions.png) | Works as expected |
| Article Details | ![screenshot](/documentation/testing/responsiveness/mobile/article-details.jpg) | ![screenshot](/documentation/testing/responsiveness/tablets/article-details.png) | ![screenshot](/documentation/testing/responsiveness/laptops/article-details.png) | Works as expected |
| Registration | ![screenshot](/documentation/testing/responsiveness/mobile/registration.jpg) | ![screenshot](/documentation/testing/responsiveness/tablets/registration.png) | ![screenshot](/documentation/testing/responsiveness/laptops/registration.png) | Works as expected |
| Login | ![screenshot](/documentation/testing/responsiveness/mobile/login.jpg) | ![screenshot](/documentation/testing/responsiveness/tablets/login.png) | ![screenshot](/documentation/testing/responsiveness/laptops/login.png) | Works as expected |

Overall, the website worked well on all devices. No layout issues were encountered, unwanted overflow or unwanted spacing was encountered during device responsiveness testing. 

## Cross-Browser Compatibility Testing


I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Microsoft Edge | Result |
| --- | --- | --- | --- | --- |
| Homepage | ![screenshot](/documentation/testing/cross-browser-compatibility/chrome/homepage.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/firefox/homepage.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/microsoft-edge/homepage.png) | Works as expected |
| Article Details | ![screenshot](/documentation/testing/cross-browser-compatibility/chrome/article-details.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/firefox/article-details.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/microsoft-edge/article-details.png) | Works as expected |
| About | ![screenshot](/documentation/testing/cross-browser-compatibility/chrome/about.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/firefox/about.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/microsoft-edge//about.png) | Works as expected |
| Create Article | ![screenshot](/documentation/testing/cross-browser-compatibility/chrome/create-article.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/firefox/create-article.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/microsoft-edge/create-article.png) | Works as expected |
| Manage Articles | ![screenshot](/documentation/testing/cross-browser-compatibility/chrome/manage-articles.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/firefox/manage-articles.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/microsoft-edge/manage-articles.png) | Works as expected |
| Categories | ![screenshot](/documentation/testing/cross-browser-compatibility/chrome/categories.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/firefox/categories.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/microsoft-edge/categories.png) | Works as expected |
| Suggestions | ![screenshot](/documentation/testing/cross-browser-compatibility/chrome/suggestions.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/firefox/suggestions.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/microsoft-edge/suggestions.png) | Works as expected |
| Login | ![screenshot](/documentation/testing/cross-browser-compatibility/chrome/login.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/firefox/login.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/microsoft-edge/login.png) | Works as expected |
| Registration | ![screenshot](/documentation/testing/cross-browser-compatibility/chrome/registration.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/firefox/registration.png) | ![screenshot](/documentation/testing/cross-browser-compatibility/microsoft-edge/registration.png) | Works as expected |

## Defensive Programming

Defensive programming measures were implemented into BoulderWiki to:
- Prevent non-superusers from having superuser privelages such as creating articles
- Protect sensitive data 
- Prevent destructive actions (such as deleting) from being done accidently
- Validate user input.

The criteria that was tested against can be seen below:

### Authentication and Security

Tests include:
- Does the application prevent users from trying to log in with incorrect credentials?
- Does the application prevent users from registering with a username that has already been taken?
- Does the application prevent users from registering with no password?
- Does the application prevent users from registering with weak passwords that are less than 8 characters and aren't alphanumeric?

### Access Control

Tests include:
- Access restrictions to pages only administrators should have access to
- Can non-superusers access the admin portal?
- Can non-superusers create articles?
- Can non-superusers mange articles?
- Can non-superusers create or delete categories?
- Can non-superusers delete other users suggestions?

- Can guest users create articles?
- Can guest users create categories?
- Can guest users leave comments?
- Can guest users make suggestions?

### Destructive Actions
- Does the application have a confirmation message that occurs when the user tries to delete a post?
- Does the application have a confirmation message that occurs when the user tries to delete a comment?
- Does the application have a confirmation message that occurs when the user tries to delete a suggestion?
- Does the application have a confirmation message that occurs when the user tries to delete a category?

### Form and Data Validation

Login
- Does the application prevent users from leaving "Username" field blank?
- Does the application prevent users from leaving "Password" field blank?

Registration:
- Does the application prevent users from leaving the "Username" field blank?
- Does the application prevent users from inputting invalid data into the "Email" field?

Comments and Suggestions
- Can users submit blank comments?
- Can users submit blank suggestions?

Creating Articles
- Can users leave the title field blank?
- Can users leave the slug field blank?
- Can users leave the content field blank?
- Can users leave the excerpt field blank?

---

### Logging In With Incorrect Credentials

![](/documentation/testing/defensive-programming/authentication-and-security/incorrect-credentials.png)

When the user tries to login with incorrect credentials, they are greeted with a warning message above the "Username" field

### Registering With An Existing Username

![](/documentation/testing/defensive-programming/authentication-and-security/existing-username.png)

If the user tries registering with a username that another user has already chosen, the user will be greeted with a warning message instructing them to "choose a different username".

### Registering With No Password

![](/documentation/testing/defensive-programming/authentication-and-security/no-password.png)

A user is unable to register with no password because the "Password" field has been given a "required" attribute. 

### Registering With Weak Passwords

![](/documentation/testing/defensive-programming/authentication-and-security/weak-passwords.png)

If the user tries registering with a weak password that does not meet the minimum criteria for password, they will be given some warning messages that tells them the password criteria that has not been met

---

###  Restricting Access To Administrator Exclusive Pages

![](/documentation/testing/defensive-programming/access-control/restricting-access.png)

A non-superuser is unable to access administrator-exclusive pages such as: 
- "Create Article"
- "Manage Articles"
- "Categories". 

This is because the links to these pages don't appear in the navbar for them. 

Also, if a non-superuser tries accessing these pages by appending them to the URL (in the URL bar of the browser), they will be led to an error page as shown in the screenshot below:

![](/documentation/testing/defensive-programming/access-control/error-page.png)

Since a non-superuser is unable to access the pages outlined above, they are unable to:
- Create articles
- Manage articles by editing or deleting them
- Add (or delete) categories

 If a non-superuser is unable to perform these tasks, then this automatically means a guest user also cannot.

### Restricting Non-Superusers From Editing or Deleting Other Users Suggestions

![](/documentation/testing/defensive-programming/access-control/deleting-suggestions.png)

From the screenshot above, you can see that a non-superuser can only see the suggestions that they've made. This means that they have no way of deleting or editing suggestions made by other users. 

### Restricting Access To the Django Admin Portal

If a non-superuser tries to access the Django admin portal by appending ```/admin``` to the end of the URL (in the browser URL bar), they are led to the page in the screenshot below:

![](/documentation/testing/defensive-programming/access-control/accessing-django-admin.png)

### Leaving Comments and Making Suggestions As A Guest User

![](/documentation/testing/defensive-programming/access-control/guest-user-comments.png)

When you are browsing as a guest user, there is no button to write a comment and the suggestions panel does not appear. Therefore, a guest user is unable to leave any comments on a post or make any suggestions. 

---

When the user performs the destructive actions outlined below, they get a confirmation prompt before proceeding.

### Deleting A Post

![](/documentation/testing/defensive-programming/destructive-actions/delete-post-confirmation.png)

### Deleting A Comment

![](/documentation/testing/defensive-programming/destructive-actions/delete-comment-confirmation.png)

### Deleting A Suggestion

![](/documentation/testing/defensive-programming/destructive-actions/delete-suggestion-confirmation.png)

### Deleting A Category

![](/documentation/testing/defensive-programming/destructive-actions/delete-category-confirmation.png)

---

### Login

![](/documentation/testing/defensive-programming/form-and-data-validation/blank-username-field.png)

When the user tries to leave the "Username" field blank, they get a warning message. 

![](/documentation/testing/defensive-programming/form-and-data-validation/blank-password-field.png)

When the user tries to leave the "Password" field blank, they get a warning message. 

### Registration

![](/documentation/testing/defensive-programming/form-and-data-validation/sign-up-blank-username-field.png)

When the user tries to leave the "Username" field blank, they get a warning message. 

![](/documentation/testing/defensive-programming/form-and-data-validation/invalid-email-input.png)

When the user tries to enter invalid data into the "Email" field, they get a warning message. 

### Submitting Blank Comments

![](/documentation/testing/defensive-programming/form-and-data-validation/submitting-blank-comments.png)

When the user tries to submit a blank comment, they get a warning message.

### Submitting Blank Suggestions

![](/documentation/testing/defensive-programming/form-and-data-validation/submitting-blank-suggestions.png)

When the user tries to submit a blank suggestion, they get a Bootstrap alert message.

### Creating Articles

- Can users leave the title field blank?
- Can users leave the slug field blank?
- Can users leave the content field blank?

![](/documentation/testing/defensive-programming/form-and-data-validation/creating-articles/blank-title.png)

If the user tries to leave the title field blank, they get a warning message.

![](/documentation/testing/defensive-programming/form-and-data-validation/creating-articles/blank-slug.png)

If the user tries to leave the slug field blank, they get a warning message.

![](/documentation/testing/defensive-programming/form-and-data-validation/blank-content.png)

If the user tries to leave the content field blank, they get a warning message.

---

## User Story Testing

### US-01 — View the Homepage (Should Have)

**User Story**

As a visitor, I want to view the homepage so that I can understand what BoulderingWiki is and begin exploring bouldering content.

Test:
- The homepage should be presented to the user when they load up the site

Expected Result:
- The homepage and everything on it should be clearly visible to all users

The screenshot below shows how the homepage looks for guests, registered users (non-superusers) and administrators (superusers)

![](/documentation/testing/user-story-testing/us-01.png)

Actual Result: Same as expected


**Overall Result/Outcome: PASS**

### US-02 — Navigate the Website (Should Have)

**User Story**

As a visitor, I want consistent navigation so that I can move between the main areas of the website easily.

Test:
- The user should be able to:
    - Get around the site with ease using the navbar
    - Switch between pages in the article directory

Expected Result: 
- There should be be plenty of navigational elements in place for users to use to browse the site, including, a navbar and pagination elements

The screenshot below shows the pages that a user is able to access. Across each page, the user has access to a navbar that stays fixed in place at the top of the page. This allows users to get around the site with ease. 

Furthermore, the user can navigate between paginated article lists on the homepage using pagination elements that stay fixed at the bottom of the page. 

|  |  |  |
| :---         |     :---:      |          ---: |
| ![](/documentation/testing/responsiveness/laptops/homepage.png)   | ![](/documentation/testing/responsiveness/laptops/about.png)    | ![](/documentation/testing/responsiveness/laptops/create-article.png)|
| ![](/documentation/testing/responsiveness/laptops/manage-articles.png)| ![](/documentation/testing/responsiveness/laptops/categories.png) | ![](/documentation/testing/responsiveness/laptops/suggestions.png) |
| ![](/documentation/testing/responsiveness/laptops/article-details.png) | ![](/documentation/testing/responsiveness/laptops/login.png) | ![](/documentation/testing/responsiveness/laptops/registration.png) |

Actual Result: 
- Same as expected

**Overall Result/Outcome: PASS**

### US-03 — View the Article Directory (Must Have) 

**User Story**

As a visitor, I want to view a list of bouldering articles so that I can discover available content. 

Test: 
- Can the user browse a list of articles in the article directory?

Expected: 
- The user should be able to clearly see a list of articles

![](/documentation/testing/user-story-testing/us-03.png)  

Actual result: 
- The user is able to view a list of articles on the homepage which are paginated in groups of 6 across multiple pages
- To navigate between pages to view articles, the user can use the pagination components at the bottom of the page
- The user can also search for articles using the search bar and/or filter articles by category

**Overall Result/Outcome: PASS**

### US-04 — Read an Article (Must Have)

**User Story**

As a visitor, I want to read a bouldering article so that I can learn about a particular topic.

**Acceptance Criteria**

Test: 
- Can a user read an articles title and content?

Expected result: 
- A user should be able to click on an article in the article directory and read its contents

The screenshot below shows an example of a page that the user is directed to when they click on an article. On this page, the user can see the contents of an article. 

![](/documentation/testing/responsiveness/laptops/article-details.png)

Actual Result: 
- Same as expected

**Overall Result/Outcome: PASS**

### US-05 — Browse Categories (Should Have)

**User Story**

As a visitor, I want to browse bouldering categories so that I can explore articles by subject.

Test:
- Can a user sort articles by categories?

Expected Result:
- A user should be able to sort articles on the page by certain categories that have been created by superusers

In the screenshot below, you can see that the homepage has a "filter by category" field that brings up a drop-down menu containing a list of categories to choose from.

![](/documentation/testing/user-story-testing/us-03.png) 

Actual Result:
- The user is able to view a list of categories available in a drop-down menu and filter articles by categories so that only articles of the selected category appear on the page

**Overall Result/Outcome: PASS**

### Epic 3 — Search

### US-06 — Search for Articles (Could Have)

**User Story**

As a visitor, I want to search for articles so that I can quickly find information about a particular bouldering topic.

Test:
- Can the user search for specific content using a search bar?

Expected Result:
- The user should be able to use a search bar on the homepage to search for specific article content
- The search bar should be able to read articles for specified keywords in the title, content, excerpt and categories - not just the title

The screenshots below show some example searches:

| Search: kilter | Search: outdoor | Search: hangboard |
| :---:         |     :---:      |          :---: |
| ![](/documentation/testing/user-story-testing/search-kilter.png)   | ![](/documentation/testing/user-story-testing/search-outdoor.png)    | ![](/documentation/testing/user-story-testing/search-hangboard.png)    |

Actual Result:
- When the user uses the search bar, it filters the article directory to only show the posts that contain the specified keyword
- The search bar looks at the post title, post content, categories, and excerpt content

**Overall Result/Outcome: PASS**

### US-07 — Register for an Account (Must Have)

**User Story**

As a visitor, I want to create an account so that I can suggest improvements to articles.

Test:
- Can the user register to create an account?

Expected Result:
- A guest user should be able to register for an account

The screenshots below show an example of an account registration. 

| Registration | Homepage and alert |
| :---:         |     :---:      | 
| ![](/documentation/testing/user-story-testing/registration-details.png)   | ![](/documentation/testing/user-story-testing/resgistration-success-alert.png) | 

Actual Result:
- A guest user is able to sign up and create an account on the "Registration" page
- Here they can enter the username and password they want to use
- After submitting the relevant information, the user is directed to the homepage and greeted with an alert saying "Successfully signed in as [username]"

**Overall Result/Outcome: PASS**

### US-08 — Log In (Must Have)

**User Story**

As a registered user, I want to log in so that I can access contribution functionality.

Test: 
- Can the user login after creating an account?

Expected Result:
- The user should be able to login after creating an account in the registration page

The screenshots below shows an example of a user logging in from the login page. 

| Registration | Homepage and alert |
| :---:         |     :---:      | 
| ![](/documentation/testing/user-story-testing/sign-in-page.png) | ![](/documentation/testing/user-story-testing/sign-in-alert.png) | 

Actual Result:
- As you can see from the test of US-07 the user is automatically logged in when they create an account and are directed to the homepage
- If the user logs out, they have to log back in again on the login page
- When the user logs in from the login page, they are directed to the homepage recieve an alert saying "Successfully signed in as [username]"

**Overall Result/Outcome: PASS**

### US-09 — Log Out (Must Have)

**User Story**

As a logged-in user, I want to log out so that I can securely end my session.

Test:
- The user should be able to log out of their account

Expected:
- The user should have the option to log out of their account and be returned to the homepage when succesfully logged out

| Sign-Out Page | Homepage and logout alert |
| :---:         |     :---:      | 
| ![](/documentation/testing/user-story-testing/sign-out.png) | ![](/documentation/testing/user-story-testing/sign-out-alert.png) | 

Actual Result:
- When the user clicks the logout button in the navbar, they are redirected to the confirmation page shown in the left screenshot above
- Then when they click the "Sign Out" button on this page, they are redirected to the homepage and recieve an alert saying "You have signed out"

**Overall Result/Outcome: PASS**

### US-10 — Suggest a Change to an Article (Must Have)

**User Story**

As a registered user, I want to suggest changes to an article so that I can help improve BoulderingWiki.

Test:
- Can the user make suggestions to articles?

Expected result:
- The user should be able to click on an article, read the article, make a suggestion for improvement, then submit the suggestion for administrators to review

| Suggestion Form | Suggestion Alert | Admin Suggestion Page |
| :---:         |     :---:      |          :---: |
| ![](/documentation/testing/user-story-testing/suggestion-panel.png)  | ![](/documentation/testing/user-story-testing/suggestion-submission.png) | ![](/documentation/testing/user-story-testing/suggestion-in-admin-page.png) |

Actual Result:
- When the user scrolls down to the bottom of an article, they can find a suggestion panel where they suggestion what improvements can be made to the articles content
- When the user submits the suggestion they get an alert message saying "Your suggestion has been submitted for review!"
- When submitted, the suggestion appears in the "Suggestions" page for administrators to review

**Overall Result/Outcome: PASS**

### US-11 — Prevent Guests from Submitting Suggestions (Must Have)

**User Story**

As the site owner, I want guests prevented from suggesting edits so that contributions can be linked to authenticated accounts.

Test:
- Can guest user submit suggestions?

Expected Result:
- As a guest user, there should be no way to submit suggestions

The screenshot below shows that the suggestions panel does not appear as a guest user.

![](/documentation/testing/user-story-testing/no-guest-user-suggestions.png)

Actual Result:
- The suggestions panel does not appear unless you're logged in as a registered user so guest users have no way of submitting suggestions

**Overall Result/Outcome: PASS**

### US-12 — Access Django Admin (Must Have)

**User Story**

As an administrator, I want to access the Django Admin so that I can manage BoulderingWiki content.

Test:
- Can the user access the Django Admin portal?

Expected Result:
- A superuser should be able to access the Django Admin portal by appending "/admin" to the end of the URL in the browsers URL bar from the homepage

| Logged In As Superuser | Appending "/admin" To URL | Admin Portal Redirect |
| :---:         |     :---:      |          :---: |
| ![](/documentation/testing/user-story-testing/logged-in-as-superuser.png)  | ![](/documentation/testing/user-story-testing/appending-admin.png) | ![](/documentation/testing/user-story-testing/admin-portal.png) |

Actual Result:
- A user needs to be an administrator (superuser) to access the Django Admin portal
- A superuser can append "/admin" to the URL in the URL bar to access the Django Admin portal
- When the user clicks enter, they are redirected to the Django Admin portal as shown in the right screenshot above

**Overall Result/Outcome: PASS**

### US-13 — View Pending Suggestions (Must Have)

**User Story**

As an administrator, I want to view pending suggestions so that I can review community contributions.

Test:
- Can an administrator view a list of suggestions?

Expected Result:
- An administrator should be able to view a list of pending suggestions either in the Django Admin portal or on an administrator-exclusive page on the website

The screenshot below shows an administrator-exclusive page where a list of suggestions can be viewed. 

![](/documentation/testing/user-story-testing/suggestion-in-admin-page.png)

Actual Result:
- An administrator is able to view a list of suggestions on a "Suggestions" page which only they can access
- On this page suggestions are sorted into two tables - one for the users own suggestions and one for other users suggestions

**Overall Result/Outcome: PASS**

### US-14 — Approve or Reject a Suggestion (Must Have)

**User Story**

As an administrator, I want to approve or reject suggested edits so that only reviewed changes affect published articles.

Test:
- Can a superuser approve or reject suggestions?

Expected Result:
- A superuser should be able to approve or reject suggestions either in the Django Admin portal or on an administrator-exclusive page on the website

| Suggestions Page | Suggestion Approval Alert | Suggestion Rejection Alert |
| :---:         |     :---:      |          :---: |
| ![](/documentation/testing/user-story-testing/suggestions-page.png)  | ![](/documentation/testing/user-story-testing/suggestion-approval-alert.png) | ![](/documentation/testing/user-story-testing/suggestion-rejection-alert.png) |

Actual Result:
- On the "Suggestions" page, an administrator has the option to reject or approve suggestions by clicking "Approve" or "Reject" buttons in the last column of the table
- When an administrator approves a suggestion, the content of the corresponding post gets updated and overwritten by the user-suggested content and an alert message appears saying "Suggestion approved applied to the post"
- An alert message appears when an administrator rejects a suggestion saying "Suggestion rejected"

**Overall Result/Outcome: PASS**

### US-15 — Manage Articles and Categories (Should Have)

**User Story**

As an administrator, I want to create, update, and delete articles and categories so that I can maintain the website's content.

Test:
- Can an administrator create, update and/or delete articles?
- Can an administrator create, update and/or delete categories?

Expected Result:
- A superuser should be able to create, update and/or delete articles?
- A superuser should be able to create, update and/or delete categories?

The 