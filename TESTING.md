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

