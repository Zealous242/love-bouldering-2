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

### file: about/admin.py

![](/documentation/testing/python-validation/about/admin.png)

### file: about/apps.py

![](/documentation/testing/python-validation/about/apps.png)

### file: about/forms.py

![](/documentation/testing/python-validation/about/forms.png)

### file: about/models.py

![](/documentation/testing/python-validation/about/models.png)

### file: about/urls.py

![](/documentation/testing/python-validation/about/urls.png)

### file: about/views.py

![](/documentation/testing/python-validation/about/views.png)



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

