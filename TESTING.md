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

The deployed BoulderWiki website was tested using the [W3C HTML Validator](https://validator.w3.org/) 