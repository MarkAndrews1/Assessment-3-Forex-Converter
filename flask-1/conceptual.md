### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  * Python helps the back-end process while JavaScript is more front-end.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
   * The **get()** method and the **try-except** method.

- What is a unit test?
  * A unit test generally test **individual** components.

- What is an integration test?
  * A integration test will test to see if the components are working well together.

- What is the role of web application framework, like Flask?
  * A web framework provides tools to help a developer interact with a database or server.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  * Depends on context concerning API capabilities, readability, and SEO considerations.

- How do you collect data from a URL placeholder parameter using Flask?
  * By passing it into a function as a parameter.

- How do you collect data from the query string using Flask?
  * **request.args['_query-str_']**

- How do you collect data from the body of the request using Flask?
  * **request.form.get('_request_')**

- What is a cookie and what kinds of things are they commonly used for?
   * Cookies are **name/string-value pair** stored by the **client**. They are commonly used to store user info such as number of times the user has visted the page, username, settings, and what their name is.

- What is the session object in Flask?
  * Session stores infomation as long as the page isn't closed or the browser.

- What does Flask's `jsonify()` do?
  * Returns the given data in a object containing a JSON representation.
